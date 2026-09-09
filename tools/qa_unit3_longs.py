# -*- coding: utf-8 -*-
"""
Unit 3: 5 Twelve-Mark Long Essay Questions (u3-q21 to u3-q25)
Animal Breeding Principles, Selection, Mating Systems & Improvement (VCI MSVE 2016 Standard)
"""

questions = [
    {
        "id": "u3-q21",
        "type": "long",
        "marks": 12,
        "question": (
            "Describe the various Bases of Selection used in domestic livestock improvement: Individual (Mass) Selection, "
            "Pedigree Selection, Collateral / Sib Selection, and Progeny Testing. Compare their principles, accuracy of estimating "
            "breeding value (r_AI), advantages, limitations, and suitability for different livestock traits. Present a comprehensive "
            "comparative summary table."
        ),
        "topicId": "u3-t02",
        "answer": (
            "<b>1. Introduction to Bases of Selection:</b><br>"
            "Selection is the non-random process that determines which individuals become parents of the next generation and how many "
            "offspring they produce. The effectiveness of selection depends on the <b>accuracy of predicting an individual's true additive "
            "breeding value (r<sub>AI</sub>)</b>. Animal breeders utilize information from four primary sources: the individual's own phenotype, "
            "ancestral pedigree records, collateral relatives (sibs), and progeny performance.<br><br>"
            "<b>2. Detailed Analysis of Each Selection Base:</b><br><br>"
            "<b>A. Individual (Mass) Selection:</b>"
            "<ul>"
            "<li><b>Principle:</b> Animals are evaluated and selected purely on their own individual phenotypic record, regardless of relatives.</li>"
            "<li><b>Accuracy:</b> <code>r<sub>AI</sub> = h = &radic;(h&sup2;)</code> (The square root of narrow-sense heritability).</li>"
            "<li><b>Advantages:</b> Simplest, lowest cost; does not require pedigree maintenance; allows high selection intensity and short generation interval.</li>"
            "<li><b>Limitations:</b> Highly inaccurate for low-heritability traits (<code>h&sup2; &lt; 0.15</code>); completely inapplicable for <b>sex-limited traits</b> in the non-expressing sex (e.g., selecting bulls for milk yield or roosters for egg production); useless for carcass traits requiring slaughter.</li>"
            "<li><b>Trait Suitability:</b> Growth rate, yearling body weight in sheep/swine/beef cattle, fleece weight, and backfat thickness measured by ultrasound.</li>"
            "</ul><br>"
            "<b>B. Pedigree Selection:</b>"
            "<ul>"
            "<li><b>Principle:</b> Selection based on the phenotypic performance of ancestors (parents, grandparents).</li>"
            "<li><b>Accuracy:</b> Based on single parent: <code>r<sub>AI</sub> = &frac12; h</code>; based on mid-parent: <code>r<sub>AI</sub> = h &times; &radic;[1 / (2 - h&sup2;)]</code> (Maximum theoretical accuracy from parents alone cannot exceed <code>1/&radic;2 = 0.71</code> even if <code>h&sup2; = 1.0</code>).</li>"
            "<li><b>Advantages:</b> Allows selection at an extremely young age (at birth or calfhood), minimizing generation interval; useful for sex-limited traits.</li>"
            "<li><b>Limitations:</b> Lower accuracy than individual selection for high-h² traits; cannot evaluate Mendelian sampling variance (variation among full sibs with identical parents). Over-reliance leads to inbreeding.</li>"
            "<li><b>Trait Suitability:</b> Preliminary screening of young dairy bulls and replacement heifers prior to maturity.</li>"
            "</ul><br>"
            "<b>C. Collateral / Sib Selection (Half-Sibs & Full-Sibs):</b>"
            "<ul>"
            "<li><b>Principle:</b> Selection based on the performance of collateral relatives of the same generation (brothers, sisters, half-sibs). Categorized into <b>Full-sib selection</b> (information from full-brothers/sisters) and <b>Half-sib selection</b>.</li>"
            "<li><b>Accuracy for <code>n</code> half-sibs:</b> <code>r<sub>AI</sub> = &frac14; n h&sup2; / &radic;[ n &times; (1 + (n - 1) &times; &frac14; h&sup2;) ]</code>. As <code>n &rarr; &infin;</code>, maximum accuracy reaches <code>0.50</code>.</li>"
            "<li><b>Advantages:</b> Essential for <b>carcass traits</b> (dressing percentage, meat tenderness, intramuscular marbling) where candidate breeding animals cannot be slaughtered themselves; valuable for sex-limited traits.</li>"
            "<li><b>Limitations:</b> Half-sib accuracy capped at 0.50; full-sibs share common maternal environment (<code>c&sup2;</code>), which can bias genetic estimates.</li>"
            "<li><b>Trait Suitability:</b> Carcass quality in pigs, broilers, and feedlot cattle.</li>"
            "</ul><br>"
            "<b>D. Progeny Testing:</b>"
            "<ul>"
            "<li><b>Principle:</b> Selection of breeding parents (particularly sires) based on the average phenotypic performance of a representative, randomly distributed sample of their daughters/offspring.</li>"
            "<li><b>Accuracy for <code>n</code> progeny:</b> <code>r<sub>AI</sub> = &radic;[ n / {n + (4 - h&sup2;) / h&sup2;} ]</code>.<br>"
            "As progeny number <code>n &rarr; &infin;</code>, <b>accuracy approaches 1.00 (100% certainty)</b> regardless of heritability! With 50 daughters, accuracy exceeds <code>0.85</code> even for traits with <code>h&sup2; = 0.20</code>.</li>"
            "<li><b>Advantages:</b> Highest possible accuracy; the definitive gold standard for sex-limited traits (milk yield in dairy bulls) and low-heritability fitness traits.</li>"
            "<li><b>Limitations:</b> <b>Severely prolongs generation interval (L)</b>: in dairy bulls, testing requires ~5 to 6 years (conception, gestation, calf rearing, daughter pregnancy, 305-day lactation), which drastically reduces annual genetic gain (<code>&Delta;G/year = R / L</code>); very expensive and requires extensive field artificial insemination recording.</li>"
            "<li><b>Trait Suitability:</b> National dairy sire evaluation schemes (e.g., Murrah buffalo and HF/Jersey crossbred bulls in India).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Introduction: Selection defined; accuracy r_AI measures correlation between estimated and true breeding value.",
            "Individual Selection: r_AI = h; simple and short generation interval; fails for sex-limited and carcass traits.",
            "Pedigree Selection: r_AI <= 0.71; enables early calfhood screening; ignores Mendelian sampling.",
            "Sib Selection: Indispensable for carcass quality and meat traits requiring slaughter.",
            "Progeny Testing: r_AI approaches 1.00 as n -> inf; ultimate accuracy for sex-limited traits; drawback is prolonged generation interval (5-6 years) and high cost.",
            "Comprehensive comparative evaluation table."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Comparison of Bases of Selection in Farm Animals",
            "headers": ["Selection Base", "Information Source", "Accuracy Formula (r_AI)", "Max Accuracy", "Generation Interval (L)", "Best Suited Traits"],
            "rows": [
                ["Individual (Mass)", "Individual's own phenotype", "r_AI = √h² = h", "1.00 (if h²=1)", "Short (evaluated at maturity)", "High h² traits expressed in both sexes (body weight, fleece weight, backfat)"],
                ["Pedigree", "Ancestors (sire, dam, grandparents)", "r_AI = 0.5 * h (one parent)", "0.71 (mid-parent)", "Very Short (evaluated at birth/weaning)", "Early screening of young dairy bulls & heifers prior to production"],
                ["Sib Selection", "Collateral relatives (full-sibs or half-sibs)", "r_AI = (1/4 n h²) / √[n (1 + (n-1) 1/4 h²)]", "0.50 (half-sibs) / 0.71 (full-sibs)", "Intermediate (same generation)", "Carcass traits requiring slaughter (dressing %, meat quality) in swine/poultry"],
                ["Progeny Testing", "Daughters / Offspring performance", "r_AI = √[n / (n + (4-h²)/h²)]", "Approaches 1.00 as n -> ∞", "Very Long (5-6 yrs in dairy cattle)", "Sex-limited traits (milk yield) and low h² fertility/fitness traits in dairy sires"]
            ]
        },
        "pyq": ["VCI Annual 2017", "IVRI 2019", "TANUVAS 2020", "GADVASU 2021", "KVASU 2022", "LUVAS 2023"]
    },
    {
        "id": "u3-q22",
        "type": "long",
        "marks": 12,
        "question": (
            "Define and classify Systems of Mating in livestock. Describe Inbreeding, detailing Wright's Path Coefficient method "
            "for calculating Inbreeding Coefficient (FX) and Coefficient of Relationship (RXY). Describe Outbreeding systems: "
            "Outcrossing, Crossbreeding (Two-way, Three-way, Rotational/Criss-crossing, and Terminal crossing), and Grading Up. "
            "Construct a table showing the recovery of superior germplasm across five generations of Grading Up."
        ),
        "topicId": "u3-t10",
        "answer": (
            "<b>1. Definition and Classification of Systems of Mating:</b><br>"
            "Mating systems refer to the planned rules according to which selected males and females are paired for reproduction. "
            "Unlike selection (which changes gene frequencies), <b>mating systems alter genotypic frequencies</b> by reorganizing genes into homozygous or heterozygous combinations.<br><br>"
            "<b>Classification of Mating Systems:</b>"
            "<ul>"
            "<li><b>1. Random Mating (Panmixia):</b> Each male has an equal probability of mating with any female in the population (maintains Hardy-Weinberg equilibrium).</li>"
            "<li><b>2. Assortative Mating:</b> Non-random pairing based on phenotypic resemblance:"
            "<ul>"
            "<li><i>Positive Assortative:</i> Mating 'like to like' (best to best) &rarr; increases phenotypic variance and extremes.</li>"
            "<li><i>Negative Assortative (Disassortative):</i> Mating 'unlike to unlike' (e.g., large bull to small cow) &rarr; reduces variance, promotes uniformity.</li>"
            "</ul></li>"
            "<li><b>3. Inbreeding:</b> Mating of individuals more closely related to each other than the average relationship of the population (increases homozygosity).</li>"
            "<li><b>4. Outbreeding:</b> Mating of individuals less closely related than the population average (increases heterozygosity and induces heterosis).</li>"
            "</ul><br>"
            "<b>2. Inbreeding & Wright's Path Coefficient Method:</b><br>"
            "<b>Sewall Wright's Formula for Inbreeding Coefficient (F<sub>X</sub>):</b><br>"
            "<b><code>F<sub>X</sub> = &sum; [ (&frac12;)<sup>n1 + n2 + 1</sup> &times; (1 + F<sub>A</sub>) ]</code></b><br>"
            "where: <code>n1</code> = number of generations from Sire (S) back to common ancestor (A);<br>"
            "<code>n2</code> = number of generations from Dam (D) back to common ancestor (A);<br>"
            "<code>F<sub>A</sub></code> = inbreeding coefficient of the common ancestor <i>A</i>.<br><br>"
            "<b>Coefficient of Relationship between two individuals X and Y (R<sub>XY</sub>):</b><br>"
            "<b><code>R<sub>XY</sub> = [ &sum; (&frac12;)<sup>n1 + n2</sup> &times; (1 + F<sub>A</sub>) ] / &radic;[ (1 + F<sub>X</sub>)(1 + F<sub>Y</sub>) ]</code></b><br><br>"
            "<i>Path Analysis Protocol:</i>"
            "<ol>"
            "<li>Convert arrow pedigree into a clean path diagram showing common ancestors connecting sire and dam.</li>"
            "<li>Identify all independent common ancestors.</li>"
            "<li>Trace all non-repeating paths from sire up to common ancestor and down to dam: <code>S &larr; ... &larr; A &rarr; ... &rarr; D</code>.</li>"
            "<li>Sum <code>(&frac12;)<sup>n</sup></code> across all independent paths.</li>"
            "</ol><br>"
            "<b>3. Outbreeding Systems in Domestic Livestock:</b>"
            "<ul>"
            "<li><b>A. Outcrossing:</b> Mating of unrelated purebred animals within the same registered breed (no common ancestor in first 4&ndash;6 generations). Main tool to introduce fresh vigor and avoid inbreeding in purebred dairy herds.</li>"
            "<li><b>B. Crossbreeding:</b> Mating of animals of two or more distinct established breeds. Exploits breed complementarity and heterosis:</li>"
            "<ul>"
            "<li><i>Two-Way Cross (Single Cross):</i> Breed A &times; Breed B &rarr; F1 crossbred (e.g., Karan Swiss: Sahiwal &times; Brown Swiss; Karan Fries: Tharparkar &times; Holstein Friesian).</li>"
            "<li><i>Three-Way Cross:</i> Crossbred F1 females (A &times; B) are mated to a third distinct purebred terminal sire breed (C) &rarr; Progeny [50% C, 25% A, 25% B]. Combines maternal heterosis of F1 dams with individual heterosis in market stock (standard in commercial pigs and market lambs).</li>"
            "<li><i>Criss-Crossing (Two-Breed Rotational Cross):</i> F1 crossbred cows are mated to purebred Sire of Breed A. Their female progeny are mated to purebred Sire of Breed B, alternating sire breeds in each generation. Maintains ~67% of maximum possible heterosis continuously without buying replacement females.</li>"
            "<li><i>Terminal Crossing:</i> All crossbred male and female offspring are sold for slaughter/meat; zero females are retained as breeding replacements (e.g., commercial broilers and terminal beef crossbreeding).</li>"
            "</ul>"
            "<li><b>C. Grading Up:</b> Mating purebred superior sires of a recognized breed to nondescript indigenous scrub females and their female descendants generation after generation. It is the fastest, cheapest method to transform a low-producing nondescript population into a high-grade productive herd.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Classification: Panmixia, assortative mating, inbreeding (increases homozygosity), and outbreeding (increases heterozygosity).",
            "Wright's formula for inbreeding (F_X) and relationship (R_XY) with path analysis rules.",
            "Outbreeding types: Outcrossing, Crossbreeding (Two-way, Three-way, Rotational/Criss-crossing, Terminal crossing), and Grading Up.",
            "Table showing progressive recovery of superior germplasm across 5 generations of Grading Up (50%, 75%, 87.5%, 93.75%, 96.88%)."
        ],
        "diagram": "",
        "table": {
            "title": "Grading Up: Progressive Recovery of Superior Purebred Inheritance Across Generations",
            "headers": ["Generation", "Mating Type (Sire x Dam)", "Superior / Improved Breed Inheritance", "Nondescript / Scrub Inheritance"],
            "rows": [
                ["Generation 1 (G1 / F1)", "Purebred Sire (100%) x Nondescript Dam (0%)", "1/2 = 50.00%", "1/2 = 50.00%"],
                ["Generation 2 (G2)", "Purebred Sire (100%) x G1 Female (50%)", "3/4 = 75.00%", "1/4 = 25.00%"],
                ["Generation 3 (G3)", "Purebred Sire (100%) x G2 Female (75%)", "7/8 = 87.50%", "1/8 = 12.50%"],
                ["Generation 4 (G4)", "Purebred Sire (100%) x G3 Female (87.5%)", "15/16 = 93.75%", "1/16 = 6.25%"],
                ["Generation 5 (G5)", "Purebred Sire (100%) x G4 Female (93.75%)", "31/32 = 96.88%", "1/32 = 3.12%"]
            ]
        },
        "pyq": ["VCI Annual 2018", "TANUVAS 2019", "IVRI 2020", "GADVASU 2021", "KVASU 2022", "MAFSU 2023"]
    },
    {
        "id": "u3-q23",
        "type": "long",
        "marks": 12,
        "question": (
            "Discuss the National Breeding Policies and Strategies for the Genetic Improvement of Dairy Cattle and Buffaloes in India. "
            "Detail: (a) Selective breeding in indigenous cattle breeds; (b) Crossbreeding policy with exotic germplasm, including the rationale "
            "for maintaining 50% to 62.5% exotic inheritance; (c) Problems of F2 breakdown and inter-se mating; (d) Grading up of nondescript "
            "buffaloes with Murrah / Nili-Ravi; and (e) Modern Progeny Testing and Field Progeny Testing (PT) schemes under the National Dairy Plan."
        ),
        "topicId": "u3-t17",
        "answer": (
            "<b>1. Overview of Indian Dairy Production Environment:</b><br>"
            "India is the world's largest milk producer (>230 million tonnes), characterized by a tropical climate with high heat/humidity, "
            "prevalence of tropical vector-borne diseases (tick-borne haemoparasites like Theileriosis, Babesiosis), low-to-medium quality crop "
            "residue feeding, and smallholder production systems. Hence, the National Breeding Policy balances high milk production with "
            "thermal tolerance, disease resistance, and reproductive longevity.<br><br>"
            "<b>2. Key Strategic Pillars of Cattle & Buffalo Improvement:</b><br><br>"
            "<b>A. Selective Breeding in Defined Indigenous Cattle Breeds:</b>"
            "<ul>"
            "<li>Recognized milch breeds (<b>Gir, Sahiwal, Red Sindhi, Tharparkar</b>) and dual-purpose breeds (<b>Kankrej, Hariana, Ongole</b>) possess superior thermotolerance (sweat gland density, slick coat), resistance to tropical haemoprotozoans, and high butterfat (A2 beta-casein allele).</li>"
            "<li>Policy mandates <b>pure selective breeding</b> in their native breeding tracts: identifying elite bull mothers, producing pedigree bulls, and conducting progeny testing/genomic evaluation without introducing exotic genes.</li>"
            "</ul><br>"
            "<b>B. Crossbreeding Policy with Exotic Germplasm & The 50&ndash;62.5% Optimum Level:</b>"
            "<ul>"
            "<li>Implemented for nondescript (scrub) zebu cattle in areas with adequate feed and veterinary support using <b>Holstein Friesian (HF)</b> in temperate/irrigated belts and <b>Jersey</b> in hot-humid/hilly coastal regions.</li>"
            "<li><b>Why Maintain 50% to 62.5% Exotic Inheritance?</b>"
            "<ul>"
            "<li><i>At 50% Exotic Level (F1 Crossbred):</i> Perfect balance: 50% exotic milk production genetics combined with 50% zebu tropical adaptability and <b>100% individual heterosis</b>. Yield increases 3 to 4 fold (from 800 kg to 2800&ndash;3200 kg per lactation), age at first calving drops from 45 months to 28&ndash;30 months.</li>"
            "<li><i>Beyond 62.5% Exotic Inheritance:</i> Severe deterioration occurs: tropical heat distress (rectal temperature rises, panting), high susceptibility to theileriosis, mastitis, repeat breeding, and high mortality under Indian climatic conditions.</li>"
            "<li><i>Below 50% Exotic Level:</i> Milk production drops substantially, failing to satisfy economic returns.</li>"
            "</ul></li>"
            "</ul><br>"
            "<b>C. Problems of F2 Breakdown and Inter-Se Mating Challenges:</b>"
            "<ul>"
            "<li>When F1 crossbreds are inter-se mated (<code>F1 &times; F1 &rarr; F2</code>), crossbred performance drops by <b>15&ndash;25%</b>.</li>"
            "<li><b>Genetic Causes of F2 Breakdown:</b> (i) <b>Loss of 50% heterosis</b> due to segregation; (ii) Breakup of favorable epistatic gene complexes (linkage disequilibrium breakdown) through meiotic recombination; (iii) Wide phenotypic segregation producing huge variability in coat type, body size, and productivity.</li>"
            "<li><b>Management of Inter-se Mating:</b> Handled by rigorous progeny testing of crossbred bulls and multi-breed composite synthesis (e.g., Frieswal = 62.5% HF + 37.5% Sahiwal, developed by ICAR-CIRC and Military Farms).</li>"
            "</ul><br>"
            "<b>D. Grading Up of Nondescript Buffaloes with Murrah / Nili-Ravi:</b>"
            "<ul>"
            "<li>Buffaloes contribute >50% of total national milk production and the majority of high-fat milk.</li>"
            "<li>Nondescript riverine buffaloes across central and peninsular India are systematically <b>graded up using frozen semen of pedigreed Murrah or Nili-Ravi bulls</b>.</li>"
            "<li>By G4/G5 generations (93.75&ndash;96.88% Murrah inheritance), buffaloes produce >2000 kg milk per lactation with 7&ndash;8% fat, transforming rural dairy economies.</li>"
            "</ul><br>"
            "<b>E. Progeny Testing (PT) and Pedigree Selection under National Dairy Plan (NDP):</b>"
            "<ul>"
            "<li>Under Rashtriya Gokul Mission and NDP-I (implemented by NDDB), large-scale <b>Field Progeny Testing (FPT)</b> programs are operational for Murrah, Mehsana, Gir, Sahiwal, and CB Frieswal.</li>"
            "<li>Young bulls (minimum 25&ndash;50 bulls/batch) are test-mated to thousands of registered farmer cows via AI; first-lactation milk records of 80&ndash;100 daughters per bull are recorded under field conditions using Animal Information Network (INAPH / Pashu Aadhaar). Top 10% proven bulls are selected for semen production.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "National breeding policy context: Balancing tropical resilience (A2 milk, heat tolerance) with productivity.",
            "Selective breeding for indigenous milch breeds (Gir, Sahiwal, Red Sindhi, Tharparkar).",
            "Crossbreeding with HF and Jersey: Scientific justification for maintaining 50% to 62.5% exotic inheritance limit.",
            "F2 breakdown analysis: Loss of 50% heterosis, recombination loss of epistatic complexes, increased segregation variance; Frieswal composite solution.",
            "Grading up nondescript buffaloes with Murrah/Nili-Ravi.",
            "Field Progeny Testing (FPT) and Pedigree Selection under NDDB/RGM using INAPH ear-tag tracking."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["VCI Annual 2017", "IVRI 2019", "TANUVAS 2020", "GADVASU 2021", "KVASU 2022", "LUVAS 2023"]
    },
    {
        "id": "u3-q24",
        "type": "long",
        "marks": 12,
        "question": (
            "Describe the Commercial Poultry Breeding Structure for the production of Hybrid Commercial Broilers and Egg Layers. "
            "Detail: (a) The 4-Way Cross Breeding Hierarchy (GGP, GP, Parent Stock, Commercial Hybrid); (b) Trait selection criteria "
            "for Male (Sire) vs Female (Dam) lines; (c) Role of sex-linked genes (rapid/slow feathering, silver/gold) in Day-Old Chick Auto-Sexing; "
            "and (d) Development of Rural / Backyard Poultry varieties in India (Vanaraja, Gramapriya, Giriraja)."
        ),
        "topicId": "u3-t21",
        "answer": (
            "<b>1. Commercial Poultry Breeding Hierarchy (The 4-Way Cross Pyramid):</b><br>"
            "Modern commercial poultry production is the most sophisticated and mathematically optimized sector in animal agriculture. "
            "Commercial birds are never purebreds; they are <b>four-line terminal crossbred hybrids</b> developed through a strict four-tier pyramid:<br>"
            "<ul>"
            "<li><b>Tier 1: Pedigree / Great-Grandparent (GGP) Lines:</b> Maintained as closed pure lines (Line A, B, C, D) under intense biosecurity. Selected via Reciprocal Recurrent Selection (RRS), family selection, and individual selection with very high selection intensity (top 1&ndash;5%).</li>"
            "<li><b>Tier 2: Grandparent (GP) Stock:</b> Crosses made within sire side (<code>A &male; &times; B &female; &rarr; AB</code>) and within dam side (<code>C &male; &times; D &female; &rarr; CD</code>).</li>"
            "<li><b>Tier 3: Parent Stock (PS):</b> Crossbred Parent females (<code>CD</code>) and Parent males (<code>AB</code>) distributed to commercial franchised hatcheries. Exploit maternal heterosis (CD dams produce maximum fertile hatching eggs).</li>"
            "<li><b>Tier 4: Commercial End-Products:</b> Mating of Parent male &times; Parent female: <code>AB &male; &times; CD &female; &rarr; ABCD Commercial Hybrid</code> (Broiler or Layer). Expresses maximum four-way individual and maternal heterosis (100% uniformity and vigor).</li>"
            "</ul><br>"
            "<b>2. Trait Selection Criteria: Sire Line vs Dam Line:</b>"
            "<ul>"
            "<li><b>Male / Sire Line (Lines A & B):</b> Heavy emphasis on rapid juvenile growth rate, breast meat yield, Feed Conversion Ratio (FCR), livability, and skeletal conformation. In layers: early sexual maturity and egg size.</li>"
            "<li><b>Female / Dam Line (Lines C & D):</b> Heavy emphasis on female reproductive fitness: total egg production, peak egg production persistency, hatchability, shell quality, fertility, and maternal feed efficiency.</li>"
            "</ul><br>"
            "<b>3. Day-Old Chick Auto-Sexing Using Sex-Linked Genes:</b><br>"
            "In commercial hatcheries, determining sex at day-old is critical (cockerels in layers are discarded; broilers can be reared sex-separate). Vent sexing is slow and expensive. <b>Sex-linked auto-sexing</b> enables instant, 100% accurate visual sexing by non-technical labor.<br><br>"
            "<b>A. Rapid vs Slow Feathering (K / k locus on Z chromosome):</b><br>"
            "<ul>"
            "<li>Slow feathering allele (<code>K</code>) is dominant over rapid feathering (<code>k</code>). In birds, males are homogametic (<code>ZZ</code>) and females heterogametic (<code>ZW</code>).</li>"
            "<li><b>Mating Design:</b> Rapid feathering Male (<code>k k</code>) &times; Slow feathering Female (<code>K W</code>):</li>"
            "<li><b>Female Chicks (Pullets):</b> Inherit Z from sire &rarr; <b><code>k W</code> (Rapid feathering)</b>: Primary wing covert feathers are distinctly longer than under-coverts at hatch.</li>"
            "<li><b>Male Chicks (Cockerels):</b> Inherit Z from dam &rarr; <b><code>K k</code> (Slow feathering)</b>: Primary wing feathers are the same length or shorter than covert feathers.</li>"
            "</ul><br>"
            "<b>B. Silver vs Gold Plumage (S / s locus on Z chromosome):</b><br>"
            "<ul>"
            "<li>Silver (<code>S</code>) is dominant over Gold/Red (<code>s</code>).</li>"
            "<li><b>Mating Design:</b> Gold Male (<code>s s</code>, e.g., Rhode Island Red) &times; Silver Female (<code>S W</code>, e.g., White Wyandotte):</li>"
            "<li><b>Female Pullets:</b> <b><code>s W</code> (Gold / Brown down)</b>.</li>"
            "<li><b>Male Cockerels:</b> <b><code>S s</code> (Silver / Creamy White down)</b>. Instant sorting by down color.</li>"
            "</ul><br>"
            "<b>4. Rural & Backyard Poultry Development in India:</b><br>"
            "To uplift rural tribal livelihoods and provide nutritional security, ICAR institutions developed hardy, multi-colored dual-purpose crossbred chicken varieties that thrive under scavenged backyard scavenging without commercial feed:"
            "<ul>"
            "<li><b>Vanaraja (ICAR-DPR, Hyderabad):</b> Multi-colored dual-purpose cross bred for free-range rural farming. Body weight: 1.5&ndash;1.8 kg at 12 weeks; produces 100&ndash;110 large brown eggs/year under scavenging. High immune competence against Ranikhet disease.</li>"
            "<li><b>Gramapriya (ICAR-DPR, Hyderabad):</b> Layer-type rural crossbred producing 200&ndash;220 tinted brown eggs/year with low feed input; excellent camouflage plumage protecting from predatory birds.</li>"
            "<li><b>Giriraja (KVAFSU, Bengaluru):</b> Multi-colored broiler-cum-egg bird with rapid growth (2.0 kg at 10 weeks) and 130&ndash;150 eggs/year.</li>"
            "<li><b>Srinidhi, Cari-Nirbheek, Pratapdhan:</b> Adapted backyard crosses incorporating native germplasm (Aseel, Kadaknath) for broodiness, escape agility, and high market preference for pigmented meat and brown eggs.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "4-Way Cross breeding structure (GGP -> GP -> PS -> Commercial 4-way ABCD hybrid).",
            "Sire line selection (growth, breast yield, FCR) vs Dam line selection (egg numbers, fertility, hatchability).",
            "Auto-sexing genetics: Female heterogamety (ZW) exploited via Z-linked slow feathering (K/k) and Silver/Gold (S/s) crosses.",
            "Indian backyard poultry breeds: Vanaraja (DPR Hyderabad), Gramapriya, Giriraja (KVAFSU), Pratapdhan for rural livelihood."
        ],
        "diagram": "",
        "table": {
            "title": "Selection Trait Priorities in Commercial Layer vs Broiler Breeding Programs",
            "headers": ["Breeding Segment", "Primary Selection Traits", "Target Commercial Benchmark", "Genetic Architecture"],
            "rows": [
                ["Commercial Hybrid Layers", "Annual egg number (hen-housed), egg weight (58-62g), shell breaking strength, early sexual maturity (18-19 wks), feed efficiency per dozen eggs", "320 - 340 eggs per year; FCR 1.9 - 2.1 kg feed/kg egg mass", "Moderate to high h² for egg size; low h² for egg numbers (exploits heterosis)"],
                ["Commercial Hybrid Broilers", "Body weight at 35-42 days, feed conversion ratio (FCR), breast meat yield, livability, ascites/skeletal defect resistance", "2.2 - 2.5 kg at 35 days; FCR 1.45 - 1.55; breast yield >22%", "Moderate to high h² (0.30 - 0.45) for growth rate and body composition"],
                ["Layer Dam Line (Lines C & D)", "High peak egg production, persistency (>90% production across 40 weeks), low adult body weight (reduces maintenance feed cost)", "92% peak hatchability; low maintenance cost", "Negative genetic correlation between egg number and body weight handled via index"],
                ["Broiler Dam Line (Lines C & D)", "Hatching egg production, fertility, hatchability under skip-a-day feed restriction", "175 - 185 hatching eggs per hen housed", "Requires strict feed restriction during rearing to prevent obesity and ovarian disorders"]
            ]
        },
        "pyq": ["VCI Annual 2018", "TANUVAS 2019", "IVRI 2020", "GADVASU 2021", "KVASU 2022", "LUVAS 2023"]
    },
    {
        "id": "u3-q25",
        "type": "long",
        "marks": 12,
        "question": (
            "Describe the Modern Reproductive and Biotechnological Tools in Animal Breeding: Artificial Insemination (AI), "
            "Sex-Sorted Semen, Ovum Pick-Up and In Vitro Fertilization (OPU-IVF), and Genomic Selection. Compare Traditional "
            "Progeny Testing with Genomic Selection (GBLUP/ssGBLUP), explaining how Genomic Selection dramatically shortens "
            "the generation interval. Outline its implementation in Indian dairy breeds."
        ),
        "topicId": "u3-t26",
        "answer": (
            "<b>1. Advanced Reproductive Technologies in Animal Breeding:</b>"
            "<ul>"
            "<li><b>A. Artificial Insemination (AI) with Frozen Semen:</b> The foundational multiplier biotechnology. A single elite bull produces 40,000&ndash;60,000 semen doses annually (diluted in tris-egg yolk-glycerol extender and frozen at -196&deg;C in liquid nitrogen), enabling the widespread dissemination of proven genetic merit across millions of cows while preventing venereal disease transmission.</li>"
            "<li><b>B. Sex-Sorted Semen Technology:</b> Based on flow-cytometric cell sorting (Beltsville sperm sorting technology). Bovine X-chromosome bearing spermatozoa contain <b>3.8% more DNA</b> than Y-spermatozoa. Sperm are stained with fluorochrome Hoechst 33342, excited by UV laser, and sorted electrostatically at 90% accuracy into X-bearing or Y-bearing fractions. Insemination of heifers with X-sorted semen produces >90% female calves, revolutionizing heifer replacement and eliminating unwanted stray male calves.</li>"
            "<li><b>C. Ovum Pick-Up and In Vitro Fertilization (OPU-IVF):</b> Transvaginal ultrasound-guided aspiration of immature cumulus-oocyte complexes (COCs) from live donor ovaries, followed by in vitro maturation (IVM), in vitro fertilization (IVF) with sexed semen, and in vitro culture (IVC) to blastocyst stage (Day 7). Overcomes the limitations of MOET: can be performed twice weekly on pregnant cows and prepubertal heifers, yielding 50&ndash;100 embryos per cow annually without hormone depletion.</li>"
            "</ul><br>"
            "<b>2. Genomic Selection (Theo Meuwissen, Hayes & Goddard, 2001):</b><br>"
            "A paradigm shift in animal breeding where <b>Genomic Estimated Breeding Values (GEBVs)</b> are calculated directly from genome-wide "
            "dense Single Nucleotide Polymorphism (SNP) markers spanning the entire livestock genome (e.g., Bovine 50K BeadChip).<br><br>"
            "<b>Operational Methodology:</b>"
            "<ol>"
            "<li><b>Reference Population:</b> A large cohort of thousands of historic sires and cows with both high-density SNP genotypes and verified phenotypic progeny records. Marker effects across all 50,000 SNPs are estimated simultaneously using Genomic BLUP (GBLUP) or Bayesian regression methods.</li>"
            "<li><b>Candidate Population (Calves):</b> Newborn calves are genotyped at birth using hair follicle or blood DNA.</li>"
            "<li><b>GEBV Prediction:</b> Calf's GEBV is calculated by summing the estimated allelic effects of all its inherited SNP alleles: <code>GEBV = &sum; (X<sub>i</sub> &times; &beta;^<sub>i</sub>)</code>.</li>"
            "</ol><br>"
            "<b>3. Traditional Progeny Testing vs. Genomic Selection:</b><br>"
            "The fundamental formula governing annual rate of genetic progress is Rendel and Robertson's equation:<br>"
            "<b><code>&Delta;G / year = (i &times; r<sub>AI</sub> &times; &sigma;<sub>A</sub>) / L</code></b><br>"
            "Genomic selection revolutionized this dynamic by drastically reducing the denominator <b>Generation Interval (L)</b> while maintaining high accuracy (<code>r<sub>AI</sub> &approx; 0.70&ndash;0.80</code>):"
            "<ul>"
            "<li>In traditional progeny testing, a dairy bull's breeding value can only be established after daughters complete their first 305-day lactation: <b>L = 5.5 to 6.0 years</b>.</li>"
            "<li>In genomic selection, GEBV is predicted with 75% accuracy <b>on the day the calf is born (L = 1.5 to 2.0 years)</b>. Semen collection begins at 12&ndash;14 months.</li>"
            "<li><b>Result:</b> Annual genetic progress (<code>&Delta;G/year</code>) <b>doubles (100% to 150% increase)</b> compared to traditional progeny testing, with massive savings in rearing costs for unselected candidate bulls.</li>"
            "</ul><br>"
            "<b>4. Genomic Selection Implementation in Indian Dairy Livestock:</b>"
            "<ul>"
            "<li><b>National Dairy Development Board (NDDB) & Rashtriya Gokul Mission (RGM):</b> Developed custom indigenous genomic chips (e.g., <b>INDUSCHIP</b>, a 55K SNP custom BeadChip optimized for zebu cattle, and <b>BUFFCHIP</b> optimized for water buffaloes).</li>"
            "<li><b>Single-Step GBLUP (ssGBLUP):</b> Integrates pedigree, genotypes, and phenotypes simultaneously using the <code>H-matrix</code> (combining relationship matrix <i>A</i> with genomic relationship matrix <i>G</i>), enabling accurate evaluation of non-genotyped smallholder cows alongside genotyped AI breeding bulls.</li>"
            "<li>Used to screen and select young indigenous Gir, Sahiwal, Kankrej, and Murrah bulls at 6 months of age for national semen stations.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "AI and Cryopreservation (-196°C) as foundation multiplier biotechnology.",
            "Sex-sorted semen: 3.8% DNA difference, flow-cytometry sorting (90% female calf accuracy).",
            "OPU-IVF: Twice-weekly ovum pickup from live donors, 50-100 embryos/yr.",
            "Genomic selection principle (Meuwissen et al. 2001): Reference population, SNP BeadChips, GEBV prediction.",
            "Mathematical comparison: Rendel-Robertson equation (ΔG/yr = i * r * σ_A / L); L reduced from 5.5 yrs to 1.5 yrs, doubling genetic gain.",
            "Indian implementation: INDUSCHIP (zebu) and BUFFCHIP (buffalo) under NDDB/RGM with single-step GBLUP (H-matrix)."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Comparison Between Traditional Progeny Testing and Genomic Selection",
            "headers": ["Feature", "Traditional Progeny Testing (PT)", "Genomic Selection (GS / ssGBLUP)"],
            "rows": [
                ["Age at Final Genetic Evaluation", "5.5 - 6.0 years (requires waiting for daughter lactation)", "At birth (1 - 2 weeks of age from blood/hair DNA)"],
                ["Generation Interval (L)", "Sire-to-son interval is 5.5 - 6.5 years", "Sire-to-son interval reduced to 1.5 - 2.0 years (70% reduction)"],
                ["Accuracy of Breeding Value (r_AI)", "0.85 - 0.90 (with 50 - 80 recorded daughters)", "0.70 - 0.80 at birth (based on dense SNP markers)"],
                ["Annual Genetic Gain (ΔG/year)", "Standard baseline (1.0x)", "Doubled (2.0x to 2.5x standard rate due to dramatic L reduction)"],
                ["Bull Maintenance Cost", "Enormous; hundreds of unproven bulls housed for 5+ years awaiting daughter records", "Very low; only top genomically ranked young calves are retained"],
                ["Evaluation of Traits Hard to Measure", "Difficult and costly for health, fertility, feed efficiency, and longevity", "Highly effective; reference population records allow GEBV prediction for all recorded traits"],
                ["Indian Tool / Implementation", "Field Progeny Testing (FPT) under NDP", "INDUSCHIP (Cattle) & BUFFCHIP (Buffalo) via NDDB/INAPH ssGBLUP"]
            ]
        },
        "pyq": ["VCI Annual 2019", "TANUVAS 2020", "IVRI 2021", "GADVASU 2022", "KVASU 2023"]
    }
]
