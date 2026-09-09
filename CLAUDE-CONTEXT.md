# CONTEXT — Animal Genetics and Breeding Studio

Read this whole file before doing anything else. It tells you who I am, what we are
building, the codebase layout, my conventions, and how I prefer to work. After reading,
say "Got it — what do you want to work on?" and wait for my actual task.

**Last updated:** 2026-09-09 (Full VCI MSVE 2016 104-topic skeleton, dual paper readiness, 100+ term glossary, offline PWA)

---

## 👤 ABOUT ME

- **Name:** Fazal Zama
- **Role:** B.V.Sc & A.H. UG student at ICAR — Indian Veterinary Research Institute (IVRI), Bareilly (Roll No. B0-350-2025)
- **Background:** Veterinary science — **NOT a coder.** Explain in plain English with
  concrete file paths and simple steps.
- **Tools I use:** Windows PC, GitHub Desktop (not command-line git), File Explorer.
  I do NOT use a terminal. Give me GUI instructions or one-click `.bat` scripts.
- **Developer Credit:** `Mr. Fazal Zama · Developer · B.V.Sc & A.H. UG · Roll No. B0-350-2025 · vet.fazalzama@gmail.com`

---

## 🎯 WHAT WE ARE BUILDING

**Animal Genetics and Breeding Studio** — a free, comprehensive academic study companion website for
**B.V.Sc & A.H. second-year Animal Genetics and Breeding**, strictly aligned with the official
Veterinary Council of India (VCI) MSVE 2016 syllabus (Credit hours 3+1 = 4) as published
in the Gazette of India.

- **Authoritative syllabus source:** `Animal Genetics outline.pdf` (in project root)
- **Architecture blueprint:** `NEW-SUBJECT-BLUEPRINT.md`
- **Working folder:** `D:/ANIMAL GENETICS APPLICATION/`
- **Sister projects:**
  - `D:/PATHOLOGY APPLICATION/` (Veterinary Pathology Studio — reference only, **DO NOT EDIT**)
  - `D:/ANIMAL NUTRITION APPLICATION/` (Animal Nutrition Studio)
  - `D:/VET MICROBIOLOGY APPLICATION/` (Veterinary Microbiology Studio)
  - `D:/VET BIOCHEMISTRY/` (Veterinary Biochemistry Studio)
  - Anatomy Studio (Live at `https://veterinaryanatomy.com/`)

This project follows the exact proven architecture, three-layer navigation model, and
**shared IVRI Academic light theme** used across the veterinary studio series.

### The 8 Core Sections
1. **Theory** — Units 1–3 of the official VCI theory syllabus (79 topics total).
2. **Practical** — Units 1–3 of the official practical syllabus (25 laboratory practicals total).
3. **WHY** — Comparative species mechanism-first genetic, population, and breeding explanations.
4. **Question & Answer** — Written-exam practice: short notes, long answers, differentiate-between tables, definitions, and numerical problems.
5. **Quiz** — MCQ / True-False / Fill-blank, with unit-wise, paper-wise, grand mock test, practical, Exam Mode (timed) and Smart Review (spaced repetition).
6. **Dashboard** — Dual VCI Board Exam readiness gauges (Paper I vs Paper II), 6-Unit Mastery Matrix, streak tracker, 84-day heatmap, and 5-box Leitner memory pipeline (0–1000 XP Genetics Mastery Index).
7. **Library** — Bookmarks · Personal Notes · Multi-colour Highlights · 100+ Term UG Animal Genetics Glossary with SpeechSynthesis audio pronunciation.
8. **Settings** — Theme selection (Light canonical default, optional Dark), data backup/restore (JSON), and about modal.

### Exam Structure (VCI Annual Board Examination)
| Examination Paper | Theory Units | Practical Units | Theory Marks | Practical Marks | Syllabus Weightage |
|---|---|---|---|---|---|
| **Paper I** | Units 1 & 2 (Biostatistics & Computer Application, Principles of Animal & Population Genetics) | Practicals 1 & 2 | 100 Marks | 60 Marks | 20% |
| **Paper II** | Unit 3 (Principles of Animal Breeding) | Practical 3 | 100 Marks | 60 Marks | 20% |

### Syllabus Breakdown (104 Topics Total)
- **Theory Unit 1: Biostatistics and Computer Application (22 topics, `u1-t01` – `u1-t22`):**
  Importance of biostatistics in veterinary science; classification and tabulation of biological data; parameter, statistic and observation; diagrammatic and graphical representation; measures of central tendency (mean, median, mode); measures of dispersion (range, quartile deviation, mean deviation, variance, standard deviation); coefficient of variation and standard error; moments, skewness and kurtosis; probability theory and theorems; Binomial and Poisson distributions; Normal distribution and standard normal curve; Pearson's and Spearman's correlation; linear regression equations and coefficients; sampling methods (random, stratified, systematic, cluster); large sample Z-test; Student's t-test (one-sample, two-sample, paired); Chi-square (χ²) test of goodness of fit and independence; experimental designs (principles of design, CRD, RBD); Analysis of Variance (ANOVA) and F-test; non-parametric tests; computer applications and DBMS; MS-Office and biological data analysis in MS-Excel.
- **Theory Unit 2: Principles of Animal and Population Genetics (29 topics, `u2-t01` – `u2-t29`):**
  History and development of genetics; mitosis vs meiosis; chromosome numbers and karyotyping in livestock and poultry; Mendelian principles (segregation, independent assortment); modified Mendelian inheritance (incomplete dominance, codominance, lethals); gene interactions and epistasis; pleiotropy, penetrance and expressivity; multiple alleles and blood groups; sex determination and dosage compensation; sex-linked, sex-limited and sex-influenced inheritance; linkage, crossing over and linkage maps; gene mutations; chromosomal aberrations (numerical and structural); cytogenetics and banding; extra-chromosomal inheritance; molecular genetics (nucleic acids structure and function); gene concept and DNA replication; molecular techniques (PCR, RFLP, sequencing); population genetics introduction; genetic structure (gene and genotypic frequencies); Hardy-Weinberg law and equilibrium; forces changing gene frequencies (mutation, migration, selection, drift); qualitative vs quantitative genetics; average effect, gene substitution and breeding value; components of phenotypic variance; genotype-environment (GxE) interaction; heritability; repeatability; genetic and phenotypic correlations.
- **Theory Unit 3: Principles of Animal Breeding (28 topics, `u3-t01` – `u3-t28`):**
  History of animal breeding; classification of breeds; economic traits of livestock and poultry; selection principles and response; bases of selection (individual, pedigree, family, sib, progeny); combined and indirect selection; methods of selection (tandem, independent culling, selection index); mating systems classification; inbreeding coefficient and coefficient of relationship; genetic and phenotypic consequences of inbreeding; outbreeding systems (crossbreeding, grading up); heterosis and hybrid vigour; selection for combining ability (RS, RRS); breeding strategies for dairy cattle and buffalo; breeding strategies for sheep, goat, swine; commercial poultry breeding; sire evaluation methods (contemporary comparison, BLUP); open nucleus breeding system (ONBS); breed synthesis; national and state breeding policies; animal genetic resources (AnGR) conservation; reproductive and biotechnological tools (AI, MOET, genomic selection); breeding for disease resistance; pet animal breeding (dog and cat breeds, pedigree sheets); breeding management of dogs and cats; pet birds breeding; wildlife population dynamics and effective population size (Ne); planned and controlled breeding of wildlife.
- **Practical Units 1–3 (25 laboratory practicals, `p1-t01` – `p3-t06`):**
  - *Practical Unit 1 (11 practicals):* Data compilation and tabulation; graphical presentation; central tendency calculations; dispersion and CV estimation; probability and normal curve problems; correlation and regression analysis; Z-test; Student's t-test; Chi-square test; ANOVA for CRD and RBD; MS-Excel biological analysis.
  - *Practical Unit 2 (8 practicals):* Monohybrid and dihybrid crosses; modified ratios and sex linkage; linkage and crossing over estimation; demonstration of karyotyping; gene and genotypic frequency calculation; testing Hardy-Weinberg equilibrium; effects of evolutionary forces; heritability and repeatability estimation.
  - *Practical Unit 3 (6 practicals):* Selection differential, intensity and generation interval; expected genetic gain and correlated response; EPA and MPPA computation; inbreeding and relationship coefficient from pedigree; heterosis estimation; sire indices and selection index construction.

---

## 🎨 THE SHARED IVRI THEME — DO NOT TOUCH COLOURS

All IVRI subject platforms (Anatomy, Pathology, Animal Nutrition, Genetics, Biochemistry, Microbiology)
share one standardised visual design system: **The Academic Light Theme** (institutional
medical blue on a soft blue-grey ground, typography in Inter + JetBrains Mono).

### The Rules
1. **`assets/css/tokens.css` is the single source of truth.** Every colour, font size, border,
   radius, shadow, and spacing value in the whole application comes from it.
2. **`tokens.css` is copied byte-for-byte from the reference project.** Never re-theme per subject.
3. **Never hard-code a hex value anywhere else.** If a colour is needed, use an existing token.
4. **Light is the default and canonical theme.** Dark mode exists solely as a night-reading
   option the student must explicitly select in Settings (`#/me`).
5. Only the **brand mark letters** (`AG`), **site title**, and `<meta name="theme-color">` change.

### The Palette (Token Values)
| Token | Value (Light) | Used For |
|---|---|---|
| `--ivri-blue` | `#1565c0` | **Primary.** Theory, Dashboard, links, brand mark `AG` |
| `--ivri-teal` | `#00897b` | Practical / Lab / Cytogenetics |
| `--ivri-purple` | `#6a48b5` | WHY / Mechanisms / Q&A Model Answers |
| `--ivri-amber` | `#b25e00` | Quiz / Assessment / Sprints (darkened for contrast) |
| `--ivri-coral` | `#d84315` | Warning / High-yield alerts |
| `--ivri-sage` | `#2e7d32` | Success / Memory Safe / Clinical notes |
| `--bg` | `#f0f4f8` | Page ground (soft medical blue-grey, never stark white) |
| `--surface` | `#ffffff` | Cards, modals, dialogs |

---

## 🗂️ FILE STRUCTURE

```
D:\ANIMAL GENETICS APPLICATION\
├── 1-CLICK-PUSH-TO-GITHUB.bat 🌟 Auto-syncs, stages, commits & pushes to GitHub
├── SYNC-TO-REPO.bat           Local offline robocopy mirror into repo/
├── index.html                 Single-page app shell. All sections live here.
├── manifest.json              PWA manifest (theme-color #1565c0)
├── service-worker.js          Offline cache (CACHE_VERSION = "vgen-v1")
├── README.md                  Content writing guide
├── REPO.md                    GitHub repository guide
├── CLAUDE-CONTEXT.md          THIS FILE (AI reads this first)
├── NEW-SUBJECT-BLUEPRINT.md   Architecture blueprint and specifications
├── Animal Genetics outline.pdf Authoritative VCI syllabus source document
│
├── repo/                      📦 PRISTINE MIRROR FOR GITHUB / USB SHARING
│   └── (Exact mirror of assets/, data/, images/, js/, tools/ and root files)
│
├── data/                      ← ALL CONTENT LIVES HERE
│   ├── data-syllabus.JS       Master index: units, topic titles, exam papers (104 topics)
│   ├── data-theory-unit1.JS   Unit 1: Biostatistics & Computer Application (22 topics)
│   ├── data-theory-unit2.JS   Unit 2: Principles of Animal & Population Genetics (29 topics)
│   ├── data-theory-unit3.JS   Unit 3: Principles of Animal Breeding (28 topics)
│   ├── data-practical.JS      All 3 practical units (25 topics)
│   ├── data-why.JS            Mechanism-first WHY entries
│   ├── data-qa.JS             Written-exam Q&A bank
│   ├── data-quiz.JS           Quiz question bank
│   └── events-data.js         Department announcements & academic updates
│
├── js/
│   ├── store.js               localStorage layer with "vgen-" prefix
│   ├── app.js                 Router + shell + section renderers + highlighter
│   ├── quiz.js                Quiz engine (window.quizApp)
│   ├── dashboard.js           Analytics & dual paper readiness (window.dashboardApp)
│   ├── glossary.js            100+ term UG dictionary + tooltip decorator + SpeechSynthesis
│   ├── search.js              Global search engine (Ctrl+K)
│   ├── deep-guide.js          Deep diagnostic guide overlay
│   └── events.js              Department announcements renderer
│
├── assets/css/
│   ├── tokens.css             ★ SHARED IVRI THEME — copy verbatim, never edit
│   ├── main.css               Reset, layout, shared components, sidebar
│   ├── sections.css           Lesson, quiz, dashboard, Q&A, and library views
│   ├── animations.css         GPU-accelerated micro-interactions
│   ├── deep-guide.css         Deep guide presentation styles
│   └── events.css             Interactive challenge card styles
│
├── images/                    theory/ practical/ why/ qa/
└── tools/
    ├── start-server.bat       Double-click → http://localhost:5179
    ├── local-server.js        Zero-dependency Node server
    ├── make-data-files.bat    Double-click → scaffolds new topic blocks
    ├── make-data-files.py     Python topic scaffolding engine
    └── sync-repo.bat          Double-click → refreshes repo/ folder
```

---

## ✍️ CONTENT WRITING STANDARD (FOR CONTENT EXPANSION)

**Target: enough for rank 1 and 10 CGPA at UG level. No PhD detail unless it genuinely
explains something. Complete UG coverage, but nothing irrelevant.**

- **`desc` (Standard view) = the complete exam answer.** Well organised, scannable,
  everything needed to write a full-marks answer. This is what I actually revise from.
- **`eliteDesc` (Deep view) = mechanism depth for toppers.** Put the extra here so it
  never clutters the answer I would write. Only include it where it explains *why*.
- **`keyPoints` = marks-scoring lines**, written so they can be lifted straight into an
  answer. Aim for 10–18 per topic.
- **`tables` = comparisons that get asked directly** (X vs Y). Aim for 2–3 per topic.
- **`clinical` = an applied note at the bottom of EVERY topic.** Written for Indian
  practice: name the breeds, field breeding policies, herd data conditions, and practical breeding decisions.
- Use ALL-CAPS bold for section headers inside `desc`, and `<ul><li>` for lists.
- HTML allowed in content fields: `<b> <i> <br> <ul> <li> <ol> <p> <sup>`.

### Mandatory Content Boundaries
- **No Darwinian theory, evolutionary-origin explanations, ancestry narratives, or
  phylogenetic speculation.** Do not say a structure "evolved from" an ancestral species.
  Keep explanations on established Mendelian genetics, cytogenetics, molecular biology, present breed characteristics,
  selection mechanics, and breeding strategies. The descriptive term "vestigial" is acceptable without an ancestral narrative.
- **Religious and mythological neutrality.** No deities, worship stories, or
  mythology-based explanations.
- **Analogy boundary.** Do not use alcohol, intoxication or alcoholic drinks as
  analogies, mnemonics or examples.
- **Preserving content depth:** Never replace a complete `desc`, `eliteDesc`, or `answer` field with a shorter summary.

---

## 🛠️ DEPLOYMENT & GITHUB WORKFLOW

1. **Daily 1-Click Publishing:**
   - Double-click `1-CLICK-PUSH-TO-GITHUB.bat`.
   - It runs robocopy to mirror the app into `repo/`, stages changes, commits with timestamp, and pushes to remote `main`.
2. **Local Mirror Tool:**
   - Run `SYNC-TO-REPO.bat` whenever an offline mirror is required for USB distribution.
3. **Cache Bumping:**
   - Bump `CACHE_VERSION` in `service-worker.js` (`vgen-v1` → `vgen-v2`) before every major release.
