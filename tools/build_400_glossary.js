// tools/build_400_glossary.js
// Assembles and generates the expanded 400-term glossary for Animal Genetics and Breeding Studio

const fs = require('fs');
const path = require('path');

const GLOSSARY_PATH = path.join(__dirname, '../js/glossary.js');
const REPO_GLOSSARY_PATH = path.join(__dirname, '../repo/js/glossary.js');

// 123 new exam-specific terms (expanding 277 to exactly 400)
const NEW_TERMS = {
    // 1. Biostatistics & Experimental Design (18 new terms -> 70 total)
    "weighted mean": {
        term: "Weighted Arithmetic Mean",
        category: "Biostatistics & Experimental Design",
        def: "An average calculated by giving varying relative importance (weights w_i) to individual observations: X_w = (Σ w_i X_i) / (Σ w_i)."
    },
    "combined mean": {
        term: "Combined (Pooled) Mean",
        category: "Biostatistics & Experimental Design",
        def: "The overall arithmetic mean computed across multiple subgroup samples with sizes n1, n2 and means X1, X2: X_c = (n1 X1 + n2 X2) / (n1 + n2)."
    },
    "trimmed mean": {
        term: "Trimmed Mean",
        category: "Biostatistics & Experimental Design",
        def: "A robust measure of central tendency calculated by discarding a specified percentage (e.g. 5% or 10%) of extreme values from both tails before averaging."
    },
    "variance of mean": {
        term: "Variance of Sample Mean (σ²_x̄)",
        category: "Biostatistics & Experimental Design",
        def: "The variance of the sampling distribution of the mean, equal to the population variance divided by the sample size: σ² / n."
    },
    "bowley skewness": {
        term: "Bowley's Quartile Skewness (S_q)",
        category: "Biostatistics & Experimental Design",
        def: "A non-parametric measure of asymmetry based on quartiles: S_q = (Q3 + Q1 - 2 Q2) / (Q3 - Q1), bounded between -1.0 and +1.0."
    },
    "leptokurtic": {
        term: "Leptokurtic Distribution (β₂ > 3)",
        category: "Biostatistics & Experimental Design",
        def: "A frequency distribution curve that is more peaked and has heavier tails than a normal distribution, with kurtosis coefficient β₂ > 3 (or excess kurtosis γ₂ > 0)."
    },
    "platykurtic": {
        term: "Platykurtic Distribution (β₂ < 3)",
        category: "Biostatistics & Experimental Design",
        def: "A frequency distribution curve that is flatter-topped and has lighter tails than a normal distribution, with kurtosis coefficient β₂ < 3 (or excess kurtosis γ₂ < 0)."
    },
    "mesokurtic": {
        term: "Mesokurtic Distribution (β₂ = 3)",
        category: "Biostatistics & Experimental Design",
        def: "A frequency distribution having normal peakedness and standard bell-shaped curvature, with kurtosis coefficient β₂ = 3 (or excess kurtosis γ₂ = 0)."
    },
    "bayes theorem": {
        term: "Bayes' Theorem",
        category: "Biostatistics & Experimental Design",
        def: "A foundational probability formula for updating the prior probability of an event given new observed evidence: P(A|B) = [P(B|A) · P(A)] / P(B)."
    },
    "conditional probability": {
        term: "Conditional Probability P(A|B)",
        category: "Biostatistics & Experimental Design",
        def: "The probability of event A occurring given that event B has already occurred: P(A|B) = P(A ∩ B) / P(B), where P(B) > 0."
    },
    "spurious correlation": {
        term: "Spurious (Nonsense) Correlation",
        category: "Biostatistics & Experimental Design",
        def: "A mathematical correlation between two biologically unrelated variables that arises purely coincidentally or due to an unmeasured lurking confounding factor."
    },
    "partial correlation": {
        term: "Partial Correlation (r_12.3)",
        category: "Biostatistics & Experimental Design",
        def: "A correlation measuring the net linear association between two variables after statistically holding constant the confounding effect of a third variable."
    },
    "multiple correlation": {
        term: "Multiple Correlation Coefficient (R)",
        category: "Biostatistics & Experimental Design",
        def: "A statistical metric measuring the degree of association between a single dependent variable and the joint combined linear effect of two or more independent variables."
    },
    "principle of least squares": {
        term: "Principle of Least Squares",
        category: "Biostatistics & Experimental Design",
        def: "The mathematical criterion used to fit a best-fitting regression line by minimizing the sum of squared vertical deviations between observed and predicted values (Σ e²)."
    },
    "standard error of estimate": {
        term: "Standard Error of Estimate (s_yx)",
        category: "Biostatistics & Experimental Design",
        def: "A measure of the scatter or dispersion of observed data points around the fitted regression line: s_yx = √[Σ(Y - Ŷ)² / (n - 2)]."
    },
    "sampling frame": {
        term: "Sampling Frame",
        category: "Biostatistics & Experimental Design",
        def: "An exhaustive, numbered directory or master register containing all sampling units in a target livestock population from which a random sample is drawn."
    },
    "critical difference": {
        term: "Critical Difference (CD / LSD)",
        category: "Biostatistics & Experimental Design",
        def: "The minimum difference required between two treatment means in an ANOVA experiment for them to be declared statistically significantly different at a chosen α level."
    },
    "split-plot design": {
        term: "Split-Plot Design",
        category: "Biostatistics & Experimental Design",
        def: "An experimental design for two or more factors where larger plots (main-plots) receive one factor while sub-divisions (sub-plots) receive the second factor with greater precision."
    },

    // 2. Classical & Mendelian Genetics (23 new terms -> 70 total)
    "monohybrid ratio": {
        term: "Monohybrid Ratio (3:1 / 1:2:1)",
        category: "Classical & Mendelian Genetics",
        def: "The Mendelian F2 progeny ratio obtained from crossing heterozygous monohybrids: 3:1 phenotypic ratio and 1:2:1 genotypic ratio."
    },
    "dihybrid ratio": {
        term: "Dihybrid Ratio (9:3:3:1)",
        category: "Classical & Mendelian Genetics",
        def: "The classic Mendelian F2 phenotypic ratio obtained from crossing dihybrids heterozygous at two independently assorting autosomal loci."
    },
    "trihybrid cross": {
        term: "Trihybrid Cross",
        category: "Classical & Mendelian Genetics",
        def: "A genetic mating involving individuals differing at three independent gene pairs, producing 8 gamete types, 64 F2 zygotic combinations, and 27:9:9:9:3:3:3:1 phenotypic classes."
    },
    "punnett square": {
        term: "Punnett Square (Checkerboard)",
        category: "Classical & Mendelian Genetics",
        def: "A graphical grid diagram devised by Reginald Punnett to calculate and visualize all possible combinations of male and female gametes during fertilization."
    },
    "testcross ratio": {
        term: "Testcross Ratio",
        category: "Classical & Mendelian Genetics",
        def: "The diagnostic phenotypic progeny ratio obtained from mating a heterozygote to a homozygous recessive tester (1:1 for monohybrid, 1:1:1:1 for dihybrid)."
    },
    "multiple allelism": {
        term: "Multiple Allelism",
        category: "Classical & Mendelian Genetics",
        def: "The condition where a single gene locus across a population is occupied by three or more alternative mutant allelic forms (e.g. ABO blood groups, rabbit coat colour)."
    },
    "rh factor": {
        term: "Rhesus (Rh) Factor",
        category: "Classical & Mendelian Genetics",
        def: "An erythrocytic surface antigen system governed by autosomal alleles (D/d) responsible for maternal-fetal immunological incompatibility in mammals."
    },
    "erythroblastosis fetalis": {
        term: "Erythroblastosis Fetalis (Hemolytic Disease)",
        category: "Classical & Mendelian Genetics",
        def: "A severe alloimmune hemolytic condition in newborn mammals (including equine neonatal isoerythrolysis) caused by maternal antibodies attacking fetal red blood cells."
    },
    "abo blood groups": {
        term: "ABO Blood Group System (Landsteiner)",
        category: "Classical & Mendelian Genetics",
        def: "The classic multiple allelic system governed by three alleles (I^A, I^B, i) on an autosomal locus exhibiting complete dominance and codominance."
    },
    "self-sterility alleles": {
        term: "Self-Sterility (S) Alleles",
        category: "Classical & Mendelian Genetics",
        def: "A multiple allelic recognition system where pollen or sperm sharing an identical S-allele with the maternal tissue is inhibited from fertilization."
    },
    "modified dihybrid ratio": {
        term: "Modified Dihybrid Ratio",
        category: "Classical & Mendelian Genetics",
        def: "Any departure from the 9:3:3:1 F2 phenotypic ratio resulting from non-allelic gene interactions (such as 9:7, 9:3:4, 12:3:1, 15:1, 13:3, or 9:6:1)."
    },
    "morgan linkage law": {
        term: "Morgan's Law of Linkage",
        category: "Classical & Mendelian Genetics",
        def: "The genetic principle formulated by Thomas Hunt Morgan stating that genes located on the same physical chromosome tend to be inherited together as a linkage unit."
    },
    "complete linkage": {
        term: "Complete Linkage",
        category: "Classical & Mendelian Genetics",
        def: "A condition where two closely positioned genes on the same chromosome are transmitted together 100% of the time without any meiotic crossing over (e.g. male Drosophila)."
    },
    "incomplete linkage": {
        term: "Incomplete Linkage",
        category: "Classical & Mendelian Genetics",
        def: "Linkage between syntenic genes separated by sufficient chromosomal distance that occasional crossing over produces both non-crossover parental and recombinant gametes."
    },
    "coupling phase": {
        term: "Coupling (Cis) Phase",
        category: "Classical & Mendelian Genetics",
        def: "A linkage arrangement where two dominant alleles reside on one homologous chromosome while both corresponding recessive alleles reside on the other (AB / ab)."
    },
    "repulsion phase": {
        term: "Repulsion (Trans) Phase",
        category: "Classical & Mendelian Genetics",
        def: "A linkage arrangement where each homologous chromosome carries one dominant and one recessive allele (Ab / aB)."
    },
    "map unit": {
        term: "Map Unit (m.u.)",
        category: "Classical & Mendelian Genetics",
        def: "A unit of relative distance on a genetic chromosome map corresponding to a recombination frequency of one percent (1% recombination = 1 centiMorgan)."
    },
    "two-point cross": {
        term: "Two-Point Testcross",
        category: "Classical & Mendelian Genetics",
        def: "A genetic testcross involving two linked gene loci to determine their recombination frequency and physical map distance."
    },
    "three-point cross": {
        term: "Three-Point Testcross",
        category: "Classical & Mendelian Genetics",
        def: "A testcross mapping procedure involving three linked loci simultaneously to determine gene order, map distances, and double-crossover interference."
    },
    "double crossover": {
        term: "Double Crossover (DCO)",
        category: "Classical & Mendelian Genetics",
        def: "The simultaneous occurrence of two distinct meiotic crossover events between two flanking genetic markers, restoring the parental arrangement of outer markers."
    },
    "non-sister chromatids": {
        term: "Non-Sister Chromatids",
        category: "Classical & Mendelian Genetics",
        def: "Chromatids belonging to opposite homologous paired chromosomes during meiosis between which molecular chiasma formation and crossing over occur."
    },
    "cistron": {
        term: "Cistron (Benzer)",
        category: "Classical & Mendelian Genetics",
        def: "The elementary functional genetic unit defined by the cis-trans complementation test; equivalent to a nucleotide sequence coding for a single polypeptide chain."
    },
    "muton": {
        term: "Muton (Benzer)",
        category: "Classical & Mendelian Genetics",
        def: "The smallest structural unit of a gene whose alteration or substitution produces a detectable phenotypic mutation; equivalent to a single nucleotide pair."
    },

    // 3. Cytogenetics & Molecular Genetics (18 new terms -> 70 total)
    "kinetochore": {
        term: "Kinetochore",
        category: "Cytogenetics & Molecular Genetics",
        def: "A specialized multi-protein disc assembled at the chromosomal centromere that anchors spindle microtubules during mitotic and meiotic anaphase segregation."
    },
    "centromere": {
        term: "Centromere (Primary Constriction)",
        category: "Cytogenetics & Molecular Genetics",
        def: "The constricted, heterochromatic chromosomal locus holding sister chromatids together that organizes the kinetochore and determines chromosome arm ratio."
    },
    "telomere": {
        term: "Telomere",
        category: "Cytogenetics & Molecular Genetics",
        def: "Specialized repetitive nucleoprotein structures (e.g. TTAGGG in mammals) capping eukaryotic chromosome ends to prevent chromosomal end-to-end fusion and degradation."
    },
    "chromomere": {
        term: "Chromomere",
        category: "Cytogenetics & Molecular Genetics",
        def: "Dense, bead-like structural chromatin condensations distributed linearly along the length of chromosomes, visible during early meiotic prophase (leptotene)."
    },
    "secondary constriction": {
        term: "Secondary Constriction",
        category: "Cytogenetics & Molecular Genetics",
        def: "A chromosomal constriction distinct from the centromere, frequently identifying the Nucleolar Organizer Region (NOR) containing 18S and 28S ribosomal RNA gene repeats."
    },
    "polytene chromosome": {
        term: "Polytene Chromosome (Giant Chromosome)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A multistranded giant chromosome formed by repeated cycles of DNA endoreduplication without cell division in dipteran salivary glands, exhibiting distinct dark bands and puffs."
    },
    "lampbrush chromosome": {
        term: "Lampbrush Chromosome",
        category: "Cytogenetics & Molecular Genetics",
        def: "A massive, highly extended meiotic prophase chromosome found in vertebrate oocytes exhibiting lateral paired loops of actively transcribed nascent RNA."
    },
    "b-chromosome": {
        term: "B-Chromosome (Supernumerary Chromosome)",
        category: "Cytogenetics & Molecular Genetics",
        def: "Extra dispensable chromosomes present in addition to the normal A-chromosome complement that do not pair with standard autosomes during meiosis."
    },
    "lyon hypothesis": {
        term: "Lyon Hypothesis (Lyonization)",
        category: "Cytogenetics & Molecular Genetics",
        def: "The genetic principle formulated by Mary Lyon stating that one of the two X chromosomes in female somatic cells is randomly and stably inactivated early in embryogenesis."
    },
    "pachytene": {
        term: "Pachytene Stage",
        category: "Cytogenetics & Molecular Genetics",
        def: "The third stage of meiotic prophase I where homologous chromosomes are fully synapsed into bivalents and reciprocal crossing over occurs at recombination nodules."
    },
    "zygotene": {
        term: "Zygotene Stage",
        category: "Cytogenetics & Molecular Genetics",
        def: "The second substage of meiotic prophase I characterized by progressive lengthwise pairing (synapsis) of homologous chromosomes via the synaptonemal complex."
    },
    "diplotene": {
        term: "Diplotene Stage",
        category: "Cytogenetics & Molecular Genetics",
        def: "The fourth stage of meiotic prophase I during which synaptonemal complexes dissolve and paired homologous chromosomes remain held together only at chiasmata."
    },
    "ring chromosome": {
        term: "Ring Chromosome",
        category: "Cytogenetics & Molecular Genetics",
        def: "An aberrant circular chromosome formed when terminal deletions occur at both ends of a chromosome followed by fusion of the broken sticky ends."
    },
    "dicentric chromosome": {
        term: "Dicentric Chromosome",
        category: "Cytogenetics & Molecular Genetics",
        def: "An unstable structural chromosome aberration featuring two active centromeres formed by chromosomal translocation or paracentric crossover, causing anaphase bridges."
    },
    "chargaff rules": {
        term: "Chargaff's Rules",
        category: "Cytogenetics & Molecular Genetics",
        def: "The biochemical laws of DNA stating that in double-stranded DNA, the molar ratio of adenine equals thymine (A = T) and guanine equals cytosine (G = C), so Purines = Pyrimidines."
    },
    "wobble hypothesis": {
        term: "Wobble Hypothesis (Crick)",
        category: "Cytogenetics & Molecular Genetics",
        def: "Crick's molecular principle explaining how a single tRNA anticodon can recognize multiple synonymous codons due to flexible non-Watson-Crick base pairing at the 3rd codon base."
    },
    "tata box": {
        term: "TATA Box (Goldberg-Hogness Box)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A conserved core promoter DNA sequence (5'-TATAAA-3') located 25-35 base pairs upstream of the eukaryotic transcription start site that binds TATA-binding protein."
    },
    "crispr-cas9": {
        term: "CRISPR-Cas9",
        category: "Cytogenetics & Molecular Genetics",
        def: "A targeted molecular genome-editing system utilizing a single guide RNA (sgRNA) and Cas9 endonuclease to generate site-specific double-strand DNA breaks for precise livestock transgenesis."
    },

    // 4. Population Genetics (18 new terms -> 50 total)
    "allelic frequency": {
        term: "Allelic (Gene) Frequency",
        category: "Population Genetics",
        def: "The relative proportion or percentage of a specific allele among all alleles at that gene locus in a sexually reproducing Mendelian population (p + q = 1.0)."
    },
    "hardy-weinberg equilibrium equation": {
        term: "Hardy-Weinberg Equilibrium Equation",
        category: "Population Genetics",
        def: "The fundamental algebraic binomial expansion p² + 2pq + q² = 1.0 expressing homozygous and heterozygous genotype frequencies in a large random-mating population."
    },
    "random genetic drift": {
        term: "Random Genetic Drift",
        category: "Population Genetics",
        def: "Stochastic changes in allele frequencies across generations resulting from random sampling error during gametogenesis, operating with high intensity in small herds."
    },
    "island model": {
        term: "Island Model of Migration (Wright)",
        category: "Population Genetics",
        def: "A population genetics migration model where a small isolated sub-population receives random migrant individuals from a large mainland reservoir at rate m."
    },
    "stepping stone model": {
        term: "Stepping Stone Model (Kimura)",
        category: "Population Genetics",
        def: "A spatial population genetic structure where gene flow occurs primarily between immediately adjacent neighboring herds or geographical colonies."
    },
    "mutation-selection balance": {
        term: "Mutation-Selection Balance",
        category: "Population Genetics",
        def: "An equilibrium state where the introduction of a deleterious recessive allele by recurrent mutation (u) is exactly balanced by its removal through natural selection (s): q_hat = √(u / s)."
    },
    "frequency-dependent selection": {
        term: "Frequency-Dependent Selection",
        category: "Population Genetics",
        def: "A mode of natural selection where the evolutionary fitness of a phenotype or genotype depends directly on its relative abundance or rarity within the herd."
    },
    "wright f-statistics": {
        term: "Wright's F-Statistics (Hierarchical Inbreeding)",
        category: "Population Genetics",
        def: "Sewall Wright's partitioned inbreeding indices measuring genetic differentiation across population levels: (1 - F_IT) = (1 - F_IS)(1 - F_ST)."
    },
    "fis": {
        term: "F_IS (Inbreeding Within Subpopulations)",
        category: "Population Genetics",
        def: "The correlation between homologous alleles within individuals relative to their local subpopulation, measuring non-random mating within herds: F_IS = (H_S - H_I) / H_S."
    },
    "fst": {
        term: "F_ST (Genetic Fixation Index)",
        category: "Population Genetics",
        def: "The proportion of total genetic diversity attributable to allele frequency divergence among distinct sub-populations or breeds: F_ST = (H_T - H_S) / H_T."
    },
    "fit": {
        term: "F_IT (Overall Inbreeding Coefficient)",
        category: "Population Genetics",
        def: "The inbreeding coefficient of an individual animal relative to the total undivided metapopulation: F_IT = (H_T - H_I) / H_T."
    },
    "sewall wright effect": {
        term: "Sewall Wright Effect",
        category: "Population Genetics",
        def: "An alternative term for random genetic drift emphasizing how allele frequencies undergo non-directional random fluctuations in small closed livestock populations."
    },
    "prepotency": {
        term: "Prepotency",
        category: "Population Genetics",
        def: "The superior capacity of an inbred homozygous sire to stamp his own phenotypic characteristics uniformly onto all his progeny regardless of the dams' genotypes."
    },
    "microevolution": {
        term: "Microevolution",
        category: "Population Genetics",
        def: "Generational shifts in allele and genotypic frequencies within a closed livestock herd driven by mutation, migration, selection, and random drift."
    },
    "polymorphic locus": {
        term: "Polymorphic Locus",
        category: "Population Genetics",
        def: "A genetic locus where the most common allele has a frequency of less than 0.99 (or 0.95), ensuring multiple alleles persist stably in the population."
    },
    "panmictic index": {
        term: "Panmictic Index (P)",
        category: "Population Genetics",
        def: "The relative degree of heterozygosity preserved in a population compared to expectation under panmixia: P = 1 - F."
    },
    "genetic polymorphism": {
        term: "Genetic Polymorphism (Ford)",
        category: "Population Genetics",
        def: "The simultaneous occurrence in the same population of two or more discontinuous genetic variants at frequencies too high to be maintained by recurrent mutation alone."
    },
    "gametic phase disequilibrium": {
        term: "Gametic Phase (Linkage) Disequilibrium (LD)",
        category: "Population Genetics",
        def: "The non-random association of alleles at two or more different loci in gametes: D = P_AB - (p_A · p_B)."
    },

    // 5. Quantitative Genetics & Inheritance (26 new terms -> 65 total)
    "infinitesimal model": {
        term: "Infinitesimal Model (Fisher 1918)",
        category: "Quantitative Genetics & Inheritance",
        def: "The mathematical assumption that quantitative traits are governed by an infinitely large number of unlinked Mendelian loci each having an infinitesimally small additive effect."
    },
    "continuous variation": {
        term: "Continuous Variation",
        category: "Quantitative Genetics & Inheritance",
        def: "Unbroken phenotypic variation across a numerical scale (such as body weight or lactation milk yield) that cannot be separated into distinct discrete classes."
    },
    "multiple factor hypothesis": {
        term: "Multiple Factor Hypothesis (Nilsson-Ehle)",
        category: "Quantitative Genetics & Inheritance",
        def: "The genetic hypothesis establishing that continuous metric traits are determined by multiple segregating Mendelian genes acting in an additive cumulative manner."
    },
    "liability model": {
        term: "Liability Model (Falconer)",
        category: "Quantitative Genetics & Inheritance",
        def: "Falconer's threshold concept positing an underlying normally distributed continuous liability scale composed of genetic and environmental risk factors."
    },
    "average effect of gene substitution": {
        term: "Average Effect of Gene Substitution (α)",
        category: "Quantitative Genetics & Inheritance",
        def: "The expected phenotypic change in performance when a single allele A2 is randomly substituted by allele A1 at a locus in the population: α = a + d(q - p)."
    },
    "additive genetic variance": {
        term: "Additive Genetic Variance (V_A)",
        category: "Quantitative Genetics & Inheritance",
        def: "The variance of true breeding values among individuals; it is the sole component of genetic variance that determines parent-offspring resemblance and responds to selection."
    },
    "non-additive genetic variance": {
        term: "Non-Additive Genetic Variance (V_NA)",
        category: "Quantitative Genetics & Inheritance",
        def: "The combined portion of genetic variance arising from intra-locus dominance interactions (V_D) and inter-locus epistatic interactions (V_I): V_NA = V_D + V_I."
    },
    "total genetic variance": {
        term: "Total Genetic Variance (V_G)",
        category: "Quantitative Genetics & Inheritance",
        def: "The overall variance attributable to all genetic differences among individuals in a population: V_G = V_A + V_D + V_I."
    },
    "environmental variance": {
        term: "Environmental Variance (V_E)",
        category: "Quantitative Genetics & Inheritance",
        def: "The variance among performance records caused by non-genetic environmental influences, partitioned into permanent (V_Ep) and temporary (V_Et) variance."
    },
    "genotype environment interaction": {
        term: "Genotype × Environment Interaction (V_GE)",
        category: "Quantitative Genetics & Inheritance",
        def: "A statistical interaction where the relative phenotypic ranking or performance difference between genotypes changes when evaluated across different environments."
    },
    "co-heritability": {
        term: "Co-Heritability",
        category: "Quantitative Genetics & Inheritance",
        def: "The ratio of additive genetic covariance between two traits to their total phenotypic covariance: Co-h² = Cov_A(X,Y) / Cov_P(X,Y)."
    },
    "paternal half-sib analysis": {
        term: "Paternal Half-Sib ANOVA",
        category: "Quantitative Genetics & Inheritance",
        def: "A hierarchical analysis of variance estimating sire component of variance (σ²_s = 0.25 V_A) to calculate narrow-sense heritability: h² = 4 σ²_s / (σ²_s + σ²_e)."
    },
    "mid-parent regression": {
        term: "Mid-Parent Regression",
        category: "Quantitative Genetics & Inheritance",
        def: "A biometric technique where progeny performance is regressed on the average of both parents (mid-parent value), with regression slope b equaling narrow-sense heritability h²."
    },
    "dam component of variance": {
        term: "Dam Component of Variance (σ²_d)",
        category: "Quantitative Genetics & Inheritance",
        def: "The variance component between dams mated to the same sire, containing 1/4 V_A + 1/4 V_D + maternal environmental effects."
    },
    "sire component of variance": {
        term: "Sire Component of Variance (σ²_s)",
        category: "Quantitative Genetics & Inheritance",
        def: "The variance component among unrelated sires in a nested half-sib design, representing exactly one-quarter of the additive genetic variance: σ²_s = 0.25 V_A."
    },
    "intra-sire regression": {
        term: "Intra-Sire Regression of Offspring on Dam",
        category: "Quantitative Genetics & Inheritance",
        def: "A regression procedure calculating dam-offspring resemblance within sire families to eliminate confounding environmental herd and sire effects: h² = 2 · b_OD."
    },
    "accuracy of breeding value": {
        term: "Accuracy of Selection (r_TI)",
        category: "Quantitative Genetics & Inheritance",
        def: "The correlation between an animal's true breeding value (T) and its estimated breeding value or selection index (I): r_TI = √[n / (n + (4 - h²) / h²)]."
    },
    "selection differential standardized": {
        term: "Standardized Selection Differential (i)",
        category: "Quantitative Genetics & Inheritance",
        def: "The selection differential expressed in units of phenotypic standard deviation: i = S / σ_P, directly determining selection intensity."
    },
    "selection response": {
        term: "Direct Selection Response (R)",
        category: "Quantitative Genetics & Inheritance",
        def: "The expected genetic change in the population mean per generation resulting from artificial selection: R = h² · S = i · r_TI · σ_A."
    },
    "annual genetic gain": {
        term: "Annual Genetic Gain (ΔG/yr)",
        category: "Quantitative Genetics & Inheritance",
        def: "The expected rate of genetic progress per year, calculated as generation response divided by generation interval: ΔG = (i · r_TI · σ_A) / L."
    },
    "selection intensity factor": {
        term: "Selection Intensity Factor (i)",
        category: "Quantitative Genetics & Inheritance",
        def: "A statistical parameter derived from the truncated normal distribution representing the mean deviation of selected animals in standard units: i = z / p."
    },
    "phenotypic standard deviation": {
        term: "Phenotypic Standard Deviation (σ_P)",
        category: "Quantitative Genetics & Inheritance",
        def: "The positive square root of total phenotypic variance (√V_P), quantifying the observable variation of a metric trait within a herd."
    },
    "additive genetic standard deviation": {
        term: "Additive Genetic Standard Deviation (σ_A)",
        category: "Quantitative Genetics & Inheritance",
        def: "The square root of additive genetic variance (√V_A), representing the standard deviation of true breeding values in the population."
    },
    "genetic covariance": {
        term: "Additive Genetic Covariance (Cov_A)",
        category: "Quantitative Genetics & Inheritance",
        def: "The covariance between the additive genetic values (breeding values) of two distinct metric traits X and Y, arising primarily from pleiotropy."
    },
    "environmental covariance": {
        term: "Environmental Covariance (Cov_E)",
        category: "Quantitative Genetics & Inheritance",
        def: "The covariance between non-genetic environmental deviations affecting two traits simultaneously in the same animal."
    },
    "pleiotropic effect on covariance": {
        term: "Pleiotropic Covariance",
        category: "Quantitative Genetics & Inheritance",
        def: "The biological phenomenon whereby single pleiotropic genes influence two different quantitative traits simultaneously, generating permanent genetic correlation."
    },

    // 6. Animal Breeding & Selection Systems (20 new terms -> 75 total)
    "robert bakewell": {
        term: "Robert Bakewell (1725–1795)",
        category: "Animal Breeding & Selection Systems",
        def: "The 18th-century English agriculturalist widely acknowledged as the founder of systematic animal breeding, who pioneered sire leasing, in-and-in breeding, and Dishley Leicester sheep."
    },
    "jay l lush": {
        term: "Jay L. Lush (1896–1982)",
        category: "Animal Breeding & Selection Systems",
        def: "The distinguished Iowa State geneticist recognized as the father of modern scientific animal breeding, author of 'Animal Breeding Plans' (1937)."
    },
    "sewall wright path coefficient": {
        term: "Wright's Method of Path Coefficients",
        category: "Animal Breeding & Selection Systems",
        def: "Sewall Wright's biometric path-tracing methodology used to trace chains of direct ancestral relationships and calculate coefficients of inbreeding and relationship."
    },
    "full-sib test": {
        term: "Full-Sib Performance Testing",
        category: "Animal Breeding & Selection Systems",
        def: "Evaluating a candidate breeding animal based on the performance records of its full brothers and sisters; particularly utilized for sex-limited and slaughter traits in poultry and pigs."
    },
    "half-sib test": {
        term: "Half-Sib Performance Testing",
        category: "Animal Breeding & Selection Systems",
        def: "Evaluating an individual's genetic merit based on the average performance records of its paternal half-siblings."
    },
    "contemporary herdmate": {
        term: "Contemporary Herdmate Comparison",
        category: "Animal Breeding & Selection Systems",
        def: "A dairy sire evaluation method comparing the lactation records of a bull's daughters against unrelated herdmates freshening in the same herd, year, and season."
    },
    "sire proof": {
        term: "Sire Proof (Daughter Average)",
        category: "Animal Breeding & Selection Systems",
        def: "An official documented evaluation of a breeding bull's transmitting ability based on the validated lactation performance of a minimum number of tested daughters."
    },
    "daughter-dam comparison": {
        term: "Daughter-Dam Comparison",
        category: "Animal Breeding & Selection Systems",
        def: "An early sire evaluation method comparing the average performance of a bull's daughters directly against the records of their respective dams (Equal Parent Index: Sire = 2 Daughter - Dam)."
    },
    "mixed model equations": {
        term: "Henderson's Mixed Model Equations (MME)",
        category: "Animal Breeding & Selection Systems",
        def: "C.R. Henderson's matrix system simultaneously solving for fixed environmental herd-year-season effects (BLUE) and random animal breeding values (BLUP): [X'X X'Z; Z'X Z'Z + A⁻¹(σ²_e/σ²_a)] [b; u] = [X'y; Z'y]."
    },
    "genomic estimated breeding value": {
        term: "Genomic Estimated Breeding Value (GEBV)",
        category: "Animal Breeding & Selection Systems",
        def: "An animal's predicted breeding value calculated directly from dense genome-wide SNP marker genotypes using marker effect weights estimated from a reference population."
    },
    "reference population": {
        term: "Reference (Training) Population",
        category: "Animal Breeding & Selection Systems",
        def: "A large population of fully genotyped and phenotyped animals used in genomic selection to estimate individual SNP marker effects for subsequent prediction in young stock."
    },
    "training population": {
        term: "Genomic Training Population",
        category: "Animal Breeding & Selection Systems",
        def: "The dataset of thousands of progeny-tested sires with verified genotypes and deregressed EBVs used to train genomic statistical prediction models."
    },
    "snp chip": {
        term: "Bovine SNP BeadChip",
        category: "Animal Breeding & Selection Systems",
        def: "A high-density DNA microarray containing tens to hundreds of thousands of single nucleotide polymorphisms (e.g. 50K or 777K chips) used for high-throughput genomic screening."
    },
    "two-way cross": {
        term: "Two-Way (Single) Cross",
        category: "Animal Breeding & Selection Systems",
        def: "The direct commercial crossing of individuals from two distinct purebred breeds (A × B) to produce F1 crossbred progeny expressing 100% individual heterosis."
    },
    "three-way cross": {
        term: "Three-Way Cross",
        category: "Animal Breeding & Selection Systems",
        def: "A crossbreeding system where an F1 crossbred female (A × B) is mated to a purebred sire of a third unrelated breed (C), exploiting both maternal and individual heterosis."
    },
    "four-way cross": {
        term: "Four-Way (Double) Cross",
        category: "Animal Breeding & Selection Systems",
        def: "The mating of two distinct F1 crossbred pairs [(A × B) × (C × D)], widely used in commercial hybrid poultry and pig production to maximize uniformity and hybrid vigor."
    },
    "inter-specific hybridization": {
        term: "Inter-Specific Hybridization",
        category: "Animal Breeding & Selection Systems",
        def: "The mating of animals belonging to two distinct biological species of the same genus, such as cattle (Bos taurus) × yak (Bos grunniens) yielding a female-fertile male-sterile Dzo."
    },
    "maternal heterosis": {
        term: "Maternal Heterosis (h^M)",
        category: "Animal Breeding & Selection Systems",
        def: "The enhanced maternal performance, fertility, and milk production exhibited by an F1 crossbred dam, providing superior maternal environment for her calves."
    },
    "individual heterosis": {
        term: "Individual (Direct) Heterosis (h^I)",
        category: "Animal Breeding & Selection Systems",
        def: "The phenotypic superiority in growth, vigor, and survivability displayed by a crossbred individual compared to the average of its purebred parental breeds."
    },
    "minimum viable population": {
        term: "Minimum Viable Population (MVP)",
        category: "Animal Breeding & Selection Systems",
        def: "The smallest isolated population size of an endangered livestock breed required to ensure a 99% probability of persistence for 1,000 years, preventing inbreeding extinction."
    }
};

function main() {
    console.log('Loading existing js/glossary.js (277 terms)...');
    const originalContent = fs.readFileSync(GLOSSARY_PATH, 'utf8');

    // Parse existing glossary object
    const fn = new Function('window', 'app', originalContent + '; return glossary;');
    const oldGlossary = fn({}, { esc: s => s, icon: s => s });

    const existingTermKeys = Object.keys(oldGlossary.terms);
    console.log(`Loaded ${existingTermKeys.length} existing terms.`);

    const newKeys = Object.keys(NEW_TERMS);
    console.log(`Prepared ${newKeys.length} new terms.`);

    if (newKeys.length !== 123) {
        throw new Error(`Expected exactly 123 new terms, found ${newKeys.length}`);
    }

    // Verify ZERO overlap
    const existingSet = new Set(existingTermKeys.map(k => k.toLowerCase()));
    const overlaps = newKeys.filter(k => existingSet.has(k.toLowerCase()));
    if (overlaps.length > 0) {
        throw new Error(`Found overlapping keys between existing and new: ${overlaps.join(', ')}`);
    }

    // Combine categories
    const mergedCategories = {};
    for (const [catName, keys] of Object.entries(oldGlossary.categories)) {
        mergedCategories[catName] = [...keys];
    }

    for (const [key, data] of Object.entries(NEW_TERMS)) {
        if (!mergedCategories[data.category]) {
            throw new Error(`Unknown category: ${data.category}`);
        }
        mergedCategories[data.category].push(key);
    }

    // Combine terms
    const mergedTerms = { ...oldGlossary.terms, ...NEW_TERMS };
    const totalTermKeys = Object.keys(mergedTerms);
    console.log(`Total merged terms: ${totalTermKeys.length}`);

    if (totalTermKeys.length !== 400) {
        throw new Error(`Expected total 400 terms, found ${totalTermKeys.length}`);
    }

    let totalCategoryKeys = 0;
    console.log('\nCategory breakdown after merge:');
    for (const [cat, keys] of Object.entries(mergedCategories)) {
        console.log(`  ${cat}: ${keys.length} terms`);
        totalCategoryKeys += keys.length;
    }
    if (totalCategoryKeys !== 400) {
        throw new Error(`Expected category total 400, found ${totalCategoryKeys}`);
    }

    // Now construct the pristine JavaScript code
    let jsCode = `// =========================================================
// GLOSSARY — B.V.Sc UG-Level Tooltip Term Dictionary
// Animal Genetics and Breeding Studio
// =========================================================
// Usage: glossary.decorate(rootElement) scans rendered HTML
// inside rootElement and wraps known terms with a hover-tooltip.
// Terms are matched longest-first to avoid partial overlap.
// =========================================================

const glossary = {
    categories: ${JSON.stringify(mergedCategories, null, 8).replace(/^ {8}/gm, '    ')},

    terms: {
`;

    // Write terms with clean formatting
    const termEntries = Object.entries(mergedTerms);
    termEntries.forEach(([key, val], idx) => {
        const isLast = idx === termEntries.length - 1;
        jsCode += `        ${JSON.stringify(key)}: {\n`;
        jsCode += `            term: ${JSON.stringify(val.term)},\n`;
        jsCode += `            category: ${JSON.stringify(val.category)},\n`;
        jsCode += `            def: ${JSON.stringify(val.def)}\n`;
        jsCode += `        }${isLast ? '' : ','}\n`;
    });

    jsCode += `    },

    // Return flat array of all terms for search indexing and library view
    getAll() {
        return Object.keys(this.terms).map(k => ({
            key: k,
            term: this.terms[k].term,
            category: this.terms[k].category,
            def: this.terms[k].def
        }));
    },

    // Sort terms longest first to avoid partial replacements
    _sortedTerms: null,
    getSortedTerms() {
        if (!this._sortedTerms) {
            this._sortedTerms = Object.keys(this.terms).sort((a, b) => b.length - a.length);
        }
        return this._sortedTerms;
    },

    decorate(rootElement) {
        if (!rootElement) return;

        const sorted = this.getSortedTerms();
        const walker = document.createTreeWalker(
            rootElement,
            NodeFilter.SHOW_TEXT,
            {
                acceptNode(node) {
                    if (!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
                    let p = node.parentElement;
                    while (p && p !== rootElement) {
                        const tag = p.tagName.toLowerCase();
                        if (['script', 'style', 'button', 'a', 'input', 'textarea', 'kbd', 'code', 'pre', 'h1', 'h2', 'h3'].includes(tag) ||
                            p.classList.contains('glossary-term') ||
                            p.classList.contains('kicker') ||
                            p.classList.contains('chip')) {
                            return NodeFilter.FILTER_REJECT;
                        }
                        p = p.parentElement;
                    }
                    return NodeFilter.FILTER_ACCEPT;
                }
            }
        );

        const textNodes = [];
        let curr;
        while (curr = walker.nextNode()) textNodes.push(curr);

        textNodes.forEach(node => {
            const original = node.nodeValue;
            let replaced = false;

            for (const key of sorted) {
                const escaped = key.replace(/[-\\/\\\\^$*+?.()|[\\]{}]/g, '\\\\$&');
                const regex = new RegExp(\`\\\\b(\${escaped})\\\\b\`, 'i');
                const match = regex.exec(node.nodeValue);

                if (match) {
                    const span = document.createElement('span');
                    const before = node.nodeValue.substring(0, match.index);
                    const matchedText = match[0];
                    const after = node.nodeValue.substring(match.index + matchedText.length);

                    span.innerHTML = \`\${app.esc(before)}<span class="glossary-term" data-term="\${key}" tabindex="0" role="button" aria-label="Definition for \${app.esc(matchedText)}">\${app.esc(matchedText)}</span>\${app.esc(after)}\`;

                    node.parentNode.replaceChild(span, node);
                    replaced = true;
                    break;
                }
            }
        });

        this.attachTooltips(rootElement);
    },

    attachTooltips(root) {
        let activeTooltip = null;

        const removeTooltip = () => {
            if (activeTooltip) {
                activeTooltip.remove();
                activeTooltip = null;
            }
        };

        root.querySelectorAll('.glossary-term').forEach(el => {
            el.addEventListener('mouseenter', (e) => {
                const key = el.dataset.term;
                const data = glossary.terms[key];
                if (!data) return;

                removeTooltip();

                const tip = document.createElement('div');
                tip.className = 'glossary-tooltip';
                tip.innerHTML = \`
                    <div class="glossary-tooltip-head">
                        <span class="glossary-tooltip-title">\${app.esc(data.term)}</span>
                        <span class="glossary-tooltip-badge">\${app.esc(data.category)}</span>
                    </div>
                    <div class="glossary-tooltip-body">\${app.esc(data.def)}</div>
                    <div class="glossary-tooltip-foot">
                        <button class="glossary-speak-btn" type="button" aria-label="Listen to pronunciation">
                            \${app.icon('speaker', 'ico--sm')} Listen
                        </button>
                        <span class="glossary-tooltip-hint">Click for dictionary</span>
                    </div>
                \`;

                document.body.appendChild(tip);
                activeTooltip = tip;

                const rect = el.getBoundingClientRect();
                const tipRect = tip.getBoundingClientRect();

                let top = rect.top - tipRect.height - 8;
                let left = rect.left + (rect.width / 2) - (tipRect.width / 2);

                if (top < 10) top = rect.bottom + 8;
                if (left < 10) left = 10;
                if (left + tipRect.width > window.innerWidth - 10) {
                    left = window.innerWidth - tipRect.width - 10;
                }

                tip.style.top = \`\${top + window.scrollY}px\`;
                tip.style.left = \`\${left}px\`;
                tip.classList.add('is-visible');

                tip.querySelector('.glossary-speak-btn').addEventListener('click', (ev) => {
                    ev.stopPropagation();
                    glossary.speak(data.term);
                });
            });

            el.addEventListener('mouseleave', () => {
                setTimeout(() => {
                    if (activeTooltip && !activeTooltip.matches(':hover')) {
                        removeTooltip();
                    }
                }, 150);
            });

            el.addEventListener('click', () => {
                removeTooltip();
                location.hash = \`#/library/glossary?q=\${encodeURIComponent(el.dataset.term)}\`;
            });
        });

        document.addEventListener('mouseover', (e) => {
            if (activeTooltip && !e.target.closest('.glossary-tooltip') && !e.target.closest('.glossary-term')) {
                removeTooltip();
            }
        });
    },

    speak(word) {
        if (!('speechSynthesis' in window)) return;
        window.speechSynthesis.cancel();
        const utter = new SpeechSynthesisUtterance(word);
        utter.rate = 0.9;
        utter.lang = 'en-GB';
        window.speechSynthesis.speak(utter);
    },

    renderGlossaryPage(container, selectedCategory = 'all', searchQuery = '') {
        const categories = Object.keys(this.categories);
        let activeCat = selectedCategory;
        let query = (searchQuery || '').toLowerCase().trim();

        const render = () => {
            let filteredKeys = Object.keys(this.terms);

            if (activeCat !== 'all') {
                const catTerms = this.categories[activeCat] || [];
                filteredKeys = filteredKeys.filter(k => catTerms.includes(k));
            }

            if (query) {
                filteredKeys = filteredKeys.filter(k => {
                    const t = this.terms[k];
                    return t.term.toLowerCase().includes(query) ||
                           t.def.toLowerCase().includes(query) ||
                           t.category.toLowerCase().includes(query);
                });
            }

            filteredKeys.sort((a, b) => this.terms[a].term.localeCompare(this.terms[b].term));

            container.innerHTML = \`
                <div class="glossary-view">
                    <div class="card-hero mb-4">
                        <div class="card-hero__content">
                            <span class="kicker">/// REFERENCE // CURRICULUM DICTIONARY</span>
                            <h1 class="card-hero__title">Animal Genetics Glossary</h1>
                            <p class="card-hero__desc">
                                Essential high-scoring terminology across Biostatistics, Population Genetics, Quantitative Traits, and Breeding Strategies with audio pronunciation.
                            </p>
                        </div>
                    </div>

                    <div class="glossary-controls mb-4">
                        <div class="search-input-wrap">
                            \${app.icon('search', 'search-icon')}
                            <input type="text" class="input glossary-search-input" placeholder="Search terminology, definitions, breeding systems..." value="\${app.esc(query)}">
                            \${query ? \`<button class="search-clear-btn" aria-label="Clear search">&times;</button>\` : ''}
                        </div>

                        <div class="glossary-categories">
                            <button class="chip \${activeCat === 'all' ? 'chip--active' : ''}" data-cat="all">
                                All Categories (\${Object.keys(glossary.terms).length})
                            </button>
                            \${categories.map(c => \`
                                <button class="chip \${activeCat === c ? 'chip--active' : ''}" data-cat="\${app.esc(c)}">
                                    \${app.esc(c)} (\${glossary.categories[c].length})
                                </button>
                            \`).join('')}
                        </div>
                    </div>

                    <div class="glossary-grid">
                        \${filteredKeys.length ? filteredKeys.map(k => {
                            const item = glossary.terms[k];
                            return \`
                                <div class="glossary-card">
                                    <div class="glossary-card-head">
                                        <div class="glossary-card-term">\${app.esc(item.term)}</div>
                                        <button class="glossary-audio-btn" data-word="\${app.esc(item.term)}" title="Pronounce term" aria-label="Pronounce \${app.esc(item.term)}">
                                            \${app.icon('speaker', 'ico--sm')}
                                        </button>
                                    </div>
                                    <div class="glossary-card-cat">\${app.esc(item.category)}</div>
                                    <div class="glossary-card-def">\${app.esc(item.def)}</div>
                                </div>
                            \`;
                        }).join('') : \`
                            <div class="empty-state">
                                <div class="empty-state__icon">\${app.icon('help')}</div>
                                <h3>No glossary terms match your search</h3>
                                <p class="text-muted">Try a different search term or select another category filter.</p>
                            </div>
                        \`}
                    </div>
                </div>
            \`;

            // Event listeners
            const input = container.querySelector('.glossary-search-input');
            input.addEventListener('input', (e) => {
                query = e.target.value.toLowerCase().trim();
                render();
                const newInput = container.querySelector('.glossary-search-input');
                newInput.focus();
                newInput.setSelectionRange(newInput.value.length, newInput.value.length);
            });

            const clearBtn = container.querySelector('.search-clear-btn');
            if (clearBtn) {
                clearBtn.addEventListener('click', () => {
                    query = '';
                    render();
                });
            }

            container.querySelectorAll('.glossary-categories .chip').forEach(btn => {
                btn.addEventListener('click', () => {
                    activeCat = btn.dataset.cat;
                    render();
                });
            });

            container.querySelectorAll('.glossary-audio-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    glossary.speak(btn.dataset.word);
                });
            });
        };

        render();
    }
};

window.glossary = glossary;
`;

    console.log('Writing 400-term expanded glossary to js/glossary.js...');
    fs.writeFileSync(GLOSSARY_PATH, jsCode, 'utf8');

    console.log('Mirroring 400-term expanded glossary to repo/js/glossary.js...');
    fs.writeFileSync(REPO_GLOSSARY_PATH, jsCode, 'utf8');

    console.log('Successfully generated and mirrored 400-term glossary!');
}

main();
