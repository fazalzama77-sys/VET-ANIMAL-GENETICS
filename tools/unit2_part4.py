# -*- coding: utf-8 -*-
"""
Unit 2 - Part 4: Topics u2-t22 to u2-t29
Principles of Animal and Population Genetics (IVRI Undergrad 10 CGPA Standard)
"""

topics = {}

topics["u2-t22"] = {
    "summary": "Forces changing gene and genotypic frequencies include systematic forces (mutation, migration, selection) that act predictably in direction and magnitude, and the dispersive stochastic force of genetic drift in finite populations.",
    "desc": (
        "<b>CLASSIFICATION OF FORCES CHANGING GENE FREQUENCY</b><br>"
        "The Hardy-Weinberg law represents an idealized static equilibrium. In living animal populations, gene and genotypic frequencies are continuously perturbed by four primary evolutionary forces, classified into two operational categories:"
        "<ol>"
        "<li><b>Systematic Forces:</b> Predictable in both <b>direction and magnitude</b>; amenable to precise mathematical modeling: "
        "<br>&bull; <b>Mutation</b> (introducing novel alleles)"
        "<br>&bull; <b>Migration / Gene Flow</b> (introducing alleles from foreign populations)"
        "<br>&bull; <b>Selection</b> (differential reproductive success of genotypes).</li>"
        "<li><b>Dispersive / Stochastic Force:</b> Predictable in <b>magnitude, but completely unpredictable in direction</b>: "
        "<br>&bull; <b>Genetic Drift</b> (random sampling fluctuations occurring in small, finite populations).</li>"
        "</ol><br>"
        "<b>1. MUTATION PRESSURE</b><br>"
        "Spontaneous recurrent mutations alter allelic frequencies very slowly:"
        "<ul>"
        "<li>Let forward mutation rate from allele A &rarr; a be <code>&mu;</code> (typically 10⁻⁵ to 10⁻⁶ per generation).</li>"
        "<li>Let reverse back-mutation rate from allele a &rarr; A be <code>&nu;</code>.</li>"
        "<li>Change in gene frequency per generation: <code>&Delta;q = &mu;p - &nu;q = &mu;(1 - q) - &nu;q</code>.</li>"
        "<li>At mutational equilibrium (<code>&Delta;q = 0</code>): "
        "<br><code>q&#770; = &mu; / (&mu; + &nu;)</code>. "
        "Because mutation rates are exceedingly low, mutation pressure alone takes tens of thousands of generations to alter population gene frequencies appreciably.</li>"
        "</ul><br>"
        "<b>2. MIGRATION (GENE FLOW)</b><br>"
        "Migration involves the movement of breeding animals from an immigrant donor population into an indigenous native herd:"
        "<ul>"
        "<li>Let <code>m</code> = Migration rate (proportion of breeding animals in the new mixed herd that are immigrants).</li>"
        "<li>Let <code>q_m</code> = Gene frequency in immigrant population.</li>"
        "<li>Let <code>q₀</code> = Gene frequency in native recipient population.</li>"
        "<li>Gene frequency in the next generation after migration: "
        "<br><code>q₁ = m &times; q_m + (1 - m) &times; q₀</code>"
        "<li>Change in gene frequency: "
        "<br><code>&Delta;q = q₁ - q₀ = m (q_m - q₀)</code>.</li>"
        "<li><i>Livestock Application:</i> Crossbreeding native non-descript zebu cows by introducing elite exotic bulls (Jersey/HF) represents large-scale planned migration (m = 0.50 per generation).</li>"
        "</ul><br>"
        "<b>3. SELECTION (ARTIFICIAL AND NATURAL)</b><br>"
        "Selection is the differential survival and reproductive rate of different genotypes. It is the primary, most powerful tool used by animal breeders to alter herd genetics:"
        "<ul>"
        "<li><b>Biological Fitness / Adaptive Value (W):</b> The relative reproductive efficiency of a genotype compared to the most favored genotype (scaled from 0 to 1.0).</li>"
        "<li><b>Selection Coefficient (s):</b> The proportional reduction in reproductive fitness against a disfavored genotype: "
        "<br><code>s = 1 - W</code> &nbsp;&rArr;&nbsp; <code>W = 1 - s</code>.</li>"
        "<li><b>Selection Against Recessive Homozygotes (aa):</b>"
        "<br>Let genotypes AA, Aa, aa have fitness values 1, 1, and 1 - s. "
        "<br>Change in recessive gene frequency per generation: "
        "<br><code>&Delta;q = - [ s &times; p &times; q&sup2; ] / [ 1 - s &times; q&sup2; ]</code>.</li>"
        "<li><b>Complete Selection Against Recessive (s = 1.0; e.g., Culling all Horned calves or Lethal recessives):</b>"
        "<br>When recessive homozygotes fail to reproduce entirely (W = 0, s = 1.0): "
        "<br><code>q₁ = q₀ / (1 + q₀)</code>, and after 't' generations: <code>q_t = q₀ / (1 + t &times; q₀)</code>. "
        "<br>Number of generations required to reduce gene frequency from q₀ to q_t: <code>t = (1 / q_t) - (1 / q₀)</code>.</li>"
        "<li><i>Topper Examination Insight:</i> As a recessive allele becomes rare (q &lt; 0.05), selection becomes <b>increasingly inefficient</b> because almost all mutant alleles are hidden in heterozygous carriers (2pq) shielded from phenotypic selection!</li>"
        "</ul><br>"
        "<b>4. GENETIC DRIFT (THE SEWALL WRIGHT EFFECT)</b><br>"
        "In small, finite populations, gametes uniting to form the next generation represent a small random sample of parental alleles. Due to random sampling error, gene frequencies fluctuate erratically from generation to generation purely by chance:"
        "<ul>"
        "<li><b>Sampling Variance of Gene Frequency:</b> <code>&sigma;&sup2;_&Delta;q = p &times; q / (2 N_e)</code>, where N_e is the <b>Effective Population Size</b>.</li>"
        "<li><b>Consequences of Genetic Drift:</b> (a) Random fixation of one allele (p = 1.0) and permanent loss of the alternative allele (q = 0); (b) Loss of heterozygosity at a rate of <code>1 / (2N_e)</code> per generation; (c) Differentiation of isolated sub-populations into distinct genetic lines.</li>"
        "<li><b>Founder Effect:</b> Genetic drift occurring when a new herd is established by a very small number of founding animals, carrying unrepresentative gene frequencies (e.g., establishing a new rabbit colony from two pairs).</li>"
        "<li><b>Bottleneck Effect:</b> A severe, catastrophic reduction in herd size due to disease outbreak, famine, or natural disaster, randomly purging alleles regardless of fitness.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Mutation-Selection Balance:</b><br>"
        "Harmful recessive lethal mutations (like BLAD in cattle) are continuously eliminated by natural and artificial selection, yet persist in populations. "
        "At <b>Mutation-Selection Equilibrium</b>, the rate of loss of alleles by selection equals the rate of input of new alleles by recurrent mutation: "
        "<br>Rate of loss by selection &approx; <code>s &times; q&sup2;</code> (or <code>q&sup2;</code> when s = 1). "
        "<br>Rate of gain by mutation = <code>&mu; &times; p &approx; &mu;</code> (since p &approx; 1.0). "
        "<br>Equating both rates: <code>s &times; q&sup2; = &mu;</code> &nbsp;&rArr;&nbsp; <b>Equilibrium Recessive Frequency:</b> <code>q&#770; = &radic;(&mu; / s)</code>. "
        "<br>For a completely lethal recessive gene (s = 1.0): <code>q&#770; = &radic;&mu;</code>. "
        "If mutation rate &mu; = 10⁻⁶, the equilibrium frequency of the lethal allele is <code>q = &radic;(10⁻⁶) = 10⁻³ = 0.001</code>, maintaining carrier frequency at <code>2pq &approx; 0.002</code> (1 in 500 animals), proving why recessive defects can never be eradicated completely by phenotypic culling alone."
    ),
    "keyPoints": [
        "Four primary forces change gene frequencies: Mutation, Migration, Selection, and Genetic Drift.",
        "Systematic forces (Mutation, Migration, Selection) are predictable in direction and magnitude.",
        "Genetic Drift is a stochastic dispersive force predictable in magnitude (pq/2Ne) but random in direction.",
        "Mutational equilibrium frequency: q̂ = μ / (μ + ν).",
        "Migration change in gene frequency: Δq = m(q_m - q₀).",
        "Selection is differential reproductive success; fitness W = 1 - s (where s is selection coefficient).",
        "Under complete selection against recessives (s = 1): q_t = q₀ / (1 + t · q₀).",
        "Generations required to reduce recessive gene frequency: t = (1 / q_t) - (1 / q₀).",
        "Selection becomes highly inefficient when the recessive allele becomes rare because alleles hide in heterozygotes.",
        "Genetic drift causes random fixation or loss of alleles and reduces heterozygosity at a rate of 1 / (2Ne).",
        "Founder effect and population bottlenecks drastically alter gene frequencies in small livestock herds.",
        "Mutation-Selection balance maintains deleterious recessive alleles at equilibrium: q̂ = √(μ / s)."
    ],
    "clinical": (
        "In artificial insemination studs, if a dairy bull carrying the recessive Citrullinemia mutation (s = 1.0 lethal) is selected and used to produce 50,000 semen straws disseminated across a state, this represents massive artificial directional migration (m). The lethal carrier frequency in the rural cattle population jumps from 0.001 to over 0.05 within a single breeding season, causing widespread neonate calf mortality unless pedigree carrier screening is enforced."
    ),
    "tables": [
        {
            "title": "Comprehensive Summary of the Four Evolutionary Forces Changing Gene Frequencies",
            "headers": ["Evolutionary Force", "Nature of Force", "Mathematical Equation for &Delta;q", "Speed of Frequency Change in Livestock"],
            "rows": [
                ["Mutation", "Systematic (predictable direction)", "&Delta;q = &mu;p - &nu;q", "Extremely slow; negligible impact in commercial breeding time"],
                ["Migration (Gene Flow)", "Systematic (predictable direction)", "&Delta;q = m (q_m - q₀)", "Rapid; immediate frequency shift proportional to immigrant proportion m"],
                ["Selection", "Systematic (predictable direction)", "&Delta;q = - [ s p q&sup2; ] / [ 1 - s q&sup2; ]", "Very powerful and rapid for intermediate frequencies; primary breeding tool"],
                ["Genetic Drift", "Dispersive (random direction)", "Var(&Delta;q) = p q / (2 N_e)", "Rapid in small herds (N &lt; 50); negligible in large populations (N &gt; 1000)"]
            ]
        }
    ],
    "img": "",
    "tags": ["evolutionary-forces", "mutation-pressure", "migration", "selection-coefficient", "genetic-drift", "sewall-wright", "founder-effect"]
}

topics["u2-t23"] = {
    "summary": "Quantitative traits exhibit continuous metric variation governed by multiple additive polygenes and environmental influences, contrasting sharply with discrete, single-gene Mendelian qualitative traits.",
    "desc": (
        "<b>COMPARISON OF QUALITATIVE AND QUANTITATIVE TRAITS</b><br>"
        "In livestock and poultry production, traits are broadly classified into two distinct genetic categories:"
        "<ul>"
        "<li><b>Qualitative (Discontinuous) Traits:</b> Traits that exhibit distinct, discrete categorical variation without intermediates (e.g., Polled vs Horned cattle; Black vs Red coat color; Rose vs Single comb in poultry). "
        "<br>&bull; Governed by one or two major genes (<b>Oligogenic inheritance</b>). "
        "<br>&bull; Environmental influence is negligible; phenotype directly reveals genotype. "
        "<br>&bull; Analyzed by counting frequencies and testing Mendelian ratios (3:1, 9:3:3:1) using Chi-square tests.</li>"
        "<li><b>Quantitative (Continuous / Metric) Traits:</b> Traits that exhibit a continuous, unbroken spectrum of phenotypic variation across a metric scale (e.g., 305-day lactation milk yield in Sahiwal cattle; body weight in broilers; wool yield in sheep; egg production in layers). "
        "<br>&bull; Governed by a large number of genes (<b>Polygenic inheritance</b>), each exerting a small, individually imperceptible additive effect. "
        "<br>&bull; Substantially influenced by environmental variations (nutrition, climate, disease, management). "
        "<br>&bull; Analyzed using biometrical statistics: Means, Variances, Covariances, Heritability (h²), and Repeatability (r).</li>"
        "</ul><br>"
        "<b>THE MULTIPLE FACTOR (POLYGENIC) HYPOTHESIS</b><br>"
        "Formulated by Swedish plant breeder <b>H. Nilsson-Ehle (1909)</b> through kernel color experiments in wheat, and mathematically unified with Mendelian genetics by <b>Sir R. A. Fisher (1918)</b>:"
        "<ul>"
        "<li>A quantitative continuous trait is governed by multiple independent Mendelian loci (polygenes).</li>"
        "<li>Each contributing allele exerts a small, cumulative <b>additive effect</b> (+d) on the phenotype without complete dominance. Non-contributing alleles add zero (0).</li>"
        "<li>As the number of polygenic loci increases (from 1 locus &rarr; 2 loci &rarr; 10 loci &rarr; 100 loci), the number of discrete phenotypic classes increases exponentially, and the gaps between classes shrink.</li>"
        "<li>When micro-environmental variation is superimposed upon this multi-locus distribution, the jagged discrete histogram smooths out into a <b>Continuous Bell-Shaped Normal Gaussian Curve</b>!</li>"
        "</ul><br>"
        "<b>PROPERTIES OF POLYGENES IN ANIMAL BREEDING</b>"
        "<ol>"
        "<li><b>Infinitesimal Model:</b> Quantitative traits are controlled by an extremely large (theoretically infinite) number of loci, each with an infinitesimally small effect.</li>"
        "<li><b>Lack of Complete Dominance:</b> Genes act primarily through additive genetic effects.</li>"
        "<li><b>Sensitivity to Environment:</b> The phenotype is the joint product of genotype and environment: <code>P = G + E</code>.</li>"
        "<li><b>Transgressive Segregation:</b> Crossing two intermediate parents can produce extreme F₂ progeny that outperform both parents due to novel combinations of positive additive polygenes.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Number of Polygenic Loci Estimation (Castle-Wright Formula):</b><br>"
        "To estimate the minimum number of segregating polygenic loci (k) contributing to a quantitative trait in livestock crosses between two extreme inbred lines (means X&#772;₁ and X&#772;₂): "
        "<br><code>k = (X&#772;₁ - X&#772;₂)&sup2; / [ 8 &times; (Var(F₂) - Var(F₁)) ]</code>. "
        "Here, <code>Var(F₁)</code> represents purely environmental variance (since F₁ is genetically uniform), while <code>Var(F₂)</code> contains both genetic and environmental variance. "
        "The difference <code>[Var(F₂) - Var(F₁)]</code> isolates the additive genetic variance, mathematically estimating the number of effective polygenic factors."
    ),
    "keyPoints": [
        "Qualitative traits exhibit discrete discontinuous variation governed by 1–2 major genes (oligogenic).",
        "Quantitative traits exhibit continuous metric variation governed by multiple polygenes (polygenic).",
        "Qualitative traits are minimally affected by environment; quantitative traits are heavily influenced by environment.",
        "Quantitative traits are evaluated biometrically using means, variances, covariances, and normal distributions.",
        "The Multiple Factor Hypothesis was formulated by H. Nilsson-Ehle (1909) and unified by R. A. Fisher (1918).",
        "Polygenes exert small, cumulative additive effects on the phenotype.",
        "Continuous normal curves in livestock traits result from polygenic inheritance combined with environmental noise.",
        "Basic quantitative model: Phenotype = Genotype + Environment (P = G + E).",
        "Virtually all economically important traits in dairy, poultry, sheep, and swine are quantitative traits.",
        "Transgressive segregation produces offspring with phenotypes more extreme than either parent.",
        "Castle-Wright formula estimates the effective number of polygenic loci segregating in a cross."
    ],
    "clinical": (
        "In dairy cattle breeding, 305-day lactation milk yield is a classic polygenic quantitative trait controlled by over 10,000 segregating SNPs across all 29 autosomes. Because environmental factors (temperature-humidity index THI, silage quality, subclinical mastitis) contribute over 70% of total phenotypic variance (heritability h² &approx; 0.25–0.30), a veterinarian cannot judge a bull's genetic merit by simply looking at his mother's raw milk yield; sophisticated biometrical BLUP breeding values are required."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Qualitative versus Quantitative Genetics in Farm Livestock",
            "headers": ["Parameter", "Qualitative Genetics", "Quantitative (Biometrical) Genetics"],
            "rows": [
                ["Type of Variation", "Discontinuous, discrete categorical classes with clear gaps", "Continuous, metric spectrum without discrete boundaries"],
                ["Number of Genes Involved", "One or two major genes (Oligogenic / Monogenic)", "Large number of polygenes (Polygenic / Infinitesimal model)"],
                ["Environmental Influence", "Negligible; phenotype directly reflects genotype", "Substantial; environment masks individual gene expression"],
                ["Measurement Scale", "Nominal counts and frequencies (proportions, percentages)", "Continuous physical scales (kg, liters, days, cm)"],
                ["Primary Statistical Tools", "Ratios (3:1, 9:3:3:1) and Pearson's Chi-square (&chi;&sup2;) test", "Means, Variances, SD, CV, ANOVA, Correlation, Regression"],
                ["Livestock Examples", "Coat color, horned/polled condition, lethal genetic defects", "305-day milk yield, body weight, fleece weight, egg production"]
            ]
        }
    ],
    "img": "",
    "tags": ["quantitative-genetics", "qualitative-traits", "polygenic-inheritance", "nilsson-ehle", "r-a-fisher", "multiple-factor-hypothesis"]
}

topics["u2-t24"] = {
    "summary": "The average effect of a gene and gene substitution quantify the expected phenotypic change from allele transmission, establishing Breeding Value (additive genetic value) as the parent's value in livestock genetic improvement.",
    "desc": (
        "<b>MATHEMATICAL MODEL OF POPULATION MEAN</b><br>"
        "In quantitative genetics, we evaluate an arbitrary single locus with two alleles, A₁ and A₂, with gene frequencies <code>p</code> and <code>q</code>. "
        "We define the genotypic values as deviations from the midpoint between the two homozygotes:"
        "<ul>"
        "<li>Genotype <code>A₁A₁</code> has genotypic value <b>+a</b>.</li>"
        "<li>Genotype <code>A₂A₂</code> has genotypic value <b>-a</b>.</li>"
        "<li>Heterozygote <code>A₁A₂</code> has genotypic value <b>d</b> (degree of dominance). "
        "<br>&bull; If d = 0: No dominance (mid-parent value). "
        "<br>&bull; If d = +a: Complete dominance of A₁. "
        "<br>&bull; If d &gt; a: Overdominance.</li>"
        "<li><b>Population Mean (&mu;):</b> The average genotypic value across the population in Hardy-Weinberg equilibrium: "
        "<br><code>&mu; = p&sup2;(+a) + 2pq(d) + q&sup2;(-a) = a(p - q) + 2pqd</code>.</li>"
        "</ul><br>"
        "<b>AVERAGE EFFECT OF A GENE (&alpha;₁ AND &alpha;₂)</b><br>"
        "Parents do not transmit intact diploid genotypes (AA, Aa, or aa) to their offspring; they transmit individual haploid gametes carrying a single allele (A₁ or A₂). "
        "The <b>Average Effect of a Gene</b> is the mean deviation from the population mean of individuals that received that specific allele from one parent, while the allele from the other parent was drawn at random from the population gene pool:"
        "<ul>"
        "<li><b>Average Effect of Allele A₁:</b> <code>&alpha;₁ = q [ a + d(q - p) ]</code></li>"
        "<li><b>Average Effect of Allele A₂:</b> <code>&alpha;₂ = - p [ a + d(q - p) ]</code></li>"
        "<li>Notice that: <code>p &alpha;₁ + q &alpha;₂ = 0</code> (sum of average effects weighted by allele frequencies is zero).</li>"
        "</ul><br>"
        "<b>AVERAGE EFFECT OF GENE SUBSTITUTION (&alpha;)</b><br>"
        "The <b>Average Effect of Gene Substitution (&alpha;)</b> is the expected change in the population mean when one allele (A₂) is systematically replaced (substituted) by its alternative allele (A₁) in the population: "
        "<br><br>"
        "<code>&alpha; = &alpha;₁ - &alpha;₂ = a + d(q - p)</code>"
        "<br><br>"
        "where <code>&alpha;₁ = q &alpha;</code> and <code>&alpha;₂ = - p &alpha;</code>. "
        "If there is no dominance (d = 0), the average effect of gene substitution is simply equal to the genotypic value: <code>&alpha; = a</code>.<br><br>"
        "<b>BREEDING VALUE (ADDITIVE GENETIC VALUE - A)</b><br>"
        "The <b>Breeding Value (BV)</b> of an individual animal is the value of that animal as a genetic parent. "
        "Formally, it is defined as <b>twice the expected deviation of its progeny mean from the population mean</b> when the individual is mated at random to a large sample of animals from the population:"
        "<br><br>"
        "<code>Breeding Value (BV) = 2 &times; (Progeny Mean - Population Mean) = 2 (P&#772;_prog - &mu;)</code>"
        "<br><br>"
        "<i>Why Multiply by 2?</i> Because the parent transmits only a sample half (50%) of its genes to its offspring; the other 50% comes from the random mates. Multiplying by 2 restores the parent's full genetic contribution.<br><br>"
        "<b>Breeding Values of the Three Genotypes:</b>"
        "<ul>"
        "<li><code>BV of A₁A₁ = 2 &alpha;₁ = 2q &alpha;</code></li>"
        "<li><code>BV of A₁A₂ = &alpha;₁ + &alpha;₂ = (q - p) &alpha;</code></li>"
        "<li><code>BV of A₂A₂ = 2 &alpha;₂ = - 2p &alpha;</code></li>"
        "</ul><br>"
        "<b>TRANSMITTING ABILITY AND EXPECTED PROGENY DIFFERENCE (EPD)</b><br>"
        "The half of the breeding value that a parent actually transmits to its offspring is called its <b>Transmitting Ability (TA)</b> or <b>Expected Progeny Difference (EPD)</b>:"
        "<br><br>"
        "<code>Transmitting Ability (TA) = EPD = 0.5 &times; Breeding Value (BV)</code>"
        "<br><br>"
        "When two selected parents are mated, the expected performance of their offspring is: "
        "<br><code>Expected Progeny Value = &mu; + 0.5 BV_sire + 0.5 BV_dam</code>."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Partitioning of Genotypic Value: Genotypic Value = BV + Dominance Deviation (G = A + D):</b><br>"
        "The true genotypic value (G) of an animal does not equal its Breeding Value (A) unless gene action is strictly additive (d = 0). "
        "The discrepancy between the genotypic value and the breeding value is the <b>Dominance Deviation (D)</b>: "
        "<br><code>G = A + D</code> (or with epistasis: <code>G = A + D + I</code>). "
        "The Dominance Deviation represents the specific intra-allelic interaction between the two alleles in that diploid individual. "
        "<b>Crucial Exam Insight:</b> An animal <b>CANNOT transmit its dominance deviation (D)</b> to its progeny because diploid allelic combinations are torn apart into single haploid alleles during meiosis! "
        "Therefore, an elite cow with high milk yield due to favorable dominance (heterosis) cannot reliably pass that superiority to her calves. <b>Only the Additive Breeding Value (A) is transmitted to offspring</b>!"
    ),
    "keyPoints": [
        "Genotypic values are expressed as deviations from homozygote midpoint: +a (A₁A₁), d (A₁A₂), -a (A₂A₂).",
        "Population mean formula in Hardy-Weinberg equilibrium: μ = a(p - q) + 2pqd.",
        "Average effect of a gene is the mean deviation of progeny receiving that allele from the population mean.",
        "Sum of average effects weighted by gene frequency is zero: pα₁ + qα₂ = 0.",
        "Average effect of gene substitution: α = α₁ - α₂ = a + d(q - p).",
        "Breeding Value (BV) is the value of an animal as a parent, defined as 2 × (Progeny Mean - Population Mean).",
        "Breeding value is multiplied by 2 because a parent contributes only half (50%) of its genes to offspring.",
        "Breeding values of genotypes: BV(A₁A₁) = 2qα; BV(A₁A₂) = (q - p)α; BV(A₂A₂) = -2pα.",
        "Transmitting Ability (TA) or Expected Progeny Difference (EPD) is exactly half the Breeding Value: TA = 0.5 · BV.",
        "Genotypic value partitions into Additive breeding value and Dominance deviation: G = A + D.",
        "Dominance and epistatic interactions are not transmitted to offspring because genotypes are dismantled at meiosis.",
        "Only the Additive Breeding Value (A) is inherited by progeny and responds to artificial selection."
    ],
    "clinical": (
        "In commercial dairy sire catalogs published by BAIF or NDDB, top Sahiwal and Murrah breeding bulls are ranked by their Estimated Breeding Value (EBV) or Predicted Transmitting Ability (PTA) for 305-day milk yield. A bull with a PTA of +350 kg is expected to sire daughters that produce, on average, 350 kg more milk per lactation than daughters of an average bull (PTA = 0) under identical herd management."
    ),
    "tables": [
        {
            "title": "Mathematical Partitioning of Genotypic Value into Additive Breeding Value and Dominance Deviation",
            "headers": ["Genotype", "Genotypic Value (G)", "Additive Breeding Value (A)", "Dominance Deviation (D = G - A)"],
            "rows": [
                ["A₁A₁ (Homozygous)", "+ a", "2 q &alpha;", "- 2 q&sup2; d"],
                ["A₁A₂ (Heterozygous)", "+ d", "(q - p) &alpha;", "+ 2 p q d"],
                ["A₂A₂ (Homozygous)", "- a", "- 2 p &alpha;", "- 2 p&sup2; d"]
            ]
        }
    ],
    "img": "",
    "tags": ["breeding-value", "average-effect", "gene-substitution", "additive-value", "dominance-deviation", "transmitting-ability", "epd"]
}

topics["u2-t25"] = {
    "summary": "Phenotypic variance partitions into additive genetic variance (the sole driver of selection progress), non-additive dominance and epistatic variances, and environmental variance components.",
    "desc": (
        "<b>PARTITIONING OF TOTAL PHENOTYPIC VARIANCE (V_P)</b><br>"
        "In a livestock population, the observable metric variation among animals for any quantitative trait is the <b>Phenotypic Variance (V_P)</b>. "
        "Formulated by Sir Ronald A. Fisher (1918), phenotypic variance is partitioned into genetic and environmental components:"
        "<br><br>"
        "<code>V_P = V_G + V_E + 2 Cov_GE + V_GE</code>"
        "<br><br>"
        "In standard experimental herds where genotypes are randomized across environments, the covariance between genotype and environment (<code>Cov_GE</code>) and the genotype-environment interaction (<code>V_GE</code>) are assumed to be zero or controlled, simplifying the model to: "
        "<br><code>V_P = V_G + V_E</code>.<br><br>"
        "<b>1. GENETIC VARIANCE (V_G) AND ITS SUB-COMPONENTS</b><br>"
        "Genetic variance is the portion of total phenotypic variance attributable to differences in genetic constitution among individuals. It is partitioned into three mutually exclusive biological components: "
        "<br><br>"
        "<code>V_G = V_A + V_D + V_I</code>"
        "<br><br>"
        "<ul>"
        "<li><b>A. Additive Genetic Variance (V_A):</b>"
        "<br>The variance of breeding values (<code>V_A = Var(A) = 2pq &alpha;&sup2;</code>). "
        "<br>Represents the variance arising from the additive, cumulative effects of individual genes across all segregating loci. "
        "<br><i>Crucial Principle:</i> <b>V_A is the single most important component in animal breeding!</b> It is the chief cause of resemblance between biological relatives, the basis of heritability in the narrow sense, and the <b>sole component that responds permanently to individual mass selection</b>!</li>"
        "<li><b>B. Dominance Genetic Variance (V_D):</b>"
        "<br>The variance of dominance deviations (<code>V_D = Var(D) = (2pqd)&sup2;</code>). "
        "<br>Arises from the non-additive interaction between alleles at the <b>same gene locus</b> (intra-allelic interaction). "
        "<br>Because diploid allelic combinations are disrupted during meiotic reduction, V_D is not transmitted from parent to offspring. It is the primary biological basis of <b>Heterosis (Hybrid Vigor)</b>, exploited through crossbreeding.</li>"
        "<li><b>C. Epistatic (Interaction) Genetic Variance (V_I):</b>"
        "<br>Arises from non-additive interactions between genes at <b>two or more different loci</b> (inter-allelic interaction). "
        "<br>Further partitioned into: <code>V_I = V_AA + V_AD + V_DD + ...</code> (Additive &times; Additive, Additive &times; Dominance, Dominance &times; Dominance variances). Largely broken by meiotic recombination.</li>"
        "</ul><br>"
        "<b>2. ENVIRONMENTAL VARIANCE (V_E) AND ITS SUB-COMPONENTS</b><br>"
        "Environmental variance includes all non-genetic sources of variation (nutrition, ambient climate, housing, disease, subclinical infections, milking management). "
        "For traits with repeated measurements over an animal's lifetime (e.g., multiple lactation records in dairy cows or multiple shearing records in sheep), V_E is subdivided into: "
        "<br><br>"
        "<code>V_E = V_Eg + V_Es</code>"
        "<br><br>"
        "<ul>"
        "<li><b>A. General (Permanent) Environmental Variance (V_Eg):</b>"
        "<br>Non-genetic environmental influences that affect the animal permanently, persisting across all subsequent lactations or production cycles throughout its lifetime. "
        "<br><i>Livestock Examples:</i> Severe calfhood malnutrition stunting skeletal frame size; permanent quarter destruction from severe clinical mastitis in first lactation; early calfhood lung damage from pneumonia. "
        "<br>V_Eg contributes to repeated performance and is captured in <b>Repeatability (r)</b>, but is <b>never transmitted to offspring</b>.</li>"
        "<li><b>B. Special (Temporary) Environmental Variance (V_Es):</b>"
        "<br>Localized, transient environmental fluctuations that affect only a single individual record or lactation, varying from day to day or year to year. "
        "<br><i>Livestock Examples:</i> A temporary spike in ambient temperature on the day of milk recording; temporary feed shortage; transient estrus excitement. Does not persist into the next lactation.</li>"
        "</ul><br>"
        "<b>THE COMPLETE EXPANDED PHENOTYPIC VARIANCE EQUATION:</b><br>"
        "<code>V_P = (V_A + V_D + V_I) + (V_Eg + V_Es)</code>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Mathematical Derivation of Additive Variance (V_A):</b><br>"
        "For a single biallelic locus in Hardy-Weinberg equilibrium with gene substitution effect &alpha;: "
        "The breeding values of AA, Aa, and aa are <code>2q&alpha;</code>, <code>(q - p)&alpha;</code>, and <code>-2p&alpha;</code>. "
        "The additive genetic variance is the mean of squared breeding values: "
        "<br><code>V_A = p&sup2;(2q&alpha;)&sup2; + 2pq[(q - p)&alpha;]&sup2; + q&sup2;(-2p&alpha;)&sup2;</code>"
        "<br><code>V_A = &alpha;&sup2; [ 4p&sup2;q&sup2; + 2pq(q - p)&sup2; + 4p&sup2;q&sup2; ] = &alpha;&sup2; [ 8p&sup2;q&sup2; + 2pq(q&sup2; - 2pq + p&sup2;) ]</code>"
        "<br><code>V_A = 2pq &alpha;&sup2; [ 4pq + q&sup2; - 2pq + p&sup2; ] = 2pq &alpha;&sup2; [ p&sup2; + 2pq + q&sup2; ] = 2pq &alpha;&sup2; (1) = 2pq &alpha;&sup2;</code>! "
        "This proves that Additive Variance is maximal when <code>p = q = 0.5</code> (<code>V_A = 0.5 &alpha;&sup2;</code>). "
        "If an allele is fixed (p = 1.0 or q = 1.0), additive genetic variance drops to zero, and selection progress halts."
    ),
    "keyPoints": [
        "Total Phenotypic Variance partitions into Genetic and Environmental components: V_P = V_G + V_E.",
        "Genetic Variance partitions into Additive, Dominance, and Epistatic variances: V_G = V_A + V_D + V_I.",
        "Additive Genetic Variance (V_A) is the variance of breeding values: V_A = 2pqα².",
        "V_A is the chief cause of resemblance between relatives and the sole driver of response to mass selection.",
        "Dominance Variance (V_D) arises from intra-allelic interactions: V_D = (2pqd)².",
        "V_D is not transmitted to offspring; it forms the primary biological basis of Heterosis (Hybrid Vigor).",
        "Epistatic Variance (V_I) arises from non-allelic interactions between different gene loci.",
        "Environmental Variance partitions into General permanent (V_Eg) and Special temporary (V_Es) components.",
        "General environmental variance (V_Eg) affects all records of an animal permanently (e.g., mastitic quarter loss).",
        "Special environmental variance (V_Es) represents transient, day-to-day fluctuations (e.g., weather, feed glitch).",
        "Complete phenotypic model: V_P = V_A + V_D + V_I + V_Eg + V_Es.",
        "Additive variance reaches its theoretical maximum when gene frequencies are equal: p = q = 0.5."
    ],
    "clinical": (
        "When evaluating a dairy cow whose 1st lactation milk yield was 4,200 kg but dropped to 2,800 kg in her 2nd lactation following gangrenous mastitis that destroyed two rear udder quarters, the breeding manager correctly recognizes that the 1,400 kg drop represents permanent general environmental variance (V_Eg). Her transmitted additive genetic merit (BV) to her progeny remains completely undamaged by the somatic udder injury."
    ),
    "tables": [
        {
            "title": "Components of Phenotypic Variance and Their Transmission Properties in Livestock",
            "headers": ["Variance Component", "Biological Source / Mechanism", "Transmitted to Progeny?", "Breeding & Selection Role"],
            "rows": [
                ["Additive Genetic Variance (V_A)", "Average additive effects of individual alleles (breeding values)", "YES (100% transmitted via sample half)", "Drives response to individual mass selection; determines h²_narrow"],
                ["Dominance Genetic Variance (V_D)", "Intra-allelic interaction at same locus (dominance deviations)", "NO (diploid genotype dismantled at meiosis)", "Underlies heterosis; exploited via crossbreeding and line crossing"],
                ["Epistatic Genetic Variance (V_I)", "Inter-allelic interactions between different gene loci", "NO (mostly broken by crossing over & assortment)", "Contributes to breed-specific nicking ability and strain synthesis"],
                ["Permanent Environment (V_Eg)", "Long-lasting non-genetic factors (calfhood nutrition, chronic disease)", "NO (strictly somatic environmental)", "Causes animal to repeat its performance; component of Repeatability"],
                ["Temporary Environment (V_Es)", "Transient, localized daily noise (heat stress, feed changes)", "NO (non-genetic random noise)", "Reduces correlation between repeated measurements on the same animal"]
            ]
        }
    ],
    "img": "",
    "tags": ["phenotypic-variance", "additive-variance", "dominance-variance", "epistatic-variance", "environmental-variance", "v-a", "v-e"]
}

topics["u2-t26"] = {
    "summary": "Genotype by Environment (G × E) interaction occurs when the relative phenotypic performance or ranking of different genotypes changes across differing environmental conditions, dictating breed adaptability.",
    "desc": (
        "<b>CONCEPT OF GENOTYPE BY ENVIRONMENT (G &times; E) INTERACTION</b><br>"
        "In basic quantitative genetics, phenotypic performance is assumed to be a simple additive sum of genotype and environment: <code>P = G + E</code>. "
        "This linear model assumes that the superior genotype in Environment 1 remains equally superior in Environment 2. "
        "However, in animal agriculture, a <b>Genotype by Environment (G &times; E) Interaction</b> occurs when the phenotypic difference between two or more genotypes depends directly on the specific environment in which they are raised, causing non-parallel reaction norms.<br><br>"
        "<b>TYPES OF G &times; E INTERACTION</b><br>"
        "<ol>"
        "<li><b>Scaling Effect (Without Change in Rank):</b>"
        "<br>The difference in performance between genotypes changes in magnitude across environments, but the <b>relative ranking of genotypes remains identical</b>. "
        "<br><i>Livestock Example:</i> Crossbred HF cows produce 20 liters/day and indigenous Sahiwal cows produce 12 liters/day in a high-input intensive dairy farm (Diff = 8 liters). Under rural smallholder low-input feeding, HF cows produce 10 liters and Sahiwal cows produce 7 liters (Diff = 3 liters). HF cows remain superior in both environments (no rank change), but the genetic superiority is scaled down under poor nutrition.</li>"
        "<li><b>Reversal of Ranking (True Cross-Over Interaction):</b>"
        "<br>The <b>ranking of genotypes reverses completely</b> across different environments. The superior genotype in one environment becomes inferior in the other! "
        "<br><i>Livestock Example:</i> Under optimal, temperature-controlled, disease-free commercial conditions, exotic Holstein-Friesian cattle vastly outproduce native zebu cattle. "
        "However, under harsh, hot-humid Indian tropical field conditions with high ambient heat, severe tick burden, and low-quality coarse crop residues, native zebu cattle (e.g., Tharparkar, Gir) significantly outperform Holstein-Friesians because of superior thermotolerance, sweat gland density, tick resistance, and low-roughage digestive efficiency!</li>"
        "</ol><br>"
        "<b>GENOTYPE-ENVIRONMENT CORRELATION (r_GE)</b><br>"
        "Distinct from interaction, <b>Genotype-Environment Correlation</b> occurs when different genotypes are <b>not distributed randomly</b> across environments, but are non-randomly paired with specific environments:"
        "<ul>"
        "<li><b>Positive Correlation:</b> Superior genotypes are deliberately provided superior nutritional environments (e.g., progressive dairy farmers giving their highest-yielding pedigreed cows the best green fodder, bypass fat, and fan-cooled housing).</li>"
        "<li><b>Negative Correlation:</b> Inferior genotypes provided superior care to compensate (e.g., giving extra milk replacer to runt or weak calves).</li>"
        "</ul><br>"
        "<b>PRACTICAL LIVESTOCK IMPLICATIONS IN INDIA</b>"
        "<ol>"
        "<li><b>Selection Environment Rule:</b> Breeding animals must be selected and progeny-tested <b>in the exact commercial environment (or agro-climatic zone) in which their commercial progeny will be required to produce</b>! Selecting dairy bulls under air-conditioned elite nucleus research stations fails to identify bulls whose daughters thrive in rural farmer village environments.</li>"
        "<li><b>Failure of Exotic Direct Importations:</b> Explains why purebred temperate European breeds (Holstein, Jersey) imported directly into tropical Indian rural conditions frequently suffer severe heat prostration, high mortality, chronic repeat breeding, and massive production crashes.</li>"
        "<li><b>Need for Composite Breeds:</b> Justifies the creation of hardy crossbred synthetic strains (e.g., Frieswal = 62.5% HF + 37.5% Sahiwal), combining high dairy yield with tropical environmental resilience.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Statistical Detection of G &times; E Interaction via Two-Way ANOVA:</b><br>"
        "In a factorial experimental design with 'g' genotypes evaluated across 'e' environments with 'r' replications: "
        "<br>The statistical model is: <code>Y_ijk = &mu; + G_i + E_j + (GE)_ij + &epsilon;_ijk</code>. "
        "<br>&bull; Degrees of freedom for G &times; E interaction: <code>df = (g - 1) &times; (e - 1)</code>. "
        "<br>&bull; F-test statistic for interaction: <code>F_GE = MS_GE / MS_Error</code>. "
        "<br>If F_GE is statistically significant (p &lt; 0.05), G &times; E interaction is proven. "
        "Furthermore, D. S. Falconer demonstrated that the performance of the same genotype in two different environments can be mathematically treated as <b>two distinct genetic traits</b>, computing the <b>genetic correlation (r_G)</b> between them. If <code>r_G &lt; 0.80</code>, G &times; E interaction is biologically significant, requiring separate breeding programs for each environment."
    ),
    "keyPoints": [
        "Genotype by Environment (G × E) interaction occurs when relative performance of genotypes changes across environments.",
        "Scaling effect alters the magnitude of performance differences without changing genotype rank order.",
        "Reversal of ranking (cross-over interaction) completely flips genotype ranks between environments.",
        "Genotype-Environment correlation (r_GE) is the non-random association of genotypes with specific environments.",
        "Positive r_GE occurs when high-merit dairy cows are provided superior nutritional management.",
        "Selection should occur in the commercial environment where progeny are expected to perform.",
        "Exotic temperate cattle underperform in tropical field conditions due to lack of thermotolerance and tick resistance.",
        "G × E interaction justifies crossbreeding exotic dairy cattle with indigenous zebu breeds (e.g., Frieswal).",
        "Two-way factorial ANOVA tests G × E interaction with df = (g - 1)(e - 1).",
        "Falconer's concept: performance in two environments represents two distinct traits; r_G < 0.80 confirms G × E."
    ],
    "clinical": (
        "In the National Dairy Development Board (NDDB) breeding programs, progeny testing of Murrah buffalo bulls is conducted across multiple rural farmer milk-recording centers in diverse agro-climatic zones rather than on a single centralized elite research farm. This multisite evaluation eliminates G &times; E interaction bias, identifying sires with high general adaptability across diverse Indian rural feeding systems."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Scaling Effect versus Rank Reversal in G × E Interaction",
            "headers": ["Parameter", "No G &times; E Interaction", "Scaling G &times; E Interaction", "Rank Reversal G &times; E Interaction"],
            "rows": [
                ["Norms of Reaction", "Completely parallel linear response lines across environments", "Non-parallel linear response lines that diverge but NEVER cross", "Intersecting response lines that cross over (Cross-over interaction)"],
                ["Genotypic Ranking", "Genotype A &gt; Genotype B in all environments", "Genotype A &gt; Genotype B in all environments", "Genotype A &gt; B in Env 1; Genotype B &gt; A in Env 2"],
                ["Magnitude of Difference", "Difference (A - B) remains identical across environments", "Difference (A - B) widens or narrows across environments", "Difference changes algebraic sign (+ to -) across environments"],
                ["Breeding Implication", "A single universal breeding program serves all environments", "Single breeding program sufficient; top sire remains top everywhere", "Must establish separate, independent breeding programs for each environment"]
            ]
        }
    ],
    "img": "",
    "tags": ["gxe-interaction", "reaction-norm", "rank-reversal", "scaling-effect", "genotype-environment-correlation", "tropical-adaptation"]
}

topics["u2-t27"] = {
    "summary": "Heritability (h²) quantifies the proportion of phenotypic variation attributable to genetic differences among individuals, with narrow-sense heritability (V_A/V_P) serving as the fundamental predictor of selection response.",
    "desc": (
        "<b>DEFINITION AND CONCEPTS OF HERITABILITY</b><br>"
        "Heritability is one of the most critical parameters in quantitative genetics and animal breeding. It measures the degree to which phenotypic differences observed among animals are determined by genetic differences. "
        "Formulated by Sewall Wright and Jay L. Lush, heritability is defined in two distinct senses:<br><br>"
        "<b>1. Broad-Sense Heritability (H² or h²_B):</b>"
        "<br>The proportion of total phenotypic variance attributable to <b>total genetic variance</b> (including additive, dominance, and epistatic effects):"
        "<br><br>"
        "<code>H&sup2; = V_G / V_P = (V_A + V_D + V_I) / V_P</code>"
        "<br><br>"
        "Measures the total genetic determination of a trait; useful in clonally propagated plants, but of limited value in sexually reproducing livestock.<br><br>"
        "<b>2. Narrow-Sense Heritability (h² or h²_N):</b>"
        "<br>The proportion of total phenotypic variance attributable exclusively to <b>additive genetic variance</b> (variance of breeding values):"
        "<br><br>"
        "<code>h&sup2; = V_A / V_P = &sigma;&sup2;_A / &sigma;&sup2;_P</code>"
        "<br><br>"
        "<i>Crucial Principle:</i> In animal breeding, whenever the term <b>'Heritability' (h²)</b> is used without qualification, it <b>always refers strictly to Narrow-Sense Heritability</b>! It represents the fraction of parental phenotypic superiority that is reliably transmitted to offspring.<br><br>"
        "<b>KEY PROPERTIES AND CHARACTERISTICS OF HERITABILITY</b>"
        "<ul>"
        "<li><b>Numerical Range:</b> Strictly bounded between 0 and 1.0 (or 0% to 100%): <code>0 &le; h&sup2; &le; 1.0</code>.</li>"
        "<li><b>Population Specificity:</b> Heritability is <b>NOT a fixed biological constant</b> for a species! It is a property of a <i>specific population</i> maintained under a <i>specific environment</i> at a <i>specific time</i>. If management becomes highly uniform (reducing V_E), h² increases. If environmental noise increases, h² decreases.</li>"
        "<li><b>Trait Classification in Farm Livestock:</b>"
        "<br>&bull; <b>High Heritability (h² &gt; 0.40):</b> Skeletal conformation traits, mature body size, butterfat and protein percentage in milk, fleece fiber diameter in sheep. Highly responsive to simple individual mass selection! "
        "<br>&bull; <b>Moderate Heritability (h² = 0.20 to 0.40):</b> 305-day lactation milk yield, birth weight, weaning weight, post-weaning average daily gain (ADG). Responsive to individual and pedigree selection. "
        "<br>&bull; <b>Low Heritability (h² &lt; 0.20):</b> Reproductive and fitness traits (calving interval, service period, fertility rate, litter size in swine, calf survival). Additive variance is low; individual mass selection is ineffective; improvement requires crossbreeding (heterosis) and optimizing herd management/nutrition!</li>"
        "</ul><br>"
        "<b>METHODS OF ESTIMATING HERITABILITY IN LIVESTOCK</b><br>"
        "<ol>"
        "<li><b>Paternal Half-Sib Correlation Method:</b>"
        "<br>The gold standard method for large farm livestock (cattle, buffalo) where one sire is mated to multiple dams, each producing one offspring. "
        "<br>One-way ANOVA partitions variance into <i>Between Sires</i> (&sigma;&sup2;_s) and <i>Within Sires</i> (&sigma;&sup2;_w): "
        "<br>Genetic covariance between paternal half-sibs equals <code>(1/4) V_A</code>. Therefore: "
        "<br><code>h&sup2; = 4 &times; &sigma;&sup2;_s / ( &sigma;&sup2;_s + &sigma;&sup2;_w )</code>. "
        "<br><i>Merit:</i> Free from dominance variance and common maternal environmental effects.</li>"
        "<li><b>Parent-Offspring Regression Method:</b>"
        "<br>Regressing offspring phenotypic performance (Y) on parental performance (X): "
        "<br>&bull; <i>Offspring on Single Parent (Dam or Sire):</i> Covariance between parent and offspring = <code>(1/2) V_A</code>. Therefore: <code>h&sup2; = 2 &times; b_OP</code>. "
        "<br>&bull; <i>Offspring on Mid-Parent Average:</i> <code>h&sup2; = b_O(P&#772;)</code>.</li>"
        "<li><b>Full-Sib Analysis:</b> Covariance between full-sibs = <code>(1/2) V_A + (1/4) V_D + V_Ec</code>. Inflated by dominance and common maternal environment (V_Ec); yields an upper-bound estimate.</li>"
        "<li><b>Realized Heritability from Selection Experiments:</b>"
        "<br>Estimated directly from the response observed in directional selection experiments: "
        "<br><code>h&sup2; = R / S = (Selection Response) / (Selection Differential)</code>.</li>"
        "</ol><br>"
        "<b>PRACTICAL APPLICATIONS IN ANIMAL BREEDING</b><br>"
        "<ul>"
        "<li><b>Predicting Expected Genetic Progress:</b> <code>&Delta;G = R = h&sup2; &times; S</code> (where S is the selection differential).</li>"
        "<li><b>Choice of Selection Method:</b> If h² is high &rarr; Individual Mass Selection; if h² is low &rarr; Progeny Testing and Family Selection.</li>"
        "<li><b>Construction of Selection Indices:</b> Used as weighting factors in multi-trait index selection.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Standard Error of Heritability Estimates:</b><br>"
        "In competitive examinations, calculating the precision of an h² estimate is vital. "
        "For the paternal half-sib correlation method with 's' sires and 'k' offspring per sire (total N = sk): "
        "<br><code>SE(h&sup2;) &approx; 4 &times; &radic;[ (2 (1 - t)&sup2; [ 1 + (k - 1)t ]&sup2;) / (k (k - 1)(s - 1)) ]</code>"
        "<br>where <code>t = h&sup2; / 4</code> is the intra-class correlation. "
        "To achieve a small, acceptable standard error (SE &le; 0.05), large sample sizes are mandatory (e.g., at least 50–100 sires with 20–30 progeny per sire, requiring thousands of animal records). "
        "Negative estimates of h² occasionally obtained from ANOVA are mathematically interpreted as sampling error artifacts and set to zero."
    ),
    "keyPoints": [
        "Heritability measures the proportion of phenotypic variance attributable to genetic variance.",
        "Broad-sense heritability: H² = V_G / V_P = (V_A + V_D + V_I) / V_P.",
        "Narrow-sense heritability: h² = V_A / V_P = σ²_A / σ²_P (standard definition in animal breeding).",
        "Heritability is strictly bounded between 0 and 1.0 (0% to 100%).",
        "Heritability is population- and environment-specific; it is not a fixed species constant.",
        "High heritability traits (h² > 0.40): conformation, fat %, mature body size, wool fiber diameter.",
        "Moderate heritability traits (h² = 0.20–0.40): 305-day milk yield, birth weight, growth rate.",
        "Low heritability traits (h² < 0.20): fertility, service period, calving interval, litter size, survival.",
        "Paternal Half-Sib Correlation formula: h² = 4 · σ²_s / (σ²_s + σ²_w).",
        "Parent-Offspring Regression formula: h² = 2 · b_OP (single parent) and h² = b_O(P̄) (mid-parent).",
        "Realized heritability from selection experiments: h² = R / S (Response / Selection Differential).",
        "Genetic gain prediction equation: ΔG = R = h² · S."
    ],
    "clinical": (
        "In a Sahiwal breeding herd where the population mean for 305-day milk yield is 2,200 kg (h² = 0.30), elite cows averaging 3,000 kg are selected as dams of future bulls. The Selection Differential is S = 3,000 - 2,200 = 800 kg. The expected genetic gain in their progeny is &Delta;G = h² &times; S = 0.30 &times; 800 = 240 kg, predicting an offspring herd mean of 2,440 kg milk under identical feeding."
    ),
    "tables": [
        {
            "title": "Representative Heritability Estimates (h²) for Major Economic Traits in Livestock and Poultry",
            "headers": ["Species", "Economic Trait", "Typical Heritability (h²)", "Heritability Category", "Recommended Selection Method"],
            "rows": [
                ["Dairy Cattle / Buffalo", "Milk Fat & Protein Percentage", "0.45 – 0.55", "High (h² &gt; 0.40)", "Individual Mass Selection"],
                ["Dairy Cattle / Buffalo", "305-day Lactation Milk Yield", "0.25 – 0.30", "Moderate (0.20–0.40)", "Progeny Testing + Pedigree Selection"],
                ["Dairy Cattle / Buffalo", "Calving Interval / Service Period", "0.05 – 0.10", "Low (h² &lt; 0.20)", "Improve Management & Nutrition (Heterosis)"],
                ["Sheep", "Fleece Clean Wool Weight", "0.35 – 0.45", "Moderate to High", "Individual Mass Selection at 1st Shearing"],
                ["Swine", "Backfat Thickness", "0.45 – 0.50", "High", "Individual Ultrasonic Mass Selection"],
                ["Poultry (Broiler)", "6-Week Body Weight", "0.35 – 0.40", "Moderate to High", "Individual Mass Selection"],
                ["Poultry (Layer)", "Annual Egg Production (Survivor)", "0.15 – 0.25", "Low to Moderate", "Family and Sib Selection"]
            ]
        }
    ],
    "img": "",
    "tags": ["heritability", "narrow-sense-heritability", "additive-genetic-variance", "paternal-half-sib", "selection-response", "progeny-testing"]
}

topics["u2-t28"] = {
    "summary": "Repeatability (r) measures the correlation between repeated phenotypic records of the same animal over time, setting the upper limit of heritability and enabling the calculation of Most Probable Producing Ability (MPPA).",
    "desc": (
        "<b>CONCEPT AND DEFINITION OF REPEATABILITY</b><br>"
        "In farm livestock, certain production traits can be measured repeatedly on the same individual animal at successive stages of its productive life: "
        "(e.g., 305-day milk yield across 1st, 2nd, 3rd, and 4th lactations in dairy cows; fleece weight across annual shearings in sheep; litter size across farrowings in sows; egg weight across laying cycles in hens). "
        "<b>Repeatability (r)</b> is the phenotypic correlation between repeated measurements of the same trait on the same individual animal over time.<br><br>"
        "<b>MATHEMATICAL FORMULATION IN TERMS OF VARIANCE COMPONENTS</b><br>"
        "Because repeated records are taken on the exact same animal, the animal's genotype (<code>V_G = V_A + V_D + V_I</code>) and its permanent environmental background (<code>V_Eg</code>) remain identical across all measurements. "
        "Only the special temporary environment (<code>V_Es</code>) fluctuates between records. Therefore, Repeatability is defined as: "
        "<br><br>"
        "<code>r = (V_G + V_Eg) / V_P = (V_A + V_D + V_I + V_Eg) / V_P</code>"
        "<br><br>"
        "<b>RELATIONSHIP BETWEEN REPEATABILITY AND HERITABILITY</b><br>"
        "Comparing the equations of Repeatability (r) and Narrow-Sense Heritability (h²):"
        "<ul>"
        "<li><code>h&sup2; = V_A / V_P</code></li>"
        "<li><code>r = (V_A + V_D + V_I + V_Eg) / V_P</code></li>"
        "<li>Notice that the numerator of repeatability contains all the terms of heritability plus dominance, epistasis, and permanent environment!</li>"
        "<li><b>Fundamental Mathematical Axiom:</b> <b>Repeatability is ALWAYS GREATER THAN or equal to Heritability:</b> "
        "<br><code>r &ge; h&sup2;</code>. "
        "Repeatability sets the <b>absolute upper limit of narrow-sense heritability</b> (h² can never exceed r!).</li>"
        "</ul><br>"
        "<b>ESTIMATION OF REPEATABILITY: INTRA-CLASS CORRELATION METHOD</b><br>"
        "Estimated via One-Way Analysis of Variance (ANOVA) with repeated measures, where 'm' records are available for each of 'n' animals:"
        "<ul>"
        "<li>Total df = mn - 1</li>"
        "<li>Between Animals df = n - 1 (Mean Square = MS_Between = <code>&sigma;&sup2;_w + m &sigma;&sup2;_b</code>)</li>"
        "<li>Within Animals df = n(m - 1) (Mean Square = MS_Within = <code>&sigma;&sup2;_w</code>)</li>"
        "<li>Between-Animal Variance Component: <code>&sigma;&sup2;_b = (MS_Between - MS_Within) / m</code></li>"
        "<li>Within-Animal Variance Component: <code>&sigma;&sup2;_w = MS_Within</code></li>"
        "<li><b>Repeatability (Intra-class Correlation, r):</b>"
        "<br><code>r = &sigma;&sup2;_b / ( &sigma;&sup2;_b + &sigma;&sup2;_w )</code>.</li>"
        "</ul><br>"
        "<b>PRACTICAL APPLICATIONS IN LIVESTOCK MANAGEMENT</b><br>"
        "<ol>"
        "<li><b>Early Culling of Low-Producing Females:</b> If a trait has high repeatability (r &ge; 0.50; e.g., milk fat %, fleece weight), an animal's first record is a reliable indicator of its future performance. Farmers can confidently cull poor-producing heifers after their 1st lactation without waiting for expensive 2nd and 3rd records. If r is low (r &le; 0.15; e.g., calving interval), 1st record has minimal predictive power.</li>"
        "<li><b>Most Probable Producing Ability (MPPA):</b>"
        "<br>Estimates an animal's future productive capacity based on 'n' past records: "
        "<br><br>"
        "<code>MPPA = Herd Mean (&mu;) + [ (n &times; r) / (1 + (n - 1)r) ] &times; (Cow's Average X&#772; - &mu;)</code>"
        "<br><br>"
        "The weighting factor <code>[ nr / (1 + (n - 1)r) ]</code> is the repeatability of the average of n records!</li>"
        "<li><b>Gain in Accuracy from Multiple Records:</b> Evaluating multiple records reduces temporary environmental variance (V_Es/n), increasing selection accuracy by: <code>&radic;[ n / (1 + (n - 1)r) ]</code>. When r is high, extra records add minimal accuracy; when r is low, multiple records substantially improve evaluation.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Diminishing Returns of Additional Records in High vs Low Repeatability Traits:</b><br>"
        "Exam numerical questions frequently test the gain in accuracy from obtaining an extra lactation record: "
        "The relative accuracy of 'n' records compared to a single record is <code>&radic;[ n / (1 + (n - 1)r) ]</code>. "
        "<br>&bull; For a high repeatability trait (<code>r = 0.60</code>): 1 record accuracy = 1.0; 2 records = 1.12 (only 12% gain); 4 records = 1.19. Obtaining additional records beyond the 2nd is economically unjustified! "
        "<br>&bull; For a low repeatability trait (<code>r = 0.15</code>): 1 record accuracy = 1.0; 4 records = 1.66 (a massive 66% gain in accuracy!). Here, collecting multiple records is essential before culling."
    ),
    "keyPoints": [
        "Repeatability (r) is the correlation between repeated phenotypic records on the same animal over time.",
        "Mathematical formula: r = (V_G + V_Eg) / V_P = (V_A + V_D + V_I + V_Eg) / V_P.",
        "Repeatability is always greater than or equal to heritability: r ≥ h².",
        "Repeatability sets the theoretical upper limit of narrow-sense heritability.",
        "Estimated via Intra-Class Correlation from one-way ANOVA: r = σ²_b / (σ²_b + σ²_w).",
        "High repeatability traits (r > 0.50): milk fat %, fleece weight, egg weight, mature body weight.",
        "Moderate repeatability traits (r = 0.30–0.50): 305-day milk yield, birth weight.",
        "Low repeatability traits (r < 0.20): service period, calving interval, maternal weaning weight.",
        "High repeatability allows confident early culling of low-producing animals after their first record.",
        "Most Probable Producing Ability: MPPA = μ + [ nr / (1 + (n - 1)r) ] · (X̄ - μ).",
        "The repeatability of the average of n records is: r_n = nr / [ 1 + (n - 1)r ].",
        "Additional records yield diminishing returns in accuracy for high-repeatability traits."
    ],
    "clinical": (
        "In an organized Murrah buffalo farm with a herd average of 2,000 kg milk (r = 0.40), a cow completes 3 lactations averaging 2,600 kg (deviation = +600 kg). Her MPPA is calculated as: MPPA = 2,000 + [ (3 &times; 0.40) / (1 + 2 &times; 0.40) ] &times; 600 = 2,000 + [ 1.2 / 1.8 ] &times; 600 = 2,000 + 400 = 2,400 kg. The farm manager reliably predicts her 4th lactation yield will be 2,400 kg, prioritizing her for elite replacement heifer production."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Heritability (h²) versus Repeatability (r)",
            "headers": ["Diagnostic Criterion", "Narrow-Sense Heritability (h²)", "Repeatability (r)"],
            "rows": [
                ["Mathematical Definition", "h&sup2; = V_A / V_P", "r = (V_A + V_D + V_I + V_Eg) / V_P"],
                ["Biological Scope", "Correlation between breeding value and phenotypic value", "Phenotypic correlation between repeated records on the same animal"],
                ["Requirement of Records", "Requires pedigreed family records across relatives", "Requires multiple records repeated on the same individual animal"],
                ["Numerical Relationship", "Always less than or equal to repeatability: h&sup2; &le; r", "Always greater than or equal to heritability: r &ge; h&sup2;"],
                ["Primary Breeding Function", "Predicts expected genetic gain from selection (&Delta;G = h&sup2;S)", "Predicts future performance (MPPA) and guides early herd culling"],
                ["Applicability to Traits", "Applicable to all traits (single or repeated)", "Applicable strictly to traits that can be measured repeatedly"]
            ]
        }
    ],
    "img": "",
    "tags": ["repeatability", "mppa", "intra-class-correlation", "lactation-records", "early-culling", "most-probable-producing-ability"]
}

topics["u2-t29"] = {
    "summary": "Genetic and phenotypic correlations measure the mutual association between different economic traits, caused biologically by pleiotropy and linkage, governing correlated responses to selection in breeding programs.",
    "desc": (
        "<b>CONCEPT OF CORRELATIONS IN ANIMAL BREEDING</b><br>"
        "Farm animals are not selected for a single trait in isolation; dairy cattle are evaluated for milk yield, fat percentage, udder conformation, and mastitis resistance simultaneously. "
        "Selecting for one trait frequently causes simultaneous, unexpected alterations in another trait. Understanding the mathematical relationships between traits requires partitioning total association into <b>Phenotypic</b>, <b>Genetic</b>, and <b>Environmental</b> correlations.<br><br>"
        "<b>1. PHENOTYPIC CORRELATION (r_P)</b><br>"
        "The directly observable linear association between two distinct metric traits (X and Y) measured on the same individual animals:"
        "<br><br>"
        "<code>r_P = Cov_P(X, Y) / [ &sigma;_PX &times; &sigma;_PY ]</code>"
        "<br><br>"
        "It is the joint outcome of underlying genetic factors and shared environmental conditions.<br><br>"
        "<b>2. GENETIC CORRELATION (r_G OR r_A)</b><br>"
        "The correlation between the <b>Additive Breeding Values</b> of animals for trait X and trait Y:"
        "<br><br>"
        "<code>r_G = Cov_A(X, Y) / [ &sigma;_AX &times; &sigma;_AY ] = Cov_A(X, Y) / &radic;[ V_AX &times; V_AY ]</code>"
        "<br><br>"
        "<b>Biological Causes of Genetic Correlation:</b>"
        "<ul>"
        "<li><b>Pleiotropy (Primary, Permanent Cause):</b> Single genes influencing both traits simultaneously through shared biochemical pathways (e.g., genes increasing milk volume also dilute solids-not-fat, causing a negative genetic correlation between milk yield and fat percentage).</li>"
        "<li><b>Linkage Disequilibrium (Secondary, Transient Cause):</b> Genes controlling trait X and trait Y are physically linked close together on the same chromosome. Crossing over gradually breaks linkage disequilibrium over generations, whereas pleiotropic correlations are permanent.</li>"
        "</ul><br>"
        "<b>3. ENVIRONMENTAL CORRELATION (r_E)</b><br>"
        "The correlation between the environmental deviations (and non-additive genetic deviations) of trait X and trait Y:"
        "<br><br>"
        "<code>r_E = Cov_E(X, Y) / [ &sigma;_EX &times; &sigma;_EY ]</code>"
        "<br><br>"
        "<b>Mathematical Synthesis of the Three Correlations:</b><br>"
        "<code>r_P = ( h_X &times; h_Y &times; r_G ) + ( e_X &times; e_Y &times; r_E )</code>"
        "<br>where <code>h_X = &radic;h&sup2;_X</code>, <code>h_Y = &radic;h&sup2;_Y</code>, <code>e_X = &radic;(1 - h&sup2;_X)</code>, and <code>e_Y = &radic;(1 - h&sup2;_Y)</code>.<br><br>"
        "<b>ESTIMATION OF GENETIC CORRELATION</b><br>"
        "Estimated via Analysis of Variance and Covariance using <b>Paternal Half-Sibs</b>:"
        "<br><br>"
        "<code>r_G = Cov_s(X, Y) / &radic;[ &sigma;&sup2;_s(X) &times; &sigma;&sup2;_s(Y) ]</code>"
        "<br><br>"
        "where <code>Cov_s(X, Y)</code> is the between-sire covariance component, and <code>&sigma;&sup2;_s(X), &sigma;&sup2;_s(Y)</code> are the between-sire variance components for traits X and Y.<br><br>"
        "<b>SIGNIFICANCE IN LIVESTOCK SELECTION</b><br>"
        "<ol>"
        "<li><b>Correlated Response to Selection (CR_Y):</b>"
        "<br>When directional selection is applied to Trait X, the indirect, correlated genetic change observed in Trait Y is: "
        "<br><br>"
        "<code>CR_Y = i_X &times; h_X &times; h_Y &times; r_G &times; &sigma;_PY</code>"
        "<br><br>"
        "where i_X = selection intensity on X, h_X and h_Y are square roots of heritabilities, and &sigma;_PY is the phenotypic standard deviation of Y.</li>"
        "<li><b>Antagonistic (Undesirable) Genetic Correlations:</b>"
        "<br>When two commercially vital traits have a negative genetic correlation:"
        "<br>&bull; <i>Lactation Milk Yield vs Milk Fat Percentage:</i> <code>r_G = -0.25 to -0.35</code> in dairy cattle. Intense selection for high milk volume causes an automatic, correlated decline in butterfat percentage! "
        "<br>&bull; <i>Broiler Growth Rate vs Reproductive Fitness:</i> Fast growth causes ascites, leg weakness, and reduced fertility in broiler breeder hens. "
        "<br>&bull; <i>Egg Production vs Egg Weight:</i> <code>r_G = -0.30</code> in layers (more eggs produce smaller egg size).</li>"
        "<li><b>Indirect Selection:</b> Selecting for a secondary trait (X) to improve primary trait (Y). Highly effective when: (a) Trait Y is difficult, expensive, or late in life to measure (e.g., feed efficiency); (b) Trait Y is sex-limited (e.g., measuring scrotal circumference in bulls to indirectly select for daughter fertility and early puberty); (c) Trait X has much higher heritability than Trait Y.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Relative Efficiency of Indirect Selection (RE):</b><br>"
        "To decide whether indirect selection on Trait X is superior to direct selection on Trait Y, calculate the <b>Relative Efficiency (RE)</b>: "
        "<br><code>RE = CR_Y / R_Y = [ i_X &times; h_X &times; h_Y &times; r_G &times; &sigma;_PY ] / [ i_Y &times; h&sup2;_Y &times; &sigma;_PY ] = (i_X / i_Y) &times; (r_G &times; h_X / h_Y)</code>. "
        "<br>Assuming equal selection intensities (i_X = i_Y): "
        "<br><code>RE = r_G &times; (h_X / h_Y) = r_G &times; &radic;(h&sup2;_X / h&sup2;_Y)</code>. "
        "Indirect selection is more efficient than direct selection (<code>RE &gt; 1.0</code>) ONLY IF: "
        "<br><code>|r_G| &times; h_X &gt; h_Y</code>. "
        "This occurs when the secondary trait has a high genetic correlation with the target trait AND has a substantially higher heritability."
    ),
    "keyPoints": [
        "Phenotypic correlation (r_P) is the observed association between two traits on the same animal.",
        "Genetic correlation (r_G) is the correlation between additive breeding values for two traits.",
        "Pleiotropy is the primary, permanent biological cause of genetic correlation.",
        "Linkage disequilibrium causes transient genetic correlation, broken over generations by crossing over.",
        "Environmental correlation (r_E) arises from shared non-genetic and managerial influences.",
        "Synthesis equation: r_P = h_X · h_Y · r_G + e_X · e_Y · r_E.",
        "Paternal half-sib genetic correlation formula: r_G = Cov_s(XY) / √[ σ²_s(X) · σ²_s(Y) ].",
        "Correlated response to selection formula: CR_Y = i_X · h_X · h_Y · r_G · σ_PY.",
        "Antagonistic genetic correlation exists between Milk Yield and Fat % (r_G ≈ -0.30) in dairy cattle.",
        "Antagonistic genetic correlation exists between Egg Number and Egg Weight (r_G ≈ -0.30) in poultry.",
        "Indirect selection uses a correlated indicator trait to improve a hard-to-measure target trait.",
        "Indirect selection is more efficient than direct selection if |r_G| · h_X > h_Y."
    ],
    "clinical": (
        "In young breeding bull evaluation, measuring scrotal circumference (cm) at 12 months of age exhibits a strong positive genetic correlation (r_G = +0.65) with daughter pregnancy rate and age at first calving. Because female fertility is sex-limited and has low heritability (h² = 0.05), selecting sires indirectly for large scrotal circumference (h² = 0.40) effectively accelerates herd reproductive performance."
    ),
    "tables": [
        {
            "title": "Major Genetic and Phenotypic Correlations Among Economic Traits in Livestock",
            "headers": ["Livestock Species", "Trait Pair (Trait X & Trait Y)", "Genetic Correlation (r_G)", "Phenotypic Correlation (r_P)", "Animal Breeding Implication"],
            "rows": [
                ["Dairy Cattle / Buffalo", "305-day Milk Yield vs Milk Fat %", "-0.25 to -0.35", "-0.20", "Antagonistic; selection for milk volume dilutes fat concentration"],
                ["Dairy Cattle / Buffalo", "305-day Milk Yield vs Protein Yield", "+0.80 to +0.90", "+0.85", "Synergistic; selecting for milk volume simultaneously increases total protein output"],
                ["Dairy Cattle / Buffalo", "Scrotal Circumference vs Age at Puberty", "-0.60 to -0.70", "-0.45", "Beneficial; larger bull testes genetically accelerates daughter sexual maturity"],
                ["Beef Cattle / Steers", "Birth Weight vs Weaning Weight", "+0.55 to +0.65", "+0.50", "Favorable for growth, but increases dystocia (calving difficulty)"],
                ["Sheep", "Body Weight vs Clean Fleece Weight", "+0.30 to +0.40", "+0.35", "Favorable dual-purpose meat and wool genetic correlation"],
                ["Layer Poultry", "Egg Number vs Average Egg Weight", "-0.25 to -0.35", "-0.20", "Antagonistic; high egg counts produce smaller individual egg size"]
            ]
        }
    ],
    "img": "",
    "tags": ["genetic-correlation", "phenotypic-correlation", "pleiotropy", "correlated-response", "indirect-selection", "antagonistic-correlation"]
}
