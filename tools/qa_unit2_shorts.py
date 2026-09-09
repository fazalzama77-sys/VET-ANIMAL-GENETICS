# -*- coding: utf-8 -*-
"""
Unit 2: 8 Five-Mark Short Answer / Difference Questions (u2-q13 to u2-q20)
Principles of Animal Genetics & Population Genetics (VCI MSVE 2016 Standard)
"""

questions = [
    {
        "id": "u2-q13",
        "type": "diff",
        "marks": 5,
        "question": "Differentiate between Mitosis and Meiosis in farm animals. Discuss the genetic significance of meiosis.",
        "topicId": "u2-t06",
        "answer": (
            "<b>Comparison between Mitosis and Meiosis:</b><br>"
            "Both are fundamental nuclear division processes in domestic animals, but they serve distinct biological purposes.<br><br>"
            "<b>Genetic Significance of Meiosis:</b>"
            "<ul>"
            "<li><b>Conservation of Species Chromosome Number:</b> Halves chromosome number from diploid (<code>2n</code>) to haploid (<code>n</code>), preventing doubling in each generation upon fertilization.</li>"
            "<li><b>Generation of Genetic Variation:</b> Produces novel recombinant gametes through crossing over (chiasma formation in Pachytene) and random independent assortment of maternal and paternal chromosomes in Anaphase I.</li>"
            "<li><b>Physical Basis of Mendelian Genetics:</b> Segregation of alleles corresponds precisely to Anaphase I homologous disjunction.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Site of occurrence: Somatic cells (mitosis) vs germ cells (meiosis).",
            "Divisions & daughter cells: One division / 2 identical diploid cells vs two divisions / 4 diverse haploid cells.",
            "Synapsis & Crossing over: Absent in mitosis; occurs in Pachytene of Meiosis I.",
            "Genetic significance: Maintains constant 2n number across generations and generates new genetic combinations via recombination."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Differences Between Mitosis and Meiosis",
            "headers": ["Feature", "Mitosis (Equational Division)", "Meiosis (Reductional Division)"],
            "rows": [
                ["Site of Occurrence", "Somatic tissues throughout body for growth & repair", "Gonadal germ cells (testes/ovaries) during gametogenesis"],
                ["Number of Nuclear Divisions", "Single equational division", "Two successive divisions (Meiosis I reductional, Meiosis II equational)"],
                ["Daughter Cells Produced", "2 genetically identical diploid (2n) daughter cells", "4 genetically unique haploid (n) gametes"],
                ["Synapsis & Chiasmata", "Completely absent; no pairing of homologues", "Present during Zygotene/Pachytene; crossing over occurs"],
                ["Centromere Division", "Centromeres divide synchronously at Anaphase", "Centromeres do NOT divide at Anaphase I; divide at Anaphase II"],
                ["Biological Role", "Tissue regeneration, asexual cell renewal, growth", "Production of haploid spermatozoa/ova, genetic recombination"]
            ]
        },
        "pyq": ["TANUVAS 2019", "IVRI 2021", "KVASU 2023"]
    },
    {
        "id": "u2-q14",
        "type": "diff",
        "marks": 5,
        "question": "Differentiate between Incomplete Dominance and Codominance with authentic farm animal examples.",
        "topicId": "u2-t02",
        "answer": (
            "<b>Incomplete Dominance vs Codominance:</b><br>"
            "Both represent non-Mendelian allelic interactions where the classic 3:1 phenotypic ratio in F2 is modified into a <b>1:2:1</b> ratio coinciding directly with the genotypic ratio. However, their molecular mechanisms differ fundamentally.<br><br>"
            "<b>Classic Animal Examples:</b>"
            "<ul>"
            "<li><b>Incomplete Dominance (Andalusian Fowl):</b> Cross between pure Black (<code>BB</code>) and Splash White (<code>bb</code>) produces an intermediate Blue phenotype (<code>Bb</code>) due to partial dosage of eumelanin. Selfing <code>Bb &times; Bb</code> yields 1 Black : 2 Blue : 1 Splash White.</li>"
            "<li><b>Codominance (Shorthorn Cattle):</b> Cross between homozygous Red (<code>C<sup>R</sup>C<sup>R</sup></code>) and White (<code>C<sup>W</sup>C<sup>W</sup></code>) produces <b>Roan</b> coat (<code>C<sup>R</sup>C<sup>W</sup></code>). Individual hairs are completely red or completely white intermixed, as both alleles are fully expressed without blending. F2 yields 1 Red : 2 Roan : 1 White.</li>"
            "<li><b>Codominance (Blood Groups):</b> Bovine blood group systems (e.g., A, B, C systems) and human ABO system (<code>I<sup>A</sup>I<sup>B</sup></code> = AB phenotype) where both antigens are simultaneously expressed on erythrocyte membranes.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Incomplete dominance produces an intermediate phenotype (quantitative dosage effect).",
            "Codominance produces simultaneous, distinct expression of both alleles without blending.",
            "Both exhibit 1:2:1 phenotypic and genotypic ratio in F2 generation.",
            "Authentic examples: Blue Andalusian fowl (incomplete) vs Roan Shorthorn cattle / AB blood group (codominance)."
        ],
        "diagram": "",
        "table": {
            "title": "Comparison Between Incomplete Dominance and Codominance",
            "headers": ["Feature", "Incomplete Dominance", "Codominance"],
            "rows": [
                ["Phenotypic Outcome in Heterozygote", "Intermediate phenotype blended between both homozygous parental types", "Both parental phenotypes expressed simultaneously without intermediate blending"],
                ["Gene Product Expression", "Quantitative dosage effect; single active allele produces inadequate enzyme level", "Both alleles produce distinct, fully active functional proteins/antigens"],
                ["F2 Phenotypic Ratio", "1 : 2 : 1 (e.g., 1 Black : 2 Blue : 1 White)", "1 : 2 : 1 (e.g., 1 Red : 2 Roan : 1 White)"],
                ["Microscopic/Cellular Basis", "Uniformly intermediate pigmentation across cells", "Mosaic of distinct red hairs and pure white hairs intermixed"],
                ["Classic Livestock Examples", "Blue Andalusian fowl; sheep ear notch trait", "Roan coat in Shorthorn cattle; erythrocyte blood group antigens"]
            ]
        },
        "pyq": ["GADVASU 2020", "IVRI 2022", "LUVAS 2023"]
    },
    {
        "id": "u2-q15",
        "type": "diff",
        "marks": 5,
        "question": "Distinguish between Sex-Linked, Sex-Limited, and Sex-Influenced Traits with livestock examples.",
        "topicId": "u2-t04",
        "answer": (
            "<b>Comparison of Sex-Related Patterns of Inheritance:</b><br>"
            "Genes showing non-autosomal or sex-differential expression are grouped into three distinct categories based on their chromosomal location and endocrine regulation.<br><br>"
            "<b>Key Examples in Farm Animals:</b>"
            "<ul>"
            "<li><b>Sex-Linked:</b> <i>Barred plumage (B)</i> in poultry located on Z chromosome. Mating non-barred rooster (<code>ZbZb</code>) with barred hen (<code>ZBW</code>) produces barred cockerels (<code>ZBZb</code>) and non-barred pullets (<code>ZbW</code>), allowing 100% accurate commercial day-old chick auto-sexing.</li>"
            "<li><b>Sex-Limited:</b> <i>Milk production</i> in dairy cattle, <i>egg production</i> in layers, and <i>cryptorchidism</i> in stallions/rams. Autosomal genes carried by both sexes but expressed exclusively in one sex due to anatomical/endocrine limits.</li>"
            "<li><b>Sex-Influenced:</b> <i>Horns in Dorset &times; Suffolk sheep</i>. Heterozygote (<code>Hh</code>) is horned in males (testosterone promotes expression) but polled in females (estrogen suppresses expression).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Sex-Linked: Gene located on sex chromosomes (X/Z); exhibits criss-cross inheritance and sex differences in reciprocal crosses.",
            "Sex-Limited: Gene on autosomes; expressed exclusively in one sex due to anatomical/hormonal prerequisites (e.g. milk yield, egg laying).",
            "Sex-Influenced: Gene on autosomes; expressed in both sexes but dominance relationship is reversed by sex hormones (e.g. sheep horns)."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Comparison of Sex-Related Traits",
            "headers": ["Characteristic", "Sex-Linked Traits", "Sex-Limited Traits", "Sex-Influenced Traits"],
            "rows": [
                ["Chromosomal Location", "Located on Sex Chromosomes (X/Z, Y/W)", "Located on Autosomes", "Located on Autosomes"],
                ["Reciprocal Cross Results", "Yield completely different phenotypic distributions in progeny", "Yield identical genotypic distributions in both sexes", "Yield identical genotypic distributions in both sexes"],
                ["Expression in Sexes", "Expressed in both sexes (dosage/criss-cross differences)", "Expressed in ONE sex only (penetrance zero in opposite sex)", "Expressed in BOTH sexes, but with different frequencies/dominance"],
                ["Role of Sex Hormones", "No direct endocrine modulation of allelic dominance", "Hormones provide anatomical/physiological prerequisite for expression", "Testosterone/estrogen alters dominance of heterozygote"],
                ["Livestock Examples", "Barred plumage in fowl (Z-linked); Haemophilia A in dogs", "Milk yield in cattle; egg production in poultry; cryptorchidism", "Horns in sheep (dominant in rams, recessive in ewes); pattern baldness"]
            ]
        },
        "pyq": ["VCI Annual 2019", "TANUVAS 2021", "KVASU 2022"]
    },
    {
        "id": "u2-q16",
        "type": "short",
        "marks": 5,
        "question": "Describe the types of Structural Chromosomal Aberrations and their reproductive consequences in livestock.",
        "topicId": "u2-t10",
        "answer": (
            "<b>Structural Chromosomal Aberrations:</b><br>"
            "Alterations in the physical architecture and linear gene sequence of chromosomes arising from chromosomal breakage followed by abnormal reunion or loss.<br><br>"
            "<b>Four Major Categories:</b>"
            "<ul>"
            "<li><b>1. Deletion (Deficiency):</b> Loss of a chromosomal segment. Can be terminal or interstitial. Leads to loss of vital genes; homozygous deletions are usually lethal, while heterozygous deletions cause phenotypic anomalies and pseudodominance (e.g., Cri-du-chat syndrome).</li>"
            "<li><b>2. Duplication:</b> Presence of an extra chromosomal segment, creating redundant gene copies (e.g., tandem or reverse duplication). Generally less harmful than deletions, but alters gene dosage and can cause embryonic mortality or phenotypic malformations.</li>"
            "<li><b>3. Inversion:</b> A 180&deg; rotation of an internal chromosomal segment following two breaks. Categorized into <b>Paracentric</b> (excluding centromere) and <b>Pericentric</b> (including centromere). Inversion heterozygotes form an <i>inversion loop</i> at pachytene; crossing over within the loop yields dicentric/acentric fragments (paracentric) or duplications/deletions (pericentric), causing gametic sterility (50% reduction in fertility).</li>"
            "<li><b>4. Translocation:</b> Transfer of a chromosomal segment to a non-homologous chromosome. Includes <b>Reciprocal translocation</b> (mutual exchange) and <b>Robertsonian translocation</b> (centric fusion of two acrocentrics). Forms cross-shaped tetravalent figures at meiotic metaphase I, causing unbalanced gametes, repeat breeding, and early embryonic death in dairy cattle (e.g., 1/29 translocation).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Deletion: Loss of chromosome segment; causes pseudodominance and lethality.",
            "Duplication: Extra chromosomal material; disrupts gene dosage.",
            "Inversion: 180° rotation; paracentric (no centromere) vs pericentric (includes centromere); forms inversion loops and subfertility.",
            "Translocation: Exchange between non-homologous chromosomes; forms tetravalents and unbalanced gametes."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2020", "GADVASU 2022", "MAFSU 2023"]
    },
    {
        "id": "u2-q17",
        "type": "short",
        "marks": 5,
        "question": "Explain the Gene Counting Method and Square Root Method for estimating allele frequencies in animal populations with numerical illustrations.",
        "topicId": "u2-t18",
        "answer": (
            "<b>Methods of Estimating Allele Frequencies:</b><br><br>"
            "<b>1. Gene Counting Method (Direct Counting):</b><br>"
            "Applicable when all genotypes can be phenotypically identified (e.g., codominance or incomplete dominance).<br>"
            "For a population of size <code>N</code> with numbers <code>D</code> (AA), <code>H</code> (Aa), and <code>R</code> (aa):<br>"
            "Total alleles = <code>2N = 2(D + H + R)</code>.<br>"
            "<code>p (freq of A) = (2D + H) / (2N) = P + &frac12; H</code><br>"
            "<code>q (freq of a) = (2R + H) / (2N) = Q + &frac12; H</code><br>"
            "<i>Illustration:</i> In 100 Shorthorn cattle: 49 Red (CRCR), 42 Roan (CRCW), 9 White (CWCW).<br>"
            "<code>p (C<sup>R</sup>) = (2 &times; 49 + 42) / 200 = 140 / 200 = 0.70</code><br>"
            "<code>q (C<sup>W</sup>) = (2 &times; 9 + 42) / 200 = 60 / 200 = 0.30</code> (Check: 0.70 + 0.30 = 1.0).<br><br>"
            "<b>2. Square Root Method:</b><br>"
            "Applicable when one allele shows complete dominance over another (heterozygotes Aa indistinguishable from homozygotes AA). Assumes population is in Hardy-Weinberg equilibrium.<br>"
            "Recessive homozygotes (aa) represent <code>q&sup2;</code>.<br>"
            "<code>q = &radic;(Number of recessive individuals / Total population N)</code><br>"
            "<code>p = 1 - q</code><br>"
            "<i>Illustration:</i> In 200 Black Angus cattle, 18 red calves (recessive bb) are born.<br>"
            "<code>q&sup2; = 18 / 200 = 0.09 &rArr; q (freq of b) = &radic;0.09 = 0.30</code><br>"
            "<code>p (freq of B) = 1 - 0.30 = 0.70</code><br>"
            "Carrier frequency (Bb) = <code>2pq = 2 &times; 0.70 &times; 0.30 = 0.42 (42%)</code>."
        ),
        "keyPoints": [
            "Gene Counting: For codominant loci where all genotypes are distinct; p = (2D + H) / 2N.",
            "Square Root: For complete dominance assuming HWE; q = sqrt(R / N), p = 1 - q.",
            "Carrier frequency estimation: 2pq = 2 * p * q.",
            "Formulas and step-by-step numerical examples included."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["TANUVAS 2021", "KVASU 2022", "LUVAS 2023"]
    },
    {
        "id": "u2-q18",
        "type": "short",
        "marks": 5,
        "question": "Explain the principle and steps of Polymerase Chain Reaction (PCR). Describe its application in screening breeding bulls for BLAD and CVM.",
        "topicId": "u2-t15",
        "answer": (
            "<b>Polymerase Chain Reaction (PCR - Kary Mullis, 1983):</b><br>"
            "An in vitro molecular technique for the enzymatic amplification of a specific target DNA sequence by several million-fold through repeated thermal cycles.<br><br>"
            "<b>Three Fundamental Thermal Steps in Each Cycle:</b>"
            "<ul>"
            "<li><b>1. Denaturation (94&ndash;95&deg;C, 30&ndash;60s):</b> High temperature disrupts hydrogen bonds between complementary bases, separating double-stranded DNA into single template strands.</li>"
            "<li><b>2. Primer Annealing (50&ndash;65&deg;C, 30&ndash;60s):</b> Sequence-specific forward and reverse oligonucleotide primers bind to complementary regions flanking the target sequence.</li>"
            "<li><b>3. Primer Extension (72&deg;C, 1 min/kb):</b> Thermostable <i>Taq</i> DNA polymerase synthesizes nascent complementary DNA strands using dNTPs in the 5'&rarr;3' direction.</li>"
            "</ul>"
            "<b>Application in Sire Screening for Lethal Recessive Genetic Defects:</b>"
            "<ul>"
            "<li><b>Bovine Leukocyte Adhesion Deficiency (BLAD):</b> A fatal autosomal recessive disease in Holstein cattle caused by an A&rarr;G point mutation at position 383 of the CD18 gene (aspartic acid &rarr; glycine substitution), abolishing a <i>TaqI</i> restriction site. PCR-RFLP accurately detects heterozygous carrier sires (normal <code>TL</code> vs carrier <code>BL</code>), preventing the spread of lethal alleles via semen distribution.</li>"
            "<li><b>Complex Vertebral Malformation (CVM):</b> Lethal defect caused by a G&rarr;T mutation in the SLC35A3 gene in Holsteins; diagnosed via PCR-RFLP or allele-specific PCR to certify artificial insemination (AI) sires as disease-free (<code>TV</code>).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "PCR principle: In vitro exponential DNA amplification using Taq polymerase and thermal cycling.",
            "3 steps: Denaturation (94-95°C), Annealing (50-65°C), Extension (72°C).",
            "Screening of breeding bulls: BLAD (CD18 point mutation) and CVM (SLC35A3 mutation) via PCR-RFLP.",
            "Prevents dissemination of lethal alleles across thousands of daughters via AI."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2021", "GADVASU 2022", "KVAFSU 2023"]
    },
    {
        "id": "u2-q19",
        "type": "short",
        "marks": 5,
        "question": "Explain the partitioning of Phenotypic Variance into its genetic and environmental components. What is the significance of Additive Genetic Variance?",
        "topicId": "u2-t24",
        "answer": (
            "<b>Partitioning of Phenotypic Variance (V<sub>P</sub>):</b><br>"
            "In quantitative genetics, the observed total variance in a polygenic metric trait (<code>V<sub>P</sub></code>) is partitioned into underlying causal components according to Falconer's model:<br>"
            "<code>V<sub>P</sub> = V<sub>G</sub> + V<sub>E</sub> + V<sub>GE</sub> + 2 Cov<sub>GE</sub></code><br>"
            "Assuming random distribution of genotypes across environments (<code>Cov<sub>GE</sub> = 0</code> and negligible <code>V<sub>GE</sub></code>):<br>"
            "<code>V<sub>P</sub> = V<sub>G</sub> + V<sub>E</sub></code><br><br>"
            "<b>Sub-partitioning of Genetic Variance (V<sub>G</sub>):</b>"
            "<ul>"
            "<li><b>Additive Genetic Variance (<code>V<sub>A</sub></code>):</b> Variance due to average additive effects of individual genes across loci. Transmissible directly from parents to offspring.</li>"
            "<li><b>Dominance Variance (<code>V<sub>D</sub></code>):</b> Variance due to non-additive intra-locus allelic interactions (masking/dominance). Broken up during meiosis; cannot be fixed by pure breeding.</li>"
            "<li><b>Epistatic / Interaction Variance (<code>V<sub>I</sub></code>):</b> Variance due to non-additive inter-locus gene interactions (<code>V<sub>AA</sub> + V<sub>AD</sub> + V<sub>DD</sub></code>).</li>"
            "</ul>"
            "<b>Sub-partitioning of Environmental Variance (V<sub>E</sub>):</b>"
            "<ul>"
            "<li><b>Permanent Environmental Variance (<code>V<sub>Eg</sub></code>):</b> Non-genetic factors affecting all records of an animal (e.g., calfhood mastitis permanently damaging an udder quarter).</li>"
            "<li><b>Temporary Environmental Variance (<code>V<sub>Es</sub></code>):</b> Transient factors affecting only a single measurement (e.g., daily feeding, ambient temperature).</li>"
            "</ul>"
            "<code>V<sub>P</sub> = V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub> + V<sub>Eg</sub> + V<sub>Es</sub></code><br><br>"
            "<b>Crucial Significance of Additive Genetic Variance (V<sub>A</sub>):</b><br>"
            "<code>V<sub>A</sub></code> is the chief genetic determinant of narrow-sense heritability (<code>h&sup2; = V<sub>A</sub>/V<sub>P</sub></code>) and governs the response to mass selection (<code>R = h&sup2;S</code>). It represents permanent, cumulative genetic progress."
        ),
        "keyPoints": [
            "Full equation: V_P = V_A + V_D + V_I + V_Eg + V_Es.",
            "Genetic components: Additive (V_A), Dominance (V_D), Epistatic (V_I).",
            "Environmental components: Permanent (V_Eg) and Temporary (V_Es).",
            "Significance of V_A: Chief transmissible component from parents to progeny; governs selection response (R = h² * S)."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["VCI Annual 2020", "TANUVAS 2022", "DUVASU 2023"]
    },
    {
        "id": "u2-q20",
        "type": "short",
        "marks": 5,
        "question": "Compare Paternal Half-Sib Correlation and Parent-Offspring Regression methods for estimating Heritability.",
        "topicId": "u2-t25",
        "answer": (
            "<b>Comparison of Heritability Estimation Methods:</b><br>"
            "Heritability is estimated from the degree of phenotypic resemblance between related individuals. The two most common biometrical methods used in livestock populations are Parent-Offspring Regression and Paternal Half-Sib Analysis of Variance (ANOVA).<br><br>"
            "<b>Mathematical Bases:</b>"
            "<ul>"
            "<li><b>Offspring-Parent Regression (<code>b<sub>OP</sub></code>):</b> Covariance between one parent and offspring equals <code>&frac12; V<sub>A</sub></code>. Hence:<br>"
            "<code>h&sup2; = 2 &times; b<sub>OP</sub></code> (single parent), or <code>h&sup2; = b<sub>O(MP)</sub></code> (mid-parent regression). Free from dominance variance.</li>"
            "<li><b>Paternal Half-Sib Correlation (<code>t</code>):</b> Sires are mated randomly to different dams, producing paternal half-sibs. Covariance between half-sibs equals <code>&frac14; V<sub>A</sub> + 1/16 V<sub>AA</sub></code>. Hence:<br>"
            "<code>h&sup2; = 4 &times; t = 4 &times; [&sigma;<sub>s</sub>&sup2; / (&sigma;<sub>s</sub>&sup2; + &sigma;<sub>e</sub>&sup2;)]</code>. Best suited for dairy cattle where bulls have hundreds of daughters across different herds.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Paternal Half-Sib: h² = 4 * t; based on sire variance component in one-way ANOVA.",
            "Offspring-Parent: h² = 2 * b_OP (single parent) or h² = b_O(MP) (mid-parent).",
            "Suitability: Half-sib is ideal for sex-limited traits (milk yield) with AI sires; Parent-offspring requires records on both generations.",
            "Half-sib is free from maternal environmental effects when dams are randomly assigned."
        ],
        "diagram": "",
        "table": {
            "title": "Comparison Between Paternal Half-Sib ANOVA and Parent-Offspring Regression",
            "headers": ["Feature", "Paternal Half-Sib Correlation", "Parent-Offspring Regression"],
            "rows": [
                ["Statistical Model", "One-way ANOVA (Between Sires and Within Sires / Between Progeny)", "Linear Regression (Offspring on Single Parent or Mid-Parent)"],
                ["Heritability Formula", "h² = 4 * t = 4 * [σ_s² / (σ_s² + σ_e²)]", "h² = 2 * b_OP (Single Parent) OR h² = b_O(MP) (Mid-Parent)"],
                ["Genetic Covariance Utilized", "Cov(HS) = 1/4 V_A + 1/16 V_AA", "Cov(OP) = 1/2 V_A + 1/4 V_AA"],
                ["Environmental Bias Risk", "Minimised if dams and herds are randomly assigned to sires", "Risk of maternal environmental correlation if dam-offspring used"],
                ["Application in Livestock", "Standard method for dairy cattle & poultry with large AI sire families", "Applicable for growth traits in sheep/swine/beef cattle where both sexes express trait"],
                ["Sex-Limited Traits", "Highly efficient (evaluates bulls using daughter records)", "Cannot use sire-daughter regression directly for sex-limited traits like milk yield"]
            ]
        },
        "pyq": ["IVRI 2019", "RAJUVAS 2021", "KVASU 2023"]
    }
]
