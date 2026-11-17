// tools/build_630_glossary.js
// Assembles and generates the expanded 630-term glossary for Animal Genetics and Breeding Studio

const fs = require('fs');
const path = require('path');

const GLOSSARY_PATH = path.join(__dirname, '../js/glossary.js');
const REPO_GLOSSARY_PATH = path.join(__dirname, '../repo/js/glossary.js');

// 90 new exam-specific terms (expanding 540 to exactly 630)
const NEW_TERMS = {
    // 1. Biostatistics & Experimental Design (15 new terms -> 105 total)
    "alternative hypothesis": {
        term: "Alternative Hypothesis (H₁ / Hₐ)",
        category: "Biostatistics & Experimental Design",
        def: "The research hypothesis proposed against the null hypothesis (H₀), asserting that a statistically significant biological difference, treatment effect, or correlation truly exists in the population."
    },
    "level of significance": {
        term: "Level of Significance (α)",
        category: "Biostatistics & Experimental Design",
        def: "The pre-selected threshold probability (commonly α = 0.05 or 0.01) of committing a Type I error—wrongly rejecting a true null hypothesis."
    },
    "p-value": {
        term: "P-Value (Probability Value)",
        category: "Biostatistics & Experimental Design",
        def: "The exact probability of obtaining an observed test statistic at least as extreme as the sample result assuming the null hypothesis (H₀) is true; H₀ is rejected when P ≤ α."
    },
    "mann-whitney u test": {
        term: "Mann-Whitney U Test",
        category: "Biostatistics & Experimental Design",
        def: "A non-parametric rank-sum hypothesis test used to compare differences between two independent sample groups when data violate normal distribution assumptions, serving as the distribution-free alternative to the unpaired t-test."
    },
    "kruskal-wallis test": {
        term: "Kruskal-Wallis H Test",
        category: "Biostatistics & Experimental Design",
        def: "A rank-based non-parametric equivalent of one-way ANOVA used to test whether three or more independent experimental groups originate from the same distribution."
    },
    "wilcoxon signed-rank test": {
        term: "Wilcoxon Signed-Rank Test",
        category: "Biostatistics & Experimental Design",
        def: "A non-parametric statistical test comparing two related, paired, or repeated biological measurements when the paired differences cannot be assumed to follow a normal distribution."
    },
    "duncan multiple range test": {
        term: "Duncan's Multiple Range Test (DMRT)",
        category: "Biostatistics & Experimental Design",
        def: "A stepwise post-hoc multiple comparison procedure used after a significant ANOVA F-test to identify which specific treatment group means differ significantly from each other."
    },
    "tukey hsd test": {
        term: "Tukey's Honestly Significant Difference (HSD) Test",
        category: "Biostatistics & Experimental Design",
        def: "A conservative post-hoc pairwise comparison test using the studentized range distribution (q) to compare all possible pairs of treatment means while controlling the family-wise Type I error rate."
    },
    "analysis of covariance": {
        term: "Analysis of Covariance (ANCOVA)",
        category: "Biostatistics & Experimental Design",
        def: "A statistical technique combining ANOVA and linear regression to evaluate treatment effects on a dependent variable while mathematically adjusting for the influence of one or more continuous covariates (e.g. initial body weight)."
    },
    "box-and-whisker plot": {
        term: "Box-and-Whisker Plot",
        category: "Biostatistics & Experimental Design",
        def: "A standardized graphical summary displaying a dataset's minimum, first quartile (Q₁), median (Q₂), third quartile (Q₃), maximum, interquartile range, and statistical outliers."
    },
    "histogram": {
        term: "Histogram",
        category: "Biostatistics & Experimental Design",
        def: "A contiguous vertical bar graph representing the frequency distribution of continuous grouped quantitative data, where bar area is proportional to class frequency."
    },
    "scatter diagram": {
        term: "Scatter Diagram (Scatter Plot)",
        category: "Biostatistics & Experimental Design",
        def: "A two-dimensional Cartesian plot of paired observations (X, Y) used to visually inspect the direction, linearity, strength, and potential outliers of a bivariate relationship."
    },
    "sampling error": {
        term: "Sampling Error",
        category: "Biostatistics & Experimental Design",
        def: "The random discrepancy between a sample statistic (such as x̄) and the true population parameter (μ) arising purely by chance from observing only a subset rather than the complete population."
    },
    "non-sampling error": {
        term: "Non-Sampling Error",
        category: "Biostatistics & Experimental Design",
        def: "Systematic or human errors introduced during data collection, weighing, recording, non-response, instrument calibration failure, or coding mistakes, which occur even in a complete census."
    },
    "central limit theorem": {
        term: "Central Limit Theorem (CLT)",
        category: "Biostatistics & Experimental Design",
        def: "A foundational statistical theorem stating that the sampling distribution of sample means approaches a normal distribution with mean μ and variance σ²/n as sample size n increases, regardless of the parent population's shape."
    },

    // 2. Classical & Mendelian Genetics (15 new terms -> 105 total)
    "law of purity of gametes": {
        term: "Law of Purity of Gametes",
        category: "Classical & Mendelian Genetics",
        def: "An alternative statement of Mendel's First Law affirming that alleles of a heterozygous pair remain completely distinct without blending and segregate cleanly so each gamete receives only a single unmodified allele."
    },
    "recessive epistasis": {
        term: "Recessive Epistasis (Supplementary Gene 9:3:4 Ratio)",
        category: "Classical & Mendelian Genetics",
        def: "A two-locus epistatic interaction where homozygosity for a recessive allele at one locus (aa) completely masks phenotypic expression of alleles at a second hypostatic locus (B/b), yielding a 9:3:4 F2 ratio (e.g. Labrador coat color)."
    },
    "duplicate recessive epistasis": {
        term: "Duplicate Recessive Epistasis (9:7 Ratio)",
        category: "Classical & Mendelian Genetics",
        def: "A complementary gene interaction in which homozygous recessive status at either of two separate loci (aa or bb) produces the identical mutant phenotype, modifying the F2 dihybrid ratio to 9:7."
    },
    "polymeric gene interaction": {
        term: "Polymeric Gene Interaction (9:6:1 Ratio)",
        category: "Classical & Mendelian Genetics",
        def: "An epistatic interaction between two independent loci controlling the same trait where dominant alleles at either locus alone give an intermediate phenotype, both together produce an enhanced phenotype, and double recessives show the base phenotype (9:6:1)."
    },
    "conditional lethal gene": {
        term: "Conditional Lethal Gene",
        category: "Classical & Mendelian Genetics",
        def: "A mutant allele that causes death only under specific restrictive environmental conditions (e.g. heat stress, cold, nutrient deficiency, or drug exposure) while permitting normal survival under permissive conditions."
    },
    "gametic lethal gene": {
        term: "Gametic Lethal Gene",
        category: "Classical & Mendelian Genetics",
        def: "A lethal allele causing the inviability or functional failure of gametes carrying it (either sperm or ova), resulting in distorted transmission ratios and failure of fertilization."
    },
    "hemizygous": {
        term: "Hemizygous",
        category: "Classical & Mendelian Genetics",
        def: "The genetic condition of a diploid individual possessing only a single copy of a gene or chromosomal segment, normally observed in heterogametic males (XY) for X-linked genes and heterogametic female birds (ZW) for Z-linked genes."
    },
    "linkage group": {
        term: "Linkage Group",
        category: "Classical & Mendelian Genetics",
        def: "All gene loci residing on the same physical chromosome that tend to be inherited together during meiosis; the maximum number of linkage groups equals the haploid chromosome number (n) of the species."
    },
    "synteny": {
        term: "Synteny",
        category: "Classical & Mendelian Genetics",
        def: "The physical co-localization of two or more genetic loci on the same chromosome, regardless of whether they are close enough to exhibit genetic linkage or undergo independent assortment (>50 cM apart)."
    },
    "genetic anticipation": {
        term: "Genetic Anticipation",
        category: "Classical & Mendelian Genetics",
        def: "A transmission phenomenon in which a genetic disorder manifests at progressively earlier ages and with increased clinical severity in successive generations, often driven by unstable trinucleotide repeat expansion."
    },
    "incomplete penetrance": {
        term: "Incomplete Penetrance",
        category: "Classical & Mendelian Genetics",
        def: "The failure of some individuals carrying a disease-causing or trait-determining genotype to express the expected phenotype at all, resulting in penetrance below 100%."
    },
    "variable expressivity": {
        term: "Variable Expressivity",
        category: "Classical & Mendelian Genetics",
        def: "Differences in the clinical severity, extent, or anatomical degree to which a trait is manifested among individuals who possess the exact same mutant genotype (e.g. polydactyly digit counts)."
    },
    "intragenic complementation": {
        term: "Intragenic (Allelic) Complementation",
        category: "Classical & Mendelian Genetics",
        def: "The restoration of partial wild-type function when two distinct mutant alleles of the very same gene encode defective polypeptides that assemble into a functional multimeric protein complex."
    },
    "uniparental inheritance": {
        term: "Uniparental Inheritance",
        category: "Classical & Mendelian Genetics",
        def: "Non-Mendelian transmission of genetic material exclusively from one parent (usually the dam via oocyte cytoplasm/mitochondria) to all progeny of both sexes."
    },
    "pedigree chart": {
        term: "Pedigree Chart",
        category: "Classical & Mendelian Genetics",
        def: "A standardized diagrammatic family tree tracing ancestral relationships and phenotypic expression across generations (squares for males, circles for females) to infer mode of inheritance and carrier status."
    },

    // 3. Cytogenetics & Molecular Genetics (15 new terms -> 110 total)
    "leptotene": {
        term: "Leptotene Stage",
        category: "Cytogenetics & Molecular Genetics",
        def: "The initial substage of meiotic prophase I in which duplicated chromatin condenses into fine, thread-like chromosomes attached at their telomeres to the nuclear envelope prior to synapsis."
    },
    "diakinesis": {
        term: "Diakinesis Stage",
        category: "Cytogenetics & Molecular Genetics",
        def: "The fifth and final substage of meiotic prophase I marked by maximal chromosome condensation, terminalization of chiasmata, nucleolar disappearance, and nuclear envelope breakdown."
    },
    "tetrasomy": {
        term: "Tetrasomy (2n + 2)",
        category: "Cytogenetics & Molecular Genetics",
        def: "An aneuploid chromosomal state in which one specific homologous chromosome is represented four times instead of twice (2n + 2) within an otherwise diploid somatic cell."
    },
    "euploidy": {
        term: "Euploidy",
        category: "Cytogenetics & Molecular Genetics",
        def: "A chromosomal constitution in which the somatic chromosome number is an exact integer multiple of the basic monoploid set (x), encompassing haploidy (n), diploidy (2n), and polyploidy (3n, 4n)."
    },
    "histone modification": {
        term: "Histone Modification",
        category: "Cytogenetics & Molecular Genetics",
        def: "Reversible post-translational covalent alterations (acetylation, methylation, phosphorylation, ubiquitination) of histone N-terminal tails that remodel chromatin compaction and regulate gene transcription."
    },
    "x-chromosome inactivation": {
        term: "X-Chromosome Inactivation (Lyonization)",
        category: "Cytogenetics & Molecular Genetics",
        def: "The random, irreversible epigenetic silencing of one of the two X chromosomes in female mammalian somatic cells during early embryogenesis via XIST non-coding RNA, forming a condensed Barr body."
    },
    "operon model": {
        term: "Operon Model",
        category: "Cytogenetics & Molecular Genetics",
        def: "A prokaryotic transcriptional regulatory unit (Jacob and Monod) consisting of an operator, promoter, and clustered structural genes transcribed together into a single polycistronic mRNA under shared repressor/inducer control."
    },
    "intron": {
        term: "Intron (Intervening Sequence)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A non-coding nucleotide segment inside a eukaryotic gene that is transcribed into pre-mRNA but subsequently excised by the spliceosome before mature mRNA export and translation."
    },
    "exon": {
        term: "Exon (Expressed Sequence)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A conserved gene segment retained in mature mRNA after RNA splicing, encoding functional amino acid domains as well as the 5' and 3' untranslated regions (UTRs)."
    },
    "rna splicing": {
        term: "RNA Splicing",
        category: "Cytogenetics & Molecular Genetics",
        def: "The post-transcriptional nuclear processing mechanism catalyzed by the spliceosome that removes introns from pre-mRNA and ligates adjacent exons into a continuous coding transcript."
    },
    "alternative splicing": {
        term: "Alternative Splicing",
        category: "Cytogenetics & Molecular Genetics",
        def: "The regulated differential inclusion or exclusion of specific exons from a single pre-mRNA transcript, enabling one eukaryotic gene to produce multiple structurally and functionally distinct protein isoforms."
    },
    "genetic code": {
        term: "Genetic Code",
        category: "Cytogenetics & Molecular Genetics",
        def: "The nearly universal, degenerate, non-overlapping, and comma-less triplet nucleotide system (64 codons) specifying the 20 standard amino acids (plus 3 stop codons) during ribosomal polypeptide synthesis."
    },
    "primer": {
        term: "Oligonucleotide Primer",
        category: "Cytogenetics & Molecular Genetics",
        def: "A short, single-stranded synthetic DNA or RNA sequence (typically 18–25 nucleotides) complementary to a target template that provides a free 3'-OH group required by DNA polymerase to initiate strand synthesis in PCR or replication."
    },
    "amplified fragment length polymorphism": {
        term: "Amplified Fragment Length Polymorphism (AFLP)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A high-throughput, dominant molecular DNA fingerprinting technique combining restriction enzyme digestion, adapter ligation, and selective PCR amplification to detect genome-wide polymorphism without prior sequence knowledge."
    },
    "random amplified polymorphic dna": {
        term: "Random Amplified Polymorphic DNA (RAPD)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A PCR-based molecular marker assay utilizing a single short (~10 bp) arbitrary oligonucleotide primer at low annealing temperatures to amplify anonymous polymorphic genomic segments."
    },

    // 4. Population Genetics (15 new terms -> 90 total)
    "disassortative mating": {
        term: "Disassortative (Negative Assortative) Mating",
        category: "Population Genetics",
        def: "A non-random mating pattern in which phenotypically dissimilar individuals mate more frequently than expected by chance, increasing population heterozygosity and maintaining genetic polymorphism."
    },
    "linkage disequilibrium": {
        term: "Linkage Disequilibrium (LD)",
        category: "Population Genetics",
        def: "The non-random statistical association of alleles at two or more distinct loci on chromosomes in a population (D = P_AB - p_A p_B ≠ 0), decaying progressively over generations through recombination."
    },
    "selective sweep": {
        term: "Selective Sweep",
        category: "Population Genetics",
        def: "The rapid reduction or elimination of nucleotide diversity at flanking neutral markers adjacent to a beneficial mutation as intense positive selection drives the favored haplotype toward fixation."
    },
    "hitchhiking effect": {
        term: "Genetic Hitchhiking",
        category: "Population Genetics",
        def: "The indirect change in frequency of a neutral or mildly deleterious allele simply because it is physically linked on the same chromosome to a nearby locus undergoing strong positive selection."
    },
    "heterozygote disadvantage": {
        term: "Heterozygote Disadvantage (Underdominance)",
        category: "Population Genetics",
        def: "A form of selection in which heterozygotes possess lower Darwinian fitness than either homozygote, leading to an unstable equilibrium and eventual fixation of one allele depending on initial frequencies."
    },
    "transient polymorphism": {
        term: "Transient Polymorphism",
        category: "Population Genetics",
        def: "Temporary genetic variation at a locus observed while a newly favored mutant allele is actively sweeping through a population toward complete fixation, replacing the ancestral allele."
    },
    "neutral mutation": {
        term: "Neutral Mutation",
        category: "Population Genetics",
        def: "A DNA sequence alteration (such as synonymous third-codon substitutions or non-coding variants) that neither enhances nor impairs an organism's Darwinian fitness, evolving predominantly via random genetic drift."
    },
    "molecular clock": {
        term: "Molecular Clock Hypothesis",
        category: "Population Genetics",
        def: "The principle (Zuckerkandl & Pauling) that neutral nucleotide or amino acid substitutions accumulate across homologous DNA/protein sequences at an approximately constant rate over evolutionary time, allowing estimation of breed divergence dates."
    },
    "polymorphic information content": {
        term: "Polymorphic Information Content (PIC)",
        category: "Population Genetics",
        def: "A standard index measuring the informativeness and discriminatory power of a genetic marker locus in linkage mapping and parentage verification based on the number and frequencies of its alleles."
    },
    "observed heterozygosity": {
        term: "Observed Heterozygosity (H_o)",
        category: "Population Genetics",
        def: "The actual directly counted proportion of genotyped individuals in a population sample that carry two different alleles at a given marker locus."
    },
    "expected heterozygosity": {
        term: "Expected Heterozygosity (H_e / Gene Diversity)",
        category: "Population Genetics",
        def: "The theoretical proportion of heterozygotes expected at a locus under Hardy-Weinberg equilibrium (H_e = 1 - Σ p_i²), widely used to quantify breed genetic diversity."
    },
    "nei genetic distance": {
        term: "Nei's Standard Genetic Distance (D)",
        category: "Population Genetics",
        def: "A widely applied statistical metric (D = -ln I) quantifying evolutionary divergence and accumulated allele frequency differences between two livestock breeds or populations based on normalized genetic identity."
    },
    "hardy-weinberg assumptions": {
        term: "Hardy-Weinberg Equilibrium Assumptions",
        category: "Population Genetics",
        def: "The idealized conditions required for stable allele and genotype frequencies: infinitely large population size, random mating (panmixia), and complete absence of selection, mutation, and migration."
    },
    "sex-linked gene frequency": {
        term: "Sex-Linked Locus Allele Frequency",
        category: "Population Genetics",
        def: "In a diploid population where males are hemizygous (XY) and females are homogametic (XX), allele frequencies initially differing between sexes oscillate and converge asymptotically toward equilibrium (q̄ = (2q_f + q_m)/3) rather than stabilizing in a single generation."
    },
    "equilibrium under selection and mutation": {
        term: "Mutation-Selection Equilibrium",
        category: "Population Genetics",
        def: "The stable balance reached in a population when the rate at which deleterious recessive alleles are continuously generated by recurrent forward mutation (u) equals the rate at which selection (s) eliminates them: q̂ = √(u/s)."
    },

    // 5. Quantitative Genetics & Inheritance (15 new terms -> 105 total)
    "producing ability": {
        term: "Producing Ability (PA)",
        category: "Quantitative Genetics & Inheritance",
        def: "The sum of an individual's total genetic merit (G) plus its permanent environmental deviation (E_p), representing the expected average phenotypic performance across repeated records of that animal (e.g. lifetime milk yield)."
    },
    "transmitting ability": {
        term: "Transmitting Ability (TA / PTA)",
        category: "Quantitative Genetics & Inheritance",
        def: "One-half of an animal's additive breeding value (½ BV), representing the average genetic superiority or inferiority an individual passes on to its offspring relative to the breed base."
    },
    "expected progeny difference": {
        term: "Expected Progeny Difference (EPD)",
        category: "Quantitative Genetics & Inheritance",
        def: "A genetic evaluation metric widely used in beef cattle, sheep, and swine equal to one-half of an animal's Estimated Breeding Value (EBV), predicting how future offspring of a sire will perform compared to the average of other sires."
    },
    "estimated breeding value": {
        term: "Estimated Breeding Value (EBV)",
        category: "Quantitative Genetics & Inheritance",
        def: "The statistically predicted additive genetic merit of an individual for a quantitative trait computed using BLUP or selection index methodology from own performance, pedigree relatives, and progeny records."
    },
    "regression of offspring on one parent": {
        term: "Single-Parent Offspring Regression (b_OP)",
        category: "Quantitative Genetics & Inheritance",
        def: "A classical quantitative genetics estimator where the linear regression coefficient of offspring phenotypic values on one parent's phenotype estimates half the narrow-sense heritability (h² = 2 × b_OP)."
    },
    "selection limit": {
        term: "Selection Limit (Selection Plateau)",
        category: "Quantitative Genetics & Inheritance",
        def: "The biological ceiling reached after many generations of intense directional selection where additive genetic variance (V_A) is exhausted through allele fixation or opposing natural selection, halting further genetic progress."
    },
    "asymmetry of response": {
        term: "Asymmetrical Selection Response",
        category: "Quantitative Genetics & Inheritance",
        def: "The common empirical observation in divergent two-way selection experiments where upward and downward selection lines achieve unequal magnitudes of genetic response due to dominance, scaling, genetic drift, or maternal effects."
    },
    "meristic trait": {
        term: "Meristic Quantitative Trait",
        category: "Quantitative Genetics & Inheritance",
        def: "A polygenic trait expressed in discrete whole-number counts rather than continuous measurements (such as litter size, number of vertebrae, or eggs laid per clutch), influenced by both genetic and environmental factors."
    },
    "scale effect": {
        term: "Scale Effect (Scale Transformation)",
        category: "Quantitative Genetics & Inheritance",
        def: "Measurement distortion in quantitative traits where variance scales proportionally with the mean or non-additive interactions appear spuriously, corrected via logarithmic, square-root, or arc-sine transformations."
    },
    "additive by additive variance": {
        term: "Additive × Additive Epistatic Variance (V_AA)",
        category: "Quantitative Genetics & Inheritance",
        def: "The component of epistatic genetic variance arising from two-locus interactions between breeding values at independent loci, partially transmissible across generations via selection."
    },
    "additive by dominance variance": {
        term: "Additive × Dominance Epistatic Variance (V_AD)",
        category: "Quantitative Genetics & Inheritance",
        def: "The non-additive genetic variance fraction generated by interactions between the additive effect of alleles at one locus and the intra-locus dominance deviation at another locus."
    },
    "dominance by dominance variance": {
        term: "Dominance × Dominance Epistatic Variance (V_DD)",
        category: "Quantitative Genetics & Inheritance",
        def: "The non-additive epistatic variance arising from interaction between heterozygote dominance deviations across two separate loci, broken up completely by Mendelian segregation and recombination."
    },
    "phenotypic covariance": {
        term: "Phenotypic Covariance (Cov_P)",
        category: "Quantitative Genetics & Inheritance",
        def: "The measurable statistical covariance between two distinct traits recorded on the same animals, equaling the sum of additive genetic covariance (Cov_A) and environmental covariance (Cov_E)."
    },
    "falconer formula": {
        term: "Falconer's Repeatability & Variance Partitioning",
        category: "Quantitative Genetics & Inheritance",
        def: "The quantitative genetic framework partitioning repeated-measure variance into permanent variance (V_G + V_Ep) and temporary environmental variance (V_Et), setting the upper theoretical limit for broad-sense heritability (h_B² ≤ r)."
    },
    "maternal genetic effect": {
        term: "Maternal Genetic Effect (m)",
        category: "Quantitative Genetics & Inheritance",
        def: "The heritable genetic influence of a dam on her offspring's early phenotype mediated through uterine nutrition, colostrum quality, milk yield, and maternal behavior rather than the genes directly inherited by the calf."
    },

    // 6. Animal Breeding & Selection Systems (15 new terms -> 115 total)
    "indirect selection": {
        term: "Indirect Selection",
        category: "Animal Breeding & Selection Systems",
        def: "Selecting breeding stock based on a secondary indicator trait (Y) rather than the target trait (X) directly—advantageous when trait Y is genetically correlated with X, more heritable, measurable earlier in life, or expressed in both sexes (e.g. scrotal circumference for daughter puberty)."
    },
    "recurrent selection": {
        term: "Recurrent Selection",
        category: "Animal Breeding & Selection Systems",
        def: "A cyclical crossbreeding selection scheme in which individuals from an outbred population are selected based on the performance of their testcross progeny produced by mating with a constant inbred tester line to exploit specific combining ability."
    },
    "introgression": {
        term: "Gene Introgression",
        category: "Animal Breeding & Selection Systems",
        def: "The targeted transfer of a specific desirable allele (e.g. polledness, heat tolerance SLICK gene, or FecB fecundity gene) from a donor breed into an adapted recipient breed via an F1 cross followed by repeated marker-assisted backcrossing."
    },
    "single-step gblup": {
        term: "Single-Step Genomic BLUP (ssGBLUP)",
        category: "Animal Breeding & Selection Systems",
        def: "An advanced unified mixed-model genetic evaluation method constructing a blended relationship matrix (H) that simultaneously incorporates pedigree (A) and SNP marker genomic (G) relationships for both genotyped and ungenotyped animals."
    },
    "genotype imputation": {
        term: "Genotype Imputation",
        category: "Animal Breeding & Selection Systems",
        def: "A statistical haplotype reconstruction process inferring missing high-density SNP genotypes in animals tested on inexpensive low-density SNP panels by referencing a densely genotyped breed reference panel."
    },
    "reproductive cloning": {
        term: "Somatic Cell Nuclear Transfer (SCNT)",
        category: "Animal Breeding & Selection Systems",
        def: "An assisted reproductive biotechnology in which the diploid nucleus of a somatic donor cell is transferred into an enucleated oocyte to produce a genetically identical nuclear clone (e.g. Dolly the sheep, Garima buffalo)."
    },
    "in vitro fertilization": {
        term: "In Vitro Fertilization (IVF / IVP)",
        category: "Animal Breeding & Selection Systems",
        def: "Laboratory maturation of harvested oocytes followed by co-incubation with capacitated spermatozoa and culture to the blastocyst stage prior to surgical or non-surgical transfer into synchronized recipient females."
    },
    "transgenesis": {
        term: "Animal Transgenesis",
        category: "Animal Breeding & Selection Systems",
        def: "The stable introduction of exogenous recombinant DNA constructs (transgenes) into an animal's germline genome via pronuclear microinjection, viral vectors, or CRISPR-Cas9 to confer novel physiological traits or pharmaceutical protein expression."
    },
    "breed characterization": {
        term: "Phenotypic & Molecular Breed Characterization",
        category: "Animal Breeding & Selection Systems",
        def: "Systematic documentation of morphological traits, production metrics, adaptive resilience, geographic distribution, and microsatellite/SNP diversity of indigenous animal populations to establish official breed registration."
    },
    "effective population size threshold": {
        term: "FAO Minimum Effective Population Size (N_e = 50)",
        category: "Animal Breeding & Selection Systems",
        def: "The international conservation guideline limiting inbreeding rate to ≤ 1% per generation (ΔF = 1 / 2N_e ≤ 0.01), requiring a minimum effective breeding population size of N_e ≥ 50 to prevent acute inbreeding depression."
    },
    "pedigree completeness index": {
        term: "Pedigree Completeness Index (PCI)",
        category: "Animal Breeding & Selection Systems",
        def: "A quantitative metric (MacCluer et al.) measuring the proportion of known ancestors across paternal and maternal lineages over a specified number of generations, critical for obtaining unbiased inbreeding and BLUP estimates."
    },
    "generation of inbreeding": {
        term: "Rate of Inbreeding (ΔF)",
        category: "Animal Breeding & Selection Systems",
        def: "The proportional decrease in population heterozygosity per generation, approximated in idealized random-mating populations as ΔF = 1 / (2N_e) or 1/(8N_m) + 1/(8N_f) under unequal sex numbers."
    },
    "optimal contribution selection": {
        term: "Optimal Contribution Selection (OCS)",
        category: "Animal Breeding & Selection Systems",
        def: "A dynamic mating optimization algorithm balancing maximum genetic gain (EBV/GEBV) against a strict constraint on average co-ancestry among selected parents, controlling long-term inbreeding while sustaining genetic variance."
    },
    "embryo cryopreservation": {
        term: "Embryo & Oocyte Cryopreservation",
        category: "Animal Breeding & Selection Systems",
        def: "Ultra-rapid vitrification or controlled slow freezing of mammalian pre-implantation embryos and oocytes in liquid nitrogen (-196°C) using cryoprotectants to conserve complete diploid maternal and paternal genomes indefinitely."
    },
    "genomic relationship matrix": {
        term: "Genomic Relationship Matrix (G-Matrix)",
        category: "Animal Breeding & Selection Systems",
        def: "A realized genetic similarity matrix (VanRaden) computed directly from genome-wide SNP allele sharing across animals, capturing Mendelian sampling deviations more accurately than expected pedigree co-ancestry (A)."
    }
};

function main() {
    console.log('Loading existing js/glossary.js (540 terms)...');
    const originalContent = fs.readFileSync(GLOSSARY_PATH, 'utf8');

    // Parse existing glossary object
    const fn = new Function('window', 'app', originalContent + '; return glossary;');
    const oldGlossary = fn({}, { esc: s => s, icon: s => s });

    const existingTermKeys = Object.keys(oldGlossary.terms);
    console.log(`Loaded ${existingTermKeys.length} existing terms.`);

    const newKeys = Object.keys(NEW_TERMS);
    console.log(`Prepared ${newKeys.length} new terms.`);

    if (newKeys.length !== 90) {
        throw new Error(`Expected exactly 90 new terms, found ${newKeys.length}`);
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

    if (totalTermKeys.length !== 630) {
        throw new Error(`Expected total 630 terms, found ${totalTermKeys.length}`);
    }

    let totalCategoryKeys = 0;
    console.log('\nCategory breakdown after merge:');
    for (const [cat, keys] of Object.entries(mergedCategories)) {
        console.log(`  ${cat}: ${keys.length} terms`);
        totalCategoryKeys += keys.length;
    }
    if (totalCategoryKeys !== 630) {
        throw new Error(`Expected category total 630, found ${totalCategoryKeys}`);
    }

    // Construct clean JS output preserving exact runtime methods from js/glossary.js
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

    const termEntries = Object.entries(mergedTerms);
    termEntries.forEach(([key, val], idx) => {
        const isLast = idx === termEntries.length - 1;
        jsCode += `        ${JSON.stringify(key)}: {\n`;
        jsCode += `            term: ${JSON.stringify(val.term)},\n`;
        jsCode += `            category: ${JSON.stringify(val.category)},\n`;
        jsCode += `            def: ${JSON.stringify(val.def)}\n`;
        jsCode += `        }${isLast ? '' : ','}\n`;
    });

    const tailMarker = `    // Return flat array of all terms for search indexing and library view`;
    const tailIndex = originalContent.indexOf(tailMarker);
    if (tailIndex === -1) {
        throw new Error('Could not locate tail runtime methods in js/glossary.js');
    }
    const tailCode = originalContent.slice(tailIndex);

    jsCode += `    },\n\n` + tailCode;

    console.log('\nWriting 630-term expanded glossary to js/glossary.js...');
    fs.writeFileSync(GLOSSARY_PATH, jsCode, 'utf8');

    if (fs.existsSync(path.dirname(REPO_GLOSSARY_PATH))) {
        console.log('Mirroring 630-term expanded glossary to repo/js/glossary.js...');
        fs.writeFileSync(REPO_GLOSSARY_PATH, jsCode, 'utf8');
    }

    console.log('Successfully generated 630-term glossary!');
}

main();
