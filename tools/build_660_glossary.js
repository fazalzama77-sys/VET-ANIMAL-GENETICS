// tools/build_660_glossary.js
// Assembles and generates the expanded 660-term glossary for Animal Genetics and Breeding Studio

const fs = require('fs');
const path = require('path');

const GLOSSARY_PATH = path.join(__dirname, '../js/glossary.js');
const REPO_GLOSSARY_PATH = path.join(__dirname, '../repo/js/glossary.js');

// 30 new exam-specific terms (expanding 630 to exactly 660)
const NEW_TERMS = {
    // 1. Biostatistics & Experimental Design (5 new terms -> 110 total)
    "sum of squares": {
        term: "Sum of Squares (SS)",
        category: "Biostatistics & Experimental Design",
        def: "The sum of squared deviations of individual observations from their group or grand mean [Σ(X_i - X̄)²], forming the fundamental numerator partitioned into Treatment SS and Error SS in ANOVA."
    },
    "mean square": {
        term: "Mean Square (MS)",
        category: "Biostatistics & Experimental Design",
        def: "An ANOVA variance estimate obtained by dividing a Sum of Squares (SS) by its associated degrees of freedom (df); the ratio of Treatment MS to Error MS gives the F-statistic."
    },
    "homoscedasticity": {
        term: "Homoscedasticity",
        category: "Biostatistics & Experimental Design",
        def: "The statistical assumption that all treatment populations or regression error terms share equal finite variance (σ₁² = σ₂² = ... = σ_k²), a core prerequisite for valid linear regression and ANOVA."
    },
    "fisher exact test": {
        term: "Fisher's Exact Test",
        category: "Biostatistics & Experimental Design",
        def: "An exact non-parametric significance test for 2×2 contingency tables of categorical counts used when small sample sizes or expected cell frequencies (< 5) invalidate standard chi-square approximations."
    },
    "incomplete block design": {
        term: "Balanced Incomplete Block Design (BIBD)",
        category: "Biostatistics & Experimental Design",
        def: "An experimental layout where block size is smaller than the total number of treatments (e.g. twin-lamb or littermate trials), structured so every pair of treatments occurs together equally often within blocks."
    },

    // 2. Classical & Mendelian Genetics (5 new terms -> 110 total)
    "meiotic drive": {
        term: "Meiotic Drive (Segregation Distortion)",
        category: "Classical & Mendelian Genetics",
        def: "A non-Mendelian transmission bias in which one allele of a heterozygote is preferentially recovered in more than 50% of functional gametes during gametogenesis, distorting expected Mendelian ratios."
    },
    "paramutation": {
        term: "Paramutation",
        category: "Classical & Mendelian Genetics",
        def: "A heritable epigenetic interaction between two alleles at a single locus where one paramutagenic allele stably alters the transcriptional state of a sensitive paramutable partner allele across subsequent generations."
    },
    "genomic imprinting": {
        term: "Genomic Imprinting",
        category: "Classical & Mendelian Genetics",
        def: "An epigenetic parent-of-origin phenomenon in mammals where only the maternal or paternal allele of specific autosomal genes is expressed while the other is silenced via differential germline DNA methylation (e.g. Callipyge sheep, IGF2 in swine)."
    },
    "loss-of-function mutation": {
        term: "Loss-of-Function Mutation",
        category: "Classical & Mendelian Genetics",
        def: "A genetic mutation that reduces (hypomorphic) or completely abolishes (amorphic/null) the normal biochemical function of the encoded protein, typically inherited as an autosomal recessive allele (e.g. BLAD, Myostatin double muscling)."
    },
    "gain-of-function mutation": {
        term: "Gain-of-Function Mutation",
        category: "Classical & Mendelian Genetics",
        def: "A mutation conferring enhanced activity (hypermorphic) or a completely novel spatial/temporal biochemical function (neomorphic) on the gene product, characteristically exhibiting dominant inheritance."
    },

    // 3. Cytogenetics & Molecular Genetics (5 new terms -> 115 total)
    "chimerism": {
        term: "Genetic Chimerism",
        category: "Cytogenetics & Molecular Genetics",
        def: "The coexistence within a single animal of two or more genetically distinct cell populations derived from separate zygotes, famously occurring as XX/XY leukocyte chimerism in heterosexual bovine freemartin twins via placental vascular anastomosis."
    },
    "mosaicism": {
        term: "Genetic Mosaicism",
        category: "Cytogenetics & Molecular Genetics",
        def: "The presence of two or more genetically distinct cell lineages within a single organism arising from post-zygotic mitotic mutation or nondisjunction within one original fertilized zygote."
    },
    "nondisjunction": {
        term: "Chromosomal Nondisjunction",
        category: "Cytogenetics & Molecular Genetics",
        def: "The failure of homologous chromosomes (Meiosis I) or sister chromatids (Meiosis II / Mitosis) to separate properly to opposite poles, generating aneuploid gametes and zygotes such as trisomics (2n+1) or monosomics (2n-1)."
    },
    "copy number variation": {
        term: "Copy Number Variation (CNV)",
        category: "Cytogenetics & Molecular Genetics",
        def: "Submicroscopic structural genomic polymorphisms (≥ 50 bp to megabases) where chromosomal segments are duplicated or deleted across individuals, influencing disease resistance, coat patterning (e.g. Tobiano/White spotting), and production traits."
    },
    "next-generation sequencing": {
        term: "Next-Generation Sequencing (NGS)",
        category: "Cytogenetics & Molecular Genetics",
        def: "High-throughput massively parallel DNA/RNA sequencing technologies generating millions of short or long reads simultaneously for whole-genome resequencing, SNP discovery, and RNA-seq transcriptomics."
    },

    // 4. Population Genetics (5 new terms -> 95 total)
    "allelic richness": {
        term: "Allelic Richness (A_r)",
        category: "Population Genetics",
        def: "A measure of population genetic diversity counting the mean number of distinct alleles per locus standardized by rarefaction to the smallest sample size, making it more sensitive to recent bottlenecks than heterozygosity."
    },
    "tajima d": {
        term: "Tajima's D Statistic",
        category: "Population Genetics",
        def: "A population genetics neutrality test comparing pairwise nucleotide differences against segregating sites to detect departures from neutral evolution such as selective sweeps, population bottlenecks, or balancing selection."
    },
    "runs of homozygosity": {
        term: "Runs of Homozygosity (ROH)",
        category: "Population Genetics",
        def: "Long, contiguous chromosomal tracts of homozygous SNP genotypes inherited identically by descent from a common ancestor; ROH length distinguishes ancient (short tracts) from recent (long tracts) inbreeding."
    },
    "genetic rescue": {
        term: "Genetic Rescue",
        category: "Population Genetics",
        def: "The intentional introduction of unrelated individuals or gametes into a small, inbred, endangered population to mask fixed deleterious recessive alleles, boost heterozygosity, and restore reproductive fitness."
    },
    "outbreeding depression": {
        term: "Outbreeding Depression",
        category: "Population Genetics",
        def: "A decline in fitness, fertility, or survival observed in hybrids (often F2 or backcrosses) resulting from crossing genetically divergent populations adapted to distinct environments, disrupting co-adapted gene complexes."
    },

    // 5. Quantitative Genetics & Inheritance (5 new terms -> 110 total)
    "quantitative trait locus": {
        term: "Quantitative Trait Locus (QTL)",
        category: "Quantitative Genetics & Inheritance",
        def: "A mapped chromosomal region harboring one or more polymorphic genes that statistically explain a measurable fraction of phenotypic variation in a polygenic quantitative trait (e.g. DGAT1 QTL on BTA14 for milk fat percentage)."
    },
    "reml": {
        term: "Restricted Maximum Likelihood (REML)",
        category: "Quantitative Genetics & Inheritance",
        def: "The gold-standard iterative statistical method for estimating additive genetic, environmental, and residual variance components in unbalanced animal breeding datasets while accounting for fixed effects and selection bias."
    },
    "reaction norm": {
        term: "Norm of Reaction (Reaction Norm)",
        category: "Quantitative Genetics & Inheritance",
        def: "A mathematical curve depicting how a single genotype produces a range of phenotypic outcomes across a continuous environmental gradient (e.g. temperature-humidity index or plane of nutrition), visualizing G × E interaction."
    },
    "canalization": {
        term: "Genetic Canalization",
        category: "Quantitative Genetics & Inheritance",
        def: "The developmental buffering capacity of an organism's genetic network (Waddington) to produce a uniform, stable wild-type phenotype despite minor environmental fluctuations or background genetic mutations."
    },
    "phenotypic plasticity": {
        term: "Phenotypic Plasticity",
        category: "Quantitative Genetics & Inheritance",
        def: "The ability of an individual carrying a fixed genotype to alter its physiology, morphology, or production level reversibly or developmentally in direct response to changing environmental conditions."
    },

    // 6. Animal Breeding & Selection Systems (5 new terms -> 120 total)
    "corrective mating": {
        term: "Corrective (Compensatory) Mating",
        category: "Animal Breeding & Selection Systems",
        def: "A planned non-random mating strategy pairing females possessing a specific conformational or functional weakness with sires strong in that exact trait to produce balanced, structurally sound progeny."
    },
    "breeding objective": {
        term: "Breeding Objective (Aggregate Genotype H)",
        category: "Animal Breeding & Selection Systems",
        def: "A formal economic definition of the long-term genetic improvement goal for a livestock enterprise, expressed as a weighted linear sum of true breeding values for all economically important traits (H = Σ v_i BV_i)."
    },
    "dissemination of genetic gain": {
        term: "Dissemination of Genetic Gain (Breeding Pyramid)",
        category: "Animal Breeding & Selection Systems",
        def: "The hierarchical flow of improved germplasm downward from elite nucleus breeding herds through multiplier units (via AI, MOET, or breeding males) to commercial production herds, accompanied by a characteristic genetic lag."
    },
    "gene bank": {
        term: "Animal Gene Bank (Cryobank)",
        category: "Animal Breeding & Selection Systems",
        def: "A dedicated national or regional biological repository (such as NBAGR Cryobank) storing deep-frozen semen, embryos, oocytes, and somatic DNA from diverse indigenous and endangered breeds as insurance against genetic erosion."
    },
    "parentage verification": {
        term: "DNA Parentage Verification",
        category: "Animal Breeding & Selection Systems",
        def: "Molecular confirmation of true biological sire and dam identity using standardized ISAG microsatellite (STR) or SNP panels, preventing pedigree misidentification errors that depress genetic gain and BLUP accuracy."
    }
};

function main() {
    console.log('Loading existing js/glossary.js (630 terms)...');
    const originalContent = fs.readFileSync(GLOSSARY_PATH, 'utf8');

    const fn = new Function('window', 'app', originalContent + '; return glossary;');
    const oldGlossary = fn({}, { esc: s => s, icon: s => s });

    const existingTermKeys = Object.keys(oldGlossary.terms);
    console.log(`Loaded ${existingTermKeys.length} existing terms.`);

    const newKeys = Object.keys(NEW_TERMS);
    console.log(`Prepared ${newKeys.length} new terms.`);

    if (newKeys.length !== 30) {
        throw new Error(`Expected exactly 30 new terms, found ${newKeys.length}`);
    }

    const existingSet = new Set(existingTermKeys.map(k => k.toLowerCase()));
    const overlaps = newKeys.filter(k => existingSet.has(k.toLowerCase()));
    if (overlaps.length > 0) {
        throw new Error(`Found overlapping keys between existing and new: ${overlaps.join(', ')}`);
    }

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

    const mergedTerms = { ...oldGlossary.terms, ...NEW_TERMS };
    const totalTermKeys = Object.keys(mergedTerms);
    console.log(`Total merged terms: ${totalTermKeys.length}`);

    if (totalTermKeys.length !== 660) {
        throw new Error(`Expected total 660 terms, found ${totalTermKeys.length}`);
    }

    let totalCategoryKeys = 0;
    console.log('\nCategory breakdown after merge:');
    for (const [cat, keys] of Object.entries(mergedCategories)) {
        console.log(`  ${cat}: ${keys.length} terms`);
        totalCategoryKeys += keys.length;
    }
    if (totalCategoryKeys !== 660) {
        throw new Error(`Expected category total 660, found ${totalCategoryKeys}`);
    }

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

    console.log('\nWriting 660-term expanded glossary to js/glossary.js...');
    fs.writeFileSync(GLOSSARY_PATH, jsCode, 'utf8');

    if (fs.existsSync(path.dirname(REPO_GLOSSARY_PATH))) {
        console.log('Mirroring 660-term expanded glossary to repo/js/glossary.js...');
        fs.writeFileSync(REPO_GLOSSARY_PATH, jsCode, 'utf8');
    }

    console.log('Successfully generated 660-term glossary!');
}

main();
