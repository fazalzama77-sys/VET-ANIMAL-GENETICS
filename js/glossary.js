// =========================================================
// GLOSSARY — B.V.Sc UG-Level Tooltip Term Dictionary
// Animal Genetics and Breeding Studio
// =========================================================
// Usage: glossary.decorate(rootElement) scans rendered HTML
// inside rootElement and wraps known terms with a hover-tooltip.
// Terms are matched longest-first to avoid partial overlap.
// =========================================================

const glossary = {
    categories: {
    "Biostatistics & Experimental Design": [
            "parameter",
            "statistic",
            "central tendency",
            "arithmetic mean",
            "median",
            "mode",
            "dispersion",
            "standard deviation",
            "variance",
            "coefficient of variation",
            "standard error",
            "skewness",
            "kurtosis",
            "probability",
            "normal distribution",
            "binomial distribution",
            "poisson distribution",
            "null hypothesis",
            "degrees of freedom",
            "t-test",
            "z-test",
            "chi-square test",
            "f-test",
            "analysis of variance",
            "completely randomized design",
            "randomized block design",
            "non-parametric test",
            "geometric mean",
            "harmonic mean",
            "range",
            "quartile deviation",
            "mean deviation",
            "interquartile range",
            "percentile",
            "frequency polygon",
            "ogive",
            "pearson correlation coefficient",
            "spearman rank correlation",
            "regression coefficient",
            "coefficient of determination",
            "type i error",
            "type ii error",
            "power of a test",
            "two-tailed test",
            "one-tailed test",
            "paired t-test",
            "yates correction",
            "latin square design",
            "simple random sampling",
            "stratified random sampling",
            "systematic sampling",
            "cluster sampling",
            "weighted mean",
            "combined mean",
            "trimmed mean",
            "variance of mean",
            "bowley skewness",
            "leptokurtic",
            "platykurtic",
            "mesokurtic",
            "bayes theorem",
            "conditional probability",
            "spurious correlation",
            "partial correlation",
            "multiple correlation",
            "principle of least squares",
            "standard error of estimate",
            "sampling frame",
            "critical difference",
            "split-plot design"
    ],
    "Classical & Mendelian Genetics": [
            "allele",
            "homozygous",
            "heterozygous",
            "genotype",
            "phenotype",
            "segregation",
            "independent assortment",
            "monohybrid cross",
            "dihybrid cross",
            "incomplete dominance",
            "codominance",
            "overdominance",
            "lethal gene",
            "epistasis",
            "pleiotropy",
            "penetrance",
            "expressivity",
            "phenocopy",
            "multiple alleles",
            "linkage",
            "crossing over",
            "recombination frequency",
            "testcross",
            "backcross",
            "reciprocal cross",
            "pure line",
            "complementary genes",
            "supplementary genes",
            "duplicate dominant genes",
            "dominant epistasis",
            "inhibitory gene",
            "duplicate genes with cumulative effect",
            "pseudoalleles",
            "isoalleles",
            "atavism",
            "epistatic gene",
            "hypostatic gene",
            "sublethal gene",
            "semi-lethal gene",
            "delayed lethal gene",
            "recombination nodule",
            "chiasma",
            "interference",
            "coefficient of coincidence",
            "centimorgan",
            "cis-trans test",
            "complementation",
            "monohybrid ratio",
            "dihybrid ratio",
            "trihybrid cross",
            "punnett square",
            "testcross ratio",
            "multiple allelism",
            "rh factor",
            "erythroblastosis fetalis",
            "abo blood groups",
            "self-sterility alleles",
            "modified dihybrid ratio",
            "morgan linkage law",
            "complete linkage",
            "incomplete linkage",
            "coupling phase",
            "repulsion phase",
            "map unit",
            "two-point cross",
            "three-point cross",
            "double crossover",
            "non-sister chromatids",
            "cistron",
            "muton"
    ],
    "Cytogenetics & Molecular Genetics": [
            "mitosis",
            "meiosis",
            "karyotype",
            "idiogram",
            "autosome",
            "sex chromosome",
            "heterogametic sex",
            "barr body",
            "dosage compensation",
            "aneuploidy",
            "polyploidy",
            "translocation",
            "inversion",
            "deletion",
            "duplication",
            "central dogma",
            "replication",
            "transcription",
            "translation",
            "pcr",
            "rflp",
            "sanger sequencing",
            "metacentric chromosome",
            "submetacentric chromosome",
            "acrocentric chromosome",
            "telocentric chromosome",
            "synaptonemal complex",
            "g-banding",
            "c-banding",
            "q-banding",
            "r-banding",
            "nor-banding",
            "monosomy",
            "nullisomy",
            "trisomy",
            "freemartinism",
            "robertsonian translocation",
            "reciprocal translocation",
            "paracentric inversion",
            "pericentric inversion",
            "isochromosome",
            "sex-linked trait",
            "sex-limited trait",
            "sex-influenced trait",
            "okazaki fragments",
            "dna ligase",
            "taq polymerase",
            "restriction endonuclease",
            "southern blotting",
            "northern blotting",
            "western blotting",
            "microsatellite",
            "kinetochore",
            "centromere",
            "telomere",
            "chromomere",
            "secondary constriction",
            "polytene chromosome",
            "lampbrush chromosome",
            "b-chromosome",
            "lyon hypothesis",
            "pachytene",
            "zygotene",
            "diplotene",
            "ring chromosome",
            "dicentric chromosome",
            "chargaff rules",
            "wobble hypothesis",
            "tata box",
            "crispr-cas9"
    ],
    "Population Genetics": [
            "gene frequency",
            "genotypic frequency",
            "hardy-weinberg equilibrium",
            "panmixia",
            "genetic drift",
            "bottle neck effect",
            "founder effect",
            "mutation pressure",
            "migration rate",
            "natural selection",
            "artificial selection",
            "polymorphism",
            "gene pool",
            "demographic stochasticity",
            "effective population size",
            "selection coefficient",
            "relative fitness",
            "overdominance fitness",
            "balanced polymorphism",
            "directional selection",
            "stabilizing selection",
            "disruptive selection",
            "assortative mating",
            "consanguinity",
            "identical by descent",
            "identical by state",
            "fixation",
            "loss of heterozygosity",
            "genetic load",
            "gene flow",
            "wahlund effect",
            "genetic distance",
            "allelic frequency",
            "hardy-weinberg equilibrium equation",
            "random genetic drift",
            "island model",
            "stepping stone model",
            "mutation-selection balance",
            "frequency-dependent selection",
            "wright f-statistics",
            "fis",
            "fst",
            "fit",
            "sewall wright effect",
            "prepotency",
            "microevolution",
            "polymorphic locus",
            "panmictic index",
            "genetic polymorphism",
            "gametic phase disequilibrium"
    ],
    "Quantitative Genetics & Inheritance": [
            "quantitative trait",
            "polygenic inheritance",
            "additive gene action",
            "dominance variance",
            "epistatic variance",
            "breeding value",
            "average effect of gene",
            "gene substitution",
            "broad sense heritability",
            "narrow sense heritability",
            "repeatability",
            "genetic correlation",
            "phenotypic correlation",
            "environmental correlation",
            "metric trait",
            "polygenes",
            "phenotypic value",
            "genotypic value",
            "environmental deviation",
            "additive genetic value",
            "dominance deviation",
            "epistatic deviation",
            "permanent environmental variance",
            "temporary environmental variance",
            "realized heritability",
            "paternal half-sib correlation",
            "offspring-parent regression",
            "full-sib correlation",
            "intraclass correlation",
            "contemporary group",
            "contemporary comparison",
            "maternal effect",
            "co-ancestry",
            "numerator relationship matrix",
            "genotype by environment correlation",
            "economic weight",
            "aggregate genotype",
            "correlated response to selection",
            "threshold trait",
            "infinitesimal model",
            "continuous variation",
            "multiple factor hypothesis",
            "liability model",
            "average effect of gene substitution",
            "additive genetic variance",
            "non-additive genetic variance",
            "total genetic variance",
            "environmental variance",
            "genotype environment interaction",
            "co-heritability",
            "paternal half-sib analysis",
            "mid-parent regression",
            "dam component of variance",
            "sire component of variance",
            "intra-sire regression",
            "accuracy of breeding value",
            "selection differential standardized",
            "selection response",
            "annual genetic gain",
            "selection intensity factor",
            "phenotypic standard deviation",
            "additive genetic standard deviation",
            "genetic covariance",
            "environmental covariance",
            "pleiotropic effect on covariance"
    ],
    "Animal Breeding & Selection Systems": [
            "selection differential",
            "selection intensity",
            "generation interval",
            "genetic gain",
            "correlated response",
            "mass selection",
            "pedigree selection",
            "progeny testing",
            "family selection",
            "sib selection",
            "tandem selection",
            "independent culling",
            "selection index",
            "inbreeding",
            "inbreeding depression",
            "inbreeding coefficient",
            "relationship coefficient",
            "outbreeding",
            "crossbreeding",
            "grading up",
            "heterosis",
            "hybrid vigour",
            "combining ability",
            "reciprocal recurrent selection",
            "sire evaluation",
            "blup",
            "most probable producing ability",
            "open nucleus breeding system",
            "animal genetic resources",
            "cryoconservation",
            "individual selection",
            "pedigree index",
            "diallel cross",
            "animal model",
            "sire model",
            "heterobeltiosis",
            "synthetic breed",
            "grading up ratio",
            "rotational crossbreeding",
            "terminal crossbreeding",
            "genomic selection",
            "linebreeding",
            "outcrossing",
            "topcrossing",
            "backcrossing",
            "species hybridization",
            "general combining ability",
            "specific combining ability",
            "closed nucleus breeding system",
            "multiple ovulation and embryo transfer",
            "ovum pick-up",
            "sex-sorted semen",
            "in-situ conservation",
            "ex-situ in-vivo conservation",
            "ex-situ in-vitro conservation",
            "robert bakewell",
            "jay l lush",
            "sewall wright path coefficient",
            "full-sib test",
            "half-sib test",
            "contemporary herdmate",
            "sire proof",
            "daughter-dam comparison",
            "mixed model equations",
            "genomic estimated breeding value",
            "reference population",
            "training population",
            "snp chip",
            "two-way cross",
            "three-way cross",
            "four-way cross",
            "inter-specific hybridization",
            "maternal heterosis",
            "individual heterosis",
            "minimum viable population"
    ]
},

    terms: {
        "parameter": {
            term: "Parameter",
            category: "Biostatistics & Experimental Design",
            def: "A descriptive numerical measure computed from an entire population (e.g. population mean μ, population variance σ²)."
        },
        "statistic": {
            term: "Statistic",
            category: "Biostatistics & Experimental Design",
            def: "A descriptive numerical measure computed from a sample drawn from a population (e.g. sample mean x̄, sample variance s²)."
        },
        "central tendency": {
            term: "Central Tendency",
            category: "Biostatistics & Experimental Design",
            def: "A single central value that summarizes and represents the entire distribution of numerical observations."
        },
        "arithmetic mean": {
            term: "Arithmetic Mean",
            category: "Biostatistics & Experimental Design",
            def: "The sum of all observations divided by the total number of observations (x̄ = Σx / n)."
        },
        "median": {
            term: "Median",
            category: "Biostatistics & Experimental Design",
            def: "The middle value in a dataset arranged in ascending or descending order of magnitude, dividing the data into two equal halves."
        },
        "mode": {
            term: "Mode",
            category: "Biostatistics & Experimental Design",
            def: "The value that occurs with the greatest frequency in a dataset."
        },
        "dispersion": {
            term: "Dispersion",
            category: "Biostatistics & Experimental Design",
            def: "The degree of scatter or variation of individual observations around their central value."
        },
        "standard deviation": {
            term: "Standard Deviation",
            category: "Biostatistics & Experimental Design",
            def: "The positive square root of the arithmetic mean of the squared deviations from the arithmetic mean."
        },
        "variance": {
            term: "Variance",
            category: "Biostatistics & Experimental Design",
            def: "The average of squared deviations of values from their arithmetic mean (s² or σ²)."
        },
        "coefficient of variation": {
            term: "Coefficient of Variation",
            category: "Biostatistics & Experimental Design",
            def: "The relative measure of dispersion expressed as a percentage: CV = (Standard Deviation / Mean) × 100."
        },
        "standard error": {
            term: "Standard Error",
            category: "Biostatistics & Experimental Design",
            def: "The standard deviation of the sampling distribution of a statistic (e.g., SE of mean = s / √n)."
        },
        "skewness": {
            term: "Skewness",
            category: "Biostatistics & Experimental Design",
            def: "The asymmetry or lack of symmetry in a frequency distribution curve."
        },
        "kurtosis": {
            term: "Kurtosis",
            category: "Biostatistics & Experimental Design",
            def: "The degree of peakedness or flatness of a frequency distribution relative to a normal distribution."
        },
        "probability": {
            term: "Probability",
            category: "Biostatistics & Experimental Design",
            def: "A numerical measure ranging from 0 to 1 indicating the likelihood of occurrence of a random event."
        },
        "normal distribution": {
            term: "Normal Distribution",
            category: "Biostatistics & Experimental Design",
            def: "A continuous bell-shaped, symmetrical probability distribution characterized by mean μ and variance σ²."
        },
        "binomial distribution": {
            term: "Binomial Distribution",
            category: "Biostatistics & Experimental Design",
            def: "A discrete probability distribution representing the number of successes in n independent Bernoulli trials with constant probability p."
        },
        "poisson distribution": {
            term: "Poisson Distribution",
            category: "Biostatistics & Experimental Design",
            def: "A discrete probability distribution for rare events occurring randomly in a fixed interval of space or time (where mean = variance = λ)."
        },
        "null hypothesis": {
            term: "Null Hypothesis",
            category: "Biostatistics & Experimental Design",
            def: "The hypothesis (H₀) stating that there is no true difference between the compared groups or parameters."
        },
        "degrees of freedom": {
            term: "Degrees of Freedom",
            category: "Biostatistics & Experimental Design",
            def: "The number of independent values or observations that are free to vary when calculating a statistical parameter."
        },
        "t-test": {
            term: "Student's t-test",
            category: "Biostatistics & Experimental Design",
            def: "A parametric test used to compare means when sample sizes are small (n < 30) and population variance is unknown."
        },
        "z-test": {
            term: "Z-test",
            category: "Biostatistics & Experimental Design",
            def: "A parametric hypothesis test used for large samples (n ≥ 30) where the sampling distribution is approximately normal."
        },
        "chi-square test": {
            term: "Chi-Square Test",
            category: "Biostatistics & Experimental Design",
            def: "A non-parametric statistical test (χ² = Σ[(O-E)²/E]) used to test goodness of fit and independence of attributes."
        },
        "f-test": {
            term: "F-test",
            category: "Biostatistics & Experimental Design",
            def: "The ratio of two independent sample variances used to test the equality of two population variances."
        },
        "analysis of variance": {
            term: "Analysis of Variance (ANOVA)",
            category: "Biostatistics & Experimental Design",
            def: "A statistical technique used to partition total variance into identifiable components attributable to specific sources and random error."
        },
        "completely randomized design": {
            term: "Completely Randomized Design (CRD)",
            category: "Biostatistics & Experimental Design",
            def: "The simplest experimental design where treatments are randomly allocated to completely homogeneous experimental units."
        },
        "randomized block design": {
            term: "Randomized Block Design (RBD)",
            category: "Biostatistics & Experimental Design",
            def: "An experimental design where heterogeneous experimental units are grouped into homogeneous blocks before allocating treatments."
        },
        "non-parametric test": {
            term: "Non-Parametric Test",
            category: "Biostatistics & Experimental Design",
            def: "A statistical distribution-free test that does not depend on strict assumptions regarding the population distribution parameters."
        },
        "allele": {
            term: "Allele",
            category: "Classical & Mendelian Genetics",
            def: "One of two or more alternative forms of a gene located at a specific chromosomal locus."
        },
        "homozygous": {
            term: "Homozygous",
            category: "Classical & Mendelian Genetics",
            def: "Possessing identical alleles at a given gene locus on homologous chromosomes (e.g. AA or aa)."
        },
        "heterozygous": {
            term: "Heterozygous",
            category: "Classical & Mendelian Genetics",
            def: "Possessing two different alleles at a given gene locus on homologous chromosomes (e.g. Aa)."
        },
        "genotype": {
            term: "Genotype",
            category: "Classical & Mendelian Genetics",
            def: "The specific genetic constitution or allelic combination of an organism."
        },
        "phenotype": {
            term: "Phenotype",
            category: "Classical & Mendelian Genetics",
            def: "The observable physical, physiological, or biochemical characteristics of an individual resulting from genotype-environment interaction."
        },
        "segregation": {
            term: "Law of Segregation",
            category: "Classical & Mendelian Genetics",
            def: "Mendel's first law stating that allelic pairs separate during gamete formation so each gamete carries only one allele."
        },
        "independent assortment": {
            term: "Independent Assortment",
            category: "Classical & Mendelian Genetics",
            def: "Mendel's second law stating that alleles of different non-linked genes assort independently during gametogenesis."
        },
        "monohybrid cross": {
            term: "Monohybrid Cross",
            category: "Classical & Mendelian Genetics",
            def: "A genetic cross between parents differing in a single pair of contrasting alleles (F₂ phenotypic ratio 3:1)."
        },
        "dihybrid cross": {
            term: "Dihybrid Cross",
            category: "Classical & Mendelian Genetics",
            def: "A genetic cross between parents differing in two pairs of contrasting alleles (F₂ phenotypic ratio 9:3:3:1)."
        },
        "incomplete dominance": {
            term: "Incomplete Dominance",
            category: "Classical & Mendelian Genetics",
            def: "A genetic interaction where heterozygous individuals express an intermediate phenotype between the two homozygotes (1:2:1 ratio)."
        },
        "codominance": {
            term: "Codominance",
            category: "Classical & Mendelian Genetics",
            def: "A condition in which both alleles of a gene pair in a heterozygote are fully expressed without blending (e.g. roan coat in Shorthorn cattle)."
        },
        "overdominance": {
            term: "Overdominance",
            category: "Classical & Mendelian Genetics",
            def: "A condition in which the heterozygote displays a phenotype superior or more extreme than either homozygote."
        },
        "lethal gene": {
            term: "Lethal Gene",
            category: "Classical & Mendelian Genetics",
            def: "A gene whose expression causes the premature death of the organism, altering standard Mendelian ratios (e.g. 2:1)."
        },
        "epistasis": {
            term: "Epistasis",
            category: "Classical & Mendelian Genetics",
            def: "A non-allelic gene interaction where one gene masks, suppresses, or modifies the phenotypic expression of another gene."
        },
        "pleiotropy": {
            term: "Pleiotropy",
            category: "Classical & Mendelian Genetics",
            def: "The phenomenon wherein a single gene influences multiple distinct and seemingly unrelated phenotypic traits."
        },
        "penetrance": {
            term: "Penetrance",
            category: "Classical & Mendelian Genetics",
            def: "The proportion of individuals carrying a particular genotype who actually manifest the corresponding phenotype."
        },
        "expressivity": {
            term: "Expressivity",
            category: "Classical & Mendelian Genetics",
            def: "The degree or intensity with which a particular genotype is expressed phenotypically among individuals showing the trait."
        },
        "phenocopy": {
            term: "Phenocopy",
            category: "Classical & Mendelian Genetics",
            def: "An environmentally induced phenotype that mimics the phenotype produced by a specific genetic mutation."
        },
        "multiple alleles": {
            term: "Multiple Alleles",
            category: "Classical & Mendelian Genetics",
            def: "A series of more than two allelic forms of a single gene existing in a population (e.g. ABO/J blood group antigens)."
        },
        "linkage": {
            term: "Genetic Linkage",
            category: "Classical & Mendelian Genetics",
            def: "The tendency of two or more genes located closely on the same chromosome to be inherited together as a unit."
        },
        "crossing over": {
            term: "Crossing Over",
            category: "Classical & Mendelian Genetics",
            def: "The reciprocal exchange of genetic material between non-sister chromatids of homologous chromosomes during pachytene of meiosis."
        },
        "recombination frequency": {
            term: "Recombination Frequency",
            category: "Classical & Mendelian Genetics",
            def: "The percentage of recombinant offspring resulting from crossing over, used as a measure of genetic map distance (1% = 1 centimorgan)."
        },
        "mitosis": {
            term: "Mitosis",
            category: "Cytogenetics & Molecular Genetics",
            def: "Equational cell division in somatic cells producing two daughter cells with identical diploid chromosome numbers."
        },
        "meiosis": {
            term: "Meiosis",
            category: "Cytogenetics & Molecular Genetics",
            def: "Reductional cell division in germ cells producing haploid gametes, facilitating genetic segregation and crossing over."
        },
        "karyotype": {
            term: "Karyotype",
            category: "Cytogenetics & Molecular Genetics",
            def: "The complete visual chromosome set of an individual, arranged systematically in pairs by size and centromere location."
        },
        "idiogram": {
            term: "Idiogram",
            category: "Cytogenetics & Molecular Genetics",
            def: "A diagrammatic schematic representation of the karyotype showing morphological features and banding patterns."
        },
        "autosome": {
            term: "Autosome",
            category: "Cytogenetics & Molecular Genetics",
            def: "Any chromosome that is not a sex chromosome (livestock cattle have 29 pairs of autosomes and 1 pair of sex chromosomes)."
        },
        "sex chromosome": {
            term: "Sex Chromosome",
            category: "Cytogenetics & Molecular Genetics",
            def: "Chromosomes involved in sex determination (XX/XY in mammals; ZZ/ZW in poultry birds)."
        },
        "heterogametic sex": {
            term: "Heterogametic Sex",
            category: "Cytogenetics & Molecular Genetics",
            def: "The sex producing two different types of gametes with respect to sex chromosomes (male XY in mammals; female ZW in birds)."
        },
        "barr body": {
            term: "Barr Body",
            category: "Cytogenetics & Molecular Genetics",
            def: "The condensed, transcriptionally inactive X chromosome visible as a sex-chromatin mass at the nuclear periphery in female somatic cells."
        },
        "dosage compensation": {
            term: "Dosage Compensation",
            category: "Cytogenetics & Molecular Genetics",
            def: "The genetic mechanism equalizing the expression of X-linked genes between males and females (Lyon's random X-inactivation)."
        },
        "aneuploidy": {
            term: "Aneuploidy",
            category: "Cytogenetics & Molecular Genetics",
            def: "A numerical chromosome aberration involving the loss or gain of one or a few individual chromosomes (e.g. monosomy 2n-1, trisomy 2n+1)."
        },
        "polyploidy": {
            term: "Polyploidy",
            category: "Cytogenetics & Molecular Genetics",
            def: "A condition in which an organism possesses three or more complete sets of chromosomes (e.g. triploidy 3n, tetraploidy 4n)."
        },
        "translocation": {
            term: "Translocation",
            category: "Cytogenetics & Molecular Genetics",
            def: "A chromosomal structural rearrangement involving the transfer of a chromosome segment to a non-homologous chromosome (e.g. Robertsonian 1/29 translocation)."
        },
        "inversion": {
            term: "Inversion",
            category: "Cytogenetics & Molecular Genetics",
            def: "A chromosomal aberration produced when a segment undergoes two breaks, rotates 180 degrees, and reunites."
        },
        "deletion": {
            term: "Deletion",
            category: "Cytogenetics & Molecular Genetics",
            def: "The loss of a chromosomal fragment and its contained genes."
        },
        "duplication": {
            term: "Duplication",
            category: "Cytogenetics & Molecular Genetics",
            def: "The presence of an extra copy of a chromosomal segment."
        },
        "central dogma": {
            term: "Central Dogma",
            category: "Cytogenetics & Molecular Genetics",
            def: "The core biological flow of genetic information: DNA replication → DNA transcription to mRNA → mRNA translation to functional protein."
        },
        "replication": {
            term: "DNA Replication",
            category: "Cytogenetics & Molecular Genetics",
            def: "The semiconservative synthesis of identical duplicate DNA molecules prior to cell division mediated by DNA polymerase."
        },
        "transcription": {
            term: "Transcription",
            category: "Cytogenetics & Molecular Genetics",
            def: "The enzymatic synthesis of an RNA molecule from a DNA template strand by RNA polymerase."
        },
        "translation": {
            term: "Translation",
            category: "Cytogenetics & Molecular Genetics",
            def: "The ribosomal synthesis of a polypeptide sequence directed by the mRNA codon sequence."
        },
        "pcr": {
            term: "Polymerase Chain Reaction (PCR)",
            category: "Cytogenetics & Molecular Genetics",
            def: "An in-vitro enzymatic technique used to exponentially amplify specific target DNA fragments through cyclic denaturation, annealing, and extension."
        },
        "rflp": {
            term: "RFLP",
            category: "Cytogenetics & Molecular Genetics",
            def: "Restriction Fragment Length Polymorphism: variation in the length of DNA fragments produced by specific restriction enzyme digestion."
        },
        "sanger sequencing": {
            term: "Sanger Sequencing",
            category: "Cytogenetics & Molecular Genetics",
            def: "The classical chain-termination method for determining nucleotide sequence using dideoxynucleotides (ddNTPs)."
        },
        "gene frequency": {
            term: "Gene (Allele) Frequency",
            category: "Population Genetics",
            def: "The relative proportion of a particular allele among all alleles at that locus in a breeding population."
        },
        "genotypic frequency": {
            term: "Genotypic Frequency",
            category: "Population Genetics",
            def: "The relative proportion of a particular genotype among all individuals in a population."
        },
        "hardy-weinberg equilibrium": {
            term: "Hardy-Weinberg Equilibrium",
            category: "Population Genetics",
            def: "The principle that allele and genotypic frequencies remain constant from generation to generation in a large, randomly mating population in the absence of evolutionary forces (p² + 2pq + q² = 1)."
        },
        "panmixia": {
            term: "Panmixia (Random Mating)",
            category: "Population Genetics",
            def: "A mating system where every individual has an equal probability of mating with any individual of the opposite sex."
        },
        "genetic drift": {
            term: "Genetic Drift",
            category: "Population Genetics",
            def: "Random fluctuations in allele frequencies from generation to generation occurring strictly due to chance sampling in small finite populations."
        },
        "bottle neck effect": {
            term: "Bottleneck Effect",
            category: "Population Genetics",
            def: "A sharp reduction in population size caused by environmental catastrophes or disease epidemics, causing drastic loss of genetic diversity."
        },
        "founder effect": {
            term: "Founder Effect",
            category: "Population Genetics",
            def: "The loss of genetic variation that occurs when a new population is established by a very small number of individuals from a larger population."
        },
        "mutation pressure": {
            term: "Mutation Pressure",
            category: "Population Genetics",
            def: "The rate at which gene frequencies are changed solely as a result of recurrent forward and backward mutations."
        },
        "migration rate": {
            term: "Migration (Gene Flow)",
            category: "Population Genetics",
            def: "The transfer of genetic variation between populations through the introduction of breeding individuals from external populations."
        },
        "natural selection": {
            term: "Natural Selection",
            category: "Population Genetics",
            def: "The differential survival and reproduction of individuals due to differences in phenotype under specific environmental conditions."
        },
        "artificial selection": {
            term: "Artificial Selection",
            category: "Population Genetics",
            def: "The deliberate process where human breeders choose which animals reproduce based on desired economic traits."
        },
        "polymorphism": {
            term: "Genetic Polymorphism",
            category: "Population Genetics",
            def: "The simultaneous occurrence in a population of two or more discontinuous alleles in frequencies too high to be maintained solely by recurrent mutation."
        },
        "quantitative trait": {
            term: "Quantitative Trait",
            category: "Quantitative Genetics & Inheritance",
            def: "A continuous metric trait controlled by multiple genes (polygenes) and strongly influenced by environmental factors (e.g. milk yield, body weight)."
        },
        "polygenic inheritance": {
            term: "Polygenic Inheritance",
            category: "Quantitative Genetics & Inheritance",
            def: "The transmission of phenotypic characters governed by the cumulative effects of many genes, each having a small additive effect."
        },
        "additive gene action": {
            term: "Additive Gene Action",
            category: "Quantitative Genetics & Inheritance",
            def: "The component of genetic variance resulting from the independent cumulative effects of individual alleles that can be passed directly from parent to offspring."
        },
        "dominance variance": {
            term: "Dominance Variance",
            category: "Quantitative Genetics & Inheritance",
            def: "The non-additive genetic variance arising from interactions between alleles at the same locus."
        },
        "epistatic variance": {
            term: "Epistatic Variance",
            category: "Quantitative Genetics & Inheritance",
            def: "The non-additive genetic variance resulting from interaction between alleles at different loci."
        },
        "breeding value": {
            term: "Breeding Value",
            category: "Quantitative Genetics & Inheritance",
            def: "The value of an individual as a genetic parent, defined as twice the expected deviation of its progeny mean from the population mean."
        },
        "average effect of gene": {
            term: "Average Effect of Gene",
            category: "Quantitative Genetics & Inheritance",
            def: "The mean deviation from the population mean of individuals that received a particular allele from one parent, the other allele coming at random."
        },
        "gene substitution": {
            term: "Average Effect of Gene Substitution",
            category: "Quantitative Genetics & Inheritance",
            def: "The expected change in mean phenotypic value when one allele is substituted for another allele at that locus."
        },
        "broad sense heritability": {
            term: "Broad-Sense Heritability",
            category: "Quantitative Genetics & Inheritance",
            def: "The proportion of total phenotypic variance attributable to total genetic variance (H² = Vg / Vp)."
        },
        "narrow sense heritability": {
            term: "Narrow-Sense Heritability",
            category: "Quantitative Genetics & Inheritance",
            def: "The proportion of total phenotypic variance attributable specifically to additive genetic variance (h² = Va / Vp)."
        },
        "repeatability": {
            term: "Repeatability",
            category: "Quantitative Genetics & Inheritance",
            def: "The correlation between repeated phenotypic measurements of the same trait on the same individual over time (sets an upper limit to heritability)."
        },
        "genetic correlation": {
            term: "Genetic Correlation",
            category: "Quantitative Genetics & Inheritance",
            def: "The correlation between the breeding values of two traits in the same individual, caused primarily by pleiotropy or linkage."
        },
        "phenotypic correlation": {
            term: "Phenotypic Correlation",
            category: "Quantitative Genetics & Inheritance",
            def: "The observable correlation between two metric traits measured directly on the same individual, combining genetic and environmental associations."
        },
        "environmental correlation": {
            term: "Environmental Correlation",
            category: "Quantitative Genetics & Inheritance",
            def: "The correlation between the environmental deviations affecting two different traits in the same animal."
        },
        "selection differential": {
            term: "Selection Differential (S)",
            category: "Animal Breeding & Selection Systems",
            def: "The numerical difference between the mean phenotypic value of selected parents and the mean of the entire parental population (S = x̄_s - x̄)."
        },
        "selection intensity": {
            term: "Selection Intensity (i)",
            category: "Animal Breeding & Selection Systems",
            def: "The selection differential expressed in units of phenotypic standard deviation: i = S / σp."
        },
        "generation interval": {
            term: "Generation Interval (L)",
            category: "Animal Breeding & Selection Systems",
            def: "The average age of parents when their offspring are born (typically 4.5–5.5 years in dairy cattle)."
        },
        "genetic gain": {
            term: "Genetic Gain (ΔG)",
            category: "Animal Breeding & Selection Systems",
            def: "The expected genetic progress per unit time achieved through selection: ΔG = (i × h² × σp) / L."
        },
        "correlated response": {
            term: "Correlated Response to Selection",
            category: "Animal Breeding & Selection Systems",
            def: "The change in an unselected second trait resulting from direct selection applied to a primary trait due to genetic correlation."
        },
        "mass selection": {
            term: "Individual (Mass) Selection",
            category: "Animal Breeding & Selection Systems",
            def: "Selection based solely on the individual's own phenotypic performance records, highly effective for traits with high heritability."
        },
        "pedigree selection": {
            term: "Pedigree Selection",
            category: "Animal Breeding & Selection Systems",
            def: "Selection based on the performance of an individual's ancestors (parents, grandparents), valuable for early culling before own performance is expressed."
        },
        "progeny testing": {
            term: "Progeny Testing",
            category: "Animal Breeding & Selection Systems",
            def: "Evaluation of a sire or dam's breeding value based on the average phenotypic performance of a representative sample of its offspring."
        },
        "family selection": {
            term: "Family Selection",
            category: "Animal Breeding & Selection Systems",
            def: "Selection based on the average phenotypic performance of whole families (full-sibs or half-sibs)."
        },
        "sib selection": {
            term: "Sib Selection",
            category: "Animal Breeding & Selection Systems",
            def: "Selection of breeding candidates based on the performance of their brothers or sisters (sibs), especially for sex-limited or slaughter traits."
        },
        "tandem selection": {
            term: "Tandem Selection",
            category: "Animal Breeding & Selection Systems",
            def: "Selecting for one trait at a time until a desired performance level is achieved, then shifting selection to a second trait."
        },
        "independent culling": {
            term: "Independent Culling Levels",
            category: "Animal Breeding & Selection Systems",
            def: "A multi-trait selection method where minimum cutoff standards are established for each trait, and individuals falling below any threshold are culled."
        },
        "selection index": {
            term: "Selection Index",
            category: "Animal Breeding & Selection Systems",
            def: "The most efficient multi-trait selection method, combining phenotypic records on multiple traits weighted by economic values and genetic parameters into a single score."
        },
        "inbreeding": {
            term: "Inbreeding",
            category: "Animal Breeding & Selection Systems",
            def: "The mating of individuals that are more closely related to each other than the average relationship of the population."
        },
        "inbreeding depression": {
            term: "Inbreeding Depression",
            category: "Animal Breeding & Selection Systems",
            def: "The reduction in mean performance, fitness, vigor, fertility, and survival that accompanies an increase in inbreeding."
        },
        "inbreeding coefficient": {
            term: "Inbreeding Coefficient (F)",
            category: "Animal Breeding & Selection Systems",
            def: "The probability that two homologous alleles at a given locus in an individual are identical by descent (IBD) from a common ancestor: F = Σ[(1/2)^(n1+n2+1) × (1+Fa)]."
        },
        "relationship coefficient": {
            term: "Coefficient of Relationship (R)",
            category: "Animal Breeding & Selection Systems",
            def: "The measure of the pedigree proportion of genes shared between two individuals that are identical by descent."
        },
        "outbreeding": {
            term: "Outbreeding",
            category: "Animal Breeding & Selection Systems",
            def: "The mating of animals that are less closely related to each other than the average relationship of the population."
        },
        "crossbreeding": {
            term: "Crossbreeding",
            category: "Animal Breeding & Selection Systems",
            def: "The mating of animals belonging to different established breeds to exploit heterosis and breed complementarity."
        },
        "grading up": {
            term: "Grading Up",
            category: "Animal Breeding & Selection Systems",
            def: "The continuous mating of non-descript or indigenous female livestock to purebred sires of a superior breed over consecutive generations."
        },
        "heterosis": {
            term: "Heterosis (Hybrid Vigour)",
            category: "Animal Breeding & Selection Systems",
            def: "The superiority in performance of crossbred progeny over the average performance of their purebred parental breeds: % Heterosis = [(F₁ - MP) / MP] × 100."
        },
        "hybrid vigour": {
            term: "Hybrid Vigour",
            category: "Animal Breeding & Selection Systems",
            def: "The increased vigor, growth rate, fertility, and hardiness observed in crossbred animals relative to mid-parent averages."
        },
        "combining ability": {
            term: "Combining Ability",
            category: "Animal Breeding & Selection Systems",
            def: "The capacity of an inbred line or breed to cross well with other lines, partitioned into General Combining Ability (GCA) and Specific Combining Ability (SCA)."
        },
        "reciprocal recurrent selection": {
            term: "Reciprocal Recurrent Selection (RRS)",
            category: "Animal Breeding & Selection Systems",
            def: "A cyclical breeding system where two distinct lines or populations are simultaneously selected based on their crossbred progeny performance."
        },
        "sire evaluation": {
            term: "Sire Evaluation",
            category: "Animal Breeding & Selection Systems",
            def: "The scientific statistical assessment of a breeding bull's transmitting ability for economic traits using daughters' performance records."
        },
        "blup": {
            term: "BLUP (Best Linear Unbiased Prediction)",
            category: "Animal Breeding & Selection Systems",
            def: "The standard mixed-model statistical methodology (Animal Model) used to estimate breeding values while simultaneously adjusting for environmental and herd-year-season fixed effects."
        },
        "most probable producing ability": {
            term: "Most Probable Producing Ability (MPPA)",
            category: "Animal Breeding & Selection Systems",
            def: "An estimate of an individual animal's future production potential based on its repeated historical performance records and the repeatability of the trait: MPPA = Population Mean + [n*r / (1 + (n-1)*r)] * (Individual Mean - Population Mean)."
        },
        "open nucleus breeding system": {
            term: "Open Nucleus Breeding System (ONBS)",
            category: "Animal Breeding & Selection Systems",
            def: "A tiered breeding structure where an elite nucleus herd is maintained, with ongoing gene flow from elite commercial base females into the nucleus."
        },
        "animal genetic resources": {
            term: "Animal Genetic Resources (AnGR)",
            category: "Animal Breeding & Selection Systems",
            def: "All livestock and avian populations of economic, cultural, or scientific value, including registered indigenous breeds and wild relatives."
        },
        "cryoconservation": {
            term: "Cryoconservation (Ex-Situ)",
            category: "Animal Breeding & Selection Systems",
            def: "The long-term preservation of semen, ova, embryos, or somatic tissue in liquid nitrogen at -196°C to safeguard genetic diversity."
        },
        "geometric mean": {
            term: "Geometric Mean",
            category: "Biostatistics & Experimental Design",
            def: "The nth root of the product of n positive observations; especially useful for computing average rates of population growth and geometric ratios."
        },
        "harmonic mean": {
            term: "Harmonic Mean",
            category: "Biostatistics & Experimental Design",
            def: "The reciprocal of the arithmetic mean of the reciprocals of observations; the appropriate average for rates of speed and work."
        },
        "range": {
            term: "Range",
            category: "Biostatistics & Experimental Design",
            def: "The difference between the maximum and minimum observations in a biological dataset; the simplest measure of dispersion."
        },
        "quartile deviation": {
            term: "Quartile Deviation (QD)",
            category: "Biostatistics & Experimental Design",
            def: "Half of the interquartile range ((Q3 - Q1) / 2), also known as the semi-interquartile range; resistant to extreme outliers."
        },
        "mean deviation": {
            term: "Mean Deviation",
            category: "Biostatistics & Experimental Design",
            def: "The arithmetic mean of the absolute deviations of observations taken from their mean or median, ignoring positive/negative signs."
        },
        "interquartile range": {
            term: "Interquartile Range (IQR)",
            category: "Biostatistics & Experimental Design",
            def: "The difference between the 75th percentile (Q3) and 25th percentile (Q1), representing the spread of the central 50% of the data."
        },
        "percentile": {
            term: "Percentile",
            category: "Biostatistics & Experimental Design",
            def: "Values that partition an ordered frequency distribution into 100 equal parts (P1 to P99) to evaluate individual rank."
        },
        "frequency polygon": {
            term: "Frequency Polygon",
            category: "Biostatistics & Experimental Design",
            def: "A graphical line representation of a continuous frequency distribution drawn by connecting the midpoints of adjacent histogram bars."
        },
        "ogive": {
            term: "Ogive (Cumulative Frequency Curve)",
            category: "Biostatistics & Experimental Design",
            def: "An S-shaped cumulative frequency curve ('less than' or 'more than') used to graphically determine medians and quartiles."
        },
        "pearson correlation coefficient": {
            term: "Pearson Correlation Coefficient (r)",
            category: "Biostatistics & Experimental Design",
            def: "A dimensionless biostatistical measure bounded between -1.0 and +1.0 quantifying the strength and direction of linear association between two continuous variables."
        },
        "spearman rank correlation": {
            term: "Spearman's Rank Correlation (ρ)",
            category: "Biostatistics & Experimental Design",
            def: "A non-parametric correlation statistic based on the ranked orders of observations, given by ρ = 1 - [6 Σ d² / (n(n² - 1))]."
        },
        "regression coefficient": {
            term: "Regression Coefficient (b)",
            category: "Biostatistics & Experimental Design",
            def: "The slope of a linear regression line representing the expected change in the dependent variable Y per unit change in independent variable X."
        },
        "coefficient of determination": {
            term: "Coefficient of Determination (r²)",
            category: "Biostatistics & Experimental Design",
            def: "The square of the Pearson correlation coefficient, measuring the proportion of total variance in the dependent variable explained by the regression model."
        },
        "type i error": {
            term: "Type I Error (α)",
            category: "Biostatistics & Experimental Design",
            def: "The statistical error committed when a true null hypothesis (H₀) is erroneously rejected; the probability of this error is the significance level α."
        },
        "type ii error": {
            term: "Type II Error (β)",
            category: "Biostatistics & Experimental Design",
            def: "The statistical error committed when a false null hypothesis (H₀) fails to be rejected; the probability of this error is denoted by β."
        },
        "power of a test": {
            term: "Power of a Statistical Test (1 - β)",
            category: "Biostatistics & Experimental Design",
            def: "The probability of correctly rejecting a false null hypothesis, mathematically defined as 1 - β."
        },
        "two-tailed test": {
            term: "Two-Tailed Test",
            category: "Biostatistics & Experimental Design",
            def: "A non-directional hypothesis test where the critical rejection region is divided equally between the upper and lower tails of the distribution."
        },
        "one-tailed test": {
            term: "One-Tailed Test",
            category: "Biostatistics & Experimental Design",
            def: "A directional hypothesis test where the critical rejection region is located entirely within one tail (upper or lower) of the distribution."
        },
        "paired t-test": {
            term: "Paired Student's t-test",
            category: "Biostatistics & Experimental Design",
            def: "A t-test procedure applied to two correlated or dependent samples (such as pre-treatment vs. post-treatment measurements on the same animal)."
        },
        "yates correction": {
            term: "Yates' Continuity Correction",
            category: "Biostatistics & Experimental Design",
            def: "An adjustment applied to 2 × 2 contingency tables in Chi-Square testing when cell frequencies are small (<5) to reduce overestimation of significance."
        },
        "latin square design": {
            term: "Latin Square Design (LSD)",
            category: "Biostatistics & Experimental Design",
            def: "An experimental field design that controls environmental heterogeneity in two orthogonal directions simultaneously (rows and columns) with t treatments."
        },
        "simple random sampling": {
            term: "Simple Random Sampling (SRS)",
            category: "Biostatistics & Experimental Design",
            def: "A fundamental probability sampling technique where every individual animal in the population has an equal and independent chance of selection."
        },
        "stratified random sampling": {
            term: "Stratified Random Sampling",
            category: "Biostatistics & Experimental Design",
            def: "A sampling method where a heterogeneous livestock population is partitioned into homogeneous sub-groups (strata) prior to drawing random samples."
        },
        "systematic sampling": {
            term: "Systematic Sampling",
            category: "Biostatistics & Experimental Design",
            def: "A sampling method where individuals are selected at regular numerical intervals (every kth animal) following an initial random start."
        },
        "cluster sampling": {
            term: "Cluster Sampling",
            category: "Biostatistics & Experimental Design",
            def: "A sampling technique where the population is divided into naturally occurring heterogeneous clusters (e.g. herds or villages) and whole clusters are randomly sampled."
        },
        "testcross": {
            term: "Testcross",
            category: "Classical & Mendelian Genetics",
            def: "A genetic mating of an individual displaying a dominant phenotype with a homozygous recessive tester to determine whether the dominant parent is homozygous or heterozygous."
        },
        "backcross": {
            term: "Backcross",
            category: "Classical & Mendelian Genetics",
            def: "The mating of an F1 crossbred individual back to either of its parental homozygous genotypes."
        },
        "reciprocal cross": {
            term: "Reciprocal Cross",
            category: "Classical & Mendelian Genetics",
            def: "A pair of genetic crosses in which the genotypes of the male and female parents are reversed to detect sex-linkage or maternal cytoplasmic effects."
        },
        "pure line": {
            term: "Pure Line (Johannsen)",
            category: "Classical & Mendelian Genetics",
            def: "A population of genetically uniform, homozygous individuals derived from repeated self-fertilization or close inbreeding of a single homozygous ancestor."
        },
        "complementary genes": {
            term: "Complementary Gene Action (9:7)",
            category: "Classical & Mendelian Genetics",
            def: "A non-allelic interaction where two dominant genes at separate loci must both be present to produce the trait, giving an F2 phenotypic ratio of 9:7."
        },
        "supplementary genes": {
            term: "Supplementary Gene Action / Recessive Epistasis (9:3:4)",
            category: "Classical & Mendelian Genetics",
            def: "An epistatic interaction where a homozygous recessive condition at one locus masks the expression of another locus, yielding a 9:3:4 F2 ratio."
        },
        "duplicate dominant genes": {
            term: "Duplicate Dominant Gene Action (15:1)",
            category: "Classical & Mendelian Genetics",
            def: "Gene interaction where the presence of a dominant allele at either of two independent loci produces the trait, yielding a 15:1 F2 ratio."
        },
        "dominant epistasis": {
            term: "Dominant Epistasis (12:3:1)",
            category: "Classical & Mendelian Genetics",
            def: "Gene interaction where a single dominant allele at one locus suppresses the phenotypic expression of both alleles at another locus, yielding a 12:3:1 F2 ratio."
        },
        "inhibitory gene": {
            term: "Inhibitory Gene Action (13:3)",
            category: "Classical & Mendelian Genetics",
            def: "Dominant-and-recessive interaction where a dominant allele at one locus acts as an inhibitor suppressing the phenotypic effect of another dominant gene, yielding a 13:3 F2 ratio."
        },
        "duplicate genes with cumulative effect": {
            term: "Duplicate Genes with Cumulative Effect (9:6:1)",
            category: "Classical & Mendelian Genetics",
            def: "Gene interaction where two dominant genes produce identical phenotypes individually, but produce an enhanced phenotype together, yielding a 9:6:1 F2 ratio."
        },
        "pseudoalleles": {
            term: "Pseudoalleles",
            category: "Classical & Mendelian Genetics",
            def: "Closely linked genes that behave functionally as alleles in complementation tests but between which rare meiotic crossing over can occur."
        },
        "isoalleles": {
            term: "Isoalleles",
            category: "Classical & Mendelian Genetics",
            def: "Alleles that produce phenotypic effects so similar that they can only be distinguished under special environmental conditions or modified genetic backgrounds."
        },
        "atavism": {
            term: "Atavism (Reversion)",
            category: "Classical & Mendelian Genetics",
            def: "The spontaneous reappearance of an ancestral phenotypic trait that had been absent in previous generations, often triggered by recombination."
        },
        "epistatic gene": {
            term: "Epistatic Gene",
            category: "Classical & Mendelian Genetics",
            def: "A gene locus that overrides, masks, or suppresses the phenotypic manifestation of an allele at another independent gene locus."
        },
        "hypostatic gene": {
            term: "Hypostatic Gene",
            category: "Classical & Mendelian Genetics",
            def: "A gene locus whose phenotypic expression is overridden, masked, or suppressed by an epistatic gene locus."
        },
        "sublethal gene": {
            term: "Sublethal Gene",
            category: "Classical & Mendelian Genetics",
            def: "A mutant gene causing the premature death of more than 50% but less than 100% of homozygous carriers before reaching reproductive maturity."
        },
        "semi-lethal gene": {
            term: "Semi-Lethal Gene",
            category: "Classical & Mendelian Genetics",
            def: "A mutant gene causing the mortality of less than 50% of homozygous individuals, with survival heavily dependent on supportive environmental conditions."
        },
        "delayed lethal gene": {
            term: "Delayed Lethal Gene",
            category: "Classical & Mendelian Genetics",
            def: "A deleterious mutant gene whose lethal phenotypic effect manifests later in adult life, often after the animal has reached reproductive maturity."
        },
        "recombination nodule": {
            term: "Recombination Nodule",
            category: "Classical & Mendelian Genetics",
            def: "Dense protein complexes positioned along the synaptonemal complex during pachytene that mediate the molecular breakage and reunion of crossing over."
        },
        "chiasma": {
            term: "Chiasma (pl. Chiasmata)",
            category: "Classical & Mendelian Genetics",
            def: "The cytologically visible X-shaped junction formed between non-sister chromatids of paired homologous chromosomes during diplotene of meiosis."
        },
        "interference": {
            term: "Chromosome Interference",
            category: "Classical & Mendelian Genetics",
            def: "The phenomenon whereby a crossover event occurring in one chromosomal region reduces the probability of a concurrent second crossover occurring nearby (Interference = 1 - Coefficient of Coincidence)."
        },
        "coefficient of coincidence": {
            term: "Coefficient of Coincidence (C)",
            category: "Classical & Mendelian Genetics",
            def: "The ratio of observed double crossover frequency to expected double crossover frequency: C = Observed DCO / Expected DCO."
        },
        "centimorgan": {
            term: "CentiMorgan (cM)",
            category: "Classical & Mendelian Genetics",
            def: "A standard unit of genetic linkage map distance defined as that physical length of chromosome within which 1% meiotic crossing over occurs."
        },
        "cis-trans test": {
            term: "Cis-Trans Complementation Test",
            category: "Classical & Mendelian Genetics",
            def: "A genetic test devised by Seymour Benzer to determine whether two mutations lie within the same functional genetic unit (cistron) or different genes."
        },
        "complementation": {
            term: "Complementation",
            category: "Classical & Mendelian Genetics",
            def: "The restoration of a wild-type phenotype when two independent recessive mutations are brought together in the same trans-heterozygote cell."
        },
        "metacentric chromosome": {
            term: "Metacentric Chromosome",
            category: "Cytogenetics & Molecular Genetics",
            def: "A chromosome whose centromere is positioned at the exact midpoint, giving equal short (p) and long (q) arms that form a V-shape during anaphase."
        },
        "submetacentric chromosome": {
            term: "Submetacentric Chromosome",
            category: "Cytogenetics & Molecular Genetics",
            def: "A chromosome whose centromere is positioned slightly off-center, producing unequal arm lengths (p short arm and q long arm) that form an L-shape."
        },
        "acrocentric chromosome": {
            term: "Acrocentric Chromosome",
            category: "Cytogenetics & Molecular Genetics",
            def: "A chromosome with a centromere located very near one end, producing a minute short p arm; all 58 bovine autosomes are acrocentric."
        },
        "telocentric chromosome": {
            term: "Telocentric Chromosome",
            category: "Cytogenetics & Molecular Genetics",
            def: "A chromosome having a terminal centromere located at the very tip, possessing only a single visible chromosome arm."
        },
        "synaptonemal complex": {
            term: "Synaptonemal Complex",
            category: "Cytogenetics & Molecular Genetics",
            def: "A tripartite protein zipper-like scaffold assembled between homologous chromosomes during zygotene to facilitate precise meiotic synapsis and crossing over."
        },
        "g-banding": {
            term: "G-Banding (Giemsa Banding)",
            category: "Cytogenetics & Molecular Genetics",
            def: "A cytogenetic staining method using mild trypsin digestion followed by Giemsa dye to produce alternating AT-rich dark and GC-rich light bands along chromosomes."
        },
        "c-banding": {
            term: "C-Banding (Centromeric Banding)",
            category: "Cytogenetics & Molecular Genetics",
            def: "A specialized chromosome staining method highlighting constitutive heterochromatin, predominantly localized at centromeres and the bovine Y chromosome."
        },
        "q-banding": {
            term: "Q-Banding (Quinacrine Banding)",
            category: "Cytogenetics & Molecular Genetics",
            def: "A fluorescent cytogenetic banding technique using quinacrine mustard to reveal brilliant AT-rich bands under ultraviolet fluorescence microscopy."
        },
        "r-banding": {
            term: "R-Banding (Reverse Banding)",
            category: "Cytogenetics & Molecular Genetics",
            def: "A thermal denaturation banding technique producing a pattern reciprocal to G-banding, highlighting transcriptionally active GC-rich chromosomal regions."
        },
        "nor-banding": {
            term: "NOR-Banding (Nucleolar Organizer Region)",
            category: "Cytogenetics & Molecular Genetics",
            def: "A silver-staining technique (Ag-NOR) that specifically stains actively transcribed ribosomal RNA gene clusters on satellite chromosomes."
        },
        "monosomy": {
            term: "Monosomy (2n - 1)",
            category: "Cytogenetics & Molecular Genetics",
            def: "An aneuploid chromosomal condition characterized by the loss of a single chromosome from a diploid set (e.g. Turner syndrome XO)."
        },
        "nullisomy": {
            term: "Nullisomy (2n - 2)",
            category: "Cytogenetics & Molecular Genetics",
            def: "An aneuploid state in which an organism is missing both homologous chromosomes of a specific chromosomal pair; typically lethal in mammals."
        },
        "trisomy": {
            term: "Trisomy (2n + 1)",
            category: "Cytogenetics & Molecular Genetics",
            def: "An aneuploidy condition involving the presence of three copies of a specific chromosome instead of the normal homologous pair."
        },
        "freemartinism": {
            term: "Freemartinism",
            category: "Cytogenetics & Molecular Genetics",
            def: "A sterile intersex bovine heifer born co-twin with a male, caused by chorionic vascular anastomosis transferring anti-Müllerian hormone and male cells in utero."
        },
        "robertsonian translocation": {
            term: "Robertsonian Translocation (Centric Fusion)",
            category: "Cytogenetics & Molecular Genetics",
            def: "A structural chromosomal aberration where two acrocentric chromosomes fuse at their centromeres into a single large metacentric chromosome (e.g. bovine 1/29 translocation)."
        },
        "reciprocal translocation": {
            term: "Reciprocal Translocation",
            category: "Cytogenetics & Molecular Genetics",
            def: "A structural aberration involving the non-homologous mutual exchange of chromosomal fragments between two non-homologous chromosomes."
        },
        "paracentric inversion": {
            term: "Paracentric Inversion",
            category: "Cytogenetics & Molecular Genetics",
            def: "A structural chromosomal inversion confined to a single chromosome arm that does not include the centromere within the inverted segment."
        },
        "pericentric inversion": {
            term: "Pericentric Inversion",
            category: "Cytogenetics & Molecular Genetics",
            def: "A structural chromosomal inversion where the chromosome breaks occur on opposite sides of the centromere, including the centromere in the inverted loop."
        },
        "isochromosome": {
            term: "Isochromosome",
            category: "Cytogenetics & Molecular Genetics",
            def: "An aberrant chromosome featuring two identical arms formed by transverse rather than longitudinal centromeric division during cell division."
        },
        "sex-linked trait": {
            term: "Sex-Linked Trait",
            category: "Cytogenetics & Molecular Genetics",
            def: "A trait governed by a gene located on the non-homologous portion of sex chromosomes (X or Z), exhibiting characteristic criss-cross transmission across generations."
        },
        "sex-limited trait": {
            term: "Sex-Limited Trait",
            category: "Cytogenetics & Molecular Genetics",
            def: "An autosomal trait whose phenotypic expression is restricted to only one biological sex due to anatomical or physiological limitations (e.g. milk yield, cryptorchidism)."
        },
        "sex-influenced trait": {
            term: "Sex-Influenced Trait",
            category: "Cytogenetics & Molecular Genetics",
            def: "An autosomal trait whose dominance and phenotypic penetrance are altered by gonadal hormones (e.g. horns in sheep, dominant in rams, recessive in ewes)."
        },
        "okazaki fragments": {
            term: "Okazaki Fragments",
            category: "Cytogenetics & Molecular Genetics",
            def: "Short stretches of newly synthesized DNA formed discontinuously in the 5' to 3' direction along the lagging template strand during replication."
        },
        "dna ligase": {
            term: "DNA Ligase",
            category: "Cytogenetics & Molecular Genetics",
            def: "An enzyme that catalyzes the creation of covalent phosphodiester bonds to join Okazaki fragments and seal nicks in the DNA sugar-phosphate backbone."
        },
        "taq polymerase": {
            term: "Taq DNA Polymerase",
            category: "Cytogenetics & Molecular Genetics",
            def: "A heat-stable DNA polymerase purified from the thermophilic bacterium Thermus aquaticus, utilized to catalyze DNA extension in automated PCR."
        },
        "restriction endonuclease": {
            term: "Restriction Endonuclease",
            category: "Cytogenetics & Molecular Genetics",
            def: "A bacterial enzyme that recognizes specific palindromic DNA sequences and cleaves the phosphodiester bonds within both strands at defined restriction sites."
        },
        "southern blotting": {
            term: "Southern Blotting",
            category: "Cytogenetics & Molecular Genetics",
            def: "A molecular hybridization method devised by Edwin Southern for transferring electrophoresed DNA fragments to a membrane for hybridization with labeled DNA probes."
        },
        "northern blotting": {
            term: "Northern Blotting",
            category: "Cytogenetics & Molecular Genetics",
            def: "A molecular biology procedure for separating, sizing, and quantifying specific cellular RNA molecules transferred from an agarose gel to a nylon membrane."
        },
        "western blotting": {
            term: "Western Blotting",
            category: "Cytogenetics & Molecular Genetics",
            def: "An analytical immunochemical method for detecting specific proteins separated by gel electrophoresis using labeled monoclonal or polyclonal antibodies."
        },
        "microsatellite": {
            term: "Microsatellite (SSR / STR)",
            category: "Cytogenetics & Molecular Genetics",
            def: "Short tandem repeats of 1 to 6 base pair motifs (e.g. (CA)n) distributed across the genome, serving as highly polymorphic codominant markers for parentage testing."
        },
        "gene pool": {
            term: "Gene Pool",
            category: "Population Genetics",
            def: "The total genetic information and complete set of all alleles possessed by all sexually reproducing individuals in a Mendelian breeding population."
        },
        "demographic stochasticity": {
            term: "Demographic Stochasticity",
            category: "Population Genetics",
            def: "Random fluctuations in population size and sex ratio resulting from probabilistic individual survival, reproductive, and mortality events in small herds."
        },
        "effective population size": {
            term: "Effective Population Size (Ne)",
            category: "Population Genetics",
            def: "The size of an idealized panmictic population that would experience the same rate of inbreeding or random genetic drift as the actual census herd: Ne = (4 Nm Nf) / (Nm + Nf)."
        },
        "selection coefficient": {
            term: "Selection Coefficient (s)",
            category: "Population Genetics",
            def: "A quantitative measure of the relative reproductive disadvantage or mortality acting against a specific genotype: s = 1 - W."
        },
        "relative fitness": {
            term: "Relative Fitness (W)",
            category: "Population Genetics",
            def: "The proportional reproductive success and survivability of a genotype relative to the most favored genotype in the population (scaled from 0.0 to 1.0)."
        },
        "overdominance fitness": {
            term: "Overdominance Fitness (Heterozygote Advantage)",
            category: "Population Genetics",
            def: "A balanced genetic state where the heterozygous genotype (Aa) possesses greater biological fitness than either parental homozygote (AA or aa)."
        },
        "balanced polymorphism": {
            term: "Balanced Polymorphism",
            category: "Population Genetics",
            def: "A dynamic equilibrium state where natural selection maintains two or more alternative alleles in a population at stable frequencies across generations."
        },
        "directional selection": {
            term: "Directional Selection",
            category: "Population Genetics",
            def: "Selection favoring phenotypes at one extreme of the distribution curve, progressively shifting the population mean toward that extreme over time."
        },
        "stabilizing selection": {
            term: "Stabilizing Selection",
            category: "Population Genetics",
            def: "Natural selection favoring intermediate phenotypic values while culling extreme variants, thereby reducing variance without shifting the population mean."
        },
        "disruptive selection": {
            term: "Disruptive Selection",
            category: "Population Genetics",
            def: "Selection favoring both phenotypic extremes over intermediate individuals, potentially generating a bimodal distribution within the population."
        },
        "assortative mating": {
            term: "Assortative Mating",
            category: "Population Genetics",
            def: "A non-random mating system where individuals pair based on phenotypic resemblance (positive assortative: like-to-like; negative: unlike-to-unlike)."
        },
        "consanguinity": {
            term: "Consanguinity",
            category: "Population Genetics",
            def: "The biological genetic relationship existing between two individuals who share at least one documented common ancestor in their pedigree."
        },
        "identical by descent": {
            term: "Identical by Descent (IBD)",
            category: "Population Genetics",
            def: "Two homologous alleles at a locus that are physical copies of a single ancestral gene carried by a shared common ancestor (the foundation of Wright's F)."
        },
        "identical by state": {
            term: "Identical by State (IBS)",
            category: "Population Genetics",
            def: "Two alleles at a locus that possess identical nucleotide sequence and function but cannot be proven to originate from a documented common ancestor."
        },
        "fixation": {
            term: "Allele Fixation",
            category: "Population Genetics",
            def: "The state when an allele reaches a frequency of 1.0 (100%) in a population, permanently eliminating all alternative alleles at that locus."
        },
        "loss of heterozygosity": {
            term: "Loss of Heterozygosity",
            category: "Population Genetics",
            def: "The gradual reduction in the proportion of heterozygous gene loci in a closed population due to inbreeding or genetic drift at rate 1 / (2 Ne) per generation."
        },
        "genetic load": {
            term: "Genetic Load",
            category: "Population Genetics",
            def: "The proportional reduction in the average biological fitness of a population compared to a theoretical optimal genotype, caused by deleterious mutations."
        },
        "gene flow": {
            term: "Gene Flow (Migration)",
            category: "Population Genetics",
            def: "The transfer and incorporation of genetic alleles from one population into another through the immigration and interbreeding of animals: Δq = m(qm - q0)."
        },
        "wahlund effect": {
            term: "Wahlund Effect",
            category: "Population Genetics",
            def: "The observed deficiency of heterozygotes that occurs when distinct sub-populations with different gene frequencies are pooled and analyzed as one population."
        },
        "genetic distance": {
            term: "Genetic Distance (Nei's D)",
            category: "Population Genetics",
            def: "A quantitative metric quantifying the degree of genetic divergence and allelic differentiation between two livestock populations or breeds."
        },
        "metric trait": {
            term: "Metric Trait",
            category: "Quantitative Genetics & Inheritance",
            def: "A continuous phenotypic trait that exhibits metric variation and can be measured on a continuous numerical scale (e.g. body weight, fleece yield)."
        },
        "polygenes": {
            term: "Polygenes (Multiple Factors)",
            category: "Quantitative Genetics & Inheritance",
            def: "Multiple non-allelic genes whose individual phenotypic effects are small, additive, and cumulative, jointly governing a quantitative trait."
        },
        "phenotypic value": {
            term: "Phenotypic Value (P)",
            category: "Quantitative Genetics & Inheritance",
            def: "The observable physical measurement or performance record of an animal for a specific metric trait: P = Genotypic Value (G) + Environmental Deviation (E)."
        },
        "genotypic value": {
            term: "Genotypic Value (G)",
            category: "Quantitative Genetics & Inheritance",
            def: "The net genetic value of an individual's complete diploid genotype for a quantitative trait, partitioned as G = A (additive) + D (dominance) + I (epistatic)."
        },
        "environmental deviation": {
            term: "Environmental Deviation (E)",
            category: "Quantitative Genetics & Inheritance",
            def: "The non-genetic component of an individual's phenotype arising from feeding, climate, disease, and management: E = P - G."
        },
        "additive genetic value": {
            term: "Additive Genetic Value (A)",
            category: "Quantitative Genetics & Inheritance",
            def: "The sum of the average effects of the individual genes carried by an animal; it is directly transmissible from parent to progeny and equals breeding value."
        },
        "dominance deviation": {
            term: "Dominance Deviation (D)",
            category: "Quantitative Genetics & Inheritance",
            def: "The non-additive genetic value arising from intra-allelic interactions between paired alleles at the same locus in a diploid individual."
        },
        "epistatic deviation": {
            term: "Epistatic Deviation (I)",
            category: "Quantitative Genetics & Inheritance",
            def: "The non-additive genetic deviation arising from interactions between alleles across two or more different gene loci."
        },
        "permanent environmental variance": {
            term: "Permanent Environmental Variance (VEp)",
            category: "Quantitative Genetics & Inheritance",
            def: "Variance caused by non-genetic environmental events (e.g. chronic mastitis, calfhood injury) that permanently alter all repeated performance records of an animal."
        },
        "temporary environmental variance": {
            term: "Temporary Environmental Variance (VEt)",
            category: "Quantitative Genetics & Inheritance",
            def: "Variance caused by transient, reversible environmental fluctuations (e.g. day-to-day weather, temporary off-feed) affecting only a single measurement."
        },
        "realized heritability": {
            term: "Realized Heritability (h²_R)",
            category: "Quantitative Genetics & Inheritance",
            def: "An empirical estimate of narrow-sense heritability calculated directly from a selection experiment as the ratio of selection response to selection differential: h² = R / S."
        },
        "paternal half-sib correlation": {
            term: "Paternal Half-Sib Correlation (PHS)",
            category: "Quantitative Genetics & Inheritance",
            def: "A widely used ANOVA method for estimating narrow-sense heritability from resemblance among half-sibs sired by common bulls: h² = 4 · t."
        },
        "offspring-parent regression": {
            term: "Offspring-Parent Regression (b_OP)",
            category: "Quantitative Genetics & Inheritance",
            def: "A biometrical regression technique for estimating heritability: h² = 2 · b_OP when regressed on a single parent, or h² = b_O,MP when regressed on mid-parent."
        },
        "full-sib correlation": {
            term: "Full-Sib Correlation",
            category: "Quantitative Genetics & Inheritance",
            def: "Resemblance among full siblings sharing 50% additive variance, 25% dominance variance, and maternal effects; provides an upper-limit estimate of heritability."
        },
        "intraclass correlation": {
            term: "Intraclass Correlation (t)",
            category: "Quantitative Genetics & Inheritance",
            def: "A statistical correlation measuring the degree of resemblance among individuals belonging to the same family or group: t = σ²_between / (σ²_between + σ²_within)."
        },
        "contemporary group": {
            term: "Contemporary Group",
            category: "Quantitative Genetics & Inheritance",
            def: "A cohort of animals of similar age, breed, and physiological state managed under uniform herd-year-season feeding and environmental conditions."
        },
        "contemporary comparison": {
            term: "Contemporary Comparison Method",
            category: "Quantitative Genetics & Inheritance",
            def: "Robertson and Rendel's sire proofing method comparing a bull's daughters directly against contemporary herdmates calving in the same herd, year, and season."
        },
        "maternal effect": {
            term: "Maternal Effect",
            category: "Quantitative Genetics & Inheritance",
            def: "The non-genetic phenotypic contribution of the dam to her offspring mediated through uterine environment, egg cytoplasm, milk yield, and maternal care."
        },
        "co-ancestry": {
            term: "Co-Ancestry (Kinship Coefficient)",
            category: "Quantitative Genetics & Inheritance",
            def: "The probability that two alleles sampled at random from two individuals are identical by descent; equal to the inbreeding coefficient of their offspring."
        },
        "numerator relationship matrix": {
            term: "Numerator Relationship Matrix (A Matrix)",
            category: "Quantitative Genetics & Inheritance",
            def: "A square, symmetric pedigree matrix summarizing the additive genetic relationships between all pairs of animals in a herd, whose inverse (A⁻¹) is used in BLUP."
        },
        "genotype by environment correlation": {
            term: "Genotype by Environment Correlation (r_GE)",
            category: "Quantitative Genetics & Inheritance",
            def: "A situation where different genotypes are non-randomly matched with specific environments (e.g. elite genetic cows receiving superior nutritional care)."
        },
        "economic weight": {
            term: "Economic Weight (Relative Economic Value)",
            category: "Quantitative Genetics & Inheritance",
            def: "The expected change in net farm profit per animal resulting from a one-unit genetic improvement in a trait while keeping other traits constant."
        },
        "aggregate genotype": {
            term: "Aggregate Genotype (Net Economic Breeding Value)",
            category: "Quantitative Genetics & Inheritance",
            def: "The overall economic breeding value of an animal defined as the linear sum of its true breeding values for several traits weighted by their economic weights: H = Σ a_i A_i."
        },
        "correlated response to selection": {
            term: "Correlated Response to Selection (CR)",
            category: "Quantitative Genetics & Inheritance",
            def: "The indirect genetic change observed in an unselected trait Y when artificial selection is practiced on a genetically correlated trait X: CR_Y = i · r_TI_X · r_G · σ_A_Y."
        },
        "threshold trait": {
            term: "Threshold Trait",
            category: "Quantitative Genetics & Inheritance",
            def: "A discontinuous, categorical trait (e.g. disease resistance, twin birth, calving ease) governed by underlying continuous polygenic liability and environmental factors crossing a physiological threshold."
        },
        "individual selection": {
            term: "Individual Selection (Performance Testing)",
            category: "Animal Breeding & Selection Systems",
            def: "Selection of breeding animals based solely on their own phenotypic performance records without considering collateral or ancestral relatives; most effective for traits with high heritability."
        },
        "pedigree index": {
            term: "Pedigree Index (PI)",
            category: "Animal Breeding & Selection Systems",
            def: "An estimate of an individual's breeding value calculated as the average of its parents' estimated breeding values (PI = 0.5 EBV_sire + 0.5 EBV_dam), used prior to the individual's own performance recording."
        },
        "diallel cross": {
            term: "Diallel Crossing",
            category: "Animal Breeding & Selection Systems",
            def: "A systematic mating scheme where a set of inbred parental lines or breeds are crossed in all possible pairwise combinations to evaluate general combining ability (GCA) and specific combining ability (SCA)."
        },
        "animal model": {
            term: "Animal Model (BLUP)",
            category: "Animal Breeding & Selection Systems",
            def: "An advanced mixed-model BLUP methodology that simultaneously predicts breeding values for all animals (males and females) across generations by incorporating the full numerator relationship matrix."
        },
        "sire model": {
            term: "Sire Model",
            category: "Animal Breeding & Selection Systems",
            def: "A mixed-model evaluation method where sires are evaluated based on daughter records with dams assumed to be random and unrelated within herds; historical precursor to full animal models."
        },
        "heterobeltiosis": {
            term: "Heterobeltiosis (Better-Parent Heterosis)",
            category: "Animal Breeding & Selection Systems",
            def: "The phenotypic superiority of an F1 crossbred individual over the better or superior of its two purebred parental breeds: [(F1 - BP) / BP] × 100."
        },
        "synthetic breed": {
            term: "Synthetic Breed (Composite Breed)",
            category: "Animal Breeding & Selection Systems",
            def: "A new livestock breed developed by intermating crossbred progeny of two or more distinct ancestral breeds followed by rigorous inter-se selection (e.g. Karan Swiss, Sunandini cattle)."
        },
        "grading up ratio": {
            term: "Grading Up Progression",
            category: "Animal Breeding & Selection Systems",
            def: "The progressive geometric replacement of native germplasm by purebred exotic germplasm across consecutive generations: 50% in F1, 75% in F2, 87.5% in F3, and 93.75% in F4."
        },
        "rotational crossbreeding": {
            term: "Rotational Crossbreeding (Criss-Crossing)",
            category: "Animal Breeding & Selection Systems",
            def: "A continuous crossbreeding system alternating purebred sires of two or three breeds on crossbred dams, maintaining 67% to 86% of maximum possible F1 heterosis indefinitely."
        },
        "terminal crossbreeding": {
            term: "Terminal Crossbreeding",
            category: "Animal Breeding & Selection Systems",
            def: "A structured commercial crossbreeding system where all crossbred male and female offspring are marketed for slaughter/meat production, with zero replacement females retained for breeding."
        },
        "genomic selection": {
            term: "Genomic Selection (Meuwissen et al.)",
            category: "Animal Breeding & Selection Systems",
            def: "A biotechnology selection system utilizing genome-wide dense SNP markers to calculate Genomic Estimated Breeding Values (GEBV) in newborn calves, halving generation interval."
        },
        "linebreeding": {
            term: "Linebreeding",
            category: "Animal Breeding & Selection Systems",
            def: "A mild, directed form of inbreeding designed to maintain a high genetic relationship to an outstanding ancestor while keeping inbreeding coefficient F below 0.12."
        },
        "outcrossing": {
            term: "Outcrossing",
            category: "Animal Breeding & Selection Systems",
            def: "The mating of unrelated animals belonging to the same pure breed (no common ancestors in the last 4 to 6 generations), introducing fresh vigor."
        },
        "topcrossing": {
            term: "Topcrossing",
            category: "Animal Breeding & Selection Systems",
            def: "The practice of mating purebred or inbred sires to non-inbred or grade females of the same species."
        },
        "backcrossing": {
            term: "Backcrossing (Introgression)",
            category: "Animal Breeding & Selection Systems",
            def: "The repetitive crossing of hybrid progeny back to an elite recurrent parental breed, used to transfer a specific gene (e.g. disease resistance) into an adapted breed."
        },
        "species hybridization": {
            term: "Species Hybridization",
            category: "Animal Breeding & Selection Systems",
            def: "The crossing of individuals belonging to two distinct biological species within the same genus (e.g. male donkey × female horse producing a sterile mule)."
        },
        "general combining ability": {
            term: "General Combining Ability (GCA)",
            category: "Animal Breeding & Selection Systems",
            def: "The average performance of an inbred line or breed across hybrid combinations with multiple tester lines, reflecting additive genetic variance (V_A)."
        },
        "specific combining ability": {
            term: "Specific Combining Ability (SCA)",
            category: "Animal Breeding & Selection Systems",
            def: "The degree to which a specific crossbred combination performs significantly better or worse than expected based on the GCA of the parents, reflecting dominance and epistasis."
        },
        "closed nucleus breeding system": {
            term: "Closed Nucleus Breeding System",
            category: "Animal Breeding & Selection Systems",
            def: "A tiered breeding structure where the elite nucleus herd is strictly closed to outside genetics, resulting in one-way gene flow downwards to commercial herds."
        },
        "multiple ovulation and embryo transfer": {
            term: "Multiple Ovulation and Embryo Transfer (MOET)",
            category: "Animal Breeding & Selection Systems",
            def: "A reproductive biotechnology where elite donor cows are superovulated with FSH and Day 7 embryos are flushed non-surgically and transferred into synchronized recipients."
        },
        "ovum pick-up": {
            term: "Ovum Pick-Up (OPU)",
            category: "Animal Breeding & Selection Systems",
            def: "Transvaginal ultrasound-guided aspiration of immature oocytes from living cows for in-vitro maturation (IVM), in-vitro fertilization (IVF), and embryo culture."
        },
        "sex-sorted semen": {
            term: "Sex-Sorted Semen",
            category: "Animal Breeding & Selection Systems",
            def: "Semen sorted into X- and Y-bearing spermatozoa via flow cytometry based on the 3.8–4.2% higher DNA content of X-sperm in cattle, achieving >90% female calves."
        },
        "in-situ conservation": {
            term: "In-Situ Conservation",
            category: "Animal Breeding & Selection Systems",
            def: "The conservation of livestock populations in their natural agricultural habitat and native agro-ecological breeding tracts by farmers and pastoral communities."
        },
        "ex-situ in-vivo conservation": {
            term: "Ex-Situ In-Vivo Conservation",
            category: "Animal Breeding & Selection Systems",
            def: "The maintenance of live breeding herds of endangered livestock outside their native geographical breeding tract in institutional farms, research stations, or zoos."
        },
        "ex-situ in-vitro conservation": {
            term: "Ex-Situ In-Vitro Cryoconservation",
            category: "Animal Breeding & Selection Systems",
            def: "The long-term preservation of animal genetic resources as cryopreserved semen, ova, embryos, or somatic tissues in liquid nitrogen at -196°C in national gene banks."
        },
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
    },

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
                const escaped = key.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
                const regex = new RegExp(`\\b(${escaped})\\b`, 'i');
                const match = regex.exec(node.nodeValue);

                if (match) {
                    const span = document.createElement('span');
                    const before = node.nodeValue.substring(0, match.index);
                    const matchedText = match[0];
                    const after = node.nodeValue.substring(match.index + matchedText.length);

                    span.innerHTML = `${app.esc(before)}<span class="glossary-term" data-term="${key}" tabindex="0" role="button" aria-label="Definition for ${app.esc(matchedText)}">${app.esc(matchedText)}</span>${app.esc(after)}`;

                    node.parentNode.replaceChild(span, node);
                    replaced = true;
                    break;
                }
            }
        });

        this.attachTooltips(rootElement);
    },

    // One shared definition popup, anchored right next to the word that was hovered or tapped.
    _tip: null,
    _tipTerm: null,
    _hoverTimer: null,

    hideTooltip() {
        clearTimeout(this._hoverTimer);
        if (this._tip) this._tip.remove();
        this._tip = null;
        this._tipTerm = null;
    },

    showTooltip(el) {
        const key = el.dataset.term;
        const data = this.terms[key];
        if (!data) return;
        if (this._tipTerm === el) return;

        this.hideTooltip();

        const tip = document.createElement('div');
        tip.className = 'glossary-tooltip';
        tip.setAttribute('role', 'dialog');
        tip.innerHTML = `
            <div class="glossary-tooltip-head">
                <span class="glossary-tooltip-title">${app.esc(data.term)}</span>
                <button class="glossary-tooltip-close" type="button" aria-label="Close">&times;</button>
            </div>
            <span class="glossary-tooltip-badge">${app.esc(data.category)}</span>
            <div class="glossary-tooltip-body">${app.esc(data.def)}</div>
            <div class="glossary-tooltip-foot">
                <button class="glossary-speak-btn" type="button" aria-label="Listen to pronunciation">
                    ${app.icon('speaker', 'ico--sm')} Listen
                </button>
                <button class="glossary-open-btn" type="button">Open in dictionary &rarr;</button>
            </div>
        `;

        document.body.appendChild(tip);
        this._tip = tip;
        this._tipTerm = el;

        // Place above the word (or below if there is no room), in page coordinates so it stays with the word.
        const rect = el.getBoundingClientRect();
        const tipRect = tip.getBoundingClientRect();
        const gap = 8;

        let top = rect.top - tipRect.height - gap;
        if (top < 10) top = rect.bottom + gap;
        let left = rect.left + (rect.width / 2) - (tipRect.width / 2);
        left = Math.max(10, Math.min(left, document.documentElement.clientWidth - tipRect.width - 10));

        tip.style.top = `${top + window.scrollY}px`;
        tip.style.left = `${left + window.scrollX}px`;
        tip.classList.add('is-visible');

        tip.addEventListener('mouseenter', () => clearTimeout(this._hoverTimer));
        tip.addEventListener('mouseleave', () => this.scheduleHide());
        tip.querySelector('.glossary-tooltip-close').addEventListener('click', () => this.hideTooltip());
        tip.querySelector('.glossary-speak-btn').addEventListener('click', () => this.speak(data.term));
        tip.querySelector('.glossary-open-btn').addEventListener('click', () => {
            this.hideTooltip();
            location.hash = `#/library/glossary/${encodeURIComponent(key)}`;
        });
    },

    scheduleHide() {
        clearTimeout(this._hoverTimer);
        this._hoverTimer = setTimeout(() => this.hideTooltip(), 200);
    },

    attachTooltips(root) {
        const hoverCapable = window.matchMedia('(hover: hover)').matches;

        root.querySelectorAll('.glossary-term').forEach(el => {
            if (hoverCapable) {
                el.addEventListener('mouseenter', () => {
                    clearTimeout(this._hoverTimer);
                    this.showTooltip(el);
                });
                el.addEventListener('mouseleave', () => this.scheduleHide());
            }

            // Tap / click toggles the definition beside the word — it never navigates away.
            el.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                if (this._tipTerm === el && !hoverCapable) this.hideTooltip();
                else this.showTooltip(el);
            });

            el.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    this.showTooltip(el);
                } else if (e.key === 'Escape') {
                    this.hideTooltip();
                }
            });
        });

        if (!this._globalListeners) {
            this._globalListeners = true;
            document.addEventListener('click', (e) => {
                if (this._tip && !e.target.closest('.glossary-tooltip') && !e.target.closest('.glossary-term')) {
                    this.hideTooltip();
                }
            });
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') this.hideTooltip();
            });
            window.addEventListener('hashchange', () => this.hideTooltip());
            window.addEventListener('resize', () => this.hideTooltip());
        }
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

            container.innerHTML = `
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
                            ${app.icon('search', 'search-icon')}
                            <input type="text" class="input glossary-search-input" placeholder="Search terminology, definitions, breeding systems..." value="${app.esc(query)}">
                            ${query ? `<button class="search-clear-btn" aria-label="Clear search">&times;</button>` : ''}
                        </div>

                        <div class="glossary-categories">
                            <button class="chip ${activeCat === 'all' ? 'chip--active' : ''}" data-cat="all">
                                All Categories (${Object.keys(glossary.terms).length})
                            </button>
                            ${categories.map(c => `
                                <button class="chip ${activeCat === c ? 'chip--active' : ''}" data-cat="${app.esc(c)}">
                                    ${app.esc(c)} (${glossary.categories[c].length})
                                </button>
                            `).join('')}
                        </div>
                    </div>

                    <div class="glossary-grid">
                        ${filteredKeys.length ? filteredKeys.map(k => {
                            const item = glossary.terms[k];
                            return `
                                <div class="glossary-card">
                                    <div class="glossary-card-head">
                                        <div class="glossary-card-term">${app.esc(item.term)}</div>
                                        <button class="glossary-audio-btn" data-word="${app.esc(item.term)}" title="Pronounce term" aria-label="Pronounce ${app.esc(item.term)}">
                                            ${app.icon('speaker', 'ico--sm')}
                                        </button>
                                    </div>
                                    <div class="glossary-card-cat">${app.esc(item.category)}</div>
                                    <div class="glossary-card-def">${app.esc(item.def)}</div>
                                </div>
                            `;
                        }).join('') : `
                            <div class="empty-state">
                                <div class="empty-state__icon">${app.icon('help')}</div>
                                <h3>No glossary terms match your search</h3>
                                <p class="text-muted">Try a different search term or select another category filter.</p>
                            </div>
                        `}
                    </div>
                </div>
            `;

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
