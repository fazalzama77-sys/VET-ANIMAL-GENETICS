const fs = require('fs');
const path = require('path');

const glossaryContent = fs.readFileSync(path.join(__dirname, '../js/glossary.js'), 'utf8');
const fn = new Function('window', 'app', glossaryContent + '; return glossary;');
const glossary = fn({}, { esc: s => s, icon: s => s });

const existingKeys = new Set(Object.keys(glossary.terms).map(k => k.toLowerCase()));
console.log('Existing terms in js/glossary.js:', existingKeys.size);

const candidates = [
    // Cat 1: Biostatistics & Experimental Design (10)
    "frequency density",
    "standard error of difference of means",
    "confidence interval",
    "pooled variance",
    "bartlett test",
    "f-distribution",
    "coefficient of concordance",
    "standard error of proportion",
    "multistage sampling",
    "factorial experiment",

    // Cat 2: Classical & Mendelian Genetics (10)
    "criss-cross inheritance",
    "holandric gene",
    "pseudoautosomal region",
    "genocopy",
    "cryptic gene",
    "isochromosome arms",
    "trihybrid ratio",
    "chiasma frequency",
    "complementation group",
    "paracentric loop",

    // Cat 3: Cytogenetics & Molecular Genetics (10)
    "karyotyping technique",
    "centromeric index",
    "arm ratio",
    "nucleosome core",
    "telomerase",
    "dna polymerase iii",
    "topoisomerase",
    "single nucleotide polymorphism",
    "dna methylation",
    "real-time pcr",

    // Cat 4: Population Genetics (10)
    "panmictic index f",
    "gene frequency drift",
    "selection coefficient against recessive",
    "recurrent mutation",
    "reverse mutation rate",
    "island model migration rate",
    "heterozygote advantage model",
    "inbreeding depression in fitness",
    "gametic disequilibrium coefficient",
    "effective population size ratio",

    // Cat 5: Quantitative Genetics & Inheritance (10)
    "infinitesimal polygenic model",
    "breeding value accuracy",
    "intra-class correlation repeatability",
    "variance due to permanent environment",
    "variance due to temporary environment",
    "paternal half-sib heritability",
    "mid-parent heritability",
    "single parent regression heritability",
    "additive genetic correlation",
    "correlated response formula",

    // Cat 6: Animal Breeding & Selection Systems (10)
    "equal parent index",
    "contemporary comparison sire proof",
    "sire model mixed equations",
    "blup animal model inverse a",
    "genomic selection reliability",
    "criss-cross breeding heterosis",
    "three-breed rotational heterosis",
    "two-breed terminal crossbreeding",
    "three-breed terminal crossbreeding",
    "ex-situ in-vitro cryo-banking"
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
    console.log(`480 + ${candidates.length} = ${480 + candidates.length} total terms!`);
}
