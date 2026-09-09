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
            "non-parametric test"
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
            "recombination frequency"
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
            "sanger sequencing"
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
            "polymorphism"
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
            "environmental correlation"
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
            "cryoconservation"
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
        }
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
                tip.innerHTML = `
                    <div class="glossary-tooltip-head">
                        <span class="glossary-tooltip-title">${app.esc(data.term)}</span>
                        <span class="glossary-tooltip-badge">${app.esc(data.category)}</span>
                    </div>
                    <div class="glossary-tooltip-body">${app.esc(data.def)}</div>
                    <div class="glossary-tooltip-foot">
                        <button class="glossary-speak-btn" type="button" aria-label="Listen to pronunciation">
                            ${app.icon('speaker', 'ico--sm')} Listen
                        </button>
                        <span class="glossary-tooltip-hint">Click for dictionary</span>
                    </div>
                `;

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

                tip.style.top = `${top + window.scrollY}px`;
                tip.style.left = `${left}px`;
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
                location.hash = `#/library/glossary?q=${encodeURIComponent(el.dataset.term)}`;
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
