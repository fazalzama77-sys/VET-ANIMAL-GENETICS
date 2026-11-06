/* ============================================================
   store.js  —  Everything that must survive a page refresh.
   Animal Genetics and Breeding Studio
   ------------------------------------------------------------
   All keys are prefixed "vgen-" so this site can never collide
   with other subject sites if served from one domain.

   IMPORTANT: if you add a NEW key, also add it to store.backupKeys()
   or the Backup/Restore file will silently miss it.
   ============================================================ */

var store = (function () {

  var PREFIX = "vgen-";

  var KEYS = {
    theme:      PREFIX + "theme",       // "light" (default) | "dark"
    detail:     PREFIX + "detail",      // "standard" | "deep"
    read:       PREFIX + "read",        // { topicId: timestamp }
    bookmarks:  PREFIX + "bookmarks",   // [ "topicId", ... ]
    notes:      PREFIX + "notes",       // { topicId: "note text" }
    highlights: PREFIX + "highlights",  // { topicId: [ {text, color}, ... ] }
    hlColor:    PREFIX + "hl-color",    // "yellow" | "green" | "blue" | "pink" | "orange" | "purple"
    quiz:       PREFIX + "quiz",        // { attempts: [], byUnit: {} }
    srs:        PREFIX + "srs",         // { questionKey: {box, due, wrong} }
    activity:   PREFIX + "activity",    // { "YYYY-MM-DD": actionCount }
    visits:     PREFIX + "visits",      // number
    onboarded:  PREFIX + "onboarded",   // "1"
    lastTopic:  PREFIX + "last-topic",  // topicId — powers "Resume studying"
    qaDone:     PREFIX + "qa-done",     // [ "qaId", ... ]
    notifySrs:  PREFIX + "notify-srs",  // boolean: whether daily SRS notification is enabled
    notifyTime: PREFIX + "notify-time", // preferred reminder time "HH:MM"
    navPos:     PREFIX + "nav-pos",     // "bottom" | "top" | "left" | "right"
    deepGuideSeen: PREFIX + "deep-guide-seen",
    topicGuideSeen: PREFIX + "topic-guide-seen",
    eventSeen:  PREFIX + "event-announcements-seen",
    installDismissed: PREFIX + "install-dismissed",
    sidebarCollapsed: PREFIX + "sidebar-collapsed",
    quizResume:  PREFIX + "quiz-resume",   // { ... } a paper left unfinished
    quizPrefs:   PREFIX + "quiz-prefs",    // remembered setup choices
    syncConfig:  PREFIX + "sync-config"
  };

  /* ---------- low level ---------- */
  function read(key, fallback) {
    try {
      var raw = localStorage.getItem(key);
      if (raw === null) return fallback;
      return JSON.parse(raw);
    } catch (e) {
      return fallback;
    }
  }

  function write(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      if (store && typeof store._onChange === "function") {
        try { store._onChange(key, value); } catch (err) {}
      }
      return true;
    } catch (e) {
      // Quota exceeded or private mode — fail quietly, never break the page.
      console.warn("[store] could not save", key, e);
      return false;
    }
  }

  /* ---------- theme ---------- */
  function getTheme() { return read(KEYS.theme, "light"); }
  function setTheme(v) {
    write(KEYS.theme, v);
    applyTheme();
  }
  function applyTheme() {
    var t = getTheme();
    if (typeof document !== "undefined" && document.documentElement) {
      document.documentElement.setAttribute("data-theme", t === "dark" ? "dark" : "light");
    }
  }

  /* ---------- detail level (Standard vs Deep) ---------- */
  function getDetail() { return read(KEYS.detail, "standard"); }
  function setDetail(v) { write(KEYS.detail, v); }

  /* ---------- read / progress ---------- */
  function getRead() { return read(KEYS.read, {}); }
  function isRead(id) { return !!getRead()[id]; }
  function toggleRead(id) {
    var m = getRead();
    if (m[id]) delete m[id]; else m[id] = Date.now();
    write(KEYS.read, m);
    logActivity();
    return !!m[id];
  }

  /* ---------- bookmarks ---------- */
  function getBookmarks() { return read(KEYS.bookmarks, []); }
  function isBookmarked(id) { return getBookmarks().indexOf(id) !== -1; }
  function toggleBookmark(id) {
    var a = getBookmarks();
    var i = a.indexOf(id);
    if (i === -1) a.push(id); else a.splice(i, 1);
    write(KEYS.bookmarks, a);
    return i === -1;
  }

  /* ---------- notes ---------- */
  function getNotes() { return read(KEYS.notes, {}); }
  function getNote(id) { return getNotes()[id] || ""; }
  function setNote(id, text) {
    var m = getNotes();
    if (text && text.trim()) m[id] = text; else delete m[id];
    write(KEYS.notes, m);
    logActivity();
  }

  /* ---------- highlights ---------- */
  var VALID_HL_COLORS = ["yellow", "green", "blue", "pink", "orange", "purple"];
  function getHighlightColor() {
    var c = read(KEYS.hlColor, "yellow");
    return VALID_HL_COLORS.indexOf(c) !== -1 ? c : "yellow";
  }
  function setHighlightColor(color) {
    if (VALID_HL_COLORS.indexOf(color) === -1) color = "yellow";
    write(KEYS.hlColor, color);
    return color;
  }
  function getHighlights() { return read(KEYS.highlights, {}); }
  /* anchor = { occ, prefix, suffix } — where in the lesson the words were
     selected, so the colour is painted on those words and not on the first
     place the same words appear. The same phrase may be highlighted in
     several places; each place is its own highlight. */
  function sameHighlight(item, text, occ) {
    var itemText = typeof item === "string" ? item : (item ? item.text : "");
    if (itemText !== text) return false;
    var itemOcc = (item && typeof item.occ === "number") ? item.occ : undefined;
    // A highlight saved before positions were recorded matches any position.
    if (itemOcc === undefined || occ === undefined) return true;
    return itemOcc === occ;
  }

  function addHighlight(id, text, color, anchor) {
    color = (color && VALID_HL_COLORS.indexOf(color) !== -1) ? color : getHighlightColor();
    var m = getHighlights();
    if (!m[id]) m[id] = [];

    var entry = { text: text, color: color };
    if (anchor && typeof anchor.occ === "number") {
      entry.occ = anchor.occ;
      entry.prefix = anchor.prefix || "";
      entry.suffix = anchor.suffix || "";
    }

    var found = false;
    for (var i = 0; i < m[id].length; i++) {
      if (sameHighlight(m[id][i], text, entry.occ)) {
        m[id][i] = entry;          // re-colouring the same spot, or upgrading an old one
        found = true;
        break;
      }
    }
    if (!found) m[id].push(entry);
    write(KEYS.highlights, m);
    logActivity();
  }

  /* occ given → remove only that spot; occ omitted → every copy of the text. */
  function removeHighlight(id, text, occ) {
    var m = getHighlights();
    if (!m[id]) return;
    m[id] = m[id].filter(function (t) {
      return !sameHighlight(t, text, occ);
    });
    if (!m[id].length) delete m[id];
    write(KEYS.highlights, m);
  }

  /* ---------- quiz results ---------- */

  /* Per-attempt question detail is what powers the review screen, but it is
     also the bulkiest thing we store. Keep the full detail only for the most
     recent papers and keep bare scores for the rest, so a year of study can
     never fill the localStorage quota. */
  var MAX_ATTEMPTS = 120;
  var DETAIL_KEEP = 25;

  function getQuiz() {
    var q = read(KEYS.quiz, { attempts: [], byUnit: {}, bySub: {} });
    if (!q || typeof q !== "object") q = {};
    if (!Array.isArray(q.attempts)) q.attempts = [];
    if (!q.byUnit || typeof q.byUnit !== "object") q.byUnit = {};
    if (!q.bySub || typeof q.bySub !== "object") q.bySub = {};
    return q;
  }

  /* Attempts are addressed by a stable id, not by array position — the list
     is trimmed from the front, so an index would point at a different paper
     the moment the cap is reached. */
  function getAttempt(id) {
    var list = getQuiz().attempts;
    for (var i = 0; i < list.length; i++) {
      if (String(list[i].id) === String(id)) return list[i];
    }
    return null;
  }

  function saveAttempt(attempt) {
    var q = getQuiz();

    attempt.id = attempt.id || (String(attempt.at || Date.now()) + "-" +
      Math.random().toString(36).slice(2, 7));

    q.attempts.push(attempt);
    if (q.attempts.length > MAX_ATTEMPTS) {
      q.attempts = q.attempts.slice(-MAX_ATTEMPTS);
    }
    // Strip heavy per-question detail off everything but the newest papers.
    for (var i = 0; i < q.attempts.length - DETAIL_KEEP; i++) {
      if (q.attempts[i].detail) delete q.attempts[i].detail;
    }

    var pct = attempt.total ? Math.round(attempt.correct / attempt.total * 100) : 0;

    function tally(key) {
      var u = q.byUnit[key] || { runs: 0, best: 0, totalQ: 0, totalCorrect: 0 };
      u.runs += 1;
      u.totalQ += attempt.total;
      u.totalCorrect += attempt.correct;
      if (pct > u.best) u.best = pct;
      u.last = pct;
      u.lastAt = attempt.at;
      q.byUnit[key] = u;
    }

    // The exact scope keeps its own record ("unit:unit-1:u1-s2", "paper:paper-1").
    tally(attempt.scope);

    // The dashboard tracks mastery under "unit:<id>", so credit every unit the
    // paper actually covered. Without this, sub-section tests and paper/grand
    // mocks never moved the unit mastery bars.
    (attempt.unitIds || []).forEach(function (uid) {
      var key = "unit:" + uid;
      if (key !== attempt.scope) tally(key);
    });

    /* Lifetime accuracy per syllabus sub-section — this is what lets the
       dashboard name the five weakest modules instead of only whole units. */
    var bySub = attempt.bySub || {};
    Object.keys(bySub).forEach(function (sid) {
      var rec = q.bySub[sid] || { total: 0, right: 0, runs: 0 };
      rec.total += bySub[sid].total || 0;
      rec.right += bySub[sid].right || 0;
      rec.runs += 1;
      rec.lastAt = attempt.at;
      q.bySub[sid] = rec;
    });

    write(KEYS.quiz, q);
    logActivity();
    return attempt.id;
  }

  /* Lifetime totals, computed once so several dashboard panels agree. */
  function quizTotals() {
    var attempts = getQuiz().attempts;
    var out = {
      runs: attempts.length, total: 0, correct: 0, attempted: 0, skipped: 0,
      seconds: 0,
      byFormat: { mcq: { total: 0, right: 0 }, tf: { total: 0, right: 0 }, fib: { total: 0, right: 0 } },
      byDiff: { 1: { total: 0, right: 0 }, 2: { total: 0, right: 0 }, 3: { total: 0, right: 0 } }
    };
    attempts.forEach(function (a) {
      out.total += a.total || 0;
      out.correct += a.correct || 0;
      out.attempted += (typeof a.attempted === "number" ? a.attempted : a.total) || 0;
      out.skipped += a.skipped || 0;
      out.seconds += a.seconds || ((a.minutes || 0) * 60);
      ["mcq", "tf", "fib"].forEach(function (f) {
        var r = a.byFormat && a.byFormat[f];
        if (r) { out.byFormat[f].total += r.total || 0; out.byFormat[f].right += r.right || 0; }
      });
      [1, 2, 3].forEach(function (d) {
        var r = a.byDiff && a.byDiff[d];
        if (r) { out.byDiff[d].total += r.total || 0; out.byDiff[d].right += r.right || 0; }
      });
    });
    return out;
  }

  function clearQuizHistory() {
    write(KEYS.quiz, { attempts: [], byUnit: {}, bySub: {} });
  }

  /* ---------- an unfinished paper, so a refresh never loses it ---------- */
  function getQuizResume() {
    var r = read(KEYS.quizResume, null);
    if (!r || !r.qs || !r.qs.length) return null;
    // A paper abandoned more than a day ago is stale; do not offer it back.
    if (Date.now() - (r.savedAt || 0) > 86400000) { clearQuizResume(); return null; }
    return r;
  }
  function setQuizResume(snapshot) { write(KEYS.quizResume, snapshot); }
  function clearQuizResume() {
    try { localStorage.removeItem(KEYS.quizResume); } catch (e) {}
  }

  /* ---------- remembered setup choices ---------- */
  function getQuizPrefs() {
    var p = read(KEYS.quizPrefs, null);
    if (!p || typeof p !== "object") return null;
    return p;
  }
  function setQuizPrefs(p) { write(KEYS.quizPrefs, p || {}); }

  /* ---------- spaced repetition (Leitner boxes 1-5) ---------- */
  function getSrs() { return read(KEYS.srs, {}); }
  function gradeSrs(key, correct) {
    var m = getSrs();
    var item = m[key] || { box: 1, due: 0, wrong: 0, seen: 0 };
    item.seen += 1;
    if (correct) {
      item.box = Math.min(5, item.box + 1);
    } else {
      item.box = 1;
      item.wrong += 1;
    }
    // Box 1..5 → review in 1, 2, 4, 8, 16 days
    var days = Math.pow(2, item.box - 1);
    item.due = Date.now() + days * 86400000;
    m[key] = item;
    write(KEYS.srs, m);
  }
  function dueSrs() {
    var m = getSrs(), now = Date.now(), out = [];
    for (var k in m) if (m[k].due <= now) out.push(k);
    return out;
  }

  /* ---------- activity / streak ---------- */
  function today() {
    var d = new Date();
    return d.getFullYear() + "-" +
      String(d.getMonth() + 1).padStart(2, "0") + "-" +
      String(d.getDate()).padStart(2, "0");
  }
  function getActivity() { return read(KEYS.activity, {}); }
  function logActivity() {
    var m = getActivity();
    var t = today();
    m[t] = (m[t] || 0) + 1;
    write(KEYS.activity, m);
  }
  function computeStreak() {
    var m = getActivity();
    var cur = 0, longest = 0, run = 0;
    var d = new Date();

    if (!m[today()]) d.setDate(d.getDate() - 1);

    for (var i = 0; i < 400; i++) {
      var key = d.getFullYear() + "-" +
        String(d.getMonth() + 1).padStart(2, "0") + "-" +
        String(d.getDate()).padStart(2, "0");
      if (m[key]) { cur++; d.setDate(d.getDate() - 1); }
      else break;
    }
    var days = Object.keys(m).sort();
    for (var j = 0; j < days.length; j++) {
      if (j > 0) {
        var prev = new Date(days[j - 1]), now2 = new Date(days[j]);
        run = ((now2 - prev) / 86400000 === 1) ? run + 1 : 1;
      } else run = 1;
      if (run > longest) longest = run;
    }
    return { current: cur, longest: Math.max(longest, cur), totalDays: days.length };
  }

  /* ---------- misc ---------- */
  function bumpVisits() {
    var n = (read(KEYS.visits, 0) || 0) + 1;
    write(KEYS.visits, n);
    return n;
  }
  function getVisits() { return read(KEYS.visits, 0) || 0; }
  function getLastTopic() { return read(KEYS.lastTopic, null); }
  function setLastTopic(id) { write(KEYS.lastTopic, id); }

  /* ---------- onboarding ---------- */
  function isOnboarded() { return !!read(KEYS.onboarded, false); }
  function setOnboarded() { write(KEYS.onboarded, 1); }
  function resetOnboarding() {
    try { localStorage.removeItem(KEYS.onboarded); } catch (e) {}
  }

  function getQaDone() { return read(KEYS.qaDone, []); }
  function toggleQaDone(id) {
    var a = getQaDone(), i = a.indexOf(id);
    if (i === -1) a.push(id); else a.splice(i, 1);
    write(KEYS.qaDone, a);
    logActivity();
    return i === -1;
  }

  /* ---------- nav position (Desktop) ---------- */
  function getNavPos() { return read(KEYS.navPos, "left"); }
  function setNavPos(pos) {
    write(KEYS.navPos, pos);
    applyNavPos();
  }
  function applyNavPos() {
    var pos = getNavPos();
    if (typeof document !== "undefined" && document.documentElement) {
      document.documentElement.setAttribute("data-nav-pos", pos);
    }
  }

  /* ---------- sidebar collapsed state (Desktop) ---------- */
  function isSidebarCollapsed() { return !!read(KEYS.sidebarCollapsed, false); }
  function setSidebarCollapsed(val) {
    write(KEYS.sidebarCollapsed, !!val);
    applySidebarState();
  }
  function toggleSidebarCollapsed() {
    var next = !isSidebarCollapsed();
    setSidebarCollapsed(next);
    return next;
  }
  function applySidebarState() {
    try {
      if (typeof document !== "undefined" && document.body) {
        if (isSidebarCollapsed()) document.body.classList.add("sidebar-collapsed");
        else document.body.classList.remove("sidebar-collapsed");
      }
    } catch (e) {}
  }

  /* ---------- daily SRS notifications ---------- */
  function getSrsNotify() { return read(KEYS.notifySrs, false); }
  function setSrsNotify(bool) { write(KEYS.notifySrs, !!bool); }
  function getSrsNotifyTime() { return read(KEYS.notifyTime, "19:00"); }
  function setSrsNotifyTime(t) { write(KEYS.notifyTime, t || "19:00"); }

  /* ---------- backup / restore ---------- */
  function backupKeys() {
    var out = [];
    for (var k in KEYS) out.push(KEYS[k]);
    return out;
  }

  function exportBackup() {
    var payload = { _app: "animal-genetics-studio", _version: 1, _at: new Date().toISOString(), data: {} };
    backupKeys().forEach(function (k) {
      var v = localStorage.getItem(k);
      if (v !== null) payload.data[k] = v;
    });
    var blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "animal-genetics-backup-" + today() + ".json";
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }

  function importBackup(file, onDone) {
    var r = new FileReader();
    r.onload = function () {
      try {
        var p = JSON.parse(r.result);
        if (!p || p._app !== "animal-genetics-studio" || !p.data) {
          onDone(false, "That does not look like a valid study backup file.");
          return;
        }
        for (var k in p.data) localStorage.setItem(k, p.data[k]);
        onDone(true, "Restored. Reloading...");
      } catch (e) {
        onDone(false, "The file could not be read.");
      }
    };
    r.readAsText(file);
  }

  function resetAll() {
    backupKeys().forEach(function (k) { localStorage.removeItem(k); });
  }

  /* ---------- Cloud Sync Config & Remote Merge ---------- */
  var DEFAULT_SYNC_DB_URL = "https://vet-pathology-default-rtdb.firebaseio.com";
  var DEFAULT_SYNC_PIN = "350-202";

  function getSyncConfig() {
    var cfg = read(KEYS.syncConfig, null);
    var defaultDevName = (/Mobi|Android|iPhone/i.test(navigator.userAgent) ? "Mobile Phone 📱" : "Tablet / PC 📟");
    if (!cfg || typeof cfg !== "object") {
      cfg = {
        enabled: true,
        dbUrl: DEFAULT_SYNC_DB_URL,
        pin: DEFAULT_SYNC_PIN,
        deviceName: defaultDevName,
        lastSyncedAt: 0,
        autoSync: true
      };
      try { localStorage.setItem(KEYS.syncConfig, JSON.stringify(cfg)); } catch (e) {}
      return cfg;
    }
    var dirty = false;
    if (!cfg.dbUrl || !String(cfg.dbUrl).trim()) {
      cfg.dbUrl = DEFAULT_SYNC_DB_URL;
      if (!cfg.lastSyncedAt) {
        cfg.pin = DEFAULT_SYNC_PIN;
      }
      cfg.enabled = true;
      dirty = true;
    }
    if (!cfg.pin || !String(cfg.pin).trim()) {
      cfg.pin = DEFAULT_SYNC_PIN;
      dirty = true;
    }
    if (!cfg.deviceName) {
      cfg.deviceName = defaultDevName;
      dirty = true;
    }
    if (cfg.autoSync === undefined) {
      cfg.autoSync = true;
      dirty = true;
    }
    if (dirty) {
      try { localStorage.setItem(KEYS.syncConfig, JSON.stringify(cfg)); } catch (e) {}
    }
    return cfg;
  }

  function setSyncConfig(cfg) {
    write(KEYS.syncConfig, cfg);
  }

  function getAllData() {
    return {
      version: 1,
      timestamp: Date.now(),
      read: getRead(),
      bookmarks: getBookmarks(),
      notes: getNotes(),
      highlights: getHighlights(),
      hlColor: getHighlightColor(),
      quiz: getQuiz(),
      srs: getSrs(),
      activity: getActivity(),
      qaDone: getQaDone(),
      lastTopic: getLastTopic()
    };
  }

  function mergeRemoteData(remote) {
    if (!remote || typeof remote !== "object") return false;
    var changed = false;

    // 1. Read status (union of read topics)
    if (remote.read && typeof remote.read === "object") {
      var localRead = getRead();
      var mergedRead = Object.assign({}, localRead);
      var readDirty = false;
      Object.keys(remote.read).forEach(function (tid) {
        var rVal = remote.read[tid];
        if (!mergedRead[tid] || (typeof rVal === "number" && rVal > (mergedRead[tid] || 0))) {
          mergedRead[tid] = rVal;
          readDirty = true;
        }
      });
      if (readDirty) {
        write(KEYS.read, mergedRead);
        changed = true;
      }
    }

    // 2. Bookmarks (union of array)
    if (Array.isArray(remote.bookmarks)) {
      var localBm = getBookmarks();
      var bmSet = {};
      localBm.forEach(function (id) { bmSet[id] = true; });
      var bmDirty = false;
      remote.bookmarks.forEach(function (id) {
        if (!bmSet[id]) {
          bmSet[id] = true;
          bmDirty = true;
        }
      });
      if (bmDirty) {
        write(KEYS.bookmarks, Object.keys(bmSet));
        changed = true;
      }
    }

    // 3. Notes (merge by topicId, keep longer/richer note)
    if (remote.notes && typeof remote.notes === "object") {
      var localNotes = getNotes();
      var mergedNotes = Object.assign({}, localNotes);
      var notesDirty = false;
      Object.keys(remote.notes).forEach(function (tid) {
        var rText = remote.notes[tid];
        if (rText && typeof rText === "string" && rText.trim()) {
          var lText = mergedNotes[tid] || "";
          if (!lText || (rText !== lText && rText.length > lText.length)) {
            mergedNotes[tid] = rText;
            notesDirty = true;
          }
        }
      });
      if (notesDirty) {
        write(KEYS.notes, mergedNotes);
        changed = true;
      }
    }

    // 4. Highlights (union by topicId, deduplicating text)
    if (remote.highlights && typeof remote.highlights === "object") {
      var localHl = getHighlights();
      var mergedHl = Object.assign({}, localHl);
      var hlDirty = false;
      Object.keys(remote.highlights).forEach(function (tid) {
        var listLocal = mergedHl[tid] || [];
        var listRemote = remote.highlights[tid] || [];
        var seen = {};
        var combined = [];
        listLocal.forEach(function (item) {
          var t = typeof item === "string" ? item : (item ? item.text : "");
          var c = typeof item === "object" && item ? item.color : "yellow";
          var occ = typeof item === "object" && item ? item.occ : undefined;
          var prefix = typeof item === "object" && item ? item.prefix : "";
          var suffix = typeof item === "object" && item ? item.suffix : "";
          if (t && !seen[t]) {
            seen[t] = true;
            combined.push({ text: t, color: c, occ: occ, prefix: prefix, suffix: suffix });
          }
        });
        listRemote.forEach(function (item) {
          var t = typeof item === "string" ? item : (item ? item.text : "");
          var c = typeof item === "object" && item ? item.color : "yellow";
          var occ = typeof item === "object" && item ? item.occ : undefined;
          var prefix = typeof item === "object" && item ? item.prefix : "";
          var suffix = typeof item === "object" && item ? item.suffix : "";
          if (t && !seen[t]) {
            seen[t] = true;
            combined.push({ text: t, color: c, occ: occ, prefix: prefix, suffix: suffix });
            hlDirty = true;
          }
        });
        mergedHl[tid] = combined;
      });
      if (hlDirty) {
        write(KEYS.highlights, mergedHl);
        changed = true;
      }
    }

    // 5. Quiz attempts (smart union & stat recomputation)
    if (remote.quiz && Array.isArray(remote.quiz.attempts)) {
      var localQuiz = getQuiz();
      var attemptMap = {};
      (localQuiz.attempts || []).forEach(function (a) {
        if (a && a.id) attemptMap[String(a.id)] = a;
      });
      var newAttemptFound = false;
      remote.quiz.attempts.forEach(function (a) {
        if (a && a.id && !attemptMap[String(a.id)]) {
          attemptMap[String(a.id)] = a;
          newAttemptFound = true;
        }
      });

      if (newAttemptFound) {
        var mergedAttempts = Object.values(attemptMap);
        mergedAttempts.sort(function (a, b) { return (a.at || 0) - (b.at || 0); });
        if (mergedAttempts.length > MAX_ATTEMPTS) {
          mergedAttempts = mergedAttempts.slice(-MAX_ATTEMPTS);
        }
        for (var i = 0; i < mergedAttempts.length - DETAIL_KEEP; i++) {
          if (mergedAttempts[i].detail) delete mergedAttempts[i].detail;
        }

        var recomputedQuiz = {
          attempts: mergedAttempts,
          byUnit: {},
          bySub: {}
        };

        mergedAttempts.forEach(function (att) {
          var pct = att.total ? Math.round(att.correct / att.total * 100) : 0;
          function tally(key) {
            var u = recomputedQuiz.byUnit[key] || { runs: 0, best: 0, totalQ: 0, totalCorrect: 0 };
            u.runs += 1;
            u.totalQ += att.total || 0;
            u.totalCorrect += att.correct || 0;
            if (pct > u.best) u.best = pct;
            u.last = pct;
            u.lastAt = att.at;
            recomputedQuiz.byUnit[key] = u;
          }
          tally(att.scope);
          (att.unitIds || []).forEach(function (uid) {
            var key = "unit:" + uid;
            if (key !== att.scope) tally(key);
          });
          var bySub = att.bySub || {};
          Object.keys(bySub).forEach(function (sid) {
            var rec = recomputedQuiz.bySub[sid] || { total: 0, right: 0, runs: 0 };
            rec.total += bySub[sid].total || 0;
            rec.right += bySub[sid].right || 0;
            rec.runs += 1;
            rec.lastAt = att.at;
            recomputedQuiz.bySub[sid] = rec;
          });
        });

        write(KEYS.quiz, recomputedQuiz);
        changed = true;
      }
    }

    // 6. Spaced Repetition (SRS)
    if (remote.srs && typeof remote.srs === "object") {
      var localSrs = getSrs();
      var mergedSrs = Object.assign({}, localSrs);
      var srsDirty = false;
      Object.keys(remote.srs).forEach(function (qk) {
        var rItem = remote.srs[qk];
        var lItem = mergedSrs[qk];
        if (!lItem || (rItem && rItem.box > lItem.box)) {
          mergedSrs[qk] = rItem;
          srsDirty = true;
        }
      });
      if (srsDirty) {
        write(KEYS.srs, mergedSrs);
        changed = true;
      }
    }

    // 7. Activity & Streak
    if (remote.activity && typeof remote.activity === "object") {
      var localAct = getActivity();
      var mergedAct = Object.assign({}, localAct);
      var actDirty = false;
      Object.keys(remote.activity).forEach(function (dt) {
        var rCnt = remote.activity[dt] || 0;
        var lCnt = mergedAct[dt] || 0;
        if (rCnt > lCnt) {
          mergedAct[dt] = rCnt;
          actDirty = true;
        }
      });
      if (actDirty) {
        write(KEYS.activity, mergedAct);
        changed = true;
      }
    }

    // 8. Practiced Q&A
    if (Array.isArray(remote.qaDone)) {
      var localQa = getQaDone();
      var qaSet = {};
      localQa.forEach(function (id) { qaSet[id] = true; });
      var qaDirty = false;
      remote.qaDone.forEach(function (id) {
        if (!qaSet[id]) {
          qaSet[id] = true;
          qaDirty = true;
        }
      });
      if (qaDirty) {
        write(KEYS.qaDone, Object.keys(qaSet));
        changed = true;
      }
    }

    // 9. Last topic studied
    if (remote.lastTopic && !getLastTopic()) {
      write(KEYS.lastTopic, remote.lastTopic);
    }

    if (changed) {
      try {
        window.dispatchEvent(new CustomEvent("vgen-store-updated", { detail: { remote: true } }));
      } catch (e) {}
    }

    return changed;
  }

  /* ---------- public API ---------- */
  return {
    KEYS: KEYS,
    getTheme: getTheme, setTheme: setTheme, applyTheme: applyTheme,
    getDetail: getDetail, setDetail: setDetail,
    getRead: getRead, isRead: isRead, toggleRead: toggleRead,
    getBookmarks: getBookmarks, isBookmarked: isBookmarked, toggleBookmark: toggleBookmark,
    getNotes: getNotes, getNote: getNote, setNote: setNote,
    getHighlights: getHighlights, addHighlight: addHighlight, removeHighlight: removeHighlight,
    getHighlightColor: getHighlightColor, setHighlightColor: setHighlightColor, VALID_HL_COLORS: VALID_HL_COLORS,
    getQuiz: getQuiz, saveAttempt: saveAttempt, getAttempt: getAttempt,
    quizTotals: quizTotals, clearQuizHistory: clearQuizHistory,
    getQuizResume: getQuizResume, setQuizResume: setQuizResume, clearQuizResume: clearQuizResume,
    getQuizPrefs: getQuizPrefs, setQuizPrefs: setQuizPrefs,
    getSrs: getSrs, gradeSrs: gradeSrs, dueSrs: dueSrs,
    getActivity: getActivity, logActivity: logActivity, computeStreak: computeStreak,
    bumpVisits: bumpVisits, getVisits: getVisits,
    getLastTopic: getLastTopic, setLastTopic: setLastTopic,
    isOnboarded: isOnboarded, setOnboarded: setOnboarded, resetOnboarding: resetOnboarding,
    getQaDone: getQaDone, toggleQaDone: toggleQaDone,
    getNavPos: getNavPos, setNavPos: setNavPos, applyNavPos: applyNavPos,
    isSidebarCollapsed: isSidebarCollapsed, setSidebarCollapsed: setSidebarCollapsed,
    toggleSidebarCollapsed: toggleSidebarCollapsed, applySidebarState: applySidebarState,
    getSrsNotify: getSrsNotify, setSrsNotify: setSrsNotify,
    getSrsNotifyTime: getSrsNotifyTime, setSrsNotifyTime: setSrsNotifyTime,
    getSyncConfig: getSyncConfig, setSyncConfig: setSyncConfig,
    getAllData: getAllData, mergeRemoteData: mergeRemoteData,
    backupKeys: backupKeys, exportBackup: exportBackup, importBackup: importBackup,
    resetAll: resetAll,
    today: today
  };
})();

if (typeof window !== "undefined") {
  store.applyTheme();
  store.applyNavPos();
  store.applySidebarState();
}
