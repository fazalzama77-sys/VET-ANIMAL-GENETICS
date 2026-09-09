# -*- coding: utf-8 -*-
"""
Unit 2: 12 Two-Mark Definitions (u2-q01 to u2-q12)
Principles of Animal Genetics & Population Genetics (VCI MSVE 2016 Standard)
"""

questions = [
    {
        "id": "u2-q01",
        "type": "define",
        "marks": 2,
        "question": "State Mendel's Law of Segregation (First Law of Inheritance) and give its physical basis.",
        "topicId": "u2-t01",
        "answer": (
            "<b>Mendel's Law of Segregation (Law of Purity of Gametes):</b><br>"
            "Alleles of a gene exist in pairs within somatic cells of an individual. During gametogenesis (meiosis), "
            "the two alleles segregate from each other cleanly without blending, such that each gamete receives only "
            "one allele of the pair with equal probability (50%).<br><br>"
            "<b>Physical Basis:</b> The disjunction and separation of homologous chromosomes during Anaphase I of meiosis."
        ),
        "keyPoints": [
            "Alleles exist in pairs and separate cleanly during gamete formation without blending.",
            "Each gamete carries only one allele of the pair (purity of gametes).",
            "Cytological basis: Disjunction of homologous chromosomes at Anaphase I."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["TANUVAS 2021", "KVASU 2022", "IVRI 2023"]
    },
    {
        "id": "u2-q02",
        "type": "define",
        "marks": 2,
        "question": "State Mendel's Law of Independent Assortment and state when it fails.",
        "topicId": "u2-t01",
        "answer": (
            "<b>Law of Independent Assortment (Mendel's Second Law):</b><br>"
            "When two or more pairs of independent, non-allelic genes are segregating simultaneously in a cross, "
            "the assortment or distribution of alleles of one gene pair into gametes is entirely independent of the "
            "distribution of alleles of any other gene pair.<br><br>"
            "<b>Condition of Failure:</b> The law fails when genes are located close together on the same chromosome "
            "(i.e., genetically linked genes with complete or partial <b>linkage</b>)."
        ),
        "keyPoints": [
            "Independent distribution of different non-allelic gene pairs into gametes.",
            "Produces standard 9:3:3:1 dihybrid phenotypic ratio.",
            "Fails in presence of genetic linkage (syntenic genes on the same chromosome)."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["GADVASU 2020", "RAJUVAS 2022", "MAFSU 2023"]
    },
    {
        "id": "u2-q03",
        "type": "define",
        "marks": 2,
        "question": "Define Pleiotropy and give one authentic livestock example.",
        "topicId": "u2-t03",
        "answer": (
            "<b>Pleiotropy:</b><br>"
            "A genetic phenomenon wherein a single gene or locus influences multiple, seemingly unrelated phenotypic "
            "traits or organ systems simultaneously.<br><br>"
            "<b>Livestock Example:</b><br>"
            "<ul>"
            "<li><b>Merle gene (M) in Dogs:</b> Causes attractive mottled coat pigmentation, but in homozygous condition (<code>MM</code>) leads to microphthalmia, deafness, and ocular coloboma.</li>"
            "<li><b>Polled gene (P) in Goats:</b> Dominant polledness allele is pleiotropically linked to recessive intersexuality / female pseudohermaphroditism in polled female goats (<code>PP</code>).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Single gene influencing two or more distinct, unrelated phenotypic characteristics.",
            "Example: Polledness-intersexuality syndrome in goats or Merle coat/deafness in canines."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2019", "LUVAS 2021", "KVAFSU 2023"]
    },
    {
        "id": "u2-q04",
        "type": "define",
        "marks": 2,
        "question": "Define Penetrance and Expressivity. Differentiate between complete and incomplete penetrance.",
        "topicId": "u2-t03",
        "answer": (
            "<ul>"
            "<li><b>Penetrance:</b> The percentage of individuals carrying a particular genotype who actually exhibit the corresponding phenotype (all-or-none statistical measure: <code>(Number showing phenotype / Number with genotype) &times; 100</code>). "
            "If less than 100%, it is termed <i>incomplete penetrance</i> (e.g., polydactyly in chickens).</li>"
            "<li><b>Expressivity:</b> The degree or severity to which a penetrant gene is phenotypically expressed in an individual (qualitative/quantitative variation, e.g., variable spotting patterns in Holstein Friesian cattle).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Penetrance: Percentage of genotype carriers showing the phenotype (all-or-none).",
            "Expressivity: Degree/intensity of phenotypic expression in penetrant individuals.",
            "Complete (100%) vs Incomplete (<100%) penetrance."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["TANUVAS 2020", "WBUAFS 2022"]
    },
    {
        "id": "u2-q05",
        "type": "define",
        "marks": 2,
        "question": "What is Dosage Compensation? State Lyon's Hypothesis.",
        "topicId": "u2-t05",
        "answer": (
            "<b>Dosage Compensation:</b> The genetic regulatory mechanism that equalizes the expression of X-linked genes "
            "between homogametic females (<code>XX</code>) having two doses and heterogametic males (<code>XY</code>) having only one dose.<br><br>"
            "<b>Lyon's Hypothesis (Mary Lyon, 1961):</b>"
            "<ul>"
            "<li>In mammalian female somatic cells, one of the two X chromosomes is randomly and permanently inactivated during early embryonic development.</li>"
            "<li>The inactivated X chromosome condenses into dense heterochromatin visible in interphase nuclei as a <b>Barr body</b> (sex chromatin).</li>"
            "<li>Explains calico/tortoiseshell coat patterning in female cats (heterozygous <code>X<sup>B</sup>X<sup>O</sup></code>).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Equalization of X-linked gene product levels between XX females and XY males.",
            "Random, permanent transcriptional inactivation of one X chromosome in female mammalian cells.",
            "Forms Barr body (condensed heterochromatin); causes cellular mosaicism."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["GADVASU 2021", "IVRI 2022", "DUVASU 2023"]
    },
    {
        "id": "u2-q06",
        "type": "define",
        "marks": 2,
        "question": "Define Robertsonian Translocation (Centric Fusion) and cite its clinical impact in cattle.",
        "topicId": "u2-t10",
        "answer": (
            "<b>Robertsonian Translocation (Centric Fusion):</b><br>"
            "A structural chromosomal rearrangement resulting from the whole-arm fusion of two acrocentric chromosomes "
            "at or near their centromeres, producing a single large bi-armed (metacentric or sub-metacentric) chromosome. "
            "The chromosome number is reduced by one (<code>2n - 1</code> in heterozygotes), but the fundamental arm number (NF) remains conserved.<br><br>"
            "<b>Clinical Impact:</b> <b>rob(1;29) translocation</b> in cattle (especially Swedish Red, Simmental, and indigenous breeds) "
            "causes 5–10% embryonic mortality and reduced fertility in heterozygous carriers due to unbalanced gametes formed during meiotic segregation."
        ),
        "keyPoints": [
            "Centric fusion of two acrocentric chromosomes into a single metacentric chromosome.",
            "Reduces diploid chromosome number (2n) while arm number (NF) remains unchanged.",
            "Example: rob(1;29) in cattle leading to repeat breeding and embryonic death."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["TANUVAS 2019", "IVRI 2021", "KVASU 2023"]
    },
    {
        "id": "u2-q07",
        "type": "define",
        "marks": 2,
        "question": "State the Hardy-Weinberg Law and write its mathematical equation for a two-allele locus.",
        "topicId": "u2-t19",
        "answer": (
            "<b>Hardy-Weinberg Law (G.H. Hardy & W. Weinberg, 1908):</b><br>"
            "In a large, randomly mating (panmictic) diploid population, both gene (allele) frequencies and genotypic frequencies "
            "remain constant from generation to generation, in the absence of disturbing evolutionary forces namely mutation, migration, "
            "selection, and random genetic drift.<br><br>"
            "<b>Mathematical Equation:</b><br>"
            "If allele frequencies are <code>p</code> (for allele <i>A</i>) and <code>q</code> (for allele <i>a</i>), where <code>p + q = 1</code>:<br>"
            "<code>p&sup2; (AA) + 2pq (Aa) + q&sup2; (aa) = 1.0</code>"
        ),
        "keyPoints": [
            "Gene and genotypic frequencies remain constant generation after generation.",
            "Assumptions: Large population, panmixia, no mutation, migration, drift, or selection.",
            "Binomial expansion: p² + 2pq + q² = 1 where p + q = 1."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["VCI Annual 2018", "RAJUVAS 2021", "LUVAS 2023"]
    },
    {
        "id": "u2-q08",
        "type": "define",
        "marks": 2,
        "question": "Define Genetic Drift (Sewall Wright Effect) and explain its biological consequences.",
        "topicId": "u2-t21",
        "answer": (
            "<b>Genetic Drift (Sewall Wright Effect):</b><br>"
            "The random fluctuation in allele frequencies from one generation to the next occurring purely by chance "
            "(sampling errors in gamete sampling) in small, finite populations.<br><br>"
            "<b>Biological Consequences:</b>"
            "<ul>"
            "<li>Leads to random fixation (frequency = 1.0) or loss (frequency = 0.0) of alleles independent of their selective advantage.</li>"
            "<li>Reduces genetic variation (heterozygosity) within small isolated herds.</li>"
            "<li>Leads to genetic divergence among isolated sub-populations.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Random changes in allele frequency due to sampling errors in small populations.",
            "Independent of natural or artificial selection.",
            "Results in fixation/loss of alleles and progressive loss of heterozygosity."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["MAFSU 2020", "IVRI 2022", "GADVASU 2023"]
    },
    {
        "id": "u2-q09",
        "type": "define",
        "marks": 2,
        "question": "Define Breeding Value (Additive Genetic Value) and state its relationship to Progeny Difference.",
        "topicId": "u2-t24",
        "answer": (
            "<b>Breeding Value (BV or A):</b><br>"
            "The value of an individual as a genetic parent. Mathematically, it is defined as twice the expected deviation "
            "of an individual's progeny mean from the population mean when mated at random to a representative sample of the population:<br>"
            "<code>BV = 2 &times; (Progeny Mean - Population Mean)</code><br><br>"
            "<b>Relationship to Progeny Difference (Transmitting Ability):</b><br>"
            "A parent transmits only a sample half of its genes (and breeding value) to each offspring through gametes. Hence:<br>"
            "<code>Progeny Difference (PD) = Predicted Transmitting Ability (PTA) = &frac12; BV</code>"
        ),
        "keyPoints": [
            "Value of an individual as a genetic parent judged by progeny performance.",
            "Formula: BV = 2 * (Progeny Mean - Population Mean).",
            "Transmitting Ability (PTA) = 1/2 of Breeding Value."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["TANUVAS 2021", "KVASU 2022", "GADVASU 2023"]
    },
    {
        "id": "u2-q10",
        "type": "define",
        "marks": 2,
        "question": "Define Heritability in Narrow Sense (h²) and Broad Sense (H²).",
        "topicId": "u2-t25",
        "answer": (
            "<ul>"
            "<li><b>Narrow-Sense Heritability (<code>h&sup2;</code>):</b> The proportion of total phenotypic variance (<code>V<sub>P</sub></code>) that is attributable to <i>additive genetic variance</i> (<code>V<sub>A</sub></code>):<br>"
            "<code>h&sup2; = V<sub>A</sub> / V<sub>P</sub> = V<sub>A</sub> / (V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub> + V<sub>E</sub>)</code><br>"
            "<i>Significance:</i> Determines the degree of resemblance between relatives and governs response to mass selection.</li>"
            "<li><b>Broad-Sense Heritability (<code>H&sup2;</code>):</b> The proportion of total phenotypic variance attributable to total genetic variance (<code>V<sub>G</sub></code>):<br>"
            "<code>H&sup2; = V<sub>G</sub> / V<sub>P</sub> = (V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub>) / V<sub>P</sub></code></li>"
            "</ul>"
        ),
        "keyPoints": [
            "Narrow sense: h² = V_A / V_P (ratio of additive genetic variance to phenotypic variance).",
            "Broad sense: H² = V_G / V_P (ratio of total genetic variance to phenotypic variance).",
            "Narrow sense determines response to selection (R = h² * S)."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["VCI Annual 2019", "IVRI 2021", "LUVAS 2022"]
    },
    {
        "id": "u2-q11",
        "type": "define",
        "marks": 2,
        "question": "Define Repeatability (r) and state its mathematical relationship with Heritability.",
        "topicId": "u2-t26",
        "answer": (
            "<b>Repeatability (r):</b><br>"
            "The intraclass correlation coefficient between repeated phenotypic records (e.g., successive lactations, fleece weights, litter sizes) "
            "of the same individual over time or environmental conditions:<br>"
            "<code>r = (V<sub>G</sub> + V<sub>Eg</sub>) / V<sub>P</sub> = (V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub> + V<sub>Eg</sub>) / V<sub>P</sub></code><br>"
            "where <code>V<sub>Eg</sub></code> is permanent environmental variance.<br><br>"
            "<b>Relationship with Heritability:</b><br>"
            "Repeatability includes both total genetic variance and permanent environmental variance. Therefore, repeatability sets the <b>upper mathematical limit of heritability</b>:<br>"
            "<code>r &ge; h&sup2;</code>"
        ),
        "keyPoints": [
            "Correlation between repeated records of the same animal over time/space.",
            "Formula: r = (V_G + V_Eg) / V_P.",
            "Always equal to or greater than heritability (r >= h²)."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["TANUVAS 2020", "RAJUVAS 2022", "KVAFSU 2023"]
    },
    {
        "id": "u2-q12",
        "type": "define",
        "marks": 2,
        "question": "Define Genetic Correlation (rG) and state its physiological causes.",
        "topicId": "u2-t27",
        "answer": (
            "<b>Genetic Correlation (<code>r<sub>G</sub></code>):</b><br>"
            "The measure of linear association between the additive breeding values of two different traits in the same individual:<br>"
            "<code>r<sub>G</sub> = Cov<sub>A(XY)</sub> / &radic;(V<sub>A(X)</sub> &times; V<sub>A(Y)</sub>)</code><br>"
            "Its value ranges from <code>-1.0</code> to <code>+1.0</code>.<br><br>"
            "<b>Physiological Causes:</b>"
            "<ul>"
            "<li><b>Pleiotropy (Primary cause):</b> A single gene simultaneously influencing both traits (e.g., milk yield and butterfat percentage, <code>r<sub>G</sub> &approx; -0.30</code>).</li>"
            "<li><b>Linkage disequilibrium (Transient cause):</b> Genes influencing both traits located closely on the same chromosome; can be broken by crossing over.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Correlation between additive breeding values of two traits.",
            "Formula: r_G = Cov_A(XY) / sqrt(V_A(X) * V_A(Y)).",
            "Primary cause is pleiotropy; secondary transient cause is genetic linkage."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2020", "GADVASU 2022", "WBUAFS 2023"]
    }
]
