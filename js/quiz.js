/* ============================================================
   quiz.js  —  The Animal Genetics and Breeding Quiz Engine
   ------------------------------------------------------------
   Features:
     - Curriculum-standard questions across Units 1 to 3
     - Strict 2 : 1 : 1 weighting (MCQ : TF : FIB)
     - Modular thematic sub-sections with dedicated module testing
     - Sequence Mode (curriculum order) vs Shuffle Mode (randomised)
     - Live feedback, keyboard shortcuts, flagging and streak awards
     - Timed exam simulation with auto-submission
     - Crash/refresh-safe: an unfinished paper can always be resumed
     - Spaced repetition (Leitner) grading on every question
     - A full post-paper analysis: pace, difficulty, format and
       sub-section mastery, a focus plan, and a filterable
       question-by-question review that is also replayable later
       from the dashboard (#/quiz/attempt/<id>).
   ============================================================ */

var quizApp = (function () {

  var host;                 // container element
  var run = null;           // active run state
  var reviewState = null;   // filter state for the analysis screen

  /* Sub-section metadata for Units 1 to 3 */
  var subSectionsByUnit = {
    "unit-1": [
      { id: "u1-s1", icon: "📊", title: "Data Classification, Central Tendency & Dispersion", desc: "Classification, tabulation, mean, median, mode, variance, standard deviation & CV" },
      { id: "u1-s2", icon: "🎲", title: "Probability & Distributions", desc: "Elementary probability, Binomial, Poisson and Normal distributions" },
      { id: "u1-s3", icon: "📈", title: "Correlation, Regression & Sampling", desc: "Pearson/Spearman correlation, regression equations, random & stratified sampling" },
      { id: "u1-s4", icon: "🧪", title: "Hypothesis Testing & Experimental Designs", desc: "Z-test, t-test, Chi-square test, ANOVA, CRD and RBD experimental designs" },
      { id: "u1-s5", icon: "💻", title: "Computer Applications & Data Analysis", desc: "Programming languages, DBMS and statistical analysis in MS-Excel" }
    ],
    "unit-2": [
      { id: "u2-s1", icon: "🧬", title: "Mendelian Genetics & Gene Interactions", desc: "Segregation, independent assortment, modified ratios, lethal genes and epistasis" },
      { id: "u2-s2", icon: "🔬", title: "Cytogenetics, Linkage & Sex Linkage", desc: "Mitosis/meiosis, karyotyping, sex determination, sex linkage, crossing over & aberrations" },
      { id: "u2-s3", icon: "🧪", title: "Molecular Genetics & Techniques", desc: "DNA/RNA structure, replication, gene concept, PCR, RFLP and sequencing" },
      { id: "u2-s4", icon: "🌐", title: "Population Genetics & Hardy-Weinberg Law", desc: "Gene/genotypic frequencies, Hardy-Weinberg equilibrium, mutation, migration, drift & selection" },
      { id: "u2-s5", icon: "📐", title: "Quantitative Genetics & Parameters", desc: "Breeding value, variance components, GxE interaction, heritability, repeatability & correlations" }
    ],
    "unit-3": [
      { id: "u3-s1", icon: "🎯", title: "Economic Traits & Selection Methods", desc: "Livestock/poultry traits, selection bases (pedigree, progeny, family) & selection index" },
      { id: "u3-s2", icon: "🔄", title: "Mating Systems, Inbreeding & Heterosis", desc: "Inbreeding coefficient, outbreeding, crossbreeding, hybrid vigour & combining ability" },
      { id: "u3-s3", icon: "🐄", title: "Livestock & Poultry Breeding Strategies", desc: "Breeding dairy cattle, buffalo, sheep, goat, swine, poultry & sire evaluation" },
      { id: "u3-s4", icon: "📜", title: "Breeding Policies & Genetic Conservation", desc: "National/state breeding programmes, ONBS, AnGR conservation & biotechnology tools" },
      { id: "u3-s5", icon: "🐾", title: "Pet, Zoo & Wild Animal Breeding", desc: "Dog, cat and pet bird breeding, wildlife effective population size (Ne) & conservation" }
    ]
  };

  var FORMAT_LABEL = { mcq: "Multiple Choice", tf: "True / False", fib: "Fill in the Blank" };
  var FORMAT_SHORT = { mcq: "MCQ", tf: "T/F", fib: "FIB" };
  var FORMAT_ICON = { mcq: "🔘", tf: "⚖️", fib: "✍️" };
  var DIFF_LABEL = { 1: "Foundational", 2: "Core UG", 3: "Rank 1 Classic" };
  var DIFF_STARS = { 1: "⭐", 2: "⭐⭐", 3: "⭐⭐⭐" };

  function getSubSectionMeta(unitId, subId) {
    if (!subId || subId === "all") return null;
    var list = subSectionsByUnit[unitId] || [];
    for (var i = 0; i < list.length; i++) {
      if (list[i].id === subId) return list[i];
    }
    // A paper spans several units, so fall back to a search across all of them.
    for (var u in subSectionsByUnit) {
      var arr = subSectionsByUnit[u];
      for (var j = 0; j < arr.length; j++) if (arr[j].id === subId) return arr[j];
    }
    return null;
  }

  function subSectionCount() {
    var n = 0;
    for (var u in subSectionsByUnit) n += subSectionsByUnit[u].length;
    return n;
  }

  /* ============================================================
     TEARDOWN — timers and key handlers must never outlive the run
     ============================================================ */
  function teardown() {
    if (run) {
      if (run.timer) { clearInterval(run.timer); run.timer = null; }
      if (run._keyHandler) {
        window.removeEventListener("keydown", run._keyHandler);
        run._keyHandler = null;
      }
    }
  }

  function resetRun() {
    teardown();
    run = null;
  }

  /* Leaving the quiz section entirely: stop the clock, drop the key
     bindings, but keep the paper on disk so it can be resumed. */
  function leave() {
    if (run && run.active) snapshot();
    teardown();
    run = null;
    reviewState = null;
  }

  /* ============================================================
     BUILDING A QUESTION SET
     ============================================================ */

  /* The written bank leans heavily on one option position, which lets a
     student guess by position instead of by knowledge. Every attempt
     re-orders the choices and moves the answer index with them.
     Purely numeric choices are sorted ascending instead — a jumbled list
     of numbers reads as a mistake. */
  function orderOptions(options, answerIndex) {
    if (!Array.isArray(options) || options.length < 2) {
      return { o: options, a: answerIndex };
    }
    if (typeof answerIndex !== "number" || !options[answerIndex]) {
      return { o: options, a: answerIndex };
    }

    var correct = options[answerIndex];
    var allNumeric = options.every(function (opt) {
      return String(opt).trim() !== "" && isFinite(String(opt).trim().replace(/,/g, ""));
    });

    var ordered;
    if (allNumeric) {
      ordered = options.slice(0).sort(function (x, y) {
        return parseFloat(String(x).replace(/,/g, "")) - parseFloat(String(y).replace(/,/g, ""));
      });
    } else {
      ordered = shuffle(options);
    }

    var newIndex = ordered.indexOf(correct);
    // Duplicate option texts would resolve to the wrong slot; leave those untouched.
    if (newIndex === -1 || ordered.filter(function (t) { return t === correct; }).length > 1) {
      return { o: options, a: answerIndex };
    }
    return { o: ordered, a: newIndex };
  }

  function bankFor(unitIds, formats, subSectionId) {
    var out = [];
    unitIds.forEach(function (uid) {
      var b = (window.quizBank || {})[uid];
      if (!b) return;
      formats.forEach(function (f) {
        (b[f] || []).forEach(function (q, i) {
          if (!q.q || !String(q.q).trim()) return;   // skip empty template rows
          if (subSectionId && subSectionId !== "all" && q.subSection !== subSectionId) return;
          var placed = f === "mcq" ? orderOptions(q.o, q.a) : { o: q.o, a: q.a };
          out.push({
            key: uid + ":" + f + ":" + i,
            format: f,
            unitId: uid,
            subSection: q.subSection || null,
            q: q.q,
            o: placed.o,
            a: placed.a,
            a_display: q.a_display || (Array.isArray(q.a) ? q.a[0] : q.a),
            e: q.e,
            topicId: q.topicId || null,
            diff: q.diff || 1
          });
        });
      });
    });
    return out;
  }

  /* Resolve the written question behind a stored answer key, so a paper
     taken weeks ago can still show its wording and explanation. */
  function bankQuestionByKey(key) {
    var parts = String(key || "").split(":");
    if (parts.length < 3) return null;
    var bucket = ((window.quizBank || {})[parts[0]] || {})[parts[1]];
    if (!bucket) return null;
    var q = bucket[parseInt(parts[2], 10)];
    return q && q.q ? q : null;
  }

  function scopeUnits(kind, id) {
    if (kind === "unit") return [id];
    if (kind === "paper") {
      var p = syllabus.meta.papers.filter(function (x) { return x.id === id; })[0];
      return p ? p.units.map(function (n) { return "unit-" + n; }) : [];
    }
    if (kind === "grand") return syllabus.theory.map(function (u) { return u.id; });
    if (kind === "practical") return syllabus.practical.map(function (u) { return u.id; });
    return [];
  }

  /* Paper labels are derived from the syllabus, never written by hand —
     the hard-coded one claimed Paper I held "Units 1, 2, 3". */
  function paperUnitLabel(paperId) {
    var p = (syllabus.meta.papers || []).filter(function (x) { return x.id === paperId; })[0];
    if (!p || !p.units || !p.units.length) return "";
    return (p.units.length === 1 ? "Unit " : "Units ") + p.units.join(", ");
  }

  function shuffle(a) {
    var copy = a.slice(0);
    for (var i = copy.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = copy[i]; copy[i] = copy[j]; copy[j] = t;
    }
    return copy;
  }

  /* The bank is stored format by format (all MCQs, then all T/F, then all
     FIB), so simply taking the first N gave a paper of nothing but MCQs.
     Take a share of each selected format instead, keeping the syllabus
     2 : 1 : 1 weighting, then restore curriculum order for Sequence Mode. */
  function pickBalanced(pool, count, orderMode, formats) {
    var wanted = (formats && formats.length ? formats : ["mcq", "tf", "fib"]);
    var weights = { mcq: 2, tf: 1, fib: 1 };

    var buckets = {};
    wanted.forEach(function (f) {
      buckets[f] = pool.filter(function (q) { return q.format === f; });
      if (orderMode === "shuffle") buckets[f] = shuffle(buckets[f]);
    });

    var present = wanted.filter(function (f) { return buckets[f].length; });
    if (!present.length) return [];

    var totalWeight = present.reduce(function (n, f) { return n + weights[f]; }, 0);

    var picked = [];
    present.forEach(function (f) {
      var share = Math.round(count * (weights[f] / totalWeight));
      picked = picked.concat(buckets[f].slice(0, Math.min(share, buckets[f].length)));
    });

    // Rounding, or a format running dry, can leave the paper short — top it
    // up from whatever questions are still unused.
    if (picked.length < count) {
      var used = {};
      picked.forEach(function (q) { used[q.key] = true; });
      var spare = [];
      present.forEach(function (f) {
        spare = spare.concat(buckets[f].filter(function (q) { return !used[q.key]; }));
      });
      if (orderMode === "shuffle") spare = shuffle(spare);
      picked = picked.concat(spare.slice(0, count - picked.length));
    }

    picked = picked.slice(0, count);

    if (orderMode === "shuffle") return shuffle(picked);

    // Sequence mode: hand them back in the order the bank lists them.
    var rank = {};
    pool.forEach(function (q, idx) { rank[q.key] = idx; });
    return picked.sort(function (x, y) { return rank[x.key] - rank[y.key]; });
  }

  function countAvailable(unitIds, subSectionId) {
    return bankFor(unitIds, ["mcq", "tf", "fib"], subSectionId).length;
  }

  function bankFormatCounts() {
    var ids = syllabus.allUnits.map(function (u) { return u.id; });
    var counts = { mcq: 0, tf: 0, fib: 0, total: 0 };
    bankFor(ids, ["mcq", "tf", "fib"]).forEach(function (q) {
      counts[q.format]++; counts.total++;
    });
    return counts;
  }

  /* ============================================================
     ROUTER ENTRY POINT
     ============================================================ */
  function render(container, params) {
    host = container;
    var kind = params.a;

    // Returning to #/quiz while a paper is open puts you back in the paper.
    // Asking for a different screen abandons it — but it is snapshotted, so
    // the hub always offers it back.
    if (run && run.active) {
      if (!kind) { paintRun(); return; }
      leave();
    }

    if (!kind) { renderHub(); return; }
    if (kind === "unit")      { renderSetup("unit", params.b); return; }
    if (kind === "paper")     { renderSetup("paper", params.b); return; }
    if (kind === "grand")     { renderSetup("grand", null); return; }
    if (kind === "practical") { renderSetup("practical", null); return; }
    if (kind === "review")    { renderReview(); return; }
    if (kind === "resume")    { resumeSaved(); return; }
    if (kind === "attempt")   { renderStoredAttempt(params.b); return; }
    renderHub();
  }

  /* ============================================================
     HUB
     ============================================================ */
  function renderHub() {
    resetRun();

    var theoryIds = syllabus.theory.map(function (u) { return u.id; });
    var pracIds = syllabus.practical.map(function (u) { return u.id; });
    var counts = bankFormatCounts();
    var totalAll = counts.total;
    var due = store.dueSrs().length;
    var q = store.getQuiz();
    var saved = store.getQuizResume();

    var unitRows = syllabus.theory.map(function (u) {
      var n = countAvailable([u.id]);
      var rec = q.byUnit["unit:" + u.id];
      var subList = subSectionsByUnit[u.id] || [];
      return '<a class="tlist__row' + (n ? '' : ' is-empty') + '" href="' +
        (n ? '#/quiz/unit/' + u.id : '#/quiz') + '">' +
        '<span class="tlist__no">U' + u.no + '</span>' +
        '<span class="tlist__body"><span class="tlist__title">' + app.esc(u.short) + '</span>' +
        '<span class="tlist__sub">' +
          (n ? '<b>' + n + ' questions</b> · ' + subList.length + ' modular sub-sections' : 'No questions added yet') +
        '</span></span>' +
        '<span class="tlist__right">' +
          (rec ? '<span class="chip ' + scoreChip(rec.best) + '">Best ' + rec.best + '%</span>' : '') +
          (n ? app.icon("chevron", "faint") : '') +
        '</span></a>';
    }).join("");

    var pracRows = syllabus.practical.map(function (u) {
      var n = countAvailable([u.id]);
      return '<a class="tlist__row' + (n ? '' : ' is-empty') + '" href="' +
        (n ? '#/quiz/unit/' + u.id : '#/quiz') + '">' +
        '<span class="tlist__no">P' + u.no + '</span>' +
        '<span class="tlist__body"><span class="tlist__title">' + app.esc(u.short) + '</span>' +
        '<span class="tlist__sub">' + (n ? n + ' questions' : 'No questions added yet') + '</span></span>' +
        '<span class="tlist__right">' + (n ? app.icon("chevron", "faint") : '') + '</span></a>';
    }).join("");

    var resumeCard = "";
    if (saved) {
      var answeredN = (saved.answers || []).filter(hasAnswer).length;
      resumeCard =
        '<div class="qz-resume">' +
          '<div class="qz-resume__body">' +
            '<span class="chip chip--warn">' + app.icon("clock") + ' Unfinished paper</span>' +
            '<h3 class="mt-2">' + app.esc(saved.label || "Animal Genetics Quiz") + '</h3>' +
            '<p class="small muted mt-1">' + answeredN + ' of ' + saved.qs.length +
            ' answered · saved ' + relTime(saved.savedAt) + '. Pick up exactly where you stopped.</p>' +
          '</div>' +
          '<div class="qz-resume__actions">' +
            '<a class="btn btn--primary" href="#/quiz/resume">Resume paper</a>' +
            '<button class="btn btn--ghost btn--sm" id="discardresume" type="button">Discard</button>' +
          '</div>' +
        '</div>';
    }

    var ratioNote = counts.total
      ? counts.mcq + ' MCQ · ' + counts.tf + ' True/False · ' + counts.fib + ' Fill-in-the-blank'
      : '';

    host.innerHTML =
      '<div class="pagehead quiz-hub-head">' +
        '<div class="row row--wrap items-center gap-2 mb-2">' +
          '<span class="chip chip--accent font-mono">🌟 ' + totalAll + ' question bank</span>' +
          (ratioNote ? '<span class="chip chip--ok">' + ratioNote + '</span>' : '') +
          '<span class="chip">' + subSectionCount() + ' sub-sections</span>' +
        '</div>' +
        '<h1>' + app.icon("quiz") + ' Animal Genetics Examination Suite</h1>' +
        '<p class="lede">Test individual sub-sections, full units, paper-wise or grand exams. ' +
        'Choose <b>Sequence Mode</b> (curriculum order) or <b>Shuffle Mode</b> (randomised), with instant feedback, ' +
        'a timed exam simulator and a full post-paper analysis.</p>' +
      '</div>' +

      resumeCard +

      (totalAll === 0
        ? '<div class="empty"><div class="empty__icon">' + app.icon("quiz") + '</div><h3>The question bank is empty</h3>' +
          '<p>Add questions in <b>data/data-quiz.JS</b>.</p></div>'
        : '') +

      '<h2 class="mt-8 flex items-center gap-2"><span>🎯</span> Comprehensive mock tests</h2>' +
      '<div class="grid grid--3 mt-4">' +
        modeCard("Paper I", "Biostatistics & Animal Genetics (" + paperUnitLabel("paper-1") + ")", countAvailable(scopeUnits("paper", "paper-1")), "#/quiz/paper/paper-1", false, "theory") +
        modeCard("Paper II", "Principles of Animal Breeding (" + paperUnitLabel("paper-2") + ")", countAvailable(scopeUnits("paper", "paper-2")), "#/quiz/paper/paper-2", false, "theory") +
        modeCard("Grand test", "All three theory units", countAvailable(theoryIds), "#/quiz/grand", false, "trophy") +
        modeCard("Practical", "All three practical units", countAvailable(pracIds), "#/quiz/practical", false, "practical") +
        modeCard("Smart Review", due + " question" + (due === 1 ? "" : "s") + " due today", due, "#/quiz/review", true, "repeat") +
      '</div>' +

      '<h2 class="mt-12 flex items-center gap-2"><span>📚</span> Theory units with modular sub-sections</h2>' +
      '<p class="small muted">Open any unit to practise a specific sub-section or the whole unit, in Sequence or Shuffle mode.</p>' +
      '<div class="tlist mt-4">' + unitRows + '</div>' +

      '<h2 class="mt-12 flex items-center gap-2"><span>🔬</span> Practical diagnostic units</h2>' +
      '<div class="tlist mt-4">' + pracRows + '</div>' +

      renderRecentResults(q);

    var discard = document.getElementById("discardresume");
    if (discard) {
      discard.addEventListener("click", function () {
        store.clearQuizResume();
        app.toast("Unfinished paper discarded");
        renderHub();
      });
    }
  }

  function scoreChip(p) {
    return p >= 85 ? "chip--ok" : p >= 70 ? "chip--accent" : p >= 50 ? "chip--warn" : "chip--danger";
  }

  /* A short ledger on the hub so the last few papers — and their full
     analysis — are one click away instead of buried in the dashboard. */
  function renderRecentResults(q) {
    var list = (q.attempts || []).slice(-6).reverse();
    if (!list.length) return "";

    return '<h2 class="mt-12 flex items-center gap-2"><span>📊</span> Recent results</h2>' +
      '<p class="small muted">Open any paper to re-read its full analysis and question-by-question review.</p>' +
      '<div class="tlist mt-4">' +
        list.map(function (a) {
          var p = app.pct(a.correct, a.total);
          return '<a class="tlist__row" href="#/quiz/attempt/' + encodeURIComponent(a.id) + '">' +
            '<span class="tlist__no">' + p + '%</span>' +
            '<span class="tlist__body">' +
              '<span class="tlist__title">' + app.esc(a.label || "Animal Genetics Quiz") + '</span>' +
              '<span class="tlist__sub">' + fullDate(a.at) + ' · ' + a.correct + '/' + a.total + ' correct' +
                (a.exam ? ' · ⏱️ timed' : '') +
                (a.skipped ? ' · ' + a.skipped + ' skipped' : '') +
              '</span>' +
            '</span>' +
            '<span class="tlist__right"><span class="chip ' + scoreChip(p) + '">' + a.correct + '/' + a.total + '</span>' +
            app.icon("chevron", "faint") + '</span>' +
          '</a>';
        }).join("") +
      '</div>';
  }

  function modeCard(title, sub, n, href, isReview, ico) {
    var disabled = !n;
    var iconHtml = ico ? app.icon(ico) : (isReview ? app.icon("repeat") : app.icon("quiz"));
    return '<a class="card card--link modecard' + (disabled ? ' is-disabled' : '') + '" href="' +
      (disabled ? '#/quiz' : href) + '">' +
      '<div class="row"><span class="card__title" style="display:flex;align-items:center;gap:6px;">' + iconHtml + ' ' + title + '</span>' +
      '<span class="chip push' + (n ? ' chip--accent' : '') + '">' + n + '</span></div>' +
      '<p class="card__desc">' + sub + '</p>' +
      (disabled ? '<p class="small faint mt-2">' +
        (isReview ? 'Nothing due — answer some questions first.' : 'No questions added yet.') + '</p>' : '') +
      '</a>';
  }

  /* ============================================================
     SETUP SCREEN WITH SUB-SECTION PICKER & SEQUENCE/SHUFFLE TOGGLE
     ============================================================ */
  function renderSetup(kind, id) {
    resetRun();
    var unitIds = scopeUnits(kind, id);
    var subSections = (kind === "unit" && subSectionsByUnit[id]) ? subSectionsByUnit[id] : [];

    var unitMeta = syllabus.unitById[id] || {};
    var label = kind === "unit"
      ? (unitMeta.stream === "practical" ? "Practical Unit " : "Unit ") + unitMeta.no + " — " + (unitMeta.short || "")
      : kind === "paper"
        ? (id === "paper-1" ? "Paper I" : "Paper II") + " — " + paperUnitLabel(id)
        : kind === "grand" ? "Grand Test — All Theory Units" : "Practical Units";

    if (!unitIds.length || !countAvailable(unitIds)) {
      host.innerHTML =
        '<div class="pagehead"><a class="btn btn--sm btn--ghost" href="#/quiz">← Quiz Hub</a>' +
        '<h1 class="mt-3">' + app.esc(label) + '</h1></div>' +
        '<div class="empty"><div class="empty__icon">' + app.icon("quiz") + '</div>' +
        '<h3>No questions written for this scope yet</h3>' +
        '<p>Add them in <b>data/data-quiz.JS</b> and they will appear here automatically.</p>' +
        '<a class="btn btn--primary mt-4" href="#/quiz">Back to the quiz hub</a></div>';
      return;
    }

    var prefs = store.getQuizPrefs() || {};
    var state = {
      subSectionId: "all",
      orderMode: prefs.orderMode === "shuffle" ? "shuffle" : "sequence",
      formats: Array.isArray(prefs.formats) && prefs.formats.length ? prefs.formats.slice(0) : ["mcq", "tf", "fib"],
      count: typeof prefs.count === "number" ? prefs.count : 20,
      exam: !!prefs.exam,
      minutes: typeof prefs.minutes === "number" ? prefs.minutes : 20
    };

    function savePrefs() {
      store.setQuizPrefs({
        orderMode: state.orderMode, formats: state.formats,
        count: state.count, exam: state.exam, minutes: state.minutes
      });
    }

    function updateView() {
      var pool = bankFor(unitIds, state.formats, state.subSectionId);
      var allPool = bankFor(unitIds, ["mcq", "tf", "fib"], state.subSectionId);

      var counts = { mcq: 0, tf: 0, fib: 0 };
      allPool.forEach(function (q) { counts[q.format]++; });
      var maxN = pool.length;

      var presets = [10, 20, 30, 45, 90, maxN].filter(function (n, idx, arr) {
        return n <= maxN && arr.indexOf(n) === idx;
      });
      if (!presets.length) presets = [maxN];
      if (state.count > maxN || presets.indexOf(state.count) === -1) {
        state.count = presets[Math.min(1, presets.length - 1)] || maxN;
      }

      var subSecHtml = "";
      if (subSections.length > 0) {
        var allCount = bankFor(unitIds, ["mcq", "tf", "fib"], "all").length;
        subSecHtml =
          '<div class="setup__row subsec-selector-row">' +
            '<div>' +
              '<b class="flex items-center gap-2"><span>📂</span> Choose sub-section / module</b>' +
              '<p class="small muted">Target a specific topic or practise all sub-sections in the unit.</p>' +
            '</div>' +
            '<div class="subsec-grid mt-3">' +
              '<button type="button" class="subsec-card' + (state.subSectionId === 'all' ? ' is-active' : '') + '" data-sub="all">' +
                '<div class="subsec-card__head">' +
                  '<span class="subsec-card__icon">🌟</span>' +
                  '<span class="subsec-card__title">All sub-sections (full unit)</span>' +
                  '<span class="chip chip--accent subsec-card__badge">' + allCount + ' Qs</span>' +
                '</div>' +
                '<p class="subsec-card__desc">Complete unit test covering all topics in the 2 : 1 : 1 exam ratio.</p>' +
              '</button>' +
              subSections.map(function (sub) {
                var c = bankFor(unitIds, ["mcq", "tf", "fib"], sub.id).length;
                var active = state.subSectionId === sub.id ? ' is-active' : '';
                return '<button type="button" class="subsec-card' + active + (c ? '' : ' is-disabled') + '" data-sub="' + sub.id + '"' + (c ? '' : ' disabled') + '>' +
                  '<div class="subsec-card__head">' +
                    '<span class="subsec-card__icon">' + sub.icon + '</span>' +
                    '<span class="subsec-card__title">' + app.esc(sub.title) + '</span>' +
                    '<span class="chip subsec-card__badge">' + c + ' Qs</span>' +
                  '</div>' +
                  '<p class="subsec-card__desc">' + app.esc(sub.desc) + '</p>' +
                '</button>';
              }).join("") +
            '</div>' +
          '</div>';
      }

      var currentSubMeta = getSubSectionMeta(id, state.subSectionId);
      var subHeadingBadge = currentSubMeta
        ? '<span class="chip chip--accent">' + currentSubMeta.icon + ' ' + app.esc(currentSubMeta.title) + '</span>'
        : (subSections.length
            ? '<span class="chip chip--accent">🌟 All ' + subSections.length + ' sub-sections</span>'
            : '');

      host.innerHTML =
        '<div class="pagehead">' +
          '<div class="row row--wrap items-center gap-2 mb-2">' +
            '<a class="btn btn--sm btn--ghost" href="#/quiz">← Quiz Hub</a>' +
            subHeadingBadge +
            '<span class="chip font-mono">' + maxN + ' available questions</span>' +
          '</div>' +
          '<h1>' + app.esc(label) + '</h1>' +
          '<p class="lede">Configure your test below — question count, format filters, order and exam timing.</p>' +
        '</div>' +

        '<div class="card setup quiz-setup-card">' +
          subSecHtml +

          /* Order Mode Toggle (Sequence vs Shuffle) */
          '<div class="setup__row">' +
            '<div>' +
              '<b class="flex items-center gap-2"><span>🔄</span> Question order mode</b>' +
              '<p class="small muted">Attempt questions in syllabus order, or shuffle them randomly.</p>' +
            '</div>' +
            '<div class="quiz-mode-toggle" id="ordermodetoggle">' +
              '<button type="button" class="toggle-pill' + (state.orderMode === 'sequence' ? ' is-selected' : '') + '" data-mode="sequence">' +
                '<span class="pill-icon">📋</span>' +
                '<span class="pill-label">Sequence Mode</span>' +
                '<span class="pill-sub">Curriculum order</span>' +
              '</button>' +
              '<button type="button" class="toggle-pill' + (state.orderMode === 'shuffle' ? ' is-selected' : '') + '" data-mode="shuffle">' +
                '<span class="pill-icon">🔀</span>' +
                '<span class="pill-label">Shuffle Mode</span>' +
                '<span class="pill-sub">Randomised order</span>' +
              '</button>' +
            '</div>' +
          '</div>' +

          /* Format selection */
          '<div class="setup__row">' +
            '<div>' +
              '<b>Question formats (2 : 1 : 1 ratio)</b>' +
              '<p class="small muted">Select any combination of question types.</p>' +
            '</div>' +
            '<div class="row row--wrap gap-3" id="fmtbox">' +
              ['mcq', 'tf', 'fib'].map(function (f) {
                var count = counts[f];
                var checked = state.formats.indexOf(f) !== -1 && count > 0;
                return '<label class="check-pill' + (checked ? ' is-checked' : '') + (count === 0 ? ' is-disabled' : '') + '">' +
                  '<input type="checkbox" data-fmt="' + f + '"' + (checked ? ' checked' : '') + (count === 0 ? ' disabled' : '') + '> ' +
                  '<span class="check-pill__icon">' + FORMAT_ICON[f] + '</span>' +
                  '<span class="check-pill__label">' + FORMAT_LABEL[f] + '</span>' +
                  '<span class="chip chip--sm ml-1">' + count + '</span>' +
                '</label>';
              }).join("") +
            '</div>' +
          '</div>' +

          /* Question count */
          '<div class="setup__row">' +
            '<div>' +
              '<b>Number of questions</b>' +
              '<p class="small muted">Choose your practice length.</p>' +
            '</div>' +
            '<div class="seg" id="segcount">' +
              presets.map(function (n) {
                var isSelected = state.count === n;
                return '<button type="button" class="seg__btn' + (isSelected ? ' is-on' : '') + '" data-count="' + n + '">' +
                  (n === maxN ? 'All (' + n + ')' : n) +
                '</button>';
              }).join("") +
            '</div>' +
          '</div>' +

          /* Exam Mode Toggle */
          '<div class="setup__row">' +
            '<div>' +
              '<b>⏱️ Exam mode (timed)</b>' +
              '<p class="small muted">Timed paper with no answer reveals until final submission — mirrors the annual university exam.</p>' +
            '</div>' +
            '<label class="switch"><input type="checkbox" id="exammode"' + (state.exam ? ' checked' : '') + '><span></span></label>' +
          '</div>' +

          /* Time Limit selector */
          '<div class="setup__row" id="timerow"' + (state.exam ? '' : ' hidden') + '>' +
            '<div>' +
              '<b>Time limit</b>' +
              '<p class="small muted">Automatic submission when the clock reaches zero.</p>' +
            '</div>' +
            '<div class="seg" id="segtime">' +
              [10, 20, 30, 45, 60].map(function (m) {
                return '<button type="button" class="seg__btn' + (state.minutes === m ? ' is-on' : '') + '" data-min="' + m + '">' + m + ' min</button>';
              }).join("") +
            '</div>' +
          '</div>' +

          /* Action Bar */
          '<div class="row mt-8 items-center row--wrap">' +
            '<a class="btn btn--ghost" href="#/quiz">Cancel</a>' +
            '<div class="push"></div>' +
            '<button class="btn btn--primary btn--lg" id="startbtn">' +
              '🚀 Start quiz (' + Math.min(state.count, maxN) + ' questions)' +
            '</button>' +
          '</div>' +
        '</div>';

      attachEvents();
    }

    function attachEvents() {
      document.querySelectorAll(".subsec-card").forEach(function (card) {
        card.addEventListener("click", function () {
          state.subSectionId = card.getAttribute("data-sub");
          updateView();
        });
      });

      document.querySelectorAll("#ordermodetoggle .toggle-pill").forEach(function (btn) {
        btn.addEventListener("click", function () {
          state.orderMode = btn.getAttribute("data-mode");
          savePrefs();
          updateView();
        });
      });

      document.querySelectorAll("[data-fmt]").forEach(function (chk) {
        chk.addEventListener("change", function () {
          var checkedFmts = Array.prototype.slice.call(document.querySelectorAll("[data-fmt]"))
            .filter(function (c) { return c.checked; })
            .map(function (c) { return c.getAttribute("data-fmt"); });
          if (!checkedFmts.length) {
            app.toast("Select at least one question format");
            chk.checked = true;
            return;
          }
          state.formats = checkedFmts;
          savePrefs();
          updateView();
        });
      });

      document.querySelectorAll("#segcount .seg__btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
          state.count = parseInt(btn.getAttribute("data-count"), 10);
          savePrefs();
          document.querySelectorAll("#segcount .seg__btn").forEach(function (b) { b.classList.remove("is-on"); });
          btn.classList.add("is-on");
          var startBtn = document.getElementById("startbtn");
          if (startBtn) startBtn.textContent = '🚀 Start quiz (' + state.count + ' questions)';
        });
      });

      var examChk = document.getElementById("exammode");
      if (examChk) {
        examChk.addEventListener("change", function (e) {
          state.exam = e.target.checked;
          savePrefs();
          var tRow = document.getElementById("timerow");
          if (tRow) tRow.hidden = !e.target.checked;
        });
      }

      document.querySelectorAll("#segtime .seg__btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
          state.minutes = parseInt(btn.getAttribute("data-min"), 10);
          savePrefs();
          document.querySelectorAll("#segtime .seg__btn").forEach(function (b) { b.classList.remove("is-on"); });
          btn.classList.add("is-on");
        });
      });

      var startBtn = document.getElementById("startbtn");
      if (startBtn) {
        startBtn.addEventListener("click", function () {
          var rawPool = bankFor(unitIds, state.formats, state.subSectionId);
          if (!rawPool.length) {
            app.toast("No questions available for this selection");
            return;
          }

          var finalQuestions = pickBalanced(rawPool, state.count, state.orderMode, state.formats);
          var runLabel = label;
          var subMeta = getSubSectionMeta(id, state.subSectionId);
          if (subMeta) runLabel = subMeta.icon + " " + subMeta.title;

          savePrefs();
          start({
            questions: finalQuestions,
            scope: kind + (id ? ":" + id : "") + (state.subSectionId !== "all" ? ":" + state.subSectionId : ""),
            label: runLabel,
            exam: state.exam,
            minutes: state.minutes,
            orderMode: state.orderMode,
            subSectionId: state.subSectionId,
            unitId: id,
            retryOf: null
          });
        });
      }
    }

    updateView();
  }

  /* ============================================================
     SMART REVIEW (spaced repetition queue)
     ============================================================ */
  function renderReview() {
    resetRun();
    var dueKeys = store.dueSrs();
    var all = bankFor(syllabus.allUnits.map(function (u) { return u.id; }), ["mcq", "tf", "fib"]);
    var pool = all.filter(function (q) { return dueKeys.indexOf(q.key) !== -1; });

    if (!pool.length) {
      host.innerHTML =
        '<div class="pagehead"><span class="eyebrow">Spaced repetition</span><h1>Smart Review</h1></div>' +
        '<div class="empty"><div class="empty__icon">✅</div><h3>Nothing due right now</h3>' +
        '<p>Questions you answer wrongly come back tomorrow, then after 2, 4, 8 and 16 days ' +
        'as you keep getting them right. Take a quiz first and this queue will fill itself.</p>' +
        '<a class="btn btn--primary mt-4" href="#/quiz">Go to the quiz hub</a></div>';
      return;
    }

    start({
      questions: shuffle(pool),
      scope: "review",
      label: "Smart Review",
      exam: false,
      minutes: 0,
      orderMode: "shuffle",
      subSectionId: "all",
      unitId: null
    });
  }

  /* ============================================================
     RUNNING A QUIZ
     ============================================================ */
  function start(cfg) {
    teardown();
    var questions = cfg.questions || [];
    run = {
      active: true,
      qs: questions,
      i: 0,
      answers: new Array(questions.length).fill(null),
      // Feedback and SRS grading are per question, never one flag for the
      // whole run — that was what made answered questions look unattempted
      // after stepping back through them.
      checked: new Array(questions.length).fill(false),
      graded: new Array(questions.length).fill(false),
      flags: new Array(questions.length).fill(false),
      times: new Array(questions.length).fill(0),
      near: new Array(questions.length).fill(false),
      scope: cfg.scope,
      label: cfg.label,
      orderMode: cfg.orderMode || "sequence",
      subSectionId: cfg.subSectionId || "all",
      unitId: cfg.unitId || (questions[0] ? questions[0].unitId : null),
      exam: !!cfg.exam,
      endsAt: cfg.exam ? Date.now() + (cfg.minutes || 20) * 60000 : 0,
      minutes: cfg.minutes || 0,
      startedAt: cfg.startedAt || Date.now(),
      retryOf: cfg.retryOf || null,
      timer: null,
      streak: 0,
      bestStreak: 0,
      tickAt: Date.now()
    };
    startTimer();
    paintRun();
  }

  function startTimer() {
    if (!run || !run.exam) return;
    run.timer = setInterval(function () {
      if (!run || !run.active) { teardown(); return; }
      if (Date.now() >= run.endsAt) { finish(true); return; }
      var t = document.getElementById("qtimer");
      if (t) {
        t.textContent = fmtTime(run.endsAt - Date.now());
        if (run.endsAt - Date.now() < 60000) t.classList.add("is-critical");
      }
    }, 1000);
  }

  /* ---------- resume support ---------- */
  function snapshot() {
    if (!run || !run.active) return;
    accrueTime();
    try {
      store.setQuizResume({
        qs: run.qs, i: run.i, answers: run.answers, checked: run.checked,
        graded: run.graded, flags: run.flags, times: run.times, near: run.near,
        scope: run.scope, label: run.label, orderMode: run.orderMode,
        subSectionId: run.subSectionId, unitId: run.unitId,
        exam: run.exam, endsAt: run.endsAt, minutes: run.minutes,
        startedAt: run.startedAt, retryOf: run.retryOf,
        bestStreak: run.bestStreak, savedAt: Date.now()
      });
    } catch (e) { /* storage full — the paper simply will not be resumable */ }
  }

  function resumeSaved() {
    var s = store.getQuizResume();
    if (!s) { renderHub(); return; }
    teardown();
    run = {
      active: true,
      qs: s.qs, i: s.i || 0,
      answers: s.answers || new Array(s.qs.length).fill(null),
      checked: s.checked || new Array(s.qs.length).fill(false),
      graded: s.graded || new Array(s.qs.length).fill(false),
      flags: s.flags || new Array(s.qs.length).fill(false),
      times: s.times || new Array(s.qs.length).fill(0),
      near: s.near || new Array(s.qs.length).fill(false),
      scope: s.scope, label: s.label, orderMode: s.orderMode,
      subSectionId: s.subSectionId, unitId: s.unitId,
      exam: !!s.exam, endsAt: s.endsAt || 0, minutes: s.minutes || 0,
      startedAt: s.startedAt || Date.now(), retryOf: s.retryOf || null,
      timer: null, streak: 0, bestStreak: s.bestStreak || 0,
      tickAt: Date.now()
    };
    // A timed paper whose clock ran out while the app was closed is over.
    if (run.exam && run.endsAt && Date.now() >= run.endsAt) { finish(true); return; }
    startTimer();
    app.toast("Paper resumed at question " + (run.i + 1));
    paintRun();
  }

  /* An answer counts as given for 0 (option A) and for False, so test the
     empty cases explicitly instead of relying on truthiness. */
  function hasAnswer(v) {
    if (v === null || v === undefined) return false;
    if (typeof v === "string") return v.trim() !== "";
    return true;
  }

  function answeredCount() {
    return run.answers.filter(hasAnswer).length;
  }

  /* Time is charged to whichever question was on screen. */
  function accrueTime() {
    if (!run) return;
    var now = Date.now();
    var delta = now - (run.tickAt || now);
    // Ignore an absurd gap — the tab was in the background, not being read.
    if (delta > 0 && delta < 10 * 60000) run.times[run.i] = (run.times[run.i] || 0) + delta;
    run.tickAt = now;
  }

  /* Grade into spaced repetition once per question per run. */
  function gradeOnce(idx) {
    if (run.graded[idx]) return;
    run.graded[idx] = true;
    store.gradeSrs(run.qs[idx].key, isCorrect(run.qs[idx], run.answers[idx]));
  }

  function goTo(idx) {
    if (idx < 0 || idx >= run.qs.length) return;
    accrueTime();
    run.i = idx;
    snapshot();
    paintRun();
  }

  function fmtTime(ms) {
    var s = Math.max(0, Math.floor(ms / 1000));
    return String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
  }

  function fmtDuration(ms) {
    var s = Math.max(0, Math.round(ms / 1000));
    if (s < 60) return s + "s";
    var m = Math.floor(s / 60);
    var r = s % 60;
    if (m < 60) return m + "m " + (r ? r + "s" : "").trim();
    return Math.floor(m / 60) + "h " + (m % 60) + "m";
  }

  function relTime(ts) {
    if (!ts) return "just now";
    var d = Date.now() - ts;
    if (d < 60000) return "moments ago";
    if (d < 3600000) return Math.round(d / 60000) + " min ago";
    if (d < 86400000) return Math.round(d / 3600000) + " h ago";
    return Math.round(d / 86400000) + " d ago";
  }

  function fullDate(ts) {
    var dt = new Date(ts);
    return dt.toLocaleDateString(undefined, { month: "short", day: "numeric" }) + " · " +
      dt.toLocaleTimeString(undefined, { hour: "2-digit", minute: "2-digit" });
  }

  /* Option letters must not run out past D. */
  function optKey(i) {
    return String.fromCharCode(65 + i);
  }

  function paintRun() {
    if (!run || !run.active) return;
    var q = run.qs[run.i];
    var given = run.answers[run.i];
    // Practice mode reveals as soon as this question is answered, and keeps
    // showing that result whenever you come back to it. Exam mode reveals
    // nothing until the paper is submitted.
    var showFeedback = !run.exam && run.checked[run.i];

    var body;
    if (q.format === "mcq") {
      body = '<div class="opts">' + (q.o || []).map(function (opt, i) {
        var cls = "opt";
        if (given === i) cls += " is-picked";
        if (showFeedback) {
          if (i === q.a) cls += " is-right";
          else if (given === i) cls += " is-wrong";
        }
        return '<button type="button" class="' + cls + '" data-pick="' + i + '"' + (showFeedback ? ' disabled' : '') + '>' +
          '<span class="opt__key">' + optKey(i) + '</span>' +
          '<span class="opt__text">' + app.esc(opt) + '</span>' +
          (showFeedback && i === q.a ? '<span class="opt__state">✓</span>' : '') +
          (showFeedback && given === i && i !== q.a ? '<span class="opt__state">✗</span>' : '') +
        '</button>';
      }).join("") + '</div>';

    } else if (q.format === "tf") {
      body = '<div class="opts opts--2">' + [true, false].map(function (v) {
        var cls = "opt opt--tf";
        if (given === v) cls += " is-picked";
        if (showFeedback) {
          if (v === q.a) cls += " is-right";
          else if (given === v) cls += " is-wrong";
        }
        return '<button type="button" class="' + cls + '" data-pick="' + v + '"' + (showFeedback ? ' disabled' : '') + '>' +
          '<span class="opt__key">' + (v ? "T" : "F") + '</span>' +
          '<span class="opt__text">' + (v ? "True" : "False") + '</span>' +
          (showFeedback && v === q.a ? '<span class="opt__state">✓</span>' : '') +
          (showFeedback && given === v && v !== q.a ? '<span class="opt__state">✗</span>' : '') +
        '</button>';
      }).join("") + '</div>';

    } else {
      var fibOk = showFeedback && isCorrect(q, given);
      body = '<div class="fib-card">' +
        '<div class="fib-input-wrap">' +
          '<input type="text" id="fibinput" class="fib-input" placeholder="Type your answer here…" autocomplete="off" autocorrect="off" spellcheck="false" ' +
          'value="' + app.esc(given !== null && given !== undefined ? String(given) : "") + '"' + (showFeedback ? ' disabled' : '') + '>' +
          (!showFeedback
            ? '<button type="button" class="btn btn--primary" id="fibsubmit">Submit</button>'
            : '') +
        '</div>' +
        (showFeedback
          ? '<div class="fib-accepted-callout ' + (fibOk ? 'is-ok' : 'is-error') + '">' +
              '<span class="badge">' + (fibOk ? '✓ Correct' : '✗ Incorrect') + '</span>' +
              '<span class="label"><b>Standard answer:</b> ' + app.esc(displayAnswer(q)) + '</span>' +
              (fibOk && run.near[run.i] ? '<span class="label small faint">Accepted with a spelling slip — write it exactly in the exam.</span>' : '') +
            '</div>'
          : '<p class="small faint mt-2">Spelling slips are forgiven, but write the exact term in the exam.</p>') +
        '</div>';
    }

    var answered = answeredCount();
    var flaggedN = run.flags.filter(Boolean).length;

    // Exam-hall style question palette: see at a glance what is answered,
    // flagged or still blank, and jump straight to anything you want.
    var palette = '<div class="qpalette mt-3">' + run.qs.map(function (item, idx) {
      var cls = "qpalette__dot";
      if (idx === run.i) cls += " is-current";
      if (hasAnswer(run.answers[idx])) {
        cls += " is-done";
        if (!run.exam && run.checked[idx]) {
          cls += isCorrect(item, run.answers[idx]) ? " is-right" : " is-wrong";
        }
      }
      if (run.flags[idx]) cls += " is-flagged";
      return '<button type="button" class="' + cls + '" data-goto="' + idx + '" ' +
        'aria-label="Question ' + (idx + 1) + (run.flags[idx] ? ', flagged' : '') + '">' + (idx + 1) + '</button>';
    }).join("") + '</div>';

    var subMeta = getSubSectionMeta(q.unitId, q.subSection);
    var subBadge = subMeta
      ? '<span class="chip chip--accent"><span class="qicon">' + subMeta.icon + '</span> ' + app.esc(subMeta.title) + '</span>'
      : '';

    var diffBadge = '<span class="chip ' + (q.diff === 3 ? 'chip--warn' : 'chip--subtle') + '">' +
      (DIFF_STARS[q.diff] || "⭐") + ' ' + (DIFF_LABEL[q.diff] || "Foundational") + '</span>';

    var orderBadge = run.orderMode === "sequence"
      ? '<span class="chip chip--subtle">📋 Sequence</span>'
      : '<span class="chip chip--subtle">🔀 Shuffle</span>';

    host.innerHTML =
      '<div class="quizrun animate-fade-in">' +
        '<div class="quizrun__bar">' +
          '<button class="btn btn--sm btn--ghost" id="quitbtn">Quit</button>' +
          '<span class="chip font-medium">' + app.esc(run.label) + '</span>' +
          orderBadge +
          '<div class="push"></div>' +
          (run.streak >= 2 ? '<span class="chip chip--accent streak-badge">🔥 Streak ' + run.streak + '</span>' : '') +
          (run.exam ? '<span class="chip chip--warn font-mono" id="qtimer">' + fmtTime(run.endsAt - Date.now()) + '</span>' : '') +
          '<span class="chip font-mono">' + (run.i + 1) + ' / ' + run.qs.length + '</span>' +
        '</div>' +

        '<div class="bar bar--lg mt-3"><div class="bar__fill" style="width:' +
          (((run.i + 1) / run.qs.length) * 100) + '%"></div></div>' +

        palette +

        '<div class="qpalette-legend small faint mt-2">' +
          '<span><i class="lg lg--done"></i> answered</span>' +
          '<span><i class="lg lg--flag"></i> flagged' + (flaggedN ? ' (' + flaggedN + ')' : '') + '</span>' +
          '<span><i class="lg lg--blank"></i> not attempted</span>' +
        '</div>' +

        '<div class="card quizcard mt-5">' +
          '<div class="quizcard__meta">' +
            '<span class="chip chip--accent font-bold">' + FORMAT_LABEL[q.format] + '</span>' +
            '<span class="chip">' + app.esc((syllabus.unitById[q.unitId] || {}).short || q.unitId) + '</span>' +
            subBadge +
            diffBadge +
            '<button type="button" class="flagbtn' + (run.flags[run.i] ? ' is-on' : '') + '" id="flagbtn" ' +
              'title="Flag this question to come back to it">' +
              '🚩 <span>' + (run.flags[run.i] ? 'Flagged' : 'Flag for review') + '</span>' +
            '</button>' +
          '</div>' +

          '<h2 class="quizcard__q mt-4">' + app.esc(q.q) + '</h2>' +

          body +

          (showFeedback && q.e
            ? '<div class="quiz-explanation-box mt-6 animate-scale-up ' + (isCorrect(q, given) ? 'is-correct' : 'is-wrong') + '">' +
                '<div class="quiz-explanation-box__head">' +
                  '<span>' + (isCorrect(q, given) ? '🎉 Correct' : '💡 Explanation & high-yield key note') + '</span>' +
                '</div>' +
                '<p class="quiz-explanation-box__body">' + q.e + '</p>' +
                (q.topicId && syllabus.topicById[q.topicId]
                  ? '<p class="small faint mt-2">Full lesson: <b>' + app.esc(syllabus.topicById[q.topicId].title) + '</b> — it is linked from your result analysis so you do not lose this paper.</p>'
                  : '') +
              '</div>'
            : '') +
        '</div>' +

        /* MCQ and True/False grade on the tap itself, so the only button
           needed here is the one that moves you on. Fill-in-the-blank still
           needs an explicit submit because typing has no natural end. */
        '<div class="row mt-6 items-center row--wrap">' +
          '<button class="btn" id="prevbtn"' + (run.i === 0 ? ' disabled' : '') + '>← Previous</button>' +
          '<div class="push"></div>' +
          '<span class="small faint mr-3">' + answered + ' of ' + run.qs.length + ' answered' +
            (flaggedN ? ' · ' + flaggedN + ' flagged' : '') + '</span>' +
          (run.i === run.qs.length - 1
            ? '<button class="btn btn--primary btn--lg" id="finishbtn">Finish &amp; see analysis 🏆</button>'
            : '<button class="btn btn--primary btn--lg" id="nextbtn">' +
                (hasAnswer(given) ? 'Next question →' : 'Skip for now →') + '</button>') +
        '</div>' +

        '<p class="small faint center mt-4">' +
          'Shortcuts: <kbd>1–9</kbd>/<kbd>A–D</kbd> answer · <kbd>T</kbd>/<kbd>F</kbd> true-false · ' +
          '<kbd>←</kbd> <kbd>→</kbd> move · <kbd>M</kbd> flag · <kbd>Enter</kbd> next' +
        '</p>' +
      '</div>';

    run.tickAt = Date.now();
    wireRun(q);
  }

  function displayAnswer(q) {
    if (q.format === "mcq") return (q.o || [])[q.a];
    if (q.format === "tf") return q.a ? "True" : "False";
    return q.a_display || (Array.isArray(q.a) ? q.a[0] : q.a);
  }

  function displayGiven(q, given) {
    if (!hasAnswer(given)) return null;
    if (q.format === "mcq") return (q.o || [])[given];
    if (q.format === "tf") return given ? "True" : "False";
    return String(given);
  }

  /* ---------- answer checking ---------- */

  /* Fill-in-the-blank is marked by meaning, not by keystrokes: case,
     spacing, accents, surrounding punctuation and a leading article are
     all ignored, and a single-character typo in a long term is accepted
     (and flagged as a spelling slip). */
  function normText(s) {
    var t = String(s == null ? "" : s).toLowerCase();
    // Strip accents where the browser supports it; older engines just skip it.
    if (t.normalize) t = t.normalize("NFD").replace(/[̀-ͯ]/g, "");
    return t;
  }

  function normFib(s) {
    var t = normText(s);
    t = t.replace(/[.,;:!?'"()\[\]]/g, " ");
    t = t.replace(/[‐-―]/g, "-");
    t = t.replace(/\s+/g, " ").trim();
    t = t.replace(/^(the|a|an)\s+/, "");
    return t;
  }

  function levenshtein(a, b) {
    if (a === b) return 0;
    if (!a.length) return b.length;
    if (!b.length) return a.length;
    var prev = [], cur = [], i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur[0] = i;
      for (j = 1; j <= b.length; j++) {
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      }
      for (j = 0; j <= b.length; j++) prev[j] = cur[j];
    }
    return prev[b.length];
  }

  function checkFib(q, given) {
    var mine = normFib(given);
    if (!mine) return { ok: false, near: false };
    var accepted = Array.isArray(q.a) ? q.a : [q.a];
    var near = false;
    for (var i = 0; i < accepted.length; i++) {
      var want = normFib(accepted[i]);
      if (!want) continue;
      if (mine === want) return { ok: true, near: false };
      // Same term, written solid vs hyphenated/spaced.
      if (mine.replace(/[\s-]/g, "") === want.replace(/[\s-]/g, "")) return { ok: true, near: false };
      // One-character typo in a term long enough for that to be unambiguous.
      if (want.length >= 5 && levenshtein(mine, want) <= 1) near = true;
    }
    return near ? { ok: true, near: true } : { ok: false, near: false };
  }

  function isCorrect(q, given) {
    if (!hasAnswer(given)) return false;
    if (q.format === "mcq") return given === q.a;
    if (q.format === "tf") return given === q.a;
    return checkFib(q, given).ok;
  }

  /* Reveal the answer for the current question, award streaks and file the
     result into spaced repetition. Practice mode only. */
  function revealCurrent(anchorEl) {
    if (run.exam || run.checked[run.i]) return;
    accrueTime();
    run.checked[run.i] = true;

    var q = run.qs[run.i];
    var ok = isCorrect(q, run.answers[run.i]);
    if (q.format === "fib" && ok) run.near[run.i] = checkFib(q, run.answers[run.i]).near;
    gradeOnce(run.i);

    if (ok) {
      run.streak = (run.streak || 0) + 1;
      if (run.streak > run.bestStreak) run.bestStreak = run.streak;
      if (app.burstConfetti && anchorEl) app.burstConfetti(anchorEl);
      if (run.streak === 3 && app.popMilestone) app.popMilestone("🔥 3 in a row!");
      else if (run.streak === 5 && app.popMilestone) app.popMilestone("🚀 5 streak — unstoppable!");
      else if (run.streak === 7 && app.popMilestone) app.popMilestone("⚡ 7 straight — pure genius!");
      else if (run.streak === 10 && app.popMilestone) app.popMilestone("👑 10 streak — Master Animal Geneticist!");
    } else {
      run.streak = 0;
    }
    snapshot();
  }

  function wireRun(q) {
    // One tap answers the question: it records the choice and, in practice
    // mode, grades it immediately. No second "check" tap.
    document.querySelectorAll("[data-pick]").forEach(function (b) {
      b.addEventListener("click", function () {
        if (!run.exam && run.checked[run.i]) return;   // already locked in
        var raw = b.getAttribute("data-pick");
        run.answers[run.i] = (q.format === "tf") ? (raw === "true") : parseInt(raw, 10);
        if (run.exam) { accrueTime(); snapshot(); }
        revealCurrent(b);
        paintRun();
      });
    });

    document.querySelectorAll("[data-goto]").forEach(function (b) {
      b.addEventListener("click", function () {
        goTo(parseInt(b.getAttribute("data-goto"), 10));
      });
    });

    var flagBtn = document.getElementById("flagbtn");
    if (flagBtn) {
      flagBtn.addEventListener("click", function () {
        run.flags[run.i] = !run.flags[run.i];
        snapshot();
        paintRun();
      });
    }

    var fib = document.getElementById("fibinput");
    if (fib) {
      if (!run.checked[run.i]) {
        setTimeout(function () { try { fib.focus(); } catch (e) {} }, 50);
      }
      fib.addEventListener("input", function () {
        run.answers[run.i] = fib.value;
      });
      fib.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
          e.preventDefault();
          run.answers[run.i] = fib.value;
          submitFib();
        }
      });
    }

    function submitFib() {
      if (!hasAnswer(run.answers[run.i])) {
        app.toast("Type your answer first");
        return;
      }
      if (run.exam || run.checked[run.i]) {
        accrueTime(); snapshot();
        advance();
        return;
      }
      revealCurrent(document.getElementById("fibsubmit"));
      paintRun();
    }

    var fibSubmit = document.getElementById("fibsubmit");
    if (fibSubmit) fibSubmit.addEventListener("click", submitFib);

    function advance() {
      if (run.i === run.qs.length - 1) confirmFinish();
      else goTo(run.i + 1);
    }

    var next = document.getElementById("nextbtn");
    if (next) next.addEventListener("click", function () {
      if (q.format === "fib") {
        var el = document.getElementById("fibinput");
        if (el) run.answers[run.i] = el.value;
      }
      goTo(run.i + 1);
    });

    var prev = document.getElementById("prevbtn");
    if (prev) prev.addEventListener("click", function () {
      if (q.format === "fib") {
        var el2 = document.getElementById("fibinput");
        if (el2) run.answers[run.i] = el2.value;
      }
      goTo(run.i - 1);
    });

    var fin = document.getElementById("finishbtn");
    if (fin) fin.addEventListener("click", function () {
      if (q.format === "fib") {
        var el3 = document.getElementById("fibinput");
        if (el3) run.answers[run.i] = el3.value;
      }
      confirmFinish();
    });

    var quit = document.getElementById("quitbtn");
    if (quit) quit.addEventListener("click", function () {
      if (confirm("Quit this paper?\n\nIt is saved, so you can resume it from the quiz hub. Nothing is scored until you finish.")) {
        snapshot();
        resetRun();
        location.hash = "#/quiz";
      }
    });

    // Global keyboard shortcuts
    function handleKey(e) {
      if (!run || !run.active) return;
      if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
      if (e.ctrlKey || e.metaKey || e.altKey) return;

      var cur = run.qs[run.i];
      var locked = !run.exam && run.checked[run.i];
      if (!locked) {
        if (cur.format === "mcq") {
          var n = -1;
          if (/^[1-9]$/.test(e.key)) n = parseInt(e.key, 10) - 1;
          else if (/^[a-zA-Z]$/.test(e.key)) n = e.key.toUpperCase().charCodeAt(0) - 65;
          if (n >= 0 && n < (cur.o || []).length) {
            e.preventDefault();
            run.answers[run.i] = n;
            if (run.exam) { accrueTime(); snapshot(); }
            revealCurrent(null);
            paintRun();
            return;
          }
        } else if (cur.format === "tf") {
          if (e.key === "t" || e.key === "T" || e.key === "1") {
            e.preventDefault();
            run.answers[run.i] = true;
            if (run.exam) { accrueTime(); snapshot(); }
            revealCurrent(null); paintRun(); return;
          }
          if (e.key === "f" || e.key === "F" || e.key === "2") {
            e.preventDefault();
            run.answers[run.i] = false;
            if (run.exam) { accrueTime(); snapshot(); }
            revealCurrent(null); paintRun(); return;
          }
        }
      }

      if (e.key === "m" || e.key === "M") {
        e.preventDefault();
        run.flags[run.i] = !run.flags[run.i];
        snapshot(); paintRun(); return;
      }
      if (e.key === "ArrowRight") { e.preventDefault(); goTo(run.i + 1); return; }
      if (e.key === "ArrowLeft") { e.preventDefault(); goTo(run.i - 1); return; }

      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        var cb = document.getElementById("nextbtn") || document.getElementById("finishbtn");
        if (cb) cb.click();
      }
    }

    if (run._keyHandler) window.removeEventListener("keydown", run._keyHandler);
    run._keyHandler = handleKey;
    window.addEventListener("keydown", run._keyHandler);
  }

  /* Never let a paper be handed in by accident with blanks on it. */
  function confirmFinish() {
    var blanks = run.qs.length - answeredCount();
    var flagged = run.flags.filter(Boolean).length;
    if (blanks || flagged) {
      var msg = "Submit this paper now?\n\n";
      if (blanks) msg += "• " + blanks + " question" + (blanks > 1 ? "s are" : " is") + " still unanswered\n";
      if (flagged) msg += "• " + flagged + " question" + (flagged > 1 ? "s are" : " is") + " flagged for review\n";
      msg += "\nUnanswered questions are marked wrong.";
      if (!confirm(msg)) {
        var firstBlank = -1;
        for (var i = 0; i < run.qs.length; i++) {
          if (!hasAnswer(run.answers[i])) { firstBlank = i; break; }
        }
        if (firstBlank === -1) firstBlank = run.flags.indexOf(true);
        if (firstBlank >= 0) goTo(firstBlank);
        return;
      }
    }
    finish(false);
  }

  /* ============================================================
     FINISHING — build the record, then hand it to the analysis view
     ============================================================ */
  function finish(timedOut) {
    if (!run) return;
    accrueTime();
    teardown();
    run.active = false;
    store.clearQuizResume();

    var correct = 0;
    var formatStats = { mcq: { total: 0, right: 0 }, tf: { total: 0, right: 0 }, fib: { total: 0, right: 0 } };
    var diffStats = { 1: { total: 0, right: 0 }, 2: { total: 0, right: 0 }, 3: { total: 0, right: 0 } };
    var subStats = {};
    var unitStats = {};
    var detail = [];
    var longest = 0, running = 0;

    run.qs.forEach(function (q, i) {
      var ok = isCorrect(q, run.answers[i]);
      var d = Math.min(3, Math.max(1, q.diff || 1));
      var sid = q.subSection || "unsorted";

      formatStats[q.format].total++;
      diffStats[d].total++;
      if (!subStats[sid]) subStats[sid] = { total: 0, right: 0, unitId: q.unitId };
      subStats[sid].total++;
      if (!unitStats[q.unitId]) unitStats[q.unitId] = { total: 0, right: 0 };
      unitStats[q.unitId].total++;

      if (ok) {
        correct++;
        formatStats[q.format].right++;
        diffStats[d].right++;
        subStats[sid].right++;
        unitStats[q.unitId].right++;
        running++;
        if (running > longest) longest = running;
      } else {
        running = 0;
      }

      detail.push({
        k: q.key, f: q.format, u: q.unitId, s: q.subSection || null, d: d,
        ok: ok, ms: Math.round(run.times[i] || 0),
        giv: displayGiven(q, run.answers[i]),
        ans: String(displayAnswer(q)),
        fl: !!run.flags[i],
        nr: !!run.near[i]
      });

      // Anything not graded during the run (exam answers, skipped questions)
      // is filed into spaced repetition now — exactly once each.
      gradeOnce(i);
    });

    var total = run.qs.length;
    var elapsedMs = Math.max(0, Date.now() - run.startedAt);
    var spentMs = run.times.reduce(function (n, t) { return n + (t || 0); }, 0);
    var seconds = Math.round((spentMs || elapsedMs) / 1000);
    var answeredTotal = answeredCount();

    var unitIds = [];
    run.qs.forEach(function (q) {
      if (q.unitId && unitIds.indexOf(q.unitId) === -1) unitIds.push(q.unitId);
    });

    var attempt = {
      at: Date.now(),
      scope: run.scope,
      label: run.label,
      total: total,
      correct: correct,
      attempted: answeredTotal,
      skipped: total - answeredTotal,
      exam: run.exam,
      seconds: seconds,
      minutes: Math.max(1, Math.round(seconds / 60)),
      limitMinutes: run.exam ? run.minutes : 0,
      unitIds: unitIds,
      subSectionId: run.subSectionId,
      orderMode: run.orderMode,
      timedOut: !!timedOut,
      bestStreak: Math.max(run.bestStreak || 0, longest),
      byFormat: formatStats,
      byDiff: diffStats,
      bySub: subStats,
      byUnit: unitStats,
      retryOf: run.retryOf || null,
      detail: detail
    };

    // Previous score for the same scope, captured before this one is filed.
    var prev = null;
    var history = store.getQuiz().attempts.filter(function (a) { return a.scope === attempt.scope; });
    if (history.length) prev = history[history.length - 1];

    var attemptId = store.saveAttempt(attempt);
    attempt.id = attemptId;

    // A timed paper can run out while the student is reading another tab.
    // The score is saved above either way; only skip drawing the result over
    // a screen that no longer belongs to the quiz.
    if (!host || !document.body.contains(host)) {
      if (timedOut && app.toast) app.toast("Time expired — your paper was submitted and saved");
      run = null;
      return;
    }

    var qsForReview = run.qs;
    run = null;
    paintAnalysis(attempt, { questions: qsForReview, prev: prev, live: true });
  }

  /* ============================================================
     OPENING A STORED PAPER (#/quiz/attempt/<id>)
     ============================================================ */
  function renderStoredAttempt(id) {
    resetRun();
    var attempt = id ? store.getAttempt(decodeURIComponent(id)) : null;
    if (!attempt) {
      host.innerHTML =
        '<div class="pagehead"><a class="btn btn--sm btn--ghost" href="#/quiz">← Quiz Hub</a>' +
        '<h1 class="mt-3">Paper not found</h1></div>' +
        '<div class="empty"><div class="empty__icon">' + app.icon("search") + '</div>' +
        '<h3>That result is no longer stored</h3>' +
        '<p>Only your most recent papers keep their full question-by-question detail.</p>' +
        '<a class="btn btn--primary mt-4" href="#/quiz">Back to the quiz hub</a></div>';
      return;
    }
    var all = store.getQuiz().attempts.filter(function (a) { return a.scope === attempt.scope; });
    var idx = -1;
    all.forEach(function (a, i) { if (String(a.id) === String(attempt.id)) idx = i; });
    var prev = idx > 0 ? all[idx - 1] : null;
    paintAnalysis(attempt, { prev: prev, live: false });
  }

  /* ============================================================
     THE ANALYSIS SCREEN
     ------------------------------------------------------------
     One renderer for a paper just finished and for a paper opened
     from history, so the review never degrades over time.
     ============================================================ */

  /* Normalise both sources into one shape the whole screen reads from. */
  function buildItems(attempt, liveQuestions) {
    if (liveQuestions && liveQuestions.length === (attempt.detail || []).length) {
      return liveQuestions.map(function (q, i) {
        var d = attempt.detail[i];
        return {
          n: i + 1, key: q.key, format: q.format, unitId: q.unitId,
          subSection: q.subSection, diff: d.d, q: q.q, e: q.e, topicId: q.topicId,
          ok: d.ok, ms: d.ms, given: d.giv, right: d.ans,
          skipped: d.giv === null || d.giv === undefined,
          flagged: d.fl, near: d.nr, options: q.o
        };
      });
    }
    return (attempt.detail || []).map(function (d, i) {
      var raw = bankQuestionByKey(d.k) || {};
      return {
        n: i + 1, key: d.k, format: d.f, unitId: d.u, subSection: d.s, diff: d.d,
        q: raw.q || "(this question is no longer in the bank)",
        e: raw.e, topicId: raw.topicId,
        ok: d.ok, ms: d.ms, given: d.giv, right: d.ans,
        skipped: d.giv === null || d.giv === undefined,
        flagged: d.fl, near: d.nr, options: null
      };
    });
  }

  function paintAnalysis(attempt, opts) {
    opts = opts || {};
    var items = buildItems(attempt, opts.questions);
    reviewState = { filter: "wrong", q: "", attempt: attempt, items: items, live: !!opts.live };
    // Nothing wrong? Open on the full paper instead of an empty list.
    if (!items.some(function (it) { return !it.ok; })) reviewState.filter = "all";

    var percent = app.pct(attempt.correct, attempt.total);
    var verdict = percent >= 85 ? "Rank 1 Distinction"
      : percent >= 70 ? "Strong First Class"
      : percent >= 50 ? "Passing Grade" : "Needs Revision";
    var chipCls = scoreChip(percent);

    var attempted = typeof attempt.attempted === "number" ? attempt.attempted : attempt.total;
    var skipped = attempt.skipped || 0;
    var attemptedAccuracy = attempted ? Math.round(attempt.correct / attempted * 100) : 0;
    var totalMs = (attempt.seconds || 0) * 1000;
    var avgMs = attempt.total ? totalMs / attempt.total : 0;

    var delta = null;
    if (opts.prev && opts.prev.total) {
      delta = percent - app.pct(opts.prev.correct, opts.prev.total);
    }

    host.innerHTML =
      '<div class="analysis animate-fade-in">' +

        (attempt.timedOut
          ? '<div class="callout mb-6"><div class="callout__title">Time expired</div>' +
            'Your paper was submitted automatically when the countdown reached zero.</div>' : '') +

        /* ---- 1. Verdict header ---- */
        '<div class="an-head">' +
          '<div class="an-head__ring">' + app.ringHtml(percent, 150) + '</div>' +
          '<div class="an-head__body">' +
            '<span class="dash-eyebrow">' + app.icon("target") + ' Paper analysis · ' + fullDate(attempt.at) + '</span>' +
            '<h1 class="mt-1">' + attempt.correct + ' out of ' + attempt.total + ' correct</h1>' +
            '<div class="row row--wrap gap-2 mt-3">' +
              '<span class="chip ' + chipCls + ' font-bold">' + verdict + '</span>' +
              '<span class="chip">' + app.esc(attempt.label || "Animal Genetics Quiz") + '</span>' +
              '<span class="chip chip--subtle">' + (attempt.orderMode === "shuffle" ? "🔀 Shuffle" : "📋 Sequence") + '</span>' +
              (attempt.exam ? '<span class="chip chip--subtle">⏱️ Exam mode' +
                (attempt.limitMinutes ? ' · ' + attempt.limitMinutes + ' min limit' : '') + '</span>' : '') +
              (delta !== null
                ? '<span class="chip ' + (delta > 0 ? 'chip--ok' : delta < 0 ? 'chip--danger' : 'chip--subtle') + '">' +
                  (delta > 0 ? '▲ +' : delta < 0 ? '▼ ' : '– ') + Math.abs(delta) + '% vs last attempt of this paper</span>'
                : '<span class="chip chip--subtle">First attempt of this paper</span>') +
            '</div>' +
            '<p class="muted small mt-3">' + verdictAdvice(percent, skipped, attempt) + '</p>' +
          '</div>' +
        '</div>' +

        /* ---- 2. Key metrics ---- */
        '<div class="an-metrics">' +
          metric("Accuracy", percent + "%", attempt.correct + " right · " + (attempt.total - attempt.correct) + " wrong") +
          metric("On attempted", attempted ? attemptedAccuracy + "%" : "—", attempted + " of " + attempt.total + " attempted") +
          metric("Left blank", String(skipped), skipped ? "Counted as wrong" : "Nothing skipped") +
          metric("Total time", fmtDuration(totalMs), attempt.exam && attempt.limitMinutes ? "of a " + attempt.limitMinutes + " min limit" : "actively on questions") +
          metric("Avg / question", fmtDuration(avgMs), paceVerdict(avgMs)) +
          metric("Best run", (attempt.bestStreak || 0) + " in a row", "Longest correct streak") +
        '</div>' +

        /* ---- 3. Format & difficulty ---- */
        '<section class="mt-10">' +
          '<h2>Where the marks went</h2>' +
          '<p class="muted small mt-1">The same paper cut three ways — by question format, by difficulty tier and by syllabus module.</p>' +
          '<div class="grid grid--2 mt-4">' +
            breakdownCard("By question format", ["mcq", "tf", "fib"].map(function (f) {
              var r = (attempt.byFormat || {})[f] || { total: 0, right: 0 };
              return { label: FORMAT_ICON[f] + " " + FORMAT_LABEL[f], right: r.right, total: r.total };
            })) +
            breakdownCard("By difficulty tier", [1, 2, 3].map(function (d) {
              var r = (attempt.byDiff || {})[d] || { total: 0, right: 0 };
              return { label: DIFF_STARS[d] + " " + DIFF_LABEL[d], right: r.right, total: r.total };
            })) +
          '</div>' +
        '</section>' +

        /* ---- 4. Sub-section mastery ---- */
        renderSubMastery(attempt) +

        /* ---- 5. Focus plan ---- */
        renderFocusPlan(attempt, items) +

        /* ---- 6. Pace analysis ---- */
        renderPaceCard(items) +

        /* ---- 7. Question-by-question review ---- */
        '<section class="mt-12" id="an-review">' +
          '<div class="row row--between">' +
            '<div>' +
              '<h2>Question-by-question review</h2>' +
              '<p class="muted small mt-1">Every question with your answer, the standard answer, the examiner\'s note and the time you spent.</p>' +
            '</div>' +
          '</div>' +
          '<div class="an-filterbar mt-4" id="an-filters"></div>' +
          '<div class="an-search mt-3">' +
            app.icon("search", "faint") +
            '<input type="text" id="an-search-input" placeholder="Search these questions…" autocomplete="off">' +
          '</div>' +
          '<div id="an-review-list" class="mt-4"></div>' +
        '</section>' +

        /* ---- 8. Actions ---- */
        '<div class="an-actions mt-12">' +
          (items.some(function (it) { return !it.ok; })
            ? '<button class="btn btn--primary btn--lg" id="an-retry-wrong">' + app.icon("repeat") +
              ' Retry the ' + items.filter(function (it) { return !it.ok; }).length + ' I missed</button>'
            : '') +
          '<button class="btn btn--lg" id="an-retake">' + app.icon("quiz") + ' Retake this paper</button>' +
          '<button class="btn btn--lg" id="an-copy">' + app.icon("copy") + ' Copy summary</button>' +
          '<a class="btn btn--lg" href="#/dashboard">' + app.icon("dashboard") + ' Dashboard</a>' +
          '<a class="btn btn--lg" href="#/quiz">' + app.icon("chevron") + ' Quiz hub</a>' +
        '</div>' +
      '</div>';

    paintReviewList();
    wireAnalysis(attempt, items);

    if (opts.live && percent >= 75 && app.burstConfetti) {
      setTimeout(function () {
        var ring = document.querySelector('.an-head__ring');
        if (ring) app.burstConfetti(ring);
        if (app.popMilestone) app.popMilestone("🏆 " + verdict + ": " + percent + "%!");
      }, 250);
    }
  }

  function metric(label, value, sub) {
    return '<div class="an-metric">' +
      '<div class="an-metric__lbl">' + label + '</div>' +
      '<div class="an-metric__val">' + app.esc(value) + '</div>' +
      '<div class="an-metric__sub">' + app.esc(sub) + '</div>' +
    '</div>';
  }

  function paceVerdict(avgMs) {
    if (!avgMs) return "—";
    var s = avgMs / 1000;
    if (s < 15) return "Very fast — check for guessing";
    if (s < 40) return "Good exam pace";
    if (s < 75) return "Thorough, a little slow";
    return "Too slow for a timed paper";
  }

  function verdictAdvice(percent, skipped, attempt) {
    if (percent >= 85) {
      return "Distinction-level command of this scope. Keep it warm through the spaced-repetition queue rather than re-reading whole units.";
    }
    if (percent >= 70) {
      return "A solid first class. The breakdown below names the two or three modules standing between you and a distinction.";
    }
    if (percent >= 50) {
      return "A pass, but the marks are uneven. Work through the weakest modules below before you attempt this paper again.";
    }
    return "This scope is not exam-ready yet. Read the lessons linked in the review below, then retry only the questions you missed." +
      (skipped ? " " + skipped + " question" + (skipped > 1 ? "s were" : " was") + " left blank — blanks score zero in the annual exam." : "");
  }

  function breakdownCard(title, rows) {
    var live = rows.filter(function (r) { return r.total > 0; });
    return '<div class="card an-card">' +
      '<h3 class="an-card__title">' + title + '</h3>' +
      (live.length
        ? '<div class="an-bars mt-3">' + live.map(function (r) {
            var p = r.total ? Math.round(r.right / r.total * 100) : 0;
            return '<div class="an-bar">' +
              '<div class="an-bar__head">' +
                '<span>' + r.label + '</span>' +
                '<span class="font-mono ' + (p >= 75 ? 'ok' : p >= 50 ? 'warn' : 'bad') + '">' + r.right + '/' + r.total + ' · ' + p + '%</span>' +
              '</div>' +
              '<div class="bar"><div class="bar__fill ' + barTone(p) + '" style="width:' + p + '%"></div></div>' +
            '</div>';
          }).join("") + '</div>'
        : '<p class="small faint mt-3">Not covered in this paper.</p>') +
    '</div>';
  }

  function barTone(p) {
    return p >= 75 ? "is-ok" : p >= 50 ? "is-warn" : "is-bad";
  }

  function renderSubMastery(attempt) {
    var subs = attempt.bySub || {};
    var rows = Object.keys(subs).map(function (sid) {
      var r = subs[sid];
      var meta = getSubSectionMeta(r.unitId, sid);
      return {
        id: sid,
        unitId: r.unitId,
        icon: meta ? meta.icon : "📘",
        title: meta ? meta.title : "Unsorted questions",
        right: r.right, total: r.total,
        pct: r.total ? Math.round(r.right / r.total * 100) : 0
      };
    }).filter(function (r) { return r.total > 0; })
      .sort(function (a, b) { return a.pct - b.pct || b.total - a.total; });

    if (!rows.length) return "";

    var unitRows = Object.keys(attempt.byUnit || {});
    var unitHtml = "";
    if (unitRows.length > 1) {
      unitHtml = '<div class="card an-card mt-4">' +
        '<h3 class="an-card__title">By unit</h3>' +
        '<div class="an-bars mt-3">' + unitRows.map(function (uid) {
          var r = attempt.byUnit[uid];
          var p = r.total ? Math.round(r.right / r.total * 100) : 0;
          var u = syllabus.unitById[uid] || {};
          return '<div class="an-bar">' +
            '<div class="an-bar__head">' +
              '<span>' + app.esc(u.short || uid) + '</span>' +
              '<span class="font-mono">' + r.right + '/' + r.total + ' · ' + p + '%</span>' +
            '</div>' +
            '<div class="bar"><div class="bar__fill ' + barTone(p) + '" style="width:' + p + '%"></div></div>' +
          '</div>';
        }).join("") + '</div>' +
      '</div>';
    }

    return '<section class="mt-10">' +
      '<h2>Sub-section mastery</h2>' +
      '<p class="muted small mt-1">Weakest module first. Each row links straight to the lesson and to a fresh test of that module alone.</p>' +
      '<div class="an-sub-list mt-4">' +
        rows.map(function (r) {
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
        }).join("") +
      '</div>' +
      unitHtml +
    '</section>';
  }

  /* The single most useful panel: what to do next, named explicitly. */
  function renderFocusPlan(attempt, items) {
    var subs = attempt.bySub || {};
    var weak = Object.keys(subs).map(function (sid) {
      var r = subs[sid];
      var meta = getSubSectionMeta(r.unitId, sid);
      return {
        id: sid, unitId: r.unitId,
        icon: meta ? meta.icon : "📘",
        title: meta ? meta.title : "Unsorted questions",
        right: r.right, total: r.total,
        pct: r.total ? Math.round(r.right / r.total * 100) : 0
      };
    }).filter(function (r) { return r.total >= 2 && r.pct < 75; })
      .sort(function (a, b) { return a.pct - b.pct; })
      .slice(0, 3);

    // Topics behind the wrong answers, so the plan can name lessons too.
    var topicTally = {};
    items.forEach(function (it) {
      if (it.ok || !it.topicId) return;
      topicTally[it.topicId] = (topicTally[it.topicId] || 0) + 1;
    });
    var topics = Object.keys(topicTally)
      .filter(function (tid) { return syllabus.topicById[tid]; })
      .sort(function (a, b) { return topicTally[b] - topicTally[a]; })
      .slice(0, 4);

    if (!weak.length && !topics.length) {
      return '<div class="callout mt-10"><div class="callout__title">🏆 No weak module in this paper</div>' +
        'Every sub-section came in at 75% or better. Keep this scope alive through the spaced-repetition queue and move on to the next unit.</div>';
    }

    return '<section class="mt-10">' +
      '<h2>Your focus plan</h2>' +
      '<p class="muted small mt-1">Built from this paper only — the shortest route from this score to the next grade band.</p>' +
      '<div class="an-plan mt-4">' +
        weak.map(function (r, i) {
          return '<div class="an-plan__step">' +
            '<span class="an-plan__num">' + (i + 1) + '</span>' +
            '<div class="an-plan__body">' +
              '<b>' + r.icon + ' ' + app.esc(r.title) + '</b>' +
              '<p class="small muted mt-1">Only ' + r.right + ' of ' + r.total + ' correct (' + r.pct + '%). ' +
              'Re-read this module, then retest it on its own before mixing it back into a full paper.</p>' +
            '</div>' +
            (r.unitId
              ? '<a class="btn btn--sm btn--primary" href="#/quiz/unit/' + r.unitId + '">Open module</a>'
              : '') +
          '</div>';
        }).join("") +
        (topics.length
          ? '<div class="an-plan__topics">' +
              '<b class="small">Lessons behind your wrong answers</b>' +
              '<div class="row row--wrap gap-2 mt-2">' +
                topics.map(function (tid) {
                  var t = syllabus.topicById[tid];
                  return '<a class="chip chip--accent" href="#/topic/' + tid + '">' + app.icon("book") + ' ' +
                    app.esc(t.title) + ' <b>(' + topicTally[tid] + ')</b></a>';
                }).join("") +
              '</div>' +
            '</div>'
          : '') +
      '</div>' +
    '</section>';
  }

  function renderPaceCard(items) {
    var timed = items.filter(function (it) { return it.ms > 0; });
    if (!timed.length) return "";

    var slowest = timed.slice(0).sort(function (a, b) { return b.ms - a.ms; }).slice(0, 3);
    var rushed = timed.filter(function (it) { return !it.ok && !it.skipped && it.ms < 12000; });
    var agonised = timed.filter(function (it) { return !it.ok && it.ms > 90000; });
    var avg = timed.reduce(function (n, it) { return n + it.ms; }, 0) / timed.length;

    var notes = [];
    if (rushed.length) {
      notes.push('<li><b>' + rushed.length + ' wrong in under 12 seconds.</b> Those are reflex answers, not recall — ' +
        'slow down and re-read the stem before choosing.</li>');
    }
    if (agonised.length) {
      notes.push('<li><b>' + agonised.length + ' wrong after more than 90 seconds.</b> Long deliberation that still ' +
        'misses means the underlying concept is missing, not the calculation. Go back to the lesson.</li>');
    }
    if (!notes.length) {
      notes.push('<li>Your timing is even across the paper — no rushed guesses and nothing you got stuck on.</li>');
    }

    return '<section class="mt-10">' +
      '<h2>Pace &amp; exam technique</h2>' +
      '<p class="muted small mt-1">How your time was spent, and what that says about how you are answering.</p>' +
      '<div class="grid grid--2 mt-4">' +
        '<div class="card an-card">' +
          '<h3 class="an-card__title">Time diagnosis</h3>' +
          '<p class="small muted mt-2">Average ' + fmtDuration(avg) + ' per question — ' + paceVerdict(avg).toLowerCase() + '.</p>' +
          '<ul class="an-notes mt-3">' + notes.join("") + '</ul>' +
        '</div>' +
        '<div class="card an-card">' +
          '<h3 class="an-card__title">Longest questions</h3>' +
          '<div class="an-bars mt-3">' +
            slowest.map(function (it) {
              var p = Math.min(100, Math.round(it.ms / slowest[0].ms * 100));
              return '<div class="an-bar">' +
                '<div class="an-bar__head">' +
                  '<span>Q' + it.n + ' · ' + (it.ok ? '<span class="ok">correct</span>' : '<span class="bad">missed</span>') + '</span>' +
                  '<span class="font-mono">' + fmtDuration(it.ms) + '</span>' +
                '</div>' +
                '<div class="bar"><div class="bar__fill ' + (it.ok ? 'is-ok' : 'is-bad') + '" style="width:' + p + '%"></div></div>' +
              '</div>';
            }).join("") +
          '</div>' +
        '</div>' +
      '</div>' +
    '</section>';
  }

  /* ---------- filterable question list ---------- */
  function filteredItems() {
    var s = reviewState;
    var q = (s.q || "").trim().toLowerCase();
    return s.items.filter(function (it) {
      if (s.filter === "wrong" && it.ok) return false;
      if (s.filter === "right" && !it.ok) return false;
      if (s.filter === "skipped" && !it.skipped) return false;
      if (s.filter === "flagged" && !it.flagged) return false;
      if (q) {
        var hay = (it.q + " " + (it.e || "") + " " + (it.right || "") + " " + (it.given || "")).toLowerCase();
        if (hay.indexOf(q) === -1) return false;
      }
      return true;
    });
  }

  function paintReviewList() {
    var s = reviewState;
    if (!s) return;

    var counts = {
      all: s.items.length,
      wrong: s.items.filter(function (i) { return !i.ok; }).length,
      skipped: s.items.filter(function (i) { return i.skipped; }).length,
      flagged: s.items.filter(function (i) { return i.flagged; }).length,
      right: s.items.filter(function (i) { return i.ok; }).length
    };

    var tabs = [
      { id: "wrong", label: "Incorrect", n: counts.wrong },
      { id: "skipped", label: "Skipped", n: counts.skipped },
      { id: "flagged", label: "Flagged", n: counts.flagged },
      { id: "right", label: "Correct", n: counts.right },
      { id: "all", label: "All questions", n: counts.all }
    ];

    var bar = document.getElementById("an-filters");
    if (bar) {
      bar.innerHTML = tabs.map(function (t) {
        return '<button type="button" class="an-filter' + (s.filter === t.id ? ' is-active' : '') +
          (t.n ? '' : ' is-empty') + '" data-filter="' + t.id + '">' +
          t.label + ' <span class="an-filter__n">' + t.n + '</span></button>';
      }).join("");
      bar.querySelectorAll("[data-filter]").forEach(function (b) {
        b.addEventListener("click", function () {
          s.filter = b.getAttribute("data-filter");
          paintReviewList();
        });
      });
    }

    var list = document.getElementById("an-review-list");
    if (!list) return;

    var rows = filteredItems();
    if (!rows.length) {
      list.innerHTML = '<div class="card p-5 text-center text-muted">' +
        (s.q ? 'No question in this paper matches “' + app.esc(s.q) + '”.'
             : 'Nothing in this category — which is good news.') + '</div>';
      return;
    }

    list.innerHTML = rows.map(function (it) {
      var unit = syllabus.unitById[it.unitId] || {};
      var subMeta = getSubSectionMeta(it.unitId, it.subSection);
      var stateCls = it.skipped ? "is-skipped" : it.ok ? "is-right" : "is-wrong";
      var stateLbl = it.skipped ? "Left blank" : it.ok ? "Correct" : "Incorrect";

      return '<article class="an-q ' + stateCls + '">' +
        '<div class="an-q__top">' +
          '<span class="an-q__n">Q' + it.n + '</span>' +
          '<span class="chip ' + (it.skipped ? 'chip--warn' : it.ok ? 'chip--ok' : 'chip--danger') + '">' + stateLbl + '</span>' +
          '<span class="chip chip--subtle font-mono">' + FORMAT_SHORT[it.format] + '</span>' +
          '<span class="chip chip--subtle">' + (DIFF_STARS[it.diff] || "⭐") + '</span>' +
          '<span class="chip chip--subtle">' + app.esc(unit.short || it.unitId) + '</span>' +
          (subMeta ? '<span class="chip chip--subtle">' + subMeta.icon + ' ' + app.esc(subMeta.title) + '</span>' : '') +
          (it.flagged ? '<span class="chip chip--warn">🚩 Flagged</span>' : '') +
          '<span class="push"></span>' +
          (it.ms ? '<span class="chip chip--subtle font-mono">' + app.icon("clock", "faint") + ' ' + fmtDuration(it.ms) + '</span>' : '') +
        '</div>' +

        '<p class="an-q__text">' + app.esc(it.q) + '</p>' +

        '<div class="an-q__answers">' +
          '<div class="an-ans ' + (it.ok ? 'is-ok' : 'is-bad') + '">' +
            '<span class="an-ans__lbl">Your answer</span>' +
            '<span class="an-ans__val">' + (it.skipped ? '<i class="faint">not answered</i>' : app.esc(String(it.given))) + '</span>' +
          '</div>' +
          '<div class="an-ans is-ok">' +
            '<span class="an-ans__lbl">Standard answer</span>' +
            '<span class="an-ans__val">' + app.esc(String(it.right)) + '</span>' +
          '</div>' +
        '</div>' +

        (it.near ? '<p class="small faint mt-2">Accepted despite a spelling slip — write it exactly in the written exam.</p>' : '') +

        (it.e
          ? '<div class="an-q__why"><b>Why:</b> ' + it.e + '</div>'
          : '') +

        (it.topicId && syllabus.topicById[it.topicId]
          ? '<a class="btn btn--sm btn--outline mt-3" href="#/topic/' + it.topicId + '">' + app.icon("book") +
            ' Read the lesson: ' + app.esc(syllabus.topicById[it.topicId].title) + '</a>'
          : '') +
      '</article>';
    }).join("");
  }

  function wireAnalysis(attempt, items) {
    var search = document.getElementById("an-search-input");
    if (search) {
      search.addEventListener("input", function () {
        reviewState.q = search.value;
        paintReviewList();
      });
    }

    var retryWrong = document.getElementById("an-retry-wrong");
    if (retryWrong) {
      retryWrong.addEventListener("click", function () {
        var keys = items.filter(function (it) { return !it.ok; }).map(function (it) { return it.key; });
        startFromKeys(keys, "Retry — " + (attempt.label || "missed questions"), attempt);
      });
    }

    var retake = document.getElementById("an-retake");
    if (retake) {
      retake.addEventListener("click", function () {
        var keys = items.map(function (it) { return it.key; });
        startFromKeys(keys, attempt.label, attempt, true);
      });
    }

    var copy = document.getElementById("an-copy");
    if (copy) {
      copy.addEventListener("click", function () {
        app.copyTextToClipboard(summaryText(attempt, items), "Result summary copied to clipboard");
      });
    }
  }

  /* Rebuild a paper from stored keys — used by "retry what I missed" and
     "retake this paper", including for a result opened from history. */
  function startFromKeys(keys, label, attempt, reshuffle) {
    var all = bankFor(syllabus.allUnits.map(function (u) { return u.id; }), ["mcq", "tf", "fib"]);
    var byKey = {};
    all.forEach(function (q) { byKey[q.key] = q; });

    var picked = keys.map(function (k) { return byKey[k]; }).filter(Boolean);
    if (!picked.length) {
      app.toast("Those questions are no longer in the bank");
      return;
    }
    if (reshuffle && attempt && attempt.orderMode === "shuffle") picked = shuffle(picked);

    start({
      questions: picked,
      scope: attempt ? attempt.scope : "retry",
      label: label || "Retry",
      exam: false,
      minutes: 0,
      orderMode: attempt ? attempt.orderMode : "sequence",
      subSectionId: attempt ? attempt.subSectionId : "all",
      unitId: attempt ? (attempt.unitIds || [])[0] : null,
      retryOf: attempt ? attempt.id : null
    });
    location.hash = "#/quiz";
    paintRun();
  }

  function summaryText(attempt, items) {
    var percent = app.pct(attempt.correct, attempt.total);
    var lines = [];
    lines.push("Animal Genetics and Breeding — " + (attempt.label || "Quiz"));
    lines.push(fullDate(attempt.at));
    lines.push("Score: " + attempt.correct + "/" + attempt.total + " (" + percent + "%)");
    lines.push("Attempted " + (attempt.attempted || 0) + " · skipped " + (attempt.skipped || 0) +
      " · time " + fmtDuration((attempt.seconds || 0) * 1000));
    lines.push("");
    lines.push("By format:");
    ["mcq", "tf", "fib"].forEach(function (f) {
      var r = (attempt.byFormat || {})[f];
      if (r && r.total) lines.push("  " + FORMAT_SHORT[f] + ": " + r.right + "/" + r.total);
    });
    var subs = attempt.bySub || {};
    var subKeys = Object.keys(subs);
    if (subKeys.length) {
      lines.push("");
      lines.push("By sub-section:");
      subKeys.forEach(function (sid) {
        var r = subs[sid];
        var meta = getSubSectionMeta(r.unitId, sid);
        lines.push("  " + (meta ? meta.title : sid) + ": " + r.right + "/" + r.total);
      });
    }
    var wrong = items.filter(function (it) { return !it.ok; });
    if (wrong.length) {
      lines.push("");
      lines.push("Missed (" + wrong.length + "):");
      wrong.forEach(function (it) {
        lines.push("  Q" + it.n + ". " + it.q);
        lines.push("     mine: " + (it.skipped ? "(blank)" : it.given) + " | answer: " + it.right);
      });
    }
    return lines.join("\n");
  }

  return {
    render: render,
    /* The dashboard names weak modules, so it needs this table too. */
    subSectionMeta: function (subId) { return getSubSectionMeta(null, subId); },
    subSectionsByUnit: subSectionsByUnit,
    reset: resetRun,
    leave: leave,
    teardown: teardown
  };
})();
