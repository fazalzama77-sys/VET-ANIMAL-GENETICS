// tools/build_480_glossary.js
// Assembles and generates the expanded 480-term glossary for Animal Genetics and Breeding Studio

const fs = require('fs');
const path = require('path');

const GLOSSARY_PATH = path.join(__dirname, '../js/glossary.js');
const REPO_GLOSSARY_PATH = path.join(__dirname, '../repo/js/glossary.js');

// 80 new exam-specific terms (expanding 400 to exactly 480)
const NEW_TERMS = {
    // 1. Biostatistics & Experimental Design (10 new terms -> 80 total)
    "class interval": {
        term: "Class Interval",
        category: "Biostatistics & Experimental Design",
        def: "The numerical width or range of quantitative values that defines each group or bin in a continuous grouped frequency distribution."
    },
    "class mark": {
        term: "Class Mark (Mid-Value)",
        category: "Biostatistics & Experimental Design",
        def: "The exact midpoint value of a class interval calculated as the arithmetic average of its lower and upper class limits: (L1 + L2) / 2."
    },
    "relative frequency": {
        term: "Relative Frequency",
        category: "Biostatistics & Experimental Design",
        def: "The proportion or fractional share of total observations falling within a specific class interval, calculated as class frequency divided by total sample size (f_i / N)."
    },
    "cumulative frequency": {
        term: "Cumulative Frequency",
        category: "Biostatistics & Experimental Design",
        def: "The running cumulative total of frequencies accumulated from the lowest interval up to the boundary of a given class interval."
    },
    "bar chart": {
        term: "Bar Chart (Bar Diagram)",
        category: "Biostatistics & Experimental Design",
        def: "A visual statistical chart that represents discrete categories of biological data using rectangular bars with lengths proportional to frequencies."
    },
    "pie chart": {
        term: "Pie Chart (Sector Diagram)",
        category: "Biostatistics & Experimental Design",
        def: "A circular statistical graphic divided into proportional angular sectors where each sector angle equals (Component Frequency / Total) × 360°."
    },
    "coefficient of alienation": {
        term: "Coefficient of Alienation (k)",
        category: "Biostatistics & Experimental Design",
        def: "A statistical index measuring the proportion of unexplained variation between two variables: k = √(1 - r²)."
    },
    "standard normal distribution": {
        term: "Standard Normal Distribution (Z-Distribution)",
        category: "Biostatistics & Experimental Design",
        def: "A standardized normal probability curve with a mean of zero (μ = 0) and a standard deviation of one (σ = 1), where Z = (X - μ) / σ."
    },
    "continuity correction": {
        term: "Continuity Correction (±0.5)",
        category: "Biostatistics & Experimental Design",
        def: "A correction factor of ±0.5 added or subtracted when approximating a discrete probability distribution (Binomial or Poisson) with a continuous normal curve."
    },
    "studentized range": {
        term: "Studentized Range (q-Statistic)",
        category: "Biostatistics & Experimental Design",
        def: "The difference between the sample maximum and sample minimum observations divided by the pooled standard error, used in Tukey's HSD post-hoc test."
    },

    // 2. Classical & Mendelian Genetics (10 new terms -> 80 total)
    "wild type": {
        term: "Wild-Type Allele (+)",
        category: "Classical & Mendelian Genetics",
        def: "The standard, non-mutant allele or phenotype that occurs with highest natural prevalence in an unselected wild population, designated with a plus (+) symbol."
    },
    "mutant allele": {
        term: "Mutant Allele",
        category: "Classical & Mendelian Genetics",
        def: "An altered nucleotide sequence arising from a mutation in a wild-type gene, producing an altered phenotype or modified biochemical function."
    },
    "amorphic allele": {
        term: "Amorphic Allele (Null Mutation)",
        category: "Classical & Mendelian Genetics",
        def: "A mutant allele causing complete loss of gene function, synthesizing zero active protein product or non-functional transcript."
    },
    "hypomorphic allele": {
        term: "Hypomorphic Allele (Leaky Mutation)",
        category: "Classical & Mendelian Genetics",
        def: "A mutant allele that produces a reduced quantity or partially active form of the normal gene product, resulting in a weakened phenotype."
    },
    "hypermorphic allele": {
        term: "Hypermorphic Allele (Gain-of-Function)",
        category: "Classical & Mendelian Genetics",
        def: "A mutant allele that produces an increased quantity of the wild-type gene product or possesses abnormally elevated catalytic activity."
    },
    "neomorphic allele": {
        term: "Neomorphic Allele",
        category: "Classical & Mendelian Genetics",
        def: "A mutant allele whose expression produces a completely novel gene product or generates an ectopic phenotypic manifestation not seen in wild-type individuals."
    },
    "antimorphic allele": {
        term: "Antimorphic Allele (Dominant-Negative)",
        category: "Classical & Mendelian Genetics",
        def: "A mutant allele whose defective gene product actively antagonizes, competes with, or inactivates the function of the co-expressed wild-type protein."
    },
    "maternal inheritance": {
        term: "Maternal Inheritance",
        category: "Classical & Mendelian Genetics",
        def: "Strict non-Mendelian extranuclear transmission where progeny phenotypes are determined solely by organellar genes (mitochondrial DNA) inherited exclusively through the egg cytoplasm."
    },
    "extranuclear inheritance": {
        term: "Extranuclear (Cytoplasmic) Inheritance",
        category: "Classical & Mendelian Genetics",
        def: "The transmission of hereditary traits governed by self-replicating genes located outside the nucleus in cytoplasmic organelles (mitochondria and chloroplasts)."
    },
    "heteroplasmy": {
        term: "Heteroplasmy",
        category: "Classical & Mendelian Genetics",
        def: "The intracellular coexistence of two or more genetically distinct populations of organellar genomes (such as wild-type and mutated mitochondrial DNA) within a single eukaryotic cell."
    },

    // 3. Cytogenetics & Molecular Genetics (15 new terms -> 85 total)
    "allopolyploidy": {
        term: "Allopolyploidy",
        category: "Cytogenetics & Molecular Genetics",
        def: "A polyploid condition resulting from the interspecific hybridization of two distinct ancestral species followed by chromosome doubling (amphidiploidy)."
    },
    "autopolyploidy": {
        term: "Autopolyploidy",
        category: "Cytogenetics & Molecular Genetics",
        def: "A polyploid state where an organism possesses three or more complete homologous chromosome sets derived entirely from within the same species."
    },
    "endoreduplication": {
        term: "Endoreduplication",
        category: "Cytogenetics & Molecular Genetics",
        def: "A modified cell cycle where chromosomal DNA replicates repeatedly in the absence of mitosis or cytokinesis, generating multistranded polytene chromosomes."
    },
    "sister chromatid exchange": {
        term: "Sister Chromatid Exchange (SCE)",
        category: "Cytogenetics & Molecular Genetics",
        def: "The reciprocal exchange of homologous DNA segments between sister chromatids during DNA replication and repair, detected via 5-bromodeoxyuridine (BrdU) harlequin staining."
    },
    "fragile site": {
        term: "Chromosomal Fragile Site",
        category: "Cytogenetics & Molecular Genetics",
        def: "Specific non-staining gaps or constrictions on metaphase chromosomes that exhibit high susceptibility to breakage, gap formation, and sister chromatid exchange."
    },
    "fluorescence in situ hybridization": {
        term: "Fluorescence In Situ Hybridization (FISH)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A molecular cytogenetic technique using fluorophore-labeled single-stranded DNA probes that anneal to complementary metaphase chromosomes to map specific gene loci."
    },
    "reverse transcriptase": {
        term: "Reverse Transcriptase (RNA-Directed DNA Polymerase)",
        category: "Cytogenetics & Molecular Genetics",
        def: "An enzyme that synthesizes a complementary DNA strand (cDNA) from a single-stranded messenger RNA template, essential for retroviral replication and RT-PCR."
    },
    "cdna library": {
        term: "cDNA Library",
        category: "Cytogenetics & Molecular Genetics",
        def: "A collection of cloned host vectors containing complementary DNA fragments reverse-transcribed from cellular mRNA, representing only transcriptionally active expressed genes."
    },
    "genomic library": {
        term: "Genomic DNA Library",
        category: "Cytogenetics & Molecular Genetics",
        def: "A comprehensive clone collection representing the entire nuclear and organellar genomic DNA of an organism, including coding exons, introns, and non-coding repetitive DNA."
    },
    "plasmid": {
        term: "Plasmid Vector",
        category: "Cytogenetics & Molecular Genetics",
        def: "A small, circular, extrachromosomal double-stranded DNA molecule capable of autonomous replication in bacteria, engineered with multiple cloning sites and antibiotic selection markers."
    },
    "promoter": {
        term: "Core Promoter",
        category: "Cytogenetics & Molecular Genetics",
        def: "A non-coding upstream DNA regulatory sequence that binds the basal transcription machinery and RNA polymerase II to initiate transcription at the correct start site."
    },
    "enhancer": {
        term: "Enhancer Element",
        category: "Cytogenetics & Molecular Genetics",
        def: "A cis-acting regulatory DNA sequence that binds activator transcription factors to significantly increase transcription initiation, operating independently of distance and orientation."
    },
    "silencer": {
        term: "Silencer Element",
        category: "Cytogenetics & Molecular Genetics",
        def: "A DNA regulatory sequence that binds repressor proteins to suppress, downregulate, or silence the transcriptional initiation of an associated gene."
    },
    "ribozyme": {
        term: "Ribozyme (Catalytic RNA)",
        category: "Cytogenetics & Molecular Genetics",
        def: "An RNA molecule possessing enzymatic catalytic activity capable of cutting and splicing phosphodiester bonds, such as the peptidyl transferase center of 28S rRNA."
    },
    "epigenetics": {
        term: "Epigenetics",
        category: "Cytogenetics & Molecular Genetics",
        def: "Mitotically and meiotically heritable changes in gene expression and cellular function that occur without any alteration in the underlying DNA nucleotide sequence (e.g. DNA methylation)."
    },

    // 4. Population Genetics (15 new terms -> 65 total)
    "demographic bottleneck": {
        term: "Demographic Bottleneck",
        category: "Population Genetics",
        def: "A drastic, sharp reduction in population size caused by environmental calamity or epidemic disease, resulting in severe loss of rare alleles and intensified genetic drift."
    },
    "admixture": {
        term: "Genetic Admixture",
        category: "Population Genetics",
        def: "The introduction of novel alleles and genetic combinations into a population through interbreeding between individuals from two or more previously isolated gene pools."
    },
    "cline": {
        term: "Genetic Cline",
        category: "Population Genetics",
        def: "A gradual, continuous geographical or ecological gradient in the frequency of a genetic allele or phenotypic character across the spatial range of a species."
    },
    "coalescence": {
        term: "Coalescent Theory",
        category: "Population Genetics",
        def: "A retrospective population genetics model that traces all present-day homologous alleles backward through genealogical history to their most recent common ancestral allele."
    },
    "effective breeding number": {
        term: "Effective Breeding Number (Nb)",
        category: "Population Genetics",
        def: "The effective number of breeding males and females that successfully contribute fertile progeny to the next generation, determining the rate of random genetic drift."
    },
    "heterozygosity": {
        term: "Observed Heterozygosity (Ho)",
        category: "Population Genetics",
        def: "The proportion of individuals in a sampled livestock population that carry two distinct alternative alleles at a designated gene locus."
    },
    "panmictic population": {
        term: "Panmictic Population",
        category: "Population Genetics",
        def: "An idealized, infinitely large biological population in which every individual has an equal probability of mating with any individual of the opposite sex."
    },
    "fitness component": {
        term: "Fitness Component",
        category: "Population Genetics",
        def: "A distinct life-history stage contributing to an animal's lifetime reproductive fitness, including embryonic survival, pre-weaning viability, age at sexual maturity, and fertility."
    },
    "subpopulation": {
        term: "Subpopulation (Deme)",
        category: "Population Genetics",
        def: "A geographically or reproductively semi-isolated localized breeding subdivision within a broader metapopulation, having characteristic internal gene frequencies."
    },
    "metapopulation": {
        term: "Metapopulation",
        category: "Population Genetics",
        def: "A regional network of spatially separated local livestock subpopulations or herds connected by occasional animal migration, gene flow, and recolonization."
    },
    "purging": {
        term: "Purging of Genetic Load",
        category: "Population Genetics",
        def: "The gradual reduction and selective elimination of deleterious recessive mutations from an inbred population through natural or artificial selection acting on exposed homozygotes."
    },
    "inbreeding load": {
        term: "Inbreeding Load",
        category: "Population Genetics",
        def: "The hidden reservoir of harmful, sublethal, and deleterious recessive alleles carried in a heterozygous state in an outbred population, revealed under inbreeding."
    },
    "haldane rule": {
        term: "Haldane's Rule",
        category: "Population Genetics",
        def: "The evolutionary generalization stating that when one sex is absent, rare, or sterile in interspecific F1 hybrid crosses, that sex is the heterogametic sex (XY in mammals, ZW in poultry)."
    },
    "isolation by distance": {
        term: "Isolation by Distance (Wright)",
        category: "Population Genetics",
        def: "The accumulation of genetic differentiation among local populations across a continuous geographic range due to limited dispersal and localized mating."
    },
    "neutral theory": {
        term: "Neutral Theory of Molecular Evolution (Kimura)",
        category: "Population Genetics",
        def: "Motoo Kimura's evolutionary paradigm postulating that the vast majority of evolutionary changes at the molecular DNA and protein level are selectively neutral and fixed by genetic drift."
    },

    // 5. Quantitative Genetics & Inheritance (15 new terms -> 80 total)
    "infinitesimal variance": {
        term: "Infinitesimal Genetic Variance",
        category: "Quantitative Genetics & Inheritance",
        def: "The additive genetic variance generated under the infinitesimal model, which remains essentially constant over short-term selection due to the immense number of contributing loci."
    },
    "full-sib family": {
        term: "Full-Sib Family",
        category: "Quantitative Genetics & Inheritance",
        def: "A group of progeny sharing both the same biological sire and dam, sharing on average 50% of their additive genes and 25% of their dominance combinations (R = 0.50)."
    },
    "half-sib family": {
        term: "Half-Sib Family",
        category: "Quantitative Genetics & Inheritance",
        def: "A cohort of offspring sharing one common parent (usually the sire) while having different opposite parents (dams), sharing on average 25% of their additive genetic merit (R = 0.25)."
    },
    "co-ancestry matrix": {
        term: "Kinship (Co-Ancestry) Matrix (K)",
        category: "Quantitative Genetics & Inheritance",
        def: "A square, symmetric pedigree matrix containing the kinship coefficients between all pairs of animals, where each entry K_ij equals half of Wright's additive relationship A_ij."
    },
    "permanent environmental ratio": {
        term: "Permanent Environmental Ratio (c²)",
        category: "Quantitative Genetics & Inheritance",
        def: "The proportion of total phenotypic variance attributable to permanent non-genetic environmental influences: c² = V_Ep / V_P."
    },
    "epistatic variance component": {
        term: "Epistatic Variance Partitioning",
        category: "Quantitative Genetics & Inheritance",
        def: "The subdivision of total epistatic variance into additive × additive (V_AA), additive × dominance (V_AD), and dominance × dominance (V_DD) interaction variances."
    },
    "dominance variance component": {
        term: "Dominance Variance Component (V_D)",
        category: "Quantitative Genetics & Inheritance",
        def: "The portion of total genetic variance resulting from interaction between paired alleles at the same locus; it is non-transmissible directly from parents to progeny."
    },
    "relative economic weight": {
        term: "Relative Economic Weight (a_i)",
        category: "Quantitative Genetics & Inheritance",
        def: "The expected change in net farm profit per animal resulting from a one-unit genetic increase in a trait while keeping other traits in the breeding goal constant."
    },
    "selection index weight": {
        term: "Selection Index Coefficient (b_i)",
        category: "Quantitative Genetics & Inheritance",
        def: "The weighting factor assigned to phenotypic trait X_i in a multi-trait selection index (I = Σ b_i X_i), calculated by solving Hazel's matrix equation: P · b = G · a."
    },
    "restricted selection index": {
        term: "Restricted Selection Index (Kempthorne & Nordskog)",
        category: "Quantitative Genetics & Inheritance",
        def: "A specialized selection index engineered with mathematical constraints to achieve genetic gain in desired traits while enforcing zero genetic change in an antagonistic trait."
    },
    "desired gains index": {
        term: "Desired Gains Selection Index (Pesek & Baker)",
        category: "Quantitative Genetics & Inheritance",
        def: "A selection index formulation where index weights are calculated directly from a specified vector of predetermined desired genetic responses for each trait."
    },
    "correlated selection differential": {
        term: "Correlated Selection Differential (S'_Y)",
        category: "Quantitative Genetics & Inheritance",
        def: "The average phenotypic superiority in an unselected correlated trait Y displayed by individuals chosen solely on the basis of trait X."
    },
    "realized response": {
        term: "Realized Genetic Response (R_R)",
        category: "Quantitative Genetics & Inheritance",
        def: "The actual observed generational change in the phenotypic mean of a livestock population subjected to artificial selection, measured against unselected control lines."
    },
    "intra-herd sire evaluation": {
        term: "Intra-Herd Sire Evaluation",
        category: "Quantitative Genetics & Inheritance",
        def: "Evaluating the genetic merit of breeding bulls based exclusively on daughter lactation records within a single herd, without adjusting for genetic differences between herds."
    },
    "multi-trait model": {
        term: "Multi-Trait Animal Model",
        category: "Quantitative Genetics & Inheritance",
        def: "A simultaneous mixed-model BLUP equation that analyzes multiple genetically correlated traits concurrently, borrowing information across traits to boost EBV accuracy."
    },

    // 6. Animal Breeding & Selection Systems (15 new terms -> 90 total)
    "animal model blup": {
        term: "Individual Animal Model (BLUP)",
        category: "Animal Breeding & Selection Systems",
        def: "Henderson's mixed-model BLUP evaluation where the additive genetic breeding value is solved for every animal (sires, dams, and young calves) using the inverse relationship matrix A⁻¹."
    },
    "sire-maternal grandsire model": {
        term: "Sire-Maternal Grandsire Model (S-MGS)",
        category: "Animal Breeding & Selection Systems",
        def: "A reduced mixed model for dairy sire proofing that fits sires and maternal grandfathers as random effects, accounting for non-random mating of elite dams."
    },
    "deregressed breeding value": {
        term: "Deregressed Breeding Value (DRP)",
        category: "Animal Breeding & Selection Systems",
        def: "An estimated breeding value mathematically transformed to remove parent average contribution and regression shrinkage, serving as an unregressed response variable in genomic training."
    },
    "marker-assisted selection": {
        term: "Marker-Assisted Selection (MAS)",
        category: "Animal Breeding & Selection Systems",
        def: "A breeding methodology where traditional phenotypic and pedigree selection is augmented by direct genotyping of DNA markers closely linked to quantitative trait loci (QTL)."
    },
    "candidate gene approach": {
        term: "Candidate Gene Approach",
        category: "Animal Breeding & Selection Systems",
        def: "A molecular genetics strategy that investigates specific genes with known physiological and biochemical roles for polymorphic causative variants affecting economic traits."
    },
    "genome-wide association study": {
        term: "Genome-Wide Association Study (GWAS)",
        category: "Animal Breeding & Selection Systems",
        def: "An experimental scan of high-density SNP markers across the entire genome in a large population to detect statistical associations with complex quantitative traits."
    },
    "composite cattle breed": {
        term: "Composite (Synthetic) Cattle Breed",
        category: "Animal Breeding & Selection Systems",
        def: "A stable, recognized cattle breed created by crossing two or more distinct pure breeds followed by inter-se mating (e.g. Frieswal: 5/8 Holstein Friesian + 3/8 Sahiwal)."
    },
    "purebred breeding": {
        term: "Purebred Breeding",
        category: "Animal Breeding & Selection Systems",
        def: "The systematic mating of registered purebred males and females belonging to the same breed to preserve breed purity, uniformity, and certified pedigree characteristics."
    },
    "criss-crossing": {
        term: "Criss-Crossing (Two-Breed Rotational Cross)",
        category: "Animal Breeding & Selection Systems",
        def: "A continuous crossbreeding system alternating purebred sires of two distinct breeds across successive generations of crossbred females, maintaining ~67% heterosis."
    },
    "three-breed rotational cross": {
        term: "Three-Breed Rotational Cross",
        category: "Animal Breeding & Selection Systems",
        def: "A continuous rotational mating system using purebred sires of three distinct breeds on crossbred dams in cyclical succession, preserving ~86% of maximum F1 heterosis."
    },
    "two-breed terminal cross": {
        term: "Two-Breed Terminal Cross",
        category: "Animal Breeding & Selection Systems",
        def: "A mating scheme where females of an adapted maternal breed (A) are crossed with terminal meat-type sires (B), and all F1 male and female progeny are slaughtered."
    },
    "three-breed terminal cross": {
        term: "Three-Breed Terminal Cross",
        category: "Animal Breeding & Selection Systems",
        def: "A commercial system where F1 crossbred cows (A × B) expressing maternal heterosis are mated to terminal sires of a third breed (C) to produce 100% market meat offspring."
    },
    "breed complementarity": {
        term: "Breed Complementarity",
        category: "Animal Breeding & Selection Systems",
        def: "The strategic exploitation of crossbreeding whereby the desirable genetic strengths of one breed compensate for the genetic shortcomings of another breed."
    },
    "juvenile in vitro embryo technology": {
        term: "Juvenile In-Vitro Embryo Technology (JIVET)",
        category: "Animal Breeding & Selection Systems",
        def: "A biotechnology protocol recovering immature oocytes from superovulated prepubertal calves (2 to 3 months of age) followed by IVF, reducing generation interval to less than one year."
    },
    "somatoplasm vs germplasm": {
        term: "Somatoplasm vs. Germplasm (Weismann)",
        category: "Animal Breeding & Selection Systems",
        def: "August Weismann's germ plasm theory establishing the separation between mortal somatic body cells (somatoplasm) and immortal, heritable reproductive cells (germplasm)."
    }
};

function main() {
    console.log('Loading existing js/glossary.js (400 terms)...');
    const originalContent = fs.readFileSync(GLOSSARY_PATH, 'utf8');

    // Parse existing glossary object
    const fn = new Function('window', 'app', originalContent + '; return glossary;');
    const oldGlossary = fn({}, { esc: s => s, icon: s => s });

    const existingTermKeys = Object.keys(oldGlossary.terms);
    console.log(`Loaded ${existingTermKeys.length} existing terms.`);

    const newKeys = Object.keys(NEW_TERMS);
    console.log(`Prepared ${newKeys.length} new terms.`);

    if (newKeys.length !== 80) {
        throw new Error(`Expected exactly 80 new terms, found ${newKeys.length}`);
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

    if (totalTermKeys.length !== 480) {
        throw new Error(`Expected total 480 terms, found ${totalTermKeys.length}`);
    }

    let totalCategoryKeys = 0;
    console.log('\nCategory breakdown after merge:');
    for (const [cat, keys] of Object.entries(mergedCategories)) {
        console.log(`  ${cat}: ${keys.length} terms`);
        totalCategoryKeys += keys.length;
    }
    if (totalCategoryKeys !== 480) {
        throw new Error(`Expected category total 480, found ${totalCategoryKeys}`);
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

    console.log('Writing 480-term expanded glossary to js/glossary.js...');
    fs.writeFileSync(GLOSSARY_PATH, jsCode, 'utf8');

    console.log('Mirroring 480-term expanded glossary to repo/js/glossary.js...');
    fs.writeFileSync(REPO_GLOSSARY_PATH, jsCode, 'utf8');

    console.log('Successfully generated and mirrored 480-term glossary!');
}

main();
