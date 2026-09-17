// tools/build_540_glossary.js
// Assembles and generates the expanded 540-term glossary for Animal Genetics and Breeding Studio

const fs = require('fs');
const path = require('path');

const GLOSSARY_PATH = path.join(__dirname, '../js/glossary.js');
const REPO_GLOSSARY_PATH = path.join(__dirname, '../repo/js/glossary.js');

// 60 new exam-specific terms (expanding 480 to exactly 540)
const NEW_TERMS = {
    // 1. Biostatistics & Experimental Design (10 new terms -> 90 total)
    "frequency density": {
        term: "Frequency Density",
        category: "Biostatistics & Experimental Design",
        def: "The ratio of class frequency to class interval width (f_i / c), representing the vertical height of a histogram bar when continuous frequency intervals are of unequal width."
    },
    "standard error of difference of means": {
        term: "Standard Error of Difference Between Means (SE_d)",
        category: "Biostatistics & Experimental Design",
        def: "The standard deviation of the sampling distribution of the difference between two sample means: SE_d = √[(σ₁²/n₁) + (σ₂²/n₂)]."
    },
    "confidence interval": {
        term: "Confidence Interval (CI)",
        category: "Biostatistics & Experimental Design",
        def: "An estimated numerical range constructed around a sample statistic with a specified probability (1 - α, e.g. 95%) that contains the true unknown population parameter."
    },
    "pooled variance": {
        term: "Pooled Sample Variance (s_p²)",
        category: "Biostatistics & Experimental Design",
        def: "A weighted average of two sample variances calculated by pooling their sums of squares across (n₁ + n₂ - 2) degrees of freedom under the assumption of equal population variances."
    },
    "bartlett test": {
        term: "Bartlett's Test for Homogeneity of Variances",
        category: "Biostatistics & Experimental Design",
        def: "A statistical hypothesis test used to verify the assumption of homoscedasticity (equal population variances) across multiple treatment groups before conducting an ANOVA F-test."
    },
    "f-distribution": {
        term: "Snedecor's F-Distribution",
        category: "Biostatistics & Experimental Design",
        def: "A continuous, right-skewed probability distribution representing the ratio of two independent chi-square random variables each divided by their respective degrees of freedom."
    },
    "coefficient of concordance": {
        term: "Kendall's Coefficient of Concordance (W)",
        category: "Biostatistics & Experimental Design",
        def: "A non-parametric statistical measure bounded between 0.0 and 1.0 that quantifies the degree of agreement and consistency among m independent judges ranking n animals."
    },
    "standard error of proportion": {
        term: "Standard Error of Sample Proportion (SE_p)",
        category: "Biostatistics & Experimental Design",
        def: "The standard deviation of the sampling distribution of an observed sample proportion p drawn from a binomial population: SE_p = √[p(1 - p) / n]."
    },
    "multistage sampling": {
        term: "Multistage Sampling",
        category: "Biostatistics & Experimental Design",
        def: "A hierarchical probability sampling method where larger sampling units are selected at the first stage and progressively smaller subunits (e.g. districts → villages → herds) are sampled subsequently."
    },
    "factorial experiment": {
        term: "Factorial Experiment (2^k)",
        category: "Biostatistics & Experimental Design",
        def: "An experimental design in which two or more biological factors are evaluated simultaneously at all possible level combinations, measuring both main effects and interaction effects."
    },

    // 2. Classical & Mendelian Genetics (10 new terms -> 90 total)
    "criss-cross inheritance": {
        term: "Criss-Cross Inheritance",
        category: "Classical & Mendelian Genetics",
        def: "The transmission pattern characteristic of sex-linked recessive genes where a trait is passed from an affected male ancestor through carrier daughters to grandsons of the next generation."
    },
    "holandric gene": {
        term: "Holandric (Y-Linked) Gene",
        category: "Classical & Mendelian Genetics",
        def: "A gene located on the non-homologous portion of the Y chromosome, transmitted exclusively from father to son across generations (e.g. SRY testis-determining factor)."
    },
    "pseudoautosomal region": {
        term: "Pseudoautosomal Region (PAR)",
        category: "Classical & Mendelian Genetics",
        def: "Homologous distal chromosomal segments located at the tips of X and Y sex chromosomes that pair and undergo regular meiotic crossing over like ordinary autosomes."
    },
    "genocopy": {
        term: "Genocopy",
        category: "Classical & Mendelian Genetics",
        def: "A phenotypic condition or defect identical to one caused by a known mutant gene, but produced by a completely different, independent mutant gene locus."
    },
    "cryptic gene": {
        term: "Cryptic (Silent) Gene",
        category: "Classical & Mendelian Genetics",
        def: "A dormant, non-expressed genetic sequence residing within a genome that can be functionally activated by rare genomic rearrangement, transposable elements, or extreme environmental shock."
    },
    "isochromosome arms": {
        term: "Isochromosome Formation",
        category: "Classical & Mendelian Genetics",
        def: "A structural chromosomal aberration where transverse rather than longitudinal centromeric division produces a chromosome with two identical mirror-image arms."
    },
    "trihybrid ratio": {
        term: "Trihybrid Phenotypic Ratio",
        category: "Classical & Mendelian Genetics",
        def: "The classic 27:9:9:9:3:3:3:1 F2 phenotypic segregation ratio resulting from crossing individuals heterozygous at three independently assorting Mendelian loci."
    },
    "chiasma frequency": {
        term: "Chiasma Frequency",
        category: "Classical & Mendelian Genetics",
        def: "The mean number of cytologically visible chiasmata observed per bivalent during diplotene of meiosis, directly proportional to the physical chromosome length."
    },
    "complementation group": {
        term: "Complementation Group",
        category: "Classical & Mendelian Genetics",
        def: "A collection of independent recessive mutant alleles that fail to complement each other in trans-heterozygotes, operationally defining a single functional gene (cistron)."
    },
    "paracentric loop": {
        term: "Paracentric Inversion Loop",
        category: "Classical & Mendelian Genetics",
        def: "A reverse chromosomal loop formed during meiotic pachytene synapsis in an inversion heterozygote; crossing over within it produces dicentric bridges and acentric fragments."
    },

    // 3. Cytogenetics & Molecular Genetics (10 new terms -> 95 total)
    "karyotyping technique": {
        term: "Lymphocyte Karyotyping Technique",
        category: "Cytogenetics & Molecular Genetics",
        def: "The cytogenetic protocol of culturing peripheral blood lymphocytes with phytohemagglutinin, arresting at metaphase with colchicine, hypotonic treatment, and Giemsa banding."
    },
    "centromeric index": {
        term: "Centromeric Index (CI)",
        category: "Cytogenetics & Molecular Genetics",
        def: "The ratio of the length of the short arm (p) of a chromosome to the total chromosome length (p + q), expressed as a percentage: CI = [p / (p + q)] × 100."
    },
    "arm ratio": {
        term: "Chromosome Arm Ratio (r)",
        category: "Cytogenetics & Molecular Genetics",
        def: "The ratio of the length of the long arm (q) to the length of the short arm (p) of a chromosome (r = q / p), used internationally to define chromosome morphological classes."
    },
    "nucleosome core": {
        term: "Nucleosome Core Particle",
        category: "Cytogenetics & Molecular Genetics",
        def: "The fundamental repeating structural unit of eukaryotic chromatin, comprising 146-147 base pairs of DNA wrapped 1.65 turns around an octamer of core histones (H2A, H2B, H3, H4)."
    },
    "telomerase": {
        term: "Telomerase (TERT)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A ribonucleoprotein reverse transcriptase enzyme that synthesizes species-specific repetitive telomeric DNA repeats (TTAGGG) onto 3' chromosome ends to preserve replicative lifespan."
    },
    "dna polymerase iii": {
        term: "DNA Polymerase III Holoenzyme",
        category: "Cytogenetics & Molecular Genetics",
        def: "The primary prokaryotic replicative enzyme complex that synthesizes leading and lagging DNA strands in the 5' to 3' direction with intrinsic 3' to 5' exonucleolytic proofreading."
    },
    "topoisomerase": {
        term: "DNA Topoisomerase (Gyrase)",
        category: "Cytogenetics & Molecular Genetics",
        def: "An enzyme that relieves torsional overwinding and positive supercoils ahead of the replication fork by transiently cleaving, swiveling, and religating phosphodiester backbones."
    },
    "single nucleotide polymorphism": {
        term: "Single Nucleotide Polymorphism (SNP)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A single base-pair genomic substitution (A, T, C, or G) present in at least 1% of a livestock population, providing high-density codominant markers for genomic selection."
    },
    "dna methylation": {
        term: "DNA Cytosine Methylation (5-mC)",
        category: "Cytogenetics & Molecular Genetics",
        def: "An epigenetic covalent enzymatic modification adding a methyl group to the 5th carbon of cytosine in CpG islands by DNA methyltransferases, causing transcriptional gene silencing."
    },
    "real-time pcr": {
        term: "Real-Time Quantitative PCR (qPCR)",
        category: "Cytogenetics & Molecular Genetics",
        def: "A molecular biology technique that monitors the exponential amplification of targeted DNA or cDNA cycle-by-cycle using fluorescent reporter dyes or hydrolysis TaqMan probes."
    },

    // 4. Population Genetics (10 new terms -> 75 total)
    "panmictic index f": {
        term: "Wright's Panmictic Inbreeding Indices",
        category: "Population Genetics",
        def: "The hierarchy of correlation coefficients (F_IS, F_ST, F_IT) quantifying the reduction in heterozygosity due to inbreeding within subpopulations and genetic divergence between breeds."
    },
    "gene frequency drift": {
        term: "Gene Frequency Sampling Drift",
        category: "Population Genetics",
        def: "The cumulative generational change in population allele frequencies occurring purely by chance sampling error during gametogenesis in herds of finite size."
    },
    "selection coefficient against recessive": {
        term: "Selection Against Recessive Homozygotes (s)",
        category: "Population Genetics",
        def: "The proportionate reduction in relative fitness of homozygous recessive animals (W_aa = 1 - s), reducing recessive allele frequency per generation by Δq = -spq² / (1 - sq²)."
    },
    "recurrent mutation": {
        term: "Recurrent Mutation Pressure (u)",
        category: "Population Genetics",
        def: "The persistent conversion of wild-type allele A to mutant allele a at a characteristic mutation rate u per generation, shifting gene frequency by Δq = u · p."
    },
    "reverse mutation rate": {
        term: "Reverse (Back) Mutation Rate (v)",
        category: "Population Genetics",
        def: "The probability per generation v that a mutant allele a mutates back to the original wild-type allele A, creating a mutation equilibrium at q̂ = u / (u + v)."
    },
    "island model migration rate": {
        term: "Island Migration Rate (m)",
        category: "Population Genetics",
        def: "The proportion m of breeding individuals in an isolated island herd that are immigrants from an outside mainland population, changing allele frequency by Δq = m(q_m - q)."
    },
    "heterozygote advantage model": {
        term: "Heterozygote Overdominance Equilibrium",
        category: "Population Genetics",
        def: "A population genetics stable equilibrium achieved when the heterozygote Aa has superior biological fitness over both homozygotes (AA: 1-s₁, Aa: 1, aa: 1-s₂), stabilizing at q̂ = s₁ / (s₁ + s₂)."
    },
    "inbreeding depression in fitness": {
        term: "Inbreeding Depression in Fitness Traits",
        category: "Population Genetics",
        def: "The phenotypic performance decline in low-heritability fitness traits (embryo survival, fertility, disease resistance) resulting from homozygous expression of deleterious recessives."
    },
    "gametic disequilibrium coefficient": {
        term: "Linkage Disequilibrium Parameter (D)",
        category: "Population Genetics",
        def: "The mathematical covariance quantifying non-random gametic association between alleles at two loci: D = P_AB - (p_A · p_B), decaying across generations at rate (1 - c)."
    },
    "effective population size ratio": {
        term: "Ne / N Census Herd Ratio",
        category: "Population Genetics",
        def: "The ratio of genetic effective population size to total census herd count (Ne / N), indicating the severity of unequal sex ratios, fertility variance, and population bottlenecks."
    },

    // 5. Quantitative Genetics & Inheritance (10 new terms -> 90 total)
    "infinitesimal polygenic model": {
        term: "Infinitesimal Polygenic Framework",
        category: "Quantitative Genetics & Inheritance",
        def: "Fisher's biometrical foundation modeling quantitative traits as the linear sum of effects of an infinite number of unlinked Mendelian loci each possessing an infinitesimally small effect."
    },
    "breeding value accuracy": {
        term: "Accuracy of Breeding Value Prediction (r_TI)",
        category: "Quantitative Genetics & Inheritance",
        def: "The statistical correlation between an animal's true unobservable additive breeding value (T) and its estimated breeding value (I): r_TI = √[n / (n + (4 - h²) / h²)]."
    },
    "intra-class correlation repeatability": {
        term: "Intra-Class Correlation Repeatability (r)",
        category: "Quantitative Genetics & Inheritance",
        def: "Repeatability formulated as the ratio of between-animal variance to total phenotypic variance across repeated lactation or fleece measurements: r = (σ²_b) / (σ²_b + σ²_w)."
    },
    "variance due to permanent environment": {
        term: "Permanent Environmental Variance Component (V_Ep)",
        category: "Quantitative Genetics & Inheritance",
        def: "The non-genetic variance caused by environmental effects (e.g. blind quarter from calfhood mastitis) that permanently alter all subsequent performance records of an animal."
    },
    "variance due to temporary environment": {
        term: "Temporary Environmental Variance Component (V_Et)",
        category: "Quantitative Genetics & Inheritance",
        def: "The transitory non-genetic variance arising from localized day-to-day fluctuations in nutrition, climate, or management affecting only a single measurement."
    },
    "paternal half-sib heritability": {
        term: "Paternal Half-Sib Heritability (4t)",
        category: "Quantitative Genetics & Inheritance",
        def: "Narrow-sense heritability estimated from the intraclass correlation t among paternal half-sibs sired by common bulls in an ANOVA model: h² = 4 · σ²_s / (σ²_s + σ²_e)."
    },
    "mid-parent heritability": {
        term: "Mid-Parent Regression Heritability",
        category: "Quantitative Genetics & Inheritance",
        def: "Narrow-sense heritability estimated directly as the slope b of the linear regression of offspring phenotypic performance on the average performance of both parents (mid-parent value)."
    },
    "single parent regression heritability": {
        term: "Offspring-Single Parent Heritability (2b)",
        category: "Quantitative Genetics & Inheritance",
        def: "Narrow-sense heritability estimated as twice the linear regression coefficient b of offspring phenotypic performance on the phenotypic record of one parent: h² = 2 · b_OP."
    },
    "additive genetic correlation": {
        term: "Additive Genetic Correlation (r_A)",
        category: "Quantitative Genetics & Inheritance",
        def: "The Pearson correlation measuring the linear relationship between the additive breeding values of two different traits, arising primarily from pleiotropic gene action: r_A = Cov_A / (σ_A₁ σ_A₂)."
    },
    "correlated response formula": {
        term: "Correlated Selection Response Formula",
        category: "Quantitative Genetics & Inheritance",
        def: "Falconer's predictive equation for the indirect genetic gain in unselected trait Y when artificial selection is applied to trait X: CR_Y = i · r_TI_X · r_A · σ_A_Y."
    },

    // 6. Animal Breeding & Selection Systems (10 new terms -> 100 total)
    "equal parent index": {
        term: "Equal Parent Index (EPI)",
        category: "Animal Breeding & Selection Systems",
        def: "An early dairy bull evaluation index based on the hypothesis that sire and dam contribute equally to daughter phenotype: Sire Transmitting Index = 2 · Daughter Average - Dam Average."
    },
    "contemporary comparison sire proof": {
        term: "Contemporary Comparison Sire Proof (CC)",
        category: "Animal Breeding & Selection Systems",
        def: "Robertson and Rendel's sire evaluation method weighting daughter records against contemporary herdmates calving in the same herd-year-season: Proof = [n / (n + 15)] · (Daughter - Herdmate)."
    },
    "sire model mixed equations": {
        term: "Sire Model BLUP Equations",
        category: "Animal Breeding & Selection Systems",
        def: "Henderson's mixed model formulation evaluating dairy bulls where sires are treated as random genetic effects and dams are treated as random and unrelated within herds."
    },
    "blup animal model inverse a": {
        term: "Henderson's Sparse Inverse A Matrix (A⁻¹)",
        category: "Animal Breeding & Selection Systems",
        def: "C.R. Henderson's landmark 1976 algorithm that constructs the exact numerical inverse of the pedigree relationship matrix (A⁻¹) directly from pedigree lists without inverting matrix A."
    },
    "genomic selection reliability": {
        term: "Genomic Selection Reliability (r²_GEBV)",
        category: "Animal Breeding & Selection Systems",
        def: "The squared correlation between an animal's true breeding value and its genomic estimated breeding value (r²_GEBV), reflecting the proportion of true genetic variance explained by dense SNPs."
    },
    "criss-cross breeding heterosis": {
        term: "Criss-Cross Equilibrium Heterosis (66.7%)",
        category: "Animal Breeding & Selection Systems",
        def: "The asymptotic equilibrium level of individual heterosis retained in a continuous two-breed rotational crossbreeding system, stabilizing at 2/3 (66.7%) of maximum F1 hybrid vigor."
    },
    "three-breed rotational heterosis": {
        term: "Three-Breed Rotational Heterosis (85.7%)",
        category: "Animal Breeding & Selection Systems",
        def: "The asymptotic equilibrium level of individual heterosis preserved in a three-breed rotational mating system, stabilizing indefinitely at 6/7 (85.7%) of maximum F1 hybrid vigor."
    },
    "two-breed terminal crossbreeding": {
        term: "Two-Breed Terminal Crossbreeding",
        category: "Animal Breeding & Selection Systems",
        def: "A commercial crossbreeding system where straightbred females of an adapted maternal breed are crossed with terminal meat-type sires, and 100% of F1 progeny are slaughtered for beef or mutton."
    },
    "three-breed terminal crossbreeding": {
        term: "Three-Breed Terminal Crossbreeding",
        category: "Animal Breeding & Selection Systems",
        def: "A crossing program where F1 crossbred females (A × B) exploiting maternal heterosis are mated to terminal sires of a third breed (C) to produce 100% market meat offspring."
    },
    "ex-situ in-vitro cryo-banking": {
        term: "Ex-Situ In-Vitro Cryo-Banking",
        category: "Animal Breeding & Selection Systems",
        def: "The long-term conservation of endangered indigenous livestock germplasm as deep-frozen semen, vitrified ova, embryos, and somatic DNA tissue at -196°C in liquid nitrogen gene banks."
    }
};

function main() {
    console.log('Loading existing js/glossary.js (480 terms)...');
    const originalContent = fs.readFileSync(GLOSSARY_PATH, 'utf8');

    // Parse existing glossary object
    const fn = new Function('window', 'app', originalContent + '; return glossary;');
    const oldGlossary = fn({}, { esc: s => s, icon: s => s });

    const existingTermKeys = Object.keys(oldGlossary.terms);
    console.log(`Loaded ${existingTermKeys.length} existing terms.`);

    const newKeys = Object.keys(NEW_TERMS);
    console.log(`Prepared ${newKeys.length} new terms.`);

    if (newKeys.length !== 60) {
        throw new Error(`Expected exactly 60 new terms, found ${newKeys.length}`);
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

    if (totalTermKeys.length !== 540) {
        throw new Error(`Expected total 540 terms, found ${totalTermKeys.length}`);
    }

    let totalCategoryKeys = 0;
    console.log('\nCategory breakdown after merge:');
    for (const [cat, keys] of Object.entries(mergedCategories)) {
        console.log(`  ${cat}: ${keys.length} terms`);
        totalCategoryKeys += keys.length;
    }
    if (totalCategoryKeys !== 540) {
        throw new Error(`Expected category total 540, found ${totalCategoryKeys}`);
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

    console.log('Writing 540-term expanded glossary to js/glossary.js...');
    fs.writeFileSync(GLOSSARY_PATH, jsCode, 'utf8');

    console.log('Mirroring 540-term expanded glossary to repo/js/glossary.js...');
    fs.writeFileSync(REPO_GLOSSARY_PATH, jsCode, 'utf8');

    console.log('Successfully generated and mirrored 540-term glossary!');
}

main();
