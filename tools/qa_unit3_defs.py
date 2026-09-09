# -*- coding: utf-8 -*-
"""
Unit 3: 12 Two-Mark Definitions (u3-q01 to u3-q12)
Animal Breeding Principles, Selection, Mating Systems & Improvement (VCI MSVE 2016 Standard)
"""

questions = [
    {
        "id": "u3-q01",
        "type": "define",
        "marks": 2,
        "question": "Define Selection Differential (S) and state its mathematical formula.",
        "topicId": "u3-t01",
        "answer": (
            "<b>Selection Differential (S):</b><br>"
            "The difference between the average phenotypic value of the selected individuals chosen as breeding parents "
            "(<code>X_bar<sub>s</sub></code>) and the average phenotypic value of the entire unselected parental generation "
            "from which they were selected (<code>X_bar<sub>p</sub></code>):<br>"
            "<code>S = X_bar<sub>s</sub> - X_bar<sub>p</sub></code><br><br>"
            "It measures the phenotypic superiority of the selected parents and is expressed in the actual units of the trait."
        ),
        "keyPoints": [
            "Difference between mean of selected parents and mean of parental population.",
            "Formula: S = X̄_s - X̄_p.",
            "Expressed in actual physical units of measurement (kg milk, grams gain)."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2020", "TANUVAS 2021", "KVASU 2022"]
    },
    {
        "id": "u3-q02",
        "type": "define",
        "marks": 2,
        "question": "Define Selection Intensity (i) and state its relationship with Selection Differential.",
        "topicId": "u3-t01",
        "answer": (
            "<b>Selection Intensity (i):</b><br>"
            "The selection differential expressed in units of standard deviation of the phenotypic trait (standardized selection differential):<br>"
            "<code>i = S / &sigma;<sub>P</sub></code> &rArr; <code>S = i &times; &sigma;<sub>P</sub></code><br><br>"
            "It is a dimensionless quantity that depends strictly on the proportion of animals selected (<code>p</code>) from a normally distributed herd, "
            "obtained as the ordinate height (<code>z</code>) of the standard normal curve divided by <code>p</code>: <code>i = z / p</code>."
        ),
        "keyPoints": [
            "Standardized selection differential: i = S / σ_P.",
            "Dimensionless value depending solely on the proportion selected (p).",
            "Relationship: S = i * σ_P."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["GADVASU 2019", "LUVAS 2021", "MAFSU 2023"]
    },
    {
        "id": "u3-q03",
        "type": "define",
        "marks": 2,
        "question": "Define Generation Interval (L) and cite typical values for cattle, sheep, and poultry.",
        "topicId": "u3-t01",
        "answer": (
            "<b>Generation Interval (L):</b><br>"
            "The average age of the parents when their replacement offspring (which become parents in the next generation) are born.<br>"
            "Mathematically computed as the average of four pathways: <code>L = (L<sub>SS</sub> + L<sub>SD</sub> + L<sub>DS</sub> + L<sub>DD</sub>) / 4</code> "
            "(Sire to Son, Sire to Daughter, Dam to Son, Dam to Daughter).<br><br>"
            "<b>Typical Values in Domestic Animals:</b>"
            "<ul>"
            "<li><b>Dairy Cattle & Buffaloes:</b> 4.5 &ndash; 5.5 years (long interval slows annual genetic gain: <code>&Delta;G/year = R / L</code>).</li>"
            "<li><b>Sheep & Goats:</b> 2.0 &ndash; 3.0 years.</li>"
            "<li><b>Swine:</b> 1.5 &ndash; 2.0 years.</li>"
            "<li><b>Poultry:</b> 1.0 &ndash; 1.2 years (allowing very rapid annual genetic progress).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Average age of parents when replacement offspring are born.",
            "Four reproductive pathways (L_SS, L_SD, L_DS, L_DD).",
            "Values: Cattle 4.5-5.5 yrs, Sheep 2-3 yrs, Poultry ~1 yr.",
            "Inversely proportional to annual genetic response (ΔG/yr = R / L)."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["VCI Annual 2019", "TANUVAS 2021", "DUVASU 2023"]
    },
    {
        "id": "u3-q04",
        "type": "define",
        "marks": 2,
        "question": "Define Inbreeding Coefficient (FX) according to Sewall Wright and Gustave Malécot.",
        "topicId": "u3-t10",
        "answer": (
            "<b>Inbreeding Coefficient (F<sub>X</sub>):</b><br>"
            "<ul>"
            "<li><b>Wright's Definition (1921):</b> The correlation coefficient between the uniting gametes that formed the individual, measuring the relative reduction in heterozygosity compared to a base population.</li>"
            "<li><b>Malécot's Definition (1948):</b> The probability that two homologous alleles at any given autosomal locus in an individual are <b>identical by descent (autozygous)</b>, having been inherited from a common ancestor.</li>"
            "</ul>"
            "<b>Wright's Formula:</b> <code>F<sub>X</sub> = &sum; [ (&frac12;)<sup>n1 + n2 + 1</sup> &times; (1 + F<sub>A</sub>) ]</code>"
        ),
        "keyPoints": [
            "Wright: Correlation between uniting gametes; proportional decrease in heterozygosity.",
            "Malécot: Probability that two alleles at a locus are identical by descent (IBD).",
            "Wright's formula: F_X = Σ [(1/2)^(n1 + n2 + 1) * (1 + F_A)]."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2020", "RAJUVAS 2022", "KVAFSU 2023"]
    },
    {
        "id": "u3-q05",
        "type": "define",
        "marks": 2,
        "question": "Define Coefficient of Relationship (RXY) and state its values for parent-offspring and full-sibs.",
        "topicId": "u3-t10",
        "answer": (
            "<b>Coefficient of Relationship (R<sub>XY</sub>):</b><br>"
            "The measure of the pedigree degree of genetic relationship between two individuals <i>X</i> and <i>Y</i>; "
            "defined as the expected fraction of their genes that are identical by descent (IBD) from one or more common ancestors:<br>"
            "<code>R<sub>XY</sub> = [ &sum; (&frac12;)<sup>n1 + n2</sup> &times; (1 + F<sub>A</sub>) ] / &radic;[ (1 + F<sub>X</sub>)(1 + F<sub>Y</sub>) ]</code><br><br>"
            "<b>Standard Relationship Values in Non-inbred Populations (F = 0):</b>"
            "<ul>"
            "<li><b>Parent & Offspring:</b> <code>R = 0.50 (50%)</code></li>"
            "<li><b>Full-Sibs:</b> <code>R = 0.50 (50%)</code></li>"
            "<li><b>Half-Sibs:</b> <code>R = 0.25 (25%)</code></li>"
            "<li><b>First Cousins:</b> <code>R = 0.125 (12.5%)</code></li>"
            "</ul>"
        ),
        "keyPoints": [
            "Fraction of genes shared between two individuals identical by descent.",
            "Formula: R_XY = Σ [(1/2)^(n1+n2) * (1+F_A)] / sqrt((1+F_X)(1+F_Y)).",
            "Values: Parent-offspring = 0.50, Full-sibs = 0.50, Half-sibs = 0.25."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["GADVASU 2021", "KVASU 2022", "WBUAFS 2023"]
    },
    {
        "id": "u3-q06",
        "type": "define",
        "marks": 2,
        "question": "Define Prepotency and state the genetic basis underlying prepotent sires.",
        "topicId": "u3-t12",
        "answer": (
            "<b>Prepotency:</b><br>"
            "The distinct ability of an individual parent (especially a breeding sire) to stamp its own characteristics "
            "upon its offspring with such uniformity that the progeny closely resemble the parent and each other, "
            "regardless of the genetic constitution of the dams to which it is mated.<br><br>"
            "<b>Genetic Basis:</b>"
            "<ul>"
            "<li>Presence of a high degree of <b>homozygosity for dominant genes</b> controlling the desired traits.</li>"
            "<li>Because the sire is homozygous dominant (<code>AA, BB, CC</code>), all his gametes carry dominant alleles, ensuring dominance over recessive alleles contributed by diverse dams.</li>"
            "<li>Often achieved through deliberate <b>linebreeding</b> to a superior ancestor.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Ability of a sire to transmit traits uniformly to offspring regardless of dam's genotype.",
            "Genetic basis: High homozygosity for dominant favorable alleles.",
            "Produces exceptional uniformity in progeny; promoted by linebreeding."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2019", "TANUVAS 2020", "LUVAS 2022"]
    },
    {
        "id": "u3-q07",
        "type": "define",
        "marks": 2,
        "question": "Define Grading Up and calculate the exotic/superior inheritance in the 4th generation (G4).",
        "topicId": "u3-t15",
        "answer": (
            "<b>Grading Up:</b><br>"
            "A system of continuous outcrossing in which purebred sires of an established, superior breed are mated "
            "successively generation after generation to nondescript, unimproved indigenous scrub females and their female descendants.<br><br>"
            "<b>Inheritance in 4th Generation (G4):</b><br>"
            "The fraction of improved/exotic breed inheritance increases in successive backcross generations according to the formula: <code>1 - (&frac12;)<sup>n</sup></code>.<br>"
            "<ul>"
            "<li>G1 (F1): <code>&frac12; = 50.0%</code> superior inheritance</li>"
            "<li>G2: <code>&frac34; = 75.0%</code> superior inheritance</li>"
            "<li>G3: <code>7/8 = 87.5%</code> superior inheritance</li>"
            "<li><b>G4: <code>15/16 = 93.75%</code> superior inheritance</b></li>"
            "</ul>"
            "By the 5th generation (31/32 or 96.88%), the graded population is practically indistinguishable from the purebred sire breed."
        ),
        "keyPoints": [
            "Mating purebred superior sires to nondescript scrub females over successive generations.",
            "Formula for generation n: 1 - (1/2)^n.",
            "G4 inheritance = 15/16 = 93.75% superior inheritance."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["VCI Annual 2018", "TANUVAS 2021", "KVASU 2023"]
    },
    {
        "id": "u3-q08",
        "type": "define",
        "marks": 2,
        "question": "Define Heterobeltiosis and differentiate it from Mid-Parent Heterosis.",
        "topicId": "u3-t14",
        "answer": (
            "<ul>"
            "<li><b>Heterobeltiosis (Better-Parent Heterosis):</b> The superiority of the crossbred (F1) hybrid over the <i>better (superior) of the two parental purebred lines</i> for a given trait:<br>"
            "<code>Heterobeltiosis (%) = [ (F1 - Better Parent) / Better Parent ] &times; 100</code><br>"
            "<i>Significance:</i> Critical benchmark in commercial breeding; crossbreeding is economically worthwhile only when F1 surpasses the better purebred parent.</li>"
            "<li><b>Mid-Parent Heterosis:</b> The superiority of the F1 hybrid over the <i>arithmetic average of the two parental lines</i>:<br>"
            "<code>Mid-Parent Heterosis (%) = [ (F1 - Mid-Parent) / Mid-Parent ] &times; 100</code></li>"
            "</ul>"
        ),
        "keyPoints": [
            "Heterobeltiosis: Superiority of F1 hybrid over the better parent: [(F1 - BP) / BP] * 100.",
            "Mid-parent heterosis: Superiority of F1 over the mean of both parents: [(F1 - MP) / MP] * 100.",
            "Commercial importance: Validates whether crossbreeding outyields the best pure breed."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2021", "GADVASU 2022", "MAFSU 2023"]
    },
    {
        "id": "u3-q09",
        "type": "define",
        "marks": 2,
        "question": "Distinguish between General Combining Ability (GCA) and Specific Combining Ability (SCA).",
        "topicId": "u3-t14",
        "answer": (
            "<ul>"
            "<li><b>General Combining Ability (GCA):</b> The average performance of a particular inbred line or parent across a wide series of crosses with other lines.<br>"
            "<i>Genetic Basis:</i> Controlled primarily by <b>additive gene action (<code>V<sub>A</sub></code>)</b>.<br>"
            "<i>Breeding Role:</i> Used to identify superior pure lines to be maintained for recurrent selection.</li>"
            "<li><b>Specific Combining Ability (SCA):</b> Cases where certain specific crosses perform significantly better or worse than expected based on the average GCA of the parental lines.<br>"
            "<i>Genetic Basis:</i> Controlled by <b>non-additive gene action (dominance <code>V<sub>D</sub></code> and epistasis <code>V<sub>I</sub></code>)</b>.<br>"
            "<i>Breeding Role:</i> Exploited in commercial terminal 2-way and 4-way poultry and swine crosses.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "GCA: Average crossbred performance across multiple lines; governed by additive gene action (V_A).",
            "SCA: Deviation of a specific cross from GCA expectation; governed by non-additive gene action (V_D + V_I).",
            "GCA used in purebred selection; SCA exploited in hybrid broiler/layer production."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["TANUVAS 2020", "RAJUVAS 2021", "LUVAS 2023"]
    },
    {
        "id": "u3-q10",
        "type": "define",
        "marks": 2,
        "question": "What is Open Nucleus Breeding System (ONBS)? State its main advantage over Closed Nucleus System.",
        "topicId": "u3-t07",
        "answer": (
            "<b>Open Nucleus Breeding System (ONBS):</b><br>"
            "A hierarchical breeding structure comprising a central high-merit <b>Nucleus herd</b> and surrounding commercial <b>Multiplier / Base herds</b>, "
            "where gene flow is <b>bidirectional</b>: superior elite females identified in the base herds are continuously introduced ('screened') into the nucleus, "
            "while elite sires born in the nucleus are disseminated down to the base herds.<br><br>"
            "<b>Main Advantages over Closed Nucleus:</b>"
            "<ul>"
            "<li><b>Controls Inbreeding:</b> Gene inflow from the base expands effective population size, keeping the rate of inbreeding (<code>&Delta;F</code>) significantly lower.</li>"
            "<li><b>Accelerates Genetic Gain:</b> Increases selection intensity by tapping exceptional outlier animals from the large commercial base population.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Hierarchical nucleus-base system with two-way gene flow (upward elite females, downward elite sires).",
            "Overcomes inbreeding depression seen in small closed nucleus herds.",
            "Higher selection intensity by screening superior females from the broad base."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["GADVASU 2020", "IVRI 2022", "KVASU 2023"]
    },
    {
        "id": "u3-q11",
        "type": "define",
        "marks": 2,
        "question": "Define Mean Kinship (MK) and state its role in conservation of endangered livestock breeds.",
        "topicId": "u3-t25",
        "answer": (
            "<b>Mean Kinship (MK):</b><br>"
            "The average coefficient of kinship (kinship coefficient <code>f<sub>ij</sub></code>) between a given individual "
            "and all living members of the current population (including itself):<br>"
            "<code>MK<sub>i</sub> = [ &sum;<sub>j=1</sub><sup>N</sup> f<sub>ij</sub> ] / N</code><br><br>"
            "<b>Role in Conservation Breeding Programs:</b>"
            "<ul>"
            "<li>Measures how genetically representative and closely related an animal is to the entire herd.</li>"
            "<li><b>Selection Criterion:</b> Animals with the <b>lowest Mean Kinship</b> possess the rarest, most unique alleles. Prioritizing low-MK individuals for breeding maximizes retained gene diversity and minimizes long-term inbreeding rates in endangered indigenous breeds (e.g., Punganur cattle, Toda buffalo).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Average kinship coefficient of an individual with all animals in the population: MK_i = (Σ f_ij) / N.",
            "Inverse indicator of genetic uniqueness.",
            "Breeding low-MK animals preserves maximum allelic diversity and minimizes population inbreeding."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["TANUVAS 2021", "KVASU 2022", "DUVASU 2023"]
    },
    {
        "id": "u3-q12",
        "type": "define",
        "marks": 2,
        "question": "Define Effective Population Size (Ne) and state Wright's formula for unequal sex ratios.",
        "topicId": "u3-t25",
        "answer": (
            "<b>Effective Population Size (N<sub>e</sub>):</b><br>"
            "The size of an ideal, panmictic population that would experience the same rate of inbreeding (<code>&Delta;F</code>) "
            "or the same rate of random genetic drift (allelic variance) as the actual census population under study.<br><br>"
            "<b>Wright's Formula for Unequal Number of Breeding Males (N<sub>m</sub>) and Females (N<sub>f</sub>):</b><br>"
            "<b><code>N<sub>e</sub> = (4 &times; N<sub>m</sub> &times; N<sub>f</sub>) / (N<sub>m</sub> + N<sub>f</sub>)</code></b><br><br>"
            "<i>Breeding Implication:</i> Because <code>N<sub>m</sub></code> is very small in artificial insemination programs (e.g., 5 bulls mated to 500 cows), <code>N<sub>e</sub></code> is overwhelmingly constrained by the number of breeding males: <code>N<sub>e</sub> &approx; 4 N<sub>m</sub> = 20</code>, resulting in rapid inbreeding accumulation despite hundreds of cows."
        ),
        "keyPoints": [
            "Size of an idealized population having identical inbreeding rate / drift as the actual population.",
            "Formula: Ne = (4 * N_m * N_f) / (N_m + N_f).",
            "Heavily constrained by the rarer sex (breeding bulls in AI programs)."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2020", "GADVASU 2021", "LUVAS 2022", "KVAFSU 2023"]
    }
]
