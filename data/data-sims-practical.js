/* ============================================================
   data-sims-practical.js — Practical Units 1, 2 & 3 Lab Benches
   Covers 100% of all 25 Practical topics: p1-t01 .. p3-t06
   ============================================================ */
(function () {
  "use strict";
  if (!window.simEngine) return;

  window.simEngine.registerTopics({
    /* ---- PRACTICAL UNIT 1 (11 Labs: p1-t01 .. p1-t11) ---- */
    "p1-t01": {
      type: "central_dispersion",
      tag: "PRACTICAL 1 · DATA TABULATION BENCH",
      title: "Virtual Bench: Compilation & Spread of Herd Milk Yield Data",
      interactiveCanvas: true,
      controls: [
        { id: "outlier", type: "slider", label: "Edit Highest Record (L)", min: 10, max: 40, step: 0.5, value: 18, format: function (v) { return v + " L"; } },
        { id: "sampleSize", type: "slider", label: "Records Compiled (n)", min: 5, max: 80, step: 5, value: 20, format: function (v) { return "n = " + v; } }
      ]
    },
    "p1-t02": {
      type: "prob_distributions",
      tag: "PRACTICAL 1 · GRAPHICAL LAB",
      title: "Virtual Bench: Histogram, Bar Diagram & Frequency Curve",
      animated: false,
      controls: [
        { id: "dist", type: "toggle", label: "Diagram Type", value: "binomial", options: [
          { value: "binomial", label: "Bar / Histogram" }, { value: "normal", label: "Frequency Curve" }, { value: "poisson", label: "Rare Event Bars" }
        ]},
        { id: "n", type: "slider", label: "Class Bins (n)", min: 5, max: 18, step: 1, value: 10, format: function (v) { return v + " bins"; } }
      ]
    },
    "p1-t03": {
      type: "central_dispersion",
      tag: "PRACTICAL 1 · CENTRAL TENDENCY CALC",
      title: "Virtual Calculator: Mean, Median & Mode (With Live Outlier Test)",
      interactiveCanvas: true,
      controls: [
        { id: "outlier", type: "slider", label: "Test Extreme Value", min: 8, max: 42, step: 0.5, value: 22, format: function (v) { return v + " L"; } },
        { id: "sampleSize", type: "slider", label: "Sample Size (n)", min: 6, max: 60, step: 2, value: 12, format: function (v) { return "n = " + v; } }
      ]
    },
    "p1-t04": {
      type: "central_dispersion",
      tag: "PRACTICAL 1 · DISPERSION & CV% CALC",
      title: "Virtual Calculator: SD, Variance (s²), CV% & Standard Error (SEM)",
      interactiveCanvas: true,
      controls: [
        { id: "outlier", type: "slider", label: "Spread / Outlier Value", min: 10, max: 42, step: 0.5, value: 25, format: function (v) { return Number(v).toFixed(1); } },
        { id: "sampleSize", type: "slider", label: "Sample Size (n for SEM)", min: 4, max: 100, step: 4, value: 16, format: function (v) { return "n = " + v; } }
      ]
    },
    "p1-t05": {
      type: "prob_distributions",
      tag: "PRACTICAL 1 · PROBABILITY & NORMAL BENCH",
      title: "Virtual Calculator: Standard Normal Z-Score & Area Under Curve",
      animated: false,
      controls: [
        { id: "dist", type: "toggle", label: "Problem Type", value: "normal", options: [
          { value: "normal", label: "Normal Curve Z" }, { value: "binomial", label: "Binomial" }, { value: "poisson", label: "Poisson" }
        ]},
        { id: "z", type: "slider", label: "Z-Score Lookup", min: -3.0, max: 3.0, step: 0.05, value: 1.64, format: function (v) { return "Z = " + Number(v).toFixed(2); } }
      ]
    },
    "p1-t06": {
      type: "corr_regression",
      tag: "PRACTICAL 1 · CORRELATION & REGRESSION BENCH",
      title: "Virtual Bench: Interactive Scatter, Pearson r, Spearman ρ & Y = a + bX",
      interactiveCanvas: true,
      controls: [
        { id: "r", type: "slider", label: "Experimental Correlation (r)", min: -0.95, max: 0.98, step: 0.02, value: 0.88, format: function (v) { return "r = " + Number(v).toFixed(2); } }
      ]
    },
    "p1-t07": {
      type: "hypothesis_test",
      tag: "PRACTICAL 1 · Z-TEST BENCH",
      title: "Virtual Bench: Large Sample Z-Test Significance Calculator",
      animated: false,
      defaultTest: "z",
      controls: [
        { id: "stat", type: "slider", label: "Calculated Z-Value", min: -3.6, max: 3.6, step: 0.05, value: 2.15, format: function (v) { return "Z = " + Number(v).toFixed(2); } },
        { id: "alpha", type: "toggle", label: "Significance Level", value: "0.05", options: [{ value: "0.05", label: "α = 0.05" }, { value: "0.01", label: "α = 0.01" }] }
      ]
    },
    "p1-t08": {
      type: "hypothesis_test",
      tag: "PRACTICAL 1 · STUDENT'S t-TEST BENCH",
      title: "Virtual Bench: One-Sample, Two-Sample & Paired t-Test Calculator",
      animated: false,
      defaultTest: "t",
      controls: [
        { id: "stat", type: "slider", label: "Calculated t-Value", min: -4.0, max: 4.0, step: 0.05, value: 2.50, format: function (v) { return "t = " + Number(v).toFixed(2); } },
        { id: "df", type: "slider", label: "Degrees of Freedom (df)", min: 2, max: 30, step: 1, value: 12, format: function (v) { return "df = " + v; } },
        { id: "alpha", type: "toggle", label: "α Level", value: "0.05", options: [{ value: "0.05", label: "α = 0.05" }, { value: "0.01", label: "α = 0.01" }] }
      ]
    },
    "p1-t09": {
      type: "hypothesis_test",
      tag: "PRACTICAL 1 · CHI-SQUARE BENCH",
      title: "Virtual Bench: Chi-Square (χ²) Goodness-of-Fit & Independence Calculator",
      animated: false,
      defaultTest: "chisq",
      controls: [
        { id: "ratio", type: "toggle", label: "Ratio to Test", value: "3:1", options: [{ value: "3:1", label: "3:1 (df=1)" }, { value: "9:3:3:1", label: "9:3:3:1 (df=3)" }] },
        { id: "stat", type: "slider", label: "Observed Deviation", min: 0, max: 4.5, step: 0.25, value: 1.75, format: function (v) { return "Dev ×" + Number(v).toFixed(2); } },
        { id: "alpha", type: "toggle", label: "α Level", value: "0.05", options: [{ value: "0.05", label: "α = 0.05" }, { value: "0.01", label: "α = 0.01" }] }
      ]
    },
    "p1-t10": {
      type: "exp_design",
      tag: "PRACTICAL 1 · ANOVA CRD/RBD BENCH",
      title: "Virtual ANOVA Table Calculator: CRD vs RBD Feeding Trial",
      animated: false,
      controls: [
        { id: "design", type: "toggle", label: "Design", value: "rbd", options: [{ value: "crd", label: "CRD (One-Way)" }, { value: "rbd", label: "RBD (Two-Way)" }] },
        { id: "trtEffect", type: "slider", label: "Diet Effect", min: 0.5, max: 6.0, step: 0.5, value: 3.5, format: function (v) { return Number(v).toFixed(1) + " L"; } },
        { id: "blockNoise", type: "slider", label: "Block Gradient", min: 0.5, max: 7.0, step: 0.5, value: 4.5, format: function (v) { return Number(v).toFixed(1) + " L"; } }
      ]
    },
    "p1-t11": {
      type: "sampling_excel",
      submode: "excel",
      tag: "PRACTICAL 1 · MS-EXCEL LAB",
      title: "Virtual MS-Excel Veterinary Statistics Formula Workbench",
      animated: false,
      controls: [
        { id: "formula", type: "toggle", label: "Excel Formula", value: "AVERAGE", options: [
          { value: "AVERAGE", label: "=AVERAGE" }, { value: "STDEV.S", label: "=STDEV.S" },
          { value: "TTEST", label: "=T.TEST" }, { value: "CHISQ.TEST", label: "=CHISQ.TEST" }
        ]}
      ]
    },

    /* ---- PRACTICAL UNIT 2 (8 Labs: p2-t01 .. p2-t08) ---- */
    "p2-t01": {
      type: "mendelian_epistasis",
      tag: "PRACTICAL 2 · MENDELIAN CROSSES LAB",
      title: "Virtual Punnett Bench: Monohybrid (3:1), Test Cross (1:1) & Dihybrid (9:3:3:1)",
      animated: false,
      controls: [
        { id: "cross", type: "toggle", label: "Cross Exercise", value: "dihybrid", options: [
          { value: "mono", label: "Monohybrid 3:1" }, { value: "test", label: "Test Cross 1:1" }, { value: "dihybrid", label: "Dihybrid 9:3:3:1" }
        ]}
      ]
    },
    "p2-t02": {
      type: "mendelian_epistasis",
      tag: "PRACTICAL 2 · MODIFIED RATIOS & EPISTASIS",
      title: "Virtual Bench: Incomplete Dominance, Lethals & Epistasis Ratios",
      animated: false,
      controls: [
        { id: "cross", type: "select", label: "Modified Ratio Problem", value: "epi_rec", options: [
          { value: "incomplete", label: "Andalusian Fowl (1:2:1)" },
          { value: "codom", label: "Shorthorn Roan (1:2:1)" },
          { value: "lethal", label: "Dexter Bulldog Lethal (2:1)" },
          { value: "epi_rec", label: "Recessive Epistasis 9:3:4 (Labrador)" },
          { value: "epi_dom", label: "Dominant Epistasis 12:3:1" },
          { value: "epi_comp", label: "Complementary 9:7" },
          { value: "epi_dup", label: "Duplicate 15:1" },
          { value: "comb", label: "Poultry Comb Shape 9:3:3:1" }
        ]}
      ]
    },
    "p2-t03": {
      type: "mitosis_meiosis_3d",
      is3D: true,
      autoPlay: true,
      tag: "PRACTICAL 2 · 3D LINKAGE & CROSSING-OVER",
      title: "3D Chiasma Crossing-Over & Recombinant Gamete Lab",
      controls: [
        { id: "division", type: "toggle", label: "Process", value: "meiosis", options: [{ value: "meiosis", label: "Meiotic Crossing-Over" }] },
        { id: "nondisj", type: "toggle", label: "Disjunction", value: "off", options: [{ value: "off", label: "Normal" }, { value: "on", label: "Nondisjunction" }] }
      ],
      steps: [
        { label: "Synapsis & Chiasma", apply: function (st) { st.params.stage = 1; } },
        { label: "Metaphase I", apply: function (st) { st.params.stage = 2; } },
        { label: "Anaphase I", apply: function (st) { st.params.stage = 3; } },
        { label: "4 Recombinant Gametes", apply: function (st) { st.params.stage = 4; } }
      ]
    },
    "p2-t04": {
      type: "karyotype_3d",
      is3D: true,
      autoPlay: true,
      tag: "PRACTICAL 2 · 3D KARYOTYPING LAB",
      title: "Virtual Cytogenetics Bench: Livestock & Poultry Karyotyping (2n)",
      controls: [
        { id: "species", type: "select", label: "Sample Species", value: "cattle", options: [
          { value: "cattle", label: "Cattle (2n=60)" }, { value: "rbuffalo", label: "River Buffalo (2n=50)" },
          { value: "sbuffalo", label: "Swamp Buffalo (2n=48)" }, { value: "sheep", label: "Sheep (2n=54)" },
          { value: "goat", label: "Goat (2n=60)" }, { value: "horse", label: "Horse (2n=64)" },
          { value: "pig", label: "Pig (2n=38)" }, { value: "dog", label: "Dog (2n=78)" },
          { value: "cat", label: "Cat (2n=38)" }, { value: "chicken", label: "Chicken (2n=78 ZZ/ZW)" }
        ]},
        { id: "morph", type: "toggle", label: "Centromere Type", value: "acrocentric", options: [
          { value: "metacentric", label: "Metacentric" }, { value: "submetacentric", label: "Submetacentric" },
          { value: "acrocentric", label: "Acrocentric" }, { value: "telocentric", label: "Telocentric" }
        ]}
      ]
    },
    "p2-t05": {
      type: "hardy_weinberg",
      tag: "PRACTICAL 2 · GENE FREQUENCY CALC",
      title: "Virtual Calculator: Gene (p, q) & Genotypic (p², 2pq, q²) Frequencies",
      animated: false,
      controls: [
        { id: "p0", type: "slider", label: "Observed Allele A Frequency (p)", min: 0.05, max: 0.95, step: 0.05, value: 0.65, format: function (v) { return "p = " + Number(v).toFixed(2); } }
      ]
    },
    "p2-t06": {
      type: "hypothesis_test",
      tag: "PRACTICAL 2 · HWE CHI-SQUARE TEST",
      title: "Virtual Bench: Testing Hardy-Weinberg Equilibrium (AA, Aa, aa; df = 1)",
      animated: false,
      defaultTest: "chisq",
      defaultRatio: "hwe",
      controls: [
        { id: "ratio", type: "toggle", label: "Test Model", value: "hwe", options: [{ value: "hwe", label: "HWE (AA/Aa/aa, df=1)" }, { value: "3:1", label: "Mendelian 3:1 (df=1)" }] },
        { id: "stat", type: "slider", label: "Heterozygote Deficit / HWE Departure", min: 0, max: 4.5, step: 0.25, value: 1.5, format: function (v) { return "Dev ×" + Number(v).toFixed(2); } },
        { id: "alpha", type: "toggle", label: "α Level", value: "0.05", options: [{ value: "0.05", label: "α = 0.05 (3.841)" }, { value: "0.01", label: "α = 0.01 (6.635)" }] }
      ]
    },
    "p2-t07": {
      type: "hardy_weinberg",
      tag: "PRACTICAL 2 · FORCES CALCULATOR",
      title: "Virtual Bench: Quantifying Selection (s), Migration (m), Mutation (μ) & Drift",
      animated: false,
      controls: [
        { id: "p0", type: "slider", label: "Initial p", min: 0.1, max: 0.9, step: 0.05, value: 0.55, format: function (v) { return Number(v).toFixed(2); } },
        { id: "selMode", type: "toggle", label: "Selection Type", value: "rec", options: [
          { value: "rec", label: "Against aa" }, { value: "dom", label: "Against A_" }, { value: "het", label: "Het. Advantage" }
        ]},
        { id: "s", type: "slider", label: "Selection (s)", min: 0, max: 0.8, step: 0.05, value: 0.25, format: function (v) { return "s = " + Number(v).toFixed(2); } },
        { id: "m", type: "slider", label: "Migration (m)", min: 0, max: 0.25, step: 0.01, value: 0.05, format: function (v) { return "m = " + Number(v).toFixed(2); } },
        { id: "mu", type: "slider", label: "Mutation (μ)", min: 0, max: 0.05, step: 0.005, value: 0.0, format: function (v) { return "μ = " + Number(v).toFixed(3); } },
        { id: "ne", type: "slider", label: "Effective Size (Nₑ)", min: 20, max: 500, step: 20, value: 60, format: function (v) { return "Nₑ = " + v; } }
      ]
    },
    "p2-t08": {
      type: "quant_variance",
      defaultMode: "variance",
      tag: "PRACTICAL 2 · h² & REPEATABILITY BENCH",
      title: "Virtual Estimator: Variance Partitioning, Heritability (h²) & Repeatability (r)",
      animated: false,
      controls: [
        { id: "va", type: "slider", label: "Additive Variance (V_A)", min: 5, max: 60, step: 5, value: 30, format: function (v) { return String(v); } },
        { id: "vd", type: "slider", label: "Dominance Variance (V_D)", min: 0, max: 30, step: 5, value: 10, format: function (v) { return String(v); } },
        { id: "vep", type: "slider", label: "Permanent Env (V_Ep)", min: 0, max: 35, step: 5, value: 15, format: function (v) { return String(v); } }
      ]
    },

    /* ---- PRACTICAL UNIT 3 (6 Labs: p3-t01 .. p3-t06) ---- */
    "p3-t01": {
      type: "selection_response",
      tag: "PRACTICAL 3 · S, i & L CALCULATOR",
      title: "Virtual Bench: Selection Differential (S), Intensity (i) & Generation Interval (L)",
      animated: false,
      controls: [
        { id: "pSel", type: "slider", label: "Top % Selected", min: 5, max: 80, step: 5, value: 20, format: function (v) { return "Top " + v + "%"; } },
        { id: "sigmaP", type: "slider", label: "Phenotypic SD (σ_P kg)", min: 200, max: 900, step: 50, value: 500, format: function (v) { return v + " kg"; } },
        { id: "L", type: "slider", label: "Generation Interval (L yrs)", min: 1.5, max: 7.5, step: 0.5, value: 5.0, format: function (v) { return Number(v).toFixed(1) + " yrs"; } }
      ]
    },
    "p3-t02": {
      type: "selection_response",
      tag: "PRACTICAL 3 · ΔG & CORRELATED RESPONSE",
      title: "Virtual Bench: Expected Genetic Gain (ΔG / gen and ΔG / year)",
      animated: false,
      controls: [
        { id: "pSel", type: "slider", label: "Top % Selected", min: 5, max: 70, step: 5, value: 15, format: function (v) { return "Top " + v + "%"; } },
        { id: "h2", type: "slider", label: "Heritability (h²)", min: 0.05, max: 0.65, step: 0.05, value: 0.30, format: function (v) { return "h² = " + Number(v).toFixed(2); } },
        { id: "L", type: "slider", label: "Generation Interval (L)", min: 1.5, max: 7.0, step: 0.5, value: 4.5, format: function (v) { return Number(v).toFixed(1) + " yrs"; } }
      ]
    },
    "p3-t03": {
      type: "epa_mppa",
      tag: "PRACTICAL 3 · EPA & MPPA BENCH",
      title: "Virtual Calculator: Estimated (EPA) & Most Probable Producing Ability (MPPA)",
      animated: false,
      controls: [
        { id: "r", type: "slider", label: "Repeatability (r)", min: 0.15, max: 0.75, step: 0.05, value: 0.45, format: function (v) { return "r = " + Number(v).toFixed(2); } },
        { id: "nA", type: "slider", label: "Cow A Lactations (n_A)", min: 1, max: 6, step: 1, value: 1, format: function (v) { return v + " rec"; } },
        { id: "nB", type: "slider", label: "Cow B Lactations (n_B)", min: 1, max: 8, step: 1, value: 4, format: function (v) { return v + " rec"; } }
      ]
    },
    "p3-t04": {
      type: "pedigree_inbreeding",
      tag: "PRACTICAL 3 · PEDIGREE F & R BENCH",
      title: "Virtual Calculator: Wright's Path-Tracing for F_X & R_XY from Pedigrees",
      animated: false,
      controls: [
        { id: "mating", type: "select", label: "Pedigree Chart", value: "fullsib", options: [
          { value: "selfing", label: "Selfing (F=0.50)" },
          { value: "parent_off", label: "Parent × Offspring (F=0.25)" },
          { value: "fullsib", label: "Full-Sib (F=0.25)" },
          { value: "halfsib", label: "Half-Sib (F=0.125)" },
          { value: "cousin", label: "First-Cousin (F=0.0625)" }
        ]},
        { id: "fA", type: "slider", label: "Common Ancestor F_A", min: 0, max: 0.25, step: 0.05, value: 0, format: function (v) { return (v * 100).toFixed(0) + "%"; } }
      ]
    },
    "p3-t05": {
      type: "crossbreeding_heterosis",
      defaultMode: "heterosis",
      tag: "PRACTICAL 3 · HETEROSIS % BENCH",
      title: "Virtual Calculator: Heterosis (H%) & Rotational Cross Retention",
      animated: false,
      controls: [
        { id: "pA", type: "slider", label: "Parent Breed A Mean", min: 1500, max: 3500, step: 100, value: 2200, format: function (v) { return v + " kg"; } },
        { id: "pB", type: "slider", label: "Parent Breed B Mean", min: 3000, max: 5800, step: 100, value: 4200, format: function (v) { return v + " kg"; } },
        { id: "f1", type: "slider", label: "Crossbred F1 Mean", min: 2500, max: 5200, step: 50, value: 3680, format: function (v) { return v + " kg"; } }
      ]
    },
    "p3-t06": {
      type: "multi_trait_selection",
      tag: "PRACTICAL 3 · SIRE & SELECTION INDEX BENCH",
      title: "Virtual Bench: Constructing & Comparing Selection Index vs ICL & Tandem",
      animated: false,
      controls: [
        { id: "method", type: "toggle", label: "Index Method", value: "index", options: [
          { value: "tandem", label: "Tandem" },
          { value: "icl", label: "Independent Culling" },
          { value: "index", label: "Selection Index (Optimal)" }
        ]}
      ]
    }
  });
})();
