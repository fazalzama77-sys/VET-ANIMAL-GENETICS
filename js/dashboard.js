/* ============================================================
   dashboard.js — Learning Analytics & Exam Readiness Engine
   ============================================================
     - 0–1000 XP Animal Genetics Mastery Index with circular gauge
     - Next-best-action prescriptions that react to real gaps
     - Dual VCI board exam readiness (Paper I vs Paper II),
       derived from the syllabus rather than hard-coded
     - Performance trend across recent papers + lifetime accuracy
       by question format and difficulty tier
     - Weakest sub-sections, named and linked
     - Interactive unit mastery matrix with real filter tabs
     - 5-box Leitner spaced repetition memory pipeline
     - 84-day activity heatmap with correct month headings
     - Assessment ledger linking straight into each paper's
       full analysis (#/quiz/attempt/<id>)
     - Knowledge vault (highlights, notes, bookmarks, Q&A)
   ============================================================ */

var dashboardApp = (function () {

  var activeFilter = "all";

  var EMPTY_TOTALS = {
    runs: 0, total: 0, correct: 0, attempted: 0, skipped: 0, seconds: 0,
    byFormat: { mcq: { total: 0, right: 0 }, tf: { total: 0, right: 0 }, fib: { total: 0, right: 0 } },
    byDiff: { 1: { total: 0, right: 0 }, 2: { total: 0, right: 0 }, 3: { total: 0, right: 0 } }
  };

  function render(host) {
    if (!host) return;

    var readMap    = store.getRead() || {};
    var quiz       = store.getQuiz() || { attempts: [], byUnit: {}, bySub: {} };
    var streak     = store.computeStreak() || { current: 0, longest: 0, totalDays: 0 };
    var activity   = store.getActivity() || {};
    var srs        = store.getSrs() || {};
    var dueCards   = (store.dueSrs && store.dueSrs()) ? store.dueSrs().length : 0;
    var notes      = store.getNotes() || {};
    var bms        = store.getBookmarks() || [];
    var highlights = store.getHighlights() || {};
    var qaDone     = store.getQaDone() || [];

    // Syllabus counts
    var theoryUnits    = syllabus.theory || [];
    var practicalUnits = syllabus.practical || [];
    var allUnits       = theoryUnits.concat(practicalUnits);
    var totalTopics    = allUnits.reduce(function (n, u) { return n + (u.topics ? u.topics.length : 0); }, 0);
    var readCount      = countReadTopics(allUnits, readMap);
    var readPct        = totalTopics ? Math.round((readCount / totalTopics) * 100) : 0;

    // Quiz statistics
    var attempts = quiz.attempts || [];
    var totals   = store.quizTotals ? store.quizTotals() : EMPTY_TOTALS;
    var totalQ = totals.total, totalCorrect = totals.correct;
    var quizAccuracy = totalQ ? Math.round((totalCorrect / totalQ) * 100) : 0;

    // Spaced repetition statistics
    var srsKeys = Object.keys(srs);
    var boxCounts = [0, 0, 0, 0, 0];
    var dueByBox = [0, 0, 0, 0, 0];
    var now = Date.now();
    srsKeys.forEach(function (k) {
      var b = Math.min(5, Math.max(1, srs[k].box || 1));
      boxCounts[b - 1]++;
      if ((srs[k].due || 0) <= now) dueByBox[b - 1]++;
    });
    var masteredCount = boxCounts[2] + boxCounts[3] + boxCounts[4]; // Box 3, 4, 5
    var retentionRate = srsKeys.length ? Math.round((masteredCount / srsKeys.length) * 100) : 0;

    // Highlights stats
    var totalHighlights = 0;
    var hlColorCounts = { yellow: 0, green: 0, blue: 0, pink: 0, orange: 0, purple: 0 };
    Object.keys(highlights).forEach(function (topId) {
      var arr = highlights[topId] || [];
      totalHighlights += arr.length;
      arr.forEach(function (h) {
        if (h && h.color && hlColorCounts[h.color] !== undefined) hlColorCounts[h.color]++;
      });
    });

    // Mastery XP Calculation (0 to 1000 XP)
    var readXP = Math.round((readCount / (totalTopics || 1)) * 400);          // 40% weight
    var quizFactor = totalQ ? (totalCorrect / totalQ) : 0;
    var quizVolume = Math.min(1, attempts.length / 8);
    var quizXP = Math.round((quizFactor * 0.7 + quizVolume * 0.3) * 350);     // 35% weight
    var srsFactor = srsKeys.length ? (masteredCount / srsKeys.length) : 0;
    var srsVolume = Math.min(1, srsKeys.length / 25);
    var srsXP = Math.round((srsFactor * 0.6 + srsVolume * 0.4) * 150);        // 15% weight
    var streakFactor = Math.min(1, streak.current / 7);
    var daysFactor = Math.min(1, streak.totalDays / 10);
    var consistencyXP = Math.round((streakFactor * 0.6 + daysFactor * 0.4) * 100); // 10% weight

    var totalXP = Math.min(1000, readXP + quizXP + srsXP + consistencyXP);
    var readinessPct = Math.min(100, Math.round(totalXP / 10));
    var rank = getRank(totalXP);

    // Circumference for the 175px gauge (radius = 70)
    var radius = 70;
    var circumference = 2 * Math.PI * radius;
    var strokeOffset = circumference - (circumference * readinessPct) / 100;

    host.innerHTML =
      '<div class="dash-elite">' +

        /* 1. Hero cockpit */
        '<div class="dash-hero">' +
          '<div class="dash-cockpit">' +
            '<div class="mastery-gauge-wrap">' +
              '<div class="mastery-svg-gauge">' +
                '<svg viewBox="0 0 175 175">' +
                  '<circle class="mastery-gauge-bg" cx="87.5" cy="87.5" r="' + radius + '"></circle>' +
                  '<circle class="mastery-gauge-fill" cx="87.5" cy="87.5" r="' + radius + '" ' +
                    'stroke-dasharray="' + circumference + '" ' +
                    'stroke-dashoffset="' + strokeOffset + '"></circle>' +
                '</svg>' +
                '<div class="mastery-gauge-center">' +
                  '<span class="mastery-gauge-val">' + totalXP + '</span>' +
                  '<span class="mastery-gauge-lbl">Mastery XP</span>' +
                '</div>' +
              '</div>' +
              '<div class="mastery-rank-badge">' + app.icon(rank.icon) + ' ' + rank.title + '</div>' +
              '<div class="xp-split" title="How your Mastery XP was earned">' +
                xpChip("Reading", readXP, 400) +
                xpChip("Quizzes", quizXP, 350) +
                xpChip("Memory", srsXP, 150) +
                xpChip("Consistency", consistencyXP, 100) +
              '</div>' +
            '</div>' +

            '<div class="dash-cockpit-info">' +
              '<span class="dash-eyebrow">' + app.icon("sparkle") + ' Learning cockpit · ' + rank.stage + '</span>' +
              '<h1 class="dash-title">Animal Genetics Analytics</h1>' +
              '<p class="dash-lede">' +
                'Exam readiness, retention health and syllabus coverage across all three VCI theory units and three practical units.' +
              '</p>' +

              '<div class="dash-metrics-grid">' +
                '<div class="dash-metric-card">' +
                  '<div class="dash-metric-head">Streak <span class="streak-flame">' + app.icon("flame") + '</span></div>' +
                  '<div class="dash-metric-val">' + streak.current + ' <small style="font-size:14px;font-weight:600">days</small></div>' +
                  '<div class="dash-metric-sub">Best: ' + streak.longest + ' days</div>' +
                '</div>' +

                '<div class="dash-metric-card">' +
                  '<div class="dash-metric-head">Syllabus <span>' + app.icon("book") + '</span></div>' +
                  '<div class="dash-metric-val">' + readPct + '%</div>' +
                  '<div class="dash-metric-sub">' + readCount + ' of ' + totalTopics + ' topics read</div>' +
                '</div>' +

                '<div class="dash-metric-card">' +
                  '<div class="dash-metric-head">Quiz accuracy <span>' + app.icon("target") + '</span></div>' +
                  '<div class="dash-metric-val">' + (totalQ ? quizAccuracy + '%' : '—') + '</div>' +
                  '<div class="dash-metric-sub">' + (totalQ
                      ? totalCorrect + ' of ' + totalQ + ' over ' + attempts.length + ' paper' + (attempts.length === 1 ? '' : 's')
                      : 'No papers taken yet') + '</div>' +
                '</div>' +

                '<div class="dash-metric-card">' +
                  '<div class="dash-metric-head">Memory health <span>' + app.icon("shield") + '</span></div>' +
                  '<div class="dash-metric-val">' + (srsKeys.length ? retentionRate + '%' : '—') + '</div>' +
                  '<div class="dash-metric-sub">' + (srsKeys.length
                      ? (dueCards ? dueCards + ' due for review' : 'Nothing due today')
                      : 'Answer a quiz to build the queue') + '</div>' +
                '</div>' +
              '</div>' +
            '</div>' +
          '</div>' +
        '</div>' +

        /* 2. Next best actions */
        renderPrescriptions(dueCards, allUnits, readMap, quiz, totalTopics, readCount) +

        /* 3. Paper I vs Paper II readiness */
        renderPaperReadiness(readMap, quiz) +

        /* 4. Performance trend + lifetime accuracy */
        renderTrendSection(attempts, totals) +

        /* 5. Weakest sub-sections */
        renderWeakSubsections(quiz) +

        /* 6. Unit mastery matrix */
        '<section>' +
          '<div class="row row--between mb-3">' +
            '<div>' +
              '<h2>Unit mastery matrix</h2>' +
              '<p class="muted small mt-1">Reading progress, question bank volume and best score per curriculum unit.</p>' +
            '</div>' +
          '</div>' +
          renderMatrixFilters(allUnits, quiz) +
          '<div id="unit-matrix-container">' +
            renderUnitMatrix(activeFilter, allUnits, readMap, quiz) +
          '</div>' +
        '</section>' +

        /* 7. Leitner pipeline */
        renderLeitnerPipeline(boxCounts, dueByBox, srsKeys.length, dueCards) +

        /* 8. Heatmap + assessment ledger */
        '<div class="grid grid--2">' +
          renderHeatmapCard(activity, streak) +
          renderRecentAttemptsCard(quiz) +
        '</div>' +

        /* 9. Knowledge vault */
        renderKnowledgeVault(totalHighlights, hlColorCounts, Object.keys(notes).length, bms.length, qaDone.length) +

      '</div>';

    attachDashboardEvents(host, allUnits, readMap, quiz);
  }

  /* ---------- helpers shared by several panels ---------- */

  /* Only count read marks that still belong to a topic in the syllabus —
     an edited syllabus used to leave orphan marks inflating coverage. */
  function countReadTopics(units, readMap) {
    var n = 0;
    units.forEach(function (u) {
      (u.topics || []).forEach(function (t) { if (readMap[t.id]) n++; });
    });
    return n;
  }

  function xpChip(label, got, max) {
    var p = max ? Math.round(got / max * 100) : 0;
    return '<span class="xp-chip" title="' + label + ': ' + got + ' of ' + max + ' XP">' +
      '<i style="width:' + p + '%"></i><b>' + label + '</b><span>' + got + '</span></span>';
  }

  function scoreChip(p) {
    return p >= 85 ? "chip--ok" : p >= 70 ? "chip--accent" : p >= 50 ? "chip--warn" : "chip--danger";
  }

  function barTone(p) {
    return p >= 75 ? "is-ok" : p >= 50 ? "is-warn" : "is-bad";
  }

  /* Which paper does a unit sit in? Theory units come from the syllabus
     definition; a practical unit follows the theory unit of the same number. */
  function paperOfUnit(unitId) {
    var no = (syllabus.unitById[unitId] || {}).no;
    var papers = (syllabus.meta && syllabus.meta.papers) || [];
    for (var i = 0; i < papers.length; i++) {
      if ((papers[i].units || []).indexOf(no) !== -1) return papers[i];
    }
    return null;
  }

  function unitsOfPaper(paperId) {
    return (syllabus.allUnits || []).filter(function (u) {
      var p = paperOfUnit(u.id);
      return p && p.id === paperId;
    });
  }

  /* ---------- Rank calculation ---------- */
  function getRank(xp) {
    if (xp >= 750) return { title: "Master Animal Geneticist", stage: "Phase 4 · Elite population genomics & sire selection", icon: "trophy" };
    if (xp >= 500) return { title: "Senior Animal Breeder", stage: "Phase 3 · Board exam ready", icon: "sparkle" };
    if (xp >= 250) return { title: "Junior Biostatistician", stage: "Phase 2 · Experimental design & genetic metrics", icon: "search" };
    return { title: "Genetics Apprentice", stage: "Phase 1 · Foundations", icon: "book" };
  }

  /* ---------- Smart action prescriptions ---------- */
  function renderPrescriptions(dueCards, allUnits, readMap, quiz, totalTopics, readCount) {
    var srsCard;
    if (dueCards > 0) {
      srsCard =
        '<div class="presc-card is-urgent">' +
          '<div>' +
            '<span class="presc-badge presc-badge--urgent">' + app.icon("clock") + ' Priority 1 · Memory decay</span>' +
            '<h3 class="presc-title mt-2">' + dueCards + ' question' + (dueCards > 1 ? 's' : '') + ' due today</h3>' +
            '<p class="presc-desc mt-1">The forgetting curve is active on these. Clear the Leitner queue now to hold what you already learned.</p>' +
          '</div>' +
          '<a class="btn btn--primary presc-btn" href="#/quiz/review">' + app.icon("repeat") + ' Clear review queue</a>' +
        '</div>';
    } else {
      srsCard =
        '<div class="presc-card">' +
          '<div>' +
            '<span class="presc-badge presc-badge--success">' + app.icon("check") + ' Memory safe</span>' +
            '<h3 class="presc-title mt-2">Nothing due for review</h3>' +
            '<p class="presc-desc mt-1">Your spaced repetition queue is clear. Everything answered is still in consolidation.</p>' +
          '</div>' +
          '<a class="btn btn--outline presc-btn" href="#/quiz">' + app.icon("quiz") + ' Practise questions</a>' +
        '</div>';
    }

    var nextTopic = findNextUnreadTopic(allUnits, readMap);
    var lessonCard;
    if (nextTopic) {
      lessonCard =
        '<div class="presc-card is-primary">' +
          '<div>' +
            '<span class="presc-badge presc-badge--primary">' + app.icon("book") + ' Next up in the syllabus</span>' +
            '<h3 class="presc-title mt-2">' + app.esc(shorten(nextTopic.title, 34)) + '</h3>' +
            '<p class="presc-desc mt-1">' + app.esc(nextTopic.unitTitle) + ' · topic ' + nextTopic.index +
              ' · ' + (totalTopics - readCount) + ' topics left</p>' +
          '</div>' +
          '<a class="btn btn--primary presc-btn" href="#/topic/' + nextTopic.id + '">' + app.icon("book") + ' Continue lesson</a>' +
        '</div>';
    } else {
      lessonCard =
        '<div class="presc-card">' +
          '<div>' +
            '<span class="presc-badge presc-badge--success">' + app.icon("trophy") + ' Full coverage</span>' +
            '<h3 class="presc-title mt-2">All ' + totalTopics + ' topics read</h3>' +
            '<p class="presc-desc mt-1">You have opened every theory and practical topic in the syllabus.</p>' +
          '</div>' +
          '<a class="btn btn--outline presc-btn" href="#/theory">' + app.icon("repeat") + ' Review lessons</a>' +
        '</div>';
    }

    var weakUnit = findWeakestUnit(allUnits, quiz);
    var quizCard =
      '<div class="presc-card">' +
        '<div>' +
          '<span class="presc-badge presc-badge--primary">' + app.icon("target") + ' Target diagnostic</span>' +
          '<h3 class="presc-title mt-2">' + app.esc(shorten(weakUnit.name, 34)) + '</h3>' +
          '<p class="presc-desc mt-1">' + (weakUnit.hasScore
            ? 'Your weakest tested unit — best score ' + weakUnit.score + '%. A focused test will move it.'
            : 'Never tested. Sit a short paper to find out where you actually stand.') + '</p>' +
        '</div>' +
        '<a class="btn btn--primary presc-btn" href="#/quiz/unit/' + weakUnit.id + '">' + app.icon("quiz") + ' Test knowledge</a>' +
      '</div>';

    return '<div class="dash-prescriptions">' + srsCard + lessonCard + quizCard + '</div>';
  }

  /* ---------- Paper I vs Paper II comparative readiness ---------- */
  function renderPaperReadiness(readMap, quiz) {
    var papers = (syllabus.meta && syllabus.meta.papers) || [];
    if (!papers.length) return "";

    function computePaper(p) {
      var units = unitsOfPaper(p.id);
      var totalT = 0, readT = 0, totalQuestions = 0;
      var scores = [];

      units.forEach(function (u) {
        var uTopics = u.topics || [];
        totalT += uTopics.length;
        uTopics.forEach(function (t) { if (readMap[t.id]) readT++; });
        totalQuestions += app.questionCount(u.id);
        var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
        if (rec && typeof rec.best === "number") scores.push(rec.best);
      });

      var readPercent = totalT ? Math.round((readT / totalT) * 100) : 0;
      var avgScore = scores.length
        ? Math.round(scores.reduce(function (a, b) { return a + b; }, 0) / scores.length) : 0;

      // A blunt but honest readiness number: half coverage, half performance,
      // and untested units drag it down because they genuinely are a risk.
      var perf = units.length ? Math.round(
        units.reduce(function (n, u) {
          var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
          return n + ((rec && typeof rec.best === "number") ? rec.best : 0);
        }, 0) / units.length) : 0;
      var readiness = Math.round(readPercent * 0.45 + perf * 0.55);

      return {
        id: p.id,
        label: p.name || p.id,
        name: paperTitle(p.id),
        unitLabel: (p.units.length === 1 ? "Unit " : "Units ") + p.units.join(", ") + " (theory + practical)",
        totalTopics: totalT, readTopics: readT, readPct: readPercent,
        totalQuestions: totalQuestions, avgScore: avgScore,
        testCount: scores.length, unitCount: units.length,
        untested: units.length - scores.length,
        readiness: readiness
      };
    }

    function paperTitle(id) {
      return id === "paper-1"
        ? "Biostatistics & Animal/Population Genetics"
        : id === "paper-2" ? "Principles of Animal Breeding" : "Examination Paper";
    }

    function renderPaperCard(p) {
      return '<div class="paper-gauge-card">' +
        '<div class="paper-card-head">' +
          '<div>' +
            '<span class="paper-badge">' + app.esc(p.label) + '</span>' +
            '<h3 class="paper-card-title mt-1">' + app.esc(p.name) + '</h3>' +
            '<p class="paper-card-subtitle">' + app.esc(p.unitLabel) + '</p>' +
          '</div>' +
          '<span class="chip ' + scoreChip(p.readiness) + ' font-bold">' + p.readiness + '% ready</span>' +
        '</div>' +

        '<div class="paper-progress-wrap">' +
          '<div class="row row--between small">' +
            '<span>Syllabus reading</span>' +
            '<span class="mono"><b>' + p.readPct + '%</b> (' + p.readTopics + '/' + p.totalTopics + ')</span>' +
          '</div>' +
          '<div class="bar" style="height:8px">' +
            '<div class="bar__fill" style="width:' + p.readPct + '%;background:var(--ivri-blue)"></div>' +
          '</div>' +
        '</div>' +

        '<div class="paper-stats-row">' +
          '<div>' +
            '<div class="paper-stat-item-val">' + p.readTopics + '</div>' +
            '<div class="paper-stat-item-lbl">Read</div>' +
          '</div>' +
          '<div>' +
            '<div class="paper-stat-item-val">' + p.totalQuestions + '</div>' +
            '<div class="paper-stat-item-lbl">Questions</div>' +
          '</div>' +
          '<div>' +
            '<div class="paper-stat-item-val">' + (p.testCount ? p.avgScore + '%' : '—') + '</div>' +
            '<div class="paper-stat-item-lbl">Best avg</div>' +
          '</div>' +
          '<div>' +
            '<div class="paper-stat-item-val">' + p.untested + '</div>' +
            '<div class="paper-stat-item-lbl">Untested units</div>' +
          '</div>' +
        '</div>' +

        '<a class="btn btn--outline mt-2" href="#/quiz/paper/' + p.id + '">' +
          app.icon("quiz") + ' Simulate ' + app.esc(p.label) + ' exam' +
        '</a>' +
      '</div>';
    }

    return '<section>' +
      '<h2>Annual examination readiness</h2>' +
      '<p class="muted small mt-1">Split according to the official VCI veterinary board exam format.</p>' +
      '<div class="paper-readiness-grid mt-4">' +
        papers.map(function (p) { return renderPaperCard(computePaper(p)); }).join("") +
      '</div>' +
    '</section>';
  }

  /* ---------- Performance trend & lifetime accuracy ---------- */
  function renderTrendSection(attempts, totals) {
    if (!attempts.length) {
      return '<section>' +
        '<h2>Performance trend</h2>' +
        '<div class="card p-5 text-center text-muted mt-4">' +
          app.icon("pulse") + '<br>' +
          'Sit your first paper and this chart will start tracking how your score moves.<br>' +
          '<a class="btn btn--primary btn--sm mt-3" href="#/quiz">Take a diagnostic test</a>' +
        '</div>' +
      '</section>';
    }

    var recent = attempts.slice(-12);
    var pts = recent.map(function (a) { return app.pct(a.correct, a.total); });
    var first = pts[0], last = pts[pts.length - 1];
    var movement = pts.length > 1 ? last - first : 0;
    var best = Math.max.apply(null, pts);
    var avg = Math.round(pts.reduce(function (n, v) { return n + v; }, 0) / pts.length);

    var formatRows = ["mcq", "tf", "fib"].map(function (f) {
      var labels = { mcq: "🔘 Multiple choice", tf: "⚖️ True / False", fib: "✍️ Fill in the blank" };
      var r = totals.byFormat[f];
      return { label: labels[f], right: r.right, total: r.total };
    }).filter(function (r) { return r.total > 0; });

    var diffRows = [1, 2, 3].map(function (d) {
      var labels = { 1: "⭐ Foundational", 2: "⭐⭐ Core UG", 3: "⭐⭐⭐ Rank 1 classic" };
      var r = totals.byDiff[d];
      return { label: labels[d], right: r.right, total: r.total };
    }).filter(function (r) { return r.total > 0; });

    return '<section>' +
      '<div class="row row--between mb-3">' +
        '<div>' +
          '<h2>Performance trend</h2>' +
          '<p class="muted small mt-1">Your last ' + recent.length + ' paper' + (recent.length === 1 ? '' : 's') +
            ', and lifetime accuracy by question type.</p>' +
        '</div>' +
        '<span class="chip ' + (movement > 0 ? 'chip--ok' : movement < 0 ? 'chip--danger' : 'chip--subtle') + '">' +
          (movement > 0 ? '▲ +' : movement < 0 ? '▼ ' : '– ') + Math.abs(movement) + '% across this run' +
        '</span>' +
      '</div>' +

      '<div class="grid grid--2 mt-2">' +
        '<div class="card an-card">' +
          '<div class="row row--between">' +
            '<h3 class="an-card__title">Score history</h3>' +
            '<span class="small faint">avg ' + avg + '% · best ' + best + '%</span>' +
          '</div>' +
          sparkline(pts) +
          '<div class="trend-legend small faint">' +
            '<span>oldest</span><span class="push"></span><span>latest · ' + last + '%</span>' +
          '</div>' +
        '</div>' +

        '<div class="card an-card">' +
          '<h3 class="an-card__title">Lifetime accuracy</h3>' +
          '<div class="an-bars mt-3">' +
            formatRows.concat(diffRows).map(function (r) {
              var p = r.total ? Math.round(r.right / r.total * 100) : 0;
              return '<div class="an-bar">' +
                '<div class="an-bar__head"><span>' + r.label + '</span>' +
                '<span class="font-mono">' + r.right + '/' + r.total + ' · ' + p + '%</span></div>' +
                '<div class="bar"><div class="bar__fill ' + barTone(p) + '" style="width:' + p + '%"></div></div>' +
              '</div>';
            }).join("") +
          '</div>' +
        '</div>' +
      '</div>' +
    '</section>';
  }

  /* A dependency-free SVG sparkline with a 50% reference line. */
  function sparkline(values) {
    var w = 520, h = 140, pad = 12;
    var n = values.length;
    var stepX = n > 1 ? (w - pad * 2) / (n - 1) : 0;
    function y(v) { return h - pad - (v / 100) * (h - pad * 2); }
    function x(i) { return pad + i * stepX; }

    var line = values.map(function (v, i) { return (i ? "L" : "M") + x(i).toFixed(1) + " " + y(v).toFixed(1); }).join(" ");
    var area = n > 1
      ? line + " L" + x(n - 1).toFixed(1) + " " + (h - pad) + " L" + x(0).toFixed(1) + " " + (h - pad) + " Z"
      : "";

    var dots = values.map(function (v, i) {
      return '<circle class="spark__dot ' + barTone(v) + '" cx="' + x(i).toFixed(1) + '" cy="' + y(v).toFixed(1) +
        '" r="' + (i === n - 1 ? 5 : 3.5) + '"><title>Paper ' + (i + 1) + ': ' + v + '%</title></circle>';
    }).join("");

    return '<div class="spark mt-3"><svg viewBox="0 0 ' + w + ' ' + h + '" preserveAspectRatio="none" role="img" ' +
      'aria-label="Score across recent papers">' +
      '<line class="spark__ref" x1="' + pad + '" x2="' + (w - pad) + '" y1="' + y(50).toFixed(1) + '" y2="' + y(50).toFixed(1) + '"/>' +
      '<line class="spark__ref spark__ref--pass" x1="' + pad + '" x2="' + (w - pad) + '" y1="' + y(75).toFixed(1) + '" y2="' + y(75).toFixed(1) + '"/>' +
      (area ? '<path class="spark__area" d="' + area + '"/>' : '') +
      (n > 1 ? '<path class="spark__line" d="' + line + '"/>' : '') +
      dots +
    '</svg></div>';
  }

  /* ---------- Weakest sub-sections, named ---------- */
  function renderWeakSubsections(quiz) {
    var bySub = quiz.bySub || {};
    var keys = Object.keys(bySub);
    if (!keys.length) return "";

    var rows = keys.map(function (sid) {
      var r = bySub[sid];
      var meta = lookupSub(sid);
      return {
        id: sid,
        unitId: meta.unitId,
        icon: meta.icon,
        title: meta.title,
        right: r.right, total: r.total,
        pct: r.total ? Math.round(r.right / r.total * 100) : 0
      };
    }).filter(function (r) { return r.total >= 2; })
      .sort(function (a, b) { return a.pct - b.pct || b.total - a.total; });

    if (!rows.length) return "";

    var weak = rows.filter(function (r) { return r.pct < 75; }).slice(0, 5);
    var strong = rows.slice(0).reverse().filter(function (r) { return r.pct >= 75; }).slice(0, 3);

    return '<section>' +
      '<div class="row row--between mb-3">' +
        '<div>' +
          '<h2>Module-level diagnosis</h2>' +
          '<p class="muted small mt-1">Lifetime accuracy per syllabus sub-section, across every paper you have sat.</p>' +
        '</div>' +
      '</div>' +
      (weak.length
        ? '<div class="an-sub-list">' + weak.map(function (r) {
            return '<div class="an-sub">' +
              '<span class="an-sub__icon">' + r.icon + '</span>' +
              '<div class="an-sub__body">' +
                '<div class="an-sub__head">' +
                  '<b>' + app.esc(r.title) + '</b>' +
                  '<span class="chip ' + scoreChip(r.pct) + '">' + r.right + '/' + r.total + ' · ' + r.pct + '%</span>' +
                '</div>' +
                '<div class="bar mt-2"><div class="bar__fill ' + barTone(r.pct) + '" style="width:' + r.pct + '%"></div></div>' +
              '</div>' +
              '<div class="an-sub__actions">' +
                (r.unitId ? '<a class="btn btn--sm btn--outline" href="#/unit/' + r.unitId + '">Read</a>' : '') +
                (r.unitId ? '<a class="btn btn--sm" href="#/quiz/unit/' + r.unitId + '">Retest</a>' : '') +
              '</div>' +
            '</div>';
          }).join("") + '</div>'
        : '<div class="callout"><div class="callout__title">🏆 No weak module</div>' +
          'Every sub-section you have been tested on is at 75% or better. Widen the net — sit a paper-wise or grand mock.</div>') +

      (strong.length
        ? '<p class="small muted mt-4">Strongest so far: ' +
          strong.map(function (r) { return '<b>' + app.esc(r.title) + '</b> (' + r.pct + '%)'; }).join(" · ") + '</p>'
        : '') +
    '</section>';
  }

  /* Sub-section metadata lives in quiz.js; fall back gracefully if the
     quiz engine has not been loaded (it always is, but never assume). */
  function lookupSub(sid) {
    var fallback = { unitId: null, icon: "📘", title: sid };
    try {
      var unitId = "unit-" + String(sid).charAt(1);
      var unit = syllabus.unitById[unitId];
      fallback.unitId = unit ? unitId : null;
      var q = window.quizApp;
      if (q && q.subSectionMeta) {
        var m = q.subSectionMeta(sid);
        if (m) return { unitId: unitId, icon: m.icon, title: m.title };
      }
    } catch (e) {}
    return fallback;
  }

  /* ---------- Unit mastery matrix filters ---------- */
  function renderMatrixFilters(allUnits, quiz) {
    function count(fn) { return allUnits.filter(fn).length; }
    var best = function (u) {
      var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
      return rec && typeof rec.best === "number" ? rec.best : null;
    };

    // These labels were hard-coded as 8/4/4 against a six-unit syllabus.
    var tabs = [
      { id: "all", label: "All units", n: allUnits.length },
      { id: "theory", label: "Theory", n: count(function (u) { return u.stream === "theory"; }) },
      { id: "practical", label: "Practical", n: count(function (u) { return u.stream === "practical"; }) },
      { id: "untested", label: "Untested", n: count(function (u) { return best(u) === null; }) },
      { id: "weak", label: "Needs practice (<60%)", n: count(function (u) { var b = best(u); return b !== null && b < 60; }) },
      { id: "mastered", label: "Mastered (≥75%)", n: count(function (u) { var b = best(u); return b !== null && b >= 75; }) }
    ];

    return '<div class="matrix-filter-bar">' +
      tabs.map(function (tab) {
        return '<button class="matrix-tab-btn' + (activeFilter === tab.id ? ' is-active' : '') + '" data-filter="' + tab.id + '">' +
          tab.label + ' <span class="an-filter__n">' + tab.n + '</span>' +
        '</button>';
      }).join("") +
    '</div>';
  }

  /* ---------- Unit mastery matrix grid ---------- */
  function renderUnitMatrix(filter, allUnits, readMap, quiz) {
    var filtered = allUnits.filter(function (u) {
      var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
      var best = rec && typeof rec.best === "number" ? rec.best : null;

      if (filter === "theory") return u.stream === "theory";
      if (filter === "practical") return u.stream === "practical";
      if (filter === "untested") return best === null;
      if (filter === "weak") return best !== null && best < 60;
      if (filter === "mastered") return best !== null && best >= 75;
      return true;
    });

    if (!filtered.length) {
      return '<div class="card p-5 text-center text-muted">No units match this filter.</div>';
    }

    return '<div class="unit-mastery-grid">' +
      filtered.map(function (u) {
        var isTheory = u.stream === "theory";
        var tag = (isTheory ? "U" : "P") + u.no;
        var paper = paperOfUnit(u.id);
        var paperTag = paper ? (paper.name || paper.id) : "—";

        var uTopics = u.topics || [];
        var done = 0;
        uTopics.forEach(function (t) { if (readMap[t.id]) done++; });
        var readP = uTopics.length ? Math.round((done / uTopics.length) * 100) : 0;

        var qn = app.questionCount(u.id);
        var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
        var bestScore = (rec && typeof rec.best === "number") ? rec.best : null;
        var avgScore = (rec && rec.totalQ) ? Math.round(rec.totalCorrect / rec.totalQ * 100) : null;

        return '<div class="unit-card-elite">' +
          '<div class="unit-card-top">' +
            '<span class="unit-card-badge">' + tag + ' · ' + app.esc(paperTag) + '</span>' +
            (bestScore !== null
              ? '<span class="chip ' + scoreChip(bestScore) + '">' + bestScore + '% best</span>'
              : '<span class="chip chip--subtle">Untested</span>') +
          '</div>' +

          '<a class="unit-card-title" href="#/unit/' + u.id + '">' + app.esc(u.short || u.title) + '</a>' +

          '<div class="unit-card-bars">' +
            '<div class="unit-bar-item">' +
              '<div class="unit-bar-label">' +
                '<span>Reading progress</span>' +
                '<span class="mono">' + done + '/' + uTopics.length + ' (' + readP + '%)</span>' +
              '</div>' +
              '<div class="bar" style="height:6px">' +
                '<div class="bar__fill" style="width:' + readP + '%;background:var(--ivri-blue)"></div>' +
              '</div>' +
            '</div>' +
            (avgScore !== null
              ? '<div class="unit-bar-item">' +
                  '<div class="unit-bar-label">' +
                    '<span>Quiz accuracy</span>' +
                    '<span class="mono">' + rec.totalCorrect + '/' + rec.totalQ + ' (' + avgScore + '%) · ' + rec.runs + ' run' + (rec.runs === 1 ? '' : 's') + '</span>' +
                  '</div>' +
                  '<div class="bar" style="height:6px">' +
                    '<div class="bar__fill ' + barTone(avgScore) + '" style="width:' + avgScore + '%"></div>' +
                  '</div>' +
                '</div>'
              : '') +
          '</div>' +

          '<div class="unit-card-actions">' +
            '<a class="btn btn--sm btn--outline" style="flex:1" href="#/unit/' + u.id + '">' + app.icon("book") + ' Read</a>' +
            (qn
              ? '<a class="btn btn--sm btn--primary" style="flex:1" href="#/quiz/unit/' + u.id + '">' + app.icon("quiz") + ' Quiz (' + qn + ')</a>'
              : '<span class="btn btn--sm is-disabled" style="flex:1">No questions yet</span>') +
          '</div>' +
        '</div>';
      }).join("") +
    '</div>';
  }

  /* ---------- 5-box Leitner memory pipeline ---------- */
  function renderLeitnerPipeline(boxCounts, dueByBox, totalCards, dueCount) {
    var intervals = ["Daily (24 h)", "Every 2 days", "Every 4 days", "Every 8 days", "Mastered (16 d)"];
    var maxBox = Math.max.apply(null, boxCounts.concat([1]));

    return '<section class="srs-pipeline-wrap">' +
      '<div class="row row--between">' +
        '<div>' +
          '<h2>Spaced repetition memory matrix</h2>' +
          '<p class="muted small mt-1">Questions climb from Box 1 to Box 5 as you keep getting them right; one slip sends a card back to Box 1.</p>' +
        '</div>' +
        (dueCount > 0
          ? '<a class="btn btn--primary btn--sm" href="#/quiz/review">' + app.icon("repeat") + ' Review ' + dueCount + ' due</a>'
          : '<span class="chip chip--ok">' + app.icon("check") + ' Queue clear</span>') +
      '</div>' +

      (totalCards
        ? '<div class="srs-pipeline-grid">' +
            boxCounts.map(function (count, idx) {
              var pctOfTotal = totalCards ? Math.round((count / totalCards) * 100) : 0;
              return '<div class="srs-box-col" data-box="' + (idx + 1) + '">' +
                '<span class="srs-box-num">Box ' + (idx + 1) + '</span>' +
                '<div class="srs-box-count">' + count + '</div>' +
                '<div class="srs-box-interval">' + intervals[idx] + '</div>' +
                '<div class="bar mt-2" style="width:100%;height:5px">' +
                  '<div class="bar__fill" style="width:' + (count / maxBox * 100) + '%"></div>' +
                '</div>' +
                '<span class="srs-box-pct mt-1">' + pctOfTotal + '% of cards' +
                  (dueByBox[idx] ? ' · <b>' + dueByBox[idx] + ' due</b>' : '') + '</span>' +
              '</div>';
            }).join("") +
          '</div>'
        : '<div class="card p-5 text-center text-muted mt-4">' +
            'The queue fills itself as you answer quiz questions — every answer files that question into a box.' +
            '<br><a class="btn btn--primary btn--sm mt-3" href="#/quiz">Answer some questions</a></div>') +
    '</section>';
  }

  /* ---------- Activity heatmap ---------- */
  function renderHeatmapCard(activity, streak) {
    var DAYS = 84;
    var cells = [];
    var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    var d = new Date();
    d.setHours(0, 0, 0, 0);
    d.setDate(d.getDate() - (DAYS - 1));

    var activeDaysCount = 0;
    var totalInteractions = 0;
    var monthSpans = [];   // month labels are derived, not guessed at thirds

    for (var i = 0; i < DAYS; i++) {
      var key = d.getFullYear() + "-" +
        String(d.getMonth() + 1).padStart(2, "0") + "-" +
        String(d.getDate()).padStart(2, "0");
      var n = activity[key] || 0;
      if (n > 0) { activeDaysCount++; totalInteractions += n; }

      var label = monthNames[d.getMonth()];
      if (!monthSpans.length || monthSpans[monthSpans.length - 1].label !== label) {
        monthSpans.push({ label: label, n: 1 });
      } else {
        monthSpans[monthSpans.length - 1].n++;
      }

      var lvl = n === 0 ? 0 : n < 3 ? 1 : n < 6 ? 2 : n < 12 ? 3 : 4;
      cells.push('<div class="hm__cell" data-lvl="' + lvl + '" title="' +
        new Date(d).toLocaleDateString(undefined, { weekday: "short", month: "short", day: "numeric" }) +
        ' — ' + (n ? n + ' study actions' : 'no activity') + '"></div>');
      d.setDate(d.getDate() + 1);
    }

    return '<div class="heatmap-card-elite">' +
      '<div class="row row--between">' +
        '<div>' +
          '<h3>Study activity heatmap</h3>' +
          '<p class="muted small mt-1">The past 12 weeks of study actions.</p>' +
        '</div>' +
        '<span class="chip font-mono">' + totalInteractions + ' actions</span>' +
      '</div>' +

      '<div class="heatmap-grid-scroll mt-4">' +
        '<div class="heatmap-months-row">' +
          monthSpans.map(function (m) {
            return '<span style="flex:' + m.n + ' 0 0">' + m.label + '</span>';
          }).join("") +
        '</div>' +
        '<div class="hm-elite">' + cells.join("") + '</div>' +
      '</div>' +

      '<div class="heatmap-summary-strip">' +
        '<div>Active days: <b>' + activeDaysCount + ' / ' + DAYS + '</b></div>' +
        '<div>Longest streak: <b>' + streak.longest + ' days</b></div>' +
        '<div class="row small faint" style="gap:4px">' +
          '<span>Less</span>' +
          [0, 1, 2, 3, 4].map(function (l) { return '<div class="hm__cell" style="width:11px;height:11px" data-lvl="' + l + '"></div>'; }).join("") +
          '<span>More</span>' +
        '</div>' +
      '</div>' +
    '</div>';
  }

  /* ---------- Assessment ledger ---------- */
  function renderRecentAttemptsCard(quiz) {
    var list = (quiz.attempts || []).slice(-7).reverse();

    if (!list.length) {
      return '<div class="heatmap-card-elite">' +
        '<h3>Assessment ledger</h3>' +
        '<p class="muted small mt-1">A record of your quizzes and simulation exams.</p>' +
        '<div class="card p-5 text-center mt-4 text-muted">' +
          app.icon("target") + '<br>No quiz attempts recorded yet.<br>' +
          '<a class="btn btn--primary btn--sm mt-3" href="#/quiz">Take a diagnostic test</a>' +
        '</div>' +
      '</div>';
    }

    return '<div class="heatmap-card-elite">' +
      '<div class="row row--between">' +
        '<div>' +
          '<h3>Assessment ledger</h3>' +
          '<p class="muted small mt-1">Open any paper for its full analysis.</p>' +
        '</div>' +
        '<a class="small" href="#/quiz">Quiz hub &rarr;</a>' +
      '</div>' +

      '<div class="tlist mt-4" style="border:none">' +
        list.map(function (a) {
          var p = app.pct(a.correct, a.total);
          var dt = new Date(a.at);
          var dateStr = dt.toLocaleDateString(undefined, { month: "short", day: "numeric" });
          var fmtLine = a.byFormat
            ? ["mcq", "tf", "fib"].filter(function (f) { return a.byFormat[f] && a.byFormat[f].total; })
                .map(function (f) {
                  var labels = { mcq: "MCQ", tf: "T/F", fib: "FIB" };
                  return labels[f] + ' ' + a.byFormat[f].right + '/' + a.byFormat[f].total;
                }).join(' · ')
            : '';
          return '<a class="tlist__row" href="#/quiz/attempt/' + encodeURIComponent(a.id) + '">' +
            '<span class="tlist__body">' +
              '<span class="tlist__title">' + app.esc(a.label || "Animal Genetics Quiz") + '</span>' +
              '<span class="tlist__sub">' + dateStr +
                (a.exam ? ' · ⏱️ timed' : '') +
                (a.orderMode ? ' · ' + (a.orderMode === "shuffle" ? "🔀 shuffle" : "📋 sequence") : '') +
                (a.seconds ? ' · ' + Math.max(1, Math.round(a.seconds / 60)) + ' min' : '') +
                (a.skipped ? ' · ' + a.skipped + ' skipped' : '') +
                (a.timedOut ? ' · ⌛ auto-submitted' : '') +
                (fmtLine ? '<br>' + fmtLine : '') +
              '</span>' +
            '</span>' +
            '<span class="tlist__right">' +
              '<span class="chip ' + scoreChip(p) + '">' + a.correct + '/' + a.total + ' (' + p + '%)</span>' +
              app.icon("chevron", "faint") +
            '</span>' +
          '</a>';
        }).join("") +
      '</div>' +
    '</div>';
  }

  /* ---------- Student knowledge vault ---------- */
  function renderKnowledgeVault(totalHl, hlColors, notesCount, bmsCount, qaCount) {
    return '<section>' +
      '<h2>Knowledge vault</h2>' +
      '<p class="muted small mt-1">Your personal repository of notes, high-yield highlights and bookmarks.</p>' +
      '<div class="vault-grid mt-4">' +
        vaultCard("#/library", "star", bmsCount, "Bookmarked topics", "Quick revision access") +
        vaultCard("#/library", "note", notesCount, "Personal notes", "Your own observations") +
        vaultCard("#/library", "pen", totalHl, "Passages highlighted", "Colour-coded key points") +
        vaultCard("#/qa", "qa", qaCount, "Exam questions revised", "Model answers reviewed") +
      '</div>' +
    '</section>';
  }

  function vaultCard(href, ico, val, title, sub) {
    return '<a class="vault-card" href="' + href + '">' +
      '<div class="vault-card-icon">' + app.icon(ico) + '</div>' +
      '<div class="vault-card-val">' + val + '</div>' +
      '<div class="vault-card-title">' + title + '</div>' +
      '<div class="vault-card-sub">' + sub + '</div>' +
    '</a>';
  }

  /* ---------- Helpers ---------- */
  function shorten(s, n) {
    if (!s) return "";
    return s.length > n ? s.slice(0, n - 1) + "…" : s;
  }

  function findNextUnreadTopic(allUnits, readMap) {
    for (var uIdx = 0; uIdx < allUnits.length; uIdx++) {
      var u = allUnits[uIdx];
      var topics = u.topics || [];
      for (var tIdx = 0; tIdx < topics.length; tIdx++) {
        var t = topics[tIdx];
        if (!readMap[t.id]) {
          return { id: t.id, title: t.title, index: t.index || (tIdx + 1), unitTitle: u.short || u.title };
        }
      }
    }
    return null;
  }

  /* An untested unit is the bigger risk, so it outranks any tested one —
     the old version stopped at the first unit it saw and could recommend a
     90% unit while a whole untested unit sat beside it. */
  function findWeakestUnit(allUnits, quiz) {
    var theory = allUnits.filter(function (u) {
      return u.stream === "theory" && app.questionCount(u.id) > 0;
    });
    if (!theory.length) theory = allUnits.filter(function (u) { return app.questionCount(u.id) > 0; });
    if (!theory.length) {
      var f = allUnits[0] || { id: "unit-1", short: "Biostatistics" };
      return { id: f.id, name: f.short || f.title, score: 0, hasScore: false };
    }

    var untested = theory.filter(function (u) {
      var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
      return !(rec && typeof rec.best === "number");
    });
    if (untested.length) {
      return { id: untested[0].id, name: untested[0].short || untested[0].title, score: 0, hasScore: false };
    }

    var worst = theory[0], worstScore = 101;
    theory.forEach(function (u) {
      var rec = quiz.byUnit["unit:" + u.id];
      if (rec.best < worstScore) { worstScore = rec.best; worst = u; }
    });
    return { id: worst.id, name: worst.short || worst.title, score: worstScore, hasScore: true };
  }

  /* ---------- Attach UI events ---------- */
  function attachDashboardEvents(host, allUnits, readMap, quiz) {
    var filterBtns = host.querySelectorAll(".matrix-tab-btn");
    var container = host.querySelector("#unit-matrix-container");

    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        activeFilter = btn.getAttribute("data-filter") || "all";
        if (container) container.innerHTML = renderUnitMatrix(activeFilter, allUnits, readMap, quiz);
      });
    });
  }

  return {
    render: render
  };
})();
