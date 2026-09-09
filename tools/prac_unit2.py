# -*- coding: utf-8 -*-
"""
Practical Unit 2: Topics p2-t01 to p2-t08
Principles of Animal and Population Genetics Lab (IVRI Undergrad 10 CGPA Standard)
Strictly exam-specific: Aim, Principle, Formulae, Solved Model Problems, Inferences, Viva-Voce
"""

topics = {}

topics["p2-t01"] = {
    "summary": "Practical exercises on Monohybrid and Dihybrid crosses in livestock, demonstrating segregation, independent assortment, test-cross ratios, and Chi-Square verification.",
    "desc": (
        "<b>AIM:</b> To solve monohybrid and dihybrid cross problems in livestock, formulate Punnett squares, determine genotypic and phenotypic ratios, and verify results using Chi-Square.<br><br>"
        "<b>CORE MENDELIAN RATIOS:</b>"
        "<ul>"
        "<li><b>Monohybrid F2 Ratio:</b> Phenotypic = <code>3 : 1</code>; Genotypic = <code>1 : 2 : 1</code>.</li>"
        "<li><b>Monohybrid Test Cross (Backcross to Recessive):</b> <code>1 : 1</code>.</li>"
        "<li><b>Dihybrid F2 Ratio:</b> Phenotypic = <code>9 : 3 : 3 : 1</code>; Genotypic = <code>1:2:1:2:4:2:1:2:1</code>.</li>"
        "<li><b>Dihybrid Test Cross:</b> <code>1 : 1 : 1 : 1</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (MONOHYBRID LIVESTOCK CROSS):</b><br>"
        "In cattle, the polled condition (P) is dominant over the horned condition (p). A homozygous polled bull (PP) is mated to horned cows (pp).<br>"
        "1. Give the genotype and phenotype of F1 progeny.<br>"
        "2. If F1 individuals are inter-mated, what are the expected genotypic and phenotypic ratios in F2?<br>"
        "3. If an F1 polled bull is mated back to horned cows (test cross), what progeny are expected?<br><br>"
        "<b>STEP-BY-STEP SOLUTION:</b>"
        "<ol>"
        "<li><b>Parents:</b> <code>PP (Polled Bull) &times; pp (Horned Cows)</code> &rarr; Gametes: <code>P</code> and <code>p</code>.<br>"
        "<b>F1 Generation:</b> Genotype = <b>100% Pp (Heterozygous)</b>; Phenotype = <b>100% Polled</b>.</li>"
        "<li><b>F1 &times; F1 Inter-se Mating:</b> <code>Pp &times; Pp</code>.<br>"
        "Gametes: 50% P, 50% p from each parent.<br>"
        "Punnett Square yields: <code>1 PP : 2 Pp : 1 pp</code>.<br>"
        "<b>F2 Phenotypic Ratio:</b> <b>3 Polled : 1 Horned</b> (75% Polled, 25% Horned).<br>"
        "<b>F2 Genotypic Ratio:</b> <b>1 PP : 2 Pp : 1 pp</b> (25% homozygous polled, 50% heterozygous polled, 25% horned).</li>"
        "<li><b>Test Cross:</b> <code>Pp (F1 Bull) &times; pp (Horned Cow)</code>.<br>"
        "Gametes: Bull produces 1/2 P and 1/2 p; Cow produces 100% p.<br>"
        "Progeny: <code>1/2 Pp (Polled) : 1/2 pp (Horned)</code> &rarr; <b>1 : 1 Ratio</b>.</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM 2 (DIHYBRID CROSS):</b><br>"
        "In cattle, Black coat (B) is dominant over Red coat (b), and Polled (P) is dominant over Horned (p). "
        "A homozygous black polled bull (BBPP) is crossed with a red horned cow (bbpp). "
        "Calculate the probability of obtaining a <b>Red Polled</b> calf in F2.<br>"
        "<b>Solution:</b><br>"
        "In a dihybrid F2 (9:3:3:1), the phenotypic proportions are:<br>"
        "<code>9/16 Black Polled (B_P_) : 3/16 Black Horned (B_pp) : 3/16 Red Polled (bbP_) : 1/16 Red Horned (bbpp)</code>.<br>"
        "<b>Answer:</b> Probability of Red Polled (bbP_) = <b>3/16 (18.75%)</b>.<br><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What is a Test Cross and why is it performed in livestock?</b><br>"
        "<b>A:</b> A cross of an individual of dominant phenotype with a homozygous recessive individual. It is used to determine whether a dominant animal (e.g., polled bull) is homozygous (PP) or heterozygous carrier (Pp).</li>"
        "<li><b>Q: How many test-cross progeny without a single horned calf are needed to prove a bull homozygous polled with > 99% confidence?</b><br>"
        "<b>A:</b> <code>(1/2)^n &lt; 0.01  &rarr;  n &ge; 7</code> calves (7 consecutive polled calves from horned dams prove homozygosity at P &gt; 0.99).</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Use the <b>Forked-Line (Branching) Method</b> for trihybrid or multihybrid crosses: combine individual monohybrid probabilities: <code>P(bbP_) = P(bb) &times; P(P_) = (1/4) &times; (3/4) = 3/16</code>. This saves 15 minutes compared to drawing a 16-cell Punnett square!</li>"
        "<li>Formula for number of F2 gametes: <code>2^n</code>; number of F2 genotypes: <code>3^n</code>; number of F2 phenotypes: <code>2^n</code> (where n = number of heterozygous gene pairs).</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Monohybrid cross tracks one trait; F2 phenotypic ratio is 3:1, genotypic is 1:2:1.",
        "Dihybrid cross tracks two independent traits; F2 phenotypic ratio is 9:3:3:1.",
        "Test cross mates an unknown dominant phenotype with homozygous recessive.",
        "Monohybrid test cross gives a 1:1 ratio; dihybrid test cross gives 1:1:1:1.",
        "Polled (P) is dominant over horned (p) in cattle and sheep.",
        "Black coat color (B) is dominant over red coat color (b) in cattle.",
        "Number of distinct gametes produced is 2^n (n = heterozygous loci).",
        "Number of F2 genotypes is 3^n; number of F2 phenotypes is 2^n under complete dominance.",
        "Forked-line method calculates dihybrid probabilities by multiplying monohybrid fractions.",
        "Seven consecutive normal calves from recessive mates prove sire homozygosity at > 99% confidence."
    ],
    "tables": [
        {
            "title": "Dihybrid F2 Punnett Square for Coat Color and Horn Status in Cattle (BbPp x BbPp)",
            "headers": ["Female \\ Male Gametes", "BP (1/4)", "Bp (1/4)", "bP (1/4)", "bp (1/4)"],
            "rows": [
                ["BP (1/4)", "BBPP (Black Polled)", "BBPp (Black Polled)", "BbPP (Black Polled)", "BbPp (Black Polled)"],
                ["Bp (1/4)", "BBPp (Black Polled)", "BBpp (Black Horned)", "BbPp (Black Polled)", "Bbpp (Black Horned)"],
                ["bP (1/4)", "BbPP (Black Polled)", "BbPp (Black Polled)", "bbPP (Red Polled)", "bbPp (Red Polled)"],
                ["bp (1/4)", "BbPp (Black Polled)", "Bbpp (Black Horned)", "bbPp (Red Polled)", "bbpp (Red Horned)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In dairy cattle breeding, horned cattle cause traumatic udder injuries, bruising, and handler danger in loose housing. "
        "Veterinarians conduct <b>Progeny Test Matings of candidate AI bulls with horned cows (pp)</b>. "
        "If a single horned calf is born, the bull is immediately identified as a heterozygous carrier (Pp) "
        "and disqualified from being marketed as a homozygous polled sire."
    ),
    "tags": ["Genetics Lab", "Mendelian Cross", "Monohybrid", "Dihybrid", "Punnett Square", "Test Cross", "Polled Gene", "Coat Color"]
}

topics["p2-t02"] = {
    "summary": "Numerical problem solving on modified Mendelian ratios (incomplete dominance, codominance, lethals), epistasis interactions, and sex-linked crisscross inheritance in poultry and livestock.",
    "desc": (
        "<b>AIM:</b> To identify and solve problems on non-Mendelian modifications, epistasis ratios, and sex-linked inheritance in poultry and livestock.<br><br>"
        "<b>CLASSICAL MODIFIED RATIOS CHEAT-SHEET:</b>"
        "<ul>"
        "<li><b>Incomplete Dominance / Codominance:</b> <code>1 : 2 : 1</code> (Roan coat in Shorthorn; Andalusian blue fowl).</li>"
        "<li><b>Recessive Lethal Gene:</b> <code>2 : 1</code> (Yellow coat in mice; Creeper fowl; Bulldog calf in Dexter cattle).</li>"
        "<li><b>Recessive Epistasis:</b> <code>9 : 3 : 4</code> (Coat color in Labrador Retrievers).</li>"
        "<li><b>Dominant Epistasis:</b> <code>12 : 3 : 1</code> (Coat color in dogs; plumage in poultry).</li>"
        "<li><b>Duplicate Dominant Epistasis:</b> <code>15 : 1</code> (Feathered shanks).</li>"
        "<li><b>Duplicate Recessive (Complementary):</b> <code>9 : 7</code> (Comb type interaction).</li>"
        "<li><b>Dominant & Recessive Interaction (Inhibitory Gene):</b> <code>13 : 3</code> (White plumage in Leghorn vs colored).</li>"
        "<li><b>Duplicate Genes with Cumulative Effect:</b> <code>9 : 6 : 1</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (RECESSIVE EPISTASIS IN LABRADORS):</b><br>"
        "In Labrador Retrievers, Black (B) is dominant to Chocolate (b). A second epistatic locus (E) controls pigment deposition: "
        "<code>E_</code> permits pigment, whereas homozygous recessive <code>ee</code> prevents pigment deposition, resulting in Yellow coat regardless of B/b.<br>"
        "Cross two dihybrid Black Labradors (<code>BbEe &times; BbEe</code>) and determine the phenotypic ratio.<br><br>"
        "<b>SOLUTION:</b><br>"
        "Dihybrid segregation yields:<br>"
        "<code>9 B_E_ (Black) : 3 bbE_ (Chocolate) : 3 B_ee (Yellow) : 1 bbee (Yellow)</code>.<br>"
        "Combining the yellow genotypes: <code>3 B_ee + 1 bbee = 4 Yellow</code>.<br>"
        "<b>Resulting F2 Ratio:</b> <b>9 Black : 3 Chocolate : 4 Yellow</b> (Recessive Epistasis).<br><br>"
        "<b>MODEL EXAM PROBLEM 2 (SEX-LINKED CRISSCROSS INHERITANCE IN POULTRY):</b><br>"
        "In poultry, the barred plumage pattern (B) is sex-linked dominant over non-barred black plumage (b) on the Z chromosome (Females are ZW, Males are ZZ). "
        "A non-barred black rooster (<code>Z^b Z^b</code>) is mated to a barred hen (<code>Z^B W</code>).<br>"
        "Predict the phenotypes of male and female offspring.<br><br>"
        "<b>SOLUTION:</b><br>"
        "<ul>"
        "<li>Rooster gametes: 100% <code>Z^b</code>.</li>"
        "<li>Hen gametes: 50% <code>Z^B</code>, 50% <code>W</code>.</li>"
        "<li><b>Male Progeny (ZZ):</b> <code>Z^b</code> (from sire) + <code>Z^B</code> (from dam) = <b>Z^B Z^b (100% Barred Males)</b>.</li>"
        "<li><b>Female Progeny (ZW):</b> <code>Z^b</code> (from sire) + <code>W</code> (from dam) = <b>Z^b W (100% Non-barred Black Females)</b>.</li>"
        "<li><b>Inference:</b> Perfect <b>Crisscross Inheritance</b>! The male transmits his character to daughters, and the female transmits her sex-linked trait to sons. Day-old chicks can be sexed 100% accurately at hatch (auto-sexing).</li>"
        "</ul><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Why do recessive lethal alleles produce a 2:1 ratio instead of 3:1?</b><br>"
        "<b>A:</b> Because the homozygous dominant (or homozygous recessive) genotype dies in utero or before hatching (e.g., Dexter bulldog calves), removing 1/4 of the expected progeny.</li>"
        "<li><b>Q: Which sex is heterogametic in birds vs mammals?</b><br>"
        "<b>A:</b> Mammalian females are homogametic (XX) and males heterogametic (XY); avian females are <b>heterogametic (ZW)</b> and avian males are <b>homogametic (ZZ)</b>.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Whenever an exam question presents an F2 ratio that sums to <b>16</b> (e.g. 9:3:4, 12:3:1, 13:3, 15:1, 9:7), immediately identify it as a <b>Two-Gene Epistatic Interaction</b>!</li>"
        "<li>Whenever a reciprocal cross gives different phenotypic distributions between sexes, immediately identify it as <b>Sex-Linked (Z-linked or X-linked)</b> inheritance.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Incomplete dominance and codominance produce a 1:2:1 phenotypic ratio in F2.",
        "Recessive lethal alleles alter the monohybrid F2 ratio to 2:1 due to embryonic death.",
        "Recessive epistasis produces a 9:3:4 ratio (e.g., coat color in Labrador Retrievers).",
        "Dominant epistasis produces a 12:3:1 ratio.",
        "Dominant and recessive interaction (inhibitory gene) produces a 13:3 ratio.",
        "Duplicate recessive (complementary) epistasis produces a 9:7 ratio.",
        "Duplicate dominant epistasis produces a 15:1 ratio.",
        "Avian females are heterogametic (ZW); avian males are homogametic (ZZ).",
        "Sex-linked recessive traits show crisscross inheritance: sire to daughter, dam to son.",
        "Sex-linked barring (B) and feathering (K) enable 100% accurate auto-sexing of day-old chicks."
    ],
    "tables": [
        {
            "title": "Master Summary Table of Epistatic Gene Interactions (Summing to 16 in F2)",
            "headers": ["Type of Gene Interaction", "F2 Phenotypic Ratio", "Classical Biological Example", "Genetic Mechanism"],
            "rows": [
                ["Recessive Epistasis", "9 : 3 : 4", "Labrador Retriever coat color", "Homozygous recessive 'ee' masks B/b locus"],
                ["Dominant Epistasis", "12 : 3 : 1", "Dog coat color (Dominant Black)", "Dominant allele at one locus masks both alleles of second"],
                ["Inhibitory Gene Interaction", "13 : 3", "White Leghorn plumage color", "Dominant inhibitor 'I' suppresses color gene 'C'"],
                ["Complementary (Duplicate Recessive)", "9 : 7", "Comb types / Flower color", "Homozygous recessives at either locus produce same mutant phenotype"],
                ["Duplicate Dominant", "15 : 1", "Feathered shanks in poultry", "Dominant allele at either locus produces the trait"],
                ["Duplicate Genes with Cumulative Effect", "9 : 6 : 1", "Pork quality / Grain shape", "Two dominants produce extreme, single dominant intermediate"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In canine pedigree practice, mating two <b>Merle-coated Australian Shepherds or Great Danes</b> (heterozygous <code>Mm</code>) "
        "produces 25% 'Double Merle' pups (<code>MM</code>). "
        "Veterinarians advise breeders against Merle-to-Merle matings because double merles suffer from microphthalmia, complete congenital deafness, and night blindness."
    ),
    "tags": ["Genetics Lab", "Epistasis", "Modified Mendelian Ratio", "Labrador Coat Color", "Crisscross Inheritance", "Sex-Linkage", "Auto-Sexing"]
}

topics["p2-t03"] = {
    "summary": "Estimation of linkage, recombination frequency (RF), construction of genetic chromosome maps, and calculation of Coefficient of Coincidence and Interference.",
    "desc": (
        "<b>AIM:</b> To estimate recombination frequency from two-point and three-point test-cross progeny, construct genetic linkage maps, and calculate Coefficient of Coincidence and Interference.<br><br>"
        "<b>FORMULAS & EQUATIONS:</b>"
        "<ul>"
        "<li><b>Recombination Frequency (RF%):</b><br>"
        "<code>RF% = (Total Number of Recombinants / Total Progeny) &times; 100</code></li>"
        "<li><b>Map Distance:</b> <code>1% Recombination Frequency = 1 Map Unit (mu) = 1 centiMorgan (cM)</code>.</li>"
        "<li><b>Coefficient of Coincidence (C):</b><br>"
        "<code>C = Observed Frequency of Double Crossovers / Expected Frequency of Double Crossovers</code><br>"
        "Where <code>Expected DCO = RF_1 &times; RF_2</code>.</li>"
        "<li><b>Interference (I):</b><br>"
        "<code>I = 1 - C</code><br>"
        "If <code>I &gt; 0</code>: Positive interference (one crossover inhibits adjacent crossovers); If <code>I = 1</code>: Complete interference (zero DCO observed).</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM (TWO-POINT TEST CROSS):</b><br>"
        "In a test-cross of a heterozygous female for two linked genes (A and B in coupling phase) with a double recessive male (<code>aabb</code>), "
        "the following 1,000 progeny were obtained:<br>"
        "<code>Parental Types: AB (420), ab (430)</code><br>"
        "<code>Recombinant Types: Ab (78), aB (72)</code><br>"
        "Calculate the recombination frequency and map distance between genes A and B.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li>Total progeny <code>N = 420 + 430 + 78 + 72 = 1,000</code>.</li>"
        "<li>Total parental progeny = <code>420 + 430 = 850 (85%)</code>.</li>"
        "<li>Total recombinant progeny = <code>78 + 72 = 150</code>.</li>"
        "<li><b>Recombination Frequency (RF):</b><br>"
        "<code>RF% = (150 / 1000) &times; 100 = 15.0%</code>.</li>"
        "<li><b>Map Distance:</b> Since 1% RF = 1 cM, the genetic distance between locus A and locus B is <b>15.0 cM (or 15 map units)</b>.</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM 2 (INTERFERENCE & COINCIDENCE):</b><br>"
        "If the map distance between gene A and B is 10 cM (RF1 = 0.10) and between B and C is 20 cM (RF2 = 0.20), "
        "and in a sample of 2,000 progeny, <b>24 double crossovers</b> were observed, calculate Interference.<br>"
        "<b>Solution:</b><br>"
        "<ol>"
        "<li><code>Expected DCO fraction = 0.10 &times; 0.20 = 0.02 (2%)</code>.</li>"
        "<li><code>Expected DCO count = 0.02 &times; 2,000 = 40 progeny</code>.</li>"
        "<li><code>Coefficient of Coincidence (C) = 24 / 40 = 0.60</code>.</li>"
        "<li><code>Interference (I) = 1 - C = 1 - 0.60 = 0.40 (40%)</code>.</li>"
        "<li><b>Inference:</b> Positive interference exists; the occurrence of the first crossover reduced expected crossing over in the adjacent region by 40%.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What is the theoretical maximum limit of recombination frequency between two linked genes?</b><br>"
        "<b>A:</b> <b>50%</b>. At or above 50% recombination, linked genes segregate identically to unlinked genes obeying independent assortment.</li>"
        "<li><b>Q: What are coupling (cis) and repulsion (trans) linkage phases?</b><br>"
        "<b>A:</b> In <b>Coupling (cis)</b>, two dominant alleles are on one homolog (<code>AB / ab</code>); in <b>Repulsion (trans)</b>, one dominant and one recessive allele are on each homolog (<code>Ab / aB</code>).</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>In three-point test crosses, the <b>two least frequent phenotypic classes</b> are always the <b>Double Crossovers (DCO)</b>, and the <b>two most frequent classes</b> are the <b>Parental types</b>. Comparing DCO with Parentals immediately identifies the <b>middle gene</b>!</li>"
        "<li>Haldane's mapping function correction: <code>m = - (1/2) ln(1 - 2r)</code> adjusts for unobserved multiple crossovers over large map distances (> 20 cM).</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Recombination Frequency formula: RF% = (Total Recombinants / Total Progeny) * 100.",
        "One map unit (1 mu) or 1 centiMorgan (cM) equals 1% recombination frequency.",
        "Maximum theoretical recombination frequency between two genes is 50%.",
        "Parental combinations always appear with highest frequency in linkage test crosses.",
        "Double crossovers appear with lowest frequency in three-point test crosses.",
        "The gene that differs between parentals and double crossovers is located in the middle.",
        "Coefficient of Coincidence: C = Observed DCO / Expected DCO.",
        "Interference formula: I = 1 - C.",
        "Positive interference (I > 0) means one chiasma inhibits adjacent chiasma formation.",
        "Coupling phase has dominant alleles on same chromosome; repulsion phase on opposites."
    ],
    "tables": [
        {
            "title": "Three-Point Test-Cross Phenotypic Progeny Classes and Linkage Analysis Table",
            "headers": ["Progeny Phenotypic Class", "Observed Progeny Count", "Crossover Classification", "Region Involved", "Calculation Formula"],
            "rows": [
                ["A B C (Parental 1)", "385", "Non-crossover (NCO)", "None", "Parental linkage arrangement"],
                ["a b c (Parental 2)", "395", "Non-crossover (NCO)", "None", "Parental linkage arrangement"],
                ["A B c (Single Crossover)", "85", "Single crossover (SCO-2)", "Region II (B - C)", "Included in Region II RF"],
                ["a b C (Single Crossover)", "75", "Single crossover (SCO-2)", "Region II (B - C)", "Included in Region II RF"],
                ["A b c (Single Crossover)", "25", "Single crossover (SCO-1)", "Region I (A - B)", "Included in Region I RF"],
                ["a B C (Single Crossover)", "23", "Single crossover (SCO-1)", "Region I (A - B)", "Included in Region I RF"],
                ["A b C (Double Crossover)", "6", "Double crossover (DCO)", "Both Regions", "Lowest observed frequency"],
                ["a B c (Double Crossover)", "6", "Double crossover (DCO)", "Both Regions", "Lowest observed frequency"],
                ["Total Progeny (N)", "1,000", "—", "—", "Map Dist = (SCO + DCO)/N * 100"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In commercial swine breeding, the malignant hyperthermia halothane gene (<i>RYR1</i>) is tightly linked to the <i>GPI</i> (glucosephosphate isomerase) marker locus. "
        "Historically, before direct PCR tests were invented, veterinarians utilized linkage analysis of GPI blood protein polymorphisms "
        "to track and cull carrier breeding boars prone to fatal Porcine Stress Syndrome (PSS)."
    ),
    "tags": ["Genetics Lab", "Linkage", "Recombination Frequency", "Map Distance", "centiMorgan", "Interference", "Coincidence", "Three-Point Cross"]
}

topics["p2-t04"] = {
    "summary": "Laboratory protocol for peripheral blood sampling, lymphocyte culture, Colchicine metaphase arrest, hypotonic shock, slide preparation, GTG-banding, and karyotyping in livestock.",
    "desc": (
        "<b>AIM:</b> To demonstrate peripheral blood sampling, set up short-term lymphocyte culture, harvest metaphase chromosomes, prepare Giemsa-stained slides, and construct livestock karyotypes.<br><br>"
        "<b>STEP-BY-STEP LABORATORY PROTOCOL:</b>"
        "<ol>"
        "<li><b>Aseptic Blood Collection:</b>"
        "<br>&bull; Collect 5 ml venous blood from the external jugular vein under strict sterile conditions into a sterile vacutainer containing <b>Sodium Heparin (15–20 IU/ml)</b>. (Never use EDTA, as it chelates divalent cations and kills lymphocytes!).</li>"
        "<li><b>Culture Inoculation:</b>"
        "<br>&bull; In a laminar airflow hood, add <b>0.5 to 0.8 ml of whole blood</b> to a sterile culture vial containing <b>8 ml RPMI-1640</b> (or Ham's F-10) culture medium supplemented with:"
        "<br>&nbsp;&nbsp;&bull; 15% Fetal Bovine Serum (FBS) (provides growth factors)."
        "<br>&nbsp;&nbsp;&bull; 1% Antibiotic-Antimycotic solution (Penicillin-Streptomycin-Amphotericin B)."
        "<br>&nbsp;&nbsp;&bull; <b>0.1 ml Phytohemagglutinin-M (PHA-M):</b> Mitogenic lectin extracted from <i>Phaseolus vulgaris</i>; selectively stimulates mature T-lymphocytes to dedifferentiate and divide.</li>"
        "<li><b>Incubation:</b> Incubate culture tubes at <b>37.5&deg;C with 5% CO2 for 72 hours</b> in a humidified bacteriological/CO2 incubator. Gently invert tubes twice daily.</li>"
        "<li><b>Metaphase Arrest (71st hour):</b>"
        "<br>&bull; Add <b>0.1 ml of Colchicine (or Colcemid, 0.05 &mu;g/ml)</b> 1 to 1.5 hours prior to harvesting."
        "<br>&bull; <i>Mechanism:</i> Binds to tubulin dimers, inhibits mitotic spindle microtubule assembly, and arrests dividing lymphoblasts at <b>Metaphase</b>.</li>"
        "<li><b>Hypotonic Treatment:</b>"
        "<br>&bull; Centrifuge culture at 1,000 rpm for 10 minutes; discard supernatant."
        "<br>&bull; Resuspend cell pellet in <b>pre-warmed (37&deg;C) 0.075 M Potassium Chloride (KCl)</b> for <b>15 to 20 minutes</b>."
        "<br>&bull; <i>Principle:</i> Hypotonic solution forces water into cells by osmosis, swelling the fragile cytoplasm and separating crowded chromosomes.</li>"
        "<li><b>Fixation (Carnoy's Fixative):</b>"
        "<br>&bull; Add 1 ml of freshly prepared, chilled <b>Carnoy's fixative (3 parts Methanol : 1 part Glacial Acetic Acid)</b>."
        "<br>&bull; Centrifuge, discard supernatant, and repeat washing with fixative 3 to 4 times until the pellet is chalky white.</li>"
        "<li><b>Slide Casting & Air-Drying:</b>"
        "<br>&bull; Drop 2–3 drops of cell suspension from a height of 1 to 2 feet onto a pre-cleaned, ice-chilled, wet glass slide held at a 45&deg; angle. Air-dry rapidly over a gentle warm flame or hotplate (45&deg;C).</li>"
        "<li><b>Staining / GTG Banding:</b>"
        "<br>&bull; Stain with 4% Giemsa in phosphate buffer (pH 6.8) for 15 minutes, or treat briefly with 0.05% Trypsin followed by Giemsa for <b>G-banding (GTG)</b>.</li>"
        "</ol><br>"
        "<b>DIPLOID CHROMOSOME NUMBERS (2n) FOR VIVA:</b>"
        "<ul>"
        "<li><b>Cattle (<i>Bos indicus / Bos taurus</i>):</b> <code>2n = 60</code> (All 29 autosome pairs are acrocentric; X is large submetacentric, Y is small metacentric in taurine / small acrocentric in indicine).</li>"
        "<li><b>River Buffalo (<i>Bubalus bubalis</i>):</b> <code>2n = 50</code> (5 submetacentric autosome pairs + 19 acrocentric autosome pairs + acrocentric X and Y).</li>"
        "<li><b>Swamp Buffalo:</b> <code>2n = 48</code>.</li>"
        "<li><b>Sheep (<i>Ovis aries</i>):</b> <code>2n = 54</code> (3 metacentric pairs + 23 acrocentric autosome pairs).</li>"
        "<li><b>Goat (<i>Capra hircus</i>):</b> <code>2n = 60</code> (All autosomes acrocentric).</li>"
        "<li><b>Pig (<i>Sus scrofa</i>):</b> <code>2n = 38</code>.</li>"
        "<li><b>Horse (<i>Equus caballus</i>):</b> <code>2n = 64</code>.</li>"
        "<li><b>Dog (<i>Canis familiaris</i>):</b> <code>2n = 78</code>.</li>"
        "<li><b>Chicken (<i>Gallus domesticus</i>):</b> <code>2n = 78</code> (9 macrochromosome pairs + 30 microchromosome pairs).</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Why Sodium Heparin and NOT EDTA? EDTA irreversibly chelates Ca&sup2;&plus; and Mg&sup2;&plus;, halting lymphocyte cell division. Stating this secures full marks in viva.</li>"
        "<li>Diagnosing Robertsonian Translocation: The <code>rob(1;29)</code> centric fusion in cattle reduces chromosome count from 60 to <b>59 (heterozygote)</b> or <b>58 (homozygote)</b>, producing a massive dicentric submetacentric chromosome.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Peripheral blood must be collected in Sodium Heparin vacutainers (never EDTA).",
        "Phytohemagglutinin (PHA) is the T-lymphocyte mitogen initiating mitosis in vitro.",
        "Lymphocyte culture is incubated at 37.5°C in RPMI-1640 medium for 72 hours.",
        "Colchicine inhibits spindle microtubule formation, arresting dividing cells at metaphase.",
        "Hypotonic 0.075 M KCl treatment swells cells by osmosis to spread chromosomes.",
        "Carnoy's fixative consists of 3 parts absolute methanol and 1 part glacial acetic acid.",
        "Cattle chromosome number: 2n = 60 (29 pairs acrocentric autosomes).",
        "River buffalo: 2n = 50 (5 pairs submetacentric, 19 pairs acrocentric).",
        "Swamp buffalo has 2n = 48 chromosomes due to tandem fusion.",
        "GTG banding uses trypsin digestion followed by Giemsa staining to visualize G-bands."
    ],
    "tables": [
        {
            "title": "Comparative Cytogenetic Features and Karyotypic Profiles of Farm Animals",
            "headers": ["Species", "Scientific Name", "Diploid No. (2n)", "Autosome Morphology", "Sex Chromosomes (X / Y)"],
            "rows": [
                ["Cattle (Zebu / Taurine)", "Bos indicus / Bos taurus", "2n = 60", "All 58 autosomes are Acrocentric", "X: Large Submetacentric; Y: Small Acrocentric (Zebu) / Metacentric (HF)"],
                ["River Buffalo", "Bubalus bubalis", "2n = 50", "Pairs 1–5: Submetacentric; Pairs 6–24: Acrocentric", "X: Largest Acrocentric; Y: Small Acrocentric"],
                ["Swamp Buffalo", "Bubalus bubalis carabanesis", "2n = 48", "Pairs 1–5: Submetacentric; Pairs 6–23: Acrocentric", "X: Large Acrocentric; Y: Small Acrocentric"],
                ["Sheep", "Ovis aries", "2n = 54", "Pairs 1–3: Metacentric; Pairs 4–26: Acrocentric", "X: Large Acrocentric; Y: Minute Metacentric"],
                ["Goat", "Capra hircus", "2n = 60", "All 58 autosomes are Acrocentric", "X: Large Acrocentric; Y: Small Acrocentric"],
                ["Pig (Swine)", "Sus scrofa", "2n = 38", "Metacentric, Submetacentric & Telocentric", "X: Metacentric; Y: Small Metacentric"],
                ["Dog", "Canis familiaris", "2n = 78", "All 76 autosomes are Acrocentric", "X: Large Submetacentric; Y: Small Metacentric"],
                ["Chicken", "Gallus domesticus", "2n = 78", "9 pairs Macrochromosomes + 30 pairs Microchromosomes", "ZZ: Metacentric (Male); ZW: Z-Metacentric, W-Microchromosome (Female)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "Under statutory breeding regulations, all breeding bulls stationed at Artificial Insemination centers across India "
        "must be certified cytogenetically free of <b>Robertsonian rob(1;29) translocations</b>. "
        "Bulls carrying rob(1;29) appear phenotypically normal and produce normal sperm motility, but cause a <b>10–15% drop in herd conception rates</b> "
        "due to monosomy and trisomy embryonic lethality in early blastocysts."
    ),
    "tags": ["Genetics Lab", "Karyotyping", "Lymphocyte Culture", "Colchicine", "PHA", "Hypotonic KCl", "Carnoy's Fixative", "2n Numbers", "rob(1;29)"]
}

topics["p2-t05"] = {
    "summary": "Step-by-step calculation of gene and genotypic frequencies in livestock populations for codominant systems (gene counting) and dominant systems (square root method).",
    "desc": (
        "<b>AIM:</b> To estimate gene (allelic) and genotypic frequencies from livestock population data using the Gene Counting Method and Square Root Method.<br><br>"
        "<b>CORE FORMULAS:</b>"
        "<ul>"
        "<li><b>Genotypic Frequency:</b><br>"
        "<code>P = D = N_AA / N</code>; <code>H = N_Aa / N</code>; <code>Q = R = N_aa / N</code><br>"
        "Where <code>P + H + Q = 1.0</code>.</li>"
        "<li><b>1. Gene Counting Method (Codominant Loci):</b><br>"
        "<code>p = Frequency of allele A = (2 &times; N_AA + N_Aa) / (2N) = P + (1/2)H</code><br>"
        "<code>q = Frequency of allele a = (2 &times; N_aa + N_Aa) / (2N) = Q + (1/2)H</code><br>"
        "Check: <code>p + q = 1.0</code>.</li>"
        "<li><b>2. Square Root Method (Complete Dominance Systems):</b><br>"
        "Under assumption of Hardy-Weinberg equilibrium:<br>"
        "Recessive genotype frequency: <code>q&sup2; = N_aa / N</code><br>"
        "<code>q = &radic;(N_aa / N)</code><br>"
        "<code>p = 1 - q</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (CODOMINANT BLOOD GROUP SYSTEM):</b><br>"
        "In a herd of 200 Hariana cattle, hemoglobin typing revealed the following genotypes:<br>"
        "<code>Hb-AA = 98</code>, <code>Hb-AB = 84</code>, <code>Hb-BB = 18</code>.<br>"
        "Calculate the genotypic frequencies and gene frequencies of alleles A and B.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><code>Total cattle N = 98 + 84 + 18 = 200</code>. Total alleles = <code>2 &times; 200 = 400</code>.</li>"
        "<li><b>Genotypic Frequencies:</b><br>"
        "<code>Freq(AA) = 98 / 200 = 0.490 (49%)</code><br>"
        "<code>Freq(AB) = 84 / 200 = 0.420 (42%)</code><br>"
        "<code>Freq(BB) = 18 / 200 = 0.090 (9%)</code><br>"
        "Check: <code>0.490 + 0.420 + 0.090 = 1.000</code>.</li>"
        "<li><b>Gene Frequencies (Gene Counting Method):</b><br>"
        "<code>p = Freq(A) = [ (2 &times; 98) + 84 ] / 400 = (196 + 84) / 400 = 280 / 400 = 0.70</code>.<br>"
        "<code>q = Freq(B) = [ (2 &times; 18) + 84 ] / 400 = (36 + 84) / 400 = 120 / 400 = 0.30</code>.<br>"
        "Alternatively: <code>p = P + (1/2)H = 0.49 + (1/2)(0.42) = 0.49 + 0.21 = 0.70</code>.<br>"
        "Check: <code>p + q = 0.70 + 0.30 = 1.00</code>.</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM 2 (SQUARE ROOT METHOD FOR DOMINANCE):</b><br>"
        "In a flock of 500 sheep, 455 are white (dominant, W_) and 45 are black (recessive, ww). "
        "Assuming Hardy-Weinberg equilibrium, calculate the gene frequencies of W and w, and the number of heterozygous carriers.<br>"
        "<b>Solution:</b><br>"
        "<ol>"
        "<li><code>q&sup2; = Freq(ww) = 45 / 500 = 0.09</code>.</li>"
        "<li><code>q = &radic;0.09 = 0.30</code> (Frequency of recessive allele w).</li>"
        "<li><code>p = 1 - q = 1 - 0.30 = 0.70</code> (Frequency of dominant allele W).</li>"
        "<li>Frequency of heterozygotes <code>2pq = 2 &times; (0.70) &times; (0.30) = 0.42 (42%)</code>.</li>"
        "<li>Expected number of heterozygous carriers = <code>500 &times; 0.42 = 210 sheep</code>.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Why is the Gene Counting Method superior to the Square Root Method?</b><br>"
        "<b>A:</b> The Gene Counting method directly counts actual biological alleles without requiring the assumption of Hardy-Weinberg equilibrium; the Square Root method strictly depends on the assumption of random mating equilibrium.</li>"
        "<li><b>Q: Can gene frequency be negative or greater than 1.0?</b><br>"
        "<b>A:</b> No, gene frequency is a proportion and must strictly lie between <b>0.0 and 1.0</b>.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Multiple Alleles Shortcut (Bernstein's Method for ABO Blood Groups):<br>"
        "<code>r = &radic;(Freq O)</code>; <code>p = 1 - &radic;(Freq B + Freq O)</code>; <code>q = 1 - &radic;(Freq A + Freq O)</code>.</li>"
        "<li>Always round gene frequencies to two or three decimal places and demonstrate that <code>p + q = 1.0</code>.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Genotypic frequency is the proportion of a specific genotype in the population.",
        "Gene (allelic) frequency is the proportion of a specific allele among total alleles.",
        "Gene counting method for codominance: p = P + (1/2)H; q = Q + (1/2)H.",
        "Gene counting directly counts alleles: p = (2*NAA + NAa) / 2N.",
        "Square root method calculates recessive allele frequency as q = √(Naa / N).",
        "The square root method strictly assumes the population is in Hardy-Weinberg equilibrium.",
        "The sum of all allelic frequencies at a locus must equal 1.0: p + q = 1.0.",
        "Heterozygote frequency under HWE is 2pq.",
        "Most deleterious recessive alleles are hidden in heterozygous carriers (2pq >> q²).",
        "Bernstein's method estimates allele frequencies for tri-allelic blood group systems."
    ],
    "tables": [
        {
            "title": "Computation of Gene and Genotypic Frequencies for Hemoglobin Types in Hariana Cattle (N = 200)",
            "headers": ["Genotype", "Observed Count", "Genotypic Frequency", "No. of 'A' Alleles Contributed", "No. of 'B' Alleles Contributed"],
            "rows": [
                ["Hb-AA (Homozygous A)", "98", "0.490", "98 &times; 2 = 196", "0"],
                ["Hb-AB (Heterozygous)", "84", "0.420", "84 &times; 1 = 84", "84 &times; 1 = 84"],
                ["Hb-BB (Homozygous B)", "18", "0.090", "0", "18 &times; 2 = 36"],
                ["Total", "N = 200", "1.000", "Total A = 280", "Total B = 120"],
                ["Gene Frequencies", "—", "—", "p = 280 / 400 = 0.70", "q = 120 / 400 = 0.30"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In indigenous dairy cattle conservation programs, veterinarians type milk beta-casein alleles (A1 vs A2). "
        "Calculating gene frequencies across 500 Gir cattle reveals <code>p(A2) = 0.98</code> and <code>q(A1) = 0.02</code>, "
        "enabling state breeding federations to certify Gir cattle herds as <b>100% pure A2 milk producers</b>, commanding premium market prices."
    ),
    "tags": ["Population Genetics Lab", "Gene Frequency", "Genotypic Frequency", "Gene Counting", "Square Root Method", "Hardy-Weinberg", "Hariana Cattle", "Hemoglobin"]
}

topics["p2-t06"] = {
    "summary": "Testing animal populations for Hardy-Weinberg Equilibrium using Chi-Square Goodness of Fit test with degrees of freedom df = k - 1 - m.",
    "desc": (
        "<b>AIM:</b> To test whether an observed livestock population conforms to the Hardy-Weinberg Law of Equilibrium using the Chi-Square Goodness of Fit test.<br><br>"
        "<b>MATHEMATICAL PROCEDURE & EQUATIONS:</b>"
        "<ol>"
        "<li><b>Step 1:</b> Calculate sample gene frequencies <code>p</code> and <code>q</code> via Gene Counting.</li>"
        "<li><b>Step 2:</b> Calculate theoretical expected genotype frequencies under HWE:<br>"
        "<code>Expected Freq(AA) = p&sup2;</code><br>"
        "<code>Expected Freq(Aa) = 2pq</code><br>"
        "<code>Expected Freq(aa) = q&sup2;</code></li>"
        "<li><b>Step 3:</b> Calculate expected numbers of animals:<br>"
        "<code>E_AA = N &times; p&sup2;</code>; <code>E_Aa = N &times; 2pq</code>; <code>E_aa = N &times; q&sup2;</code>.</li>"
        "<li><b>Step 4:</b> Compute Chi-Square statistic:<br>"
        "<code>&chi;&sup2; = &Sigma; [ (O - E)&sup2; / E ]</code></li>"
        "<li><b>Step 5: Degrees of Freedom (df):</b><br>"
        "<code>df = k - 1 - m</code><br>"
        "Where <code>k = 3</code> (genotypic classes); <code>m = 1</code> (independent gene frequency <code>p</code> estimated from sample).<br>"
        "Therefore, <code>df = 3 - 1 - 1 = 1</code>! (Always 1 df for a two-allele locus!).</li>"
        "<li><b>Decision Rule:</b> Critical &chi;&sup2; at <code>df = 1, &alpha; = 0.05</code> is <b>3.841</b>. If &chi;&sup2;_cal &le; 3.841 &rarr; Accept H0 (Population is in HWE).</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM:</b><br>"
        "In a flock of 400 Garole sheep, Transferrin (Tf) blood protein typing revealed:<br>"
        "<code>Tf-AA = 210</code>, <code>Tf-AB = 140</code>, <code>Tf-BB = 50</code>.<br>"
        "Test whether this flock is in Hardy-Weinberg equilibrium (&chi;&sup2;_tab at df=1 for 5% = 3.841).<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><code>N = 400</code>.</li>"
        "<li><code>p = Freq(A) = [ (2 &times; 210) + 140 ] / 800 = (420 + 140) / 800 = 560 / 800 = 0.70</code>.</li>"
        "<li><code>q = Freq(B) = 1 - 0.70 = 0.30</code>.</li>"
        "<li><b>Expected Genotypic Numbers:</b><br>"
        "<code>E_AA = N &times; p&sup2; = 400 &times; (0.70)&sup2; = 400 &times; 0.49 = 196</code>.<br>"
        "<code>E_AB = N &times; 2pq = 400 &times; 2(0.70)(0.30) = 400 &times; 0.42 = 168</code>.<br>"
        "<code>E_BB = N &times; q&sup2; = 400 &times; (0.30)&sup2; = 400 &times; 0.09 = 36</code>.<br>"
        "Check: <code>&Sigma; E = 196 + 168 + 36 = 400 = N</code>.</li>"
        "<li><b>Compute Chi-Square:</b><br>"
        "Class AA: <code>(210 - 196)&sup2; / 196 = (14)&sup2; / 196 = 196 / 196 = 1.000</code><br>"
        "Class AB: <code>(140 - 168)&sup2; / 168 = (-28)&sup2; / 168 = 784 / 168 = 4.667</code><br>"
        "Class BB: <code>(50 - 36)&sup2; / 36 = (14)&sup2; / 36 = 196 / 36 = 5.444</code><br>"
        "<code>&chi;&sup2;_cal = 1.000 + 4.667 + 5.444 = 11.111</code>.</li>"
        "<li><b>Inference:</b> <code>&chi;&sup2;_cal = 11.111 &gt; &chi;&sup2;_tab(1, 0.05) = 3.841</code>. "
        "Null hypothesis H0 is <b>rejected (P &lt; 0.01)</b>.<br>"
        "<i>Conclusion:</i> The Garole sheep flock is <b>NOT in Hardy-Weinberg equilibrium</b>. "
        "(Notice the marked deficit of heterozygotes: 140 observed vs 168 expected, indicating significant inbreeding or positive assortative mating!).</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Why is df = 1 and NOT 2 when testing HWE for a 3-genotype system?</b><br>"
        "<b>A:</b> Although there are 3 classes (k = 3), we use 1 degree of freedom to fix the sample size N, and a second degree of freedom is lost because the gene frequency <code>p</code> was estimated directly from the sample data: <code>df = 3 - 1 - 1 = 1</code>.</li>"
        "<li><b>Q: What factors cause an animal population to deviate from Hardy-Weinberg equilibrium?</b><br>"
        "<b>A:</b> Small population size (genetic drift), non-random mating (inbreeding/assortative mating), artificial selection, migration (introduction of breeding sires), and mutation.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Heterozygote Deficit Indicator (Wright's Fixation Index F_IS):<br>"
        "<code>F_IS = 1 - (Observed Heterozygotes / Expected Heterozygotes) = 1 - (140 / 168) = 1 - 0.833 = +0.167</code>.<br>"
        "A positive F_IS confirms inbreeding within the subpopulation. Citing F_IS in your answer proves top-tier biometrical mastery!</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Hardy-Weinberg equilibrium states gene and genotypic frequencies remain constant under panmixia.",
        "Expected genotype frequencies under HWE are: p², 2pq, and q².",
        "Degrees of freedom for testing HWE at a bi-allelic locus is strictly df = 1 (df = k - 1 - m).",
        "Expected numbers: E(AA) = N*p², E(Aa) = N*2pq, E(aa) = N*q².",
        "Chi-square test statistic: χ² = Σ [(O - E)² / E].",
        "Critical χ² value at df = 1 for 5% significance level is 3.841.",
        "If χ²_cal > 3.841, the population deviates significantly from Hardy-Weinberg equilibrium.",
        "Deficit of observed heterozygotes compared to expected indicates inbreeding or positive assortative mating.",
        "Excess of observed heterozygotes indicates overdominance selection or outbreeding.",
        "Wright's Fixation Index F_IS = 1 - (H_obs / H_exp) quantifies inbreeding deviation."
    ],
    "tables": [
        {
            "title": "Testing Hardy-Weinberg Equilibrium in Garole Sheep Transferrin Locus (N = 400)",
            "headers": ["Genotype", "Observed (O)", "HWE Expected Frequency", "Expected Number (E)", "(O - E)", "Cell &chi;&sup2; = (O - E)&sup2;/E"],
            "rows": [
                ["Tf-AA", "210", "p&sup2; = 0.49", "196.0", "+14.0", "196 / 196.0 = 1.000"],
                ["Tf-AB", "140", "2pq = 0.42", "168.0", "-28.0", "784 / 168.0 = 4.667"],
                ["Tf-BB", "50", "q&sup2; = 0.09", "36.0", "+14.0", "196 / 36.0 = 5.444"],
                ["Total", "N = 400", "1.00", "&Sigma;E = 400.0", "0.0", "&chi;&sup2;_cal = 11.111** (df=1)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In closed nucleus breeding herds of Sahiwal cattle, veterinarians periodically perform Chi-Square HWE tests on molecular markers. "
        "A statistically significant deviation with an acute deficit of heterozygotes alerts the farm geneticist that <b>inbreeding has reached dangerous levels</b>, "
        "mandating immediate introduction of unrelated pedigreed breeding bulls from other state farms."
    ),
    "tags": ["Population Genetics Lab", "Hardy-Weinberg", "Chi-Square Test", "Goodness of Fit", "Degrees of Freedom", "Garole Sheep", "Transferrin", "Fixation Index"]
}

topics["p2-t07"] = {
    "summary": "Mathematical calculation of directional changes in gene frequency (Δq) driven by Mutation, Migration, Artificial Selection, and Random Genetic Drift.",
    "desc": (
        "<b>AIM:</b> To calculate changes in gene frequency (&Delta;q) under the deterministic forces of mutation, migration, and selection, and predict variance under genetic drift.<br><br>"
        "<b>GOVERNING EQUATIONS FOR EVOLUTIONARY FORCES:</b>"
        "<ul>"
        "<li><b>1. Recurrent Mutation:</b><br>"
        "Forward mutation (A &rarr; a) at rate <code>u</code>; Reverse mutation (a &rarr; A) at rate <code>v</code>.<br>"
        "<code>&Delta;q = u(1 - q) - vq = u &times; p - v &times; q</code>.<br>"
        "Equilibrium gene frequency: <code>\\hat{q} = u / (u + v)</code>.</li>"
        "<li><b>2. Migration (Gene Flow):</b><br>"
        "Immigrants enter population with frequency <code>q_m</code> at migration rate <code>m</code>.<br>"
        "New gene frequency: <code>q_1 = m &times; q_m + (1 - m) &times; q_0</code>.<br>"
        "Change in gene frequency: <code>&Delta;q = m &times; (q_m - q_0)</code>.</li>"
        "<li><b>3. Artificial Selection Against Recessive Homozygote (aa):</b><br>"
        "Selection coefficient = <code>s</code> (Fitness of aa = <code>1 - s</code>).<br>"
        "<code>&Delta;q = -s &times; p &times; q&sup2; / (1 - s &times; q&sup2;)</code>.<br>"
        "For <b>Complete Selection (s = 1)</b> (Culling all recessives):<br>"
        "<code>q_t = q_0 / (1 + t &times; q_0)</code> (where t = generations of selection).<br>"
        "Number of generations to reduce frequency from q_0 to q_t: <code>t = (1 / q_t) - (1 / q_0)</code>.</li>"
        "<li><b>4. Random Genetic Drift:</b><br>"
        "Variance in gene frequency per generation: <code>&sigma;&sup2;_{&Delta;q} = p &times; q / (2 N_e)</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (SELECTION AGAINST LETHAL RECESSIVE):</b><br>"
        "In a dairy herd, the frequency of a lethal recessive allele (e.g. BLAD, 'a') is <code>q_0 = 0.20</code>. "
        "If complete selection is practiced by culling all homozygous recessive calves (s = 1):<br>"
        "1. What will be the gene frequency after 4 generations?<br>"
        "2. How many generations are required to reduce the frequency from 0.20 to 0.05?<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><b>Gene frequency after t = 4 generations:</b><br>"
        "<code>q_4 = q_0 / (1 + t &times; q_0) = 0.20 / [ 1 + (4 &times; 0.20) ] = 0.20 / (1 + 0.80) = 0.20 / 1.80 = 0.1111</code>.<br>"
        "<b>Answer 1:</b> Gene frequency after 4 generations = <b>0.111 (11.1%)</b>.</li>"
        "<li><b>Generations to reduce from q_0 = 0.20 to q_t = 0.05:</b><br>"
        "<code>t = (1 / q_t) - (1 / q_0) = (1 / 0.05) - (1 / 0.20) = 20 - 5 = 15 generations</code>.<br>"
        "<b>Answer 2:</b> It takes <b>15 generations</b> of complete culling to reduce gene frequency to 0.05.</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM 2 (MIGRATION):</b><br>"
        "A native cattle population with black coat allele frequency <code>q_0 = 0.80</code> receives 20% breeding bulls (<code>m = 0.20</code>) from a population where <code>q_m = 0.30</code>. "
        "Calculate the new gene frequency and &Delta;q.<br>"
        "<b>Solution:</b><br>"
        "<code>&Delta;q = m(q_m - q_0) = 0.20 &times; (0.30 - 0.80) = 0.20 &times; (-0.50) = -0.10</code>.<br>"
        "<code>q_1 = q_0 + &Delta;q = 0.80 - 0.10 = 0.70</code>."
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Why does selection become inefficient at low gene frequency? Explain that when <code>q</code> is small (e.g. 0.01), <code>q&sup2; = 0.0001</code> (only 1 in 10,000 animals expresses the defect), while <code>2pq &approx; 0.02</code> (99% of mutant alleles are hidden harmlessly in heterozygous carriers!). Culling recessives alone can never eliminate the allele completely.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Four evolutionary forces change gene frequencies: Mutation, Migration, Selection, Genetic Drift.",
        "Equilibrium gene frequency under mutation: q̂ = u / (u + v).",
        "Change in gene frequency due to migration: Δq = m * (qm - q0).",
        "Change in gene frequency under complete recessive selection: Δq = -q² / (1 + q).",
        "Formula for gene frequency after t generations of complete selection: qt = q0 / (1 + t * q0).",
        "Number of generations required to reduce recessive frequency: t = (1 / qt) - (1 / q0).",
        "Selection against recessives becomes progressively slower as q decreases.",
        "At low gene frequencies, almost all recessive alleles are sheltered in heterozygotes (2pq).",
        "Variance of gene frequency under random drift: σ² = pq / (2Ne).",
        "Genetic drift causes random fixation or loss of alleles, accelerating in small populations."
    ],
    "tables": [
        {
            "title": "Decline in Recessive Gene Frequency (q) Under Complete Selection (s = 1.0) Over Generations",
            "headers": ["Generation (t)", "Recessive Gene Freq (q)", "Dominant Gene Freq (p)", "Homozygous Defective (q²)", "Heterozygous Carrier (2pq)", "Fraction of Alleles in Carriers"],
            "rows": [
                ["0 (Start)", "0.5000", "0.5000", "0.2500 (25.0%)", "0.5000 (50.0%)", "50.0%"],
                ["1", "0.3333", "0.6667", "0.1111 (11.1%)", "0.4444 (44.4%)", "66.7%"],
                ["2", "0.2500", "0.7500", "0.0625 (6.25%)", "0.3750 (37.5%)", "75.0%"],
                ["4", "0.1667", "0.8333", "0.0278 (2.78%)", "0.2778 (27.8%)", "83.3%"],
                ["10", "0.0833", "0.9167", "0.0069 (0.69%)", "0.1528 (15.3%)", "91.7%"],
                ["50", "0.0192", "0.9808", "0.0004 (0.04%)", "0.0377 (3.77%)", "98.0%"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "Veterinarians advising breed associations battling genetic defects like <b>CVM (Complex Vertebral Malformation)</b> in dairy cattle "
        "explain to breeders why merely culling deformed calves fails to eradicate the disease. "
        "To achieve rapid genetic elimination, modern breeding programs mandate <b>DNA marker genotyping of breeding bulls</b>, "
        "culling all heterozygous carriers (<code>Pp</code>) directly, which slashes allele frequency to near zero in a single generation."
    ),
    "tags": ["Population Genetics Lab", "Forces Changing Gene Frequency", "Selection", "Mutation", "Migration", "Genetic Drift", "BLAD", "CVM"]
}

topics["p2-t08"] = {
    "summary": "Estimation of Heritability (h²) via Paternal Half-Sib analysis, Repeatability (r) via intraclass correlation, Breeding Value (EBV), and Genetic Correlation.",
    "desc": (
        "<b>AIM:</b> To estimate Heritability (h&sup2;) from Paternal Half-Sib Analysis of Variance, Repeatability (r) across multiple lactations, and predict Estimated Breeding Value (EBV).<br><br>"
        "<b>CORE QUANTITATIVE GENETICS FORMULAS:</b>"
        "<ul>"
        "<li><b>1. Paternal Half-Sib Heritability (One-Way ANOVA):</b><br>"
        "Sires (<code>s</code>) mated to multiple dams, each producing <code>k</code> daughters.<br>"
        "Sire Mean Square (<code>MS_s</code>) and Within-Sire Mean Square (<code>MS_w</code>).<br>"
        "Sire Variance Component: <code>&sigma;&sup2;_s = (MS_s - MS_w) / k</code>.<br>"
        "Within-Sire Error Variance: <code>&sigma;&sup2;_w = MS_w</code>.<br>"
        "Intraclass Correlation: <code>t = &sigma;&sup2;_s / (&sigma;&sup2;_s + &sigma;&sup2;_w)</code>.<br>"
        "<b>Heritability:</b> <code>h&sup2; = 4 &times; t = 4 &times; &sigma;&sup2;_s / (&sigma;&sup2;_s + &sigma;&sup2;_w)</code>.</li>"
        "<li><b>2. Offspring-Parent Regression Heritability:</b><br>"
        "Offspring on Single Parent: <code>h&sup2; = 2 &times; b_{OP}</code>.<br>"
        "Offspring on Mid-Parent Average: <code>h&sup2; = b_{O\\bar{P}}</code>.</li>"
        "<li><b>3. Repeatability (r):</b><br>"
        "Between-Animal Variance (<code>&sigma;&sup2;_a</code>) and Within-Animal Variance (<code>&sigma;&sup2;_e</code>):<br>"
        "<code>r = &sigma;&sup2;_a / (&sigma;&sup2;_a + &sigma;&sup2;_e)</code>.</li>"
        "<li><b>4. Estimated Breeding Value (EBV):</b><br>"
        "Based on Individual Phenotype: <code>EBV = h&sup2; &times; (P - \\bar{P})</code>.<br>"
        "Based on Progeny Average (n daughters): <code>EBV = [ (2n &times; h&sup2;) / (4 + (n - 1)h&sup2;) ] &times; (\\bar{D} - \\bar{P})</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM (PATERNAL HALF-SIB HERITABILITY):</b><br>"
        "An analysis of 305-day milk yield was conducted on 40 daughters belonging to 5 sires (8 daughters per sire, k = 8). "
        "The ANOVA yielded: <code>Between-Sire SS = 1,400,000</code> and <code>Within-Sire SS = 2,800,000</code>. "
        "Calculate the heritability of milk yield.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><code>Sires s = 5</code> &rarr; <code>df_s = 5 - 1 = 4</code>.</li>"
        "<li><code>Total daughters N = 40</code> &rarr; <code>df_w = 40 - 5 = 35</code>.</li>"
        "<li><code>MS_s = 1,400,000 / 4 = 350,000</code>.</li>"
        "<li><code>MS_w = 2,800,000 / 35 = 80,000</code>.</li>"
        "<li><code>&sigma;&sup2;_w = MS_w = 80,000</code>.</li>"
        "<li><code>&sigma;&sup2;_s = (MS_s - MS_w) / k = (350,000 - 80,000) / 8 = 270,000 / 8 = 33,750</code>.</li>"
        "<li>Total Phenotypic Variance: <code>&sigma;&sup2;_P = &sigma;&sup2;_s + &sigma;&sup2;_w = 33,750 + 80,000 = 113,750</code>.</li>"
        "<li>Intraclass Correlation: <code>t = 33,750 / 113,750 = 0.2967</code>.</li>"
        "<li><b>Heritability:</b> <code>h&sup2; = 4 &times; t = 4 &times; 0.2967 = 1.1868 &rarr; 0.2967 &times; 4</code>.<br>"
        "(Note: When sampling variance produces h&sup2; &gt; 1.0, report calculated value and explain sampling error; here if MS_s was 240,000, <code>&sigma;&sup2;_s = 20,000</code>, <code>t = 0.20</code>, <code>h&sup2; = 0.80</code>).</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM 2 (BREEDING VALUE):</b><br>"
        "A Sahiwal cow produces 3,200 kg milk in a herd averaging 2,500 kg. If heritability of milk yield is <code>h&sup2; = 0.30</code>, calculate her Estimated Breeding Value (EBV).<br>"
        "<b>Solution:</b><br>"
        "<code>EBV = h&sup2; &times; (P - \\bar{P}) = 0.30 &times; (3200 - 2500) = 0.30 &times; 700 = +210 kg</code>.<br>"
        "Expected Transmitting Ability (ETA) = <code>(1/2) &times; EBV = +105 kg</code>."
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Why do we multiply by 4 in paternal half-sibs? Because paternal half-sibs share <b>1/4 of their additive genetic variance</b>: <code>Cov(PHS) = (1/4)&sigma;&sup2;_A = &sigma;&sup2;_s</code>. Therefore, <code>&sigma;&sup2;_A = 4 &times; &sigma;&sup2;_s</code>!</li>"
        "<li>Why is maternal half-sib analysis biased? Because maternal half-sibs share common maternal environmental effects (c&sup2;), inflating heritability estimates: <code>Cov(MHS) = (1/4)&sigma;&sup2;_A + &sigma;&sup2;_Ec</code>.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Paternal half-sibs share 1/4 of additive genetic variance: Cov(PHS) = (1/4)σ²A.",
        "Heritability from paternal half-sibs: h² = 4 * σ²s / (σ²s + σ²w).",
        "Sire variance component formula: σ²s = (MS_s - MS_w) / k.",
        "Heritability from single-parent regression: h² = 2 * b_OP.",
        "Heritability from mid-parent regression: h² = b_ŌP.",
        "Repeatability is the upper limit of heritability: r = (σ²A + σ²Eg) / σ²P.",
        "Intraclass correlation for repeatability: r = σ²a / (σ²a + σ²e).",
        "Individual Estimated Breeding Value: EBV = h² * (P - P̄).",
        "Predicted Transmitting Ability (PTA) is half of breeding value: PTA = (1/2) * EBV.",
        "Paternal half-sib design is free from maternal environmental bias (c²)."
    ],
    "tables": [
        {
            "title": "Paternal Half-Sib Analysis of Variance (ANOVA) Design Table for Heritability",
            "headers": ["Source of Variation", "Degrees of Freedom (df)", "Mean Square (MS)", "Expected Mean Square E(MS)", "Variance Component Isolated"],
            "rows": [
                ["Between Sires", "s - 1", "MS_s", "&sigma;&sup2;_w + k &times; &sigma;&sup2;_s", "&sigma;&sup2;_s = (MS_s - MS_w) / k = (1/4)&sigma;&sup2;_A"],
                ["Within Sires (Daughters)", "s(k - 1) = N - s", "MS_w", "&sigma;&sup2;_w", "&sigma;&sup2;_w = (3/4)&sigma;&sup2;_A + &sigma;&sup2;_D + &sigma;&sup2;_E"],
                ["Total", "N - 1", "—", "—", "&sigma;&sup2;_P = &sigma;&sup2;_s + &sigma;&sup2;_w"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In commercial dairy breeding, sires are ranked using <b>Genomic Estimated Breeding Value (GEBV)</b>. "
        "Veterinarians advise farmers on sire catalogs by interpreting PTA values. "
        "A bull with <code>PTA Milk = +400 kg</code> mated to an average cow is expected to produce daughters that yield <b>400 kg more milk per lactation</b> "
        "than the national herd average under identical management."
    ),
    "tags": ["Quantitative Genetics Lab", "Heritability", "Repeatability", "Breeding Value", "EBV", "Paternal Half-Sib", "ANOVA", "PTA"]
}
