# -*- coding: utf-8 -*-
"""
Unit 3 - Part 3: Topics u3-t15 to u3-t21
Principles of Animal Breeding (IVRI Undergrad 10 CGPA Standard)
"""

topics = {}

topics["u3-t15"] = {
    "summary": "Breeding strategies for small ruminants and swine optimize functional economic traits: fine/carpet wool and mutton prolificacy (FecB gene) in sheep, milk/meat/pashmina in goats, and litter size with feed efficiency in commercial crossbred swine.",
    "desc": (
        "<b>I. BREEDING STRATEGIES FOR SHEEP (OVINE)</b><br>"
        "Sheep in India (~74 million) are raised under extensive pastoralist transhumance systems across four agro-ecological zones:"
        "<ul>"
        "<li><b>Classification of Indian Sheep Breeds by Utility:</b>"
        "<br>&bull; <i>Apparel / Fine Wool:</i> Kashmir Merino, Gaddi, Nilgiri, Karnah."
        "<br>&bull; <i>Carpet Wool:</i> <b>Chokla</b> ('Merino of Rajasthan', produces world-class carpet wool), Magra, Nali, Marwari, Pugal, Jaisalmeri."
        "<br>&bull; <i>Mutton / Meat Breeds:</i> <b>Nellore</b> (tallest Indian sheep, Andhra Pradesh), Mandya (compact meaty conformation, Karnataka), Deccani, Madras Red, Mecheri."
        "<br>&bull; <i>Prolific Breeds:</i> <b>Garole</b> (Sundarbans, West Bengal; carries the fecundity gene <code>FecB</code> for twin/triplet births).</li>"
        "<li><b>Breeding Policies & Strategies:</b>"
        "<br>1. <b>Fine Wool Production:</b> Crossbreeding indigenous coarse-wool ewes with exotic fine-wool sires (Rambouillet and Soviet Merino) up to 50–75% inheritance (e.g., development of <b>Bharat Merino</b> and <b>Kashmir Merino</b>). In native fine-wool tracts (Kashmir valley), selective breeding is practiced."
        "<br>2. <b>Carpet Wool Production:</b> <b>Rigorous Selective Breeding within pure breeds</b> (Chokla, Magra, Nali) for greasy fleece yield, staple length, and medullation percentage (optimal medullation for carpet wool: 25–35%). Crossbreeding with exotic fine wool is strictly avoided as it renders wool too fine for durable carpets."
        "<br>3. <b>Mutton Production:</b> Selective breeding within indigenous mutton breeds (Nellore, Mandya) for 6-month and 9-month body weight, feed conversion efficiency, and dressing percentage (> 50%). Crossing with exotic mutton breeds (Suffolk, Dorset) produced fast-growing lambs for intensive feedlots."
        "<br>4. <b>Prolificacy Introgression (The Avishaan Breakthrough):</b> CSWRI Avikanagar introgressed the <code>FecB</code> (Booroola) mutation from tiny Garole sheep into Malpura mutton sheep, synthesizing the celebrated <b>Avishaan</b> prolific sheep strain (twinning rate elevated to 40–50%).</li>"
        "</ul><br>"
        "<b>II. BREEDING STRATEGIES FOR GOATS (CAPRINE — 'POOR MAN'S COW')</b><br>"
        "Goats (~148 million in India) provide critical rural food security, requiring targeted regional breeding programs:"
        "<ul>"
        "<li><b>Functional Breed Classes:</b>"
        "<br>&bull; <i>Dairy:</i> <b>Jamunapari</b> (majestic roman nose, long pendulous ears, yield 2.5–3.5 kg/day), <b>Beetal</b> (Punjab; prime dairy goat used as improver buck), Barbari (compact urban stall-fed dairy goat), Surti, Jakhrana."
        "<br>&bull; <i>Meat (Chevon):</i> <b>Black Bengal</b> (celebrated worldwide for unmatched prolificacy: 80% twinning/triplets, early sexual maturity at 6–8 months, premium tender meat, and supreme Export-quality 'Kidd' leather), Osmanabadi, Sirohi, Malabari (Tellicherry)."
        "<br>&bull; <i>Pashmina / Cashmere:</i> <b>Changthangi</b> (Ladakh, 4,000+ meters altitude) and <b>Chegu</b> (Himachal Pradesh) produce ultra-fine undercoat fiber (< 15 microns diameter) during freezing winters.</li>"
        "<li><b>Breeding Policy:</b>"
        "<br>&bull; <b>Pure Breeding and Selective Breeding</b> within well-defined native breeds. Commercial crossbreeding with exotic dairy goats (Saanen, Alpine) or meat goats (Boer) has yielded limited success in smallholder systems due to feed scarcity and heat stress."
        "<br>&bull; <b>Grading Up</b> of non-descript scrub goats using superior pedigreed bucks of Beetal, Sirohi, or Barbari breeds."
        "<br>&bull; Selection criteria: 90-day milk yield in dairy breeds; 6-month body weight and kidding rate (twins/triplets per year) in meat breeds.</li>"
        "</ul><br>"
        "<b>III. BREEDING STRATEGIES FOR SWINE (PORCINE)</b><br>"
        "Swine possess the highest fecundity (litter size 8–12), shortest generation interval (1 year), and highest feed conversion efficiency among livestock:"
        "<ul>"
        "<li><b>Breeding Policy:</b>"
        "<br>1. <b>Selective Breeding in Indigenous Pigs:</b> Indigenous breeds (Ghungroo of West Bengal, Niang Megha of Meghalaya, Doom of Assam, Tenyi Vo of Nagaland) selected for disease resistance, scavenging capacity, and maternal mothering ability."
        "<br>2. <b>Crossbreeding of Non-descript Scrub Sows with Exotic Boars:</b> Exotic breeds used: <b>Large White Yorkshire (LWY)</b>, <b>Landrace</b>, <b>Duroc</b>, and <b>Hampshire</b>."
        "<br>&bull; Maintaining <b>50% to 75% exotic inheritance</b> produces superior commercial pigs combining tropical disease tolerance with rapid growth (reaching 80–90 kg at 8 months vs 30–40 kg in desi pigs)."
        "<br>&bull; Examples of ICAR synthesized crossbred pig varieties: <b>Jharsuk</b> (75% LWY + 25% Desi; BAU Ranchi), <b>Rani</b> and <b>Asha</b> (ICAR-NRC on Pig, Guwahati).</li>"
        "<li><b>Selection Index for Swine:</b> <code>I = b1(Litter size at birth) + b2(Litter weight at weaning) + b3(Post-weaning daily gain) - b4(Backfat thickness)</code>.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Molecular Genetics of Prolificacy & Carcass Quality:</b><br>"
        "To achieve maximum marks in advanced examinations, detail the specific major genes:"
        "<ul>"
        "<li><b>The FecB (Booroola) Mutation in Sheep:</b> Point mutation (A746G transition resulting in Q249R amino acid substitution) in the <b>BMPR1B (Bone Morphogenetic Protein Receptor Type 1B)</b> gene on chromosome 6. Each copy of the mutant <code>FecB^B</code> allele advances granulosa cell differentiation, maturing smaller ovarian follicles precociously and adding <b>0.8 to 1.5 extra ovulations</b> per estrus, transforming single-bearing sheep into twin-bearing ewes.</li>"
        "<li><b>The Halothane (Hal / RYR1) Gene in Swine:</b> Mutation (C1843T in Ryanodine Receptor 1 gene) causes <b>Porcine Stress Syndrome (PSS)</b> and Pale, Soft, Exudative (PSE) pork. Sires must be tested via PCR-RFLP to guarantee homozygosity for the normal halothane-negative allele (<code>NN</code>).</li>"
        "<li><b>IGF2 Intron 3 Mutation in Pigs:</b> A single base substitution (G3072A) in an evolutionary conserved repressor motif of <i>IGF2</i> upregulates postnatal skeletal muscle growth, increasing lean meat percentage by 3–4%.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Chokla sheep of Rajasthan produces the finest carpet wool in India with optimal 25–35% medullation.",
        "Nellore is the tallest Indian sheep breed, selected primarily for mutton conformation and growth.",
        "The Garole sheep of Sundarbans carries the FecB (Booroola) mutation on BMPR1B for high prolificacy.",
        "Avishaan is a three-breed synthetic sheep (Garole x Malpura x Patanwadi) exhibiting 40–50% twinning rate.",
        "Bharat Merino was developed at CSWRI Avikanagar by crossing indigenous ewes with Rambouillet/Merino.",
        "Jamunapari and Beetal are premier Indian dairy goat breeds; Beetal is widely used as an improver buck.",
        "Black Bengal goat is globally celebrated for high prolificacy (twinning/triplets) and premium 'Kidd' leather.",
        "Changthangi and Chegu goats of high Himalayas produce luxury undercoat fiber called Pashmina (< 15 microns).",
        "Swine have the shortest generation interval and highest fecundity among farm livestock.",
        "Crossbreeding indigenous sows with Large White Yorkshire (50-75% exotic) synthesizes fast-growing meat pigs.",
        "Porcine Stress Syndrome (PSS) causing PSE pork is linked to the Ryanodine Receptor (RYR1) halothane gene."
    ],
    "tables": [
        {
            "title": "Breeding Priorities and Improver Breeds for Small Ruminants and Swine in India",
            "headers": ["Species / Sector", "Target Product / Trait", "Premier Indigenous Breeds", "Improver / Exotic Germplasm", "Key Selection Criteria"],
            "rows": [
                ["Sheep (Fine Wool)", "Apparel wool (< 22 microns)", "Kashmir Merino, Gaddi, Nilgiri", "Rambouillet, Soviet Merino", "Clean fleece weight, low fiber diameter (< 21 &mu;m)"],
                ["Sheep (Carpet Wool)", "Durable carpet fleece", "Chokla, Magra, Nali, Pugal", "Pure indigenous selection (No exotics)", "Greasy fleece yield, staple length, medullation (25-35%)"],
                ["Sheep (Mutton)", "Chevon-like lamb meat", "Nellore, Mandya, Deccani, Mecheri", "Dorset, Suffolk (terminal feedlot)", "6-month body weight (> 20 kg), dressing percentage (> 50%)"],
                ["Goat (Dairy)", "Lactation milk yield", "Jamunapari, Beetal, Barbari, Jakhrana", "Pure indigenous selective breeding", "90-day milk yield (> 150 kg), lactation length, udder shape"],
                ["Goat (Meat)", "Kidding rate & chevon", "Black Bengal, Osmanabadi, Sirohi", "Selective breeding / grading up", "Litter size at birth (twins/triplets), 6-month growth rate"],
                ["Goat (Pashmina)", "Luxury warm undercoat", "Changthangi (Ladakh), Chegu (HP)", "Strict native preservation in cold deserts", "Fiber fineness (< 14.5 &mu;m), down fiber yield per clip"],
                ["Swine (Pork)", "Lean meat & litter size", "Ghungroo, Niang Megha, Desi scrub", "Large White Yorkshire, Landrace, Duroc", "Litter size at birth (> 10), 8-month weight (> 80 kg), low backfat"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In field sheep development projects, introducing purebred exotic rams (Merino/Rambouillet) directly into hot, arid, thorn-scrub rangelands "
        "often results in fatal pneumonia, solar dermatitis, and starvation due to inability to graze rough xerophytic vegetation. "
        "Field veterinarians must recommend the use of <b>hardy 50% crossbred rams (e.g., Avikalin / Bharat Merino rams)</b> or utilize <b>Pedigreed Superior Chokla Rams</b>, "
        "ensuring environmental resilience is maintained while boosting flock fleece weight by 35–50%."
    ),
    "tags": ["Sheep Breeding", "Goat Breeding", "Swine Breeding", "Chokla", "Black Bengal", "FecB", "Avishaan", "Pashmina", "LWY"]
}

topics["u3-t16"] = {
    "summary": "Commercial poultry breeding utilizes specialized female and male lines evaluated via multi-trait selection indexes and Reciprocal Recurrent Selection to produce standardized four-way cross commercial broilers and layers.",
    "desc": (
        "<b>STRUCTURE OF THE MODERN COMMERCIAL POULTRY INDUSTRY</b><br>"
        "The poultry industry is the most genetically sophisticated and vertically integrated livestock sector in the world. "
        "It is organized as a strict genetic pyramid with four tiers:"
        "<ol>"
        "<li><b>Primary Breeding Nucleus (Pedigree Lines):</b> Elite pure lines (Lines A, B, C, D) maintained under ultra-strict biosecurity with individual electronic tracking.</li>"
        "<li><b>Great-Grandparents (GGP):</b> Multiplication of pure lines.</li>"
        "<li><b>Grandparents (GP):</b> Crosses between pure lines within line types (e.g., Male Line A &times; B &rarr; Sire Parent; Female Line C &times; D &rarr; Dam Parent).</li>"
        "<li><b>Parent Stock (PS):</b> Crossbred parents (AB males &times; CD females) maintained by commercial hatcheries to produce <b>Four-Way Cross Commercial Chicks (ABCD)</b> sold to farmers.</li>"
        "</ol><br>"
        "<b>I. BREEDING STRATEGY FOR COMMERCIAL EGG LAYERS</b><br>"
        "Commercial layers are bred for maximum production of clean, marketable eggs with minimum feed consumption:"
        "<ul>"
        "<li><b>White Egg Layers:</b> Derived almost exclusively from specialized inbred lines and strains of <b>Single Comb White Leghorn (SCWL)</b>."
        "<br>&bull; <i>Examples of International / Indian Commercial Hybrids:</i> BV-300 (Venkateshwara Hatcheries), Babcock-300, Hy-Line W-36, Bovans White, HH-260."
        "<br>&bull; <i>Performance Benchmarks:</i> 320–335 eggs per hen housed up to 72 weeks; feed conversion 1.30–1.38 kg feed per dozen eggs; adult body weight 1.4–1.6 kg.</li>"
        "<li><b>Brown Egg Layers:</b> Developed by crossing <b>Rhode Island Red (RIR)</b>, <b>New Hampshire</b>, and <b>Australorp</b> lines with barred or silver lines."
        "<br>&bull; Allows <b>Auto-sexing at Hatch:</b> Day-old chicks can be sexed visually by down plumage color (e.g., gold/brown females vs silver/white males) or feathering speed (slow vs rapid feathering alleles <code>K/k+</code>).</li>"
        "<li><b>Key Selection Traits in Layer Lines:</b>"
        "<br>&bull; Hen-housed egg production to 64/72 weeks (h&sup2; = 0.15–0.25)."
        "<br>&bull; Age at first egg / sexual maturity (optimal: 18–20 weeks; h&sup2; = 0.35–0.45)."
        "<br>&bull; Average egg weight (target: 54–58 g; h&sup2; = 0.50–0.60)."
        "<br>&bull; Egg shell quality (breaking strength > 3.5 kg/cm&sup2;, shell thickness > 0.35 mm to minimize breakage)."
        "<br>&bull; Internal egg quality (Haugh units > 75, absence of blood/meat spots)."
        "<br>&bull; Feed conversion ratio (FCR: kg feed per kg egg mass)."
        "<br>&bull; Docility and absence of cannibalism / feather pecking.</li>"
        "</ul><br>"
        "<b>II. BREEDING STRATEGY FOR COMMERCIAL BROILERS (MEAT TYPE)</b><br>"
        "Broilers are juvenile chickens of either sex grown strictly for rapid muscular meat deposition:"
        "<ul>"
        "<li><b>Line Specialization in Broiler Hybrids:</b>"
        "<br>&bull; <b>Male (Sire) Lines:</b> Developed from <b>White Cornish</b> (Indian Game). Selected intensely for juvenile body weight, broad chest angle, massive breast muscle yield, strong legs/skeletal integrity, and low feed conversion ratio."
        "<br>&bull; <b>Female (Dam) Lines:</b> Developed from <b>White Plymouth Rock</b> (or synthetic synthetic lines). Selected for high egg production, fertility, and hatchability (to produce cheap day-old broiler chicks in volume) while maintaining adequate growth rate.</li>"
        "<li><b>Commercial Broiler Benchmarks (at 35–42 days of age):</b>"
        "<br>&bull; Live body weight: <b>2.2 to 2.6 kg</b>."
        "<br>&bull; Feed Conversion Ratio (FCR): <b>1.45 to 1.55</b>."
        "<br>&bull; Dressing percentage: <b>72–75%</b> (with breast meat yield > 24%)."
        "<br>&bull; Mortality / Livability: &ge; 97%."
        "<br>&bull; <i>Leading Global / Indian Strains:</i> Cobb-500, Ross-308, Hubbard, Vencobb-400.</li>"
        "</ul><br>"
        "<b>III. RURAL / BACKYARD POULTRY BREEDING STRATEGIES IN INDIA</b><br>"
        "Commercial hybrids perish under harsh village scavenging conditions. Indian agricultural research institutes (ICAR-DPR, ICAR-CARI) developed specialized <b>Dual-Purpose Rural Varieties</b>:"
        "<ul>"
        "<li><b>Key Desired Rural Traits:</b> Multi-colored camouflage plumage (evades predatory hawks/dogs), long shanks, scavenging ability, disease hardiness, agility, laying tinted/brown eggs (fetches premium price in village markets).</li>"
        "<li><b>Celebrated ICAR Rural Varieties:</b>"
        "<br>&bull; <b>Vanaraja</b> (ICAR-DPR Hyderabad): Dual-purpose bird for rural scavenging; males reach 1.8 kg at 12 weeks; females lay 100–110 brown eggs/year."
        "<br>&bull; <b>Gramapriya</b> (ICAR-DPR Hyderabad): Rural layer bird; lays 200–220 brown eggs/year with high livability."
        "<br>&bull; <b>CARI-Nirbheek</b> (ICAR-CARI Izatnagar): Cross of indigenous fierce fighting cock <b>Aseel</b> with exotic White Leghorn; highly prized for majestic aggressiveness, predator evasion, and tasty meat."
        "<br>&bull; <b>Giriraja</b> and <b>Swarnadhara</b> (KVAFSU, Bengaluru); <b>Kuroiler</b> (commercial dual-purpose scavenger).</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>The Broiler Breeder Paradox & Autosexing Genetics:</b><br>"
        "In university exams, elaborate on these two critical advanced concepts:"
        "<ul>"
        "<li><b>The Broiler Breeder Paradox:</b> Intense selection for rapid juvenile growth and voracious appetite results in severe obesity, low libido in roosters, erratic double ovulations, follicular atresia, and dismal hatchability in adult broiler parent stock! "
        "Breeding companies overcome this by: (a) Selecting dam lines with higher reproductive threshold, and (b) Enforcing rigorous <b>Quantitative Feed Restriction (Skip-a-Day Feeding)</b> during the rearing period (6 to 20 weeks) to keep broiler parent breeders lean and reproductively fertile.</li>"
        "<li><b>Molecular Feather-Sexing System:</b> Uses sex-linked late feathering allele <code>K</code> vs rapid feathering allele <code>k+</code> on the Z chromosome:"
        "<br>&bull; Cross: Rapid-feathering sire (<code>Z^{k+} Z^{k+}</code>) &times; Late-feathering dam (<code>Z^K W</code>)."
        "<br>&bull; Female progeny receive <code>Z^{k+}</code> from sire and <code>W</code> from dam &rarr; <b>Rapid feathering females</b> (primary wing coverts shorter than primary flight feathers at day 1)."
        "<br>&bull; Male progeny receive <code>Z^K</code> from dam and <code>Z^{k+}</code> from sire &rarr; <b>Late feathering males</b> (covert feathers as long as or longer than flight feathers)."
        "<br>&bull; Enables non-vent, 100% accurate visual sorting of thousands of day-old chicks per hour!</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Poultry breeding is structured as a 4-tier genetic pyramid: Pedigree -> GGP -> GP -> Commercial Parents.",
        "Commercial layers and broilers are four-way crosses (ABCD) exploiting specific combining ability.",
        "White egg layers are derived from Single Comb White Leghorn (SCWL) purelines (e.g., BV-300, Babcock-300).",
        "Commercial layers produce 320-335 eggs per year with an FCR of 1.30-1.38 kg feed per dozen eggs.",
        "Commercial broilers are produced by crossing White Cornish (sire line) with White Plymouth Rock (dam line).",
        "Broilers achieve 2.2-2.5 kg live weight in 35-40 days with an FCR of 1.45-1.55.",
        "Auto-sexing at hatch is achieved using sex-linked genes: plumage color (gold/silver) or feathering speed (K/k+).",
        "Skip-a-day feed restriction is mandatory in broiler parent stock to prevent obesity and reproductive failure.",
        "Vanaraja (meat+egg) and Gramapriya (egg) are premier rural poultry varieties developed by ICAR-DPR.",
        "CARI-Nirbheek incorporates indigenous Aseel germplasm for camouflage, agility, and predator defense.",
        "Reciprocal Recurrent Selection (RRS) is the standard selection design used to improve commercial hybrid vigor."
    ],
    "tables": [
        {
            "title": "Comprehensive Contrast Between Commercial Layer, Broiler, and Rural Poultry Lines",
            "headers": ["Parameter / Feature", "Commercial White Layer", "Commercial Broiler", "Rural Backyard Variety (e.g., Vanaraja)"],
            "rows": [
                ["Foundation Breeds", "Single Comb White Leghorn (pure strains)", "White Cornish (Sire) x White Plymouth Rock (Dam)", "Indigenous (Aseel/Desi) x Exotic Dual-Purpose (RIR/Australorp)"],
                ["Primary Product", "Table eggs (white shelled)", "Tender juvenile meat (broiler carcass)", "Dual purpose (scavenged meat + brown eggs)"],
                ["Market Age / Target", "72–80 weeks of continuous production", "35 to 42 days of age", "10–12 weeks for meat (1.8 kg); 72 weeks for eggs"],
                ["Performance Output", "320–335 eggs per hen housed", "2.2 to 2.6 kg live body weight", "100–110 tinted eggs/yr; 1.8 kg cockerel weight"],
                ["Feed Conversion (FCR)", "1.30–1.35 kg feed / dozen eggs", "1.45–1.55 kg feed / kg live gain", "Thrives on household waste, insects, and weed seeds"],
                ["Management System", "Intensive environmentally controlled cage/aviary", "Intensive deep litter / environmentally controlled houses", "Free-range backyard scavenging with night shelter"],
                ["Predator Defense", "Zero defense; highly flighty and vulnerable", "Zero defense; heavy muscular build", "High alertness, fast runner, flight ability, camouflage plumage"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "Veterinarians advising commercial broiler farms frequently manage metabolic diseases triggered by extreme genetic selection for rapid growth: "
        "<b>Ascites Syndrome (Water Belly)</b> due to pulmonary hypertension when massive pectoral muscles outgrow cardio-respiratory capacity, and "
        "<b>Sudden Death Syndrome (Flip-Over Disease)</b>. "
        "Management solutions include strict lighting control programs (providing 4–6 hours of darkness in weeks 2 and 3 to moderate early growth rate) "
        "and physical feed mashing/pelleting adjustments to relieve metabolic stress on the juvenile heart."
    ),
    "tags": ["Poultry Breeding", "Commercial Layers", "Commercial Broilers", "White Leghorn", "White Cornish", "Vanaraja", "Auto-sexing", "Ascites"]
}

topics["u3-t17"] = {
    "summary": "Sire evaluation identifies bulls of superior genetic merit for sex-limited dairy traits, progressing from historical Contemporary Comparison to modern Best Linear Unbiased Prediction (BLUP) using Henderson's mixed models.",
    "desc": (
        "<b>IMPORTANCE OF SIRE EVALUATION IN DAIRY BREEDING</b><br>"
        "In dairy cattle and buffalo improvement, <b>over 80% of total genetic progress</b> achieved across a population is directly attributable to sire selection. "
        "This disproportionate impact arises because: (a) Selection intensity is enormously higher in males (1 bull mates with tens of thousands of cows via AI), and "
        "(b) Milk production and reproductive traits are <b>sex-limited</b>: bulls carry and transmit the genes for lactation yield but never express the phenotype themselves. "
        "Consequently, sires must be evaluated through the milk production performance of their female relatives, primarily their daughters (<b>Progeny Testing</b>).<br><br>"
        "<b>HISTORICAL METHODS OF SIRE EVALUATION</b><br>"
        "<ol>"
        "<li><b>Simple Daughter Average:</b>"
        "<br>&bull; <code>Index = Daughter Mean (\bar{D})</code>"
        "<br>&bull; <i>Fatal Flaw:</i> Completely ignores the genetic contribution of the dams to which the bull was mated, as well as the environmental/management level of the herd.</li>"
        "<li><b>Daughter-Dam Comparison (Intermediate Index / Mount Hope Index):</b>"
        "<br>&bull; Proposed by Hansson (1913) and Yapp (1925): assumes daughter phenotype is the exact intermediate between sire's breeding value and dam's phenotype: <code>\bar{D} = (Sire BV + \bar{Dam}) / 2</code>."
        "<br>&bull; <code>Sire BV = 2\bar{D} - \bar{Dam}</code>"
        "<br>&bull; <i>Flaw:</i> Assumes identical environment for dams and daughters (violated by secular environmental improvements over time).</li>"
        "<li><b>Contemporary Comparison (CC Method — Robertson and Rendel, 1954):</b>"
        "<br>&bull; Compares the first-lactation milk yield of a sire's daughters with <b>contemporaries</b> (first-lactation daughters of other sires that calved in the <i>same herd, same year, and same season</i>)."
        "<br>&bull; <i>Contemporary Difference (CD):</i> <code>d_i = \bar{Y}_i - \bar{C}_i</code> (Daughter mean minus Contemporary mean in herd <i>i</i>)."
        "<br>&bull; <i>Weighting Factor (n1 n2 / (n1 + n2)):</i> <code>w_i = (n1_i &times; n2_i) / (n1_i + n2_i)</code>, where <code>n1</code> is number of daughters and <code>n2</code> is number of contemporaries in herd <i>i</i>."
        "<br>&bull; Eliminates general herd environmental differences, but fails to adjust for the genetic merit of the contemporary sires.</li>"
        "<li><b>Herdmate Comparison (HMC):</b>"
        "<br>&bull; Compares daughters with all other cows (all parities, age-adjusted using mature equivalent factors) calving in the same herd-year-season."
        "<br>&bull; Provided larger contemporary groups in small herds, but suffered biases from non-random age adjustments.</li>"
        "</ol><br>"
        "<b>BEST LINEAR UNBIASED PREDICTION (BLUP)</b><br>"
        "Developed by <b>Charles Roy Henderson (1973)</b> at Cornell University, BLUP is universally recognized as the <b>gold-standard biometrical methodology</b> for sire evaluation and animal ranking worldwide.<br><br>"
        "<b>Properties of BLUP Estimates:</b>"
        "<ul>"
        "<li><b>Best:</b> Minimizes the prediction error variance <code>Var(\\hat{u} - u)</code>; maximizes correlation between true (u) and predicted (\\hat{u}) breeding values.</li>"
        "<li><b>Linear:</b> Predicted breeding values are linear functions of the observed phenotypic records (y).</li>"
        "<li><b>Unbiased:</b> The mathematical expectation of the prediction error is zero: <code>E(\\hat{u}) = E(u)</code>.</li>"
        "<li><b>Prediction:</b> Evaluates random genetic effects (breeding values) rather than fixed population parameters.</li>"
        "</ul><br>"
        "<b>Henderson's Linear Mixed Model Equation (MME):</b><br>"
        "<code>y = X&beta; + Zu + e</code><br>"
        "Where:"
        "<ul>"
        "<li><b>y:</b> Vector of observed phenotypic records (e.g., 305-day milk yields).</li>"
        "<li><b>&beta;:</b> Vector of unknown <b>fixed environmental effects</b> (e.g., Herd-Year-Season of calving, parity, age class).</li>"
        "<li><b>u:</b> Vector of unknown <b>random genetic additive effects</b> (Estimated Breeding Values, EBV).</li>"
        "<li><b>e:</b> Vector of random residual environmental errors.</li>"
        "<li><b>X, Z:</b> Known incidence design matrices connecting records (y) to fixed (&beta;) and random (u) effects.</li>"
        "</ul><br>"
        "<b>The Mixed Model Equations (MME) Solved Simultaneously:</b><br>"
        "<code>[ X'X &nbsp;&nbsp;&nbsp; X'Z ] [ \\hat{&beta;} ] &nbsp; = &nbsp; [ X'y ]</code><br>"
        "<code>[ Z'X &nbsp;&nbsp;&nbsp; Z'Z + A⁻¹&alpha; ] [ \\hat{u} ] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ Z'y ]</code><br>"
        "Where:"
        "<ul>"
        "<li><b>A⁻¹:</b> The inverse of the <b>Numerator Relationship Matrix</b> (Henderson's breakthrough rules allow rapid direct inversion of A directly from pedigree paths without inverting huge matrices!).</li>"
        "<li><b>&alpha;:</b> Variance ratio: <code>&alpha; = &sigma;&sup2;_e / &sigma;&sup2;_u = (1 - h&sup2;) / h&sup2;</code>.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Why BLUP Supercedes All Historical Methods (Exam Scoring Points):</b><br>"
        "In university exams, score full marks by listing the distinct theoretical advantages of BLUP over CC and HMC:"
        "<ol>"
        "<li><b>Simultaneous Estimation:</b> BLUP simultaneously estimates fixed environmental effects (&beta;) and predicts random genetic breeding values (u), avoiding two-step estimation bias.</li>"
        "<li><b>Incorporation of Pedigree Relationships (A⁻¹):</b> Utilizes all known ancestral, collateral (sib), and descendant relationships. A young bull with zero daughters can still receive a reliable BLUP breeding value based on his sire, dam, and half-sibs!</li>"
        "<li><b>Adjustment for Genetic Merit of Mates (Non-Random Mating):</b> If an elite sire was deliberately mated to the herd's best dams, BLUP cleanly separates and strips out the dam's genetic contribution.</li>"
        "<li><b>Adjustment for Genetic Competition (Merit of Contemporaries):</b> Automatically adjusts for whether a sire's daughters competed against daughters of mediocre bulls or daughters of international superstar sires.</li>"
        "<li><b>Accounts for Genetic Trends:</b> Removes bias caused by genetic progress over calendar time across decades.</li>"
        "<li><b>Corrects for Selective Culling:</b> Adjusts for early culling of low-producing daughters during first lactation.</li>"
        "</ol>"
    ),
    "keyPoints": [
        "Over 80% of genetic improvement in dairy cattle populations is driven by sire selection.",
        "Milk yield is sex-limited; bulls must be evaluated indirectly through daughter records (progeny testing).",
        "Daughter-Dam comparison (Yapp's Index: 2D - Dam) fails due to environmental changes between generations.",
        "Robertson and Rendel (1954) developed Contemporary Comparison (CC) to compare daughters with herdmates.",
        "CC uses weighting factor w = (n1 * n2) / (n1 + n2) based on daughter and contemporary group size.",
        "C.R. Henderson (1973) developed Best Linear Unbiased Prediction (BLUP) using Mixed Model Equations.",
        "BLUP is: Best (minimum variance), Linear (linear function of y), Unbiased (E[u] = u), Prediction (random EBV).",
        "Henderson's model equation: y = Xβ + Zu + e (β = fixed effects; u = random genetic breeding values).",
        "The coefficient matrix incorporates A⁻¹ (inverse of numerator relationship matrix) and α = (1 - h²) / h².",
        "Henderson established simple algorithm rules to compute A⁻¹ directly from pedigree without matrix inversion.",
        "BLUP adjusts simultaneously for: herd-year-season, genetic merit of mates, genetic trend, and merit of contemporaries."
    ],
    "tables": [
        {
            "title": "Historical Evolution of Dairy Sire Evaluation Methodologies",
            "headers": ["Method / Era", "Pioneering Proponent", "Information Utilized", "Primary Environmental Adjustment", "Major Limitations / Biases"],
            "rows": [
                ["Daughter Average (Pre-1920)", "Early cattle breeders", "Daughter records only", "None", "Severely biased by herd management level; ignores dam genetic merit"],
                ["Daughter-Dam Index (1925)", "Yapp, Hansson", "Daughters and Dams", "Dam deviation (2D - Dam)", "Assumes dams and daughters had identical environments; ignores contemporaries"],
                ["Contemporary Comparison (1954)", "Robertson & Rendel", "Daughters vs Contemporaries", "Herd-Year-Season contemporary average", "Fails to adjust for genetic merit of contemporary sires or non-random mates"],
                ["Herdmate Comparison (1960)", "USDA dairy scientists", "Daughters vs all herdmates", "Age-adjusted herdmate average", "Biased by inaccurate age adjustment factors and within-herd genetic trends"],
                ["Animal Model BLUP (1973-Present)", "C.R. Henderson", "Complete pedigree + all relatives", "Simultaneous Generalized Least Squares (MME)", "Gold standard; computationally demanding; requires comprehensive pedigree records"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In India's <b>National Dairy Plan (NDP-I)</b> and Rashtriya Gokul Mission, the National Dairy Development Board (NDDB) "
        "implements <b>Field Progeny Testing (FPT)</b> programs for Murrah buffaloes and Sahiwal/Mehsana cattle using Animal Model BLUP. "
        "A batch of 20–30 young test bulls is distributed across hundreds of smallholder village AI centers, inseminating thousands of registered village cows. "
        "Milk yields of daughters are recorded monthly by certified milk recorders. "
        "The BLUP software estimates the <b>Breeding Value (EBV)</b> with > 70% reliability, identifying top-ranked 'Proven Sires' whose semen is then frozen in millions of doses for nationwide genetic improvement."
    ),
    "tags": ["Sire Evaluation", "BLUP", "C.R. Henderson", "Contemporary Comparison", "Progeny Testing", "Mixed Model Equations", "Numerator Relationship Matrix"]
}

topics["u3-t18"] = {
    "summary": "Nucleus breeding systems structure populations hierarchically into nucleus, multiplier, and commercial tiers, contrasting closed nucleus systems with Open Nucleus Breeding Systems (ONBS) that permit two-way elite gene flow.",
    "desc": (
        "<b>CONCEPT OF NUCLEUS BREEDING SYSTEMS</b><br>"
        "Traditional progeny testing in dairy cattle is exceptionally slow (generation interval 6–7 years), costly, and difficult to manage in developing countries with small scattered herds. "
        "To overcome these bottlenecks, <b>Nucleus Breeding Systems (NBS)</b> concentrate superior elite seedstock into a central breeding station (the <b>Nucleus</b>) where intensive performance recording, artificial reproduction, and selection are conducted with utmost biometrical rigor.<br><br>"
        "<b>HIERARCHICAL TIERS IN NUCLEUS SYSTEMS</b><br>"
        "A typical livestock population is organized into three distinct tiers (Pyramid Structure):"
        "<ol>"
        "<li><b>The Nucleus Tier (Top 1–5%):</b> Elite animals subjected to intense recording and selection. Sires and dams of future generations are produced here.</li>"
        "<li><b>The Multiplier Tier (Intermediate 10–15%):</b> Multiplies breeding males, crossbred females, or elite semen straws received from the nucleus to generate commercial seedstock.</li>"
        "<li><b>The Commercial / Base Population Tier (Bottom 80–90%):</b> Production herds owned by farmers where commercial meat, milk, wool, or eggs are produced.</li>"
        "</ol><br>"
        "<b>I. CLOSED NUCLEUS BREEDING SYSTEM (CNBS)</b><br>"
        "<ul>"
        "<li><b>Structure:</b> Once the nucleus herd is established from initial foundation stock, <b>the herd is permanently closed to all external germplasm</b>.</li>"
        "<li><b>Gene Flow:</b> Strictly <b>one-way downward</b> (Nucleus &rarr; Multiplier &rarr; Commercial Base). No animals from the commercial base can ever enter the nucleus.</li>"
        "<li><b>Critical Disadvantages:</b>"
        "<br>&bull; <i>Rapid Accumulation of Inbreeding:</i> Small effective population size (Ne) in the closed nucleus causes inbreeding to build up rapidly: <code>&Delta;F = 1 / (2 Ne)</code>."
        "<br>&bull; <i>Genetic Drift & Loss of Variance:</i> Limits long-term genetic gain as favorable alleles can be lost by chance."
        "<br>&bull; <i>Ignores Base Population Genetic Gems:</i> Outstanding, exceptional cows appearing spontaneously in the millions of commercial base herds are completely locked out of the breeding program.</li>"
        "</ul><br>"
        "<b>II. OPEN NUCLEUS BREEDING SYSTEM (ONBS)</b><br>"
        "Introduced to eliminate the flaws of closed systems, ONBS incorporates a <b>two-way dynamic gene flow</b> between the nucleus and the commercial base herds:"
        "<ul>"
        "<li><b>Two-Way Gene Flow:</b>"
        "<br>&bull; <i>Downward Flow:</i> Superior nucleus sires (or their semen) are transferred down to multiplier and commercial base herds for routine breeding."
        "<br>&bull; <i>Upward Flow:</i> Top-performing exceptional females from the commercial base population are identified via field screening, purchased or leased, and <b>promoted upward into the nucleus</b> to replace inferior nucleus females!</li>"
        "<li><b>Proportion of Replacements:</b> Typically, <b>10% to 20% of female replacements</b> entering the nucleus each year originate from the commercial base herds.</li>"
        "<li><b>Major Advantages of ONBS:</b>"
        "<br>1. <b>Reduces Inbreeding Rate (&Delta;F):</b> Infusion of fresh unrelated germplasm from the base keeps inbreeding accumulation significantly lower than in closed systems."
        "<br>2. <b>Increases Selection Differential (&Delta;S):</b> Taps into the vast phenotypic diversity of millions of commercial animals, allowing much higher selection intensity."
        "<br>3. <b>Higher Annual Genetic Gain (&Delta;G):</b> Computer simulations prove ONBS achieves <b>10% to 15% greater annual genetic progress</b> than CNBS."
        "<br>4. <b>Overcomes Lack of Field Infrastructure:</b> Perfect for developing countries where comprehensive field milk recording is impossible across millions of smallholders. Only the central nucleus requires sophisticated recording!</li>"
        "</ul><br>"
        "<b>INTEGRATION OF MOET WITH ONBS (MOET-ONBS)</b><br>"
        "Combining <b>Multiple Ovulation and Embryo Transfer (MOET)</b> with ONBS accelerates genetic gains:"
        "<ul>"
        "<li><b>Juvenile MOET:</b> Elite heifer calves in the nucleus are superovulated and flushed at 8–10 months of age before puberty, transferring embryos into base surrogate recipients. Sires are selected on full-sib/half-sib performance, <b>halving the generation interval (L = 3.5 years vs 7 years)</b>!</li>"
        "<li><b>Adult MOET:</b> Sires and dams selected on their own first lactation record and full-sib family performance at 3.5 years of age.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Mathematical Modeling of Gene Flow in ONBS (James 1977 Model):</b><br>"
        "In university exams, explain John W. James's (1977) classic biometrical formulation for open nucleus systems:"
        "<ul>"
        "<li>Let <code>u_N</code> and <code>u_B</code> be the genetic levels of the Nucleus and Base tiers. At asymptotic equilibrium under constant selection:"
        "<br><code>u_N - u_B = L_B &times; &Delta;G</code> (where <code>L_B</code> is generation lag of base behind nucleus, typically 1.5 to 2.0 generations).</li>"
        "<li>Optimal migration rate (<code>p</code>) of base females into the nucleus depends on: (a) Ratio of nucleus size to base size, and (b) Accuracy of field testing in the base. "
        "When base herds have even moderate recording accuracy (r_TI &ge; 0.40), optimal replacement of nucleus females by base cows is <b>15% to 20%</b>, minimizing inbreeding coefficient: <code>&Delta;F_{ONBS} &approx; (1 - p)&sup2; &Delta;F_{CNBS}</code>.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Nucleus breeding systems concentrate elite seedstock into a centralized nucleus for intensive recording.",
        "The breeding pyramid consists of three tiers: Nucleus (1-5%), Multiplier (10-15%), and Commercial Base (80-90%).",
        "In Closed Nucleus Breeding Systems (CNBS), gene flow is strictly one-way downward (Nucleus to Base).",
        "CNBS suffers from rapid inbreeding accumulation (ΔF = 1 / 2Ne) and genetic drift.",
        "In Open Nucleus Breeding Systems (ONBS), gene flow is two-way: downward for sires and upward for elite dams.",
        "In ONBS, 10–20% of female replacements entering the nucleus are sourced from superior base commercial herds.",
        "ONBS generates 10–15% higher annual genetic gain (ΔG) than closed nucleus systems.",
        "ONBS drastically reduces inbreeding rate by continually infusing diverse genetic variants from the base.",
        "ONBS is the ideal breeding system for smallholder livestock systems in developing countries like India.",
        "Combining MOET with ONBS (MOET-ONBS) cuts the generation interval in dairy cattle from 6–7 years to 3.5 years.",
        "Juvenile MOET flushes prepubertal heifers, selecting parents entirely on sib and collateral pedigree records."
    ],
    "tables": [
        {
            "title": "Comprehensive Comparison Between Closed (CNBS) and Open Nucleus Breeding Systems (ONBS)",
            "headers": ["Parameter / Criterion", "Closed Nucleus Breeding System (CNBS)", "Open Nucleus Breeding System (ONBS)"],
            "rows": [
                ["Direction of Gene Flow", "Strictly one-way (Nucleus &rarr; Multiplier &rarr; Commercial)", "Two-way (Sires flow downward; elite base females flow upward)"],
                ["External Germplasm Entry", "Zero; completely barred after foundation", "Allowed; 10–20% top base females enter nucleus each generation"],
                ["Inbreeding Accumulation Rate (&Delta;F)", "High (confined to small nucleus Ne; risk of inbreeding depression)", "Low to moderate (diluted by elite base female introductions)"],
                ["Genetic Diversity / Effective Size", "Restricted; prone to random genetic drift", "Expansive; captures whole-population genetic variation"],
                ["Annual Genetic Gain (&Delta;G)", "Baseline rate", "10% to 15% higher than CNBS"],
                ["Screening of Base Population", "None; commercial animals ignored", "Continuous field milk recording / screening of superior rural animals"],
                ["Suitability for Indian Conditions", "Poor (risk of inbreeding in small government farms)", "Ideal (integrates progressive village dairy farmers into nucleus improvement)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "The <b>Patanwadi and Marwari Sheep Improvement Project</b> in Gujarat and Rajasthan operated successfully on the ONBS model. "
        "A central nucleus farm maintained at CSWRI Arid Region Campus maintains elite pedigreed rams. "
        "Field recording teams screen migratory pastoralist flocks (Maldharis/Raikas). "
        "Ewes yielding over 1.8 kg greasy fleece or demonstrating consistent twinning are purchased from pastoralists at a 30% premium and brought to the nucleus. "
        "In return, superior tested young rams from the nucleus are distributed back to pastoralists, resulting in a sustainable <b>symbiotic genetic cycle</b>."
    ),
    "tags": ["ONBS", "CNBS", "Nucleus Breeding", "Open Nucleus Breeding System", "MOET", "Gene Flow", "Genetic Lag", "Pyramid Structure"]
}

topics["u3-t19"] = {
    "summary": "Development and synthesis of new breeds and strains in livestock and poultry combines foundation crossbreeding, fixing optimal exotic inheritance, inter-se mating, and intense selection to create stable, productive genotypes.",
    "desc": (
        "<b>RATIONALE AND STEPS IN DEVELOPING SYNTHETIC BREEDS</b><br>"
        "A <b>Synthetic Breed (Composite Breed)</b> is a new, stable, true-breeding population synthesized by crossing two or more distinct established breeds, followed by inter-se mating and multi-generation directional selection for specific economic goals.<br><br>"
        "<b>Five Sequential Steps in Synthesizing a New Breed:</b>"
        "<ol>"
        "<li><b>Step 1: Choice of Foundation Parental Breeds:</b>"
        "<br>&bull; Selected for complementary genetic strengths (e.g., crossing a high-yielding exotic breed with a hardy, disease-tolerant indigenous Zebu breed).</li>"
        "<li><b>Step 2: Foundation Crossbreeding:</b>"
        "<br>&bull; Mating parental breeds to generate F1 crossbreds, followed by backcrossing or multiple-cross designs to achieve the <b>desired proportion of exotic vs indigenous inheritance</b> (typically 50% to 62.5% exotic).</li>"
        "<li><b>Step 3: Inter-se Mating (Mating Crossbreds to Crossbreds):</b>"
        "<br>&bull; Crossing F1 &times; F1, F2 &times; F2, or 5/8 &times; 5/8 crossbreds among themselves. "
        "<br>&bull; <i>Challenge:</i> Overcoming F2 recombination breakdown through large population size and pedigree control.</li>"
        "<li><b>Step 4: Intensive Directional Selection:</b>"
        "<br>&bull; Applying high selection intensity using Selection Indexes, BLUP sire evaluation, and progeny testing to continuously increase additive genetic merit for target economic traits.</li>"
        "<li><b>Step 5: Stabilization, Characterization, and Breed Registration:</b>"
        "<br>&bull; Practicing mild linebreeding to establish phenotypic uniformity, conformational distinctiveness, prepotency, and stable breed standards over 5 to 7 generations.</li>"
        "</ol><br>"
        "<b>CELEBRATED INDIAN SYNTHETIC LIVESTOCK BREEDS</b><br>"
        "<b>1. Dairy Cattle:</b>"
        "<ul>"
        "<li><b>Frieswal (3/8 Sahiwal + 5/8 Holstein-Friesian = 62.5% HF):</b>"
        "<br>&bull; <i>Developed by:</i> ICAR-Central Institute for Research on Cattle (CIRC), Meerut in collaboration with the Directorate of Military Farms."
        "<br>&bull; <i>Performance:</i> Mature 305-day lactation yield > <b>4,000 kg milk</b> with 4.0% fat; age at first calving 30–32 months; exceptional adaptability to Indian tropical climate.</li>"
        "<li><b>Karan Swiss:</b> Developed at ICAR-NDRI Karnal by crossing Brown Swiss sires with Sahiwal and Red Sindhi cows (inheritance: ~50% Brown Swiss). Mature lactation yield: ~3,500 kg.</li>"
        "<li><b>Karan Fries:</b> Developed at ICAR-NDRI Karnal by crossing Holstein-Friesian sires with Tharparkar cows (inheritance: 50% HF + 50% Tharparkar). Mature lactation yield: <b>3,800 to 4,200 kg</b>.</li>"
        "<li><b>Sunandini:</b> Synthesized in Kerala (KLDB) by crossing non-descript local cattle with Brown Swiss, Jersey, and HF (stabilized at ~50–60% exotic dairy inheritance).</li>"
        "</ul><br>"
        "<b>2. Sheep (Fine Wool, Dual Purpose & Prolific):</b>"
        "<ul>"
        "<li><b>Bharat Merino:</b> Developed at CSWRI Avikanagar (Rajasthan) by crossing indigenous Chokla and Nali ewes with Rambouillet and Soviet Merino rams (stabilized at <b>75% exotic fine wool inheritance</b>). Produces high-grade apparel fleece (< 21 microns, clean fleece yield > 2.5 kg).</li>"
        "<li><b>Avikalin:</b> Developed at CSWRI Avikanagar by crossing Rambouillet rams with Malpura coarse-wool ewes (50:50). Superior dual-purpose carpet/apparel sheep.</li>"
        "<li><b>Avishaan:</b> Synthesized at CSWRI Avikanagar by crossing <b>Malpura &times; Garole &times; Patanwadi</b>. Carries the <code>FecB</code> prolificacy gene, yielding 40–50% twin births and 60% higher meat output per ewe per year.</li>"
        "</ul><br>"
        "<b>3. Swine (Crossbred Synthetic Pigs):</b>"
        "<ul>"
        "<li><b>Jharsuk:</b> Developed at Birsa Agricultural University (BAU), Ranchi (75% Large White Yorkshire + 25% Indigenous Desi). Black-coated, hardy, reaches 80 kg at 8 months with litter size 8–10.</li>"
        "<li><b>Rani & Asha:</b> Developed at ICAR-NRC on Pig, Rani (Guwahati). Crossbreds of Hampshire/Ghungroo and LWY adapted to North-Eastern agro-climatic conditions.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Retention of Heterosis in Synthetic / Composite Breeds:</b><br>"
        "In university exams, contrast rotational crossing with synthetic breed development:"
        "<ul>"
        "<li>While rotational crossing requires keeping purebred sires of multiple breeds perpetually, a <b>Synthetic Breed acts as a single, self-contained purebred breed</b> once formed, mating like to like!</li>"
        "<li><b>Mathematical Retained Heterosis in a Composite Breed (Dickerson 1969 Model):</b><br>"
        "<code>RH = [ 1 - &Sigma; (p_i)&sup2; ] &times; 100</code> (where <code>p_i</code> is the genetic fraction contributed by breed <i>i</i>)."
        "<br>&bull; In a <b>2-breed 50:50 composite</b> (e.g., Karan Fries: 1/2 HF + 1/2 Tharparkar): <code>RH = [1 - (0.5&sup2; + 0.5&sup2;)] = [1 - 0.50] = 50.0%</code> retained heterosis forever!"
        "<br>&bull; In a <b>4-breed composite</b> (each 25%): <code>RH = [1 - 4(0.25&sup2;)] = [1 - 0.25] = 75.0%</code> retained heterosis permanently captured without any future crossbreeding!</li>"
        "</ul>"
    ),
    "keyPoints": [
        "A synthetic (composite) breed is formed by crossing two or more breeds followed by inter-se mating and selection.",
        "Steps in breed development: Foundation crossing -> Inter-se mating -> Directional selection -> Stabilization.",
        "Synthetic breeds retain permanent heterosis without needing to maintain separate purebred parental lines.",
        "Retained heterosis in a composite breed is calculated as RH = [ 1 - Σ (pi)² ] * 100.",
        "Frieswal is India's premier synthetic dairy cattle breed (62.5% HF + 37.5% Sahiwal), yielding > 4,000 kg milk.",
        "Frieswal was collaboratively developed by ICAR-CIRC Meerut and the Military Farm Directorate.",
        "Karan Fries (HF x Tharparkar) and Karan Swiss (Brown Swiss x Sahiwal) were developed at ICAR-NDRI Karnal.",
        "Sunandini is a composite dairy cattle breed developed in Kerala using Brown Swiss and Jersey crosses.",
        "Bharat Merino was synthesized at CSWRI Avikanagar with 75% exotic fine-wool inheritance (Rambouillet/Merino).",
        "Avishaan is a three-breed prolific sheep (Malpura x Garole x Patanwadi) carrying the FecB fecundity mutation.",
        "Jharsuk (75% LWY + 25% Desi) is a stabilized crossbred pig developed for tribal smallholders by BAU Ranchi."
    ],
    "tables": [
        {
            "title": "Celebrated Synthetic (Composite) Livestock Breeds Developed in India",
            "headers": ["Synthetic Breed", "Species", "Parental Genetic Composition", "Developing Institution", "Target Economic Productivity"],
            "rows": [
                ["Frieswal", "Dairy Cattle", "62.5% Holstein-Friesian + 37.5% Sahiwal", "ICAR-CIRC Meerut & Military Farms", "305-day milk yield > 4,000 kg, 4.0% fat, age at 1st calving ~30 mo"],
                ["Karan Fries", "Dairy Cattle", "50% Holstein-Friesian + 50% Tharparkar", "ICAR-NDRI Karnal", "Lactation yield 3,800–4,200 kg; excellent tropical heat tolerance"],
                ["Karan Swiss", "Dairy Cattle", "50% Brown Swiss + 50% Sahiwal/Red Sindhi", "ICAR-NDRI Karnal", "Lactation yield 3,300–3,600 kg; robust constitution"],
                ["Sunandini", "Dairy Cattle", "50–60% Brown Swiss/Jersey + Local non-descript", "Kerala Livestock Development Board (KLDB)", "Lactation yield 2,800–3,200 kg; adapted to high humidity"],
                ["Bharat Merino", "Sheep (Apparel Wool)", "75% Rambouillet/Soviet Merino + 25% Chokla/Nali", "ICAR-CSWRI Avikanagar", "Annual apparel fleece > 2.5 kg, fiber diameter < 20.5 &mu;m"],
                ["Avikalin", "Sheep (Dual Purpose)", "50% Rambouillet + 50% Malpura", "ICAR-CSWRI Avikanagar", "Carpet/apparel wool yield 2.0 kg + fast mutton growth"],
                ["Avishaan", "Sheep (Prolific Meat)", "Malpura x Garole x Patanwadi (FecB carrier)", "ICAR-CSWRI Avikanagar", "40–50% twin births; 60% higher lamb meat yield per ewe"],
                ["Jharsuk", "Swine (Pork)", "75% Large White Yorkshire + 25% Desi pig", "Birsa Agricultural University, Ranchi", "80 kg live weight at 8 months; litter size at birth ~9–10"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "When managing commercial herds of <b>Frieswal</b> or <b>Karan Fries</b> cattle, veterinarians must educate farm managers "
        "that these animals are <b>stabilized true-breeding synthetic populations</b>, NOT first-generation F1 crossbreds. "
        "Therefore, farmers should mate Frieswal cows to <b>proven, progeny-tested Frieswal bulls</b> (via frozen semen provided by CIRC Meerut), "
        "rather than mating them back to pure 100% Holstein-Friesian sires (which would push exotic inheritance beyond 81%, triggering severe heat prostration and reproductive failure)."
    ),
    "tags": ["Synthetic Breeds", "Breed Synthesis", "Frieswal", "Karan Fries", "Karan Swiss", "Bharat Merino", "Avishaan", "Jharsuk", "Retained Heterosis"]
}

topics["u3-t20"] = {
    "summary": "Livestock breeding policies in India are governed by national flagship missions including the Rashtriya Gokul Mission, National Dairy Plan, and ICAR-coordinated networks to conserve native germplasm while upgrading productivity.",
    "desc": (
        "<b>CONSTITUTIONAL AND INSTITUTIONAL FRAMEWORK</b><br>"
        "In India, 'Preservation, protection and improvement of stock and prevention of animal diseases' is a <b>State Subject</b> under Entry 15 of the State List (Seventh Schedule of the Indian Constitution). "
        "However, national policy coordination, guidelines, international germplasm import regulations, and flagship funding are spearheaded by the <b>Department of Animal Husbandry and Dairying (DAHD)</b>, Ministry of Fisheries, Animal Husbandry and Dairying, Government of India.<br><br>"
        "<b>THE NATIONAL LIVESTOCK BREEDING POLICY DIRECTIVES</b><br>"
        "The national breeding guidelines categorize bovine populations into three distinct streams:"
        "<ol>"
        "<li><b>Defined Indigenous Bovine Breeds (In Native Tracts):</b>"
        "<br>&bull; Strict mandate for <b>Selective Breeding within the pure breed</b>."
        "<br>&bull; Zero exotic crossbreeding permitted in defined native breeding tracts (e.g., Gir in Saurashtra, Sahiwal in Punjab/Rajasthan, Kankrej in Gujarat, Murrah in Haryana).</li>"
        "<li><b>Non-Descript / Scrub Cattle:</b>"
        "<br>&bull; Subjected to <b>Crossbreeding with Exotic Dairy Sires (Jersey or Holstein-Friesian)</b>."
        "<br>&bull; Exotic inheritance capped strictly between <b>50% and 62.5%</b>."
        "<br>&bull; Jersey is mandated for hilly, forested, tribal, and low-input rainfed zones; HF is restricted to irrigated commercial milk sheds with high fodder availability.</li>"
        "<li><b>Non-Descript / Scrub Buffaloes:</b>"
        "<br>&bull; Subjected to continuous <b>Grading Up with pure Murrah</b> semen (or Mehsana / Surti / Jaffarabadi in Western India).</li>"
        "</ol><br>"
        "<b>KEY NATIONAL BREEDING PROGRAMMES AND MISSIONS</b><br>"
        "<ul>"
        "<li><b>1. Rashtriya Gokul Mission (RGM):</b>"
        "<br>&bull; Launched in December 2014 under the National Programme for Bovine Breeding and Dairy Development (NPBBDD)."
        "<br>&bull; <i>Core Objectives:</i> (a) Development and conservation of indigenous bovine breeds, (b) Breed improvement via scientific selection to enhance milk productivity, (c) Upgrading non-descript cattle using elite indigenous germplasm."
        "<br>&bull; <i>Major Infrastructure Components:</i>"
        "<br>&nbsp;&nbsp;&bull; <b>Gokul Grams:</b> Integrated indigenous cattle breeding centers established in native breeding tracts."
        "<br>&nbsp;&nbsp;&bull; <b>National Kamdhenu Breeding Centres (NKBC):</b> Centers of Excellence for indigenous breeds established in Northern and Southern India (Kiratpur, MP and Chintaladevi, AP)."
        "<br>&nbsp;&nbsp;&bull; <b>Establishment of IVF / ETT Labs & Sex-Sorted Semen Facilities:</b> Subsidized production of sex-sorted semen (> 90% female calves) and multiplication of elite donors via IVF."
        "<br>&nbsp;&nbsp;&bull; <b>National Genomic Chip (INDUSCHIP & BUFCHIP):</b> Custom SNP chips designed by NBAGR/NDDB for early genomic selection of indigenous calves.</li>"
        "<li><b>2. National Dairy Plan Phase I (NDP-I):</b>"
        "<br>&bull; Multi-state project implemented by the National Dairy Development Board (NDDB) funded by the World Bank (2012–2019)."
        "<br>&bull; Implemented large-scale <b>Field Progeny Testing (FPT)</b> for Murrah, Mehsana, and Frieswal, and <b>Pedigree Selection (PS)</b> for Sahiwal, Gir, Tharparkar, and Rathi."
        "<br>&bull; Upgraded semen production stations into 'A' and 'B' accredited bio-secure standards.</li>"
        "<li><b>3. All India Coordinated Research Projects (AICRPs) of ICAR:</b>"
        "<br>&bull; <b>AICRP on Cattle (CIRC Meerut):</b> Monitored the synthesis and field testing of the Frieswal breed and indigenous breed improvement units."
        "<br>&bull; <b>Network Project on Buffalo Improvement (CIRB Hisar):</b> Evaluates Murrah, Nili-Ravi, Jaffarabadi, Surti, Bhadawari, Pandharpuri, and Swamp buffaloes."
        "<br>&bull; <b>AICRP on Sheep Breeding (CSWRI Avikanagar) & AICRP on Goat Improvement (CIRG Makhdoom):</b> Elite buck/ram distribution and participatory farmer-flock improvement."
        "<br>&bull; <b>AICRP on Poultry Breeding (DPR Hyderabad):</b> Rural poultry parent stock dissemination (Vanaraja, Gramapriya).</li>"
        "</ul><br>"
        "<b>ROLE OF ICAR-NBAGR IN BREED REGISTRATION</b><br>"
        "The <b>National Bureau of Animal Genetic Resources (NBAGR), Karnal (Haryana)</b> is the sole nodal agency mandated to officially register, characterize, and document all livestock and poultry breeds in India. "
        "Each newly recognized breed is assigned an official <b>Breed Accession Number</b> (e.g., <code>INDIA_CATTLE_...</code>), securing national sovereignty over indigenous animal genetic resources under the Convention on Biological Diversity (CBD)."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>INDUSCHIP & BUFCHIP: Indigenous Bovine Genomics:</b><br>"
        "In university exams, detail India's indigenous genomic breakthrough under RGM:"
        "<ul>"
        "<li>Western commercial SNP chips (Illumina BovineSNP50) were designed on taurine dairy cattle (<i>Bos taurus</i>) and exhibited high 'ascertainment bias' and low polymorphic call rates when used on Indian Zebu cattle (<i>Bos indicus</i>) and riverine buffaloes (<i>Bubalus bubalis</i>).</li>"
        "<li>To overcome this, NDDB and ICAR-NBAGR sequenced the whole genome of native cattle and buffaloes, developing: "
        "<br>&bull; <b>INDUSCHIP (medium density custom chip ~45,000 SNPs):</b> Optimized specifically for Indian native cattle (Gir, Sahiwal, Kankrej, Red Sindhi).</li>"
        "<br>&bull; <b>BUFCHIP:</b> The world's first specialized genomic chip for River Buffaloes.</li>"
        "<li>Allows estimation of <b>Genomic Estimated Breeding Values (GEBV)</b> at birth from a drop of blood or hair follicle, slashing generation interval and accelerating genetic progress by > 50%!</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Livestock improvement is a State Subject under Entry 15 of the Seventh Schedule of the Indian Constitution.",
        "National livestock breeding directives mandate pure selective breeding in native tracts of indigenous breeds.",
        "Exotic crossbreeding is restricted to non-descript cattle, capped at 50% to 62.5% exotic inheritance.",
        "Grading up with pure Murrah sires is the national policy for non-descript scrub buffaloes.",
        "Rashtriya Gokul Mission (RGM) was launched in December 2014 for indigenous bovine development.",
        "RGM established Gokul Grams and National Kamdhenu Breeding Centres (Kiratpur, MP & Chintaladevi, AP).",
        "RGM promotes sex-sorted semen technology (> 90% female calves) and indigenous genomic chips.",
        "INDUSCHIP and BUFCHIP are custom SNP chips developed for indigenous cattle and buffalo genomic selection.",
        "National Dairy Plan (NDP-I) implemented Field Progeny Testing and Pedigree Selection across major dairy breeds.",
        "ICAR-NBAGR Karnal is the sole national authority for officially registering new livestock and poultry breeds.",
        "Each registered breed receives a unique official National Accession Number securing sovereign rights."
    ],
    "tables": [
        {
            "title": "Summary of Key National Livestock Breeding Programs and Institutions in India",
            "headers": ["Programme / Institution", "Nodal Agency / Ministry", "Mandate & Target Species", "Flagship Interventions / Achievements"],
            "rows": [
                ["Rashtriya Gokul Mission (RGM)", "DAHD, Govt of India", "Indigenous Cattle and Buffaloes", "Gokul Grams, National Kamdhenu Centres, IVF labs, Sex-sorted semen, INDUSCHIP"],
                ["National Dairy Plan-I (NDP-I)", "NDDB (World Bank funded)", "Bovines (Cattle & Buffaloes)", "Field Progeny Testing (FPT), Pedigree Selection (PS), A-grade semen station accreditation"],
                ["ICAR-NBAGR Karnal", "ICAR (DARE)", "All Farm Livestock & Poultry", "Breed characterization, official registration, Accession number allocation, Gene Bank"],
                ["AICRP on Cattle", "ICAR-CIRC Meerut", "Crossbred & Indigenous Cattle", "Frieswal breed synthesis (62.5% HF + 37.5% Sahiwal), bull evaluation networks"],
                ["Network Project on Buffalo (NPBI)", "ICAR-CIRB Hisar", "Murrah & Regional Buffaloes", "Progeny testing of Murrah bulls, elite germplasm dissemination across 10 centers"],
                ["AICRP on Sheep Breeding", "ICAR-CSWRI Avikanagar", "Indigenous & Crossbred Sheep", "Bharat Merino, Avishaan prolific sheep, carpet wool genetic improvement"],
                ["AICRP on Poultry Breeding", "ICAR-DPR Hyderabad", "Commercial & Rural Poultry", "Development and dissemination of Vanaraja, Gramapriya, and Srinidhi chicken lines"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In field veterinary hospital practice, veterinarians are the primary executors of state breeding policies. "
        "When an owner of a registered purebred Sahiwal or Gir cow demands exotic Holstein-Friesian semen, "
        "the veterinarian must <b>refuse and counsel the owner</b> on national breeding policy regulations. "
        "Crossing a high-yielding indigenous cow with HF ruins the genetic purity of the indigenous nucleus tract, "
        "whereas inseminating her with <b>progeny-tested elite Sahiwal/Gir semen</b> maintains purebred registered pedigree status, "
        "secures high milk yield, and produces male calves eligible for procurement by state semen stations at premium prices."
    ),
    "tags": ["Breeding Policies", "Rashtriya Gokul Mission", "RGM", "NDP-I", "ICAR-NBAGR", "INDUSCHIP", "BUFCHIP", "National Kamdhenu Breeding Centre"]
}

topics["u3-t21"] = {
    "summary": "Conservation of Animal Genetic Resources (AnGR) protects unique indigenous livestock diversity against extinction through in-situ habitat conservation and ex-situ in-vivo/cryogenic gene banking under FAO guidelines.",
    "desc": (
        "<b>ANIMAL GENETIC RESOURCES (AnGR) AND THE NEED FOR CONSERVATION</b><br>"
        "<b>Animal Genetic Resources (AnGR)</b> encompass all avian and mammalian species used, or having potential for use, in food, agriculture, and draft power. "
        "India possesses unparalleled biodiversity, currently recognizing over <b>212 registered indigenous breeds</b> of cattle, buffaloes, sheep, goats, horses, camels, pigs, yaks, and poultry.<br><br>"
        "<b>Drivers of Genetic Erosion (Threats to Indigenous Breeds):</b>"
        "<ul>"
        "<li>Indiscriminate crossbreeding of native breeds with exotic stock leading to genetic dilution.</li>"
        "<li>Mechanization of agriculture reducing economic reliance on magnificent draft breeds (e.g., Amritmahal, Hallikar, Khillari, Kangayam).</li>"
        "<li>Loss of traditional grazing lands (common property resources / charagah) and shrinking pastoralist routes.</li>"
        "<li>Introduction of intensive mono-production systems favoring high-input commercial hybrids.</li>"
        "<li>Severe droughts, natural disasters, epidemics, and rural-urban migration of pastoral communities.</li>"
        "</ul><br>"
        "<b>UNIQUE ADAPTIVE QUALITIES OF INDIGENOUS BREEDS REQUIRING CONSERVATION</b><br>"
        "Indigenous breeds possess irreplaceable genetic complexes sculpted by centuries of natural and human selection:"
        "<ol>"
        "<li><b>Thermotolerance:</b> High density of sweat glands, larger surface area (dewlap/sheath), heat-shock protein gene expression (<code>HSP70</code>, <code>HSP90</code>).</li>"
        "<li><b>Disease & Parasite Resistance:</b> Innate resistance to tick-borne hemoprotozoan diseases (Tropical Theileriosis, Babesiosis, Anaplasmosis), foot-and-mouth disease (FMD), and gastrointestinal nematodes.</li>"
        "<li><b>Coarse Fodder Conversion:</b> Exceptional ability to survive and produce milk on high-lignin, low-nitrogen crop residues and withstand drought feed scarcity.</li>"
        "<li><b>A2 Beta-Casein Allele:</b> Almost 100% of indigenous Indian cattle carry the <code>A2</code> allele of beta-casein (proline at position 67), avoiding the inflammatory BCM-7 peptide associated with taurine A1 milk.</li>"
        "</ol><br>"
        "<b>FAO RISK CATEGORIES FOR LIVESTOCK POPULATIONS</b><br>"
        "Breeds are classified based on total breeding females: <b>Critical</b> (< 100 breeding females), <b>Endangered</b> (100 to 1,000 breeding females), <b>Vulnerable</b> (1,000 to 10,000 breeding females), and <b>Not at Risk</b> (> 10,000 females).<br><br>"
        "<b>I. IN-SITU CONSERVATION (ON-FARM / NATIVE HABITAT)</b><br>"
        "Conservation of livestock populations within their natural agricultural ecosystems and home breeding tracts where they developed their distinctive traits:"
        "<ul>"
        "<li><b>Practices:</b>"
        "<br>&bull; Maintenance of livestock by traditional pastoralist communities (Maldharis, Raikas, Kurubas, Bakarwals, Gujjars)."
        "<br>&bull; Establishment of institutional herds in state livestock farms and Gaushalas located within native breeding tracts."
        "<br>&bull; Provision of incentives, breed societies, breed shows, and premium milk procurement pricing for purebred native livestock."
        "<li><b>Advantages:</b> Allows the breed to continue evolving dynamically under changing climatic and disease pressures; preserves pastoral ethno-veterinary culture.</li>"
        "</ul><br>"
        "<b>II. EX-SITU CONSERVATION (OUTSIDE NATIVE HABITAT)</b><br>"
        "<ol>"
        "<li><b>Ex-situ In-vivo:</b> Maintaining living herds or flocks outside their native tract in university livestock research farms, agricultural colleges, or zoological parks.</li>"
        "<li><b>Ex-situ In-vitro (Cryogenic Gene Banking):</b>"
        "<br>&bull; Storage of biological germplasm at cryogenic temperatures in liquid nitrogen (<b>-196&deg;C</b>)."
        "<br>&bull; <b>National Gene Bank at ICAR-NBAGR, Karnal:</b>"
        "<br>&nbsp;&nbsp;&bull; <i>Deep-frozen Semen:</i> Hundreds of thousands of semen doses from pedigree-characterized, disease-free native sires."
        "<br>&nbsp;&nbsp;&bull; <i>Embryo Banking:</i> Cryopreserved in-vivo derived and in-vitro produced embryos."
        "<br>&nbsp;&nbsp;&bull; <i>DNA & Tissue Repositories:</i> Genomic DNA samples, somatic cell lines (fibroblasts for potential somatic cell nuclear transfer / cloning), and ovarian tissue banking.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Conservation Genetics: Safe Effective Population Size (Ne) & Inbreeding Limits:</b><br>"
        "In university exams, explain the population genetics principles governing conservation design:"
        "<ul>"
        "<li><b>Franklin's 50/500 Rule of Conservation:</b>"
        "<br>&bull; <i>Short-term Conservation:</i> Minimum <b>Ne &ge; 50</b> to prevent catastrophic inbreeding depression (limits inbreeding accumulation to <code>&Delta;F &le; 1%</code> per generation: <code>&Delta;F = 1 / (2 Ne) = 1/100 = 0.01</code>)."
        "<br>&bull; <i>Long-term Conservation:</i> Minimum <b>Ne &ge; 500</b> to maintain long-term evolutionary potential and genetic variance, balancing new mutational variance with drift loss.</li>"
        "<li><b>Optimal Contribution Theory (Meuwissen 1997):</b> Mathematical algorithm implemented in gene bank management to maximize genetic diversity while restricting cumulative inbreeding: <code>Max: c'u - &lambda; c'Ac</code> (where <code>c</code> is the vector of parental genetic contributions, <code>u</code> is breeding value, and <code>A</code> is the relationship matrix).</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Animal Genetic Resources (AnGR) include all domesticated livestock and avian species used for food and agriculture.",
        "India possesses over 212 registered indigenous breeds characterized by ICAR-NBAGR Karnal.",
        "Primary threats to AnGR: indiscriminate crossbreeding, mechanization of draft power, and loss of grazing lands.",
        "Indigenous Zebu cattle possess superior heat tolerance (HSP70/90), tick resistance, and 100% A2 milk allele.",
        "FAO categorizes endangered breeds into Critical (< 100 females), Endangered (100–1000), and Vulnerable.",
        "In-situ conservation maintains livestock within their native breeding tract and traditional pastoralist systems.",
        "In-situ conservation allows continued dynamic adaptation and co-evolution with local parasites and climate.",
        "Ex-situ in-vivo conservation maintains live animals in dedicated research farms and gaushalas outside the tract.",
        "Ex-situ in-vitro conservation cryopreserves semen, embryos, and somatic cells at -196°C in liquid nitrogen.",
        "The National Gene Bank at ICAR-NBAGR Karnal preserves the national repository of cryopreserved AnGR germplasm.",
        "Franklin's 50/500 rule mandates Ne ≥ 50 for short-term inbreeding avoidance and Ne ≥ 500 for long-term genetic variance."
    ],
    "tables": [
        {
            "title": "Comprehensive Comparison Between In-situ and Ex-situ Livestock Conservation Methods",
            "headers": ["Parameter / Feature", "In-situ Conservation (On-Farm)", "Ex-situ In-vivo (Institutional Farms)", "Ex-situ In-vitro (Cryogenic Gene Bank)"],
            "rows": [
                ["Location / Setting", "Native breeding tract / pastoral agro-ecosystem", "Research institutions, universities, gaushalas", "National Gene Bank (ICAR-NBAGR, Karnal)"],
                ["Form of Germplasm", "Live breeding herds in production", "Live animals maintained in captivity", "Deep-frozen semen (-196&deg;C), vitrified embryos, DNA, somatic cells"],
                ["Evolutionary Adaptation", "Dynamic; continuous co-evolution with pathogens & climate", "Static to artificial; adapted to farm management", "Completely frozen in time; zero genetic change"],
                ["Capital Infrastructure", "Low; relies on existing farmers and pastoralists", "High; requires land, housing, feed, and labor", "High initial lab cost; extremely low long-term maintenance per sample"],
                ["Risk of Extinction Events", "Vulnerable to local epidemics, famines, droughts", "Vulnerable to institutional disease outbreaks", "Safe from field epidemics; vulnerable only to liquid nitrogen failure"],
                ["Community & Cultural Value", "High; sustains rural livelihoods and pastoral culture", "Moderate; serves educational/research role", "None directly; serves as emergency insurance backup"],
                ["Reconstitution Potential", "Immediate (already in active reproduction)", "Immediate (live animals ready for breeding)", "Requires AI, embryo transfer, or cloning to regenerate live animals"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "Veterinarians working in native tracts of endangered indigenous breeds (e.g., <b>Punganur dwarf cattle</b> of Andhra Pradesh, "
        "<b>Vechur cattle</b> of Kerala, <b>Bhadawari high-fat buffalo</b> of Chambal ravines, or <b>Krishna Valley cattle</b>) "
        "have a statutory duty to prevent genetic extinction. "
        "When an owner brings a pure Punganur or Vechur cow for insemination, the veterinarian must NEVER use exotic HF/Jersey semen. "
        "The veterinarian must maintain a dedicated liquid nitrogen container containing certified purebred Punganur/Vechur semen straws "
        "sourced from state conservation farms or NBAGR, actively preserving these irreplaceable dwarf germplasm pools."
    ),
    "tags": ["AnGR", "Conservation Genetics", "In-situ Conservation", "Ex-situ Conservation", "Cryopreservation", "ICAR-NBAGR", "Vechur", "Punganur", "50/500 Rule"]
}
