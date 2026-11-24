/* ============================================================
   data-sims-unit2.js — Unit 2 (Principles of Animal & Pop. Genetics)
   Covers 100% of Theory Unit 2 topics: u2-t01 through u2-t29
   ============================================================ */
(function () {
  "use strict";
  if (!window.simEngine) return;

  var speciesOpts = [
    { value: "cattle", label: "Cattle (2n=60)" }, { value: "rbuffalo", label: "River Buffalo (2n=50)" },
    { value: "sbuffalo", label: "Swamp Buffalo (2n=48)" }, { value: "sheep", label: "Sheep (2n=54)" },
    { value: "goat", label: "Goat (2n=60)" }, { value: "pig", label: "Pig (2n=38)" },
    { value: "horse", label: "Horse (2n=64)" }, { value: "dog", label: "Dog (2n=78)" },
    { value: "cat", label: "Cat (2n=38)" }, { value: "chicken", label: "Chicken (2n=78 ZZ/ZW)" }
  ];

  var morphOpts = [
    { value: "metacentric", label: "Metacentric (V)" }, { value: "submetacentric", label: "Submetacentric (L)" },
    { value: "acrocentric", label: "Acrocentric (J)" }, { value: "telocentric", label: "Telocentric (I)" }
  ];

  window.simEngine.registerTopics({
    "u2-t01": {
      type: "mendelian_epistasis",
      tag: "UNIT 2 · HISTORY OF GENETICS",
      title: "Foundations of Genetics: Mendel's Ratios to Gene Interactions",
      animated: false,
      controls: [
        { id: "cross", type: "select", label: "Classic Genetic Milestone", value: "mono", options: [
          { value: "mono", label: "1866 Mendel: Monohybrid 3:1" },
          { value: "dihybrid", label: "1866 Mendel: Dihybrid 9:3:3:1" },
          { value: "comb", label: "1905 Bateson & Punnett: Poultry Comb 9:3:3:1" },
          { value: "incomplete", label: "Incomplete Dominance: Andalusian Fowl 1:2:1" }
        ]}
      ]
    },
    "u2-t02": {
      type: "mitosis_meiosis_3d",
      is3D: true,
      autoPlay: true,
      tag: "UNIT 2 · 3D CELL DIVISION",
      title: "3D Mitosis vs Meiosis, Chiasma Crossing-Over & Nondisjunction",
      controls: [
        { id: "division", type: "toggle", label: "Division Mode", value: "meiosis", options: [
          { value: "meiosis", label: "Meiosis (2n → 4 × n)" }, { value: "mitosis", label: "Mitosis (2n → 2 × 2n)" }
        ]},
        { id: "nondisj", type: "toggle", label: "Nondisjunction", value: "off", options: [
          { value: "off", label: "Normal Disjunction" }, { value: "on", label: "Nondisjunction (2n±1)" }
        ]}
      ],
      steps: [
        { label: "Interphase", apply: function (st) { st.params.stage = 0; } },
        { label: "Prophase I / Chiasma", apply: function (st) { st.params.stage = 1; } },
        { label: "Metaphase", apply: function (st) { st.params.stage = 2; } },
        { label: "Anaphase", apply: function (st) { st.params.stage = 3; } },
        { label: "Daughter Cells", apply: function (st) { st.params.stage = 4; } }
      ]
    },
    "u2-t03": {
      type: "karyotype_3d",
      is3D: true,
      autoPlay: true,
      tag: "UNIT 2 · 3D KARYOTYPE EXPLORER",
      title: "3D Chromosome Morphology & Livestock/Poultry Diploid Numbers",
      controls: [
        { id: "species", type: "select", label: "Livestock / Poultry Species", value: "cattle", options: speciesOpts },
        { id: "morph", type: "toggle", label: "3D Centromere Type", value: "acrocentric", options: morphOpts }
      ]
    },
    "u2-t04": {
      type: "mendelian_epistasis",
      tag: "UNIT 2 · MENDELIAN LAWS",
      title: "Live Punnett Square: Segregation (3:1), Test Cross (1:1) & Dihybrid (9:3:3:1)",
      animated: false,
      controls: [
        { id: "cross", type: "toggle", label: "Mendelian Cross", value: "mono", options: [
          { value: "mono", label: "Monohybrid (3:1)" }, { value: "test", label: "Test Cross (1:1)" }, { value: "dihybrid", label: "Dihybrid (9:3:3:1)" }
        ]}
      ]
    },
    "u2-t05": {
      type: "mendelian_epistasis",
      tag: "UNIT 2 · MODIFIED MENDELIAN",
      title: "Incomplete Dominance (1:2:1), Codominance & Lethal Genes (2:1)",
      animated: false,
      controls: [
        { id: "cross", type: "toggle", label: "Modified Inheritance", value: "incomplete", options: [
          { value: "incomplete", label: "Andalusian Blue (1:2:1)" },
          { value: "codom", label: "Shorthorn Roan (1:2:1)" },
          { value: "lethal", label: "Dexter Bulldog Lethal (2:1)" }
        ]}
      ]
    },
    "u2-t06": {
      type: "mendelian_epistasis",
      tag: "UNIT 2 · EPISTASIS BUILDER",
      title: "Interactive Epistasis Ratio Lab (9:3:4, 12:3:1, 9:7, 15:1 & Poultry Comb)",
      animated: false,
      controls: [
        { id: "cross", type: "select", label: "Epistasis / Non-Allelic Interaction", value: "epi_rec", options: [
          { value: "epi_rec", label: "Recessive Epistasis 9:3:4 (Labrador Coat)" },
          { value: "epi_dom", label: "Dominant Epistasis 12:3:1" },
          { value: "epi_comp", label: "Complementary Genes 9:7" },
          { value: "epi_dup", label: "Duplicate Dominant 15:1" },
          { value: "comb", label: "Poultry Comb Shape 9:3:3:1 (Walnut/Rose/Pea/Single)" }
        ]}
      ]
    },
    "u2-t07": {
      type: "mendelian_epistasis",
      tag: "UNIT 2 · PLEIOTROPY & PENETRANCE",
      title: "Pleiotropy (Dexter/White Cat) & Penetrance/Expressivity Explorer",
      animated: false,
      controls: [
        { id: "cross", type: "toggle", label: "Phenotypic Expression", value: "lethal", options: [
          { value: "lethal", label: "Pleiotropic Lethal (Dexter 2:1)" },
          { value: "incomplete", label: "Intermediate Expressivity (1:2:1)" },
          { value: "mono", label: "Complete Penetrance (3:1)" }
        ]}
      ]
    },
    "u2-t08": {
      type: "mendelian_epistasis",
      tag: "UNIT 2 · MULTIPLE ALLELES",
      title: "Codominance & Blood Group Allelic Series in Farm Animals",
      animated: false,
      controls: [
        { id: "cross", type: "toggle", label: "Allelic System", value: "codom", options: [
          { value: "codom", label: "Codominant Blood / Coat (1:2:1)" },
          { value: "mono", label: "Dominant-Recessive (3:1)" }
        ]}
      ]
    },
    "u2-t09": {
      type: "karyotype_3d",
      is3D: true,
      autoPlay: true,
      tag: "UNIT 2 · SEX DETERMINATION",
      title: "XX/XY Mammals vs ZZ/ZW Poultry (Heterogametic Female!)",
      controls: [
        { id: "species", type: "toggle", label: "Sex System", value: "chicken", options: [
          { value: "chicken", label: "Chicken ZZ♂ / ZW♀ (2n=78)" },
          { value: "cattle", label: "Cattle XX♀ / XY♂ (2n=60)" },
          { value: "horse", label: "Horse XX♀ / XY♂ (2n=64)" }
        ]},
        { id: "morph", type: "toggle", label: "3D Chromosome Shape", value: "submetacentric", options: morphOpts }
      ]
    },
    "u2-t10": {
      type: "karyotype_3d",
      is3D: true,
      autoPlay: true,
      tag: "UNIT 2 · SEX-LINKED INHERITANCE",
      title: "Sex-Linked (Z-Linked Barring), Sex-Limited & Sex-Influenced Traits",
      controls: [
        { id: "species", type: "toggle", label: "Model Species", value: "chicken", options: [
          { value: "chicken", label: "Poultry (Z-linked Barred Plumage)" },
          { value: "sheep", label: "Sheep (Sex-Influenced Horns)" },
          { value: "cattle", label: "Cattle (Sex-Limited Milk Yield)" }
        ]},
        { id: "morph", type: "toggle", label: "Chromosome View", value: "metacentric", options: morphOpts }
      ]
    },
    "u2-t11": {
      type: "mitosis_meiosis_3d",
      is3D: true,
      autoPlay: true,
      tag: "UNIT 2 · 3D CROSSING-OVER",
      title: "3D Homologous Synapsis, Chiasma Formation & Genetic Recombination",
      controls: [
        { id: "division", type: "toggle", label: "View", value: "meiosis", options: [{ value: "meiosis", label: "Meiotic Crossing-Over" }] },
        { id: "nondisj", type: "toggle", label: "Disjunction", value: "off", options: [{ value: "off", label: "Normal Recombination" }, { value: "on", label: "Nondisjunction" }] }
      ],
      steps: [
        { label: "Synapsis & Chiasma", apply: function (st) { st.params.stage = 1; } },
        { label: "Metaphase I Alignment", apply: function (st) { st.params.stage = 2; } },
        { label: "Anaphase I Separation", apply: function (st) { st.params.stage = 3; } },
        { label: "Recombinant Gametes", apply: function (st) { st.params.stage = 4; } }
      ]
    },
    "u2-t12": {
      type: "dna_molecular_3d",
      is3D: true,
      autoPlay: true,
      defaultMode: "mutation",
      tag: "UNIT 2 · 3D GENE MUTATIONS",
      title: "3D DNA Point Mutations: Silent, Missense, Nonsense & Frameshift",
      controls: [
        { id: "mutation", type: "toggle", label: "Mutation Type", value: "missense", options: [
          { value: "none", label: "Wild-Type" }, { value: "silent", label: "Silent" },
          { value: "missense", label: "Missense" }, { value: "nonsense", label: "Nonsense (STOP)" },
          { value: "frameshift", label: "Frameshift" }
        ]}
      ]
    },
    "u2-t13": {
      type: "aberrations_3d",
      is3D: true,
      autoPlay: true,
      tag: "UNIT 2 · 3D ABERRATIONS",
      title: "3D Structural & Numerical Chromosomal Aberrations (incl. Cattle 1/29)",
      controls: [
        { id: "aberration", type: "select", label: "Chromosomal Aberration", value: "robertsonian", options: [
          { value: "robertsonian", label: "Robertsonian 1/29 Translocation (Cattle 2n=59)" },
          { value: "deletion", label: "Deletion (Segment C Lost)" },
          { value: "duplication", label: "Duplication (Segment C Doubled)" },
          { value: "inversion", label: "Inversion (B-C-D Flipped)" },
          { value: "translocation", label: "Reciprocal Translocation" },
          { value: "trisomy", label: "Numerical: Trisomy (2n + 1)" }
        ]}
      ]
    },
    "u2-t14": {
      type: "karyotype_3d",
      is3D: true,
      autoPlay: true,
      tag: "UNIT 2 · CYTOGENETICS & BANDING",
      title: "3D G-Banded Chromosome & Livestock Karyotyping Bench",
      controls: [
        { id: "species", type: "select", label: "Species Karyotype", value: "rbuffalo", options: speciesOpts },
        { id: "morph", type: "toggle", label: "Banded Morphology", value: "submetacentric", options: morphOpts }
      ]
    },
    "u2-t15": {
      type: "dna_molecular_3d",
      is3D: true,
      autoPlay: true,
      defaultMode: "helix",
      tag: "UNIT 2 · EXTRA-CHROMOSOMAL",
      title: "3D Mitochondrial DNA (mtDNA) & Maternal Inheritance Visualizer",
      controls: [
        { id: "mode", type: "toggle", label: "DNA View", value: "helix", options: [
          { value: "helix", label: "3D DNA Helix" }, { value: "mutation", label: "mtDNA Point Variant" }
        ]}
      ]
    },
    "u2-t16": {
      type: "dna_molecular_3d",
      is3D: true,
      autoPlay: true,
      defaultMode: "helix",
      tag: "UNIT 2 · 3D NUCLEIC ACIDS",
      title: "3D Watson-Crick B-DNA Double Helix (A=T 2H, G≡C 3H, Antiparallel)",
      controls: [
        { id: "mode", type: "toggle", label: "Molecular View", value: "helix", options: [
          { value: "helix", label: "B-DNA Double Helix" }, { value: "replication", label: "Unwound Fork" }
        ]}
      ]
    },
    "u2-t17": {
      type: "dna_molecular_3d",
      is3D: true,
      autoPlay: true,
      defaultMode: "replication",
      tag: "UNIT 2 · REPLICATION & CENTRAL DOGMA",
      title: "3D Semi-Conservative DNA Replication Fork & Central Dogma",
      controls: [
        { id: "mode", type: "toggle", label: "Process", value: "replication", options: [
          { value: "replication", label: "Replication Fork" }, { value: "helix", label: "Intact Template" }, { value: "mutation", label: "Codon Effect" }
        ]}
      ]
    },
    "u2-t18": {
      type: "dna_molecular_3d",
      is3D: false,
      animated: false,
      defaultMode: "pcr",
      tag: "UNIT 2 · MOLECULAR TECHNIQUES",
      title: "PCR Exponential Amplification (2ⁿ) & RFLP Agarose Gel Lab",
      controls: [
        { id: "cycles", type: "slider", label: "PCR Thermal Cycles (n)", min: 5, max: 30, step: 1, value: 20, format: function (v) { return v + " cycles"; } }
      ]
    },
    "u2-t19": {
      type: "hardy_weinberg",
      tag: "UNIT 2 · POPULATION GENETICS",
      title: "Gene Pool Dynamics: Individual Genotype vs Population Frequencies",
      animated: false,
      controls: [
        { id: "p0", type: "slider", label: "Initial Dominant Allele Freq (p)", min: 0.05, max: 0.95, step: 0.05, value: 0.50, format: function (v) { return "p = " + Number(v).toFixed(2); } }
      ]
    },
    "u2-t20": {
      type: "hardy_weinberg",
      tag: "UNIT 2 · GENE & GENOTYPIC FREQ",
      title: "Allele (p, q) & Genotype (p², 2pq, q²) Frequency Visualizer",
      animated: false,
      controls: [
        { id: "p0", type: "slider", label: "Allele A Frequency (p)", min: 0.05, max: 0.95, step: 0.05, value: 0.60, format: function (v) { return "p = " + Number(v).toFixed(2); } }
      ]
    },
    "u2-t21": {
      type: "hardy_weinberg",
      tag: "UNIT 2 · HARDY-WEINBERG LAW",
      title: "Hardy-Weinberg Equilibrium (p² + 2pq + q² = 1) Multi-Generation Lab",
      animated: false,
      controls: [
        { id: "p0", type: "slider", label: "Initial p", min: 0.05, max: 0.95, step: 0.05, value: 0.50, format: function (v) { return "p = " + Number(v).toFixed(2); } },
        { id: "s", type: "slider", label: "Selection Against aa (s)", min: 0, max: 0.8, step: 0.05, value: 0, format: function (v) { return "s = " + Number(v).toFixed(2); } }
      ]
    },
    "u2-t22": {
      type: "hardy_weinberg",
      tag: "UNIT 2 · FORCES CHANGING GENE FREQ",
      title: "Population Forces Simulator: Selection (s), Migration (m), Mutation (μ) & Drift (Nₑ)",
      animated: false,
      controls: [
        { id: "p0", type: "slider", label: "Initial p", min: 0.1, max: 0.9, step: 0.05, value: 0.6, format: function (v) { return Number(v).toFixed(2); } },
        { id: "selMode", type: "toggle", label: "Selection Type", value: "rec", options: [
          { value: "rec", label: "Against aa" }, { value: "dom", label: "Against A_" }, { value: "het", label: "Heterozygote Adv." }
        ]},
        { id: "s", type: "slider", label: "Selection Intensity (s)", min: 0, max: 0.8, step: 0.05, value: 0.3, format: function (v) { return "s = " + Number(v).toFixed(2); } },
        { id: "m", type: "slider", label: "Migration Rate (m)", min: 0, max: 0.25, step: 0.01, value: 0.0, format: function (v) { return "m = " + Number(v).toFixed(2); } },
        { id: "mu", type: "slider", label: "Mutation Rate (μ)", min: 0, max: 0.05, step: 0.005, value: 0.0, format: function (v) { return "μ = " + Number(v).toFixed(3); } },
        { id: "ne", type: "slider", label: "Effective Herd Size (Nₑ)", min: 15, max: 500, step: 15, value: 50, format: function (v) { return "Nₑ = " + v; } }
      ]
    },
    "u2-t23": {
      type: "quant_variance",
      defaultMode: "polygenic",
      tag: "UNIT 2 · POLYGENIC INHERITANCE",
      title: "Qualitative → Quantitative Transition: Polygenic Bell Curve Builder",
      animated: false,
      controls: [
        { id: "loci", type: "slider", label: "Number of Polygenic Loci (n)", min: 1, max: 6, step: 1, value: 3, format: function (v) { return v + " loci"; } },
        { id: "envBlur", type: "slider", label: "Environmental Variation Blur", min: 0, max: 1.0, step: 0.05, value: 0.45, format: function (v) { return Math.round(v * 100) + "%"; } }
      ]
    },
    "u2-t24": {
      type: "quant_variance",
      defaultMode: "variance",
      tag: "UNIT 2 · BREEDING VALUE & V_A",
      title: "Additive Genetic Variance (V_A) & Transmissible Breeding Value",
      animated: false,
      controls: [
        { id: "va", type: "slider", label: "Additive Variance (V_A)", min: 5, max: 70, step: 5, value: 35, format: function (v) { return String(v); } },
        { id: "vd", type: "slider", label: "Dominance Variance (V_D)", min: 0, max: 40, step: 2, value: 12, format: function (v) { return String(v); } },
        { id: "vet", type: "slider", label: "Environmental Variance (V_E)", min: 10, max: 70, step: 5, value: 35, format: function (v) { return String(v); } }
      ]
    },
    "u2-t25": {
      type: "quant_variance",
      defaultMode: "variance",
      tag: "UNIT 2 · VARIANCE PARTITIONING",
      title: "Phenotypic Variance Lab: V_P = V_A + V_D + V_I + V_Ep + V_Et",
      animated: false,
      controls: [
        { id: "va", type: "slider", label: "Additive (V_A)", min: 5, max: 60, step: 5, value: 30, format: function (v) { return String(v); } },
        { id: "vd", type: "slider", label: "Dominance (V_D)", min: 0, max: 35, step: 5, value: 15, format: function (v) { return String(v); } },
        { id: "vi", type: "slider", label: "Epistatic (V_I)", min: 0, max: 25, step: 5, value: 5, format: function (v) { return String(v); } },
        { id: "vep", type: "slider", label: "Permanent Env (V_Ep)", min: 0, max: 35, step: 5, value: 15, format: function (v) { return String(v); } }
      ]
    },
    "u2-t26": {
      type: "quant_variance",
      defaultMode: "gxe",
      tag: "UNIT 2 · G × E INTERACTION",
      title: "Genotype × Environment Interaction Plot (Holstein vs Sahiwal)",
      animated: false,
      controls: [
        { id: "gxe", type: "slider", label: "Tropical Heat/Disease Stress (G × E)", min: 0, max: 1.2, step: 0.05, value: 0.95, format: function (v) { return Math.round(v * 100) + "%"; } }
      ]
    },
    "u2-t27": {
      type: "quant_variance",
      defaultMode: "variance",
      tag: "UNIT 2 · HERITABILITY (h²)",
      title: "Narrow-Sense (h²) vs Broad-Sense (H²) Heritability Explorer",
      animated: false,
      controls: [
        { id: "va", type: "slider", label: "Additive Variance (V_A)", min: 5, max: 65, step: 5, value: 25, format: function (v) { return String(v); } },
        { id: "vd", type: "slider", label: "Dominance Variance (V_D)", min: 0, max: 30, step: 5, value: 10, format: function (v) { return String(v); } },
        { id: "vet", type: "slider", label: "Temporary Env (V_Et)", min: 10, max: 70, step: 5, value: 45, format: function (v) { return String(v); } }
      ]
    },
    "u2-t28": {
      type: "quant_variance",
      defaultMode: "variance",
      tag: "UNIT 2 · REPEATABILITY (r)",
      title: "Why Repeatability (r) is ALWAYS the Upper Limit of Heritability (h²)",
      animated: false,
      controls: [
        { id: "va", type: "slider", label: "Additive (V_A)", min: 5, max: 50, step: 5, value: 25, format: function (v) { return String(v); } },
        { id: "vep", type: "slider", label: "Permanent Env (V_Ep — Udder/Growth)", min: 0, max: 40, step: 5, value: 20, format: function (v) { return String(v); } },
        { id: "vet", type: "slider", label: "Temporary Env (V_Et)", min: 10, max: 65, step: 5, value: 35, format: function (v) { return String(v); } }
      ]
    },
    "u2-t29": {
      type: "corr_regression",
      tag: "UNIT 2 · GENETIC CORRELATIONS",
      title: "Genetic & Phenotypic Correlation (r_G vs r_P) Between Economic Traits",
      hint: "Slide correlation from negative (Milk Yield vs Fat %) to positive (Body Weight vs Growth Rate)",
      interactiveCanvas: true,
      xLabel: "Trait 1: Milk Yield (kg)",
      yLabel: "Trait 2: Fat % (Negative r) or Protein Yield (Positive r)",
      controls: [
        { id: "r", type: "slider", label: "Genetic Correlation (r_G)", min: -0.90, max: 0.95, step: 0.05, value: -0.45, format: function (v) { return "r_G = " + Number(v).toFixed(2); } }
      ]
    }
  });
})();
