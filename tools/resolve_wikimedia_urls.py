# -*- coding: utf-8 -*-
"""
Batch-resolve all 79 Theory topics + 25 Practical topics to exact Wikimedia Commons URLs
in just 3 batch API requests (zero rate limiting).
"""
import urllib.request
import urllib.parse
import json
import time
import os

USER_AGENT = "VetGeneticsStudyApp/1.0 (https://github.com/fazalzama77-sys/VET-ANIMAL-GENETICS; personal educational use)"

# Topic -> (Source Type: 'wiki' or 'file', Identifier, Caption)
TOPICS = {
    # ================= UNIT 1: BIOSTATISTICS =================
    "u1-t01": ("file", "File:Examples of descriptive tools.png", "Biostatistical Analysis Framework: Visual summary of descriptive and inferential statistical distributions in biological sciences."),
    "u1-t02": ("file", "File:Example histogram.png", "Tabulation & Frequency Distribution: Grouped class intervals and frequency distribution of continuous measurements."),
    "u1-t03": ("wiki", "Sampling_(statistics)", "Population versus Sample: Extracting a representative random sample (statistic) from a biological population (parameter)."),
    "u1-t04": ("wiki", "Histogram", "Graphical Representation of Data: Histogram and frequency distribution curve of continuous variables."),
    "u1-t05": ("file", "File:Comparison mean median mode.svg", "Measures of Central Tendency: Geometric position of Mode, Median, and Arithmetic Mean across skewed and symmetric curves."),
    "u1-t06": ("wiki", "Standard_deviation", "Measures of Dispersion: Standard Deviation (σ) bands and cumulative dispersion around the population mean."),
    "u1-t07": ("wiki", "Central_limit_theorem", "Standard Error of the Mean (SEM) & Coefficient of Variation: Convergence of sample mean distributions toward a normal curve as sample size (n) increases."),
    "u1-t08": ("file", "File:Bivariate mean median mode.svg", "Moments, Skewness & Kurtosis: Asymmetry (positive vs. negative skewness) and peakedness in probability distributions."),
    "u1-t09": ("wiki", "Venn_diagram", "Elementary Probability Theory: Sample space, intersection (A ∩ B), union (A ∪ B), and conditional probability relationships."),
    "u1-t10": ("wiki", "Binomial_distribution", "Binomial & Poisson Probability Distributions: Discrete probability mass function (PMF) across varying parameters (n, p)."),
    "u1-t11": ("wiki", "Normal_distribution", "Normal (Gaussian) Distribution: Bell-shaped probability density curve showing empirical ±1σ (68.27%), ±2σ (95.45%), and ±3σ (99.73%) intervals."),
    "u1-t12": ("wiki", "Pearson_correlation_coefficient", "Correlation Analysis: Scatter diagrams illustrating strength and direction of Pearson's linear correlation coefficient (r)."),
    "u1-t13": ("wiki", "Linear_regression", "Linear Regression Analysis: Least-squares regression line (Y = a + bX) fitted to bivariate observations."),
    "u1-t14": ("wiki", "Stratified_sampling", "Sampling Methods: Stratified and random sampling partitioning a heterogeneous population into homogeneous strata."),
    "u1-t15": ("wiki", "Z-test", "Large Sample Z-Test & Hypothesis Testing: Standard normal critical rejection regions and p-value thresholds."),
    "u1-t16": ("wiki", "Student's_t-distribution", "Small Sample Student's t-Test: Family of t-distribution curves across degrees of freedom (ν) approaching the standard normal curve."),
    "u1-t17": ("wiki", "Chi-squared_distribution", "Chi-Square (χ²) Test of Significance: Probability density curves across degrees of freedom for Goodness of Fit and Independence."),
    "u1-t18": ("file", "File:Nuisance variable.jpg", "Experimental Designs (CRD & RBD): Controlling nuisance environmental gradients through blocking and randomization."),
    "u1-t19": ("wiki", "F-distribution", "Analysis of Variance (ANOVA) & F-Test: Snedecor's F-distribution curves comparing between-group to within-group variance."),
    "u1-t20": ("wiki", "Kolmogorov–Smirnov_test", "Non-Parametric Statistical Tests: Distribution-free cumulative empirical comparison for rank and ordinal biological data."),
    "u1-t21": ("file", "File:Relational database terms.svg", "Database Management Systems (DBMS): Relational table structure with primary keys, records (rows), and attributes (columns)."),
    "u1-t22": ("wiki", "Spreadsheet", "Veterinary Data Analysis using Spreadsheets: Automated tabular cells, statistical formulas, and graphical chart generation."),

    # ================= UNIT 2: ANIMAL & POPULATION GENETICS =================
    "u2-t01": ("wiki", "Gregor_Mendel", "History of Animal Genetics: Gregor Johann Mendel and the foundational laws of particulate inheritance."),
    "u2-t02": ("wiki", "Meiosis", "Cell Division (Mitosis vs. Meiosis): Chromosomal replication, homologous pairing, crossing over, and reductional division."),
    "u2-t03": ("wiki", "Centromere", "Chromosome Morphology & Classification: Structural organization of chromatids, centromere constriction, and telomeres."),
    "u2-t04": ("wiki", "Mendelian_inheritance", "Mendelian Principles: Segregation of alleles and independent assortment illustrated by Mendelian cross diagrams."),
    "u2-t05": ("wiki", "Dominance_(genetics)", "Modified Mendelian Inheritance: Autosomal dominance, incomplete dominance, and codominant allele expression."),
    "u2-t06": ("wiki", "Epistasis", "Epistasis & Gene Interactions: Non-allelic interaction modifying classical dihybrid ratios (e.g., coat colour inheritance)."),
    "u2-t07": ("wiki", "Pleiotropy", "Pleiotropy, Penetrance & Expressivity: Genotype-to-phenotype mapping where single loci affect multiple biological traits."),
    "u2-t08": ("wiki", "ABO_blood_group_system", "Multiple Alleles & Blood Group Systems: Co-dominant and multi-allelic cell-surface antigen inheritance."),
    "u2-t09": ("wiki", "Sex-determination_system", "Chromosomal Sex Determination Mechanisms: Comparative XX/XY (mammalian) and ZZ/ZW (avian) chromosomal systems."),
    "u2-t10": ("file", "File:X-linked recessive (2).svg", "Sex-Linked Inheritance: Criss-cross transmission of X-linked alleles from carrier dams to affected male progeny."),
    "u2-t11": ("wiki", "Chromosomal_crossover", "Genetic Linkage & Crossing Over: Chiasma formation and reciprocal exchange of chromatid segments during pachytene."),
    "u2-t12": ("wiki", "Point_mutation", "Gene Mutations: Molecular mechanisms of base substitution (transition, transversion) and frameshift mutations."),
    "u2-t13": ("wiki", "Mutation", "Chromosomal Aberrations: Structural chromosome mutations — Deletion, Duplication, Inversion, and Translocation."),
    "u2-t14": ("wiki", "Karyotype", "Cytogenetics & Karyotyping: G-banded metaphase chromosome idiogram arranged by size and centromere position."),
    "u2-t15": ("wiki", "Mitochondrial_DNA", "Extra-Chromosomal (Mitochondrial) Inheritance: Circular maternal mtDNA genome encoding oxidative phosphorylation genes."),
    "u2-t16": ("wiki", "DNA", "Molecular Structure of Nucleic Acids: Watson-Crick DNA double helix showing sugar-phosphate backbone and complementary base pairs."),
    "u2-t17": ("wiki", "DNA_replication", "DNA Replication & Central Dogma: Semiconservative replication fork with leading and lagging strands, helicase, and DNA polymerase."),
    "u2-t18": ("wiki", "Polymerase_chain_reaction", "Molecular Techniques (PCR, RFLP, Sequencing): Exponential amplification of target DNA via thermal cycling."),
    "u2-t19": ("file", "File:Unlinked vs. Linked Genes.svg", "Population Genetics Foundations: Distribution and transmission of alleles across segregating loci in a population."),
    "u2-t20": ("file", "File:Allele Substn.jpg", "Genetic Structure of a Population: Genotypic values and allele frequency distribution across a diploid locus."),
    "u2-t21": ("wiki", "Hardy–Weinberg_principle", "Hardy-Weinberg Equilibrium Law: Parabolic relationship between allele frequencies (p, q) and genotype frequencies (p², 2pq, q²)."),
    "u2-t22": ("file", "File:Effects of Genetic Drift on Large and Small Populations.jpg", "Forces Changing Gene Frequency: Stochastic allele frequency fluctuations (Genetic Drift) in small vs. large populations."),
    "u2-t23": ("file", "File:Example of a Genome-wide QTL-Scan from PLoS Biology.jpg", "Quantitative vs. Qualitative Genetics: Continuous polygenic inheritance and genome-wide QTL distribution across multiple additive loci."),
    "u2-t24": ("file", "File:Additive and Dominance Effects.png", "Average Effect of Gene & Breeding Value: Partitioning genotypic values into linear additive effects (BV) and dominance deviations."),
    "u2-t25": ("file", "File:Example of QTL-Scan on a single Chromosom from PLoS Biology.jpg", "Components of Phenotypic Variance: Quantitative Trait Locus (QTL) mapping and partitioning of genetic variance."),
    "u2-t26": ("wiki", "Phenotypic_plasticity", "Genotype × Environment (G × E) Interaction: Reaction norms illustrating differential phenotypic expression across environments."),
    "u2-t27": ("file", "File:Response to selection.jpg", "Heritability (h²) & Selection Response: Relationship between narrow-sense heritability (slope) and genetic gain (R = h²S)."),
    "u2-t28": ("file", "File:Intraclass correlation coefficient graph improved.svg", "Repeatability (r): Intraclass correlation measuring consistency of repeated longitudinal measurements on the same animal."),
    "u2-t29": ("wiki", "Spearman's_rank_correlation_coefficient", "Genetic & Phenotypic Correlations: Bivariate association and correlated response between quantitative traits."),

    # ================= UNIT 3: ANIMAL BREEDING =================
    "u3-t01": ("wiki", "Selective_breeding", "History of Animal Breeding: Artificial selection and domestication transforming ancestral wild types into specialized breeds."),
    "u3-t02": ("wiki", "Zebu", "Classification of Livestock Breeds: Indigenous humped Zebu cattle (Bos indicus) adapted to tropical climates."),
    "u3-t03": ("wiki", "Dairy_cattle", "Economic Traits of Dairy Livestock: Mammary conformation and 305-day lactation production characteristics."),
    "u3-t04": ("file", "File:Directional, Disruptive and Stabilizing Selections.svg", "Selection in Animal Breeding: Directional, Stabilizing, and Disruptive selection shifting population genetic mean."),
    "u3-t05": ("wiki", "Pedigree_chart", "Bases of Selection: Standard pedigree chart tracking ancestral and collateral performance across generations."),
    "u3-t06": ("wiki", "Punnett_square", "Combined & Indirect Selection: Combining individual and family genetic information to maximize selection accuracy."),
    "u3-t07": ("wiki", "Directional_selection", "Methods of Selection: Truncation selection threshold retaining elite breeding individuals above the culling point."),
    "u3-t08": ("wiki", "Test_cross", "Classification of Mating Systems: Genetic pairing schemas comparing random panmixia and targeted assortative matings."),
    "u3-t09": ("file", "File:Child first cousins Homozy BD.png", "Inbreeding Coefficient (FX) & Relationship (RXY): Pedigree path loop showing identity by descent (IBD) from common ancestors."),
    "u3-t10": ("file", "File:Inbreeding depression in Delphinium nelsonii.png", "Inbreeding Depression: Fitness and performance decline resulting from increased homozygosity of deleterious recessives."),
    "u3-t11": ("file", "File:Backcrossing 1.jpg", "Outbreeding & Crossbreeding Systems: Grading up and backcrossing schema progressively replacing indigenous genes."),
    "u3-t12": ("file", "File:Heterosis.svg", "Heterosis (Hybrid Vigour): F1 crossbred superiority exceeding the mid-parent average due to dominance and overdominance."),
    "u3-t13": ("wiki", "Hybrid_(biology)", "Selection for Combining Ability (RRS): Reciprocal recurrent hybridization maximizing specific combining ability."),
    "u3-t14": ("wiki", "Sahiwal_cattle", "Breeding Strategies for Dairy Cattle: Indigenous Sahiwal dairy cattle — premier milch zebu breed of India."),
    "u3-t15": ("wiki", "Jamnapari_goat", "Breeding Strategies for Sheep, Goats & Swine: Indigenous Jamnapari goat breed utilized in meat and milk improvement."),
    "u3-t16": ("wiki", "Leghorn_chicken", "Commercial Poultry Breeding: White Leghorn strain selected for high egg production and feed efficiency."),
    "u3-t17": ("wiki", "Holstein_Friesian", "Sire Evaluation & Progeny Testing (BLUP): Elite dairy genetics evaluated across contemporary herd-year-season groups."),
    "u3-t18": ("file", "File:Founder effect with drift.jpg", "Open Nucleus Breeding System (ONBS): Gene flow between elite nucleus breeding herds and base populations."),
    "u3-t19": ("wiki", "Gyr_cattle", "Development of New Breeds & Synthetic Strains: Indigenous Gir cattle genetics used in synthetic crossbred strains."),
    "u3-t20": ("wiki", "Murrah_buffalo", "National Livestock Breeding Policies in India: Elite Murrah riverine buffalo — cornerstone of Indian dairy improvement."),
    "u3-t21": ("wiki", "Cryoconservation_of_animal_genetic_resources", "Conservation of Animal Genetic Resources (AnGR): Ex-situ cryoconservation in liquid nitrogen gene banks (-196°C)."),
    "u3-t22": ("wiki", "Artificial_insemination", "Reproductive Biotechnologies (AI, MOET, IVF): Artificial insemination and assisted reproductive technology in cattle."),
    "u3-t23": ("wiki", "Major_histocompatibility_complex", "Breeding for Disease Resistance: MHC (BoLA) molecular structure mediating genetic resistance to pathogens."),
    "u3-t24": ("wiki", "German_Shepherd", "Dog & Cat Breeds and Conformation Standards: Working dog anatomical conformation and breed standard morphology."),
    "u3-t25": ("file", "File:Estrous cycle.png", "Breeding Management & Estrous Detection: Hormonal fluctuations (Estrogen, LH surge, Progesterone) across the estrous cycle."),
    "u3-t26": ("wiki", "Budgerigar", "Common Pet Birds & Avian Breeding Management: Captive breeding and colour genetics in Budgerigars."),
    "u3-t27": ("file", "File:Bottleneck Effect.jpg", "Effective Population Size (Ne) & Wildlife Dynamics: Genetic bottleneck reducing allelic diversity in small captive populations."),
    "u3-t28": ("wiki", "Captive_breeding", "Planned Wildlife Breeding & Conservation: Captive breeding and reintroduction programme for endangered species.")
}

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    wiki_items = {tid: val for tid, val in TOPICS.items() if val[0] == "wiki"}
    file_items = {tid: val for tid, val in TOPICS.items() if val[0] == "file"}

    resolved = {}

    # 1. Batch resolve wiki titles
    wiki_titles = list(set(val[1] for val in wiki_items.values()))
    title_to_url = {}
    for i in range(0, len(wiki_titles), 40):
        batch = wiki_titles[i:i+40]
        url = (
            "https://en.wikipedia.org/w/api.php?action=query&redirects=1&titles="
            + urllib.parse.quote("|".join(batch))
            + "&prop=pageimages&piprop=original|thumbnail&pithumbsize=960&format=json"
        )
        data = fetch_json(url)
        q = data.get("query", {})
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        redir = {r["from"]: r["to"] for r in q.get("redirects", [])}
        page_by_title = {}
        for p in q.get("pages", {}).values():
            t_src = p.get("thumbnail", {}).get("source") or p.get("original", {}).get("source")
            page_by_title[p.get("title")] = t_src
        for orig in batch:
            t = norm.get(orig, orig.replace("_", " "))
            t = redir.get(t, t)
            title_to_url[orig] = page_by_title.get(t)
        time.sleep(0.4)

    for tid, (_, wtitle, cap) in wiki_items.items():
        resolved[tid] = {"url": title_to_url.get(wtitle), "caption": cap}

    # 2. Batch resolve Commons File titles
    file_titles = list(set(val[1] for val in file_items.values()))
    file_to_url = {}
    for i in range(0, len(file_titles), 40):
        batch = file_titles[i:i+40]
        url = (
            "https://commons.wikimedia.org/w/api.php?action=query&titles="
            + urllib.parse.quote("|".join(batch))
            + "&prop=imageinfo&iiprop=url&iiurlwidth=960&format=json"
        )
        data = fetch_json(url)
        q = data.get("query", {})
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        page_by_title = {}
        for p in q.get("pages", {}).values():
            ii = p.get("imageinfo", [{}])[0]
            page_by_title[p.get("title")] = ii.get("thumburl") or ii.get("url")
        for orig in batch:
            t = norm.get(orig, orig)
            file_to_url[orig] = page_by_title.get(t)
        time.sleep(0.4)

    for tid, (_, ftitle, cap) in file_items.items():
        resolved[tid] = {"url": file_to_url.get(ftitle), "caption": cap}

    missing = [tid for tid, v in resolved.items() if not v["url"]]
    print(f"Resolved {len(resolved) - len(missing)} / {len(resolved)} topics!")
    if missing:
        print("Missing:", missing)

    out_path = os.path.join(os.path.dirname(__file__), "verified_urls.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(resolved, f, indent=2)

if __name__ == "__main__":
    main()
