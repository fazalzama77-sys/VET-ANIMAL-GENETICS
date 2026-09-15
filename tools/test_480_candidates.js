const fs = require('fs');
const path = require('path');

const glossaryContent = fs.readFileSync(path.join(__dirname, '../js/glossary.js'), 'utf8');
const fn = new Function('window', 'app', glossaryContent + '; return glossary;');
const glossary = fn({}, { esc: s => s, icon: s => s });

const existingKeys = new Set(Object.keys(glossary.terms).map(k => k.toLowerCase()));
console.log('Existing terms in js/glossary.js:', existingKeys.size);

const candidates = [
    // Cat 1: Biostatistics & Experimental Design (10)
    "class interval",
    "class mark",
    "relative frequency",
    "cumulative frequency",
    "bar chart",
    "pie chart",
    "coefficient of alienation",
    "standard normal distribution",
    "continuity correction",
    "studentized range",

    // Cat 2: Classical & Mendelian Genetics (10)
    "wild type",
    "mutant allele",
    "amorphic allele",
    "hypomorphic allele",
    "hypermorphic allele",
    "neomorphic allele",
    "antimorphic allele",
    "maternal inheritance",
    "extranuclear inheritance",
    "heteroplasmy",

    // Cat 3: Cytogenetics & Molecular Genetics (15)
    "allopolyploidy",
    "autopolyploidy",
    "endoreduplication",
    "sister chromatid exchange",
    "fragile site",
    "fluorescence in situ hybridization",
    "reverse transcriptase",
    "cdna library",
    "genomic library",
    "plasmid",
    "promoter",
    "enhancer",
    "silencer",
    "ribozyme",
    "epigenetics",

    // Cat 4: Population Genetics (15)
    "demographic bottleneck",
    "admixture",
    "cline",
    "coalescence",
    "effective breeding number",
    "heterozygosity",
    "panmictic population",
    "fitness component",
    "subpopulation",
    "metapopulation",
    "purging",
    "inbreeding load",
    "haldane rule",
    "isolation by distance",
    "neutral theory",

    // Cat 5: Quantitative Genetics & Inheritance (15)
    "infinitesimal variance",
    "full-sib family",
    "half-sib family",
    "co-ancestry matrix",
    "permanent environmental ratio",
    "epistatic variance component",
    "dominance variance component",
    "relative economic weight",
    "selection index weight",
    "restricted selection index",
    "desired gains index",
    "correlated selection differential",
    "realized response",
    "intra-herd sire evaluation",
    "multi-trait model",

    // Cat 6: Animal Breeding & Selection Systems (15)
    "animal model blup",
    "sire-maternal grandsire model",
    "deregressed breeding value",
    "marker-assisted selection",
    "candidate gene approach",
    "genome-wide association study",
    "composite cattle breed",
    "purebred breeding",
    "criss-crossing",
    "three-breed rotational cross",
    "two-breed terminal cross",
    "three-breed terminal cross",
    "breed complementarity",
    "juvenile in vitro embryo technology",
    "somatoplasm vs germplasm"
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
    console.log(`400 + ${candidates.length} = ${400 + candidates.length} total terms!`);
}
