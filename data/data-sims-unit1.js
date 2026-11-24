/* ============================================================
   data-sims-unit1.js — Unit 1 (Biostatistics & Computer App)
   Covers 100% of Theory Unit 1 topics: u1-t01 through u1-t22
   ============================================================ */
(function () {
  "use strict";
  if (!window.simEngine) return;

  var stdCentralCtrls = [
    { id: "outlier", type: "slider", label: "Extreme Animal / Outlier Value", min: 6, max: 42, step: 0.5, value: 18, format: function (v) { return Number(v).toFixed(1) + " L"; } },
    { id: "sampleSize", type: "slider", label: "Sample Size (n) for SEM", min: 4, max: 100, step: 2, value: 10, format: function (v) { return "n = " + v; } }
  ];

  window.simEngine.registerTopics({
    "u1-t01": {
      type: "central_dispersion",
      tag: "UNIT 1 · BIOSTATISTICS INTRO",
      title: "Veterinary Biological Variation & Herd Summary Lab",
      hint: "Drag the red cow observation or move the slider to see how biostatistics summarizes variable herd records",
      interactiveCanvas: true,
      xLabel: "Daily Milk Yield (litres/day)",
      controls: stdCentralCtrls
    },
    "u1-t02": {
      type: "central_dispersion",
      tag: "UNIT 1 · CLASSIFICATION & TABULATION",
      title: "Biological Data Distribution & Class Spread Explorer",
      hint: "Drag the outlier to see how raw herd observations shift class intervals and summary averages",
      interactiveCanvas: true,
      xLabel: "Birth Weight of Calves (kg)",
      dataset: [20, 22, 23, 24, 24, 25, 25, 26, 27, 28],
      controls: [
        { id: "outlier", type: "slider", label: "Largest Calf Weight (kg)", min: 18, max: 44, step: 0.5, value: 28, format: function (v) { return v + " kg"; } },
        { id: "sampleSize", type: "slider", label: "Tabulated Sample Size (n)", min: 5, max: 100, step: 5, value: 25, format: function (v) { return "n = " + v; } }
      ]
    },
    "u1-t03": {
      type: "sampling_excel",
      tag: "UNIT 1 · PARAMETER vs STATISTIC",
      title: "Population Parameter (μ, σ) vs Sample Statistic (x̄, s)",
      hint: "Switch sampling schemes to see how a sample statistic estimates the true herd parameter",
      animated: false,
      controls: [
        { id: "method", type: "toggle", label: "Sampling Scheme", value: "srs", options: [
          { value: "srs", label: "Simple Random" }, { value: "stratified", label: "Stratified" },
          { value: "systematic", label: "Systematic" }, { value: "cluster", label: "Cluster" }
        ]}
      ]
    },
    "u1-t04": {
      type: "prob_distributions",
      tag: "UNIT 1 · GRAPHICAL REPRESENTATION",
      title: "Discrete Bar Chart vs Continuous Frequency Curve",
      hint: "Toggle between discrete histograms (Binomial/Poisson) and continuous frequency curves (Normal)",
      animated: false,
      controls: [
        { id: "dist", type: "toggle", label: "Graph Type", value: "normal", options: [
          { value: "normal", label: "Frequency Curve (Normal)" },
          { value: "binomial", label: "Discrete Bar (Binomial)" },
          { value: "poisson", label: "Rare Counts (Poisson)" }
        ]},
        { id: "z", type: "slider", label: "Cutoff Z-Score", min: -3, max: 3, step: 0.1, value: 1.0, format: function (v) { return "Z = " + Number(v).toFixed(1); } }
      ]
    },
    "u1-t05": {
      type: "central_dispersion",
      tag: "UNIT 1 · CENTRAL TENDENCY",
      title: "Mean vs Median vs Mode: Live Outlier Resistance Lab",
      hint: "Drag the red dot right to watch Mean jump while Median resists outliers!",
      interactiveCanvas: true,
      controls: stdCentralCtrls,
      steps: [
        { label: "Symmetric Herd", apply: function (st) { st.params.outlier = 18; } },
        { label: "Mild Skew", apply: function (st) { st.params.outlier = 28; } },
        { label: "Extreme Outlier", apply: function (st) { st.params.outlier = 40; } }
      ]
    },
    "u1-t06": {
      type: "central_dispersion",
      tag: "UNIT 1 · DISPERSION",
      title: "Variance (s²), Standard Deviation (s) & Spread Visualizer",
      hint: "Widen the outlier to see why Variance & SD inflate quadratically with extreme deviations",
      interactiveCanvas: true,
      controls: [
        { id: "outlier", type: "slider", label: "Extreme Deviation Value", min: 10, max: 42, step: 0.5, value: 24, format: function (v) { return Number(v).toFixed(1); } },
        { id: "sampleSize", type: "slider", label: "Sample Size (n)", min: 5, max: 100, step: 5, value: 20, format: function (v) { return "n = " + v; } }
      ]
    },
    "u1-t07": {
      type: "central_dispersion",
      tag: "UNIT 1 · CV% & SEM",
      title: "Coefficient of Variation (CV%) & Standard Error (SD/√n)",
      hint: "Slide Sample Size n from 4 to 100 — watch SEM shrink by √n while SD stays unchanged!",
      interactiveCanvas: true,
      controls: [
        { id: "sampleSize", type: "slider", label: "Sample Size (n)", min: 4, max: 100, step: 2, value: 16, format: function (v) { return "n = " + v; } },
        { id: "outlier", type: "slider", label: "Herd Spread / Outlier", min: 12, max: 40, step: 0.5, value: 18, format: function (v) { return Number(v).toFixed(1); } }
      ]
    },
    "u1-t08": {
      type: "skew_kurtosis",
      tag: "UNIT 1 · SKEWNESS & KURTOSIS",
      title: "Interactive Skewness (β₁) & Kurtosis (β₂) Morphing Curve",
      hint: "Morph between Positive/Negative Skew and Leptokurtic/Mesokurtic/Platykurtic peaks",
      animated: false,
      controls: [
        { id: "skew", type: "slider", label: "Skewness Direction", min: -2.0, max: 2.0, step: 0.1, value: 1.2, format: function (v) { return Number(v).toFixed(1); } },
        { id: "kurt", type: "slider", label: "Kurtosis (β₂)", min: 1.8, max: 5.0, step: 0.1, value: 3.0, format: function (v) { return "β₂ = " + Number(v).toFixed(1); } }
      ],
      steps: [
        { label: "Symmetric Mesokurtic", apply: function (st) { st.params.skew = 0; st.params.kurt = 3.0; } },
        { label: "Positive Skew", apply: function (st) { st.params.skew = 1.6; st.params.kurt = 3.0; } },
        { label: "Negative Skew", apply: function (st) { st.params.skew = -1.6; st.params.kurt = 3.0; } },
        { label: "Leptokurtic Peak", apply: function (st) { st.params.skew = 0; st.params.kurt = 4.6; } },
        { label: "Platykurtic Flat", apply: function (st) { st.params.skew = 0; st.params.kurt = 2.0; } }
      ]
    },
    "u1-t09": {
      type: "prob_distributions",
      tag: "UNIT 1 · PROBABILITY THEORY",
      title: "Probability Theorems & Binomial Trial Simulator",
      hint: "Adjust trial count n and success probability p (e.g., 0.50 calf sex ratio or 0.25 recessive carrier)",
      animated: false,
      controls: [
        { id: "dist", type: "toggle", label: "Model", value: "binomial", options: [
          { value: "binomial", label: "Binomial Trials" }, { value: "poisson", label: "Rare Events" }
        ]},
        { id: "n", type: "slider", label: "Number of Trials (n)", min: 4, max: 20, step: 1, value: 10, format: function (v) { return "n = " + v; } },
        { id: "p", type: "slider", label: "Probability of Success (p)", min: 0.05, max: 0.95, step: 0.05, value: 0.50, format: function (v) { return "p = " + Number(v).toFixed(2); } }
      ]
    },
    "u1-t10": {
      type: "prob_distributions",
      tag: "UNIT 1 · BINOMIAL & POISSON",
      title: "Binomial B(n, p) vs Poisson P(λ) Distribution Lab",
      hint: "Compare Mean > Variance (Binomial) vs Mean = Variance = λ (Poisson)",
      animated: false,
      controls: [
        { id: "dist", type: "toggle", label: "Distribution", value: "binomial", options: [
          { value: "binomial", label: "Binomial B(n,p)" }, { value: "poisson", label: "Poisson P(λ)" }
        ]},
        { id: "n", type: "slider", label: "Binomial Trials (n)", min: 4, max: 20, step: 1, value: 12, format: function (v) { return "n = " + v; } },
        { id: "p", type: "slider", label: "Binomial p", min: 0.05, max: 0.95, step: 0.05, value: 0.25, format: function (v) { return Number(v).toFixed(2); } },
        { id: "lambda", type: "slider", label: "Poisson Rate (λ)", min: 0.5, max: 10, step: 0.5, value: 3.5, format: function (v) { return "λ = " + Number(v).toFixed(1); } }
      ]
    },
    "u1-t11": {
      type: "prob_distributions",
      tag: "UNIT 1 · NORMAL DISTRIBUTION",
      title: "Standard Normal Curve (68.27% / 95.45% / 99.73%) & Z-Lookup",
      hint: "Slide Z to read exact cumulative probability P(Z ≤ z) and area within ±|Z|",
      animated: false,
      controls: [
        { id: "dist", type: "toggle", label: "View", value: "normal", options: [{ value: "normal", label: "Standard Normal Curve" }] },
        { id: "z", type: "slider", label: "Standard Normal Z-Score", min: -3.0, max: 3.0, step: 0.05, value: 1.96, format: function (v) { return "Z = " + Number(v).toFixed(2); } },
        { id: "mu", type: "slider", label: "Population Mean (μ)", min: 50, max: 150, step: 5, value: 100, format: function (v) { return "μ = " + v; } },
        { id: "sigma", type: "slider", label: "Standard Deviation (σ)", min: 5, max: 30, step: 1, value: 15, format: function (v) { return "σ = " + v; } }
      ]
    },
    "u1-t12": {
      type: "corr_regression",
      tag: "UNIT 1 · CORRELATION",
      title: "Pearson (r) & Spearman Rank (ρ) Interactive Scatter Lab",
      hint: "Slide target r (−1 to +1) or click directly on the plot to add animal observations",
      interactiveCanvas: true,
      controls: [
        { id: "r", type: "slider", label: "Target Correlation (r)", min: -0.98, max: 0.98, step: 0.02, value: 0.86, format: function (v) { return "r = " + Number(v).toFixed(2); } }
      ]
    },
    "u1-t13": {
      type: "corr_regression",
      tag: "UNIT 1 · LINEAR REGRESSION",
      title: "Least-Squares Regression (Ŷ = a + bX) & Residuals Lab",
      hint: "Click anywhere to add points and watch slope b, intercept a, R², and red residual errors update live",
      interactiveCanvas: true,
      xLabel: "Heart Girth X (cm)",
      yLabel: "Predicted Body Weight Y (kg)",
      controls: [
        { id: "r", type: "slider", label: "Strength of Relationship", min: -0.95, max: 0.98, step: 0.02, value: 0.90, format: function (v) { return "r = " + Number(v).toFixed(2); } }
      ]
    },
    "u1-t14": {
      type: "sampling_excel",
      tag: "UNIT 1 · SAMPLING METHODS",
      title: "Herd Sampling Simulator: SRS vs Stratified vs Systematic vs Cluster",
      hint: "Switch sampling methods across the 40-animal, 4-shed veterinary farm",
      animated: false,
      controls: [
        { id: "method", type: "toggle", label: "Sampling Method", value: "stratified", options: [
          { value: "srs", label: "Simple Random" }, { value: "stratified", label: "Stratified" },
          { value: "systematic", label: "Systematic (k=5)" }, { value: "cluster", label: "Cluster (Shed 2)" }
        ]}
      ]
    },
    "u1-t15": {
      type: "hypothesis_test",
      tag: "UNIT 1 · LARGE SAMPLE Z-TEST",
      title: "Large Sample Z-Test Critical Region & Rejection Lab",
      hint: "Slide Calculated Z across ±1.96 (α=0.05) and ±2.58 (α=0.01) to test H₀",
      animated: false,
      defaultTest: "z",
      controls: [
        { id: "stat", type: "slider", label: "Calculated Z-Statistic", min: -3.8, max: 3.8, step: 0.05, value: 2.20, format: function (v) { return "Z = " + Number(v).toFixed(2); } },
        { id: "alpha", type: "toggle", label: "Significance Level (α)", value: "0.05", options: [{ value: "0.05", label: "α = 0.05 (±1.96)" }, { value: "0.01", label: "α = 0.01 (±2.58)" }] }
      ]
    },
    "u1-t16": {
      type: "hypothesis_test",
      tag: "UNIT 1 · STUDENT'S t-TEST",
      title: "Student's t-Test (Small Sample, df) Live Critical Region",
      hint: "Lower df to see heavier t-distribution tails require a larger t-value to reject H₀!",
      animated: false,
      defaultTest: "t",
      controls: [
        { id: "stat", type: "slider", label: "Calculated t-Statistic", min: -4.0, max: 4.0, step: 0.05, value: 2.45, format: function (v) { return "t = " + Number(v).toFixed(2); } },
        { id: "df", type: "slider", label: "Degrees of Freedom (df)", min: 2, max: 30, step: 1, value: 10, format: function (v) { return "df = " + v; } },
        { id: "alpha", type: "toggle", label: "Significance Level (α)", value: "0.05", options: [{ value: "0.05", label: "α = 0.05" }, { value: "0.01", label: "α = 0.01" }] }
      ]
    },
    "u1-t17": {
      type: "hypothesis_test",
      tag: "UNIT 1 · CHI-SQUARE TEST",
      title: "Chi-Square (χ²) Mendelian 3:1 & 9:3:3:1 Goodness-of-Fit Lab",
      hint: "Adjust Observed Deviation from expected Mendelian offspring and watch χ² cross the critical threshold",
      animated: false,
      defaultTest: "chisq",
      controls: [
        { id: "ratio", type: "toggle", label: "Expected Ratio", value: "3:1", options: [{ value: "3:1", label: "Monohybrid 3:1 (df=1)" }, { value: "9:3:3:1", label: "Dihybrid 9:3:3:1 (df=3)" }] },
        { id: "stat", type: "slider", label: "Observed Deviation from Expected", min: 0, max: 4.5, step: 0.25, value: 1.5, format: function (v) { return "Dev ×" + Number(v).toFixed(2); } },
        { id: "alpha", type: "toggle", label: "α Level", value: "0.05", options: [{ value: "0.05", label: "α = 0.05" }, { value: "0.01", label: "α = 0.01" }] }
      ]
    },
    "u1-t18": {
      type: "exp_design",
      tag: "UNIT 1 · EXPERIMENTAL DESIGNS",
      title: "CRD vs RBD Farm Pen Randomization & Local Control Lab",
      hint: "Toggle CRD vs RBD to watch blocking pull shed/parity noise out of Error MS and boost F-ratio!",
      animated: false,
      controls: [
        { id: "design", type: "toggle", label: "Experimental Design", value: "rbd", options: [{ value: "crd", label: "CRD (No Blocking)" }, { value: "rbd", label: "RBD (Blocked by Parity)" }] },
        { id: "trtEffect", type: "slider", label: "True Diet Difference (L)", min: 0.5, max: 6.0, step: 0.5, value: 3.0, format: function (v) { return Number(v).toFixed(1) + " L"; } },
        { id: "blockNoise", type: "slider", label: "Parity / Shed Gradient", min: 0.5, max: 7.0, step: 0.5, value: 4.5, format: function (v) { return Number(v).toFixed(1) + " L"; } }
      ]
    },
    "u1-t19": {
      type: "exp_design",
      tag: "UNIT 1 · ANOVA & F-TEST",
      title: "One-Way (CRD) & Two-Way (RBD) ANOVA F-Ratio Breakdown",
      hint: "Inspect the live ANOVA table below the farm grid as Treatment Effect and Error MS change",
      animated: false,
      controls: [
        { id: "design", type: "toggle", label: "ANOVA Model", value: "rbd", options: [{ value: "crd", label: "One-Way ANOVA (CRD)" }, { value: "rbd", label: "Two-Way ANOVA (RBD)" }] },
        { id: "trtEffect", type: "slider", label: "Between-Group Signal", min: 0.5, max: 6.0, step: 0.5, value: 3.5, format: function (v) { return Number(v).toFixed(1); } },
        { id: "blockNoise", type: "slider", label: "Block Heterogeneity", min: 0.5, max: 7.0, step: 0.5, value: 4.0, format: function (v) { return Number(v).toFixed(1); } }
      ]
    },
    "u1-t20": {
      type: "skew_kurtosis",
      tag: "UNIT 1 · NON-PARAMETRIC TESTS",
      title: "When to Switch to Non-Parametric Tests (Skewed / Ordinal Data)",
      hint: "Increase Skewness to see why parametric t/ANOVA assumptions fail and Mann-Whitney / Kruskal-Wallis are chosen",
      animated: false,
      controls: [
        { id: "skew", type: "slider", label: "Data Skewness (e.g., Parasite Egg Count)", min: -2.0, max: 2.0, step: 0.1, value: 1.7, format: function (v) { return Number(v).toFixed(1); } },
        { id: "kurt", type: "slider", label: "Tail Peakedness (β₂)", min: 1.8, max: 5.0, step: 0.1, value: 4.2, format: function (v) { return "β₂ = " + Number(v).toFixed(1); } }
      ]
    },
    "u1-t21": {
      type: "sampling_excel",
      submode: "excel",
      tag: "UNIT 1 · DBMS & COMPUTERS",
      title: "Veterinary Herd DBMS Table & Formula Workbench",
      hint: "Switch live functions to inspect relational Primary Key structure and automated herd queries",
      animated: false,
      controls: [
        { id: "formula", type: "toggle", label: "Query / Function", value: "AVERAGE", options: [
          { value: "AVERAGE", label: "AVERAGE()" }, { value: "STDEV.S", label: "STDEV.S()" },
          { value: "TTEST", label: "T.TEST()" }, { value: "CHISQ.TEST", label: "CHISQ.TEST()" }
        ]}
      ]
    },
    "u1-t22": {
      type: "sampling_excel",
      submode: "excel",
      tag: "UNIT 1 · MS-EXCEL BIOSTATISTICS",
      title: "Interactive MS-Excel Veterinary Data Analysis Lab",
      hint: "Select an Excel statistical formula to see highlighted cell ranges and live output",
      animated: false,
      controls: [
        { id: "formula", type: "toggle", label: "MS-Excel Formula", value: "TTEST", options: [
          { value: "AVERAGE", label: "=AVERAGE" }, { value: "STDEV.S", label: "=STDEV.S" },
          { value: "TTEST", label: "=T.TEST" }, { value: "CHISQ.TEST", label: "=CHISQ.TEST" }
        ]}
      ]
    }
  });
})();
