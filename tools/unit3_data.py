# tools/unit3_data.py
# Unit 3: Principles of Animal Breeding
# 180 questions: 90 MCQs, 45 True/False, 45 Fill in the Blanks
# Exactly 18 MCQs, 9 T/F, 9 FIB per sub-section across u3-s1 to u3-s5

unit3_mcq = [
    # ============================================================
    # u3-s1: Economic Traits & Selection Methods (18 MCQs)
    # ============================================================
    {
        "q": "Who is universally recognized as the 'Father of Animal Breeding' for pioneering progeny testing, sire letting, and linebreeding?",
        "o": ["Robert Bakewell", "Jay L. Lush", "Gregor Mendel", "Charles Darwin"],
        "a": 0,
        "e": "Robert Bakewell (1725–1795) of Dishley, England, pioneered systematic animal breeding, sire leasing, and progeny testing.",
        "topicId": "u3-t01",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Who is celebrated as the 'Father of Modern Animal Breeding' for writing the landmark book 'Animal Breeding Plans' (1937)?",
        "o": ["Robert Bakewell", "Jay L. Lush", "C. R. Henderson", "Sewall Wright"],
        "a": 1,
        "e": "Jay L. Lush formalised the application of quantitative biometrical genetics, heritability, and selection index to livestock improvement.",
        "topicId": "u3-t01",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Which livestock breed was developed by Robert Bakewell using systematic inbreeding and progeny selection?",
        "o": ["Dishley Leicester sheep", "Shorthorn cattle", "Holstein-Friesian", "Jersey cattle"],
        "a": 0,
        "e": "Robert Bakewell created the Dishley Leicester sheep, Shire horse, and Dishley Longhorn cattle.",
        "topicId": "u3-t01",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "In dairy cattle, the standard duration of lactation milk yield standardized for official genetic evaluation is:",
        "o": ["180 days", "240 days", "305 days", "365 days"],
        "a": 2,
        "e": "Official dairy records standardise milk production to a 305-day lactation period to enable fair genetic comparisons across parities.",
        "topicId": "u3-t03",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "The period intervening between calving and the subsequent fertile conception in a dairy cow is termed the:",
        "o": ["Dry period", "Service period", "Gestation period", "Inter-calving period"],
        "a": 1,
        "e": "The service period is the interval from parturition to successful conception (ideally 60–90 days for a 12–13 month calving interval).",
        "topicId": "u3-t03",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Which economic trait in commercial broiler poultry is measured as the ratio of total feed consumed to body weight gain?",
        "o": ["Average Daily Gain (ADG)", "Feed Conversion Ratio (FCR)", "Protein Efficiency Ratio (PER)", "Dressing percentage"],
        "a": 1,
        "e": "Feed Conversion Ratio (FCR = kg Feed / kg Gain) measures feed efficiency; lower FCR indicates superior feed conversion.",
        "topicId": "u3-t03",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "The difference between the mean phenotypic value of selected breeding parents and the mean of the entire parental herd is the:",
        "o": ["Genetic gain", "Selection differential (S)", "Selection intensity (i)", "Heritability"],
        "a": 1,
        "e": "Selection differential (S = P_selected - P_pop) measures the superiority of selected parents over the unselected herd average.",
        "topicId": "u3-t04",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Selection intensity (i) is defined mathematically as the selection differential (S) divided by the:",
        "o": ["Population mean", "Phenotypic standard deviation (σ_P)", "Additive genetic variance", "Generation interval"],
        "a": 1,
        "e": "Selection intensity i = S / σ_P. It standardises the selection differential in units of standard deviation.",
        "topicId": "u3-t04",
        "subSection": "u3-s1",
        "diff": 2
    },
    {
        "q": "The average age of parents when their offspring are born is termed the:",
        "o": ["Life expectancy", "Productive life", "Generation interval (L)", "Calving interval"],
        "a": 2,
        "e": "Generation interval (L) is the average age of parents at the birth of their replacement offspring (e.g. 5–6 years in dairy cattle).",
        "topicId": "u3-t04",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "In the fundamental equation for annual genetic gain, ΔG = (i * r_TI * σ_A) / L, what does r_TI represent?",
        "o": ["Repeatability", "Accuracy of selection", "Inbreeding coefficient", "Relationship coefficient"],
        "a": 1,
        "e": "r_TI is the accuracy of selection, defined as the correlation between the true breeding value (T) and the selection criterion (I).",
        "topicId": "u3-t04",
        "subSection": "u3-s1",
        "diff": 2
    },
    {
        "q": "Individual (Mass) selection is most effective and accurate for traits that have:",
        "o": ["Low heritability and sex-limited expression", "High heritability and expression in both sexes", "Zero heritability", "Strong negative dominance"],
        "a": 1,
        "e": "Individual mass selection (r_TI = sqrt(h²)) works best when heritability is high and the trait can be measured directly on both sexes early in life.",
        "topicId": "u3-t05",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "For sex-limited traits like milk production in dairy bulls, which selection basis provides the most accurate estimate of breeding value?",
        "o": ["Individual mass selection", "Progeny testing", "Tandem selection", "Independent culling"],
        "a": 1,
        "e": "Progeny testing evaluates a sire based on the performance of a large group of daughters, providing high accuracy for sex-limited traits.",
        "topicId": "u3-t05",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "What is the primary operational disadvantage of progeny testing in dairy cattle breeding?",
        "o": ["Low accuracy of sire proofs", "Substantially increases generation interval and breeding costs", "Decreases inbreeding", "Prevents artificial insemination"],
        "a": 1,
        "e": "Waiting for daughters to be born, reach sexual maturity, conceive, and complete 305-day lactations delays sire proof until the bull is 5–6 years old.",
        "topicId": "u3-t05",
        "subSection": "u3-s1",
        "diff": 2
    },
    {
        "q": "Which basis of selection is indispensable for traits that require slaughtering the animal, such as meat quality or carcass traits?",
        "o": ["Pedigree selection", "Sib selection (or progeny testing)", "Mass selection", "Tandem selection"],
        "a": 1,
        "e": "Because carcass evaluation is destructive, breeding candidates are selected based on the slaughtered carcass records of their full-sibs or half-sibs.",
        "topicId": "u3-t05",
        "subSection": "u3-s1",
        "diff": 2
    },
    {
        "q": "Selecting for a secondary trait (X) in order to achieve genetic improvement in a primary trait (Y) is called:",
        "o": ["Tandem selection", "Indirect selection", "Mass selection", "Family selection"],
        "a": 1,
        "e": "Indirect selection exploits the genetic correlation between an easily measured secondary trait X and an expensive/difficult primary trait Y.",
        "topicId": "u3-t06",
        "subSection": "u3-s1",
        "diff": 2
    },
    {
        "q": "Which multi-trait selection method selects for one trait at a time until reaching the target, and is mathematically the least efficient?",
        "o": ["Independent Culling Levels", "Selection Index", "Tandem Selection", "BLUP selection"],
        "a": 2,
        "e": "Tandem selection improves one trait at a time, but genetic progress in the first trait is often eroded while selecting for subsequent negatively correlated traits.",
        "topicId": "u3-t07",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "In which multi-trait selection method are animals culled if they fail to meet a minimum threshold in any single trait, regardless of superiority in others?",
        "o": ["Tandem selection", "Selection Index", "Independent Culling Levels (ICL)", "Mass selection"],
        "a": 2,
        "e": "Independent Culling Levels establishes minimum cutoff standards for each trait; failure in any one trait results in automatic culling.",
        "topicId": "u3-t07",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Who formulated the mathematical theory of the Selection Index in animal breeding in 1943?",
        "o": ["L. N. Hazel", "Robert Bakewell", "Francis Galton", "C. R. Henderson"],
        "a": 0,
        "e": "L. N. Hazel (1943) developed the Selection Index method, which Hazel and Lush proved is mathematically the most efficient selection method.",
        "topicId": "u3-t07",
        "subSection": "u3-s1",
        "diff": 2
    },

    # ============================================================
    # u3-s2: Mating Systems, Inbreeding & Heterosis (18 MCQs)
    # ============================================================
    {
        "q": "The mating of animals that are more closely related to each other than the average of the population is termed:",
        "o": ["Outcrossing", "Crossbreeding", "Inbreeding", "Grading up"],
        "a": 2,
        "e": "Inbreeding is the mating of related individuals (e.g. parent-offspring, full-sibs) sharing common ancestors.",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "Who developed the formula for calculating the Inbreeding Coefficient (F) and the path analysis method in 1921?",
        "o": ["Gregor Mendel", "Sewall Wright", "Jay L. Lush", "R. A. Fisher"],
        "a": 1,
        "e": "Sewall Wright (1921) formulated the Inbreeding Coefficient (F) measuring the probability of alleles being identical by descent (IBD).",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "What is the inbreeding coefficient (F) resulting from one generation of full-sib mating (brother × sister) with non-inbred parents?",
        "o": ["0.125 (12.5%)", "0.25 (25%)", "0.50 (50%)", "0.0625 (6.25%)"],
        "a": 1,
        "e": "Full-sib mating produces F = 0.25 (25% inbreeding) in the offspring. Parent-offspring mating also yields F = 0.25.",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "What is the inbreeding coefficient (F) of offspring produced by mating half-sibs (half-brother × half-sister)?",
        "o": ["0.25", "0.125 (12.5%)", "0.0625", "0.50"],
        "a": 1,
        "e": "Half-sibs share one common parent; offspring from half-sib mating have F = (1/2)³ = 0.125 (12.5%).",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 2
    },
    {
        "q": "What is the coefficient of relationship (R_XY) between a non-inbred parent and its offspring?",
        "o": ["1.0 (100%)", "0.50 (50%)", "0.25 (25%)", "0.125 (12.5%)"],
        "a": 1,
        "e": "A parent transmits exactly 50% of its genes to each offspring; hence the coefficient of relationship R = 0.50.",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "A mild, directed form of inbreeding designed to concentrate the inheritance of an outstanding ancestor (e.g. grandsire) is termed:",
        "o": ["Close inbreeding", "Linebreeding", "Outcrossing", "Topcrossing"],
        "a": 1,
        "e": "Linebreeding is deliberate mild inbreeding (F usually 0.05–0.12) designed to keep high genetic relationship to a celebrated ancestor while avoiding close inbreeding.",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "What is the primary genetic consequence of continuous inbreeding in a closed livestock population?",
        "o": ["Increases heterozygosity", "Increases homozygosity and prepotency", "Eliminates all mutations", "Increases genetic variation"],
        "a": 1,
        "e": "Inbreeding brings identical-by-descent alleles together, increasing homozygosity across loci and increasing prepotency (the ability to transmit uniform traits).",
        "topicId": "u3-t10",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "The reduction in vigor, fertility, and survival traits that accompanies increased inbreeding is termed:",
        "o": ["Genetic drift", "Inbreeding depression", "Heterosis", "Atavism"],
        "a": 1,
        "e": "Inbreeding depression is the decline in fitness-related metric traits (reproductive rate, viability, milk yield) resulting from increased homozygosity of deleterious recessives.",
        "topicId": "u3-t10",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "Which class of economic traits suffers the greatest degree of inbreeding depression?",
        "o": ["Carcass quality traits", "Skeletal conformation", "Reproduction and early survival traits", "Mature body size"],
        "a": 2,
        "e": "Traits closely linked to biological fitness (fertility, embryo survival, neonatal viability) have low heritability and suffer the most severe inbreeding depression.",
        "topicId": "u3-t10",
        "subSection": "u3-s2",
        "diff": 2
    },
    {
        "q": "Mating unrelated animals within the very same pure breed (no common ancestor in the last 4–6 generations) is called:",
        "o": ["Outcrossing", "Crossbreeding", "Species hybridization", "Linebreeding"],
        "a": 0,
        "e": "Outcrossing is the mating of unrelated individuals of the same pure breed, introducing fresh vigor without altering breed purity.",
        "topicId": "u3-t11",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "The continuous backcrossing of non-descript (scrub) females to purebred elite sires of a defined breed for several generations is:",
        "o": ["Crossbreeding", "Grading up", "Outcrossing", "Rotational breeding"],
        "a": 1,
        "e": "Grading up continuously uses purebred bulls on grade/native females, reaching 99.2% purebred inheritance by the 7th generation.",
        "topicId": "u3-t11",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "In grading up, what is the proportion of purebred inheritance in the third (F₃) generation offspring?",
        "o": ["50% (1/2)", "75% (3/4)", "87.5% (7/8)", "93.75% (15/16)"],
        "a": 2,
        "e": "F1 = 50% (1/2); F2 = 75% (3/4); F3 = 87.5% (7/8); F4 = 93.75% (15/16); F5 = 96.88% (31/32).",
        "topicId": "u3-t11",
        "subSection": "u3-s2",
        "diff": 2
    },
    {
        "q": "A mule is a sterile interspecific hybrid produced by crossing a:",
        "o": ["Male donkey (Jack) with a female horse (Mare)", "Male horse (Stallion) with a female donkey (Jennet)", "Bull with a female yak", "Ram with a female goat"],
        "a": 0,
        "e": "Mule = Jack (male donkey) × Mare (female horse). The reciprocal cross, Stallion (male horse) × Jennet (female donkey), produces a Hinny.",
        "topicId": "u3-t11",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "What is the diploid chromosome number (2n) of a mule?",
        "o": ["60", "62", "63", "64"],
        "a": 2,
        "e": "Horse provides n = 32 and Donkey provides n = 31, producing a hybrid mule with 2n = 63 chromosomes that cannot pair during meiotic meiosis, causing sterility.",
        "topicId": "u3-t11",
        "subSection": "u3-s2",
        "diff": 2
    },
    {
        "q": "The phenomenon where crossbred offspring excel the average performance of their purebred parental breeds is called:",
        "o": ["Inbreeding depression", "Heterosis (Hybrid Vigour)", "Prepotency", "Epistasis"],
        "a": 1,
        "e": "Heterosis (hybrid vigor) is the phenotypic superiority of F1 crossbreds over the average of the parental breeds.",
        "topicId": "u3-t12",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "Which genetic hypothesis explains heterosis by postulating that the heterozygous genotype (Aa) is superior to both homozygotes (AA and aa)?",
        "o": ["Dominance hypothesis", "Overdominance hypothesis", "Epistasis hypothesis", "Complementary hypothesis"],
        "a": 1,
        "e": "The overdominance hypothesis (Shull and East, 1908) asserts that heterozygotes possess physiological superiority over both parental homozygotes.",
        "topicId": "u3-t12",
        "subSection": "u3-s2",
        "diff": 2
    },
    {
        "q": "General Combining Ability (GCA) is primarily a function of which type of gene action?",
        "o": ["Additive genetic variance (V_A)", "Dominance variance (V_D)", "Epistatic variance (V_I)", "Environmental variance"],
        "a": 0,
        "e": "GCA reflects the average performance of a line in hybrid combinations and is predominantly governed by additive gene action (V_A).",
        "topicId": "u3-t13",
        "subSection": "u3-s2",
        "diff": 2
    },
    {
        "q": "Which breeding scheme developed by Comstock, Robinson, and Harvey simultaneously selects for both General and Specific Combining Ability?",
        "o": ["Tandem selection", "Reciprocal Recurrent Selection (RRS)", "Pedigree selection", "Grading up"],
        "a": 1,
        "e": "RRS uses two genetically diverse populations that serve as mutual testers for each other, maximizing both additive and non-additive gene effects.",
        "topicId": "u3-t13",
        "subSection": "u3-s2",
        "diff": 2
    },

    # ============================================================
    # u3-s3: Livestock & Poultry Breeding Strategies (18 MCQs)
    # ============================================================
    {
        "q": "Which celebrated indigenous dairy cattle breed of India originated in the Montgomery district (now in Pakistan) and is renowned for docility and heat tolerance?",
        "o": ["Sahiwal", "Gir", "Red Sindhi", "Tharparkar"],
        "a": 0,
        "e": "Sahiwal is the premier indigenous dairy breed of India/Pakistan, with high milk yields and extensive use in tropical crossbreeding.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Which indigenous dairy cattle breed of Gujarat has a convex forehead, pendulous long ears, and lyre-shaped horns?",
        "o": ["Kankrej", "Gir", "Dangi", "Deoni"],
        "a": 1,
        "e": "Gir cattle from Saurashtra (Gujarat) are known for their prominent dome-like forehead and pendulous leaf-like curled ears.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Under Indian national breeding policy, what is the recommended optimal level of exotic inheritance in crossbred dairy cattle?",
        "o": ["25% to 35%", "50% to 62.5% (or 5/8)", "75% to 87.5%", "100% purebred"],
        "a": 1,
        "e": "National breeding policy caps exotic inheritance at 50% to 62.5% to combine high milk yield with tropical disease resistance and heat tolerance.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The synthetic dairy cattle strain 'Karan Swiss' developed at NDRI, Karnal, was synthesized by crossing Brown Swiss with:",
        "o": ["Sahiwal and Red Sindhi", "Tharparkar", "Gir", "Hariana"],
        "a": 0,
        "e": "Karan Swiss was synthesized at NDRI Karnal by crossing exotic Brown Swiss sires with indigenous Sahiwal and Red Sindhi cows.",
        "topicId": "u3-t19",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The synthetic dairy cattle strain 'Karan Fries' developed at NDRI, Karnal, is a cross between:",
        "o": ["Holstein-Friesian and Tharparkar", "Jersey and Sahiwal", "Brown Swiss and Gir", "Holstein-Friesian and Red Sindhi"],
        "a": 0,
        "e": "Karan Fries was evolved at NDRI Karnal by crossing Holstein-Friesian sires with indigenous Tharparkar cows.",
        "topicId": "u3-t19",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The synthetic dairy cattle breed 'Frieswal' developed by ICAR-CIRC Meerut carries what proportion of Holstein-Friesian inheritance?",
        "o": ["50%", "62.5% (5/8)", "75%", "87.5%"],
        "a": 1,
        "e": "Frieswal carries 62.5% (5/8) Holstein-Friesian and 37.5% (3/8) Sahiwal inheritance.",
        "topicId": "u3-t19",
        "subSection": "u3-s3",
        "diff": 2
    },
    {
        "q": "The premier riverine dairy buffalo breed of India, renowned as the 'Black Gold' of Haryana, is the:",
        "o": ["Jaffarabadi", "Murrah", "Surti", "Bhadawari"],
        "a": 1,
        "e": "Murrah buffaloes from Haryana are the world's premier dairy buffaloes, characterized by tightly curled jet-black horns and high milk yield.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Which buffalo breed is famous for producing the highest milk fat percentage (up to 12–14%) with a copper-colored coat?",
        "o": ["Murrah", "Mehsana", "Bhadawari", "Nili-Ravi"],
        "a": 2,
        "e": "Bhadawari buffaloes (from Uttar Pradesh/Madhya Pradesh) have a distinctive copper-colored coat and produce milk with 8–13% fat content.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Which indigenous sheep breed of Rajasthan is famous for producing the finest carpet wool and is known as the 'Merino of Rajasthan'?",
        "o": ["Magra", "Nali", "Chokla", "Marwari"],
        "a": 2,
        "e": "Chokla sheep (Shekhawati tract) produce the finest carpet wool in India, earning the title 'Merino of Rajasthan'.",
        "topicId": "u3-t15",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The fine-wool crossbred sheep breed 'Hissardale' was synthesized at Hisar by crossing Australian Merino rams with:",
        "o": ["Bikaneri (Magra) ewes", "Nellore ewes", "Deccani ewes", "Mandya ewes"],
        "a": 0,
        "e": "Hissardale was developed at the Government Livestock Farm, Hisar, by mating Australian Merino rams with Bikaneri ewes.",
        "topicId": "u3-t19",
        "subSection": "u3-s3",
        "diff": 2
    },
    {
        "q": "Which prolific Indian goat breed of West Bengal is celebrated for high twinning rates, early sexual maturity, and tender chevon?",
        "o": ["Jamunapari", "Beetal", "Black Bengal", "Barbari"],
        "a": 2,
        "e": "Black Bengal goats are renowned for multiple births (twins/triplets), excellent skin/leather quality, and superior meat tenderness.",
        "topicId": "u3-t15",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The world-famous luxury cashmere (Pashmina) fiber is harvested from the undercoat of which goat breed found in Ladakh?",
        "o": ["Changthangi (Cheghu)", "Gaddi", "Sirohi", "Osmanabadi"],
        "a": 0,
        "e": "Changthangi and Cheghu goats living at high altitudes in Ladakh/Himalayas produce ultra-fine Pashmina cashmere fiber (<15 microns).",
        "topicId": "u3-t15",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "In commercial poultry broiler breeding, the sire line is typically developed from which heavy, muscular meat breed?",
        "o": ["White Leghorn", "White Cornish", "Rhode Island Red", "Australorp"],
        "a": 1,
        "e": "White Cornish provides broad breast conformation, fast muscle growth, and heavy muscling for broiler sire lines.",
        "topicId": "u3-t16",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "In commercial poultry egg layer breeding, the most widely utilized breed for white-shelled egg production is:",
        "o": ["Single Comb White Leghorn", "Plymouth Rock", "New Hampshire", "Aseel"],
        "a": 0,
        "e": "Single Comb White Leghorn (SCWL) is the foundation of all modern high-producing white-egg layer strains worldwide.",
        "topicId": "u3-t16",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Who developed the Best Linear Unbiased Prediction (BLUP) methodology and Mixed Model Equations in 1973?",
        "o": ["Charles Roy Henderson", "Jay L. Lush", "Sewall Wright", "Robert Bakewell"],
        "a": 0,
        "e": "C. R. Henderson developed BLUP, which is the international gold standard algorithm for modern sire evaluation and genetic prediction.",
        "topicId": "u3-t17",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "What is the key advantage of an Open Nucleus Breeding System (ONBS) over a Closed Nucleus Breeding System?",
        "o": ["Allows genetically superior females from commercial herds to enter the nucleus", "Completely stops all gene flow", "Eliminates all AI costs", "Requires no record keeping"],
        "a": 0,
        "e": "In ONBS, elite females from commercial/farmer herds are allowed into the nucleus, broadening the gene pool and lowering the rate of inbreeding.",
        "topicId": "u3-t18",
        "subSection": "u3-s3",
        "diff": 2
    },
    {
        "q": "The dual-purpose backyard poultry variety 'Vanaraja' was developed by which ICAR institute?",
        "o": ["ICAR-CARI, Izatnagar", "ICAR-DPR, Hyderabad", "ICAR-NDRI, Karnal", "ICAR-IVRI, Bareilly"],
        "a": 1,
        "e": "Vanaraja was developed by the Directorate of Poultry Research (ICAR-DPR), Hyderabad, for rural and backyard free-range farming.",
        "topicId": "u3-t19",
        "subSection": "u3-s3",
        "diff": 2
    },
    {
        "q": "In sire evaluation, Contemporary Comparison compares the performance of a bull's daughters against:",
        "o": ["Their own dams", "Contemporary herdmates born in the same herd, year, and season", "The national breed average", "Full-sibs only"],
        "a": 1,
        "e": "Contemporary comparison adjusts for herd environmental differences by comparing daughters directly against contemporary herdmates in the same season.",
        "topicId": "u3-t17",
        "subSection": "u3-s3",
        "diff": 2
    },

    # ============================================================
    # u3-s4: Breeding Policies & Genetic Conservation (18 MCQs)
    # ============================================================
    {
        "q": "Which ICAR nodal bureau in Karnal is responsible for the identification, characterization, and registration of new livestock and poultry breeds in India?",
        "o": ["ICAR-NBAGR, Karnal", "ICAR-NDRI, Karnal", "ICAR-IVRI, Bareilly", "ICAR-CIRC, Meerut"],
        "a": 0,
        "e": "The National Bureau of Animal Genetic Resources (NBAGR), Karnal, is the official nodal agency for cataloguing and registering indigenous livestock breeds.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "The conservation of endangered livestock populations within their natural agricultural habitat by local farmers is termed:",
        "o": ["In-situ conservation", "Ex-situ in-vitro conservation", "Cryoconservation", "Ex-situ in-vivo conservation"],
        "a": 0,
        "e": "In-situ conservation maintains livestock populations in their original dynamic ecosystems where they continue to adapt to local conditions.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "At what ultra-low temperature is animal germplasm (semen, embryos, oocytes) cryopreserved in liquid nitrogen in National Gene Banks?",
        "o": ["-20°C", "-79°C", "-196°C", "-273°C"],
        "a": 2,
        "e": "Liquid nitrogen operates at -196°C, suspending all biological enzymatic processes and preserving germplasm indefinitely.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "Which flagship government mission launched in 2014 focuses on the development and genetic conservation of indigenous bovine breeds in India?",
        "o": ["Operation Flood", "Rashtriya Gokul Mission (RGM)", "Key Village Scheme", "National Livestock Mission"],
        "a": 1,
        "e": "The Rashtriya Gokul Mission was launched for the genetic upgradation and conservation of indigenous bovine breeds and establishment of Gokul Grams.",
        "topicId": "u3-t20",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "In Multiple Ovulation and Embryo Transfer (MOET), on which day post-insemination are bovine embryos non-surgically flushed from the donor uterus?",
        "o": ["Day 3", "Day 7", "Day 14", "Day 21"],
        "a": 1,
        "e": "Embryos reach the morula/blastocyst stage and enter the uterine horns by Day 7, which is the optimal time for non-surgical catheter flushing.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "Which hormone is standardly administered to donor cows to induce superovulation in a MOET program?",
        "o": ["Progesterone", "Follicle Stimulating Hormone (FSH)", "Oxytocin", "Prolactin"],
        "a": 1,
        "e": "Pituitary-derived FSH (or eCG/PMSG) is administered over 4 days to stimulate multiple ovarian follicles to mature and ovulate simultaneously.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "Flow cytometric sorting of X- and Y-bearing spermatozoa for sex-sorted semen is based on the fact that bovine X-sperm contain:",
        "o": ["3.8% to 4.2% more DNA than Y-sperm", "50% more protein than Y-sperm", "A negative surface charge", "Two flagella"],
        "a": 0,
        "e": "Because the bovine X chromosome is substantially larger than the Y chromosome, X-bearing spermatozoa contain approximately 3.8–4.2% more total DNA.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "Who proposed the methodology of Genomic Selection using genome-wide dense SNP markers in 2001?",
        "o": ["Meuwissen, Hayes, and Goddard", "Hazel and Lush", "Robertson and Rendel", "Watson and Crick"],
        "a": 0,
        "e": "Theo Meuwissen, Ben Hayes, and Mike Goddard (2001) proposed Genomic Selection to predict Genomic Estimated Breeding Values (GEBV) from SNP markers.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "The primary operational benefit of Genomic Selection in dairy cattle breeding is:",
        "o": ["Halving the generation interval by selecting bulls at birth", "Eliminating the need for liquid nitrogen", "Guaranteeing 100% female calves", "Preventing all recessive mutations"],
        "a": 0,
        "e": "Genomic selection predicts a bull's breeding value from a DNA sample at birth, eliminating the 5–6 year waiting period for daughter milking records.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "In cattle, the Major Histocompatibility Complex (MHC) linked to disease resistance and immune response is termed:",
        "o": ["HLA", "BoLA (Bovine Leukocyte Antigen)", "SLA", "DLA"],
        "a": 1,
        "e": "BoLA (Bovine Leukocyte Antigen) is the bovine MHC complex, whose polymorphic alleles correlate with resistance to mastitis and tick infestation.",
        "topicId": "u3-t23",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "In commercial poultry, which blood group / MHC locus is famously linked with genetic resistance to Marek's disease?",
        "o": ["A locus", "B locus (e.g. B21 allele)", "C locus", "D locus"],
        "a": 1,
        "e": "The B21 allele of the chicken MHC (B blood group system) confers strong genetic resistance to tumor formation by Marek's disease herpesvirus.",
        "topicId": "u3-t23",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "Genetic resistance to classical Scrapie in sheep is determined by polymorphisms in which gene?",
        "o": ["BoLA-DRB3 gene", "Prion Protein (PrP) gene", "Myostatin gene", "Kappa-casein gene"],
        "a": 1,
        "e": "The prion protein (PrP) gene at codons 136, 154, and 171 controls scrapie resistance; the ARR allele confers resistance, while VRQ confers susceptibility.",
        "topicId": "u3-t23",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "The Operation Flood program that spearheaded the White Revolution in India was launched by NDDB in the year:",
        "o": ["1952", "1964", "1970", "1991"],
        "a": 2,
        "e": "Operation Flood was launched in 1970 by the National Dairy Development Board (NDDB) under Dr. Verghese Kurien, transforming India into the top milk producer.",
        "topicId": "u3-t20",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "Which bovine milk protein genetic variant is widely preferred in indigenous zebu cattle due to human health benefits?",
        "o": ["A1 beta-casein", "A2 beta-casein", "Alpha-lactalbumin", "Beta-lactoglobulin"],
        "a": 1,
        "e": "Indigenous Bos indicus cattle almost exclusively produce the A2 beta-casein allele (proline at position 67), which does not release inflammatory BCM-7 peptide.",
        "topicId": "u3-t23",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "In-vitro fertilization (IVF) coupled with transvaginal aspiration of immature oocytes from live cows is called:",
        "o": ["Ovum Pick-Up (OPU)", "Embryo splitting", "Nuclear transfer", "Sperm sexing"],
        "a": 0,
        "e": "OPU (Ovum Pick-Up) uses ultrasound-guided needle aspiration to recover oocytes from pregnant or cycling cows for in-vitro embryo production.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "The Intensive Cattle Development Project (ICDP) in India was initiated during which decade?",
        "o": ["1950s", "1960s (1964–65)", "1980s", "2000s"],
        "a": 1,
        "e": "ICDP was initiated in 1964–65 to provide intensive cattle breeding, nutrition, and disease control packages around major dairy plants.",
        "topicId": "u3-t20",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "Which indigenous sheep breed of Rajasthan has been designated as an endangered germplasm needing urgent in-situ conservation?",
        "o": ["Chokla", "Sonadi", "Malpura", "Pugal / Kheri"],
        "a": 3,
        "e": "Several native breeds with restricted geographical pockets (e.g. Pugal sheep, Toda buffalo, Punganur dwarf cow) require targeted conservation.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "In artificial insemination of cattle, the standard volume of a French mini-straw used for packaging frozen semen is:",
        "o": ["0.25 mL", "0.50 mL", "1.0 mL", "2.0 mL"],
        "a": 0,
        "e": "French mini-straws hold 0.25 mL of diluted semen (containing ~20 million progressively motile spermatozoa), while medium straws hold 0.50 mL.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 1
    },

    # ============================================================
    # u3-s5: Pet, Zoo & Wild Animal Breeding (18 MCQs)
    # ============================================================
    {
        "q": "Which celebrated Indian sighthound breed originated in Karnataka and Maharashtra and has been inducted into the Indian Army?",
        "o": ["Mudhol Hound (Caravan Hound)", "Rajapalayam", "Chippiparai", "Kombai"],
        "a": 0,
        "e": "The Mudhol Hound is an ancient Indian sighthound known for exceptional speed, stamina, and keen hunting vision.",
        "topicId": "u3-t24",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The Rajapalayam dog breed, characterized by a milk-white coat, pink nose, and golden eyes, originated in which Indian state?",
        "o": ["Kerala", "Tamil Nadu", "Karnataka", "Punjab"],
        "a": 1,
        "e": "The Rajapalayam is a royal sighthound native to Rajapalayam town in Virudhunagar district, Tamil Nadu.",
        "topicId": "u3-t24",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "Under the Kennel Club classification, the Labrador Retriever and Golden Retriever belong to which dog breed group?",
        "o": ["Hound group", "Sporting (Gun dog) group", "Terrier group", "Toy group"],
        "a": 1,
        "e": "Retrievers and spaniels belong to the Sporting (or Gun dog) group, bred to locate and retrieve game birds.",
        "topicId": "u3-t24",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "What is the average gestation length in the domestic canine bitch?",
        "o": ["45 days", "63 days (range 58–68 days)", "90 days", "114 days"],
        "a": 1,
        "e": "Canine pregnancy averages 63 days from ovulation (range 58 to 68 days).",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The canine estrous cycle stage characterized by vulvar swelling, serosanguinous discharge, and attraction of males without permitting mating is:",
        "o": ["Proestrus", "Estrus", "Diestrus", "Anestrus"],
        "a": 0,
        "e": "Proestrus lasts ~9 days. The bitch displays bloody discharge and swollen vulva but will vigorously refuse mating until entering estrus.",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "During canine mating, the mechanical 'copulatory tie' that locks the dog and bitch together for 15–30 minutes is caused by swelling of the:",
        "o": ["Os penis", "Bulbus glandis", "Prostate gland", "Glans clitoridis"],
        "a": 1,
        "e": "The spherical swelling of the bulbus glandis of the canine penis inside the female vestibular constrictor muscle creates the copulatory lock.",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "Domestic feline queens exhibit which unique ovulatory mechanism during reproduction?",
        "o": ["Spontaneous cyclical ovulation", "Induced (reflex) ovulation triggered by coitus", "Seasonal monoestrus only", "Silent ovulation without estrus"],
        "a": 1,
        "e": "Cats are induced (reflex) ovulators; tactile stimulation of the cervix by the penile spines during coitus triggers the LH surge and subsequent ovulation.",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "What is the average gestation length in the domestic cat (queen)?",
        "o": ["45 days", "63 to 65 days", "80 days", "30 days"],
        "a": 1,
        "e": "The gestation period of domestic queens averages 63–65 days (similar to dogs).",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "What is the standard incubation period for fertile eggs of the popular pet bird, the Budgerigar (Melopsittacus undulatus)?",
        "o": ["10–12 days", "18 days", "28 days", "35 days"],
        "a": 1,
        "e": "Budgerigar eggs have an average incubation period of 18 days (Cockatiels take ~19–21 days).",
        "topicId": "u3-t26",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "In conservation genetics, the size of an idealized panmictic population that has the same rate of inbreeding or genetic drift as the actual population is the:",
        "o": ["Census population size (N)", "Effective population size (N_e)", "Minimum viable population (MVP)", "Carrying capacity (K)"],
        "a": 1,
        "e": "Effective population size (N_e) accounts for unequal sex ratios and variance in family size, measuring the genetic breeding capacity of the herd.",
        "topicId": "u3-t27",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "What is Wright's formula for effective population size (N_e) when the numbers of breeding males (N_m) and breeding females (N_f) are unequal?",
        "o": ["N_e = (4 * N_m * N_f) / (N_m + N_f)", "N_e = (N_m + N_f) / 2", "N_e = N_m * N_f", "N_e = (2 * N_m * N_f) / (N_m + N_f)"],
        "a": 0,
        "e": "N_e = (4 * N_m * N_f) / (N_m + N_f). If there is only 1 breeding male and 100 females, N_e ≈ 4, causing massive genetic drift.",
        "topicId": "u3-t27",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "According to the famous 50/500 rule in conservation biology, what minimum effective population size (N_e) is needed to avoid short-term inbreeding depression?",
        "o": ["10", "50", "500", "5000"],
        "a": 1,
        "e": "Franklin and Soulé proposed N_e = 50 to prevent short-term inbreeding depression, and N_e = 500 to retain long-term evolutionary potential.",
        "topicId": "u3-t27",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "In captive wild animal breeding in modern zoos, which document records the complete ancestry and breeding history of all captive individuals of a species?",
        "o": ["Studbook", "Pedigree certificate", "Herdbook", "Taxonomic ledger"],
        "a": 0,
        "e": "International and regional Studbooks (managed by species survival coordinators) trace the full lineage of every captive individual to minimize inbreeding.",
        "topicId": "u3-t28",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "Which statutory body oversees and regulates captive animal management and conservation breeding programs in recognized zoos across India?",
        "o": ["Central Zoo Authority (CZA)", "Animal Welfare Board of India (AWBI)", "Wildlife Trust of India (WTI)", "National Biodiversity Authority (NBA)"],
        "a": 0,
        "e": "The Central Zoo Authority (CZA) is the statutory body under the Ministry of Environment, Forest and Climate Change governing Indian zoos and breeding programs.",
        "topicId": "u3-t28",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The world-renowned Vulture Conservation Breeding Centre (VCBC) established by BNHS to breed critically endangered Gyps vultures is located at:",
        "o": ["Pinjore, Haryana", "Kaziranga, Assam", "Gir, Gujarat", "Dehradun, Uttarakhand"],
        "a": 0,
        "e": "Jatayu Conservation Breeding Centre at Pinjore (Haryana) was set up by BNHS and Haryana Forest Dept to breed Gyps vultures decimated by diclofenac.",
        "topicId": "u3-t28",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "The Padmaja Naidu Himalayan Zoological Park in Darjeeling is globally celebrated for the successful conservation breeding of which endangered species?",
        "o": ["Red Panda and Snow Leopard", "Asiatic Lion", "Gharial", "Great Indian Bustard"],
        "a": 0,
        "e": "Darjeeling Zoo is internationally acclaimed for its successful captive breeding programs for Red Pandas and Snow Leopards.",
        "topicId": "u3-t28",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "What ISO microchip frequency standard is standardly used for electronic identification of pet animals and zoo species in India?",
        "o": ["134.2 kHz (ISO 11784/11785)", "125 kHz", "915 MHz", "2.4 GHz"],
        "a": 0,
        "e": "The global standard for animal RFID microchip identification is 134.2 kHz conforming to ISO 11784 (15-digit code) and ISO 11785.",
        "topicId": "u3-t24",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "A genetic condition in purebred dogs where the femoral head does not fit properly into the acetabular pelvic socket is called:",
        "o": ["Canine Hip Dysplasia (CHD)", "Patellar luxation", "Ectrodactyly", "Intervertebral disc disease"],
        "a": 0,
        "e": "Canine Hip Dysplasia (CHD) is a multifactorial polygenic inherited defect common in large breeds like German Shepherds and Labradors.",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    }
]

unit3_tf = [
    # ============================================================
    # u3-s1: Economic Traits & Selection Methods (9 T/F)
    # ============================================================
    {
        "q": "Robert Bakewell formulated the breeding principle 'Breed the best to the best' and pioneered sire letting.",
        "a": True,
        "e": "Robert Bakewell (1725–1795) transformed animal breeding into a systematic science by leasing rams and bulls to test their progeny.",
        "topicId": "u3-t01",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "The official standard lactation length for genetic evaluation of dairy cows is 305 days.",
        "a": True,
        "e": "Official milk yield records are standardized to 305 days to eliminate differences caused by variable lactation lengths.",
        "topicId": "u3-t03",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Selection differential is the difference between the mean of selected parents and the mean of the unselected population.",
        "a": True,
        "e": "Selection differential S = P_selected - P_pop, measuring the phenotypic superiority of chosen breeders.",
        "topicId": "u3-t04",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Increasing the generation interval increases the annual rate of genetic gain.",
        "a": False,
        "e": "Because generation interval L is in the denominator (ΔG = (i * r_TI * σ_A) / L), increasing L reduces the annual rate of genetic gain.",
        "topicId": "u3-t04",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Progeny testing is the most reliable basis of selection for sex-limited traits of low heritability like dairy milk production.",
        "a": True,
        "e": "Evaluating sires on the lactation records of 30–50 daughters provides high selection accuracy for sex-limited low-heritability traits.",
        "topicId": "u3-t05",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Tandem selection is mathematically the most efficient method of multi-trait selection.",
        "a": False,
        "e": "Tandem selection is the LEAST efficient method; Hazel and Lush proved that the Selection Index is mathematically the most efficient.",
        "topicId": "u3-t07",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "In Independent Culling Levels, an animal excelling exceptionally in milk yield will be retained even if it fails the fertility culling standard.",
        "a": False,
        "e": "In Independent Culling Levels, failure in any single trait results in immediate disqualification, regardless of superiority in other traits.",
        "topicId": "u3-t07",
        "subSection": "u3-s1",
        "diff": 2
    },
    {
        "q": "L. N. Hazel (1943) developed the theory and methodology of the Selection Index in animal breeding.",
        "a": True,
        "e": "Hazel developed the selection index combining multiple traits weighted by their economic weights and genetic covariances.",
        "topicId": "u3-t07",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Sib selection is essential for carcass and meat quality traits where the breeding candidate cannot be slaughtered.",
        "a": True,
        "e": "Because measuring meat quality requires animal slaughter, candidates are chosen based on the performance of their slaughtered siblings.",
        "topicId": "u3-t05",
        "subSection": "u3-s1",
        "diff": 1
    },

    # ============================================================
    # u3-s2: Mating Systems, Inbreeding & Heterosis (9 T/F)
    # ============================================================
    {
        "q": "One generation of full-brother × full-sister mating produces an inbreeding coefficient of F = 0.25 (25%).",
        "a": True,
        "e": "Full-sib mating results in a 25% probability that two homologous alleles in the offspring are identical by descent (F = 0.25).",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "The coefficient of relationship between half-sibs is 0.50.",
        "a": False,
        "e": "Half-sibs share one common parent and have a coefficient of relationship R = 0.25. Full-sibs share both parents and have R = 0.50.",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "Inbreeding increases heterozygosity and creates new genetic variation in a closed population.",
        "a": False,
        "e": "Inbreeding increases homozygosity and reduces heterozygosity, fixing alleles and splitting the herd into distinct inbred lines.",
        "topicId": "u3-t10",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "Inbreeding depression is most severe for reproductive and fitness traits, while carcass traits suffer minimal depression.",
        "a": True,
        "e": "Fitness, fertility, and survival traits have low heritability and suffer sharp inbreeding depression, whereas high-heritability carcass traits are little affected.",
        "topicId": "u3-t10",
        "subSection": "u3-s2",
        "diff": 2
    },
    {
        "q": "Grading up continuously uses purebred elite sires on grade/non-descript females generation after generation.",
        "a": True,
        "e": "Grading up systematically replaces native scrub genetics with purebred inheritance, reaching 99.2% purebred blood in 7 generations.",
        "topicId": "u3-t11",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "A mule is produced by crossing a male horse with a female donkey.",
        "a": False,
        "e": "A mule is Jack (male donkey) × Mare (female horse). Male horse × Female donkey produces a Hinny.",
        "topicId": "u3-t11",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "Heterosis is highest for traits that have low heritability, such as fertility and embryo survival.",
        "a": True,
        "e": "Heterosis and inbreeding depression are mirror opposites: traits with low heritability show the largest percentage heterosis upon crossbreeding.",
        "topicId": "u3-t12",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "The overdominance hypothesis of heterosis states that the heterozygote (Aa) is superior to both homozygotes (AA and aa).",
        "a": True,
        "e": "The overdominance hypothesis postulates direct single-locus heterozygous superiority.",
        "topicId": "u3-t12",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "Reciprocal Recurrent Selection (RRS) simultaneously utilizes both General Combining Ability and Specific Combining Ability.",
        "a": True,
        "e": "RRS uses two populations as mutual testers, exploiting both additive variance (GCA) and dominance/epistatic variance (SCA).",
        "topicId": "u3-t13",
        "subSection": "u3-s2",
        "diff": 2
    },

    # ============================================================
    # u3-s3: Livestock & Poultry Breeding Strategies (9 T/F)
    # ============================================================
    {
        "q": "Sahiwal is an indigenous dairy cattle breed of India originating from the Montgomery district.",
        "a": True,
        "e": "Sahiwal is renowned for heavy milk production, tick resistance, and heat tolerance in tropical dairy farming.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Indian national breeding policy recommends grading up indigenous cattle to 100% pure Holstein-Friesian.",
        "a": False,
        "e": "Policy strictly limits exotic inheritance to 50%–62.5% (or 5/8) to prevent heat prostration and disease breakdown in tropical field conditions.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The Frieswal synthetic dairy strain carries 62.5% Holstein-Friesian and 37.5% Sahiwal blood.",
        "a": True,
        "e": "Developed jointly by ICAR-CIRC Meerut and Military Farms, Frieswal carries exactly 5/8 (62.5%) HF and 3/8 (37.5%) Sahiwal inheritance.",
        "topicId": "u3-t19",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Bhadawari buffaloes produce milk with the highest fat percentage (up to 12–14%) among Indian buffalo breeds.",
        "a": True,
        "e": "Bhadawari buffaloes are renowned for milk fat percentages ranging from 8% to 13%, and possess a copper-colored body coat.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Chokla sheep of Rajasthan are widely referred to as the 'Merino of Rajasthan' for fine carpet wool.",
        "a": True,
        "e": "Chokla produces high-quality fine carpet wool with superior staple crimp and luster.",
        "topicId": "u3-t15",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Black Bengal goats are known for poor prolificacy, rarely producing more than a single kid per kidding.",
        "a": False,
        "e": "Black Bengal is celebrated for extreme prolificacy, routinely kidding twins, triplets, and quadruplets.",
        "topicId": "u3-t15",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "C. R. Henderson developed the Best Linear Unbiased Prediction (BLUP) method for animal genetic evaluation.",
        "a": True,
        "e": "Charles Roy Henderson developed BLUP and Mixed Model Equations (MME) in 1973, revolutionizing global dairy sire proofing.",
        "topicId": "u3-t17",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "In an Open Nucleus Breeding System (ONBS), gene flow is strictly one-way from the nucleus to commercial herds.",
        "a": False,
        "e": "In ONBS, gene flow is two-way: elite superior females from commercial herds are actively screened and admitted into the nucleus herd.",
        "topicId": "u3-t18",
        "subSection": "u3-s3",
        "diff": 2
    },
    {
        "q": "Single Comb White Leghorn is the primary foundation breed for commercial white egg layer chicken lines.",
        "a": True,
        "e": "White Leghorns are early-maturing, small-bodied, efficient feed converters producing high numbers of large white eggs.",
        "topicId": "u3-t16",
        "subSection": "u3-s3",
        "diff": 1
    },

    # ============================================================
    # u3-s4: Breeding Policies & Genetic Conservation (9 T/F)
    # ============================================================
    {
        "q": "ICAR-NBAGR, Karnal, is the nodal national agency responsible for registering and assigning accession numbers to new Indian livestock breeds.",
        "a": True,
        "e": "The National Bureau of Animal Genetic Resources in Karnal is the sole authority cataloguing and registering indigenous livestock breeds.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "In-situ conservation maintains livestock populations outside their native agro-ecological habitat in national zoos.",
        "a": False,
        "e": "In-situ conservation maintains animals in their native natural farming habitat. Maintaining them outside in zoos or parks is ex-situ in-vivo.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "Animal germplasm is cryopreserved in liquid nitrogen at -196°C in the National Gene Bank.",
        "a": True,
        "e": "Liquid nitrogen at -196°C arrests all biological and enzymatic degradation, storing viable semen and embryos indefinitely.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "In Multiple Ovulation and Embryo Transfer (MOET), bovine embryos are flushed on Day 7 post-insemination.",
        "a": True,
        "e": "Day 7 blastocysts/morulae are located in the uterine horns and can be flushed non-surgically using a Foley catheter.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "Genomic selection increases the generation interval in dairy cattle breeding.",
        "a": False,
        "e": "Genomic selection drastically REDUCES generation interval (halving it from 5–6 years down to ~1.5–2 years) because breeding values are evaluated at birth.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "Bovine X-bearing spermatozoa contain approximately 3.8% to 4.2% more DNA than Y-bearing spermatozoa.",
        "a": True,
        "e": "The difference in DNA content allows flow cytometric sorting of Hoechst-stained live spermatozoa into X and Y populations with >90% purity.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "The B21 allele of the chicken MHC complex is linked to genetic resistance against Marek's disease virus.",
        "a": True,
        "e": "Chickens homozygous or heterozygous for the B21 haplotype show marked resistance to lymphoid tumor development by Marek's disease virus.",
        "topicId": "u3-t23",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "Scrapie resistance in sheep is governed by polymorphisms in the prion protein (PrP) gene.",
        "a": True,
        "e": "PrP codon variations (specifically the ARR haplotype) confer high resistance to classical scrapie transmission.",
        "topicId": "u3-t23",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "Indigenous Bos indicus (zebu) cattle predominantly produce the A1 beta-casein milk variant.",
        "a": False,
        "e": "Indian zebu cattle almost 100% naturally produce the beneficial A2 beta-casein variant; A1 is prevalent in European Bos taurus breeds.",
        "topicId": "u3-t23",
        "subSection": "u3-s4",
        "diff": 1
    },

    # ============================================================
    # u3-s5: Pet, Zoo & Wild Animal Breeding (9 T/F)
    # ============================================================
    {
        "q": "The Mudhol Hound is an indigenous Indian sighthound breed native to Karnataka and Maharashtra.",
        "a": True,
        "e": "The Mudhol (Caravan) Hound is a hardy sighthound developed in the Deccan plateau, used for hunting and border security.",
        "topicId": "u3-t24",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The gestation period of a domestic canine bitch averages 63 days.",
        "a": True,
        "e": "Average canine pregnancy lasts 63 days from ovulation (range 58–68 days).",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The domestic cat is an induced (reflex) ovulator requiring coital stimulation for ovulation.",
        "a": True,
        "e": "Coitus stimulates vaginal/cervical mechanoreceptors in queens, triggering an LH surge that induces ovulation 24–48 hours later.",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "In canine mating, the copulatory tie is caused by the enlargement of the bulbus glandis of the penis.",
        "a": True,
        "e": "Venous engorgement of the bulbus glandis locks the penis within the female vestibule for 15–30 minutes, ensuring sperm transfer.",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "An unequal sex ratio (e.g. 1 male and 100 females) substantially increases the effective population size (N_e).",
        "a": False,
        "e": "A skewed sex ratio drastically DECREASES N_e (N_e = 4*1*100 / 101 ≈ 3.96), accelerating genetic drift and inbreeding.",
        "topicId": "u3-t27",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "According to the 50/500 rule in conservation genetics, N_e = 50 is recommended to avoid short-term inbreeding depression.",
        "a": True,
        "e": "N_e = 50 limits inbreeding to 1% per generation; N_e = 500 maintains long-term quantitative genetic variation.",
        "topicId": "u3-t27",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "A Studbook records the pedigree and demographic history of an endangered captive species across zoological parks.",
        "a": True,
        "e": "Studbooks prevent inadvertent inbreeding by directing optimal breeding pairings between unrelated zoo animals globally.",
        "topicId": "u3-t28",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The Central Zoo Authority (CZA) is the statutory body regulating captive conservation breeding programs in India.",
        "a": True,
        "e": "CZA coordinates coordinated conservation breeding for 73 endangered species across Indian zoos.",
        "topicId": "u3-t28",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "Standard electronic pet microchips operate at 134.2 kHz conforming to ISO 11784/11785 standards.",
        "a": True,
        "e": "ISO 11784/11785 134.2 kHz RFID microchips with 15-digit codes are the global standard for companion animal identification.",
        "topicId": "u3-t24",
        "subSection": "u3-s5",
        "diff": 1
    }
]

unit3_fib = [
    # ============================================================
    # u3-s1: Economic Traits & Selection Methods (9 FIB)
    # ============================================================
    {
        "q": "Robert ______ (1725–1795) is universally recognized as the Father of Animal Breeding.",
        "a": ["Bakewell"],
        "a_display": "Bakewell",
        "e": "Robert Bakewell of Dishley introduced systematic inbreeding, sire letting, and progeny testing.",
        "topicId": "u3-t01",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "The Father of Modern Animal Breeding who authored 'Animal Breeding Plans' in 1937 was Jay L. ______.",
        "a": ["Lush"],
        "a_display": "Lush",
        "e": "Jay L. Lush established the biometrical foundation of quantitative livestock improvement at Iowa State.",
        "topicId": "u3-t01",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "The standard duration of lactation milk yield standardized for official dairy cattle evaluation is ______ days.",
        "a": ["305", "305 days"],
        "a_display": "305",
        "e": "305-day milk yield is the standard production period in dairy cattle breeding.",
        "topicId": "u3-t03",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "The difference between the mean performance of selected parents and the unselected herd mean is the selection ______.",
        "a": ["differential"],
        "a_display": "Differential",
        "e": "Selection differential S = P_selected - P_pop.",
        "topicId": "u3-t04",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "The average age of parents when replacement offspring are born is termed the generation ______.",
        "a": ["interval"],
        "a_display": "Interval",
        "e": "Generation interval (L) is the turnover time of a breeding generation.",
        "topicId": "u3-t04",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Selecting dairy sires based on the milk production of their daughters is called ______ testing.",
        "a": ["progeny", "progeny testing"],
        "a_display": "Progeny",
        "e": "Progeny testing evaluates the transmitting ability of dairy bulls using daughter lactation records.",
        "topicId": "u3-t05",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "Selecting for a correlated trait X to achieve genetic change in trait Y is known as ______ selection.",
        "a": ["indirect"],
        "a_display": "Indirect",
        "e": "Indirect selection uses genetic correlation to improve difficult or sex-limited traits.",
        "topicId": "u3-t06",
        "subSection": "u3-s1",
        "diff": 2
    },
    {
        "q": "The multi-trait selection method that selects for only one trait at a time is ______ selection.",
        "a": ["tandem", "tandem selection"],
        "a_display": "Tandem",
        "e": "Tandem selection is the least efficient multi-trait selection strategy.",
        "topicId": "u3-t07",
        "subSection": "u3-s1",
        "diff": 1
    },
    {
        "q": "The linear combination score weighting multiple traits by economic and genetic values is the Selection ______.",
        "a": ["Index", "selection index"],
        "a_display": "Index",
        "e": "Hazel's Selection Index (I = Σ b_i X_i) is the most efficient multi-trait selection method.",
        "topicId": "u3-t07",
        "subSection": "u3-s1",
        "diff": 1
    },

    # ============================================================
    # u3-s2: Mating Systems, Inbreeding & Heterosis (9 FIB)
    # ============================================================
    {
        "q": "Sewall Wright formulated the inbreeding coefficient denoted by the capital letter ______.",
        "a": ["F"],
        "a_display": "F",
        "e": "Wright's inbreeding coefficient F measures probability of identity by descent.",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "The inbreeding coefficient resulting from a full-brother × full-sister mating is ______ (or 25%).",
        "a": ["0.25", "25%", "1/4"],
        "a_display": "0.25 (25%)",
        "e": "Full-sib mating produces F = 0.25 in the progeny.",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "The coefficient of relationship between a non-inbred dam and her calf is ______ (or 50%).",
        "a": ["0.50", "0.5", "50%", "1/2"],
        "a_display": "0.50 (50%)",
        "e": "Parent and offspring share 50% of their genes (R = 0.50).",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "A mild form of inbreeding directed toward maintaining a high relationship to an outstanding ancestor is ______.",
        "a": ["linebreeding"],
        "a_display": "Linebreeding",
        "e": "Linebreeding concentrates the genetic contribution of a superior ancestor while keeping F low.",
        "topicId": "u3-t09",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "The decline in fitness and fertility accompanying inbreeding is called inbreeding ______.",
        "a": ["depression"],
        "a_display": "Depression",
        "e": "Inbreeding depression results from the manifestation of deleterious homozygous recessives.",
        "topicId": "u3-t10",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "The systematic mating of purebred sires to non-descript native females generation after generation is ______ up.",
        "a": ["grading", "grading up"],
        "a_display": "Grading",
        "e": "Grading up replaces scrub genetics with purebred inheritance over 5–7 generations.",
        "topicId": "u3-t11",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "A sterile hybrid produced by mating a male donkey (jack) with a female horse (mare) is a ______.",
        "a": ["mule"],
        "a_display": "Mule",
        "e": "Jack × Mare = Mule (sterile, 2n = 63).",
        "topicId": "u3-t11",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "Hybrid vigour resulting from crossbreeding is also scientifically known as ______.",
        "a": ["heterosis"],
        "a_display": "Heterosis",
        "e": "Heterosis is the superior performance of crossbred progeny over parental breed averages.",
        "topicId": "u3-t12",
        "subSection": "u3-s2",
        "diff": 1
    },
    {
        "q": "The breeding method in commercial poultry that selects simultaneously for GCA and SCA is Reciprocal Recurrent ______ (RRS).",
        "a": ["Selection", "selection"],
        "a_display": "Selection",
        "e": "RRS (Reciprocal Recurrent Selection) uses two populations as mutual testers.",
        "topicId": "u3-t13",
        "subSection": "u3-s2",
        "diff": 2
    },

    # ============================================================
    # u3-s3: Livestock & Poultry Breeding Strategies (9 FIB)
    # ============================================================
    {
        "q": "Under Indian breeding policy, exotic inheritance in crossbred dairy cattle is restricted between 50% and ______ percent.",
        "a": ["62.5", "62.5%", "5/8"],
        "a_display": "62.5% (5/8)",
        "e": "Exotic inheritance is capped at 50% to 62.5% to balance milk yield and environmental adaptation.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The synthetic dairy cattle breed carrying 62.5% Holstein-Friesian and 37.5% Sahiwal blood developed at Meerut is ______.",
        "a": ["Frieswal"],
        "a_display": "Frieswal",
        "e": "Frieswal was developed by ICAR-CIRC Meerut and the Military Farms Directorate.",
        "topicId": "u3-t19",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The premier dairy buffalo breed of Haryana, famous as the 'Black Gold', is the ______.",
        "a": ["Murrah"],
        "a_display": "Murrah",
        "e": "Murrah buffalo is the highest-yielding dairy buffalo breed of India.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The copper-colored buffalo breed famous for yielding milk fat up to 13% is the ______.",
        "a": ["Bhadawari"],
        "a_display": "Bhadawari",
        "e": "Bhadawari buffaloes of UP/MP produce milk with the highest fat percentage.",
        "topicId": "u3-t14",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The premier carpet-wool sheep breed known as the 'Merino of Rajasthan' is the ______.",
        "a": ["Chokla"],
        "a_display": "Chokla",
        "e": "Chokla sheep produce fine carpet fleece in Rajasthan.",
        "topicId": "u3-t15",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The prolific goat breed of West Bengal noted for multiple births and fine chevon is the Black ______.",
        "a": ["Bengal"],
        "a_display": "Bengal",
        "e": "Black Bengal goats excel in fecundity, twinning, and skin quality.",
        "topicId": "u3-t15",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "Commercial broiler chicken sire lines are developed from the White ______ breed for muscling.",
        "a": ["Cornish"],
        "a_display": "Cornish",
        "e": "White Cornish contributes heavy breast muscle and rapid weight gain.",
        "topicId": "u3-t16",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "The modern statistical algorithm developed by C. R. Henderson for sire evaluation is abbreviated as ______.",
        "a": ["BLUP"],
        "a_display": "BLUP",
        "e": "BLUP (Best Linear Unbiased Prediction) is the international standard for sire evaluation.",
        "topicId": "u3-t17",
        "subSection": "u3-s3",
        "diff": 1
    },
    {
        "q": "A breeding system allowing elite females from commercial herds into the nucleus is an ______ Nucleus Breeding System.",
        "a": ["Open", "open nucleus"],
        "a_display": "Open",
        "e": "Open Nucleus Breeding Systems (ONBS) feature two-way gene flow, reducing inbreeding.",
        "topicId": "u3-t18",
        "subSection": "u3-s3",
        "diff": 2
    },

    # ============================================================
    # u3-s4: Breeding Policies & Genetic Conservation (9 FIB)
    # ============================================================
    {
        "q": "The ICAR bureau responsible for registration of livestock breeds in India is ICAR-______ in Karnal.",
        "a": ["NBAGR"],
        "a_display": "NBAGR",
        "e": "ICAR-NBAGR (National Bureau of Animal Genetic Resources) registers domestic breeds.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "Preservation of livestock in their native agricultural habitat by farmers is ______-situ conservation.",
        "a": ["in", "in-situ", "in situ"],
        "a_display": "In",
        "e": "In-situ conservation maintains breeds within their natural agricultural ecosystems.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "Animal semen and embryos are cryopreserved in liquid nitrogen at a temperature of -______ °C.",
        "a": ["196", "196°C", "196 C"],
        "a_display": "196",
        "e": "Liquid nitrogen maintains -196°C for indefinite germplasm cryostorage.",
        "topicId": "u3-t21",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "The national program launched in 2014 for indigenous bovine conservation is the Rashtriya ______ Mission.",
        "a": ["Gokul"],
        "a_display": "Gokul",
        "e": "Rashtriya Gokul Mission (RGM) focuses on indigenous breed development.",
        "topicId": "u3-t20",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "In MOET, bovine embryos are non-surgically flushed from the donor uterus on Day ______ post-insemination.",
        "a": ["7", "seven"],
        "a_display": "7",
        "e": "Day 7 morula/blastocyst embryos are flushed from the uterine horns.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "Genomic selection predicts a calf's breeding value using high-density ______ markers on DNA chips.",
        "a": ["SNP", "snps"],
        "a_display": "SNP",
        "e": "Single Nucleotide Polymorphisms (SNPs) provide whole-genome markers for GEBV estimation.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "The Major Histocompatibility Complex of cattle is termed ______ (Bovine Leukocyte Antigen).",
        "a": ["BoLA"],
        "a_display": "BoLA",
        "e": "BoLA is the polymorphic MHC genetic complex of cattle.",
        "topicId": "u3-t23",
        "subSection": "u3-s4",
        "diff": 1
    },
    {
        "q": "In commercial poultry, the B______ allele confers strong resistance to Marek's disease.",
        "a": ["21"],
        "a_display": "21",
        "e": "The B21 MHC haplotype provides genetic resistance to Marek's disease virus.",
        "topicId": "u3-t23",
        "subSection": "u3-s4",
        "diff": 2
    },
    {
        "q": "The French mini-straw standardly used for packaging frozen bull semen has a volume of 0.______ mL.",
        "a": ["25", "25 ml"],
        "a_display": "25",
        "e": "French mini-straws hold 0.25 mL of cryopreserved semen.",
        "topicId": "u3-t22",
        "subSection": "u3-s4",
        "diff": 1
    },

    # ============================================================
    # u3-s5: Pet, Zoo & Wild Animal Breeding (9 FIB)
    # ============================================================
    {
        "q": "The indigenous sighthound of Karnataka and Maharashtra inducted into the Indian Army is the ______ Hound.",
        "a": ["Mudhol", "Caravan"],
        "a_display": "Mudhol",
        "e": "The Mudhol Hound is a celebrated native sighthound of Karnataka.",
        "topicId": "u3-t24",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The royal white sighthound breed of Tamil Nadu is the ______.",
        "a": ["Rajapalayam"],
        "a_display": "Rajapalayam",
        "e": "Rajapalayam is an indigenous sighthound of Tamil Nadu with white coat and pink nose.",
        "topicId": "u3-t24",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The average gestation period of the domestic canine bitch is ______ days.",
        "a": ["63", "sixty three", "sixty-three"],
        "a_display": "63",
        "e": "Canine gestation averages 63 days (58–68 days).",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "During canine mating, the copulatory tie is caused by the swelling of the ______ glandis.",
        "a": ["bulbus", "bulbus glandis"],
        "a_display": "Bulbus",
        "e": "The bulbus glandis engorges with blood, creating the copulatory lock.",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "The domestic feline queen is an ______ ovulator, requiring coitus to trigger an LH surge.",
        "a": ["induced", "reflex"],
        "a_display": "Induced",
        "e": "Cats are induced (reflex) ovulators.",
        "topicId": "u3-t25",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The average incubation period for fertile Budgerigar eggs is ______ days.",
        "a": ["18", "eighteen"],
        "a_display": "18",
        "e": "Budgerigar eggs hatch after approximately 18 days of incubation.",
        "topicId": "u3-t26",
        "subSection": "u3-s5",
        "diff": 2
    },
    {
        "q": "In conservation genetics, the effective population size is denoted by N with subscript ______.",
        "a": ["e", "E"],
        "a_display": "e (N_e)",
        "e": "N_e is the effective population size.",
        "topicId": "u3-t27",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The registry that maintains the genealogical history of an endangered captive zoo species is a ______.",
        "a": ["studbook"],
        "a_display": "Studbook",
        "e": "Studbooks track the pedigree of captive wild animals to avoid inbreeding.",
        "topicId": "u3-t28",
        "subSection": "u3-s5",
        "diff": 1
    },
    {
        "q": "The statutory body governing Indian zoological parks and conservation breeding is the Central ______ Authority (CZA).",
        "a": ["Zoo"],
        "a_display": "Zoo",
        "e": "The Central Zoo Authority (CZA) regulates captive conservation breeding in India.",
        "topicId": "u3-t28",
        "subSection": "u3-s5",
        "diff": 1
    }
]
