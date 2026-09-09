# Animal Genetics and Breeding Studio

A modern, fast, offline-first curriculum companion for **B.V.Sc & A.H. second-year Animal Genetics and Breeding**, following the official VCI MSVE syllabus (Credit hours 3+1 = 4). Built in pure vanilla JavaScript, HTML, and CSS — zero build steps, zero npm dependencies, zero complex toolchains.

---

## How to Run It

### Option A — Instant Local Server (Recommended)
Double-click **`tools/start-server.bat`**.
Open your browser to:
```
http://localhost:5179
```
*(Press `Ctrl+C` in the command window to stop the server).*

### Option B — Direct Double-Click
Double-click **`index.html`** in File Explorer. Every route, lesson reader, quiz runner, and dashboard view runs directly from `file:///`.

---

## Project Structure

```
D:\ANIMAL GENETICS APPLICATION\
│
├── index.html                 Single-page application shell.
├── manifest.json              PWA manifest (standalone, theme-color #1565c0).
├── service-worker.js          Offline caching (CACHE_VERSION = "vgen-v1").
├── 1-CLICK-PUSH-TO-GITHUB.bat Double-click → syncs repo, stages, commits, and pushes to GitHub!
├── SYNC-TO-REPO.bat           Double-click → mirrors all files into repo/ sequentially.
├── README.md                  This content guide.
├── REPO.md                    Student repository & GitHub guide.
├── CLAUDE-CONTEXT.md          The project's living context memory file.
├── NEW-SUBJECT-BLUEPRINT.md   Architecture blueprint and specifications.
├── Animal Genetics outline.pdf Authoritative VCI syllabus source document.
│
├── repo/                      📦 PRISTINE MIRROR FOLDER FOR DRAG-AND-DROP UPLOADS
│   ├── assets/                Sequential copy of assets/
│   ├── data/                  Sequential copy of data/
│   ├── images/                Sequential copy of images/
│   ├── js/                    Sequential copy of js/
│   └── tools/                 Sequential copy of tools/
│
├── data/                      ← ★ ALL SUBJECT CONTENT LIVES HERE ★
│   ├── data-syllabus.JS       Master index: units, topic titles, exam papers (104 topics)
│   ├── data-theory-unit1.JS   Unit 1: Biostatistics & Computer Application (22 topics)
│   ├── data-theory-unit2.JS   Unit 2: Principles of Animal & Population Genetics (29 topics)
│   ├── data-theory-unit3.JS   Unit 3: Principles of Animal Breeding (28 topics)
│   ├── data-practical.JS      All 3 practical units (25 practicals)
│   ├── data-why.JS            Mechanism-first comparative "WHY" entries
│   ├── data-qa.JS             Written-exam practice bank (Short notes, Long answers, etc.)
│   ├── data-quiz.JS           MCQ / True-False / Fill-in-the-Blank question bank
│   └── events-data.js         Department announcements & academic updates
│
├── js/                        ← Application Engines (Vanilla JS)
│   ├── store.js               localStorage layer with "vgen-" prefix
│   ├── app.js                 Router, page renderers, highlighter, and audio reader
│   ├── quiz.js                Quiz engine with Paper I, Paper II, Grand Test, & SRS
│   ├── dashboard.js           Analytics, dual exam readiness, & Leitner memory pipeline
│   ├── glossary.js            100+ Animal Genetics terms dictionary with SpeechSynthesis
│   ├── search.js              Global Ctrl+K instant search engine
│   ├── deep-guide.js          Deep diagnostic guide overlay
│   └── events.js              Department announcements renderer
│
├── assets/                    ← Design System (Copied Verbatim)
│   └── css/
│       ├── tokens.css         Academic Light Medical Blue Theme tokens
│       ├── main.css           Base reset, typography, and responsive layout
│       ├── sections.css       Lesson view, quiz cards, dashboard, and library
│       ├── deep-guide.css     Diagnostic modal styles
│       ├── events.css         Department events presentation styles
│       └── animations.css     Hardware-accelerated micro-interactions
│
└── tools/                     ← Student Automation Scripts
    ├── start-server.bat       Instant local HTTP server (Port 5179)
    ├── local-server.js        Zero-dependency Node HTTP server
    ├── make-data-files.bat    Regenerates empty topic templates from syllabus
    ├── make-data-files.py     Python topic scaffolding engine
    └── sync-repo.bat          Local folder sync script
```

---

## Content Writing Guide

When adding content to any topic in `data/data-theory-unit*.JS` or `data/data-practical.JS`:

```js
theoryData["unit-1"]["u1-t01"] = {
  summary:   "One clear sentence capturing the core definition or concept.",
  desc:      "Full UG university exam answer. Use ALL-CAPS bold for headings, lists with <ul><li>, and concise explanations.",
  eliteDesc: "Deep quantitative/molecular mechanism for topper ranking. Leave empty if standard desc is sufficient.",
  keyPoints: [
    "High-scoring point 1 directly scoreable in VCI exams.",
    "High-scoring point 2 with key formulas, numericals, or thresholds."
  ],
  clinical:  "Applied field or clinical significance under Indian livestock conditions.",
  tables:    [
    {
      title: "Comparison of Method X versus Method Y",
      headers: ["Parameter", "Method X", "Method Y"],
      rows: [
        ["Sample Size Requirement", "Small (n < 30)", "Large (n >= 30)"],
        ["Assumed Population Variance", "Unknown (estimated via s)", "Known or large sample"]
      ]
    }
  ],
  img:       "",
  tags:      ["biostatistics", "hypothesis-testing"]
};
```

---

## Developer Credit

- **Developer:** Mr. Fazal Zama &middot; B.V.Sc & A.H. UG Student &middot; ICAR — Indian Veterinary Research Institute (IVRI), Bareilly &middot; Roll No. B0-350-2025
- **Contact:** [vet.fazalzama@gmail.com](mailto:vet.fazalzama@gmail.com)
