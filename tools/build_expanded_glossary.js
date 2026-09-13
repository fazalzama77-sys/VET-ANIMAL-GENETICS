// tools/build_expanded_glossary.js
// Assembles and generates the expanded 277-term glossary for Animal Genetics and Breeding Studio

const fs = require('fs');
const path = require('path');

const GLOSSARY_PATH = path.join(__dirname, '../js/glossary.js');
const REPO_GLOSSARY_PATH = path.join(__dirname, '../repo/js/glossary.js');

// 150 new exam-specific terms
const NEW_TERMS = {
    // 1. Biostatistics & Experimental Design (25 new terms)
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

    // 2. Classical & Mendelian Genetics (25 new terms)
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

    // 3. Cytogenetics & Molecular Genetics (30 new terms)
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

    // 4. Population Genetics (20 new terms)
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

    // 5. Quantitative Genetics & Inheritance (25 new terms)
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

    // 6. Animal Breeding & Selection Systems (25 new terms)
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
    }
};

function main() {
    console.log('Loading existing js/glossary.js...');
    const originalContent = fs.readFileSync(GLOSSARY_PATH, 'utf8');

    // Parse existing glossary object
    const fn = new Function('window', 'app', originalContent + '; return glossary;');
    const oldGlossary = fn({}, { esc: s => s, icon: s => s });

    const existingTermKeys = Object.keys(oldGlossary.terms);
    console.log(`Loaded ${existingTermKeys.length} existing terms.`);

    const newKeys = Object.keys(NEW_TERMS);
    console.log(`Prepared ${newKeys.length} new terms.`);

    if (newKeys.length !== 150) {
        throw new Error(`Expected exactly 150 new terms, found ${newKeys.length}`);
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

    if (totalTermKeys.length !== 277) {
        throw new Error(`Expected total 277 terms, found ${totalTermKeys.length}`);
    }

    let totalCategoryKeys = 0;
    console.log('\nCategory breakdown after merge:');
    for (const [cat, keys] of Object.entries(mergedCategories)) {
        console.log(`  ${cat}: ${keys.length} terms`);
        totalCategoryKeys += keys.length;
    }
    if (totalCategoryKeys !== 277) {
        throw new Error(`Expected category total 277, found ${totalCategoryKeys}`);
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

    console.log('Writing expanded glossary to js/glossary.js...');
    fs.writeFileSync(GLOSSARY_PATH, jsCode, 'utf8');

    console.log('Mirroring expanded glossary to repo/js/glossary.js...');
    fs.writeFileSync(REPO_GLOSSARY_PATH, jsCode, 'utf8');

    console.log('Successfully generated and mirrored 277-term glossary!');
}

main();
