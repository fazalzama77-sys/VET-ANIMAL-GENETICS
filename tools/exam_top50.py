# tools/exam_top50.py
# ------------------------------------------------------------
# EXAM TOP-50 — the fifty most examinable questions per theory unit
# (150 in total), written against the VCI MSVE syllabus outline in
# "Animal Genetics outline.pdf".
#
# Each unit: 26 MCQ + 12 True/False + 12 Fill-in-the-blank = 50
# (as close to the bank's 2 : 1 : 1 weighting as 50 allows).
#
# Priorities, in order:
#   1. syllabus topics the original 540-question bank left empty or
#      thin (gene mutation, breed classification, mating systems,
#      penetrance, cytogenetics, non-parametric tests, pet birds ...)
#   2. the numericals examiners set every year (GM, CV, SE, r from
#      b_yx and b_xy, Spearman, df, gene frequency, 2pq, R = h²S,
#      heterosis %, Ne ...)
#   3. classic one-line facts (who / which breed / which stage)
#
# Every question carries "exam": True so the quiz can offer an
# "Exam Top 50" module for each unit. assemble_quiz.py appends these
# after the original bank, so existing question keys never move.
# ------------------------------------------------------------

# ============================================================
# UNIT 1 — BIOSTATISTICS AND COMPUTER APPLICATION
# ============================================================
exam_unit1_mcq = [
    # ---- u1-s1: classification, central tendency, dispersion, moments ----
    {
        "q": "The word 'Statistics' is derived from the Latin word 'status', which means:",
        "o": ["Political state", "Numerical data", "Chance or probability", "Measurement"],
        "a": 0,
        "e": "'Statistics' comes from the Latin 'status' (Italian 'statista') meaning a political state — early statistics were facts collected by the state about its population and resources.",
        "topicId": "u1-t01", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "A statistical table in which data are classified according to only ONE characteristic is called a:",
        "o": ["Simple (one-way) table", "Two-way table", "Manifold table", "Complex table"],
        "a": 0,
        "e": "A simple or one-way table shows one characteristic only (e.g., number of cattle by breed). Two-way tables show two characteristics; manifold (complex) tables show three or more.",
        "topicId": "u1-t02", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "The number of piglets born per litter is an example of a:",
        "o": ["Continuous variable", "Discrete variable", "Qualitative attribute", "Constant"],
        "a": 1,
        "e": "Litter size can only take whole-number values (0, 1, 2 ...), so it is a discrete (discontinuous) variable. Body weight or milk yield, which can take any value in a range, are continuous.",
        "topicId": "u1-t03", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "In a pie diagram, the angle of the sector for a component is calculated as:",
        "o": ["(Component value / Total) × 100", "(Component value / Total) × 360°", "(Component value / Total) × 180°", "(Total / Component value) × 360°"],
        "a": 1,
        "e": "A full circle is 360°, so each component gets (component ÷ total) × 360°. Multiplying by 100 gives the percentage, not the angle.",
        "topicId": "u1-t04", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "The geometric mean of the observations 4, 8 and 16 is:",
        "o": ["8", "9.33", "6.86", "12"],
        "a": 0,
        "e": "GM = (4 × 8 × 16)^(1/3) = (512)^(1/3) = 8. Note that GM (8) < AM (9.33), as it always is for unequal positive values.",
        "topicId": "u1-t05", "subSection": "u1-s1", "diff": 2
    },
    {
        "q": "Which average is the most appropriate for averaging rates, ratios and speeds (e.g., average speed over equal distances)?",
        "o": ["Arithmetic mean", "Geometric mean", "Harmonic mean", "Median"],
        "a": 2,
        "e": "The harmonic mean (reciprocal of the mean of reciprocals) is correct for rates and speeds. For any set of unequal positive values, AM > GM > HM.",
        "topicId": "u1-t05", "subSection": "u1-s1", "diff": 2
    },
    {
        "q": "The variance (population formula, dividing by N) of the values 2, 4, 6, 8 and 10 is:",
        "o": ["8", "10", "2.83", "4"],
        "a": 0,
        "e": "Mean = 6. Squared deviations = 16 + 4 + 0 + 4 + 16 = 40. Variance = 40 / 5 = 8 (SD = 2.83). The sample variance, dividing by n − 1, would be 10.",
        "topicId": "u1-t06", "subSection": "u1-s1", "diff": 2
    },
    {
        "q": "A herd has a mean daily milk yield of 10 kg with a standard deviation of 2 kg. The coefficient of variation is:",
        "o": ["5%", "20%", "12%", "0.2%"],
        "a": 1,
        "e": "CV = (SD / Mean) × 100 = (2 / 10) × 100 = 20%. CV is unit-free, so it compares variability between traits measured in different units.",
        "topicId": "u1-t07", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "If the sample size is increased four times, the standard error of the mean becomes:",
        "o": ["Double", "Half", "One-fourth", "Unchanged"],
        "a": 1,
        "e": "SE = σ / √n. Multiplying n by 4 multiplies √n by 2, so the SE is halved. Larger samples give more precise estimates of the mean.",
        "topicId": "u1-t07", "subSection": "u1-s1", "diff": 2
    },
    {
        "q": "The second central moment (μ₂) of a distribution is equal to its:",
        "o": ["Mean", "Variance", "Standard deviation", "Coefficient of skewness"],
        "a": 1,
        "e": "μ₂ = Σ(X − X̄)² / N, which is the variance. μ₁ is always zero, μ₃ measures skewness (β₁ = μ₃² / μ₂³) and μ₄ measures kurtosis (β₂ = μ₄ / μ₂²).",
        "topicId": "u1-t08", "subSection": "u1-s1", "diff": 1
    },

    # ---- u1-s2: probability & distributions ----
    {
        "q": "A fair coin is tossed twice. The probability of getting at least one head is:",
        "o": ["1/4", "1/2", "3/4", "1"],
        "a": 2,
        "e": "Sample space = {HH, HT, TH, TT}. Only TT has no head, so P(at least one head) = 1 − 1/4 = 3/4.",
        "topicId": "u1-t09", "subSection": "u1-s2", "diff": 1
    },
    {
        "q": "A and B are independent events with P(A) = 0.5 and P(B) = 0.4. The probability that both occur, P(A ∩ B), is:",
        "o": ["0.2", "0.9", "0.1", "0.45"],
        "a": 0,
        "e": "For independent events, P(A ∩ B) = P(A) × P(B) = 0.5 × 0.4 = 0.2. (P(A ∪ B) would be 0.5 + 0.4 − 0.2 = 0.7.)",
        "topicId": "u1-t09", "subSection": "u1-s2", "diff": 2
    },
    {
        "q": "For a binomial distribution with n = 10 and p = 0.5, the variance is:",
        "o": ["5", "2.5", "1.58", "0.25"],
        "a": 1,
        "e": "Variance = npq = 10 × 0.5 × 0.5 = 2.5 (mean = np = 5, SD = √2.5 = 1.58). In a binomial distribution the variance is always less than the mean.",
        "topicId": "u1-t10", "subSection": "u1-s2", "diff": 2
    },
    {
        "q": "The mean daily milk yield of a herd is 10 kg with SD 2 kg. The standard normal (Z) score of a cow yielding 14 kg is:",
        "o": ["1.0", "2.0", "4.0", "0.5"],
        "a": 1,
        "e": "Z = (X − μ) / σ = (14 − 10) / 2 = 2.0. The cow lies 2 SD above the herd mean — among roughly the top 2.3% of the herd.",
        "topicId": "u1-t11", "subSection": "u1-s2", "diff": 2
    },

    # ---- u1-s3: correlation, regression, sampling ----
    {
        "q": "The correlation coefficient between tick load and daily milk yield in a herd is r = −0.85. This indicates:",
        "o": ["A strong negative (inverse) relationship", "A weak positive relationship", "No relationship", "That ticks cause exactly 85% of the loss in yield"],
        "a": 0,
        "e": "The sign gives the direction (negative: as tick load rises, yield falls) and the size gives the strength (0.85 is strong). Correlation alone does not prove cause, and r² = 0.72 — not 0.85 — is the proportion of variation explained.",
        "topicId": "u1-t12", "subSection": "u1-s3", "diff": 1
    },
    {
        "q": "In ranking 5 bulls by two judges, Σd² = 10. Spearman's rank correlation coefficient is:",
        "o": ["0.5", "0.25", "0.75", "0.9"],
        "a": 0,
        "e": "ρ = 1 − 6Σd² / [n(n² − 1)] = 1 − (6 × 10) / (5 × 24) = 1 − 60/120 = 0.5.",
        "topicId": "u1-t12", "subSection": "u1-s3", "diff": 3
    },
    {
        "q": "The regression equation of body weight (Y) on age (X) is Y = 2 + 0.5X. The predicted Y when X = 10 is:",
        "o": ["7", "5", "12", "2.5"],
        "a": 0,
        "e": "Y = 2 + 0.5 × 10 = 2 + 5 = 7. Here 2 is the intercept and 0.5 is the regression coefficient b_yx (change in Y per unit change in X).",
        "topicId": "u1-t13", "subSection": "u1-s3", "diff": 1
    },
    {
        "q": "The lottery method and tables of random numbers are used for drawing a:",
        "o": ["Simple random sample", "Purposive sample", "Quota sample", "Judgement sample"],
        "a": 0,
        "e": "In simple random sampling every unit has an equal chance of selection, ensured by the lottery method or random number tables (Tippett's, Fisher & Yates). Purposive, quota and judgement samples are non-random.",
        "topicId": "u1-t14", "subSection": "u1-s3", "diff": 1
    },

    # ---- u1-s4: tests of hypothesis, designs, ANOVA, non-parametric ----
    {
        "q": "As the degrees of freedom increase, Student's t-distribution approaches the:",
        "o": ["Normal distribution", "Chi-square distribution", "Poisson distribution", "F-distribution with 1 df"],
        "a": 0,
        "e": "The t-distribution has heavier tails than the normal curve for small samples; with about 30 or more df it is practically identical to the standard normal, which is why the Z-test is used for large samples.",
        "topicId": "u1-t16", "subSection": "u1-s4", "diff": 2
    },
    {
        "q": "In an unpaired (two independent samples) t-test with n₁ = 12 and n₂ = 10 animals, the degrees of freedom are:",
        "o": ["22", "20", "21", "11"],
        "a": 1,
        "e": "df = n₁ + n₂ − 2 = 12 + 10 − 2 = 20. (A paired t-test with n pairs has n − 1 df.)",
        "topicId": "u1-t16", "subSection": "u1-s4", "diff": 2
    },
    {
        "q": "In an F₂ of 160 animals, 100 are dominant and 60 recessive. Tested against the expected 3:1 ratio, the calculated χ² value is:",
        "o": ["13.33", "3.33", "10.00", "6.67"],
        "a": 0,
        "e": "Expected = 120 : 40. χ² = (100 − 120)²/120 + (60 − 40)²/40 = 3.33 + 10.00 = 13.33. This exceeds the table value 3.84 (1 df, 5%), so the fit to 3:1 is rejected.",
        "topicId": "u1-t17", "subSection": "u1-s4", "diff": 3
    },
    {
        "q": "In a Completely Randomized Design with 4 treatments and a total of 20 observations, the error degrees of freedom are:",
        "o": ["16", "19", "3", "15"],
        "a": 0,
        "e": "Total df = N − 1 = 19; treatment df = t − 1 = 3; error df = N − t = 20 − 4 = 16.",
        "topicId": "u1-t19", "subSection": "u1-s4", "diff": 2
    },
    {
        "q": "The non-parametric alternative to the paired t-test is the:",
        "o": ["Wilcoxon signed-rank test", "Kruskal–Wallis H test", "Chi-square test", "F-test"],
        "a": 0,
        "e": "The Wilcoxon signed-rank test compares paired observations without assuming normality. Mann–Whitney U replaces the unpaired t-test; Kruskal–Wallis replaces one-way ANOVA.",
        "topicId": "u1-t20", "subSection": "u1-s4", "diff": 2
    },
    {
        "q": "Which one of the following is NOT a non-parametric test?",
        "o": ["Sign test", "Kruskal–Wallis test", "Student's t-test", "Mann–Whitney U test"],
        "a": 2,
        "e": "Student's t-test is parametric — it assumes normally distributed data. The sign, Kruskal–Wallis and Mann–Whitney tests are distribution-free (non-parametric).",
        "topicId": "u1-t20", "subSection": "u1-s4", "diff": 1
    },

    # ---- u1-s5: computer applications ----
    {
        "q": "Which component of MS-Office is a relational database management system?",
        "o": ["MS-Access", "MS-Word", "MS-PowerPoint", "MS-Paint"],
        "a": 0,
        "e": "MS-Access stores data in related tables and supports queries, forms and reports — suited to herd registers and breeding records. Excel is a spreadsheet, not a true DBMS.",
        "topicId": "u1-t21", "subSection": "u1-s5", "diff": 1
    },
    {
        "q": "The standard protocol used for SENDING e-mail across the internet is:",
        "o": ["SMTP", "HTTP", "FTP", "POP3"],
        "a": 0,
        "e": "SMTP (Simple Mail Transfer Protocol) sends mail; POP3 and IMAP retrieve it; HTTP transfers web pages; FTP transfers files.",
        "topicId": "u1-t22", "subSection": "u1-s5", "diff": 2
    },
]

exam_unit1_tf = [
    {
        "q": "A parameter is a numerical value calculated from a sample.",
        "a": False,
        "e": "False. A parameter describes the whole population (μ, σ); a statistic is computed from a sample (x̄, s) and is used to estimate the parameter.",
        "topicId": "u1-t03", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "The median is not affected by extreme values (outliers) in the data.",
        "a": True,
        "e": "True. The median depends only on the middle position, so one very high-yielding cow barely moves it, whereas the arithmetic mean is pulled strongly toward extreme values.",
        "topicId": "u1-t05", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "Range is the simplest measure of dispersion and depends only on the two extreme observations.",
        "a": True,
        "e": "True. Range = largest − smallest value. Because it ignores all the middle values, it is easily distorted by a single outlier.",
        "topicId": "u1-t06", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "The classical (a priori) definition of probability assumes that all the possible outcomes are equally likely.",
        "a": True,
        "e": "True. Classical probability = favourable cases ÷ total equally likely cases (e.g., 1/6 for a die). When outcomes are not equally likely, the relative-frequency (empirical) definition is used.",
        "topicId": "u1-t09", "subSection": "u1-s2", "diff": 1
    },
    {
        "q": "The Poisson distribution is a continuous probability distribution.",
        "a": False,
        "e": "False. Poisson (like binomial) is a discrete distribution of counts — 0, 1, 2 … rare events. The normal distribution is continuous.",
        "topicId": "u1-t10", "subSection": "u1-s2", "diff": 1
    },
    {
        "q": "When r = ±1 (perfect correlation), the two regression lines coincide.",
        "a": True,
        "e": "True. With perfect correlation both lines are the same line. As r moves toward 0 the angle between them widens, and at r = 0 they are perpendicular.",
        "topicId": "u1-t13", "subSection": "u1-s3", "diff": 2
    },
    {
        "q": "Replication in an experiment makes it possible to estimate the experimental error and increases precision.",
        "a": True,
        "e": "True. Without replication there is no estimate of error variance and no valid test of significance; more replicates reduce the standard error of treatment means.",
        "topicId": "u1-t18", "subSection": "u1-s4", "diff": 1
    },
    {
        "q": "In MS-Excel, every formula must begin with an equal (=) sign.",
        "a": True,
        "e": "True. Typing =AVERAGE(B2:B21) returns a result; without the '=' Excel treats the entry as plain text.",
        "topicId": "u1-t22", "subSection": "u1-s5", "diff": 1
    },
    {
        "q": "The Chi-square test should be applied to actual frequencies (counts), not to percentages or proportions.",
        "a": True,
        "e": "True. χ² = Σ(O − E)² / E is valid only for absolute frequencies; converting counts to percentages distorts the statistic.",
        "topicId": "u1-t17", "subSection": "u1-s4", "diff": 2
    },
    {
        "q": "A Randomized Block Design is preferred over CRD when the experimental material is heterogeneous in one direction.",
        "a": True,
        "e": "True. RBD groups units into homogeneous blocks (local control) to remove one source of variation. CRD suits fully homogeneous material; Latin square removes two sources.",
        "topicId": "u1-t18", "subSection": "u1-s4", "diff": 2
    },
    {
        "q": "The calculated value of F in an analysis of variance can never be negative.",
        "a": True,
        "e": "True. F is a ratio of two mean squares (variances), both of which are sums of squares divided by df and therefore never negative.",
        "topicId": "u1-t19", "subSection": "u1-s4", "diff": 2
    },
    {
        "q": "A Local Area Network (LAN) connects computers spread across different countries.",
        "a": False,
        "e": "False. A LAN covers a small area such as a building or campus. Networks spanning cities, countries or continents are Wide Area Networks (WAN); the internet is the largest WAN.",
        "topicId": "u1-t22", "subSection": "u1-s5", "diff": 1
    },
]

exam_unit1_fib = [
    {
        "q": "The systematic arrangement of classified data in rows and columns is called ______.",
        "a": ["tabulation"],
        "a_display": "Tabulation",
        "e": "Tabulation follows classification: it presents data in rows (stubs) and columns (captions) for easy comparison.",
        "topicId": "u1-t02", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "The graph obtained by joining the mid-points of the tops of the rectangles of a histogram is called a frequency ______.",
        "a": ["polygon"],
        "a_display": "Polygon",
        "e": "Joining the mid-points of histogram bars gives the frequency polygon; smoothing it gives the frequency curve.",
        "topicId": "u1-t04", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "The individual measurement recorded on each experimental unit (e.g., the weight of one calf) is called an ______.",
        "a": ["observation"],
        "a_display": "Observation",
        "e": "An observation is a single recorded value of a variable; many observations together form the data from which statistics are computed.",
        "topicId": "u1-t03", "subSection": "u1-s1", "diff": 1
    },
    {
        "q": "The mean deviation is the least when deviations are measured from the ______.",
        "a": ["median"],
        "a_display": "Median",
        "e": "The sum of absolute deviations is minimum about the median; the sum of SQUARED deviations is minimum about the arithmetic mean.",
        "topicId": "u1-t06", "subSection": "u1-s1", "diff": 2
    },
    {
        "q": "When the null hypothesis is rejected, the hypothesis that is accepted is called the ______ hypothesis.",
        "a": ["alternative", "alternate", "H1", "H₁"],
        "a_display": "Alternative (H₁)",
        "e": "H₁ (alternative hypothesis) states that a real difference exists; it may be two-tailed (≠) or one-tailed (> or <).",
        "topicId": "u1-t15", "subSection": "u1-s4", "diff": 1
    },
    {
        "q": "Because it was developed by Carl Friedrich Gauss, the normal distribution is also called the ______ distribution.",
        "a": ["Gaussian", "Gauss"],
        "a_display": "Gaussian",
        "e": "De Moivre first described the normal curve; Laplace and Gauss developed it for errors of observation, so it is also called the Gaussian curve or normal curve of error.",
        "topicId": "u1-t11", "subSection": "u1-s2", "diff": 1
    },
    {
        "q": "In an MS-Excel worksheet, the box formed by the intersection of a row and a column is called a ______.",
        "a": ["cell"],
        "a_display": "Cell",
        "e": "Each cell has an address such as B4 (column B, row 4); data and formulas are entered cell by cell.",
        "topicId": "u1-t22", "subSection": "u1-s5", "diff": 1
    },
    {
        "q": "A complete list of all the units of a population from which a sample is drawn is called the sampling ______.",
        "a": ["frame"],
        "a_display": "Frame",
        "e": "The sampling frame (e.g., the register of all animals in a district) must be complete and up to date for random sampling to be valid.",
        "topicId": "u1-t14", "subSection": "u1-s3", "diff": 2
    },
    {
        "q": "In a Chi-square goodness-of-fit test with k classes (and no parameter estimated from the data), the degrees of freedom are k − ______.",
        "a": ["1", "one"],
        "a_display": "1",
        "e": "df = k − 1. One further df is lost for each parameter estimated from the data (e.g., k − 2 when the gene frequency is estimated when testing Mendelian or H–W ratios with 3 classes).",
        "topicId": "u1-t17", "subSection": "u1-s4", "diff": 2
    },
    {
        "q": "In one-way ANOVA, the total sum of squares is partitioned into the treatment sum of squares and the ______ sum of squares.",
        "a": ["error", "residual", "error or residual", "within"],
        "a_display": "Error (residual / within-group)",
        "e": "Total SS = Treatment (between-group) SS + Error (within-group, residual) SS. In RBD a block SS is also separated out.",
        "topicId": "u1-t19", "subSection": "u1-s4", "diff": 2
    },
    {
        "q": "The Wilcoxon, Mann–Whitney and Kruskal–Wallis tests are called ______ tests because they make no assumption about the shape of the population distribution.",
        "a": ["non-parametric", "nonparametric", "non parametric", "distribution-free", "distribution free"],
        "a_display": "Non-parametric (distribution-free)",
        "e": "Non-parametric tests work on ranks or signs and do not assume normality, which makes them suitable for small samples and ordinal data.",
        "topicId": "u1-t20", "subSection": "u1-s4", "diff": 1
    },
    {
        "q": "The MS-Office application used to create slide-show presentations is Microsoft ______.",
        "a": ["PowerPoint", "Power Point"],
        "a_display": "PowerPoint",
        "e": "Word is for documents, Excel for spreadsheets and statistical analysis, PowerPoint for presentations, and Access for databases.",
        "topicId": "u1-t22", "subSection": "u1-s5", "diff": 1
    },
]

# ============================================================
# UNIT 2 — PRINCIPLES OF ANIMAL AND POPULATION GENETICS
# ============================================================
exam_unit2_mcq = [
    # ---- u2-s1: Mendelian genetics, gene interaction, pleiotropy, alleles ----
    {
        "q": "Thomas Hunt Morgan's experiments on Drosophila established the principle of:",
        "o": ["Linkage and sex-linked inheritance", "Independent assortment", "Operon model of gene regulation", "Hardy–Weinberg equilibrium"],
        "a": 0,
        "e": "Morgan (Nobel Prize 1933) showed with the white-eye mutant of Drosophila that genes lie on chromosomes, are linked, and can be sex-linked.",
        "topicId": "u2-t01", "subSection": "u2-s1", "diff": 1
    },
    {
        "q": "In a dihybrid cross (AaBb × AaBb), what proportion of the F₂ is homozygous at BOTH loci?",
        "o": ["1/16", "4/16", "9/16", "6/16"],
        "a": 1,
        "e": "Homozygous for both: AABB, AAbb, aaBB and aabb — 4 of 16 = 1/4. (Each has probability 1/4 × 1/4 = 1/16.)",
        "topicId": "u2-t04", "subSection": "u2-s1", "diff": 3
    },
    {
        "q": "A modified dihybrid F₂ ratio of 15:1 indicates:",
        "o": ["Duplicate dominant genes", "Complementary genes", "Dominant epistasis", "Supplementary genes"],
        "a": 0,
        "e": "15:1 arises when a dominant allele at either locus gives the same phenotype (duplicate gene action); only aabb shows the other phenotype. Complementary = 9:7, dominant epistasis = 12:3:1, supplementary (recessive epistasis) = 9:3:4.",
        "topicId": "u2-t06", "subSection": "u2-s1", "diff": 2
    },
    {
        "q": "When only 70% of animals carrying a dominant gene show the corresponding phenotype, the gene is said to show:",
        "o": ["Incomplete penetrance", "Variable expressivity", "Pleiotropy", "Codominance"],
        "a": 0,
        "e": "Penetrance is the percentage of individuals with a genotype that express the phenotype at all; here it is 70% (incomplete). Expressivity is the degree of expression among those that do show it.",
        "topicId": "u2-t07", "subSection": "u2-s1", "diff": 1
    },
    {
        "q": "Coat colour in rabbits (full colour C, chinchilla c^ch, Himalayan c^h and albino c) is a classic example of:",
        "o": ["Multiple alleles", "Polygenic inheritance", "Epistasis", "Linkage"],
        "a": 0,
        "e": "Four alleles at the same C locus form a dominance series C > c^ch > c^h > c. A diploid animal carries only two of them, but the population carries all four.",
        "topicId": "u2-t08", "subSection": "u2-s1", "diff": 1
    },
    {
        "q": "How many different genotypes are possible at a locus with 4 multiple alleles?",
        "o": ["10", "8", "16", "6"],
        "a": 0,
        "e": "Number of genotypes = n(n + 1)/2 = 4 × 5 / 2 = 10 (4 homozygotes + 6 heterozygotes).",
        "topicId": "u2-t08", "subSection": "u2-s1", "diff": 2
    },

    # ---- u2-s2: cell division, chromosomes, sex, linkage, mutation, aberrations ----
    {
        "q": "The reduction of chromosome number from diploid to haploid takes place during:",
        "o": ["Meiosis I", "Meiosis II", "Mitosis", "Interphase"],
        "a": 0,
        "e": "Homologous chromosomes separate at anaphase I, so meiosis I is the reductional division. Meiosis II separates sister chromatids and is equational, like mitosis.",
        "topicId": "u2-t02", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "Chiasmata between homologous chromosomes first become clearly visible during:",
        "o": ["Diplotene", "Leptotene", "Zygotene", "Diakinesis"],
        "a": 0,
        "e": "Prophase I: leptotene (threads) → zygotene (synapsis) → pachytene (crossing over) → diplotene (homologues repel; chiasmata visible) → diakinesis (terminalisation of chiasmata).",
        "topicId": "u2-t02", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "The diploid chromosome number (2n) of the domestic pig (Sus scrofa domesticus) is:",
        "o": ["38", "40", "54", "60"],
        "a": 0,
        "e": "Pig 2n = 38 (the same number as the cat). Sheep 54, cattle and goat 60, horse 64, dog and chicken 78.",
        "topicId": "u2-t03", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "How many Barr bodies are seen in the somatic cells of an XXY individual?",
        "o": ["1", "0", "2", "3"],
        "a": 0,
        "e": "Number of Barr bodies = number of X chromosomes − 1. An XXY (Klinefelter-type) individual therefore has one Barr body despite being phenotypically male.",
        "topicId": "u2-t09", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "Which of the following is an example of a sex-LIMITED trait?",
        "o": ["Egg production in poultry", "Haemophilia A in dogs", "Scurs in cattle", "Roan coat colour in Shorthorn cattle"],
        "a": 0,
        "e": "Sex-limited traits are expressed in only one sex although both carry the genes (egg production, milk yield). Haemophilia A is sex-linked, scurs is sex-influenced and roan is codominance.",
        "topicId": "u2-t10", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "The barring gene used for auto-sexing day-old chicks is located on the:",
        "o": ["Z chromosome", "W chromosome", "An autosome", "Mitochondrial DNA"],
        "a": 0,
        "e": "Barring (B) is Z-linked. Males are ZZ and females ZW, so a non-barred cock × barred hen cross gives barred males and non-barred females that can be sexed at hatch.",
        "topicId": "u2-t10", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "If the coefficient of coincidence in a three-point test cross is 0.3, the interference is:",
        "o": ["0.7", "0.3", "1.3", "0.09"],
        "a": 0,
        "e": "Interference = 1 − coefficient of coincidence = 1 − 0.3 = 0.7. Coincidence = observed double crossovers ÷ expected double crossovers.",
        "topicId": "u2-t11", "subSection": "u2-s2", "diff": 3
    },
    {
        "q": "Replacement of one purine by another purine (e.g., A → G) in DNA is called a:",
        "o": ["Transition", "Transversion", "Frameshift mutation", "Deletion"],
        "a": 0,
        "e": "Transition = purine ↔ purine or pyrimidine ↔ pyrimidine. Transversion = purine ↔ pyrimidine. Both are point (substitution) mutations.",
        "topicId": "u2-t12", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "Insertion or deletion of a single base pair within the coding sequence of a gene produces a:",
        "o": ["Frameshift mutation", "Silent mutation", "Transition", "Missense mutation only"],
        "a": 0,
        "e": "Adding or removing one base shifts the triplet reading frame, so every codon downstream is misread — usually producing a non-functional protein.",
        "topicId": "u2-t12", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "Ultraviolet (UV) radiation causes mutation mainly by forming:",
        "o": ["Thymine (pyrimidine) dimers", "Double-strand breaks only", "Base analogues", "Deamination of cytosine"],
        "a": 0,
        "e": "UV light links adjacent pyrimidines (mainly thymine–thymine) on the same strand into dimers that distort the helix. Ionising radiation (X-rays, gamma rays) causes strand breaks.",
        "topicId": "u2-t12", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "A chromosomal inversion in which the inverted segment INCLUDES the centromere is called:",
        "o": ["Pericentric inversion", "Paracentric inversion", "Reciprocal translocation", "Isochromosome"],
        "a": 0,
        "e": "Pericentric inversions include the centromere and can change arm ratio; paracentric inversions lie entirely within one arm.",
        "topicId": "u2-t13", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "For karyotyping, dividing cells are arrested at metaphase by treating the culture with:",
        "o": ["Colchicine", "Phytohaemagglutinin", "Trypsin", "Giemsa"],
        "a": 0,
        "e": "Colchicine (or colcemid) inhibits spindle formation and arrests cells at metaphase, when chromosomes are most condensed. PHA stimulates lymphocytes to divide; trypsin and Giemsa are used for G-banding.",
        "topicId": "u2-t14", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "Which feature distinguishes extra-chromosomal (cytoplasmic) inheritance from Mendelian inheritance?",
        "o": ["Reciprocal crosses give different results", "Traits segregate in a 3:1 ratio", "Genes are located on autosomes", "Both parents contribute equally"],
        "a": 0,
        "e": "Cytoplasmic genes (e.g., mitochondrial DNA) come mainly through the egg, so reciprocal crosses differ and the trait follows the mother. Mendelian ratios are not obtained.",
        "topicId": "u2-t15", "subSection": "u2-s2", "diff": 2
    },

    # ---- u2-s3: molecular genetics ----
    {
        "q": "A double-stranded DNA sample contains 20% adenine. Its cytosine content is:",
        "o": ["30%", "20%", "40%", "60%"],
        "a": 0,
        "e": "Chargaff's rule: A = T and G = C. A + T = 40%, so G + C = 60%, giving C = 30%.",
        "topicId": "u2-t16", "subSection": "u2-s3", "diff": 2
    },

    # ---- u2-s4: population genetics ----
    {
        "q": "The mathematical foundations of population genetics were laid mainly by:",
        "o": ["R. A. Fisher, J. B. S. Haldane and Sewall Wright", "Mendel, Morgan and Bateson", "Watson, Crick and Wilkins", "Darwin, Lamarck and Wallace"],
        "a": 0,
        "e": "Fisher, Haldane and Wright (1918–1932) combined Mendelian genetics with natural selection, founding population and quantitative genetics.",
        "topicId": "u2-t19", "subSection": "u2-s4", "diff": 1
    },
    {
        "q": "Selection against a completely recessive gene becomes very slow when its frequency (q) is low because:",
        "o": ["Most recessive alleles are carried, hidden, in heterozygotes", "The mutation rate becomes very high", "Heterozygotes are always culled", "Dominant alleles are lost by drift"],
        "a": 0,
        "e": "When q is small, q² (affected animals) is tiny while 2pq (carriers) is far larger, so culling affected animals removes very few alleles. Carrier detection (test mating, DNA tests) is needed to eliminate such genes.",
        "topicId": "u2-t22", "subSection": "u2-s4", "diff": 2
    },
    {
        "q": "In a population in Hardy–Weinberg equilibrium, 4% of calves show a recessive defect (aa). The frequency of carriers (Aa) is:",
        "o": ["0.32", "0.16", "0.04", "0.64"],
        "a": 0,
        "e": "q² = 0.04 → q = 0.2, p = 0.8. Carriers = 2pq = 2 × 0.8 × 0.2 = 0.32 — eight times as many carriers as affected calves.",
        "topicId": "u2-t21", "subSection": "u2-s4", "diff": 3
    },
    {
        "q": "For a sex-linked gene whose frequencies differ between males and females, Hardy–Weinberg equilibrium is attained:",
        "o": ["Gradually, with oscillation over several generations", "In a single generation of random mating", "Never, under random mating", "Only after selection is applied"],
        "a": 0,
        "e": "With sex-linked genes, the difference in gene frequency between the sexes halves (and changes sign) each generation, so equilibrium is approached gradually — unlike autosomal genes, which reach it in one generation.",
        "topicId": "u2-t21", "subSection": "u2-s4", "diff": 3
    },

    # ---- u2-s5: quantitative genetics ----
    {
        "q": "The polygenic (multiple factor) inheritance of quantitative traits was first demonstrated by Nilsson-Ehle using:",
        "o": ["Kernel colour in wheat", "Seed shape in pea", "Eye colour in Drosophila", "Comb shape in poultry"],
        "a": 0,
        "e": "Nilsson-Ehle (1909) showed that several genes with small, additive effects produce the graded kernel colours in wheat — the basis of the multiple factor hypothesis.",
        "topicId": "u2-t23", "subSection": "u2-s5", "diff": 2
    },
    {
        "q": "Genotype × environment (G × E) interaction is said to exist when:",
        "o": ["The relative performance of genotypes changes from one environment to another", "All genotypes perform equally in every environment", "Environment has no effect on phenotype", "Genotypic and environmental values are correlated"],
        "a": 0,
        "e": "G × E means genotypes rank or differ differently across environments — e.g., an exotic crossbred superior on an organised farm but not under village conditions. Genotype–environment correlation is a different concept.",
        "topicId": "u2-t26", "subSection": "u2-s5", "diff": 2
    },
]

exam_unit2_tf = [
    {
        "q": "The chromosome theory of inheritance was proposed by Sutton and Boveri.",
        "a": True,
        "e": "True. Sutton and Boveri (1902–03) independently noted that chromosome behaviour in meiosis parallels Mendel's factors; Morgan later proved it experimentally.",
        "topicId": "u2-t01", "subSection": "u2-s1", "diff": 1
    },
    {
        "q": "Sister chromatids separate during anaphase I of meiosis.",
        "a": False,
        "e": "False. Homologous chromosomes separate at anaphase I; sister chromatids separate at anaphase II (and at mitotic anaphase).",
        "topicId": "u2-t02", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "The domestic fowl has a diploid number of 78, including many small microchromosomes.",
        "a": True,
        "e": "True. The chicken karyotype (2n = 78) has a few macrochromosomes and many tiny microchromosomes; sex chromosomes are ZZ (male) and ZW (female).",
        "topicId": "u2-t03", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "Mendel's law of independent assortment holds for genes located on different (non-homologous) chromosomes.",
        "a": True,
        "e": "True. Genes on different chromosomes (or far apart on one) assort independently; closely linked genes do not, which is why Mendel's 9:3:3:1 fails for them.",
        "topicId": "u2-t04", "subSection": "u2-s1", "diff": 1
    },
    {
        "q": "Expressivity refers to the degree or intensity with which a penetrant gene is expressed in different individuals.",
        "a": True,
        "e": "True. Penetrance asks whether the trait appears at all; expressivity asks how strongly it appears among the individuals that show it.",
        "topicId": "u2-t07", "subSection": "u2-s1", "diff": 1
    },
    {
        "q": "Sex-linked recessive traits appear more frequently in the heterogametic sex.",
        "a": True,
        "e": "True. The heterogametic sex (XY males in mammals, ZW females in birds) is hemizygous, so a single recessive allele is expressed — e.g., haemophilia A in male dogs.",
        "topicId": "u2-t10", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "Polyploidy is more common in animals than in plants.",
        "a": False,
        "e": "False. Polyploidy is common in plants (wheat, banana) but rare in animals, because it disturbs sex-chromosome balance and meiosis; in livestock it usually causes embryonic death.",
        "topicId": "u2-t13", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "Most spontaneous gene mutations are recessive and harmful to the organism.",
        "a": True,
        "e": "True. Random changes rarely improve a well-adapted gene, and most loss-of-function mutations are recessive — so they hide in carriers and appear on inbreeding.",
        "topicId": "u2-t12", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "The genetic correlation between two traits can be negative.",
        "a": True,
        "e": "True. r_G ranges from −1 to +1. For example, milk yield and fat percentage are negatively correlated genetically, so selection for yield tends to lower fat %.",
        "topicId": "u2-t29", "subSection": "u2-s5", "diff": 1
    },
    {
        "q": "Population genetics studies the genetic make-up of groups of individuals rather than the offspring of single matings.",
        "a": True,
        "e": "True. Mendelian genetics predicts the progeny of individual crosses; population genetics deals with gene and genotype frequencies of whole populations and the forces that change them.",
        "topicId": "u2-t19", "subSection": "u2-s4", "diff": 1
    },
    {
        "q": "Mutation alone can change gene frequencies rapidly within a few generations.",
        "a": False,
        "e": "False. Mutation rates are very low (about 10⁻⁵ to 10⁻⁶ per locus per generation), so recurrent mutation changes gene frequency extremely slowly; it mainly supplies the raw variation.",
        "topicId": "u2-t22", "subSection": "u2-s4", "diff": 2
    },
    {
        "q": "Dominance deviation is transmitted from parent to offspring and is the basis of predicting breeding value.",
        "a": False,
        "e": "False. Parents pass on genes, not genotypes, so dominance and epistatic deviations are recreated anew each generation. Breeding value depends only on the additive (average) effects of genes.",
        "topicId": "u2-t25", "subSection": "u2-s5", "diff": 2
    },
]

exam_unit2_fib = [
    {
        "q": "The direction of shell coiling in the snail Limnaea, decided by the mother's genotype rather than the offspring's own, is a classic example of maternal ______.",
        "a": ["effect", "effects", "inheritance"],
        "a_display": "Effect",
        "e": "In maternal effect the offspring's phenotype follows the mother's nuclear genotype (via substances in the egg), so the ratio appears one generation late. It differs from true cytoplasmic (mitochondrial) inheritance.",
        "topicId": "u2-t15", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "Because it halves the chromosome number, meiosis I is called the ______ division.",
        "a": ["reductional", "reduction"],
        "a_display": "Reductional",
        "e": "Meiosis I is reductional (2n → n); meiosis II is equational, like mitosis.",
        "topicId": "u2-t02", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "The diploid chromosome number of the horse (Equus caballus) is ______.",
        "a": ["64", "2n = 64", "2n=64"],
        "a_display": "64",
        "e": "Horse 2n = 64 and donkey 2n = 62, so the mule has 63 chromosomes — the unpaired set disrupts meiosis and makes it sterile.",
        "topicId": "u2-t03", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "The pentose sugar present in RNA is ______.",
        "a": ["ribose", "D-ribose"],
        "a_display": "Ribose",
        "e": "RNA contains ribose (with a 2′-OH group) and uracil; DNA contains deoxyribose and thymine.",
        "topicId": "u2-t16", "subSection": "u2-s3", "diff": 1
    },
    {
        "q": "A point mutation that changes an amino-acid codon into a stop codon, producing a truncated protein, is called a ______ mutation.",
        "a": ["nonsense"],
        "a_display": "Nonsense",
        "e": "Nonsense mutations create UAA, UAG or UGA in the reading frame. A missense mutation substitutes one amino acid; a silent mutation changes no amino acid.",
        "topicId": "u2-t12", "subSection": "u2-s2", "diff": 2
    },
    {
        "q": "The term 'mutation' was coined by Hugo ______ from his work on Oenothera lamarckiana.",
        "a": ["de Vries", "Vries", "deVries"],
        "a_display": "de Vries",
        "e": "Hugo de Vries (1901) proposed the mutation theory from sudden heritable changes he saw in the evening primrose.",
        "topicId": "u2-t12", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "An aneuploid with chromosome constitution 2n + 1 is called a ______.",
        "a": ["trisomic", "trisomy", "trisome"],
        "a_display": "Trisomic (trisomy)",
        "e": "2n + 1 = trisomy, 2n − 1 = monosomy, 2n − 2 = nullisomy, 2n + 2 = tetrasomy.",
        "topicId": "u2-t13", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "The systematic arrangement of metaphase chromosomes in homologous pairs by size and centromere position is called a ______.",
        "a": ["karyotype", "karyogram", "idiogram"],
        "a_display": "Karyotype (karyogram)",
        "e": "A karyotype is used to detect numerical and structural aberrations (e.g., the 1/29 translocation) in breeding bulls. A diagrammatic karyotype is an idiogram.",
        "topicId": "u2-t14", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "Mitochondrial DNA is inherited almost exclusively through the ______.",
        "a": ["mother", "dam", "female", "maternal line", "egg", "ovum"],
        "a_display": "Mother (dam)",
        "e": "Mitochondria come from the egg's cytoplasm; sperm mitochondria are destroyed after fertilisation. mtDNA is therefore used to trace maternal lineages and domestication origins.",
        "topicId": "u2-t15", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "An individual carrying three complete sets of chromosomes (3n) is called a ______.",
        "a": ["triploid"],
        "a_display": "Triploid",
        "e": "Euploidy changes whole sets (3n triploid, 4n tetraploid); aneuploidy changes single chromosomes (2n + 1, 2n − 1).",
        "topicId": "u2-t13", "subSection": "u2-s2", "diff": 1
    },
    {
        "q": "Traits governed by many genes, each with a small additive effect, and showing continuous variation are called ______ traits.",
        "a": ["polygenic", "quantitative", "metric", "polygenic or quantitative"],
        "a_display": "Polygenic (quantitative)",
        "e": "Milk yield, body weight and growth rate are polygenic traits; they are measured, not classified, and are strongly affected by environment.",
        "topicId": "u2-t23", "subSection": "u2-s5", "diff": 1
    },
    {
        "q": "Heritability in the broad sense is the ratio of genotypic variance (V_G) to ______ variance.",
        "a": ["phenotypic", "VP", "V_P", "Vp", "total phenotypic"],
        "a_display": "Phenotypic (V_P)",
        "e": "Broad sense H² = V_G / V_P. Narrow sense h² = V_A / V_P, which is the one used to predict response to selection.",
        "topicId": "u2-t25", "subSection": "u2-s5", "diff": 1
    },
]

# ============================================================
# UNIT 3 — PRINCIPLES OF ANIMAL BREEDING
# ============================================================
exam_unit3_mcq = [
    # ---- u3-s1: history, breeds, economic traits, selection ----
    {
        "q": "The world's first herd book, Coates' Herd Book (1822), was opened for which breed?",
        "o": ["Shorthorn cattle", "Holstein-Friesian cattle", "Jersey cattle", "Thoroughbred horse"],
        "a": 0,
        "e": "Coates' Herd Book (1822) recorded Shorthorn pedigrees. Herd books fixed breed identity and made pedigree selection possible. (The Thoroughbred has a General Stud Book, begun in 1791.)",
        "topicId": "u3-t01", "subSection": "u3-s1", "diff": 2
    },
    {
        "q": "On the basis of utility, the Sahiwal breed of cattle is classified as a:",
        "o": ["Milch breed", "Draught breed", "Dual-purpose breed", "Beef breed"],
        "a": 0,
        "e": "Milch (dairy) breeds: Sahiwal, Gir, Red Sindhi, Rathi. Dual-purpose: Hariana, Tharparkar, Kankrej, Ongole. Draught: Hallikar, Amritmahal, Khillar, Kangayam, Nagori.",
        "topicId": "u3-t02", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "The Hariana breed of cattle is classified as a:",
        "o": ["Dual-purpose breed", "Milch breed", "Draught breed", "Beef breed"],
        "a": 0,
        "e": "Hariana cows are fair milkers and the bullocks are good draught animals, so Hariana is a dual-purpose breed.",
        "topicId": "u3-t02", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "Which of the following is a typical DRAUGHT breed of Indian cattle?",
        "o": ["Hallikar", "Gir", "Red Sindhi", "Sahiwal"],
        "a": 0,
        "e": "Hallikar (Karnataka) belongs to the Mysore type of draught breeds with Amritmahal and Khillar. Gir, Red Sindhi and Sahiwal are milch breeds.",
        "topicId": "u3-t02", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "The home tract of the Murrah buffalo is:",
        "o": ["Haryana (Rohtak, Hisar, Jind)", "Gujarat (Saurashtra)", "Punjab (Ferozpur – Nili-Ravi tract)", "Andhra Pradesh (Guntur)"],
        "a": 0,
        "e": "Murrah — the best Indian dairy buffalo, with tightly curled horns — comes from Rohtak, Hisar and Jind in Haryana. Jaffarabadi is from Gujarat, Nili-Ravi from Punjab.",
        "topicId": "u3-t02", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "The economically ideal calving interval in dairy cattle is about:",
        "o": ["12–13 months", "18–20 months", "24 months", "8–9 months"],
        "a": 0,
        "e": "A 12–13 month calving interval (one calf a year) maximises lifetime milk and calves. It depends on the service period, since gestation is about 280 days.",
        "topicId": "u3-t03", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "The heritability of lactation milk yield is 0.3 and the selection differential is 400 kg. The expected response to selection per generation is:",
        "o": ["120 kg", "400 kg", "133 kg", "1333 kg"],
        "a": 0,
        "e": "R = h² × S = 0.3 × 400 = 120 kg. Only the heritable part of the selection differential is passed on to the next generation.",
        "topicId": "u3-t04", "subSection": "u3-s1", "diff": 2
    },
    {
        "q": "In a selection index, each trait is weighted according to its:",
        "o": ["Relative economic value, heritability and genetic/phenotypic correlations", "Phenotypic mean only", "Order of measurement", "Number of records only"],
        "a": 0,
        "e": "Hazel's index I = b₁P₁ + b₂P₂ + … uses weights derived from economic values, heritabilities and genetic and phenotypic (co)variances, making it the most efficient multi-trait method.",
        "topicId": "u3-t07", "subSection": "u3-s1", "diff": 2
    },
    {
        "q": "Pedigree selection is most useful when:",
        "o": ["The animal is young and has no performance record of its own", "The trait is highly heritable and recorded early in both sexes", "Many progeny records are already available", "Ancestors are more than five generations away"],
        "a": 0,
        "e": "Pedigree information lets breeders choose young animals (e.g., bull calves for milk yield) before their own or progeny records exist. Close ancestors (parents, grandparents) carry most of the value.",
        "topicId": "u3-t05", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "Indirect selection for trait X through a correlated trait Y is more effective than direct selection when:",
        "o": ["Y has a higher heritability than X and the genetic correlation between them is high", "The genetic correlation between X and Y is zero", "X is easy and cheap to measure early in life", "Y has lower heritability than X"],
        "a": 0,
        "e": "Correlated response exceeds direct response when i_Y · h_Y · r_G > i_X · h_X — i.e., Y is more heritable, strongly genetically correlated with X, or measurable earlier or more intensely.",
        "topicId": "u3-t06", "subSection": "u3-s1", "diff": 3
    },

    # ---- u3-s2: mating systems, inbreeding, outbreeding, heterosis ----
    {
        "q": "Mating of individuals that resemble each other phenotypically more closely than the population average is called:",
        "o": ["Positive assortative mating", "Negative assortative mating", "Inbreeding", "Random mating"],
        "a": 0,
        "e": "Positive assortative mating (like × like, phenotypically) increases variance and homozygosity for the trait without the animals being related. Inbreeding refers to genetic relationship.",
        "topicId": "u3-t08", "subSection": "u3-s2", "diff": 1
    },
    {
        "q": "The synthetic crossbred cattle 'Vrindavani' was developed at:",
        "o": ["ICAR-IVRI, Izatnagar", "ICAR-NDRI, Karnal", "ICAR-CIRC, Meerut", "Kerala Livestock Development Board"],
        "a": 0,
        "e": "Vrindavani (IVRI) combines Holstein-Friesian, Brown Swiss and Jersey with Hariana. Karan Fries and Karan Swiss are NDRI; Frieswal is CIRC (Military Farms); Sunandini is Kerala.",
        "topicId": "u3-t19", "subSection": "u3-s3", "diff": 2
    },
    {
        "q": "Crossbreeding in which purebred sires of two breeds are used alternately in successive generations is called:",
        "o": ["Criss-crossing", "Grading up", "Topcrossing", "Backcrossing"],
        "a": 0,
        "e": "Criss-crossing is two-breed rotational crossing; bringing in a third breed makes it triple crossing or three-breed rotation.",
        "topicId": "u3-t11", "subSection": "u3-s2", "diff": 1
    },
    {
        "q": "The mean 6-month body weights of two parental breeds are 200 kg and 300 kg, and their F₁ cross averages 275 kg. The percentage heterosis is:",
        "o": ["10%", "37.5%", "8.3%", "25%"],
        "a": 0,
        "e": "Mid-parent = (200 + 300)/2 = 250 kg. Heterosis % = (F₁ − MP) / MP × 100 = (275 − 250)/250 × 100 = 10%.",
        "topicId": "u3-t12", "subSection": "u3-s2", "diff": 2
    },
    {
        "q": "On inter se mating of F₁ crossbreds, the F₂ generation retains what proportion of the heterosis seen in the F₁?",
        "o": ["50%", "100%", "25%", "0%"],
        "a": 0,
        "e": "Heterozygosity — and so heterosis from dominance — is halved from F₁ to F₂. This is why rotational crossbreeding or fresh F₁ production is used to keep it.",
        "topicId": "u3-t12", "subSection": "u3-s2", "diff": 2
    },
    {
        "q": "General combining ability (GCA) and specific combining ability (SCA) mainly reflect, respectively:",
        "o": ["Additive and non-additive gene action", "Non-additive and additive gene action", "Environmental and genetic effects", "Maternal and paternal effects"],
        "a": 0,
        "e": "GCA (average performance of a line in crosses) comes from additive effects; SCA (the extra performance of a particular cross) comes from dominance and epistasis. RRS improves both.",
        "topicId": "u3-t13", "subSection": "u3-s2", "diff": 2
    },

    # ---- u3-s3: breeding strategies, sire evaluation, new breeds ----
    {
        "q": "'Wall eyes' (whitish, walled eyes) are a characteristic feature of which buffalo breed?",
        "o": ["Nili-Ravi", "Murrah", "Mehsana", "Surti"],
        "a": 0,
        "e": "Nili-Ravi (Punjab) buffaloes typically have wall eyes and white markings on the forehead, face, legs and tail switch ('panch kalyani').",
        "topicId": "u3-t14", "subSection": "u3-s3", "diff": 1
    },
    {
        "q": "The Jamunapari goat, noted for its Roman nose and long pendulous ears, originates from:",
        "o": ["Etawah district, Uttar Pradesh", "Barmer, Rajasthan", "West Bengal", "Kutch, Gujarat"],
        "a": 0,
        "e": "Jamunapari (Chakarnagar, Etawah, UP) is a large dual-purpose milk and meat goat. Black Bengal is the prolific meat goat of West Bengal.",
        "topicId": "u3-t15", "subSection": "u3-s3", "diff": 1
    },
    {
        "q": "Kadaknath, an indigenous chicken breed famous for its black meat, belongs to:",
        "o": ["Madhya Pradesh (Jhabua and Dhar)", "Assam", "Andhra Pradesh", "Kerala"],
        "a": 0,
        "e": "Kadaknath ('Kali Masi') has fibromelanosis — black skin, flesh and bones — and holds a GI tag for Jhabua, Madhya Pradesh.",
        "topicId": "u3-t16", "subSection": "u3-s3", "diff": 1
    },
    {
        "q": "The contemporary comparison method of sire evaluation was developed by:",
        "o": ["Robertson and Rendel (1954)", "C. R. Henderson (1973)", "L. N. Hazel (1943)", "J. L. Lush (1937)"],
        "a": 0,
        "e": "Robertson and Rendel's contemporary comparison compares a bull's daughters with the daughters of other bulls calving in the same herd, year and season. Henderson developed BLUP; Hazel the selection index.",
        "topicId": "u3-t17", "subSection": "u3-s3", "diff": 3
    },
    {
        "q": "In the equiparent (Rice's) sire index, the sire's index is computed as:",
        "o": ["2D − M", "D − M", "(D + M) / 2", "2M − D"],
        "a": 0,
        "e": "A daughter receives half her genes from each parent, so D = (S + M)/2 and therefore S = 2D − M, where D = daughters' average and M = their dams' average.",
        "topicId": "u3-t17", "subSection": "u3-s3", "diff": 2
    },

    # ---- u3-s4: policies, conservation, biotechnology, disease resistance ----
    {
        "q": "Under India's cattle breeding policy for crossbreeding non-descript cattle, exotic inheritance is generally to be stabilised at about:",
        "o": ["50%", "100%", "25%", "87.5%"],
        "a": 0,
        "e": "About 50% exotic inheritance (up to 62.5% in some states) combines exotic milk yield with indigenous heat tolerance and disease resistance; higher levels do poorly under Indian field conditions.",
        "topicId": "u3-t20", "subSection": "u3-s4", "diff": 2
    },
    {
        "q": "The Booroola (FecB) gene, which increases ovulation rate and litter size in sheep, was originally introduced into the Booroola Merino from which Indian breed?",
        "o": ["Garole", "Nellore", "Chokla", "Marwari"],
        "a": 0,
        "e": "The FecB mutation (in BMPR1B) came from Garole sheep of the Sundarbans in West Bengal; one copy raises ovulation rate by about 1.5.",
        "topicId": "u3-t23", "subSection": "u3-s4", "diff": 2
    },

    # ---- u3-s5: pet, zoo and wild animal breeding ----
    {
        "q": "The queen (female domestic cat) is best described as a(n):",
        "o": ["Induced (reflex) ovulator", "Spontaneous ovulator", "Monoestrous animal", "Anoestrous animal throughout the year"],
        "a": 0,
        "e": "The queen ovulates only after coital stimulation (induced ovulation) and is seasonally polyoestrous, cycling in long days. Rabbits, ferrets and camelids are also induced ovulators.",
        "topicId": "u3-t25", "subSection": "u3-s5", "diff": 1
    },
    {
        "q": "In adult budgerigars, the sexes are usually told apart by the colour of the cere, which is:",
        "o": ["Blue in males, brown or beige in females", "Brown in males, blue in females", "Red in males, white in females", "Identical in both sexes"],
        "a": 0,
        "e": "The cere (fleshy band above the beak) is blue in mature cocks and brown, tan or whitish-blue in hens — the simplest way to form breeding pairs.",
        "topicId": "u3-t26", "subSection": "u3-s5", "diff": 2
    },
    {
        "q": "A captive herd of an endangered deer breeds with 1 male and 9 females. Its effective population size (Ne) is:",
        "o": ["3.6", "10", "9", "4"],
        "a": 0,
        "e": "Ne = 4NmNf / (Nm + Nf) = (4 × 1 × 9) / (1 + 9) = 36/10 = 3.6. A skewed sex ratio makes Ne far smaller than the 10 animals counted.",
        "topicId": "u3-t27", "subSection": "u3-s5", "diff": 3
    },
]

exam_unit3_tf = [
    {
        "q": "Tharparkar is a dual-purpose breed of cattle from Rajasthan.",
        "a": True,
        "e": "True. Tharparkar (Thar desert, Barmer–Jodhpur) is hardy, a good milker and yields useful draught bullocks.",
        "topicId": "u3-t02", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "Response to selection is directly proportional to the heritability of the trait.",
        "a": True,
        "e": "True. R = h² × S, so for the same selection differential a more heritable trait responds faster.",
        "topicId": "u3-t04", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "Combined selection uses an animal's own performance together with the performance of its relatives.",
        "a": True,
        "e": "True. Combined selection weights individual and family (sib or progeny) information, usually through an index, and is more accurate than either alone.",
        "topicId": "u3-t06", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "Random mating, in which every male has an equal chance of mating with every female, is also called panmixia.",
        "a": True,
        "e": "True. Panmixia is the random mating assumed by the Hardy–Weinberg law; assortative mating and inbreeding are forms of non-random mating.",
        "topicId": "u3-t08", "subSection": "u3-s2", "diff": 1
    },
    {
        "q": "Beetal is a large milch goat breed of Punjab.",
        "a": True,
        "e": "True. Beetal (Gurdaspur, Amritsar) is a large dual-purpose goat valued for milk, and is widely used to upgrade local goats.",
        "topicId": "u3-t15", "subSection": "u3-s3", "diff": 1
    },
    {
        "q": "The term 'heterosis' was coined by G. H. Shull.",
        "a": True,
        "e": "True. Shull (1914) coined 'heterosis' while working on hybrid maize; in livestock it is used through crossbreeding and rotational systems.",
        "topicId": "u3-t12", "subSection": "u3-s2", "diff": 1
    },
    {
        "q": "The heterosis obtained in the F₁ is fully retained in the F₂ produced by inter se mating of the F₁.",
        "a": False,
        "e": "False. F₂ retains only about half of the F₁ heterosis, because half of the heterozygosity is lost on inter se mating.",
        "topicId": "u3-t12", "subSection": "u3-s2", "diff": 1
    },
    {
        "q": "Cryopreservation of semen and embryos is a method of ex-situ (in-vitro) conservation of animal genetic resources.",
        "a": True,
        "e": "True. Gene banks store frozen semen, embryos, oocytes and DNA away from the live population (ex-situ in-vitro); keeping live animals on farms outside the native tract is ex-situ in-vivo.",
        "topicId": "u3-t21", "subSection": "u3-s4", "diff": 1
    },
    {
        "q": "Sexed semen is produced by separating X- and Y-bearing sperm with flow cytometry on the basis of their DNA content.",
        "a": True,
        "e": "True. X-bearing bull sperm carry about 4% more DNA than Y-bearing sperm; flow sorting of stained sperm gives about 90% accuracy for female calves.",
        "topicId": "u3-t22", "subSection": "u3-s4", "diff": 2
    },
    {
        "q": "Selecting bulls whose daughters have low somatic cell counts can improve genetic resistance to mastitis.",
        "a": True,
        "e": "True. Somatic cell score is genetically correlated with clinical mastitis and more heritable and easier to record, so it is used for indirect selection for resistance.",
        "topicId": "u3-t23", "subSection": "u3-s4", "diff": 2
    },
    {
        "q": "The bitch is a polyoestrous animal that comes into heat every 21 days.",
        "a": False,
        "e": "False. The bitch is monoestrous, usually cycling once or twice a year (every 6–7 months), with a long anoestrus between cycles. The 21-day cycle belongs to the cow, sow and doe.",
        "topicId": "u3-t25", "subSection": "u3-s5", "diff": 1
    },
    {
        "q": "The effective population size (Ne) is usually larger than the actual number of breeding animals.",
        "a": False,
        "e": "False. Unequal sex ratios, variation in family size and fluctuating numbers make Ne almost always SMALLER than the census number — which is why small zoo populations lose variation fast.",
        "topicId": "u3-t27", "subSection": "u3-s5", "diff": 2
    },
]

exam_unit3_fib = [
    {
        "q": "The Gir breed of cattle takes its name from the Gir forests of the state of ______.",
        "a": ["Gujarat"],
        "a_display": "Gujarat",
        "e": "Gir (Saurashtra, Gujarat) is a milch breed with a convex forehead and long pendulous ears; it is also widely used in Brazil.",
        "topicId": "u3-t02", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "The genetic ability of N'Dama cattle of West Africa to survive and produce under trypanosome challenge is called ______.",
        "a": ["trypanotolerance", "trypano-tolerance", "trypano tolerance"],
        "a_display": "Trypanotolerance",
        "e": "Trypanotolerance is a classic example of genetic disease resistance; breeding such animals is cheaper and more sustainable than repeated drug treatment.",
        "topicId": "u3-t23", "subSection": "u3-s4", "diff": 2
    },
    {
        "q": "The weight of wool shorn from a sheep before scouring (washing) is called the ______ fleece weight.",
        "a": ["greasy", "grease"],
        "a_display": "Greasy",
        "e": "Greasy fleece weight is the main economic trait of wool sheep; clean fleece weight is measured after scouring removes grease, suint and dirt.",
        "topicId": "u3-t03", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "Mating of phenotypically dissimilar individuals (e.g., large × small) is called negative ______ mating.",
        "a": ["assortative"],
        "a_display": "Assortative",
        "e": "Negative (disassortative) assortative mating pulls offspring toward the mean and slightly increases heterozygosity.",
        "topicId": "u3-t08", "subSection": "u3-s2", "diff": 2
    },
    {
        "q": "The inbreeding coefficient (F) is the probability that the two alleles at a locus in an individual are identical by ______.",
        "a": ["descent"],
        "a_display": "Descent",
        "e": "Alleles identical by descent are copies of one allele carried by a common ancestor, which is why F measures the increase in homozygosity due to inbreeding.",
        "topicId": "u3-t09", "subSection": "u3-s2", "diff": 2
    },
    {
        "q": "The Ongole breed of dual-purpose cattle originates from the state of ______.",
        "a": ["Andhra Pradesh", "Andhra"],
        "a_display": "Andhra Pradesh",
        "e": "Ongole (Nellore, Guntur, Prakasam) is a large dual-purpose breed; exported as 'Nellore', it became the dominant beef breed of Brazil.",
        "topicId": "u3-t02", "subSection": "u3-s1", "diff": 1
    },
    {
        "q": "The hypothesis that heterosis results from favourable dominant alleles from each parent masking the unfavourable recessive alleles of the other is the ______ hypothesis.",
        "a": ["dominance"],
        "a_display": "Dominance",
        "e": "The dominance hypothesis (Davenport, Bruce, Jones) explains heterosis by complementary dominant genes; the overdominance hypothesis (Shull, East) says the heterozygote itself is superior.",
        "topicId": "u3-t12", "subSection": "u3-s2", "diff": 2
    },
    {
        "q": "The Sunandini crossbred cattle (Brown Swiss / Jersey × local) were developed in the state of ______.",
        "a": ["Kerala"],
        "a_display": "Kerala",
        "e": "Sunandini was developed under the Indo-Swiss Project in Kerala.",
        "topicId": "u3-t19", "subSection": "u3-s3", "diff": 2
    },
    {
        "q": "The world's first mammal cloned from an adult somatic cell, 'Dolly' the sheep (1996), was produced by somatic cell nuclear ______.",
        "a": ["transfer"],
        "a_display": "Transfer (SCNT)",
        "e": "In SCNT the nucleus of a somatic cell is placed into an enucleated oocyte. India's NDRI, Karnal, later produced the first cloned buffalo calves this way.",
        "topicId": "u3-t22", "subSection": "u3-s4", "diff": 1
    },
    {
        "q": "A record of an animal's ancestry over several generations, used when selecting dogs and cats, is called a ______ sheet.",
        "a": ["pedigree"],
        "a_display": "Pedigree",
        "e": "The pedigree sheet lists sire, dam and grand-parents with registration numbers and titles; Kennel Club registration depends on it.",
        "topicId": "u3-t24", "subSection": "u3-s5", "diff": 1
    },
    {
        "q": "Budgerigars and lovebirds are ______ nesters, so a nest box must be provided for breeding in captivity.",
        "a": ["cavity", "hole", "cavity-nesting"],
        "a_display": "Cavity (hole)",
        "e": "In the wild these parrots nest in tree hollows; in aviaries a wooden nest box with a concave floor is given.",
        "topicId": "u3-t26", "subSection": "u3-s5", "diff": 2
    },
    {
        "q": "The CCMB facility at Hyderabad that uses assisted reproduction and gene banking to conserve endangered wild animals is called ______.",
        "a": ["LaCONES", "Lacones"],
        "a_display": "LaCONES",
        "e": "LaCONES (Laboratory for the Conservation of Endangered Species) does semen and gamete banking, DNA fingerprinting and assisted reproduction for Indian wildlife.",
        "topicId": "u3-t28", "subSection": "u3-s5", "diff": 2
    },
]


# Tag every question so the quiz can offer a dedicated "Exam Top 50" module.
def _tag(items):
    for it in items:
        it["exam"] = True
    return items


for _lst in (exam_unit1_mcq, exam_unit1_tf, exam_unit1_fib,
             exam_unit2_mcq, exam_unit2_tf, exam_unit2_fib,
             exam_unit3_mcq, exam_unit3_tf, exam_unit3_fib):
    _tag(_lst)
