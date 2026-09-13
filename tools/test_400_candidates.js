const fs = require('fs');
const path = require('path');

const glossaryContent = fs.readFileSync(path.join(__dirname, '../js/glossary.js'), 'utf8');
const fn = new Function('window', 'app', glossaryContent + '; return glossary;');
const glossary = fn({}, { esc: s => s, icon: s => s });

const existingKeys = new Set(Object.keys(glossary.terms).map(k => k.toLowerCase()));
console.log('Existing terms in js/glossary.js:', existingKeys.size);

const candidates = [
    // Cat 1: Biostatistics (18)
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
    "split-plot design",

    // Cat 2: Mendelian (23)
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
    "muton",

    // Cat 3: Cytogenetics & Molecular (18)
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
    "crispr-cas9",

    // Cat 4: Population Genetics (18)
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
    "gametic phase disequilibrium",

    // Cat 5: Quantitative Genetics (26)
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
    "pleiotropic effect on covariance",

    // Cat 6: Breeding (20)
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
];

console.log('Total candidate terms:', candidates.length);

// Check for internal duplicates
const candidateSet = new Set();
const internalDuplicates = [];
candidates.forEach(c => {
    const low = c.toLowerCase();
    if (candidateSet.has(low)) internalDuplicates.push(low);
    candidateSet.add(low);
});

if (internalDuplicates.length) {
    console.error('Internal duplicates in candidates:', internalDuplicates);
} else {
    console.log('✓ Zero internal duplicates in candidates.');
}

// Check collisions with existing
const collisions = candidates.filter(c => existingKeys.has(c.toLowerCase()));
if (collisions.length) {
    console.error('Collisions with existing terms:', collisions);
} else {
    console.log('✓ Zero collisions with existing terms!');
    console.log(`277 + ${candidates.length} = ${277 + candidates.length} total terms!`);
}
