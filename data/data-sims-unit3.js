/* ============================================================
   data-sims-unit3.js — Unit 3 (Principles of Animal Breeding)
   Covers 100% of Theory Unit 3 topics: u3-t01 through u3-t28
   ============================================================ */
(function () {
  "use strict";
  if (!window.simEngine) return;

  var selControls = [
    { id: "pSel", type: "slider", label: "Proportion Selected (Top p%)", min: 5, max: 80, step: 5, value: 20, format: function (v) { return "Top " + v + "%"; } },
    { id: "h2", type: "slider", label: "Heritability (h²)", min: 0.05, max: 0.65, step: 0.05, value: 0.25, format: function (v) { return "h² = " + Number(v).toFixed(2); } },
    { id: "L", type: "slider", label: "Generation Interval (L yrs)", min: 1.0, max: 8.0, step: 0.5, value: 5.0, format: function (v) { return Number(v).toFixed(1) + " yrs"; } }
  ];

  var pedigreeOpts = [
    { value: "selfing", label: "Selfing (F=50%)" },
    { value: "parent_off", label: "Parent × Offspring (F=25%)" },
    { value: "fullsib", label: "Full-Sib (F=25%)" },
    { value: "halfsib", label: "Half-Sib (F=12.5%)" },
    { value: "cousin", label: "First-Cousin (F=6.25%)" }
  ];

  window.simEngine.registerTopics({
    "u3-t01": {
      type: "selection_response",
      tag: "UNIT 3 · BREEDING MILESTONES",
      title: "From Robert Bakewell to Quantitative Genetic Gain (ΔG/year)",
      animated: false,
      controls: selControls
    },
    "u3-t02": {
      type: "quant_variance",
      defaultMode: "gxe",
      tag: "UNIT 3 · BREED CLASSIFICATION",
      title: "Exotic vs Indigenous Breeds: Performance Across Environments",
      animated: false,
      controls: [
        { id: "gxe", type: "slider", label: "Tropical Adaptation Factor", min: 0, max: 1.2, step: 0.05, value: 0.90, format: function (v) { return Math.round(v * 100) + "%"; } }
      ]
    },
    "u3-t03": {
      type: "selection_response",
      tag: "UNIT 3 · ECONOMIC TRAITS",
      title: "Economic Trait Response by Heritability (Fertility vs Milk vs Carcass)",
      animated: false,
      controls: selControls,
      steps: [
        { label: "Fertility (h²=0.05)", apply: function (st) { st.params.h2 = 0.05; st.params.pSel = 25; } },
        { label: "Milk Yield (h²=0.25)", apply: function (st) { st.params.h2 = 0.25; st.params.pSel = 20; } },
        { label: "Fat% / Carcass (h²=0.50)", apply: function (st) { st.params.h2 = 0.50; st.params.pSel = 15; } }
      ]
    },
    "u3-t04": {
      type: "selection_response",
      tag: "UNIT 3 · SELECTION RESPONSE",
      title: "Truncation Selection Lab: ΔG = h²·S = (i · r_IA · σ_A) / L",
      animated: false,
      controls: selControls,
      steps: [
        { label: "Mild Selection (50%)", apply: function (st) { st.params.pSel = 50; } },
        { label: "Dairy Dam Cutoff (20%)", apply: function (st) { st.params.pSel = 20; } },
        { label: "Elite AI Bull (5%)", apply: function (st) { st.params.pSel = 5; } }
      ]
    },
    "u3-t05": {
      type: "sire_blup_onbs",
      tag: "UNIT 3 · BASES OF SELECTION",
      title: "Progeny Testing Accuracy (r_IA) & Daughter Number Simulator",
      animated: false,
      controls: [
        { id: "method", type: "toggle", label: "Evaluation", value: "blup", options: [{ value: "raw", label: "Raw Daughter Avg" }, { value: "blup", label: "Progeny Test (CC/BLUP)" }] },
        { id: "nDau", type: "slider", label: "Number of Progeny (n)", min: 5, max: 120, step: 5, value: 40, format: function (v) { return v + " daughters"; } }
      ]
    },
    "u3-t06": {
      type: "corr_regression",
      tag: "UNIT 3 · INDIRECT SELECTION",
      title: "Correlated Response (CR_Y) via Genetic Correlation (r_G)",
      hint: "Adjust genetic correlation r_G to see how selecting on Trait X pulls Trait Y indirectly",
      interactiveCanvas: true,
      xLabel: "Selected Trait X (e.g., Yearling Weight)",
      yLabel: "Correlated Trait Y (e.g., Mature Weight / Feed Efficiency)",
      controls: [
        { id: "r", type: "slider", label: "Genetic Correlation (r_G)", min: -0.85, max: 0.95, step: 0.05, value: 0.75, format: function (v) { return "r_G = " + Number(v).toFixed(2); } }
      ]
    },
    "u3-t07": {
      type: "multi_trait_selection",
      tag: "UNIT 3 · MULTI-TRAIT SELECTION",
      title: "Tandem vs Independent Culling Levels vs Selection Index Comparator",
      animated: false,
      controls: [
        { id: "method", type: "toggle", label: "Selection Method", value: "index", options: [
          { value: "tandem", label: "Tandem (1 Trait)" },
          { value: "icl", label: "Independent Culling (L-Cut)" },
          { value: "index", label: "Selection Index (Diagonal)" }
        ]}
      ]
    },
    "u3-t08": {
      type: "pedigree_inbreeding",
      tag: "UNIT 3 · MATING SYSTEMS",
      title: "Non-Random Mating Spectrum: Close Inbreeding to Linebreeding",
      animated: false,
      controls: [
        { id: "mating", type: "select", label: "Mating System", value: "halfsib", options: pedigreeOpts },
        { id: "fA", type: "slider", label: "Common Ancestor F_A", min: 0, max: 0.25, step: 0.05, value: 0, format: function (v) { return (v * 100).toFixed(0) + "%"; } }
      ]
    },
    "u3-t09": {
      type: "pedigree_inbreeding",
      tag: "UNIT 3 · WRIGHT'S INBREEDING",
      title: "Wright's Inbreeding Coefficient (F_X) & Relationship (R_XY) Path Tracer",
      animated: false,
      controls: [
        { id: "mating", type: "select", label: "Pedigree Relationship", value: "fullsib", options: pedigreeOpts },
        { id: "fA", type: "slider", label: "Ancestor Inbreeding (F_A)", min: 0, max: 0.25, step: 0.05, value: 0, format: function (v) { return (v * 100).toFixed(0) + "%"; } }
      ]
    },
    "u3-t10": {
      type: "pedigree_inbreeding",
      tag: "UNIT 3 · INBREEDING DEPRESSION",
      title: "Homozygosity Rise & Inbreeding Depression Explorer",
      animated: false,
      controls: [
        { id: "mating", type: "toggle", label: "Inbreeding Intensity", value: "fullsib", options: [
          { value: "cousin", label: "Mild (6.25%)" }, { value: "halfsib", label: "Half-Sib (12.5%)" },
          { value: "fullsib", label: "Full-Sib (25%)" }, { value: "selfing", label: "Extreme (50%)" }
        ]},
        { id: "fA", type: "slider", label: "Prior Ancestor F_A", min: 0, max: 0.25, step: 0.05, value: 0.1, format: function (v) { return (v * 100).toFixed(0) + "%"; } }
      ]
    },
    "u3-t11": {
      type: "crossbreeding_heterosis",
      defaultMode: "grading",
      tag: "UNIT 3 · OUTBREEDING & GRADING-UP",
      title: "Grading-Up Generational Lab (50% → 75% → 87.5% → 98.44% Purebred)",
      animated: false,
      controls: [
        { id: "mode", type: "toggle", label: "Outbreeding Mode", value: "grading", options: [
          { value: "grading", label: "Grading-Up Generations" }, { value: "heterosis", label: "Crossbreeding Systems" }
        ]},
        { id: "gens", type: "slider", label: "Backcross Generations (n)", min: 1, max: 8, step: 1, value: 7, format: function (v) { return "Gen " + v; } }
      ]
    },
    "u3-t12": {
      type: "crossbreeding_heterosis",
      defaultMode: "heterosis",
      tag: "UNIT 3 · HETEROSIS (H%)",
      title: "Crossbreeding & Heterosis (H%) Retention Comparator",
      animated: false,
      controls: [
        { id: "mode", type: "toggle", label: "View", value: "heterosis", options: [
          { value: "heterosis", label: "Heterosis Comparator" }, { value: "grading", label: "Grading-Up" }
        ]},
        { id: "pA", type: "slider", label: "Indigenous Breed Mean (P_A)", min: 1500, max: 3500, step: 100, value: 2200, format: function (v) { return v + " kg"; } },
        { id: "pB", type: "slider", label: "Exotic Breed Mean (P_B)", min: 3000, max: 6000, step: 100, value: 4400, format: function (v) { return v + " kg"; } },
        { id: "f1", type: "slider", label: "F1 Crossbred Mean (F̄₁)", min: 2500, max: 5500, step: 50, value: 3800, format: function (v) { return v + " kg"; } }
      ]
    },
    "u3-t13": {
      type: "crossbreeding_heterosis",
      defaultMode: "heterosis",
      tag: "UNIT 3 · COMBINING ABILITY (RS/RRS)",
      title: "Recurrent & Reciprocal Recurrent Selection (Specific Combining Ability)",
      animated: false,
      controls: [
        { id: "pA", type: "slider", label: "Line A Performance", min: 1800, max: 3200, step: 100, value: 2400, format: function (v) { return v + " kg"; } },
        { id: "pB", type: "slider", label: "Line B Performance", min: 2800, max: 4600, step: 100, value: 3600, format: function (v) { return v + " kg"; } },
        { id: "f1", type: "slider", label: "Crossbred (A×B) F1 Merit", min: 2600, max: 5000, step: 50, value: 3750, format: function (v) { return v + " kg"; } }
      ]
    },
    "u3-t14": {
      type: "crossbreeding_heterosis",
      defaultMode: "grading",
      tag: "UNIT 3 · DAIRY CATTLE & BUFFALO",
      title: "Indian Dairy Breeding: Grading-Up Murrah/Sahiwal & Crossbreeding",
      animated: false,
      controls: [
        { id: "mode", type: "toggle", label: "Strategy", value: "grading", options: [
          { value: "grading", label: "Grading-Up Nondescript" }, { value: "heterosis", label: "Exotic Crossbreeding" }
        ]},
        { id: "gens", type: "slider", label: "Generations of Purebred Sire Use", min: 1, max: 8, step: 1, value: 6, format: function (v) { return "G" + v; } }
      ]
    },
    "u3-t15": {
      type: "selection_response",
      tag: "UNIT 3 · SHEEP, GOAT & SWINE",
      title: "Short Generation Interval (L) Advantage in Small Ruminants & Swine",
      animated: false,
      controls: [
        { id: "pSel", type: "slider", label: "Replacement Selection %", min: 5, max: 60, step: 5, value: 15, format: function (v) { return "Top " + v + "%"; } },
        { id: "h2", type: "slider", label: "Trait h² (Fleece/Growth/Litter)", min: 0.10, max: 0.55, step: 0.05, value: 0.35, format: function (v) { return "h² = " + Number(v).toFixed(2); } },
        { id: "L", type: "slider", label: "Generation Interval L (Swine ~2 yr, Sheep ~3 yr)", min: 1.5, max: 5.0, step: 0.5, value: 2.0, format: function (v) { return Number(v).toFixed(1) + " yrs"; } }
      ]
    },
    "u3-t16": {
      type: "crossbreeding_heterosis",
      defaultMode: "heterosis",
      tag: "UNIT 3 · COMMERCIAL POULTRY",
      title: "Commercial Layer & Broiler 3-Way / 4-Way Cross Hybrid Vigour",
      animated: false,
      controls: [
        { id: "pA", type: "slider", label: "Sire Line (Cornish) Index", min: 1800, max: 3500, step: 100, value: 2500, format: function (v) { return v + " g"; } },
        { id: "pB", type: "slider", label: "Dam Line (Plymouth Rock) Index", min: 1800, max: 3500, step: 100, value: 2300, format: function (v) { return v + " g"; } },
        { id: "f1", type: "slider", label: "Commercial Broiler Hybrid", min: 2000, max: 4200, step: 50, value: 2850, format: function (v) { return v + " g"; } }
      ]
    },
    "u3-t17": {
      type: "sire_blup_onbs",
      tag: "UNIT 3 · SIRE EVALUATION & BLUP",
      title: "Raw Daughter Average vs Contemporary Comparison & BLUP Ranking Lab",
      animated: false,
      controls: [
        { id: "method", type: "toggle", label: "Evaluation Method", value: "blup", options: [
          { value: "raw", label: "Raw Daughter Avg (Biased!)" },
          { value: "blup", label: "Contemporary Comp. / BLUP" }
        ]},
        { id: "nDau", type: "slider", label: "Daughters per Sire (n)", min: 5, max: 120, step: 5, value: 40, format: function (v) { return v + " daughters"; } }
      ]
    },
    "u3-t18": {
      type: "sire_blup_onbs",
      tag: "UNIT 3 · ONBS (OPEN NUCLEUS)",
      title: "Open Nucleus Breeding System (ONBS) & Elite Sire Selection",
      animated: false,
      controls: [
        { id: "method", type: "toggle", label: "Sire Selection", value: "blup", options: [
          { value: "blup", label: "ONBS BLUP Ranking" }, { value: "raw", label: "Unadjusted Herd Avg" }
        ]},
        { id: "nDau", type: "slider", label: "Nucleus + Base Progeny", min: 10, max: 120, step: 10, value: 60, format: function (v) { return v + " records"; } }
      ]
    },
    "u3-t19": {
      type: "crossbreeding_heterosis",
      defaultMode: "heterosis",
      tag: "UNIT 3 · BREED SYNTHESIS",
      title: "Synthetic Breed Formation (Karan Swiss, Karan Fries, Vrindavani, Avikalin)",
      animated: false,
      controls: [
        { id: "pA", type: "slider", label: "Indigenous Parent (Sahiwal/Hariana)", min: 1600, max: 3000, step: 100, value: 2100, format: function (v) { return v + " kg"; } },
        { id: "pB", type: "slider", label: "Exotic Parent (HF / Brown Swiss)", min: 3500, max: 6000, step: 100, value: 4800, format: function (v) { return v + " kg"; } },
        { id: "f1", type: "slider", label: "Synthesized Stabilized Population", min: 2500, max: 5200, step: 50, value: 3850, format: function (v) { return v + " kg"; } }
      ]
    },
    "u3-t20": {
      type: "crossbreeding_heterosis",
      defaultMode: "grading",
      tag: "UNIT 3 · NATIONAL BREEDING POLICY",
      title: "Indian National Breeding Policy: Stabilizing 50–62.5% Exotic & Grading-Up",
      animated: false,
      controls: [
        { id: "mode", type: "toggle", label: "Policy Tool", value: "grading", options: [
          { value: "grading", label: "Grading-Up Nondescript" }, { value: "heterosis", label: "Crossbred Stabilization" }
        ]},
        { id: "gens", type: "slider", label: "Generations", min: 1, max: 8, step: 1, value: 5, format: function (v) { return "G" + v; } }
      ]
    },
    "u3-t21": {
      type: "hardy_weinberg",
      tag: "UNIT 3 · AnGR CONSERVATION",
      title: "Endangered Indigenous Breeds: Genetic Drift Risk at Small Nₑ",
      animated: false,
      controls: [
        { id: "p0", type: "slider", label: "Rare Allele Frequency (p)", min: 0.1, max: 0.9, step: 0.05, value: 0.35, format: function (v) { return Number(v).toFixed(2); } },
        { id: "ne", type: "slider", label: "Effective Breed Size (Nₑ)", min: 15, max: 300, step: 15, value: 30, format: function (v) { return "Nₑ = " + v; } }
      ]
    },
    "u3-t22": {
      type: "selection_response",
      tag: "UNIT 3 · AI, MOET & GENOMIC SELECTION",
      title: "How AI, MOET & Genomic Selection Slash Generation Interval (L) & Boost ΔG/yr",
      animated: false,
      controls: selControls,
      steps: [
        { label: "Conventional PT (L=6.5 yr)", apply: function (st) { st.params.L = 6.5; st.params.pSel = 15; } },
        { label: "MOET Nucleus (L=3.5 yr)", apply: function (st) { st.params.L = 3.5; st.params.pSel = 10; } },
        { label: "Genomic Selection (L=2.0 yr)", apply: function (st) { st.params.L = 2.0; st.params.pSel = 5; } }
      ]
    },
    "u3-t23": {
      type: "hardy_weinberg",
      tag: "UNIT 3 · DISEASE RESISTANCE",
      title: "Selection Against Susceptible Recessive Alleles (BLAD / CVM / Scrapie)",
      animated: false,
      controls: [
        { id: "p0", type: "slider", label: "Resistant Allele Freq (p)", min: 0.1, max: 0.9, step: 0.05, value: 0.5, format: function (v) { return Number(v).toFixed(2); } },
        { id: "s", type: "slider", label: "Selection Against Susceptible (s)", min: 0, max: 0.9, step: 0.05, value: 0.5, format: function (v) { return "s = " + Number(v).toFixed(2); } }
      ]
    },
    "u3-t24": {
      type: "karyotype_3d",
      is3D: true,
      autoPlay: true,
      tag: "UNIT 3 · DOG & CAT BREEDS",
      title: "Companion Animal Cytogenetics: Dog (2n=78) vs Cat (2n=38) & Pedigree",
      controls: [
        { id: "species", type: "toggle", label: "Companion Species", value: "dog", options: [
          { value: "dog", label: "Dog (2n=78, Acrocentric)" }, { value: "cat", label: "Cat (2n=38, Bi-armed)" }
        ]},
        { id: "morph", type: "toggle", label: "Chromosome Type", value: "acrocentric", options: [
          { value: "acrocentric", label: "Acrocentric" }, { value: "metacentric", label: "Metacentric" }
        ]}
      ]
    },
    "u3-t25": {
      type: "pedigree_inbreeding",
      tag: "UNIT 3 · CANINE/FELINE BREEDING",
      title: "Pedigree Inbreeding Check in Purebred Dog & Cat Breeding",
      animated: false,
      controls: [
        { id: "mating", type: "select", label: "Planned Mating", value: "cousin", options: pedigreeOpts },
        { id: "fA", type: "slider", label: "Champion Sire F_A", min: 0, max: 0.25, step: 0.05, value: 0.05, format: function (v) { return (v * 100).toFixed(0) + "%"; } }
      ]
    },
    "u3-t26": {
      type: "karyotype_3d",
      is3D: true,
      autoPlay: true,
      tag: "UNIT 3 · PET BIRDS BREEDING",
      title: "Avian ZZ (Male) / ZW (Female) Genetics & Sex-Linked Plumage",
      controls: [
        { id: "species", type: "toggle", label: "Avian Model", value: "chicken", options: [
          { value: "chicken", label: "Avian ZZ♂ / ZW♀ (2n=78)" }
        ]},
        { id: "morph", type: "toggle", label: "Macrochromosome Shape", value: "metacentric", options: [
          { value: "metacentric", label: "Metacentric" }, { value: "submetacentric", label: "Submetacentric" }
        ]}
      ]
    },
    "u3-t27": {
      type: "hardy_weinberg",
      tag: "UNIT 3 · WILDLIFE Nₑ & DRIFT",
      title: "Captive Wildlife Population Dynamics: Small Nₑ & Genetic Bottleneck",
      animated: false,
      controls: [
        { id: "p0", type: "slider", label: "Founder Allele Freq (p)", min: 0.1, max: 0.9, step: 0.05, value: 0.5, format: function (v) { return Number(v).toFixed(2); } },
        { id: "ne", type: "slider", label: "Effective Population Size (Nₑ)", min: 10, max: 250, step: 10, value: 20, format: function (v) { return "Nₑ = " + v; } }
      ]
    },
    "u3-t28": {
      type: "pedigree_inbreeding",
      tag: "UNIT 3 · WILDLIFE CONSERVATION",
      title: "Zoo Studbook & Minimum-Inbreeding Mating Planner",
      animated: false,
      controls: [
        { id: "mating", type: "select", label: "Captive Pairing Scenario", value: "halfsib", options: pedigreeOpts },
        { id: "fA", type: "slider", label: "Founder Inbreeding (F_A)", min: 0, max: 0.25, step: 0.05, value: 0, format: function (v) { return (v * 100).toFixed(0) + "%"; } }
      ]
    }
  });
})();
