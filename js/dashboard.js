/* ============================================================
   dashboard.js — Simple, Colorful & Actionable Learning Analytics
   ============================================================
   Designed to be so simple and intuitive that a 13-year-old can
   instantly understand their progress at a glance:
     - Clear Level & Grade Hero (Level 1 to Level 4)
     - 4 Big Power Cards: Lessons Read, Quiz Score, Streak, Memory
     - "What Should I Do Today?" 3 one-click action quests
     - Simple Exam Readiness: Paper 1 vs Paper 2 side-by-side
     - Unit Report Cards with 1-click Read and Quiz buttons
     - "Your Memory Strength": simple 3-tier memory vault
     - Activity Tracker and Recent Quiz Hall of Fame
     - Knowledge Vault (Bookmarks, Notes, Highlights, Q&A)
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
    var streak     = store.computeStreak ? store.computeStreak() : { current: 0, longest: 0, totalDays: 0 };
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

    // Spaced repetition statistics (Simplified into Learning, Stronger, Mastered)
    var srsKeys = Object.keys(srs);
    var learningCount = 0; // Box 1 & 2
    var strongerCount = 0; // Box 3 & 4
    var masteredCount = 0; // Box 5
    var now = Date.now();

    srsKeys.forEach(function (k) {
      var b = Math.min(5, Math.max(1, srs[k].box || 1));
      if (b <= 2) learningCount++;
      else if (b <= 4) strongerCount++;
      else masteredCount++;
    });

    var retentionRate = srsKeys.length
      ? Math.round(((strongerCount + masteredCount) / srsKeys.length) * 100)
      : 0;

    // Highlights stats
    var totalHighlights = 0;
    Object.keys(highlights).forEach(function (topId) {
      totalHighlights += (highlights[topId] || []).length;
    });

    // Mastery XP Calculation (0 to 1000 XP)
    var readXP = Math.round((readCount / (totalTopics || 1)) * 400);          // 40% weight
    var quizFactor = totalQ ? (totalCorrect / totalQ) : 0;
    var quizVolume = Math.min(1, attempts.length / 8);
    var quizXP = Math.round((quizFactor * 0.7 + quizVolume * 0.3) * 350);     // 35% weight
    var srsFactor = srsKeys.length ? ((strongerCount + masteredCount) / srsKeys.length) : 0;
    var srsVolume = Math.min(1, srsKeys.length / 25);
    var srsXP = Math.round((srsFactor * 0.6 + srsVolume * 0.4) * 150);        // 15% weight
    var streakFactor = Math.min(1, streak.current / 7);
    var daysFactor = Math.min(1, streak.totalDays / 10);
    var consistencyXP = Math.round((streakFactor * 0.6 + daysFactor * 0.4) * 100); // 10% weight

    var totalXP = Math.min(1000, readXP + quizXP + srsXP + consistencyXP);
    var readinessPct = Math.min(100, Math.round(totalXP / 10));
    var rank = getSimpleRank(totalXP);

    // Friendly overview summary sentence
    var summaryMessage = getFriendlySummary(readPct, quizAccuracy, attempts.length, streak.current);

    host.innerHTML =
      '<div class="dash-simplified animate-fade-in">' +

        /* 1. Clear, Friendly Level & Report Card Hero */
        '<div class="dash-hero-clean">' +
          '<div class="dash-hero-grid">' +

            /* Left: Level Badge & Ring */
            '<div class="dash-hero-gauge-col">' +
              '<div class="dash-level-ring-wrap">' +
                app.ringHtml(readinessPct, 150) +
                '<div class="dash-level-ring-center">' +
                  '<span class="dash-level-ring-xp">' + totalXP + '</span>' +
                  '<span class="dash-level-ring-label">Score XP</span>' +
                '</div>' +
              '</div>' +
              '<div class="dash-rank-badge">' + rank.icon + ' ' + rank.title + '</div>' +
              '<div class="dash-next-rank-hint mt-2">' + rank.nextHint + '</div>' +
            '</div>' +

            /* Right: Clear Plain-English Status */
            '<div class="dash-hero-info-col">' +
              '<div class="dash-hero-pill-row">' +
                '<span class="dash-badge-pill dash-badge-pill--blue">⭐ ' + rank.title + '</span>' +
                '<span class="dash-badge-pill dash-badge-pill--green">' + readinessPct + '% Exam Ready</span>' +
                (streak.current > 0 ? '<span class="dash-badge-pill dash-badge-pill--flame">🔥 ' + streak.current + ' Day Streak</span>' : '') +
              '</div>' +
              '<h1 class="dash-hero-title mt-2">Animal Genetics Progress</h1>' +
              '<p class="dash-hero-summary mt-2">' + summaryMessage + '</p>' +

              /* Simple XP Breakdown Bar */
              '<div class="dash-xp-breakdown mt-4">' +
                '<div class="dash-xp-bar">' +
                  '<div class="dash-xp-segment dash-xp-segment--read" style="width:' + (readXP / 10) + '%" title="Reading: ' + readXP + ' XP"></div>' +
                  '<div class="dash-xp-segment dash-xp-segment--quiz" style="width:' + (quizXP / 10) + '%" title="Quizzes: ' + quizXP + ' XP"></div>' +
                  '<div class="dash-xp-segment dash-xp-segment--memory" style="width:' + (srsXP / 10) + '%" title="Memory: ' + srsXP + ' XP"></div>' +
                  '<div class="dash-xp-segment dash-xp-segment--streak" style="width:' + (consistencyXP / 10) + '%" title="Consistency: ' + consistencyXP + ' XP"></div>' +
                '</div>' +
                '<div class="dash-xp-legend mt-2">' +
                  '<span><i class="dot dot--read"></i> 📖 Reading (' + readXP + ')</span>' +
                  '<span><i class="dot dot--quiz"></i> 🎯 Quizzes (' + quizXP + ')</span>' +
                  '<span><i class="dot dot--memory"></i> 🧠 Memory (' + srsXP + ')</span>' +
                  '<span><i class="dot dot--streak"></i> 🔥 Daily (' + consistencyXP + ')</span>' +
                '</div>' +
              '</div>' +

            '</div>' +
          '</div>' +
        '</div>' +

        /* 2. Four Big Colorful Power Cards (At a glance) */
        '<div class="dash-power-grid mt-6">' +
          powerCard("📖", "Lessons Completed", readCount + " of " + totalTopics, readPct + "% of syllabus done", readPct, "blue", "#/theory") +
          powerCard("🎯", "Quiz Accuracy", (totalQ ? quizAccuracy + "%" : "—"), (totalQ ? "You get ~" + Math.round(quizAccuracy / 10) + " out of 10 right! 🎉" : "Take a quiz to see score!"), quizAccuracy, "amber", "#/quiz") +
          powerCard("🔥", "Study Streak", streak.current + " " + (streak.current === 1 ? "Day" : "Days"), "Best record: " + streak.longest + " days", Math.min(100, streak.current * 15), "coral", "#/theory") +
          powerCard("🧠", "Memory Strength", (srsKeys.length ? retentionRate + "%" : "Ready!"), (dueCards ? "⚠️ " + dueCards + " cards need a quick review!" : "All cards fresh & remembered!"), retentionRate || 100, "green", "#/quiz/review") +
        '</div>' +

        /* 3. "What Should I Do Today?" 3 Quick Quests */
        '<div class="dash-section-head mt-10">' +
          '<div class="dash-section-title"><span>🚀</span> What Should I Do Today?</div>' +
          '<p class="dash-section-sub">Pick any of these 3 easy 1-click missions to level up your score.</p>' +
        '</div>' +
        renderQuickQuests(dueCards, allUnits, readMap, quiz, totalTopics, readCount) +

        /* 4. Exam Readiness: Paper 1 vs Paper 2 Side-by-Side */
        '<div class="dash-section-head mt-12">' +
          '<div class="dash-section-title"><span>📋</span> Annual Board Exam Readiness</div>' +
          '<p class="dash-section-sub">Official VCI exams are divided into Paper I and Paper II. Check how prepared you are for each!</p>' +
        '</div>' +
        renderPaperReadiness(readMap, quiz) +

        /* 5. Unit Progress Report Card */
        '<div class="dash-section-head mt-12">' +
          '<div class="dash-section-title"><span>⭐</span> Unit Report Cards</div>' +
          '<p class="dash-section-sub">Your progress across every theory and practical unit. Click to read or take a quick quiz!</p>' +
        '</div>' +
        renderMatrixFilters(allUnits, quiz) +
        '<div id="unit-matrix-container" class="mt-4">' +
          renderUnitReportCards(activeFilter, allUnits, readMap, quiz) +
        '</div>' +

        /* 6. Kid-Friendly Memory Vault (3 Simple Steps instead of confusing 5 boxes) */
        '<div class="dash-section-head mt-12">' +
          '<div class="dash-section-title"><span>🧠</span> Memory Vault (Spaced Repetition)</div>' +
          '<p class="dash-section-sub">Every time you answer a question correctly, it moves up a level and stays in your memory longer.</p>' +
        '</div>' +
        renderSimpleMemoryVault(learningCount, strongerCount, masteredCount, srsKeys.length, dueCards) +

        /* 7. Activity Calendar + Recent Quiz Attempts */
        '<div class="grid grid--2 mt-12">' +
          renderSimpleActivityCard(activity, streak) +
          renderRecentQuizScoresCard(quiz) +
        '</div>' +

        /* 8. Knowledge Vault */
        '<div class="dash-section-head mt-12">' +
          '<div class="dash-section-title"><span>🗂️</span> Your Personal Study Vault</div>' +
          '<p class="dash-section-sub">Saved bookmarks, personal revision notes, and highlighted key sentences.</p>' +
        '</div>' +
        renderKnowledgeVault(totalHighlights, Object.keys(notes).length, bms.length, qaDone.length) +

      '</div>';

    attachDashboardEvents(host, allUnits, readMap, quiz);
  }

  /* Helpers */
  function countReadTopics(units, readMap) {
    var n = 0;
    units.forEach(function (u) {
      (u.topics || []).forEach(function (t) { if (readMap[t.id]) n++; });
    });
    return n;
  }

  function getSimpleRank(xp) {
    if (xp >= 750) {
      return {
        title: "Level 4 · Master Breeder",
        icon: "👑",
        nextHint: "⭐ Maximum Level Reached! You are an Animal Genetics Wizard!"
      };
    }
    if (xp >= 500) {
      return {
        title: "Level 3 · Senior Geneticist",
        icon: "🧬",
        nextHint: (750 - xp) + " XP needed to reach Level 4: Master Breeder 👑"
      };
    }
    if (xp >= 250) {
      return {
        title: "Level 2 · Animal Scientist",
        icon: "🔬",
        nextHint: (500 - xp) + " XP needed to reach Level 3: Senior Geneticist 🧬"
      };
    }
    return {
      title: "Level 1 · Genetics Explorer",
      icon: "⭐",
      nextHint: (250 - xp) + " XP needed to reach Level 2: Animal Scientist 🔬"
    };
  }

  function getFriendlySummary(readPct, quizAccuracy, attemptsCount, streakDays) {
    if (readPct >= 80 && quizAccuracy >= 80) {
      return "Outstanding work! You've mastered almost the entire syllabus and your quiz scores are at Distinction level! 🏆";
    }
    if (attemptsCount === 0) {
      return "Welcome! Start by reading a lesson or playing a 5-minute quiz to see your progress bar light up!";
    }
    if (readPct > 40 && quizAccuracy >= 70) {
      return "You're on track for a First Class! Keep reading lessons and clearing your daily quizzes to push for distinction! 🚀";
    }
    if (streakDays >= 3) {
      return "Awesome daily consistency! You've studied " + streakDays + " days in a row — keep the flame burning today! 🔥";
    }
    return "Every lesson you read and every quiz you play moves your exam readiness higher. Pick a mission below to get started!";
  }

  function powerCard(icon, title, val, sub, barPct, color, link) {
    return '<a class="dash-power-card dash-power-card--' + color + '" href="' + link + '">' +
      '<div class="dash-power-card__top">' +
        '<span class="dash-power-card__icon">' + icon + '</span>' +
        '<span class="dash-power-card__title">' + title + '</span>' +
      '</div>' +
      '<div class="dash-power-card__val">' + app.esc(val) + '</div>' +
      '<div class="dash-power-card__bar-wrap">' +
        '<div class="dash-power-card__bar" style="width:' + Math.min(100, Math.max(0, barPct)) + '%"></div>' +
      '</div>' +
      '<div class="dash-power-card__sub">' + app.esc(sub) + '</div>' +
    '</a>';
  }

  /* 3 Quick Quests (Simple & Actionable) */
  function renderQuickQuests(dueCards, allUnits, readMap, quiz, totalTopics, readCount) {
    var nextTopic = findNextUnreadTopic(allUnits, readMap);
    var weakUnit = findWeakestUnit(allUnits, quiz);

    // Quest 1: Reading Quest
    var readQuest = nextTopic
      ? '<div class="dash-quest-card dash-quest-card--blue">' +
          '<div class="dash-quest-card__badge">MISSION 1 · NEXT LESSON</div>' +
          '<h3 class="dash-quest-card__title">' + app.esc(nextTopic.title) + '</h3>' +
          '<p class="dash-quest-card__desc">' + app.esc(nextTopic.unitTitle) + ' · ' + (totalTopics - readCount) + ' lessons left to complete syllabus.</p>' +
          '<a class="btn btn--primary btn--quest" href="#/topic/' + nextTopic.id + '">📖 Open Lesson →</a>' +
        '</div>'
      : '<div class="dash-quest-card dash-quest-card--blue">' +
          '<div class="dash-quest-card__badge">MISSION 1 · SYLLABUS COMPLETE</div>' +
          '<h3 class="dash-quest-card__title">All ' + totalTopics + ' Lessons Read!</h3>' +
          '<p class="dash-quest-card__desc">You have unlocked and read every topic in the entire course. Fantastic!</p>' +
          '<a class="btn btn--outline btn--quest" href="#/theory">Review Lessons →</a>' +
        '</div>';

    // Quest 2: Quiz Quest
    var quizQuest =
      '<div class="dash-quest-card dash-quest-card--amber">' +
        '<div class="dash-quest-card__badge">MISSION 2 · 5-MIN QUIZ</div>' +
        '<h3 class="dash-quest-card__title">' + app.esc(weakUnit.name) + '</h3>' +
        '<p class="dash-quest-card__desc">' + (weakUnit.hasScore
          ? "Target this unit to boost your best score (" + weakUnit.score + "%)."
          : "Untested unit! Play a quick quiz to find your current score.") + '</p>' +
        '<a class="btn btn--primary btn--quest" href="#/quiz/unit/' + weakUnit.id + '">🎯 Play 5-Min Quiz →</a>' +
      '</div>';

    // Quest 3: Memory Quest
    var memoryQuest = dueCards > 0
      ? '<div class="dash-quest-card dash-quest-card--green is-urgent">' +
          '<div class="dash-quest-card__badge">MISSION 3 · MEMORY REFRESH</div>' +
          '<h3 class="dash-quest-card__title">' + dueCards + ' Flashcards Ready</h3>' +
          '<p class="dash-quest-card__desc">Refresh them in 2 minutes so you don\'t forget what you learned!</p>' +
          '<a class="btn btn--primary btn--quest" href="#/quiz/review">🧠 Quick 2-Min Review →</a>' +
        '</div>'
      : '<div class="dash-quest-card dash-quest-card--green">' +
          '<div class="dash-quest-card__badge">MISSION 3 · MEMORY REFRESH</div>' +
          '<h3 class="dash-quest-card__title">Memory Vault 100% Fresh</h3>' +
          '<p class="dash-quest-card__desc">No cards are overdue today. Everything you learned is locked in!</p>' +
          '<a class="btn btn--outline btn--quest" href="#/quiz">Practice Questions →</a>' +
        '</div>';

    return '<div class="dash-quests-grid mt-4">' + readQuest + quizQuest + memoryQuest + '</div>';
  }

  /* Paper I vs Paper II Dual Examination Readiness */
  function renderPaperReadiness(readMap, quiz) {
    var papers = (syllabus.meta && syllabus.meta.papers) || [];
    if (!papers.length) return "";

    function paperTitle(id) {
      return id === "paper-1"
        ? "Biostatistics & Animal Genetics"
        : id === "paper-2" ? "Principles of Animal Breeding" : "Examination Paper";
    }

    function unitsOfPaper(paperId) {
      return (syllabus.allUnits || []).filter(function (u) {
        var no = (syllabus.unitById[u.id] || {}).no;
        var p = (syllabus.meta.papers || []).filter(function (x) { return x.id === paperId; })[0];
        return p && (p.units || []).indexOf(no) !== -1;
      });
    }

    function computePaper(p) {
      var units = unitsOfPaper(p.id);
      var totalT = 0, readT = 0;
      var scores = [];

      units.forEach(function (u) {
        var uTopics = u.topics || [];
        totalT += uTopics.length;
        uTopics.forEach(function (t) { if (readMap[t.id]) readT++; });
        var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
        if (rec && typeof rec.best === "number") scores.push(rec.best);
      });

      var readPercent = totalT ? Math.round((readT / totalT) * 100) : 0;
      var avgScore = scores.length
        ? Math.round(scores.reduce(function (a, b) { return a + b; }, 0) / scores.length) : 0;

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
        unitLabel: (p.units.length === 1 ? "Unit " : "Units ") + p.units.join(", "),
        totalTopics: totalT, readTopics: readT, readPct: readPercent,
        avgScore: avgScore,
        testCount: scores.length, unitCount: units.length,
        readiness: readiness
      };
    }

    return '<div class="dash-papers-grid mt-4">' +
      papers.map(function (pRaw) {
        var p = computePaper(pRaw);
        var statusBadge = p.readiness >= 75 ? "⭐ Distinction Ready!" : p.readiness >= 50 ? "👍 Good Progress!" : "⚡ Needs Practice";
        var theme = p.id === "paper-1" ? "blue" : "emerald";

        return '<div class="dash-paper-card dash-paper-card--' + theme + '">' +
          '<div class="dash-paper-card__top">' +
            '<div>' +
              '<span class="dash-paper-card__tag">' + app.esc(p.label) + '</span>' +
              '<h3 class="dash-paper-card__title mt-1">' + app.esc(p.name) + '</h3>' +
              '<p class="dash-paper-card__units">' + app.esc(p.unitLabel) + ' · ' + p.unitCount + ' Units</p>' +
            '</div>' +
            '<div class="dash-paper-card__gauge">' +
              app.ringHtml(p.readiness, 84) +
            '</div>' +
          '</div>' +

          '<div class="dash-paper-card__stats mt-4">' +
            '<div class="dash-paper-stat">' +
              '<span class="dash-paper-stat__val">' + p.readPct + '%</span>' +
              '<span class="dash-paper-stat__lbl">📖 Lessons (' + p.readTopics + '/' + p.totalTopics + ')</span>' +
            '</div>' +
            '<div class="dash-paper-stat">' +
              '<span class="dash-paper-stat__val">' + (p.testCount ? p.avgScore + "%" : "—") + '</span>' +
              '<span class="dash-paper-stat__lbl">🎯 Quiz Score</span>' +
            '</div>' +
            '<div class="dash-paper-stat">' +
              '<span class="dash-paper-stat__val">' + p.readiness + '%</span>' +
              '<span class="dash-paper-stat__lbl">' + statusBadge + '</span>' +
            '</div>' +
          '</div>' +

          '<div class="dash-paper-card__actions mt-4">' +
            '<a class="btn btn--primary btn--play-paper" href="#/quiz/paper/' + p.id + '">' +
              '🚀 Practice ' + app.esc(p.label) + ' Mock Exam →' +
            '</a>' +
          '</div>' +
        '</div>';
      }).join("") +
    '</div>';
  }

  /* Unit Report Cards Filters */
  function renderMatrixFilters(allUnits, quiz) {
    function count(fn) { return allUnits.filter(fn).length; }
    var best = function (u) {
      var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
      return rec && typeof rec.best === "number" ? rec.best : null;
    };

    var tabs = [
      { id: "all", label: "🌟 All Units", n: allUnits.length },
      { id: "theory", label: "📘 Theory Units", n: count(function (u) { return u.stream === "theory"; }) },
      { id: "practical", label: "🔬 Practical Units", n: count(function (u) { return u.stream === "practical"; }) },
      { id: "mastered", label: "🏆 Mastered (≥75%)", n: count(function (u) { var b = best(u); return b !== null && b >= 75; }) }
    ];

    return '<div class="matrix-filter-bar mt-4">' +
      tabs.map(function (tab) {
        return '<button class="matrix-tab-btn' + (activeFilter === tab.id ? ' is-active' : '') + '" data-filter="' + tab.id + '">' +
          tab.label + ' <span class="an-filter__n">' + tab.n + '</span>' +
        '</button>';
      }).join("") +
    '</div>';
  }

  /* Unit Report Cards Grid (Simple, kid-friendly cards) */
  function renderUnitReportCards(filter, allUnits, readMap, quiz) {
    var filtered = allUnits.filter(function (u) {
      var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
      var best = rec && typeof rec.best === "number" ? rec.best : null;
      if (filter === "theory") return u.stream === "theory";
      if (filter === "practical") return u.stream === "practical";
      if (filter === "mastered") return best !== null && best >= 75;
      return true;
    });

    if (!filtered.length) {
      return '<div class="card p-5 text-center text-muted">No units match this filter.</div>';
    }

    return '<div class="dash-unit-cards-grid">' +
      filtered.map(function (u) {
        var isTheory = u.stream === "theory";
        var tag = (isTheory ? "Theory Unit " : "Practical Unit ") + u.no;
        var uTopics = u.topics || [];
        var done = 0;
        uTopics.forEach(function (t) { if (readMap[t.id]) done++; });
        var readP = uTopics.length ? Math.round((done / uTopics.length) * 100) : 0;

        var qn = app.questionCount(u.id);
        var rec = quiz.byUnit && quiz.byUnit["unit:" + u.id];
        var bestScore = (rec && typeof rec.best === "number") ? rec.best : null;

        var stars = bestScore >= 85 ? "⭐⭐⭐" : bestScore >= 70 ? "⭐⭐" : bestScore !== null ? "⭐" : "○";

        return '<div class="dash-unit-card">' +
          '<div class="dash-unit-card__head">' +
            '<span class="dash-unit-card__tag">' + tag + '</span>' +
            '<span class="dash-unit-card__stars">' + stars + '</span>' +
          '</div>' +

          '<h3 class="dash-unit-card__title">' + app.esc(u.short || u.title) + '</h3>' +

          '<div class="dash-unit-card__progress mt-3">' +
            '<div class="row row--between small">' +
              '<span>Reading Progress</span>' +
              '<b>' + done + '/' + uTopics.length + ' (' + readP + '%)</b>' +
            '</div>' +
            '<div class="bar mt-1" style="height:7px"><div class="bar__fill" style="width:' + readP + '%;background:var(--ivri-blue)"></div></div>' +
          '</div>' +

          '<div class="dash-unit-card__quiz-stat mt-3">' +
            (bestScore !== null
              ? '<span class="chip ' + (bestScore >= 75 ? 'chip--ok' : 'chip--warn') + '">Best Quiz: ' + bestScore + '%</span>'
              : '<span class="chip chip--subtle">Quiz: Not Tested Yet</span>') +
            '<span class="small faint">' + qn + ' Questions</span>' +
          '</div>' +

          '<div class="dash-unit-card__buttons mt-4">' +
            '<a class="btn btn--sm btn--outline" href="#/unit/' + u.id + '">📖 Read Lessons</a>' +
            (qn
              ? '<a class="btn btn--sm btn--primary" href="#/quiz/unit/' + u.id + '">🎯 Play Quiz</a>'
              : '') +
          '</div>' +
        '</div>';
      }).join("") +
    '</div>';
  }

  /* Kid-Friendly Memory Vault (3 Simple Steps) */
  function renderSimpleMemoryVault(learning, stronger, mastered, total, dueCount) {
    var maxVal = Math.max(learning, stronger, mastered, 1);

    return '<div class="dash-memory-vault mt-4">' +
      '<div class="dash-memory-vault__hero">' +
        '<div class="dash-memory-vault__status">' +
          '<h3 class="dash-memory-vault__title">' + (mastered + stronger) + ' of ' + (total || 0) + ' Cards Memorized</h3>' +
          '<p class="dash-memory-vault__sub">As you practice quizzes, questions climb to Mastered status and stay remembered for exams!</p>' +
        '</div>' +
        (dueCount > 0
          ? '<a class="btn btn--primary btn--play" href="#/quiz/review">🧠 Review ' + dueCount + ' Cards Due Today →</a>'
          : '<span class="chip chip--ok">✓ Memory Vault Up-To-Date</span>') +
      '</div>' +

      '<div class="dash-memory-vault__steps mt-4">' +
        memoryStepCard("🥉 Step 1", "Just Learning", learning, "Cards you've seen once", "amber", maxVal) +
        memoryStepCard("🥈 Step 2", "Getting Stronger", stronger, "Remembered after 2-3 reviews", "blue", maxVal) +
        memoryStepCard("🥇 Step 3", "Locked In Memory!", mastered, "Permanent long-term memory", "green", maxVal) +
      '</div>' +
    '</div>';
  }

  function memoryStepCard(badge, title, count, sub, color, maxVal) {
    var pct = Math.round((count / maxVal) * 100);
    return '<div class="dash-mem-step dash-mem-step--' + color + '">' +
      '<span class="dash-mem-step__badge">' + badge + '</span>' +
      '<div class="dash-mem-step__val">' + count + '</div>' +
      '<div class="dash-mem-step__title">' + title + '</div>' +
      '<div class="dash-mem-step__bar-wrap mt-2">' +
        '<div class="dash-mem-step__bar" style="width:' + pct + '%"></div>' +
      '</div>' +
      '<div class="dash-mem-step__sub mt-1">' + sub + '</div>' +
    '</div>';
  }

  /* Activity Heatmap */
  function renderSimpleActivityCard(activity, streak) {
    var DAYS = 28; // Simple 4-week calendar
    var cells = [];
    var d = new Date();
    d.setHours(0, 0, 0, 0);
    d.setDate(d.getDate() - (DAYS - 1));

    var activeDays = 0;
    for (var i = 0; i < DAYS; i++) {
      var key = d.getFullYear() + "-" +
        String(d.getMonth() + 1).padStart(2, "0") + "-" +
        String(d.getDate()).padStart(2, "0");
      var n = activity[key] || 0;
      if (n > 0) activeDays++;
      var lvl = n === 0 ? 0 : n < 3 ? 1 : n < 6 ? 2 : 3;
      var dateLabel = d.toLocaleDateString(undefined, { weekday: "short", month: "short", day: "numeric" });
      cells.push('<div class="dash-cal-cell" data-lvl="' + lvl + '" title="' + dateLabel + ' — ' + (n ? n + ' study actions' : 'no activity') + '"></div>');
      d.setDate(d.getDate() + 1);
    }

    return '<div class="dash-card-box">' +
      '<div class="row row--between items-center">' +
        '<div>' +
          '<h3>📅 Past 4 Weeks Study Calendar</h3>' +
          '<p class="muted small mt-1">Study every day to build your streak!</p>' +
        '</div>' +
        '<span class="chip chip--accent font-bold">' + activeDays + ' of 28 Days Active</span>' +
      '</div>' +

      '<div class="dash-cal-grid mt-4">' +
        cells.join("") +
      '</div>' +

      '<div class="row row--between items-center mt-4 small muted">' +
        '<span>🔥 Current streak: <b>' + streak.current + ' days</b></span>' +
        '<div class="row items-center gap-1">' +
          '<span>Less</span>' +
          '<div class="dash-cal-cell" data-lvl="0"></div>' +
          '<div class="dash-cal-cell" data-lvl="1"></div>' +
          '<div class="dash-cal-cell" data-lvl="2"></div>' +
          '<div class="dash-cal-cell" data-lvl="3"></div>' +
          '<span>More</span>' +
        '</div>' +
      '</div>' +
    '</div>';
  }

  /* Recent Quiz Scores Card */
  function renderRecentQuizScoresCard(quiz) {
    var list = (quiz.attempts || []).slice(-5).reverse();

    if (!list.length) {
      return '<div class="dash-card-box">' +
        '<h3>🏆 Recent Quiz Scores</h3>' +
        '<p class="muted small mt-1">Your recent quiz report cards will appear here.</p>' +
        '<div class="p-5 text-center text-muted">' +
          'No quiz scores recorded yet.<br>' +
          '<a class="btn btn--primary btn--sm mt-3" href="#/quiz">Play Your First Quiz Challenge</a>' +
        '</div>' +
      '</div>';
    }

    return '<div class="dash-card-box">' +
      '<div class="row row--between items-center">' +
        '<div>' +
          '<h3>🏆 Recent Quiz Scores</h3>' +
          '<p class="muted small mt-1">Click any score to see the full question review.</p>' +
        '</div>' +
        '<a class="small" href="#/quiz">Quiz Arena →</a>' +
      '</div>' +

      '<div class="dash-recent-list mt-3">' +
        list.map(function (a) {
          var p = app.pct(a.correct, a.total);
          var dt = new Date(a.at);
          var dateStr = dt.toLocaleDateString(undefined, { month: "short", day: "numeric" });
          var chip = p >= 85 ? "chip--ok" : p >= 70 ? "chip--accent" : p >= 50 ? "chip--warn" : "chip--danger";

          return '<a class="dash-recent-row" href="#/quiz/attempt/' + encodeURIComponent(a.id) + '">' +
            '<div>' +
              '<b class="dash-recent-title">' + app.esc(a.label || "Animal Genetics Quiz") + '</b>' +
              '<div class="dash-recent-sub">' + dateStr + ' · ' + a.correct + '/' + a.total + ' correct (' + p + '%)' + (a.exam ? ' · ⏱️ Timed' : '') + '</div>' +
            '</div>' +
            '<span class="chip ' + chip + '">' + p + '%</span>' +
          '</a>';
        }).join("") +
      '</div>' +
    '</div>';
  }

  /* Knowledge Vault */
  function renderKnowledgeVault(totalHl, notesCount, bmsCount, qaCount) {
    return '<div class="vault-grid mt-4">' +
      vaultCard("#/library", "⭐", bmsCount, "Bookmarked Topics", "Quick access to favorite lessons", "gold") +
      vaultCard("#/library", "📝", notesCount, "Personal Notes", "Your own study summaries", "blue") +
      vaultCard("#/library", "🖍️", totalHl, "Highlighted Passages", "Important textbook sentences", "pink") +
      vaultCard("#/qa", "💬", qaCount, "Exam Q&As Reviewed", "Practiced past exam answers", "green") +
    '</div>';
  }

  function vaultCard(href, emoji, val, title, sub, color) {
    return '<a class="dash-vault-card dash-vault-card--' + color + '" href="' + href + '">' +
      '<div class="dash-vault-card__icon">' + emoji + '</div>' +
      '<div class="dash-vault-card__val">' + val + '</div>' +
      '<div class="dash-vault-card__title">' + title + '</div>' +
      '<div class="dash-vault-card__sub">' + sub + '</div>' +
    '</a>';
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

  function attachDashboardEvents(host, allUnits, readMap, quiz) {
    var filterBtns = host.querySelectorAll(".matrix-tab-btn");
    var container = host.querySelector("#unit-matrix-container");

    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        activeFilter = btn.getAttribute("data-filter") || "all";
        if (container) container.innerHTML = renderUnitReportCards(activeFilter, allUnits, readMap, quiz);
      });
    });
  }

  return {
    render: render
  };
})();
