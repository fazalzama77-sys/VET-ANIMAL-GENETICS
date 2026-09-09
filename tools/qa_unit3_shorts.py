# -*- coding: utf-8 -*-
"""
Unit 3: 8 Five-Mark Short Answer / Difference Questions (u3-q13 to u3-q20)
Animal Breeding Principles, Selection, Mating Systems & Improvement (VCI MSVE 2016 Standard)
"""

questions = [
    {
        "id": "u3-q13",
        "type": "diff",
        "marks": 5,
        "question": "Compare Tandem Selection, Independent Culling Levels, and Selection Index methods for multi-trait selection in livestock.",
        "topicId": "u3-t09",
        "answer": (
            "<b>Comparison of Multi-Trait Selection Methods (Hazel & Lush, 1942):</b><br>"
            "In commercial livestock breeding, animals must be improved simultaneously for several economically important traits "
            "(e.g., milk yield, fat percentage, age at first calving, and mastitis resistance). Three methods are available.<br><br>"
            "<b>Relative Genetic Efficiency (Hazel and Lush):</b><br>"
            "Assuming traits are uncorrelated and equally important, relative efficiency is:<br>"
            "<b>Selection Index (1.00) &gt; Independent Culling Levels (0.70&ndash;0.80) &gt; Tandem Selection (1 / &radic;n)</b>.<br>"
            "When selecting for 4 traits (<code>n = 4</code>), tandem selection is only half as efficient (<code>1/&radic;4 = 0.50</code>) as an index."
        ),
        "keyPoints": [
            "Tandem: Selects one trait at a time; least efficient; genetic regression in unselected traits due to negative correlations.",
            "Independent Culling: Establishes minimum cutoff for each trait; culls animals failing any threshold regardless of excellence in others.",
            "Selection Index: Total net merit score I = Σ b_i X_i; most efficient; compensates weakness in one trait with superiority in another."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Comparison of Multi-Trait Selection Methods",
            "headers": ["Feature", "Tandem Selection", "Independent Culling Levels (ICL)", "Selection Index (Hazel, 1943)"],
            "rows": [
                ["Selection Approach", "Selects for one trait at a time over generations until target is achieved, then switches to next trait", "Establishes independent minimum threshold standards for all traits simultaneously", "Combines all traits into a single aggregate economic score: I = b1*X1 + b2*X2 + ... + bn*Xn"],
                ["Compensation Among Traits", "Zero compensation (only one trait evaluated per phase)", "Zero compensation; exceptional merit in one trait cannot compensate failure in another", "Complete compensation; exceptional merit in one trait balances slight deficiency in another"],
                ["Relative Efficiency", "Least efficient: 1 / √n (where n = number of traits)", "Intermediate efficiency (~70-80% of index efficiency)", "Most efficient mathematically and economically (100% benchmark)"],
                ["Impact of Negative Correlations", "High risk; selecting for milk yield severely deteriorates fat percentage during that phase", "Moderate; may cull too many animals if antagonistic traits are selected together", "Optimal; economic weights and genetic covariances directly account for negative correlations"],
                ["Practical Application", "Rarely used commercially; historical method", "Widely used at culling gates (e.g., culling bulls failing semen motility standards)", "Standard tool in modern dairy, swine, and poultry genetic evaluation (e.g., TPI, NM$)"]
            ]
        },
        "pyq": ["IVRI 2019", "TANUVAS 2021", "KVASU 2022", "GADVASU 2023"]
    },
    {
        "id": "u3-q14",
        "type": "diff",
        "marks": 5,
        "question": "Differentiate between Close Breeding and Linebreeding with animal pedigree examples and breeding goals.",
        "topicId": "u3-t12",
        "answer": (
            "<b>Comparison between Close Breeding and Linebreeding:</b><br>"
            "Both are forms of inbreeding (mating of individuals more closely related than the average of the population), "
            "but they differ sharply in their degree of relationship, intensity of inbreeding, and breeding objectives.<br><br>"
            "<b>Breeding Goals:</b>"
            "<ul>"
            "<li><b>Close Breeding:</b> Used experimentally to rapidly uncover and purge lethal recessive genes, create homozygous inbred lines for heterosis in crossbreeding, and establish laboratory animal lines.</li>"
            "<li><b>Linebreeding:</b> Used commercially by master breeders to concentrate the genetic contribution (high relationship <code>R</code>) of an outstanding, proven ancestral sire or dam across generations while keeping the inbreeding coefficient (<code>F</code>) low and safe.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Close breeding: Matings between first-degree relatives (sire-daughter, brother-sister); F >= 0.25; high risk of inbreeding depression.",
            "Linebreeding: Matings aimed at maintaining high relationship (R) to an admired ancestor while keeping F < 0.10.",
            "Close breeding purges deleterious recessives; Linebreeding preserves prepotency and elite ancestral germplasm."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Differences Between Close Breeding and Linebreeding",
            "headers": ["Feature", "Close Breeding", "Linebreeding"],
            "rows": [
                ["Pedigree Mating Type", "Mating of first-degree relatives: Full brother x Full sister, Sire x Daughter, Dam x Son", "Mating of more distant relatives: Grandson x Granddaughter, Half-sib x Half-sib, Cousin x Cousin directed towards an elite ancestor"],
                ["Inbreeding Coefficient (F)", "Increases very rapidly (F >= 0.25 or 25% in a single generation)", "Maintained at a low, controlled level (typically F < 0.10 or 10%)"],
                ["Relationship to Common Ancestor", "General relationship to multiple recent ancestors", "Concentrates genetic relationship (R >= 0.25 to 0.50) specifically to one outstanding admired ancestor"],
                ["Risk of Inbreeding Depression", "Extremely high risk of juvenile mortality, reduced fertility, and lethal anomalies", "Minimal to mild risk; allows continuous culling of slight abnormalities"],
                ["Primary Breeding Objective", "Purging lethal recessives; generating homozygous parental inbred lines for hybrid vigor", "Conserving elite sire/dam genes; fixing type and prepotency in a registered pedigree herd"],
                ["Suitability for Commercial Farmers", "Strongly discouraged in commercial farm stock", "Recommended for elite pedigree seedstock breeders with rigorous culling"]
            ]
        },
        "pyq": ["TANUVAS 2020", "IVRI 2021", "KVASU 2023"]
    },
    {
        "id": "u3-q15",
        "type": "short",
        "marks": 5,
        "question": "Describe the Genetic and Phenotypic Consequences of Inbreeding Depression in Dairy Livestock. How can it be managed?",
        "topicId": "u3-t11",
        "answer": (
            "<b>Inbreeding Depression in Dairy Livestock:</b><br>"
            "The reduction in phenotypic mean performance, biological fitness, vigor, and fertility resulting from the mating of related individuals.<br><br>"
            "<b>1. Genetic Consequences:</b>"
            "<ul>"
            "<li><b>Increase in Homozygosity:</b> Rate of increase in homozygosity equals <code>F</code>. Alleles become fixed (<code>AA</code> or <code>aa</code>).</li>"
            "<li><b>Uncovering Deleterious Recessive Alleles:</b> Recessive lethal or sub-lethal alleles previously masked in heterozygous state (<code>Aa</code>) are expressed as homozygotes (<code>aa</code>) (e.g., BLAD, CVM, Mule foot, dwarfism).</li>"
            "<li><b>Decline in Heterozygote Advantage:</b> Loss of overdominance at loci where heterozygotes are biologically superior.</li>"
            "</ul>"
            "<b>2. Phenotypic Consequences on Dairy Production and Fitness:</b>"
            "<ul>"
            "<li><b>Milk Production:</b> For every 1% increase in inbreeding (<code>&Delta;F = 0.01</code>), 305-day lactation milk yield declines by <b>15 to 25 kg</b>, and lifetime production declines by over 200 kg.</li>"
            "<li><b>Reproduction & Fertility:</b> Calving interval increases, service period prolongs, age at first calving increases, and embryonic mortality rises significantly.</li>"
            "<li><b>Calf Survivability & Vigor:</b> Birth weight decreases by 0.5 kg per 1% F; pre-weaning calf mortality increases due to suppressed immunocompetence.</li>"
            "</ul>"
            "<b>3. Remedial Management Strategies:</b>"
            "<ul>"
            "<li><b>Outcrossing / Line Crossing:</b> Mating inbred females to unrelated purebred sires completely restores vigor and eliminates inbreeding depression in a single generation.</li>"
            "<li><b>Pedigree Mating Allocation Software:</b> Utilizing computerized mating programs (e.g., minimum kinship mating) to ensure planned matings maintain <code>F &le; 6.25%</code> in commercial herds.</li>"
            "<li><b>Expanding Effective Sire Base:</b> Avoiding over-reliance on a single popular AI sire family.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Definition: Decline in fitness and vigor due to mating related individuals.",
            "Genetic basis: Proportional increase in homozygosity and exposure of deleterious recessives.",
            "Phenotypic losses: 15-25 kg milk loss per 1% F, delayed puberty, poor conception, calf mortality.",
            "Remedies: Outcrossing, computerized mating allocation to cap F < 6.25%, rotating AI sire lines."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["VCI Annual 2019", "GADVASU 2021", "LUVAS 2022", "MAFSU 2023"]
    },
    {
        "id": "u3-q16",
        "type": "diff",
        "marks": 5,
        "question": "Explain the Genetic Theories of Heterosis (Hybrid Vigor): Dominance Hypothesis vs Overdominance Hypothesis.",
        "topicId": "u3-t14",
        "answer": (
            "<b>Theories of Heterosis (Hybrid Vigor):</b><br>"
            "Heterosis is the phenotypic superiority of crossbred F1 progeny over the average of their purebred parental lines. "
            "Two primary genetic hypotheses explain this phenomenon.<br><br>"
            "<b>Reconciliation (Modern Consensus):</b><br>"
            "Extensive quantitative and molecular QTL studies demonstrate that <b>both mechanisms operate simultaneously</b>: "
            "the Dominance mechanism accounts for the major share of heterosis across polygenic production traits through the masking "
            "of thousands of mildly deleterious recessives, while Overdominance operates decisively at specific immune and regulatory loci "
            "(e.g., Major Histocompatibility Complex MHC/BoLA loci conferring enhanced disease resistance in crossbreds)."
        ),
        "keyPoints": [
            "Dominance Hypothesis (Davenport, Bruce, Keeble & Pellew): Superiority due to masking of deleterious recessives by favorable dominant alleles.",
            "Overdominance Hypothesis (East & Shull): Superiority due to physiological heterozygote advantage (Aa > AA or aa).",
            "Dominance predicts heterosis could theoretically be fixed in pure homozygotes; Overdominance states it can never be fixed in homozygotes.",
            "Modern consensus: Both mechanisms contribute, with dominance predominant in yield traits and overdominance prominent in immune/fitness traits."
        ],
        "diagram": "",
        "table": {
            "title": "Comparison Between Dominance and Overdominance Theories of Heterosis",
            "headers": ["Feature", "Dominance Hypothesis (Davenport 1908, Bruce 1910)", "Overdominance Hypothesis (East 1908, Shull 1908)"],
            "rows": [
                ["Basic Premise", "Heterosis results from the masking of unfavorable recessive alleles by favorable dominant alleles at multiple loci (AAbbCCdd x aaBBccDD -> AaBbCcDd)", "Heterosis results from superior intrinsic physiological/biochemical activity of the heterozygous genotype itself (Aa > AA and Aa > aa)"],
                ["Gene Action Involved", "Additive and intra-locus complete/partial dominance (V_A and V_D)", "Intra-locus overdominance / single-gene heterosis"],
                ["Number of Genes Required", "Requires multiple complementary loci with linked dominant alleles", "Can occur at a single heterozygous gene locus"],
                ["Can Heterosis be Fixed in Purebreds?", "Theoretically YES, if an individual homozygous for all dominant alleles (AABBCCDD) could be synthesized (hindered only by linkage)", "Theoretically IMPOSSIBLE; segregation in subsequent generations inevitably breaks up heterozygosity"],
                ["Explanation for F2 Breakdown", "Segregation and recombination separates favorable dominant alleles into different gametes", "Reduction of heterozygosity by 50% in F2 directly halves the overdominant advantage"],
                ["Classic Biological Evidence", "Complementary gene action in polygenic growth and yield traits", "Sickle cell anemia resistance to malaria in humans; MHC/BoLA heterozygote disease resistance in cattle"]
            ]
        },
        "pyq": ["IVRI 2018", "TANUVAS 2020", "GADVASU 2022", "KVASU 2023"]
    },
    {
        "id": "u3-q17",
        "type": "short",
        "marks": 5,
        "question": "Describe the concept and operational 3-year cycle of Reciprocal Recurrent Selection (RRS). Why is it superior to Recurrent Selection?",
        "topicId": "u3-t14",
        "answer": (
            "<b>Reciprocal Recurrent Selection (RRS - Comstock, Robinson & Harvey, 1949):</b><br>"
            "A cyclic breeding system designed to improve two genetically distinct populations (Line A and Line B) simultaneously "
            "based on their crossbred progeny performance (A &times; B), effectively exploiting <b>both General Combining Ability (GCA - additive variance) "
            "and Specific Combining Ability (SCA - non-additive dominance and epistatic variance)</b>.<br><br>"
            "<b>Operational 3-Year Cycle in Poultry / Swine:</b>"
            "<ul>"
            "<li><b>Year 1 (Test Crossing):</b> Sires and dams of Line A are mated to individuals of Line B (A &times; B), and reciprocally sires and dams of Line B are mated to Line A (B &times; A). Simultaneously, purebred lines are reproduced or pure semen/stock preserved.</li>"
            "<li><b>Year 2 (Crossbred Performance Testing):</b> The resulting crossbred progeny (AB and BA) are tested under commercial field conditions for economic traits (e.g., egg number, feed conversion ratio, broiler body weight). Line A and Line B parents are evaluated based on the performance of their crossbred progeny.</li>"
            "<li><b>Year 3 (Purebred Multiplication of Selected Elite):</b> High-performing parents (or their purebred progeny) from Line A are inter-se mated to reproduce pure Line A. Similarly, elite Line B individuals are mated to reproduce pure Line B. The cycle then repeats.</li>"
            "</ul>"
            "<b>Superiority over Simple Recurrent Selection:</b><br>"
            "In simple recurrent selection, a single tester is used (only one line is improved). In RRS, <b>each population acts as the tester for the other</b>, "
            "ensuring mutual, reciprocal genetic divergence and maximizing commercial crossbred heterosis in every subsequent cycle."
        ),
        "keyPoints": [
            "Concept: Simultaneous improvement of two distinct lines based on crossbred performance.",
            "Exploits both GCA (additive) and SCA (non-additive dominance/epistasis).",
            "3-year cycle: Year 1 test-cross (A x B and B x A); Year 2 evaluate crossbred progeny; Year 3 inter-se mate best purebred parents within each line.",
            "Superior to recurrent selection because both lines improve reciprocally and become increasingly complementary."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["TANUVAS 2019", "IVRI 2021", "KVAFSU 2023"]
    },
    {
        "id": "u3-q18",
        "type": "diff",
        "marks": 5,
        "question": "Compare Contemporary Comparison (Daughter-Dam Comparison) and Animal Model BLUP for sire evaluation in dairy cattle.",
        "topicId": "u3-t06",
        "answer": (
            "<b>Comparison of Sire Evaluation Methods:</b><br>"
            "Evaluating the genetic merit of dairy bulls is the cornerstone of dairy genetic improvement. Over the past century, "
            "methodology has evolved from phenotypic daughter comparisons to advanced statistical linear models.<br><br>"
            "<b>Why Animal Model BLUP is Superior:</b>"
            "<ul>"
            "<li>Uses the <b>numerator relationship matrix (A-matrix)</b> incorporating all pedigree relatives (parents, sibs, progeny) simultaneously.</li>"
            "<li>Simultaneously evaluates cows and bulls on the exact same scale, eliminating dam merit bias and preferential mating.</li>"
            "<li>Accounts for non-random herd-year-season (HYS) contemporary group effects and adjusts for genetic trends across generations.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Contemporary Comparison: Compares daughters against herdmates; ignores non-random mating and genetic merit of dams.",
            "BLUP (Best Linear Unbiased Prediction - C.R. Henderson): Matrix-based mixed model (y = Xb + Zu + e); incorporates numerator relationship matrix (A).",
            "BLUP accounts for fixed environmental effects (HYS), genetic trend, and unequal mating merit of dams."
        ],
        "diagram": "",
        "table": {
            "title": "Comparison Between Contemporary Comparison and Animal Model BLUP",
            "headers": ["Feature", "Contemporary Comparison (Herdmate Comparison)", "Animal Model BLUP (Henderson, 1973)"],
            "rows": [
                ["Statistical Model", "Simple phenotypic difference: Daughter Mean - Herdmate Contemporary Mean", "Mixed Linear Model: y = Xb + Zu + e (b = fixed effects, u = random breeding values)"],
                ["Pedigree Information", "Uses only daughter records; ignores all collateral relatives and ancestry", "Incorporate complete pedigree information via Numerator Relationship Matrix (A^-1)"],
                ["Dam Genetic Merit", "Assumes all dams are of average genetic merit; biased by preferential mating", "Directly accounts for dam merit; completely unbiased by preferential mating of elite cows to top bulls"],
                ["Environmental Adjustment", "Corrects roughly for herd average, but sensitive to small contemporary group size", "Simultaneously estimates fixed herd-year-season (HYS) effects and random genetic effects"],
                ["Genetic Trend Handling", "Cannot adjust for genetic progress over time; older sires unfairly compared to younger sires", "Completely adjusts for genetic trends, allowing fair comparison across generations"],
                ["Current Status", "Obsolete; used historically prior to 1980s", "Global gold standard for national dairy cattle genetic evaluations worldwide"]
            ]
        },
        "pyq": ["IVRI 2020", "GADVASU 2021", "KVASU 2022", "LUVAS 2023"]
    },
    {
        "id": "u3-q19",
        "type": "short",
        "marks": 5,
        "question": "Describe the hormonal protocol and operational steps of Multiple Ovulation and Embryo Transfer (MOET) in cattle.",
        "topicId": "u3-t26",
        "answer": (
            "<b>Multiple Ovulation and Embryo Transfer (MOET):</b><br>"
            "A reproductive biotechnology whereby a genetically superior donor cow is superovulated with exogenous gonadotropins, "
            "inseminated with elite sire semen, and the resulting viable blastocysts are non-surgically recovered (flushed) and transferred "
            "to synchronized recipient surrogate mothers.<br><br>"
            "<b>Step-by-Step Bovine Protocol:</b>"
            "<ol>"
            "<li><b>Selection of Donor and Recipient Females:</b> Donor: Top 1&ndash;5% genetic merit, regular estrous cycles, free from reproductive disease. Recipients: Healthy, cycling, fertile cows/heifers.</li>"
            "<li><b>Superovulation of Donor:</b> On Day 9&ndash;11 of the estrous cycle (mid-luteal phase), administer <b>porcine Pituitary FSH (pFSH, total dose 200&ndash;400 mg)</b> in 8 declining doses given intramuscularly twice daily over 4 consecutive days (e.g., 50/50, 40/40, 30/30, 20/20 mg).</li>"
            "<li><b>Luteolysis (PGF2&alpha;):</b> Concurrently with the 5th or 6th injection of FSH (on Day 3 of protocol), inject a luteolytic dose of <b>PGF2&alpha; (e.g., Cloprostenol 500 &mu;g)</b> to induce rapid luteolysis of the corpus luteum and induce estrus within 40&ndash;48 hours.</li>"
            "<li><b>Insemination:</b> Inseminate donor at 12, 24, and 36 hours after standing heat onset using high-quality semen (often 2 doses per insemination) to ensure fertilization of all ovulated ova.</li>"
            "<li><b>Non-Surgical Embryo Flushing (Day 7):</b> Exactly <b>Day 7 post-estrus</b> (when embryos are in morula or early blastocyst stage residing in the uterine horns), introduce a sterile two-way or three-way Foley catheter into the uterine horn. Inflate balloon (10&ndash;15 mL) to seal cervix. Infuse Dulbecco's Phosphate Buffered Saline (DPBS) supplemented with 1% BSA or fetal calf serum, flushing 500&ndash;1000 mL per horn into an embryo filter.</li>"
            "<li><b>Embryo Evaluation & Transfer:</b> Screen filter under stereomicroscope. Grade embryos according to IETS standards (Code 1 Excellent/Good, Code 2 Fair, Code 3 Poor, Code 4 Degenerate). Transfer Stage 4&ndash;6 embryos into the ipsilateral uterine horn of recipient cows synchronized to within &plusmn;24 hours of donor estrus, or cryopreserve in 1.5 M ethylene glycol in liquid nitrogen (-196&deg;C).</li>"
            "</ol>"
        ),
        "keyPoints": [
            "Definition of MOET as superovulation, AI, flushing, and transfer to recipients.",
            "pFSH protocol: 8 declining doses twice daily starting Day 9-11 of cycle.",
            "Luteolysis on Day 3 of protocol using PGF2α (cloprostenol).",
            "Day 7 non-surgical flushing with Foley catheter using DPBS.",
            "IETS embryo grading and transfer to synchronized recipients (±24h estrus match) or cryopreservation."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["VCI Annual 2019", "IVRI 2021", "TANUVAS 2022", "KVASU 2023"]
    },
    {
        "id": "u3-q20",
        "type": "diff",
        "marks": 5,
        "question": "Differentiate between In-situ and Ex-situ conservation of Animal Genetic Resources (AnGR) with Indian livestock examples.",
        "topicId": "u3-t24",
        "answer": (
            "<b>Conservation of Animal Genetic Resources (AnGR):</b><br>"
            "India possesses immense indigenous animal genetic diversity (212 registered indigenous breeds recognized by ICAR-NBAGR). "
            "To prevent the extinction of threatened native germplasm (e.g., Punganur, Red Sindhi, Toda, Nilgiri), two conservation strategies are implemented.<br><br>"
            "<b>FAO Recommendation for AnGR:</b><br>"
            "In-situ and Ex-situ conservation should be implemented in an integrated, complementary manner: In-situ maintains the living, "
            "evolving population in pastoral communities, while Ex-situ (Cryoconservation in the National Gene Bank at NBAGR Karnal) provides "
            "a permanent safety backup against catastrophic disease outbreaks or climatic disasters."
        ),
        "keyPoints": [
            "In-situ: Conservation within natural ecological habitat where animals evolved (live breeding herds in farmers' fields).",
            "Ex-situ in vivo: Maintaining live animals outside native tract (state farms, universities, zoos).",
            "Ex-situ in vitro: Cryopreservation of germplasm (semen, embryos, somatic cells, DNA) at -196°C in gene banks (NBAGR Karnal).",
            "Dynamic evolutionary adaptation (in-situ) vs frozen static insurance (ex-situ)."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Differences Between In-situ and Ex-situ Conservation of AnGR",
            "headers": ["Feature", "In-situ Conservation", "Ex-situ Conservation (In vivo & In vitro)"],
            "rows": [
                ["Definition & Location", "Maintenance of live populations in their natural production environments where they evolved and adapted", "Maintenance of live animals outside native tract (in vivo) OR cryopreserved germplasm at -196°C (in vitro)"],
                ["Dynamic Adaptation & Evolution", "Continuous evolutionary adaptation to changing climatic pathogens and local forage resources", "Evolution is halted (in vitro cryopreservation freezes genetic change at sampling point)"],
                ["Operational Cost", "Relatively low public capital cost; supported by livestock owners who generate livelihood from animals", "High initial capital and maintenance costs for liquid nitrogen infrastructure, cryo-tanks, and state livestock farms"],
                ["Utilization & Livelihoods", "Provides active economic products (milk, draught, meat, dung) and cultural value to rural pastoral communities", "Animals or germplasm remain largely non-productive storage backups until reconstituted"],
                ["Risk of Disease / Disasters", "Vulnerable to local epidemics (FMD, Anthrax, Lumpy Skin Disease), droughts, and civil strife", "Secure from local environmental disasters; housed in biosecure repositories"],
                ["Indian Examples", "Community breeding tracts of Toda buffaloes in Nilgiris; Kangayam cattle in Tamil Nadu pastoral systems", "National Gene Bank at ICAR-NBAGR Karnal (cryopreserved semen doses of 50+ indigenous breeds); institutional nucleus herds"]
            ]
        },
        "pyq": ["TANUVAS 2020", "IVRI 2021", "GADVASU 2022", "DUVASU 2023"]
    }
]
