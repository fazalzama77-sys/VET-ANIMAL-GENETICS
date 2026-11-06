/* ============================================================
   quiz.js  —  The Animal Genetics and Breeding Quiz Engine
   ------------------------------------------------------------
   Features:
     - Interactive, playful, colorful and gamified Ed-Tech UI/UX
     - 100% Silent: zero irritating sound effects
     - Question Map Drawer: clean, non-cluttered slide-down navigator
     - Instant visual feedback: vibrant option highlights, micro-animations,
       confetti bursts, celebratory milestone badges
     - Curriculum-standard questions across Units 1 to 3
     - Strict 2 : 1 : 1 weighting (MCQ : TF : FIB)
     - Modular thematic sub-sections with dedicated module testing
     - Sequence Mode (curriculum order) vs Shuffle Mode (randomised)
     - Timed exam simulation with auto-submission
     - Crash/refresh-safe: unfinished papers can always be resumed
     - Spaced repetition (Leitner) grading on every question
     - Comprehensive post-paper analysis with 1-click retry of missed questions
   ============================================================ */

var quizApp = (function () {

  var host;                 // container element
  var run = null;           // active run state
  var reviewState = null;   // filter state for the analysis screen
  var mapDrawerOpen = false;// question map drawer toggle

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
  var FORMAT_ICON  = { mcq: "🔘", tf: "⚖️", fib: "✍️" };
  var DIFF_LABEL   = { 1: "Foundational", 2: "Core UG", 3: "Rank 1 Classic" };
  var DIFF_STARS   = { 1: "⭐", 2: "⭐⭐", 3: "⭐⭐⭐" };

  var EXAM_META = {
    id: "exam", icon: "🔥", title: "Exam Top 50 — High-Yield Questions",
    desc: "The hand-picked questions most likely to be asked in the annual exam, spread across the whole unit syllabus."
  };

  function getSubSectionMeta(unitId, subId) {
    if (!subId || subId === "all") return null;
    if (subId === "exam") return EXAM_META;
    var list = subSectionsByUnit[unitId] || [];
    for (var i = 0; i < list.length; i++) {
      if (list[i].id === subId) return list[i];
    }
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

  /* Teardown */
  function teardown() {
    if (run) {
      if (run.timer) { clearInterval(run.timer); run.timer = null; }
      if (run._keyHandler) {
        window.removeEventListener("keydown", run._keyHandler);
        run._keyHandler = null;
      }
    }
    mapDrawerOpen = false;
  }

  function resetRun() {
    teardown();
    run = null;
  }

  function leave() {
    if (run && run.active) snapshot();
    teardown();
    run = null;
    reviewState = null;
  }

  /* Option ordering */
  function orderOptions(options, answerIndex) {
    if (!Array.isArray(options) || options.length < 2) return { o: options, a: answerIndex };
    if (typeof answerIndex !== "number" || !options[answerIndex]) return { o: options, a: answerIndex };

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
          if (!q.q || !String(q.q).trim()) return;
          if (subSectionId === "exam") {
            if (!q.exam) return;
          } else if (subSectionId && subSectionId !== "all" && q.subSection !== subSectionId) return;
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
            diff: q.diff || 1,
            exam: !!q.exam
          });
        });
      });
    });
    return out;
  }

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
      var p = (syllabus.meta.papers || []).filter(function (x) { return x.id === id; })[0];
      return p ? p.units.map(function (n) { return "unit-" + n; }) : [];
    }
    if (kind === "grand") return syllabus.theory.map(function (u) { return u.id; });
    if (kind === "practical") return syllabus.practical.map(function (u) { return u.id; });
    return [];
  }

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

  /* Router entry point */
  function render(container, params) {
    host = container;
    var kind = params.a;

    if (run && run.active) {
      if (!kind) { paintRun(); return; }
      leave();
    }

    if (!kind) { renderHub(); return; }
    if (kind === "unit")      { renderSetup("unit", params.b); return; }
    if (kind === "paper")     { renderSetup("paper", params.b); return; }
    if (kind === "grand")     { renderSetup("grand", null, params.b === "exam"); return; }
    if (kind === "practical") { renderSetup("practical", null); return; }
    if (kind === "review")    { renderReview(); return; }
    if (kind === "resume")    { resumeSaved(); return; }
    if (kind === "attempt")   { renderStoredAttempt(params.b); return; }
    renderHub();
  }

  /* ============================================================
     QUIZ HUB — Playful, Colorful, Engaging Game Arena (Silent)
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
    var streak = store.computeStreak ? store.computeStreak() : { current: 0 };

    var resumeCard = "";
    if (saved) {
      var answeredN = (saved.answers || []).filter(hasAnswer).length;
      resumeCard =
        '<div class="qz-resume-card animate-scale-up">' +
          '<div class="qz-resume-card__icon">⏳</div>' +
          '<div class="qz-resume-card__body">' +
            '<div class="qz-resume-card__tag">UNFINISHED GAME IN PROGRESS</div>' +
            '<h3 class="qz-resume-card__title">' + app.esc(saved.label || "Animal Genetics Quiz") + '</h3>' +
            '<p class="qz-resume-card__meta">' + answeredN + ' of ' + saved.qs.length +
            ' answered · saved ' + relTime(saved.savedAt) + '. Jump right back in!</p>' +
          '</div>' +
          '<div class="qz-resume-card__actions">' +
            '<a class="btn btn--primary btn--play" href="#/quiz/resume">🚀 Resume Playing</a>' +
            '<button class="btn btn--ghost btn--sm" id="discardresume" type="button">Discard</button>' +
          '</div>' +
        '</div>';
    }

    var unitCardsHtml = syllabus.theory.map(function (u) {
      var n = countAvailable([u.id]);
      var rec = q.byUnit["unit:" + u.id];
      var bestScore = rec ? rec.best : null;
      var examN = countAvailable([u.id], "exam");
      var subList = subSectionsByUnit[u.id] || [];

      var unitThemes = {
        "unit-1": { gradient: "linear-gradient(135deg, #1565c0, #0288d1)", icon: "📊", name: "Biostatistics & Excel" },
        "unit-2": { gradient: "linear-gradient(135deg, #6a48b5, #8e24aa)", icon: "🧬", name: "Principles of Genetics" },
        "unit-3": { gradient: "linear-gradient(135deg, #00897b, #2e7d32)", icon: "🐄", name: "Animal Breeding" }
      };
      var theme = unitThemes[u.id] || { gradient: "linear-gradient(135deg, #1565c0, #00897b)", icon: "📘", name: u.short };

      return '<div class="qz-unit-card">' +
        '<div class="qz-unit-card__head" style="background:' + theme.gradient + '">' +
          '<span class="qz-unit-card__badge">Unit ' + u.no + '</span>' +
          '<span class="qz-unit-card__emoji">' + theme.icon + '</span>' +
        '</div>' +
        '<div class="qz-unit-card__body">' +
          '<h3 class="qz-unit-card__title">' + app.esc(u.short) + '</h3>' +
          '<p class="qz-unit-card__desc">' + subList.length + ' topic modules · ' + n + ' practice questions</p>' +
          '<div class="qz-unit-card__tags mt-3">' +
            '<span class="chip chip--sm chip--accent">' + n + ' Qs</span>' +
            (examN ? '<span class="chip chip--sm chip--warn">🔥 ' + examN + ' Exam Top</span>' : '') +
            (bestScore !== null ? '<span class="chip chip--sm ' + scoreChip(bestScore) + '">Best ' + bestScore + '%</span>' : '<span class="chip chip--sm chip--subtle">Untested</span>') +
          '</div>' +
        '</div>' +
        '<div class="qz-unit-card__foot">' +
          '<a class="btn btn--primary btn--play-unit" href="#/quiz/unit/' + u.id + '">Play Unit ' + u.no + ' →</a>' +
        '</div>' +
      '</div>';
    }).join("");

    host.innerHTML =
      '<div class="quiz-hub animate-fade-in">' +

        /* 1. Playful Gamified Hero Banner */
        '<div class="qz-hero-banner">' +
          '<div class="qz-hero-decor qz-hero-decor--1">🧬</div>' +
          '<div class="qz-hero-decor qz-hero-decor--2">⭐</div>' +
          '<div class="qz-hero-decor qz-hero-decor--3">🎯</div>' +
          '<div class="qz-hero-content">' +
            '<div class="qz-hero-pills">' +
              '<span class="qz-pill qz-pill--gold">🏆 Game Arena</span>' +
              '<span class="qz-pill qz-pill--cyan">⚡ ' + totalAll + ' Questions</span>' +
              '<span class="qz-pill qz-pill--flame">🔥 ' + streak.current + ' Day Streak</span>' +
            '</div>' +
            '<h1 class="qz-hero-title">Animal Genetics Quiz Arena</h1>' +
            '<p class="qz-hero-subtitle">Level up your veterinary knowledge with colorful challenges, instant feedback, and real exam simulations!</p>' +
          '</div>' +
        '</div>' +

        resumeCard +

        /* 2. Challenge Modes Grid */
        '<div class="qz-section-head mt-8">' +
          '<div class="qz-section-title"><span>🎮</span> Choose Your Challenge Mode</div>' +
          '<p class="qz-section-sub">Pick from full mock exams, rapid-fire exam questions, or smart spaced memory review.</p>' +
        '</div>' +

        '<div class="qz-modes-grid mt-4">' +
          modeGameCard("Grand Championship Mock", "All 3 theory units combined in full 2:1:1 official exam weighting.", countAvailable(theoryIds), "#/quiz/grand", "trophy", "gold", "⭐ Full Simulation") +
          modeGameCard("🔥 Exam Top 150 Rapid-Fire", "The highest-yield, most frequently tested questions for annual exams.", countAvailable(theoryIds, "exam"), "#/quiz/grand/exam", "flame", "coral", "🔥 High-Yield") +
          modeGameCard("Paper I Arena", "Biostatistics & Animal Genetics (" + paperUnitLabel("paper-1") + ").", countAvailable(scopeUnits("paper", "paper-1")), "#/quiz/paper/paper-1", "atom", "blue", "Paper I") +
          modeGameCard("Paper II Arena", "Principles of Animal Breeding (" + paperUnitLabel("paper-2") + ").", countAvailable(scopeUnits("paper", "paper-2")), "#/quiz/paper/paper-2", "flask", "emerald", "Paper II") +
          modeGameCard("Practical Diagnostics", "Numericals, karyotyping, selection index and Mendelian crosses.", countAvailable(pracIds), "#/quiz/practical", "lab", "purple", "Practical") +
          modeGameCard("Smart Memory Workout", due ? due + " cards due for spaced review right now!" : "Queue clear! All cards fresh.", due, "#/quiz/review", "repeat", "mint", "🧠 Memory Flash", !due) +
        '</div>' +

        /* 3. Unit-by-Unit Quest Arena */
        '<div class="qz-section-head mt-12">' +
          '<div class="qz-section-title"><span>📚</span> Unit Mastery Quests</div>' +
          '<p class="qz-section-sub">Target individual curriculum units or zoom into specific module sub-sections.</p>' +
        '</div>' +

        '<div class="qz-units-grid mt-4">' +
          unitCardsHtml +
        '</div>' +

        /* 4. Recent Results Hall of Fame */
        renderRecentResults(q) +

      '</div>';

    var discard = document.getElementById("discardresume");
    if (discard) {
      discard.addEventListener("click", function () {
        store.clearQuizResume();
        app.toast("Unfinished paper discarded");
        renderHub();
      });
    }
  }

  function modeGameCard(title, desc, n, href, ico, themeColor, badgeText, disabled) {
    return '<a class="qz-game-card qz-game-card--' + themeColor + (disabled ? ' is-disabled' : '') + '" href="' + (disabled ? '#/quiz' : href) + '">' +
      '<div class="qz-game-card__top">' +
        '<span class="qz-game-card__tag">' + badgeText + '</span>' +
        '<span class="qz-game-card__count">' + n + ' Qs</span>' +
      '</div>' +
      '<div class="qz-game-card__icon-wrap">' + app.icon(ico) + '</div>' +
      '<h3 class="qz-game-card__title">' + title + '</h3>' +
      '<p class="qz-game-card__desc">' + desc + '</p>' +
      '<div class="qz-game-card__btn">Play Now →</div>' +
    '</a>';
  }

  function scoreChip(p) {
    return p >= 85 ? "chip--ok" : p >= 70 ? "chip--accent" : p >= 50 ? "chip--warn" : "chip--danger";
  }

  function renderRecentResults(q) {
    var list = (q.attempts || []).slice(-6).reverse();
    if (!list.length) return "";

    return '<div class="qz-section-head mt-12">' +
      '<div class="qz-section-title"><span>🏆</span> Recent Game Hall of Fame</div>' +
      '<p class="qz-section-sub">Click any past game to open the full question-by-question walkthrough.</p>' +
    '</div>' +
    '<div class="qz-results-grid mt-4">' +
      list.map(function (a) {
        var p = app.pct(a.correct, a.total);
        var chip = scoreChip(p);
        var medal = p >= 85 ? "🥇" : p >= 70 ? "🥈" : p >= 50 ? "🥉" : "📝";
        return '<a class="qz-result-pill" href="#/quiz/attempt/' + encodeURIComponent(a.id) + '">' +
          '<span class="qz-result-pill__medal">' + medal + '</span>' +
          '<div class="qz-result-pill__body">' +
            '<div class="qz-result-pill__title">' + app.esc(a.label || "Animal Genetics Quiz") + '</div>' +
            '<div class="qz-result-pill__sub">' + fullDate(a.at) + ' · ' + (a.exam ? '⏱️ timed · ' : '') + a.correct + ' of ' + a.total + ' correct</div>' +
          '</div>' +
          '<div class="qz-result-pill__score ' + chip + '">' + p + '%</div>' +
        '</a>';
      }).join("") +
    '</div>';
  }

  /* ============================================================
     SETUP SCREEN — 4-Step Interactive Mission Configuration
     ============================================================ */
  function renderSetup(kind, id, preselectExam) {
    resetRun();
    var unitIds = scopeUnits(kind, id);
    var subSections = (kind === "unit" && subSectionsByUnit[id]) ? subSectionsByUnit[id] : [];

    var unitMeta = syllabus.unitById[id] || {};
    var label = kind === "unit"
      ? (unitMeta.stream === "practical" ? "Practical Unit " : "Unit ") + unitMeta.no + " — " + (unitMeta.short || "")
      : kind === "paper"
        ? (id === "paper-1" ? "Paper I" : "Paper II") + " — " + paperUnitLabel(id)
        : kind === "grand" ? "Grand Mock Test — All Theory Units" : "Practical Units Diagnostic";

    if (!unitIds.length || !countAvailable(unitIds)) {
      host.innerHTML =
        '<div class="pagehead"><a class="btn btn--sm btn--ghost" href="#/quiz">← Back to Quiz Arena</a>' +
        '<h1 class="mt-3">' + app.esc(label) + '</h1></div>' +
        '<div class="empty"><div class="empty__icon">' + app.icon("quiz") + '</div>' +
        '<h3>No questions written for this selection yet</h3>' +
        '<a class="btn btn--primary mt-4" href="#/quiz">Return to Quiz Arena</a></div>';
      return;
    }

    var prefs = store.getQuizPrefs() || {};
    var state = {
      subSectionId: preselectExam ? "exam" : "all",
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
        var examCount = bankFor(unitIds, ["mcq", "tf", "fib"], "exam").length;
        subSecHtml =
          '<div class="qz-setup-step">' +
            '<div class="qz-setup-step__head">' +
              '<span class="qz-setup-step__num">1</span>' +
              '<div>' +
                '<h3 class="qz-setup-step__title">Choose Your Target Topic Module</h3>' +
                '<p class="qz-setup-step__sub">Focus on a specific chapter or test the full unit in official exam ratios.</p>' +
              '</div>' +
            '</div>' +
            '<div class="subsec-grid mt-3">' +
              '<button type="button" class="subsec-card' + (state.subSectionId === 'all' ? ' is-active' : '') + '" data-sub="all">' +
                '<div class="subsec-card__head">' +
                  '<span class="subsec-card__icon">🌟</span>' +
                  '<span class="subsec-card__title">All Sub-Sections (Full Unit)</span>' +
                  '<span class="chip chip--accent subsec-card__badge">' + allCount + ' Qs</span>' +
                '</div>' +
                '<p class="subsec-card__desc">Complete comprehensive test covering all chapters in 2 : 1 : 1 exam ratio.</p>' +
              '</button>' +
              (examCount
                ? '<button type="button" class="subsec-card subsec-card--exam' + (state.subSectionId === 'exam' ? ' is-active' : '') + '" data-sub="exam">' +
                    '<div class="subsec-card__head">' +
                      '<span class="subsec-card__icon">' + EXAM_META.icon + '</span>' +
                      '<span class="subsec-card__title">' + app.esc(EXAM_META.title) + '</span>' +
                      '<span class="chip chip--warn subsec-card__badge">' + examCount + ' Qs</span>' +
                    '</div>' +
                    '<p class="subsec-card__desc">' + app.esc(EXAM_META.desc) + '</p>' +
                  '</button>'
                : '') +
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

      host.innerHTML =
        '<div class="qz-setup-container animate-fade-in">' +
          '<div class="qz-setup-header">' +
            '<a class="btn btn--sm btn--ghost" href="#/quiz">← Back to Arena</a>' +
            '<div class="qz-setup-title-wrap">' +
              '<h1 class="qz-setup-title">' + app.esc(label) + '</h1>' +
              '<p class="qz-setup-lede">Configure your game settings below — question count, format mix, and timed challenge.</p>' +
            '</div>' +
            '<span class="chip chip--accent font-mono">' + maxN + ' available questions</span>' +
          '</div>' +

          '<div class="qz-setup-card mt-6">' +
            subSecHtml +

            /* Step: Game Style & Order */
            '<div class="qz-setup-step">' +
              '<div class="qz-setup-step__head">' +
                '<span class="qz-setup-step__num">' + (subSections.length ? '2' : '1') + '</span>' +
                '<div>' +
                  '<h3 class="qz-setup-step__title">Question Order &amp; Style</h3>' +
                  '<p class="qz-setup-step__sub">Choose whether to follow the syllabus order or test your recall with random shuffle.</p>' +
                '</div>' +
              '</div>' +
              '<div class="quiz-mode-toggle mt-3" id="ordermodetoggle">' +
                '<button type="button" class="toggle-pill' + (state.orderMode === 'sequence' ? ' is-selected' : '') + '" data-mode="sequence">' +
                  '<span class="pill-icon">📋</span>' +
                  '<span class="pill-label">Sequence Mode</span>' +
                  '<span class="pill-sub">Follows curriculum order step-by-step</span>' +
                '</button>' +
                '<button type="button" class="toggle-pill' + (state.orderMode === 'shuffle' ? ' is-selected' : '') + '" data-mode="shuffle">' +
                  '<span class="pill-icon">🔀</span>' +
                  '<span class="pill-label">Shuffle Mode</span>' +
                  '<span class="pill-sub">Randomises questions for active recall</span>' +
                '</button>' +
              '</div>' +
            '</div>' +

            /* Step: Formats */
            '<div class="qz-setup-step">' +
              '<div class="qz-setup-step__head">' +
                '<span class="qz-setup-step__num">' + (subSections.length ? '3' : '2') + '</span>' +
                '<div>' +
                  '<h3 class="qz-setup-step__title">Question Formats (2 : 1 : 1 Exam Ratio)</h3>' +
                  '<p class="qz-setup-step__sub">Toggle the formats you want to include in this challenge.</p>' +
                '</div>' +
              '</div>' +
              '<div class="row row--wrap gap-3 mt-3" id="fmtbox">' +
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

            /* Step: Question Count */
            '<div class="qz-setup-step">' +
              '<div class="qz-setup-step__head">' +
                '<span class="qz-setup-step__num">' + (subSections.length ? '4' : '3') + '</span>' +
                '<div>' +
                  '<h3 class="qz-setup-step__title">Number of Questions</h3>' +
                  '<p class="qz-setup-step__sub">Pick your workout size from a quick 10-question sprint to a full marathon.</p>' +
                '</div>' +
              '</div>' +
              '<div class="seg mt-3" id="segcount">' +
                presets.map(function (n) {
                  var isSelected = state.count === n;
                  var label = n === 10 ? '⚡ 10 (Sprint)' : n === 20 ? '🎯 20 (Standard)' : n === 30 ? '🚀 30 (Deep Dive)' : (n === maxN ? '🏆 All (' + n + ')' : n);
                  return '<button type="button" class="seg__btn' + (isSelected ? ' is-on' : '') + '" data-count="' + n + '">' + label + '</button>';
                }).join("") +
              '</div>' +
            '</div>' +

            /* Step: Exam Mode */
            '<div class="qz-setup-step">' +
              '<div class="row row--between items-center">' +
                '<div>' +
                  '<h3 class="qz-setup-step__title">⏱️ Exam Simulation Mode</h3>' +
                  '<p class="qz-setup-step__sub">Timed challenge with no answers revealed until submission — exactly like the real board exam!</p>' +
                '</div>' +
                '<label class="switch"><input type="checkbox" id="exammode"' + (state.exam ? ' checked' : '') + '><span></span></label>' +
              '</div>' +
              '<div class="mt-4" id="timerow"' + (state.exam ? '' : ' hidden') + '>' +
                '<div class="small muted mb-2 font-bold">Select Countdown Limit:</div>' +
                '<div class="seg" id="segtime">' +
                  [10, 20, 30, 45, 60].map(function (m) {
                    return '<button type="button" class="seg__btn' + (state.minutes === m ? ' is-on' : '') + '" data-min="' + m + '">' + m + ' min</button>';
                  }).join("") +
                '</div>' +
              '</div>' +
            '</div>' +

          '</div>' +

          /* Bottom Launch Dock */
          '<div class="qz-launch-dock mt-6">' +
            '<a class="btn btn--ghost" href="#/quiz">Cancel</a>' +
            '<div class="qz-launch-dock__info">' +
              '<span>Configured: <b>' + Math.min(state.count, maxN) + ' Questions</b></span>' +
              '<span> · ' + (state.orderMode === "shuffle" ? "🔀 Shuffled" : "📋 Sequence") + '</span>' +
              (state.exam ? '<span> · ⏱️ ' + state.minutes + ' min</span>' : '<span> · 💡 Instant Feedback</span>') +
            '</div>' +
            '<button class="btn btn--primary btn--lg btn--launch" id="startbtn">' +
              '🚀 Launch Challenge (' + Math.min(state.count, maxN) + ' Questions)' +
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
          updateView();
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
          if (subMeta && state.subSectionId === "exam") runLabel = label + " · 🔥 Exam Top";
          else if (subMeta) runLabel = subMeta.icon + " " + subMeta.title;

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

  /* Smart review (spaced repetition) */
  function renderReview() {
    resetRun();
    var dueKeys = store.dueSrs();
    var all = bankFor(syllabus.allUnits.map(function (u) { return u.id; }), ["mcq", "tf", "fib"]);
    var pool = all.filter(function (q) { return dueKeys.indexOf(q.key) !== -1; });

    if (!pool.length) {
      host.innerHTML =
        '<div class="pagehead"><span class="eyebrow">Spaced Memory Workout</span><h1>Smart Memory Queue</h1></div>' +
        '<div class="empty"><div class="empty__icon">🎉</div><h3>Your memory queue is 100% clear!</h3>' +
        '<p>All your reviewed cards are safely consolidated. Questions you miss in quizzes will automatically reappear here when it is time to refresh your memory.</p>' +
        '<a class="btn btn--primary mt-4" href="#/quiz">Play a Quiz Challenge</a></div>';
      return;
    }

    start({
      questions: shuffle(pool),
      scope: "review",
      label: "Smart Memory Review",
      exam: false,
      minutes: 0,
      orderMode: "shuffle",
      subSectionId: "all",
      unitId: null
    });
  }

  /* Running a quiz */
  function start(cfg) {
    teardown();
    var questions = cfg.questions || [];
    run = {
      active: true,
      qs: questions,
      i: 0,
      answers: new Array(questions.length).fill(null),
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
        var remain = run.endsAt - Date.now();
        t.textContent = fmtTime(remain);
        if (remain < 60000) t.classList.add("is-critical");
      }
    }, 1000);
  }

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
    } catch (e) {}
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
    if (run.exam && run.endsAt && Date.now() >= run.endsAt) { finish(true); return; }
    startTimer();
    app.toast("Paper resumed at Question " + (run.i + 1));
    paintRun();
  }

  function hasAnswer(v) {
    if (v === null || v === undefined) return false;
    if (typeof v === "string") return v.trim() !== "";
    return true;
  }

  function answeredCount() {
    return run.answers.filter(hasAnswer).length;
  }

  function accrueTime() {
    if (!run) return;
    var now = Date.now();
    var delta = now - (run.tickAt || now);
    if (delta > 0 && delta < 10 * 60000) run.times[run.i] = (run.times[run.i] || 0) + delta;
    run.tickAt = now;
  }

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

  function optKey(i) {
    return String.fromCharCode(65 + i);
  }

  /* ============================================================
     IN-RUN QUIZ UI — Non-Cluttered, Colorful, Tactile & Playful (Silent)
     ============================================================ */
  function paintRun() {
    if (!run || !run.active) return;
    var q = run.qs[run.i];
    var given = run.answers[run.i];
    var showFeedback = !run.exam && run.checked[run.i];
    var isAnswerCorrect = showFeedback && isCorrect(q, given);

    var body;
    if (q.format === "mcq") {
      body = '<div class="opts opts--gamified">' + (q.o || []).map(function (opt, i) {
        var cls = "opt opt--gamified";
        var isPicked = given === i;
        if (isPicked) cls += " is-picked";
        if (showFeedback) {
          if (i === q.a) cls += " is-right";
          else if (isPicked) cls += " is-wrong";
        }
        return '<button type="button" class="' + cls + '" data-pick="' + i + '"' + (showFeedback ? ' disabled' : '') + '>' +
          '<span class="opt__key">' + optKey(i) + '</span>' +
          '<span class="opt__text">' + app.esc(opt) + '</span>' +
          (showFeedback && i === q.a ? '<span class="opt__state opt__state--ok">✓ Correct</span>' : '') +
          (showFeedback && isPicked && i !== q.a ? '<span class="opt__state opt__state--bad">✗ Incorrect</span>' : '') +
        '</button>';
      }).join("") + '</div>';

    } else if (q.format === "tf") {
      body = '<div class="opts opts--2 opts--gamified">' + [true, false].map(function (v) {
        var cls = "opt opt--tf opt--gamified";
        var isPicked = given === v;
        if (isPicked) cls += " is-picked";
        if (showFeedback) {
          if (v === q.a) cls += " is-right";
          else if (isPicked) cls += " is-wrong";
        }
        var icon = v ? "🟢" : "🔴";
        return '<button type="button" class="' + cls + '" data-pick="' + v + '"' + (showFeedback ? ' disabled' : '') + '>' +
          '<span class="opt__key opt__key--tf">' + (v ? "T" : "F") + '</span>' +
          '<span class="opt__text">' + icon + ' ' + (v ? "True" : "False") + '</span>' +
          (showFeedback && v === q.a ? '<span class="opt__state opt__state--ok">✓ Correct</span>' : '') +
          (showFeedback && isPicked && v !== q.a ? '<span class="opt__state opt__state--bad">✗ Incorrect</span>' : '') +
        '</button>';
      }).join("") + '</div>';

    } else {
      var fibOk = showFeedback && isCorrect(q, given);
      body = '<div class="fib-card fib-card--gamified">' +
        '<div class="fib-input-wrap">' +
          '<input type="text" id="fibinput" class="fib-input" placeholder="Type your answer here and press Enter…" autocomplete="off" autocorrect="off" spellcheck="false" ' +
          'value="' + app.esc(given !== null && given !== undefined ? String(given) : "") + '"' + (showFeedback ? ' disabled' : '') + '>' +
          (!showFeedback
            ? '<button type="button" class="btn btn--primary btn--submit-fib" id="fibsubmit">Submit ↵</button>'
            : '') +
        '</div>' +
        (showFeedback
          ? '<div class="fib-accepted-callout ' + (fibOk ? 'is-ok' : 'is-error') + '">' +
              '<span class="badge">' + (fibOk ? '✓ Correct Answer' : '✗ Incorrect') + '</span>' +
              '<span class="label"><b>Standard answer:</b> ' + app.esc(displayAnswer(q)) + '</span>' +
              (fibOk && run.near[run.i] ? '<span class="label small faint">Accepted with a slight spelling slip — remember the exact term for exams!</span>' : '') +
            '</div>'
          : '<p class="small faint mt-2">💡 Tip: Type the key term. Minor typos/casing are forgiven.</p>') +
        '</div>';
    }

    var answered = answeredCount();
    var flaggedN = run.flags.filter(Boolean).length;
    var progressPct = Math.round(((run.i + 1) / run.qs.length) * 100);

    /* Question Drawer / Navigator Map (Keeps the screen clean, opens on demand!) */
    var paletteHtml = '<div class="quiz-map-drawer' + (mapDrawerOpen ? ' is-open' : '') + '" id="mapdrawer">' +
      '<div class="quiz-map-drawer__head">' +
        '<div class="quiz-map-drawer__title">🗺️ Question Navigator Map</div>' +
        '<div class="quiz-map-drawer__legend">' +
          '<span class="qz-leg qz-leg--done">● Answered</span>' +
          '<span class="qz-leg qz-leg--flag">🚩 Flagged (' + flaggedN + ')</span>' +
          '<span class="qz-leg qz-leg--blank">○ Blank (' + (run.qs.length - answered) + ')</span>' +
        '</div>' +
      '</div>' +
      '<div class="quiz-map-drawer__grid">' +
        run.qs.map(function (item, idx) {
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
            'title="Question ' + (idx + 1) + (run.flags[idx] ? ' (Flagged)' : '') + '">' +
            (run.flags[idx] ? '🚩' : (idx + 1)) +
          '</button>';
        }).join("") +
      '</div>' +
      '<div class="quiz-map-drawer__footer">' +
        '<span class="quiz-dock-status">' + answered + ' of ' + run.qs.length + ' answered' +
          (flaggedN ? ' · 🚩 ' + flaggedN + ' flagged' : '') + '</span>' +
        '<button type="button" class="btn btn--sm btn--submit-test" id="drawersubmitbtn" title="Submit test and view results">🏁 Submit Test</button>' +
      '</div>' +
    '</div>';

    var subMeta = getSubSectionMeta(q.unitId, q.subSection);
    var subBadge = subMeta
      ? '<span class="chip chip--accent"><span class="qicon">' + subMeta.icon + '</span> ' + app.esc(subMeta.title) + '</span>'
      : '';
    var unitMeta = syllabus.unitById[q.unitId] || {};

    host.innerHTML =
      '<div class="quizrun-arena animate-fade-in">' +

        /* Top Bar: Clean, focused, Question map button */
        '<div class="quizrun__topbar">' +
          '<button class="btn btn--sm btn--ghost" id="quitbtn" title="Exit challenge safely">✕ Quit</button>' +
          '<span class="chip chip--subtle font-mono qz-badge-progress">Q ' + (run.i + 1) + ' of ' + run.qs.length + '</span>' +

          '<div class="quizrun__topbar-center">' +
            '<div class="qz-progress-track">' +
              '<div class="qz-progress-fill" style="width:' + progressPct + '%"></div>' +
              '<span class="qz-progress-label">' + progressPct + '%</span>' +
            '</div>' +
          '</div>' +

          '<div class="quizrun__topbar-right">' +
            (run.streak >= 2
              ? '<span class="chip chip--accent streak-badge" title="Consecutive correct answers">🔥 ' + run.streak + ' Streak!</span>'
              : '') +
            (run.exam
              ? '<span class="chip chip--warn font-mono" id="qtimer">⏱️ ' + fmtTime(run.endsAt - Date.now()) + '</span>'
              : '') +
            '<button type="button" class="btn btn--sm btn--outline qz-map-btn" id="mapdrawerbtn">' +
              '🗺️ Map (' + answered + '/' + run.qs.length + ') ' + (mapDrawerOpen ? '▲' : '▼') +
            '</button>' +
            '<button type="button" class="btn btn--sm btn--submit-test qz-top-submit-btn" id="topsubmitbtn" title="Submit test and view results">🏁 Submit Test</button>' +
          '</div>' +
        '</div>' +

        paletteHtml +

        /* The Question Stage Card */
        '<div class="card quizcard-stage mt-4">' +

          '<div class="quizcard-stage__meta">' +
            '<span class="chip chip--accent font-bold">' + FORMAT_ICON[q.format] + ' ' + FORMAT_LABEL[q.format] + '</span>' +
            '<span class="chip">' + app.esc(unitMeta.short || q.unitId) + '</span>' +
            subBadge +
            '<span class="chip chip--subtle">' + (DIFF_STARS[q.diff] || "⭐") + ' ' + (DIFF_LABEL[q.diff] || "Foundational") + '</span>' +
            (q.exam ? '<span class="chip chip--warn">🔥 Exam Top</span>' : '') +
            '<button type="button" class="flagbtn-stage' + (run.flags[run.i] ? ' is-on' : '') + '" id="flagbtn" title="Bookmark to review before finishing">' +
              '🚩 <span>' + (run.flags[run.i] ? 'Flagged for Review' : 'Flag Question') + '</span>' +
            '</button>' +
          '</div>' +

          '<h2 class="quizcard-stage__q mt-4">' + app.esc(q.q) + '</h2>' +

          body +

          /* High-yield key takeaway note */
          (showFeedback && q.e
            ? '<div class="quiz-explanation-box mt-6 animate-scale-up ' + (isAnswerCorrect ? 'is-correct' : 'is-wrong') + '">' +
                '<div class="quiz-explanation-box__head">' +
                  '<span>' + (isAnswerCorrect ? '🎉 Great Job! Correct Answer' : '💡 Explanation & High-Yield Key Note') + '</span>' +
                '</div>' +
                '<p class="quiz-explanation-box__body">' + q.e + '</p>' +
                (q.topicId && syllabus.topicById[q.topicId]
                  ? '<div class="mt-3"><a class="btn btn--sm btn--outline" href="#/topic/' + q.topicId + '" target="_blank">' +
                      '📖 Open Full Lesson: ' + app.esc(syllabus.topicById[q.topicId].title) + ' ↗</a></div>'
                  : '') +
              '</div>'
            : '') +

        '</div>' +

        /* Unified Bottom Action Dock — No scattered buttons! */
        '<div class="quiz-action-dock mt-6">' +
          '<button class="btn btn--dock" id="prevbtn"' + (run.i === 0 ? ' disabled' : '') + '>← Previous</button>' +
          '<div class="quiz-action-dock__center">' +
            '<button type="button" class="btn btn--sm btn--ghost flag-toggle-dock' + (run.flags[run.i] ? ' is-on' : '') + '" id="flagdockbtn">' +
              '🚩 ' + (run.flags[run.i] ? 'Flagged' : 'Flag') +
            '</button>' +
            '<span class="quiz-dock-status">' + answered + ' of ' + run.qs.length + ' answered' +
              (flaggedN ? ' · 🚩 ' + flaggedN + ' flagged' : '') + '</span>' +
            '<button type="button" class="btn btn--sm btn--submit-test qz-dock-submit-btn" id="docksubmitbtn" title="Submit test at any time">🏁 Submit Test</button>' +
          '</div>' +
          (run.i === run.qs.length - 1
            ? '<button class="btn btn--primary btn--lg btn--finish-quiz" id="finishbtn">🏁 Submit Test &amp; Results 🏆</button>'
            : '<button class="btn btn--primary btn--lg btn--next-quiz' + (hasAnswer(given) ? ' is-ready' : '') + '" id="nextbtn">' +
                (hasAnswer(given) ? 'Next Question →' : 'Skip for Now →') + '</button>') +
        '</div>' +

        '<div class="quiz-shortcuts-hint mt-3 center small faint">' +
          '🎮 Keyboard shortcuts: <kbd>1–4</kbd> / <kbd>A–D</kbd> choose · <kbd>T</kbd>/<kbd>F</kbd> true-false · ' +
          '<kbd>←</kbd> <kbd>→</kbd> navigate · <kbd>M</kbd> flag · <kbd>Enter</kbd> next' +
        '</div>' +

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

  /* Answer checking & text normalisation */
  function normText(s) {
    var t = String(s == null ? "" : s).toLowerCase();
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
      if (mine.replace(/[\s-]/g, "") === want.replace(/[\s-]/g, "")) return { ok: true, near: false };
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
      if (run.streak === 3 && app.popMilestone) app.popMilestone("🔥 3 Streak! You're on fire!");
      else if (run.streak === 5 && app.popMilestone) app.popMilestone("🚀 5 in a row! Unstoppable!");
      else if (run.streak === 7 && app.popMilestone) app.popMilestone("⚡ 7 Streak! Genetic Genius!");
      else if (run.streak === 10 && app.popMilestone) app.popMilestone("👑 10 Streak! Master Geneticist!");
    } else {
      run.streak = 0;
    }
    snapshot();
  }

  function wireRun(q) {
    document.querySelectorAll("[data-pick]").forEach(function (b) {
      b.addEventListener("click", function () {
        if (!run.exam && run.checked[run.i]) return;
        var raw = b.getAttribute("data-pick");
        run.answers[run.i] = (q.format === "tf") ? (raw === "true") : parseInt(raw, 10);
        if (run.exam) { accrueTime(); snapshot(); }
        revealCurrent(b);
        paintRun();
      });
    });

    // Map drawer toggle
    var mapBtn = document.getElementById("mapdrawerbtn");
    if (mapBtn) {
      mapBtn.addEventListener("click", function () {
        mapDrawerOpen = !mapDrawerOpen;
        var drawer = document.getElementById("mapdrawer");
        if (drawer) drawer.classList.toggle("is-open", mapDrawerOpen);
        mapBtn.innerHTML = '🗺️ Map (' + answeredCount() + '/' + run.qs.length + ') ' + (mapDrawerOpen ? '▲' : '▼');
      });
    }

    document.querySelectorAll("[data-goto]").forEach(function (b) {
      b.addEventListener("click", function () {
        mapDrawerOpen = false;
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

    var flagDockBtn = document.getElementById("flagdockbtn");
    if (flagDockBtn) {
      flagDockBtn.addEventListener("click", function () {
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
        app.toast("Type your answer first!");
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

    function handleTestSubmit() {
      if (q.format === "fib") {
        var el3 = document.getElementById("fibinput");
        if (el3 && el3.value) run.answers[run.i] = el3.value;
      }
      confirmFinish();
    }

    var fin = document.getElementById("finishbtn");
    if (fin) fin.addEventListener("click", handleTestSubmit);
    var topSub = document.getElementById("topsubmitbtn");
    if (topSub) topSub.addEventListener("click", handleTestSubmit);
    var dockSub = document.getElementById("docksubmitbtn");
    if (dockSub) dockSub.addEventListener("click", handleTestSubmit);
    var drawerSub = document.getElementById("drawersubmitbtn");
    if (drawerSub) drawerSub.addEventListener("click", handleTestSubmit);

    var quit = document.getElementById("quitbtn");
    if (quit) quit.addEventListener("click", function () {
      if (confirm("Pause and exit this paper?\n\nIt is saved safely, so you can resume right where you left off from the quiz hub.")) {
        snapshot();
        resetRun();
        location.hash = "#/quiz";
      }
    });

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

  function confirmFinish() {
    var answered = answeredCount();
    var blanks = run.qs.length - answered;
    var flagged = run.flags.filter(Boolean).length;
    if (blanks || flagged) {
      var msg = "Submit Test Now?\n\n";
      msg += "• " + answered + " of " + run.qs.length + " questions answered\n";
      if (blanks) msg += "• " + blanks + " question" + (blanks > 1 ? "s are" : " is") + " still unanswered\n";
      if (flagged) msg += "• " + flagged + " question" + (flagged > 1 ? "s are" : " is") + " flagged for review\n";
      msg += "\nUnanswered questions will be marked incorrect.\nClick OK to submit your test, or Cancel to continue answering.";
      if (!confirm(msg)) {
        var firstBlank = -1;
        for (var i = 0; i < run.qs.length; i++) {
          if (!hasAnswer(run.answers[i])) { firstBlank = i; break; }
        }
        if (firstBlank === -1) firstBlank = run.flags.indexOf(true);
        if (firstBlank >= 0) goTo(firstBlank);
        return;
      }
    } else {
      if (!confirm("Submit Test Now?\n\n🎉 You answered all " + run.qs.length + " questions!\n\nClick OK to submit and view your detailed report card.")) {
        return;
      }
    }
    finish(false);
  }

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

    var prev = null;
    var history = store.getQuiz().attempts.filter(function (a) { return a.scope === attempt.scope; });
    if (history.length) prev = history[history.length - 1];

    var attemptId = store.saveAttempt(attempt);
    attempt.id = attemptId;

    if (!host || !document.body.contains(host)) {
      if (timedOut && app.toast) app.toast("Time expired — your paper was submitted and saved");
      run = null;
      return;
    }

    var qsForReview = run.qs;
    run = null;
    paintAnalysis(attempt, { questions: qsForReview, prev: prev, live: true });
  }

  function renderStoredAttempt(id) {
    resetRun();
    var attempt = id ? store.getAttempt(decodeURIComponent(id)) : null;
    if (!attempt) {
      host.innerHTML =
        '<div class="pagehead"><a class="btn btn--sm btn--ghost" href="#/quiz">← Back to Arena</a>' +
        '<h1 class="mt-3">Paper not found</h1></div>' +
        '<div class="empty"><div class="empty__icon">' + app.icon("search") + '</div>' +
        '<h3>That result is no longer stored in your history</h3>' +
        '<a class="btn btn--primary mt-4" href="#/quiz">Return to Quiz Arena</a></div>';
      return;
    }
    var all = store.getQuiz().attempts.filter(function (a) { return a.scope === attempt.scope; });
    var idx = -1;
    all.forEach(function (a, i) { if (String(a.id) === String(attempt.id)) idx = i; });
    var prev = idx > 0 ? all[idx - 1] : null;
    paintAnalysis(attempt, { prev: prev, live: false });
  }

  /* ============================================================
     ANALYSIS SCREEN — Triumphant, Colorful, Crystal Clear
     ============================================================ */
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
    if (!items.some(function (it) { return !it.ok; })) reviewState.filter = "all";

    var percent = app.pct(attempt.correct, attempt.total);
    var verdict = percent >= 85 ? "Rank 1 Distinction"
      : percent >= 70 ? "Strong First Class"
      : percent >= 50 ? "Passing Grade" : "Needs Revision";
    var chipCls = scoreChip(percent);

    var attempted = typeof attempt.attempted === "number" ? attempt.attempted : attempt.total;
    var skipped = attempt.skipped || 0;
    var totalMs = (attempt.seconds || 0) * 1000;
    var avgMs = attempt.total ? totalMs / attempt.total : 0;

    var delta = null;
    if (opts.prev && opts.prev.total) {
      delta = percent - app.pct(opts.prev.correct, opts.prev.total);
    }

    host.innerHTML =
      '<div class="analysis animate-fade-in">' +

        (attempt.timedOut
          ? '<div class="callout callout--warn mb-6"><div class="callout__title">⏱️ Time Expired</div>' +
            'Your challenge was submitted automatically when the countdown reached zero.</div>' : '') +

        /* Triumphant Hero Header */
        '<div class="an-head-gamified">' +
          '<div class="an-head-gamified__ring">' + app.ringHtml(percent, 140) + '</div>' +
          '<div class="an-head-gamified__body">' +
            '<div class="an-head-gamified__badge ' + chipCls + '">🏆 ' + verdict + '</div>' +
            '<h1 class="an-head-gamified__title">' + attempt.correct + ' of ' + attempt.total + ' Correct (' + percent + '%)</h1>' +
            '<div class="row row--wrap gap-2 mt-2">' +
              '<span class="chip">' + app.esc(attempt.label || "Animal Genetics Quiz") + '</span>' +
              '<span class="chip chip--subtle">' + (attempt.orderMode === "shuffle" ? "🔀 Shuffled" : "📋 Sequence") + '</span>' +
              (attempt.exam ? '<span class="chip chip--subtle">⏱️ Exam Simulation</span>' : '') +
              (delta !== null
                ? '<span class="chip ' + (delta > 0 ? 'chip--ok' : delta < 0 ? 'chip--danger' : 'chip--subtle') + '">' +
                  (delta > 0 ? '▲ +' : delta < 0 ? '▼ ' : '– ') + Math.abs(delta) + '% vs previous attempt</span>'
                : '') +
            '</div>' +
            '<p class="muted small mt-3">' + verdictAdvice(percent, skipped, attempt) + '</p>' +
          '</div>' +
        '</div>' +

        /* 4 Big Power Cards */
        '<div class="an-metrics-grid mt-6">' +
          metricCard("🎯", "Overall Accuracy", percent + "%", attempt.correct + " correct · " + (attempt.total - attempt.correct) + " missed", "blue") +
          metricCard("⚡", "Pace & Timing", fmtDuration(avgMs) + " / Q", paceVerdict(avgMs), "amber") +
          metricCard("🔥", "Best Streak", (attempt.bestStreak || 0) + " In A Row", "Longest correct run", "coral") +
          metricCard("⏳", "Total Duration", fmtDuration(totalMs), skipped ? skipped + " questions left blank" : "All questions answered", "green") +
        '</div>' +

        /* Quick Action Dock */
        '<div class="an-actions-hero mt-8">' +
          (items.some(function (it) { return !it.ok; })
            ? '<button class="btn btn--primary btn--lg btn--retry-action" id="an-retry-wrong">' +
                '🔁 Retry Missed (' + items.filter(function (it) { return !it.ok; }).length + ' Questions)</button>'
            : '') +
          '<button class="btn btn--lg" id="an-retake">🔄 Retake Full Quiz</button>' +
          '<a class="btn btn--lg" href="#/quiz">🎮 Back to Arena</a>' +
          '<a class="btn btn--lg" href="#/dashboard">📊 Open Dashboard</a>' +
        '</div>' +

        /* Sub-Section Mastery Breakdown */
        renderSubMastery(attempt) +

        /* Question-by-Question Review with Filter Tabs */
        '<section class="mt-12" id="an-review">' +
          '<div class="row row--between items-center">' +
            '<div>' +
              '<h2>Question-by-Question Review</h2>' +
              '<p class="muted small mt-1">Review your answers, verify the standard textbook terms, and read the biological mechanisms.</p>' +
            '</div>' +
          '</div>' +
          '<div class="an-filterbar mt-4" id="an-filters"></div>' +
          '<div class="an-search mt-3">' +
            app.icon("search", "faint") +
            '<input type="text" id="an-search-input" placeholder="Search these questions, terms or explanations…" autocomplete="off">' +
          '</div>' +
          '<div id="an-review-list" class="mt-4"></div>' +
        '</section>' +

      '</div>';

    paintReviewList();
    wireAnalysis(attempt, items);

    if (opts.live && percent >= 75 && app.burstConfetti) {
      setTimeout(function () {
        var ring = document.querySelector('.an-head-gamified__ring');
        if (ring) app.burstConfetti(ring);
        if (app.popMilestone) app.popMilestone("🏆 " + verdict + " (" + percent + "%)!");
      }, 250);
    }
  }

  function metricCard(icon, title, val, sub, tone) {
    return '<div class="an-metric-card an-metric-card--' + tone + '">' +
      '<div class="an-metric-card__icon">' + icon + '</div>' +
      '<div class="an-metric-card__val">' + app.esc(val) + '</div>' +
      '<div class="an-metric-card__title">' + title + '</div>' +
      '<div class="an-metric-card__sub">' + app.esc(sub) + '</div>' +
    '</div>';
  }

  function paceVerdict(avgMs) {
    if (!avgMs) return "—";
    var s = avgMs / 1000;
    if (s < 15) return "Very swift recall!";
    if (s < 40) return "Excellent exam pace!";
    if (s < 75) return "Thorough, careful deliberation";
    return "A bit slow for a timed paper";
  }

  function verdictAdvice(percent, skipped, attempt) {
    if (percent >= 85) return "Distinction grade mastery! Keep this knowledge warm through the spaced repetition queue.";
    if (percent >= 70) return "A solid first class! Review the missed questions below to push this into the 90%+ bracket.";
    if (percent >= 50) return "A passing score, but there is room for improvement. Retry the questions you missed to lock in the concepts.";
    return "This section needs another revision pass. Read the linked lessons below and retry your missed questions." +
      (skipped ? " (" + skipped + " question" + (skipped > 1 ? "s were" : " was") + " left blank)." : "");
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

    return '<section class="mt-10">' +
      '<h2>Sub-Section Module Breakdown</h2>' +
      '<p class="muted small mt-1">See exactly where your marks came from. Weakest modules appear first.</p>' +
      '<div class="an-sub-grid mt-4">' +
        rows.map(function (r) {
          return '<div class="an-sub-card">' +
            '<div class="an-sub-card__head">' +
              '<span class="an-sub-card__icon">' + r.icon + '</span>' +
              '<b class="an-sub-card__title">' + app.esc(r.title) + '</b>' +
              '<span class="chip ' + scoreChip(r.pct) + '">' + r.right + '/' + r.total + ' (' + r.pct + '%)</span>' +
            '</div>' +
            '<div class="bar mt-2"><div class="bar__fill ' + barTone(r.pct) + '" style="width:' + r.pct + '%"></div></div>' +
            '<div class="an-sub-card__actions mt-3">' +
              (r.unitId ? '<a class="btn btn--sm btn--outline" href="#/unit/' + r.unitId + '">📖 Read Lesson</a>' : '') +
              (r.unitId ? '<a class="btn btn--sm btn--primary" href="#/quiz/unit/' + r.unitId + '">🎯 Retest Module</a>' : '') +
            '</div>' +
          '</div>';
        }).join("") +
      '</div>' +
    '</section>';
  }

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
      { id: "wrong", label: "❌ Missed", n: counts.wrong },
      { id: "flagged", label: "🚩 Flagged", n: counts.flagged },
      { id: "skipped", label: "○ Skipped", n: counts.skipped },
      { id: "right", label: "✅ Correct", n: counts.right },
      { id: "all", label: "All Questions", n: counts.all }
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
        (s.q ? 'No questions match “' + app.esc(s.q) + '”.'
             : 'No questions in this filter — that is great news!') + '</div>';
      return;
    }

    list.innerHTML = rows.map(function (it) {
      var unit = syllabus.unitById[it.unitId] || {};
      var subMeta = getSubSectionMeta(it.unitId, it.subSection);
      var stateCls = it.skipped ? "is-skipped" : it.ok ? "is-right" : "is-wrong";
      var stateLbl = it.skipped ? "○ Left Blank" : it.ok ? "✓ Correct" : "✗ Missed";

      return '<article class="an-q-card ' + stateCls + '">' +
        '<div class="an-q-card__top">' +
          '<span class="an-q-card__n">Q' + it.n + '</span>' +
          '<span class="chip ' + (it.skipped ? 'chip--warn' : it.ok ? 'chip--ok' : 'chip--danger') + '">' + stateLbl + '</span>' +
          '<span class="chip chip--subtle font-mono">' + FORMAT_SHORT[it.format] + '</span>' +
          '<span class="chip chip--subtle">' + app.esc(unit.short || it.unitId) + '</span>' +
          (subMeta ? '<span class="chip chip--subtle">' + subMeta.icon + ' ' + app.esc(subMeta.title) + '</span>' : '') +
          (it.flagged ? '<span class="chip chip--warn">🚩 Flagged</span>' : '') +
          '<span class="push"></span>' +
          (it.ms ? '<span class="chip chip--subtle font-mono">' + app.icon("clock", "faint") + ' ' + fmtDuration(it.ms) + '</span>' : '') +
        '</div>' +

        '<p class="an-q-card__text">' + app.esc(it.q) + '</p>' +

        '<div class="an-q-card__answers">' +
          '<div class="an-ans ' + (it.ok ? 'is-ok' : 'is-bad') + '">' +
            '<span class="an-ans__lbl">Your answer:</span>' +
            '<span class="an-ans__val">' + (it.skipped ? '<i class="faint">not answered</i>' : app.esc(String(it.given))) + '</span>' +
          '</div>' +
          '<div class="an-ans is-ok">' +
            '<span class="an-ans__lbl">Standard textbook answer:</span>' +
            '<span class="an-ans__val">' + app.esc(String(it.right)) + '</span>' +
          '</div>' +
        '</div>' +

        (it.near ? '<p class="small faint mt-2">Accepted with a slight spelling typo — remember to write it exactly in written exams!</p>' : '') +

        (it.e
          ? '<div class="an-q-card__why"><b>💡 Biological Mechanism &amp; Note:</b> ' + it.e + '</div>'
          : '') +

        (it.topicId && syllabus.topicById[it.topicId]
          ? '<a class="btn btn--sm btn--outline mt-3" href="#/topic/' + it.topicId + '">' + app.icon("book") +
            ' Read textbook lesson: ' + app.esc(syllabus.topicById[it.topicId].title) + '</a>'
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
        startFromKeys(keys, "Retry Missed Questions (" + keys.length + ")", attempt);
      });
    }

    var retake = document.getElementById("an-retake");
    if (retake) {
      retake.addEventListener("click", function () {
        var keys = items.map(function (it) { return it.key; });
        startFromKeys(keys, attempt.label, attempt, true);
      });
    }
  }

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

  return {
    render: render,
    subSectionMeta: function (subId) { return getSubSectionMeta(null, subId); },
    subSectionsByUnit: subSectionsByUnit,
    reset: resetRun,
    leave: leave,
    teardown: teardown
  };
})();
