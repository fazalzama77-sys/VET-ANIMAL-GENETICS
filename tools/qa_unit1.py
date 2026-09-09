# -*- coding: utf-8 -*-
"""
Q&A Bank Unit 1: Topics u1-q01 to u1-q25
Biostatistics and Computer Application (VCI MSVE 2nd Year B.V.Sc. & A.H. Standard)
12 Two-Mark Definitions + 8 Five-Mark Short Notes + 5 Twelve-Mark Long Essays
"""
null = None
true = True
false = False

questions = [
    # =========================================================================
    # 12 TWO-MARK DEFINITIONS (marks: 2, type: "define")
    # =========================================================================
    {
        "id": "u1-q01",
        "type": "define",
        "marks": 2,
        "question": "Define Biostatistics and state its primary scope in veterinary science.",
        "topicId": "u1-t01",
        "answer": (
            "<b>Biostatistics</b> (or Biometry) is the application of statistical principles, methods, and mathematical probability "
            "to the collection, compilation, presentation, analysis, and interpretation of biological, medical, and veterinary data.<br><br>"
            "<b>Scope in Veterinary Medicine:</b>"
            "<ul>"
            "<li>Designing clinical vaccine and anthelmintic efficacy trials.</li>"
            "<li>Evaluating genetic parameters (heritability, breeding values) in livestock improvement.</li>"
            "<li>Epidemiological disease surveillance and setting normal clinical biochemical reference intervals.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Definition as application of statistics to biological/veterinary data.",
            "Key scope: Clinical trials, genetic parameter estimation, disease surveillance."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["IVRI 2021", "TANUVAS 2022", "GADVASU 2023"]
    },
    {
        "id": "u1-q02",
        "type": "define",
        "marks": 2,
        "question": "Define Parameter and Statistic. Give two examples of each.",
        "topicId": "u1-t03",
        "answer": (
            "<ul>"
            "<li><b>Parameter:</b> Any numerical descriptive measure computed from the <i>entire population</i>. It is a constant, fixed value, typically denoted by Greek letters."
            "<br><i>Examples:</i> Population Mean (<code>&mu;</code>), Population Standard Deviation (<code>&sigma;</code>), Population Variance (<code>&sigma;&sup2;</code>).</li>"
            "<li><b>Statistic:</b> Any numerical descriptive measure computed from a <i>sample</i> drawn from the population. It is a random variable that varies from sample to sample, denoted by Roman letters."
            "<br><i>Examples:</i> Sample Mean (<code>\\bar{X}</code>), Sample Standard Deviation (<code>s</code>), Sample Variance (<code>s&sup2;</code>).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Parameter: Characteristic of entire population (constant, Greek letters μ, σ).",
            "Statistic: Characteristic of a sample (variable, Roman letters X̄, s)."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["VCI Annual 2019", "WBUAFS 2022"]
    },
    {
        "id": "u1-q03",
        "type": "define",
        "marks": 2,
        "question": "State Sturges' Rule for determining the number of class intervals in a frequency distribution.",
        "topicId": "u1-t02",
        "answer": (
            "<b>Sturges' Rule</b> is an empirical biometrical formula used to determine the optimal number of class intervals (<code>k</code>) "
            "when constructing a continuous grouped frequency distribution from <code>N</code> raw observations:<br><br>"
            "<code>k = 1 + 3.322 &times; log10(N)</code><br><br>"
            "Where:"
            "<ul>"
            "<li><code>k</code> = Number of class intervals (rounded to nearest integer).</li>"
            "<li><code>N</code> = Total number of observations (sample size).</li>"
            "<li><code>Class Width (h)</code> = <code>Range / k = (X_max - X_min) / k</code>.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Formula: k = 1 + 3.322 * log10(N).",
            "Class width formula: h = Range / k."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["MAFSU 2020", "KVAFSU 2023"]
    },
    {
        "id": "u1-q04",
        "type": "define",
        "marks": 2,
        "question": "Define Cumulative Frequency Curve (Ogive) and state its primary graphical application.",
        "topicId": "u1-t04",
        "answer": (
            "An <b>Ogive</b> is a smooth, S-shaped (sigmoidal) graphical curve obtained by plotting cumulative frequencies against class boundaries.<br>"
            "<ul>"
            "<li><b>Less-than Ogive:</b> Plots 'less-than' cumulative frequencies against <i>upper class boundaries</i> (rising curve).</li>"
            "<li><b>More-than Ogive:</b> Plots 'more-than' cumulative frequencies against <i>lower class boundaries</i> (falling curve).</li>"
            "</ul>"
            "<b>Primary Application:</b> The perpendicular dropped to the X-axis from the point where 'Less-than' and 'More-than' ogives intersect determines the <b>Median</b> (as well as quartiles Q1, Q3 and percentiles) graphically."
        ),
        "keyPoints": [
            "Sigmoidal curve plotting cumulative frequency against class boundaries.",
            "Intersection of less-than and more-than ogives gives graphical Median."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["RAJUVAS 2021", "SVVU 2022"]
    },
    {
        "id": "u1-q05",
        "type": "define",
        "marks": 2,
        "question": "Define Mode and state the empirical relationship between Mean, Median, and Mode.",
        "topicId": "u1-t05",
        "answer": (
            "<b>Mode</b> is that value of a variable which occurs with the greatest frequency in a distribution (the most common or typical observation).<br><br>"
            "<b>Empirical Relationship:</b> In a moderately asymmetrical (skewed) biological distribution, the relationship formulated by Karl Pearson is:<br>"
            "<code>Mode = 3 &times; Median - 2 &times; Mean</code><br>"
            "Or: <code>Mean - Mode = 3 &times; (Mean - Median)</code>."
        ),
        "keyPoints": [
            "Mode is the observation occurring with maximum frequency.",
            "Empirical formula: Mode = 3 * Median - 2 * Mean."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["IVRI 2020", "LUVAS 2021"]
    },
    {
        "id": "u1-q06",
        "type": "define",
        "marks": 2,
        "question": "Define Coefficient of Variation (CV%) and state why it is preferred over Standard Deviation.",
        "topicId": "u1-t07",
        "answer": (
            "<b>Coefficient of Variation (CV%)</b> is the relative measure of dispersion expressing standard deviation as a percentage of the arithmetic mean:<br>"
            "<code>CV% = (s / \\bar{X}) &times; 100</code><br><br>"
            "<b>Why Preferred:</b>"
            "<ul>"
            "<li>CV is a <b>pure, unitless number</b> (dimensionless).</li>"
            "<li>Enables direct comparison of variability between traits with completely different units of measurement (e.g., comparing variability of body weight in kg vs milk yield in liters, or flock uniformity in broilers).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Formula: CV% = (s / X̄) * 100.",
            "Unitless measure enabling comparison across different traits and units."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["TANUVAS 2023", "NDVSU 2022"]
    },
    {
        "id": "u1-q07",
        "type": "define",
        "marks": 2,
        "question": "Enumerate four essential properties of the Standard Normal Curve.",
        "topicId": "u1-t11",
        "answer": (
            "<ol>"
            "<li><b>Bell-shaped and Perfectly Symmetrical:</b> Symmetrical about <code>Z = 0</code>; Skewness <code>&beta;_1 = 0</code>, Kurtosis <code>&beta;_2 = 3</code> (Mesokurtic).</li>"
            "<li><b>Coincident Averages:</b> <code>Mean = Median = Mode = 0</code>; Standard Deviation <code>&sigma; = 1</code>.</li>"
            "<li><b>Asymptotic Tails:</b> Tails extend infinitely in both directions, approaching but never touching the horizontal axis.</li>"
            "<li><b>Total Area Unity:</b> Total area under curve is <b>1.0 (100%)</b>; <code>&mu; &plusmn; 1&sigma; = 68.27%</code>, <code>&mu; &plusmn; 2&sigma; = 95.45%</code>, <code>&mu; &plusmn; 3&sigma; = 99.73%</code>.</li>"
            "</ol>"
        ),
        "keyPoints": [
            "Mean = Median = Mode = 0; SD = 1.",
            "Area: μ ± 1σ = 68.27%, μ ± 2σ = 95.45%, μ ± 3σ = 99.73%."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["VCI Annual 2022", "GADVASU 2021"]
    },
    {
        "id": "u1-q08",
        "type": "define",
        "marks": 2,
        "question": "Define Pearson's Correlation Coefficient (r) and state its mathematical range.",
        "topicId": "u1-t12",
        "answer": (
            "<b>Pearson's Product-Moment Correlation Coefficient (r)</b> is a mathematical measure of the degree, strength, and direction "
            "of linear association between two continuous quantitative biological variables (X and Y):<br><br>"
            "<code>r = Cov(X, Y) / [ &sigma;_X &times; &sigma;_Y ] = SP_xy / &radic;(SS_x &times; SS_y)</code><br><br>"
            "<b>Mathematical Range:</b> Strictly bounded between <b>-1.0 and +1.0</b> (<code>-1 &le; r &le; +1</code>)."
            "<br>&bull; <code>r = +1</code>: Perfect positive linear correlation."
            "<br>&bull; <code>r = -1</code>: Perfect negative linear correlation."
            "<br>&bull; <code>r = 0</code>: Zero linear correlation."
        ),
        "keyPoints": [
            "Measures linear relationship: r = Cov(X,Y) / (σX * σY).",
            "Range: -1.0 to +1.0."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["IVRI 2019", "WBUAFS 2021"]
    },
    {
        "id": "u1-q09",
        "type": "define",
        "marks": 2,
        "question": "Define Null Hypothesis (H0) and Alternative Hypothesis (H1).",
        "topicId": "u1-t15",
        "answer": (
            "<ul>"
            "<li><b>Null Hypothesis (H0):</b> A hypothesis of no difference, no effect, or no association formulated for possible rejection. "
            "It states that any observed difference between sample statistic and population parameter is purely due to chance sampling error."
            "<br><i>Example:</i> <code>H0: &mu;_1 = &mu;_2</code> (New anthelmintic does not alter mean fecal egg counts).</li>"
            "<li><b>Alternative Hypothesis (H1):</b> A hypothesis that complements and contradicts H0, accepted when H0 is rejected. "
            "It indicates a real, statistically significant biological effect."
            "<br><i>Example:</i> <code>H1: &mu;_1 &ne; &mu;_2</code> (Two-tailed) or <code>H1: &mu;_1 &gt; &mu;_2</code> (One-tailed).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "H0: Hypothesis of no difference/effect, set up for rejection.",
            "H1: Statement of actual biological difference, accepted when H0 rejected."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["RAJUVAS 2022", "SVVU 2021"]
    },
    {
        "id": "u1-q10",
        "type": "define",
        "marks": 2,
        "question": "Differentiate between Type I Error and Type II Error in hypothesis testing.",
        "topicId": "u1-t15",
        "answer": (
            "<ul>"
            "<li><b>Type I Error (&alpha; Error):</b> The error committed by <b>rejecting the null hypothesis (H0) when it is actually TRUE</b>. "
            "The probability of committing Type I error is the <b>Level of Significance (&alpha;)</b> (commonly fixed at 0.05 or 0.01)."
            "<br><i>Clinical analogy:</i> Falsely declaring a healthy cow to be diseased (False Positive).</li>"
            "<li><b>Type II Error (&beta; Error):</b> The error committed by <b>accepting (failing to reject) H0 when it is actually FALSE</b>. "
            "The probability is denoted by <code>&beta;</code>, and <code>(1 - &beta;)</code> is the <b>Power of the Test</b>."
            "<br><i>Clinical analogy:</i> Falsely clearing a truly infected cow as healthy (False Negative).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Type I Error (α): Rejecting true H0 (False Positive).",
            "Type II Error (β): Failing to reject false H0 (False Negative); Power = 1 - β."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["LUVAS 2022", "TANUVAS 2020"]
    },
    {
        "id": "u1-q11",
        "type": "define",
        "marks": 2,
        "question": "Define Degrees of Freedom (df) in biostatistics and give an example.",
        "topicId": "u1-t16",
        "answer": (
            "<b>Degrees of Freedom (df)</b> is the total number of independent observations or values in a statistical calculation "
            "that are free to vary after imposing necessary mathematical restrictions or constraints (such as sample mean or sample total).<br><br>"
            "<code>df = Total observations (n) - Number of independent constraints (k)</code><br><br>"
            "<i>Example:</i> In calculating sample variance <code>s&sup2;</code> from <code>n</code> observations, one constraint is imposed "
            "because deviations must sum to zero (<code>&Sigma;(X - \\bar{X}) = 0</code>). Hence, <code>df = n - 1</code>."
        ),
        "keyPoints": [
            "Number of independent values free to vary minus number of restrictions.",
            "df = n - 1 in sample variance because one degree of freedom is lost estimating mean."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["IVRI 2022", "MAFSU 2021"]
    },
    {
        "id": "u1-q12",
        "type": "define",
        "marks": 2,
        "question": "State the three fundamental principles of experimental design formulated by Sir R.A. Fisher.",
        "topicId": "u1-t18",
        "answer": (
            "<ol>"
            "<li><b>Replication:</b> Repetition of the experimental treatments under identical conditions to provide an estimate of experimental error and increase precision.</li>"
            "<li><b>Randomization:</b> Allocation of experimental treatments to experimental units strictly by chance, ensuring unbiased estimates of treatment means and valid error variance.</li>"
            "<li><b>Local Control:</b> Grouping or blocking heterogeneous experimental units into homogenous blocks (e.g., blocking cows by parity or body weight) to isolate extraneous variation from experimental error.</li>"
            "</ol>"
        ),
        "keyPoints": [
            "Three principles: Replication, Randomization, and Local Control.",
            "Replication estimates error; Randomization eliminates bias; Local Control reduces error."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["VCI Annual 2021", "KVAFSU 2022"]
    },

    # =========================================================================
    # 8 FIVE-MARK SHORT ANSWER QUESTIONS (marks: 5, type: "short" / "diff")
    # =========================================================================
    {
        "id": "u1-q13",
        "type": "diff",
        "marks": 5,
        "question": "Differentiate between Primary Data and Secondary Data. Explain methods of collecting primary livestock data.",
        "topicId": "u1-t01",
        "answer": (
            "<b>DEFINITION AND CONTRAST:</b><br>"
            "Biological and livestock data are classified into Primary and Secondary based on original source and collection agency.<br><br>"
            "<b>METHODS OF COLLECTING PRIMARY LIVESTOCK DATA:</b>"
            "<ol>"
            "<li><b>Direct Personal Observation / Measurement:</b> The veterinarian directly measures animal parameters using calibrated instruments (e.g., weighing calves on platform scales, recording milk yields via flow meters, taking rectal temperatures). Highest accuracy.</li>"
            "<li><b>Questionnaires & Farmer Interviews:</b> Distributed structured schedules to livestock owners during field surveys (e.g., recording daily feed intake, grazing hours, estrus observations).</li>"
            "<li><b>Automated Electronic Sensors:</b> Modern IoT sensors such as RFID tags, rumination collars, pedometers, and automated milking system (AMS) computer logs.</li>"
            "</ol>"
        ),
        "keyPoints": [
            "Primary data: First-hand, original data collected directly for specific study.",
            "Secondary data: Pre-existing data compiled from published records/databases.",
            "Collection methods: Direct measurement, farmer questionnaires, RFID/sensor logs."
        ],
        "diagram": "",
        "table": {
            "title": "Comparison Between Primary and Secondary Biological Data",
            "headers": ["Parameter / Criterion", "Primary Data", "Secondary Data"],
            "rows": [
                ["Origin", "First-hand, original collection by investigator", "Second-hand; gathered from pre-existing records"],
                ["Collection Cost & Time", "High cost, labor-intensive, time-consuming", "Low cost, rapid, easily accessible"],
                ["Reliability & Accuracy", "Highly reliable; investigator controls protocol", "Variable; depends on original reporting accuracy"],
                ["Veterinary Example", "Weighing 50 heifers directly on farm scale", "Analyzing 10-year milk yield records from farm registers"]
            ]
        },
        "pyq": ["IVRI 2020", "TANUVAS 2021", "NDVSU 2023"]
    },
    {
        "id": "u1-q14",
        "type": "short",
        "marks": 5,
        "question": "Describe the properties, comparative merits, and demerits of Arithmetic Mean and Median in biological data.",
        "topicId": "u1-t05",
        "answer": (
            "<b>I. ARITHMETIC MEAN (\\bar{X}):</b>"
            "<ul>"
            "<li><b>Properties:</b> Rigidly defined; based on all observations; algebraic manipulations possible (<code>&Sigma;(X - \\bar{X}) = 0</code>; Combined Mean formula <code>\\bar{X}_{12} = (n_1 \\bar{X}_1 + n_2 \\bar{X}_2)/(n_1 + n_2)</code>).</li>"
            "<li><b>Merits:</b> Most stable and reliable average; forms the mathematical engine of advanced biometrics (ANOVA, regression, heritability).</li>"
            "<li><b>Demerits:</b> Severely distorted by extreme outliers; cannot be calculated for open-ended frequency classes.</li>"
            "</ul><br>"
            "<b>II. MEDIAN (M_e):</b>"
            "<ul>"
            "<li><b>Properties:</b> Positional average; divides arrayed distribution into two exactly equal halves (50% above, 50% below).</li>"
            "<li><b>Merits:</b> Completely immune to extreme outliers; can be located graphically via ogives; can be computed for open-ended tables.</li>"
            "<li><b>Demerits:</b> Not based on all observations; incapable of further algebraic treatment; higher sampling fluctuations.</li>"
            "</ul><br>"
            "<b>VETERINARY PREFERENCE RULE:</b> Use <b>Arithmetic Mean</b> for symmetrical livestock traits (body weight, gestation length). "
            "Use <b>Median</b> for highly skewed data with extreme outliers (Somatic Cell Count in mastitis, days open, parasite egg counts)."
        ),
        "keyPoints": [
            "Mean: Based on all values, mathematically tractable, highly sensitive to outliers.",
            "Median: Positional average, robust against extreme values and open-ended classes.",
            "Biological preference: Mean for normal traits, Median for skewed/parasitological data."
        ],
        "diagram": "",
        "table": {
            "title": "Comparison Between Arithmetic Mean and Median",
            "headers": ["Criterion", "Arithmetic Mean (\\bar{X})", "Median (M_e)"],
            "rows": [
                ["Mathematical Basis", "Algebraic centroid (&Sigma;X / n)", "Positional middle value (N/2)"],
                ["Sensitivity to Outliers", "Extremely sensitive (distorted by extremes)", "Completely robust (unaffected by extremes)"],
                ["Further Algebraic Treatment", "Fully capable (combined mean, variance, ANOVA)", "Not capable of further algebraic manipulation"],
                ["Graphical Determination", "Cannot be determined graphically", "Determined by intersection of Ogives"]
            ]
        },
        "pyq": ["GADVASU 2020", "VCI Annual 2022"]
    },
    {
        "id": "u1-q15",
        "type": "diff",
        "marks": 5,
        "question": "Differentiate between Standard Deviation (SD) and Standard Error of Mean (SE). Explain their clinical significance.",
        "topicId": "u1-t07",
        "answer": (
            "<b>DEFINITIONS & FORMULAS:</b>"
            "<ul>"
            "<li><b>Standard Deviation (s):</b> The positive square root of the arithmetic mean of squared deviations from the mean: <code>s = &radic;[ &Sigma;(X - \\bar{X})&sup2; / (n - 1) ]</code>. Measures biological variation among individual animals.</li>"
            "<li><b>Standard Error of Mean (SE):</b> The standard deviation of the sampling distribution of sample means: <code>SE_\\bar{x} = s / &radic;n</code>. Measures the precision and reliability of the estimated sample mean.</li>"
            "</ul><br>"
            "<b>CLINICAL & SCIENTIFIC SIGNIFICANCE:</b>"
            "<ul>"
            "<li><b>When to report SD:</b> When describing biological diversity and reference ranges within a herd (e.g., 'Normal cow rectal temperature = 38.6 &plusmn; 0.5&deg;C').</li>"
            "<li><b>When to report SE:</b> When publishing experimental trial comparisons and constructing 95% Confidence Intervals: <code>\\bar{X} &plusmn; 1.96 &times; SE</code> (e.g., 'Mean milk yield of bypass-fat group = 14.2 &plusmn; 0.4 kg').</li>"
            "</ul>"
        ),
        "keyPoints": [
            "SD measures individual biological variability within a population: s = √(SS / (n-1)).",
            "SE measures precision of the sample mean estimate: SE = s / √n.",
            "As sample size n increases, SD remains stable while SE decreases toward zero."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Distinction: Standard Deviation vs Standard Error",
            "headers": ["Feature / Parameter", "Standard Deviation (SD)", "Standard Error of Mean (SE)"],
            "rows": [
                ["What it Measures", "Biological dispersion of individual animals around sample mean", "Sampling variability and precision of the sample mean"],
                ["Formula", "s = &radic;[ &Sigma;(X - \\bar{X})&sup2; / (n - 1) ]", "SE_\\bar{x} = s / &radic;n"],
                ["Effect of Increasing Sample Size (n)", "Remains stable (converges to population &sigma;)", "Decreases progressively toward zero (1/&radic;n rate)"],
                ["Primary Reporting Purpose", "Clinical reference intervals (Mean &plusmn; 2 SD)", "Research trial treatment comparisons (Mean &plusmn; SE)"]
            ]
        },
        "pyq": ["IVRI 2021", "WBUAFS 2023", "SVVU 2020"]
    },
    {
        "id": "u1-q16",
        "type": "short",
        "marks": 5,
        "question": "Describe the Poisson Distribution: Mathematical equation, conditions of validity, and biological applications in veterinary medicine.",
        "topicId": "u1-t10",
        "answer": (
            "<b>DEFINITION & PROBABILITY MASS FUNCTION:</b><br>"
            "The <b>Poisson Distribution</b>, formulated by Sim&eacute;on Denis Poisson (1837), is a discrete probability distribution "
            "for modeling the occurrence of rare biological events in a continuous continuum of time, space, or volume:<br><br>"
            "<code>P(X = x) = (e^{-&lambda;} &times; &lambda;^x) / x!</code> &nbsp;&nbsp;&nbsp;&nbsp; (for x = 0, 1, 2, ...)<br>"
            "Where: <code>&lambda;</code> = Mean rate of occurrence per unit interval; <code>e &approx; 2.71828</code>.<br><br>"
            "<b>DISTINCTIVE BIOMETRICAL PROPERTIES:</b>"
            "<ul>"
            "<li><b>Single Parameter Distribution:</b> Completely defined by a single parameter <code>&lambda;</code>.</li>"
            "<li><b>Equidispersion Identity:</b> <code>Mean = Variance = &lambda;</code> (Mean equals Variance!).</li>"
            "</ul><br>"
            "<b>CONDITIONS OF VALIDITY:</b>"
            "<ol>"
            "<li>Number of trials <code>n</code> is very large (<code>n &rarr; &infin;</code>).</li>"
            "<li>Probability of event occurrence <code>p</code> is extremely small (rare event, <code>p &rarr; 0</code>).</li>"
            "<li>Their product is a finite constant: <code>np = &lambda;</code>.</li>"
            "</ol><br>"
            "<b>VETERINARY BIOLOGICAL EXAMPLES:</b>"
            "<ul>"
            "<li>Hemocytometer counts of red/white blood cells per counting chamber grid square.</li>"
            "<li>Bacterial colony counts (CFU) on agar culture plates.</li>"
            "<li>Occurrence of rare congenital malformations (e.g., dicephalus calves) in a dairy population.</li>"
            "<li>Dairy cow twinning rate under natural mating conditions.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Formula: P(X=x) = (e^-λ * λ^x) / x!.",
            "Single parameter distribution where Mean = Variance = λ.",
            "Applicable for rare events with large n and very small p (np = λ).",
            "Veterinary uses: Hemocytometer blood counts, CFU bacterial plates, congenital birth defects."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["RAJUVAS 2020", "TANUVAS 2022"]
    },
    {
        "id": "u1-q17",
        "type": "short",
        "marks": 5,
        "question": "Explain Linear Regression and Regression Coefficients (b_yx and b_xy). State the mathematical relationships between regression and correlation.",
        "topicId": "u1-t13",
        "answer": (
            "<b>DEFINITION:</b><br>"
            "<b>Regression Analysis</b> estimates the mathematical functional relationship between a dependent variable (Y) and one or more independent variables (X), "
            "enabling quantitative prediction of Y from known values of X.<br><br>"
            "<b>REGRESSION COEFFICIENTS:</b>"
            "<ul>"
            "<li><b>Regression Coefficient of Y on X (b_yx):</b> Measures the average unit change in Y per unit increase in X:<br>"
            "<code>b_yx = SP_xy / SS_x = r &times; (s_y / s_x)</code></li>"
            "<li><b>Regression Coefficient of X on Y (b_xy):</b> Measures the unit change in X per unit increase in Y:<br>"
            "<code>b_xy = SP_xy / SS_y = r &times; (s_x / s_y)</code></li>"
            "</ul><br>"
            "<b>MATHEMATICAL RELATIONSHIPS (EXAM SCORING RULES):</b>"
            "<ol>"
            "<li><b>Geometric Mean Property:</b> The correlation coefficient is the geometric mean of the two regression coefficients:<br>"
            "<code>r = &plusmn; &radic;(b_yx &times; b_xy)</code>.</li>"
            "<li><b>Sign Consistency:</b> Both regression coefficients and the correlation coefficient must have the <b>identical algebraic sign</b> (all positive or all negative).</li>"
            "<li><b>Magnitude Restriction:</b> If one regression coefficient is greater than 1.0, the other must be less than 1.0 (since <code>b_yx &times; b_xy = r&sup2; &le; 1.0</code>).</li>"
            "<li><b>Intersection Point:</b> The two regression lines always intersect at the point of their means: <code>(\\bar{X}, \\bar{Y})</code>.</li>"
            "</ol>"
        ),
        "keyPoints": [
            "b_yx = SPxy / SSx = r * (sy / sx); measures unit change in Y per unit X.",
            "r = ± √(b_yx * b_xy) (geometric mean property).",
            "Both regression slopes and r share the exact same algebraic sign.",
            "The two regression lines intersect at the coordinates of their means (X̄, Ȳ)."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["MAFSU 2022", "IVRI 2023", "LUVAS 2021"]
    },
    {
        "id": "u1-q18",
        "type": "short",
        "marks": 5,
        "question": "Short note on Student's Paired t-test: Principle, Assumptions, Formula, and Clinical Application.",
        "topicId": "u1-t16",
        "answer": (
            "<b>PRINCIPLE:</b><br>"
            "The <b>Paired t-test</b> is applied when two sets of observations are intrinsically paired or matched—most commonly in <b>'Before-and-After' clinical trials</b> "
            "conducted on the exact same group of animals. It eliminates inter-animal variation, isolating the true therapeutic drug effect.<br><br>"
            "<b>ASSUMPTIONS:</b>"
            "<ol>"
            "<li>Observations are paired and drawn randomly.</li>"
            "<li>The differences <code>d_i = X_{after} - X_{before}</code> follow a normal distribution.</li>"
            "</ol><br>"
            "<b>FORMULAS & DEGREES OF FREEDOM:</b>"
            "<ul>"
            "<li>Individual difference: <code>d_i = X_{2i} - X_{1i}</code>.</li>"
            "<li>Mean difference: <code>\\bar{d} = (&Sigma; d) / n</code>.</li>"
            "<li>Standard deviation of differences: <code>s_d = &radic;[ { &Sigma;d&sup2; - (&Sigma;d)&sup2;/n } / (n - 1) ]</code>.</li>"
            "<li>Standard Error: <code>SE_\\bar{d} = s_d / &radic;n</code>.</li>"
            "<li><b>Test Statistic:</b> <code>t_cal = | \\bar{d} | / (s_d / &radic;n)</code> with <b>df = n - 1</b> (where n = number of pairs).</li>"
            "</ul><br>"
            "<b>CLINICAL APPLICATION:</b>"
            "Testing anthelmintic efficacy by comparing fecal egg counts (EPG) in 10 sheep <i>before dosing</i> vs <i>14 days post-dosing</i>; "
            "or testing antipyretic drugs by recording rectal temperatures before vs 2 hours post-injection."
        ),
        "keyPoints": [
            "Used for before-and-after trials on the same animals (paired design).",
            "Eliminates inter-animal baseline variation, drastically increasing test sensitivity.",
            "Formula: t = d̄ / (sd / √n) with df = n - 1.",
            "Veterinary uses: Anthelmintic trials (EPG drop), antipyretic drug evaluations."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["TANUVAS 2021", "KVAFSU 2020", "VCI Annual 2020"]
    },
    {
        "id": "u1-q19",
        "type": "short",
        "marks": 5,
        "question": "What is Yates' Correction for Continuity in Chi-Square Test? State when and why it is applied.",
        "topicId": "u1-t17",
        "answer": (
            "<b>DEFINITION & CONCEPT:</b><br>"
            "<b>Yates' Correction for Continuity</b>, introduced by Frank Yates (1934), is a mathematical adjustment applied to the 2&times;2 contingency "
            "Chi-Square test to correct for approximating a discrete binomial distribution with a continuous Chi-Square distribution.<br><br>"
            "<b>FORMULA FOR 2&times;2 CONTINGENCY TABLE:</b><br>"
            "<code>&chi;&sup2;_{corrected} = [ N &times; ( |ad - bc| - N/2 )&sup2; ] / [ (a + b)(c + d)(a + c)(b + d) ]</code><br>"
            "Where <code>a, b, c, d</code> are cell frequencies and <code>N = a + b + c + d</code>.<br><br>"
            "<b>WHEN TO APPLY (MANDATORY CONDITIONS):</b>"
            "<ol>"
            "<li>Applicable <b>strictly when degrees of freedom df = 1</b> (i.e. 2&times;2 contingency tables).</li>"
            "<li>Applied when any expected cell frequency is small (<b>E &lt; 5</b>) and total sample size N is between 20 and 40.</li>"
            "</ol><br>"
            "<b>WHY APPLIED:</b>"
            "Without Yates' correction, the uncorrected &chi;&sup2; value is systematically over-estimated (inflated), leading to false rejection of true null hypotheses (Type I error). "
            "Subtracting <code>N/2</code> from <code>|ad - bc|</code> reduces the calculated &chi;&sup2;, making the test conservative and statistically valid."
        ),
        "keyPoints": [
            "Yates' correction adjusts for approximating discrete frequencies with a continuous curve.",
            "Formula: χ² = [ N * (|ad - bc| - N/2)² ] / [ (a+b)(c+d)(a+c)(b+d) ].",
            "Mandatory condition: df = 1 (2x2 table) and any expected cell frequency E < 5.",
            "Prevents inflation of test statistic and controls Type I error."
        ],
        "diagram": "",
        "table": null,
        "pyq": ["WBUAFS 2022", "IVRI 2022", "NDVSU 2021"]
    },
    {
        "id": "u1-q20",
        "type": "diff",
        "marks": 5,
        "question": "Differentiate between Completely Randomized Design (CRD) and Randomized Block Design (RBD).",
        "topicId": "u1-t18",
        "answer": (
            "<b>CORE CONCEPTS:</b><br>"
            "CRD and RBD are fundamental agricultural and veterinary experimental designs differing in local control and layout.<br><br>"
            "<b>PRIMARY DIFFERENCES:</b>"
            "<ul>"
            "<li><b>CRD:</b> Treatments are assigned randomly across the entire experimental material without grouping. Relies on only 2 principles: <b>Randomization and Replication</b>. "
            "Best suited for homogenous laboratory conditions (broiler chicks of identical age/weight in battery brooders; in-vitro cell culture).</li>"
            "<li><b>RBD:</b> Experimental units are grouped into homogenous blocks along one known source of variation (e.g., initial body weight, parity, lactation yield). "
            "Treatments are randomly assigned within each block. Utilizes all 3 principles: <b>Randomization, Replication, and Local Control</b>. "
            "Standard for large animal farm trials (dairy cattle feeding trials).</li>"
            "</ul>"
        ),
        "keyPoints": [
            "CRD uses 2 principles (Randomization, Replication); assumes homogenous units.",
            "RBD uses all 3 principles (adds Local Control via blocking in one direction).",
            "Error df in CRD: N - k; Error df in RBD: (k - 1)(r - 1).",
            "RBD isolates block variation, yielding smaller error variance and higher precision."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Comparison: CRD vs RBD Experimental Designs",
            "headers": ["Criterion / Feature", "Completely Randomized Design (CRD)", "Randomized Block Design (RBD)"],
            "rows": [
                ["Principles Applied", "2 (Randomization & Replication)", "3 (Randomization, Replication & Local Control)"],
                ["Experimental Material", "Completely homogenous throughout", "Heterogeneous in one direction (blocked into homogenous groups)"],
                ["Layout & Blocking", "Zero blocking; treatments assigned at random", "Replications organized into distinct blocks"],
                ["Degrees of Freedom for Error", "N - k = k(r - 1)", "(k - 1)(r - 1)"],
                ["Precision & Efficiency", "Lower if units are heterogeneous", "Higher (isolates block variance from error)"],
                ["Field Veterinary Application", "Laboratory broiler chick trials / Petrie dishes", "Dairy cattle feeding trials (blocked by parity/yield)"]
            ]
        },
        "pyq": ["RAJUVAS 2021", "TANUVAS 2023", "VCI Annual 2019"]
    },

    # =========================================================================
    # 5 TWELVE-MARK LONG ANSWER QUESTIONS (marks: 12, type: "long")
    # =========================================================================
    {
        "id": "u1-q21",
        "type": "long",
        "marks": 12,
        "question": "Describe Measures of Dispersion in biological data: Range, Quartile Deviation, Mean Deviation, Standard Deviation, Variance, and Coefficient of Variation. Discuss their formulas, biological significance, and comparative merits.",
        "topicId": "u1-t06",
        "answer": (
            "<b>INTRODUCTION & DEFINITION:</b><br>"
            "Dispersion (or variation) measures the extent of scatter, spread, or deviation of individual observations around a central value (usually the arithmetic mean). "
            "Averages alone are inadequate: two herds of dairy cattle may both average 10 kg milk/day, but Herd A (9–11 kg) is highly uniform, while Herd B (2–18 kg) is wildly erratic. "
            "Measures of dispersion quantify this variation.<br><br>"
            "<b>I. ABSOLUTE MEASURES OF DISPERSION:</b><br>"
            "<ol>"
            "<li><b>Range (R):</b>"
            "<br>&bull; <i>Formula:</i> <code>R = X_max - X_min</code>."
            "<br>&bull; <i>Merits:</i> Simplest to calculate and understand."
            "<br>&bull; <i>Demerits:</i> Based on only two extreme values; highly unstable under sampling fluctuations. Used in farm quality control charts.</li>"
            "<li><b>Quartile Deviation (Semi-Interquartile Range - QD):</b>"
            "<br>&bull; <i>Formula:</i> <code>QD = (Q_3 - Q_1) / 2</code> (where Q1 = 25th percentile, Q3 = 75th percentile)."
            "<br>&bull; <i>Merits:</i> Completely immune to extreme outliers; can be calculated for open-ended frequency distributions."
            "<br>&bull; <i>Demerits:</i> Ignores the central 50% distribution of observations; incapable of further algebraic operations.</li>"
            "<li><b>Mean Deviation (MD):</b>"
            "<br>&bull; <i>Formula:</i> <code>MD = &Sigma; |X - \\bar{X}| / n</code> (or about Median)."
            "<br>&bull; <i>Demerits:</i> Disregards mathematical algebraic signs (treating negative deviations as positive absolute values), rendering it mathematically non-rigorous.</li>"
            "<li><b>Variance (s&sup2;) & Standard Deviation (s):</b>"
            "<br>&bull; Introduced by Karl Pearson (1893); the gold standard of absolute dispersion."
            "<br>&bull; <i>Sample Variance Formula:</i> <code>s&sup2; = [ &Sigma;X&sup2; - (&Sigma;X)&sup2;/n ] / (n - 1)</code> (Uses Bessel's correction <code>n - 1</code> for unbiased estimation)."
            "<br>&bull; <i>Standard Deviation:</i> <code>s = &radic;(s&sup2;)</code>."
            "<br>&bull; <i>Merits:</i> Based on all observations; mathematically tractable; squared deviations overcome the sign problem without arbitrary absolute bars; forms the basis of ANOVA and heritability.</li>"
            "</ol><br>"
            "<b>II. RELATIVE MEASURES OF DISPERSION (COEFFICIENT OF VARIATION):</b><br>"
            "<code>CV% = (s / \\bar{X}) &times; 100</code><br>"
            "<ul>"
            "<li>Pure, unitless percentage enabling direct comparison between traits with different units (e.g. body weight in kg vs milk yield in liters).</li>"
            "<li><b>Flock Uniformity Benchmark:</b> In broiler chickens, <code>CV &le; 8%</code> signifies excellent flock uniformity; <code>CV &gt; 14%</code> indicates underlying disease or uneven feed distribution.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Dispersion quantifies the scatter of observations around central tendency.",
            "Range: Simplest, Xmax - Xmin, highly sensitive to extremes.",
            "Quartile Deviation: (Q3 - Q1) / 2, robust against outliers, used with median.",
            "Mean Deviation: Ignores negative signs, mathematically non-rigorous.",
            "Standard Deviation: s = √(SS / (n-1)), gold standard based on all values with Bessel's correction.",
            "Coefficient of Variation: CV% = (s / X̄) * 100, unitless measure of relative variability.",
            "Biological relevance: Flock uniformity in poultry, reference interval determination in clinical pathology."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Summary of Measures of Dispersion",
            "headers": ["Measure", "Formula (Sample)", "Mathematical Rigor", "Sensitivity to Outliers", "Primary Veterinary Utility"],
            "rows": [
                ["Range", "X_max - X_min", "Lowest (only 2 values)", "Extreme sensitivity", "Milk cooling tank temperature monitoring"],
                ["Quartile Deviation", "(Q_3 - Q_1) / 2", "Moderate (positional)", "Completely immune", "Skewed somatic cell counts / parasite egg counts"],
                ["Mean Deviation", "&Sigma;|X - \\bar{X}| / n", "Low (ignores signs)", "Moderate", "Economic reporting of livestock sales"],
                ["Standard Deviation", "&radic;[ &Sigma;(X - \\bar{X})&sup2; / (n-1) ]", "Highest (algebraically sound)", "Sensitive to extremes", "Estimating heritability, Z-tests, t-tests, ANOVA"],
                ["Coefficient of Variation", "(s / \\bar{X}) &times; 100", "Highest (dimensionless)", "Reflects SD sensitivity", "Broiler flock weight uniformity, trial precision"]
            ]
        },
        "pyq": ["IVRI 2019", "TANUVAS 2022", "VCI Annual 2021", "GADVASU 2023"]
    },
    {
        "id": "u1-q22",
        "type": "long",
        "marks": 12,
        "question": "Give a detailed account of the Normal Distribution: Mathematical equation, essential properties of standard normal curve, area under the curve (Empirical Rule), and veterinary clinical applications.",
        "topicId": "u1-t11",
        "answer": (
            "<b>INTRODUCTION & DISCOVERY:</b><br>"
            "The <b>Normal Distribution</b> (Gaussian Distribution), discovered by Abraham de Moivre (1733) and developed by Carl Friedrich Gauss (1809), "
            "is the most vital continuous probability distribution in biological, medical, and quantitative genetic science. "
            "Under the <b>Central Limit Theorem</b>, polygenic quantitative traits (milk yield, body weight, fleece weight) influenced by thousands of small-effect genes and environmental factors naturally follow a normal distribution.<br><br>"
            "<b>MATHEMATICAL PROBABILITY DENSITY FUNCTION (PDF):</b><br>"
            "<code>f(X) = [ 1 / (&sigma; &times; &radic;(2&pi;)) ] &times; e^{ - (X - &mu;)&sup2; / (2&sigma;&sup2;) }</code> &nbsp;&nbsp;&nbsp;&nbsp; (-&infin; &lt; X &lt; +&infin;)<br>"
            "Where: <code>&mu;</code> = Population Mean; <code>&sigma;</code> = Population Standard Deviation; <code>&pi; &approx; 3.14159</code>; <code>e &approx; 2.71828</code>.<br><br>"
            "<b>THE STANDARD NORMAL DISTRIBUTION (Z-DISTRIBUTION):</b><br>"
            "By substituting the standard normal variate <code>Z = (X - &mu;) / &sigma;</code>, the distribution is transformed into <code>Z ~ N(0, 1)</code> with Mean <code>&mu; = 0</code> and Variance <code>&sigma;&sup2; = 1</code>:<br>"
            "<code>&phi;(Z) = [ 1 / &radic;(2&pi;) ] &times; e^{ - Z&sup2; / 2 }</code>.<br><br>"
            "<b>ESSENTIAL BIOMETRICAL PROPERTIES:</b>"
            "<ol>"
            "<li><b>Unimodal and Bell-Shaped:</b> Symmetrical about the vertical axis passing through <code>Z = 0</code>.</li>"
            "<li><b>Coincidence of Central Tendencies:</b> <code>Mean = Median = Mode = &mu;</code>.</li>"
            "<li><b>Skewness & Kurtosis:</b> Skewness coefficient <code>&beta;_1 = 0</code> (unskewed); Kurtosis <code>&beta;_2 = 3</code> (Mesokurtic).</li>"
            "<li><b>Points of Inflexion:</b> The curvature changes from convex to concave at exactly <code>X = &mu; &plusmn; &sigma;</code>.</li>"
            "<li><b>Total Probability Area:</b> Total area under the curve is exactly <b>1.0 (100%)</b>.</li>"
            "</ol><br>"
            "<b>THE EMPIRICAL RULE (AREA UNDER THE CURVE):</b>"
            "<ul>"
            "<li><code>&mu; &plusmn; 1&sigma;</code> encloses <b>68.27%</b> of all biological observations (approx. 2/3 of herd).</li>"
            "<li><code>&mu; &plusmn; 1.96&sigma;</code> encloses <b>95.00%</b> (95% Confidence Interval boundaries).</li>"
            "<li><code>&mu; &plusmn; 2&sigma;</code> encloses <b>95.45%</b> (Clinical reference interval limits).</li>"
            "<li><code>&mu; &plusmn; 2.58&sigma;</code> encloses <b>99.00%</b>.</li>"
            "<li><code>&mu; &plusmn; 3&sigma;</code> encloses <b>99.73%</b> (Practically the entire population).</li>"
            "</ul><br>"
            "<b>VETERINARY & CLINICAL APPLICATIONS:</b>"
            "<ol>"
            "<li><b>Establishing Clinical Reference Intervals:</b> In clinical biochemistry, normal physiological ranges (e.g. serum calcium 9.0–11.5 mg/dl, blood urea nitrogen, total protein) are established as <code>&mu; &plusmn; 2&sigma;</code> in healthy animal cohorts.</li>"
            "<li><b>Livestock Selection Thresholds:</b> Calculating truncation selection points to identify top 1%, 5%, or 10% elite breeding sires.</li>"
            "<li><b>Statistical Inference Engine:</b> Forms the mathematical foundation for large-sample Z-tests, Student's t-test, F-test, and ANOVA.</li>"
            "</ol>"
        ),
        "keyPoints": [
            "Mathematical PDF: f(X) = [1 / (σ√(2π))] * e^[-(X-μ)² / (2σ²)].",
            "Standard Normal Variate: Z = (X - μ) / σ with Mean = 0, SD = 1.",
            "Symmetrical, bell-shaped, mesokurtic (β2 = 3), Mean = Median = Mode.",
            "Empirical Rule: μ ± 1σ = 68.27%, μ ± 2σ = 95.45%, μ ± 3σ = 99.73%.",
            "95% CI boundaries: Z = ± 1.96; 99% CI: Z = ± 2.58.",
            "Points of inflexion occur at X = μ ± 1σ.",
            "Clinical uses: Serum biochemical reference ranges (μ ± 2σ), selection truncation lines."
        ],
        "diagram": "",
        "table": {
            "title": "Area Under the Standard Normal Curve (Critical Z-Values)",
            "headers": ["Z-Score Range", "Area Enclosed (%)", "Area in Both Tails (%)", "Veterinary Biological Application"],
            "rows": [
                ["&mu; &plusmn; 1.00 &sigma;", "68.27%", "31.73%", "Typical average herd performance zone"],
                ["&mu; &plusmn; 1.645 &sigma;", "90.00%", "10.00% (5% each tail)", "One-tailed 5% significance threshold"],
                ["&mu; &plusmn; 1.96 &sigma;", "95.00%", "5.00% (2.5% each tail)", "Two-tailed 5% significance & 95% Confidence Interval"],
                ["&mu; &plusmn; 2.00 &sigma;", "95.45%", "4.55%", "Standard Clinical Pathology Reference Interval"],
                ["&mu; &plusmn; 2.58 &sigma;", "99.00%", "1.00% (0.5% each tail)", "Two-tailed 1% significance threshold (Highly Significant)"],
                ["&mu; &plusmn; 3.00 &sigma;", "99.73%", "0.27%", "Natural biological variation limits in livestock"]
            ]
        },
        "pyq": ["VCI Annual 2020", "IVRI 2021", "RAJUVAS 2022", "KVAFSU 2023"]
    },
    {
        "id": "u1-q23",
        "type": "long",
        "marks": 12,
        "question": "Discuss Large Sample Tests (Z-test) in biological research: Single Mean, Difference of Two Means, Single Proportion, and Difference Between Two Proportions. Detail hypotheses, test statistics, and decision rules.",
        "topicId": "u1-t15",
        "answer": (
            "<b>INTRODUCTION & LARGE SAMPLE THEORY:</b><br>"
            "When the sample size is large (<b>n &ge; 30</b>), the sampling distribution of means and proportions approaches a normal distribution "
            "regardless of the shape of the parent population (<b>Central Limit Theorem</b>). "
            "Furthermore, the sample standard deviation (<code>s</code>) becomes a very close approximation of population standard deviation (<code>&sigma;</code>). "
            "Hence, the <b>Standard Normal Z-test</b> is applied.<br><br>"
            "<b>I. TEST FOR A SINGLE MEAN:</b>"
            "<ul>"
            "<li><i>Hypothesis:</i> <code>H0: &mu; = &mu;_0</code> vs <code>H1: &mu; &ne; &mu;_0</code>.</li>"
            "<li><i>Test Statistic:</i> <code>Z_cal = | \\bar{X} - &mu;_0 | / (s / &radic;n)</code>.</li>"
            "<li><i>Veterinary Example:</i> Testing whether a sample of 50 Sahiwal cows with mean lactation yield 2,650 kg differs significantly from the breed standard of 2,500 kg.</li>"
            "</ul><br>"
            "<b>II. TEST FOR DIFFERENCE OF TWO INDEPENDENT MEANS:</b>"
            "<ul>"
            "<li><i>Hypothesis:</i> <code>H0: &mu;_1 = &mu;_2</code> vs <code>H1: &mu;_1 &ne; &mu;_2</code>.</li>"
            "<li><i>Standard Error of Difference:</i> <code>SE = &radic;[ (s_1&sup2; / n_1) + (s_2&sup2; / n_2) ]</code>.</li>"
            "<li><i>Test Statistic:</i> <code>Z_cal = | \\bar{X}_1 - \\bar{X}_2 | / &radic;[ (s_1&sup2; / n_1) + (s_2&sup2; / n_2) ]</code>.</li>"
            "<li><i>Veterinary Example:</i> Comparing daily milk yield between bypass-fat fed buffaloes (n1=50) and control buffaloes (n2=50).</li>"
            "</ul><br>"
            "<b>III. TEST FOR A SINGLE PROPORTION:</b>"
            "<ul>"
            "<li><i>Hypothesis:</i> <code>H0: P = P_0</code> vs <code>H1: P &ne; P_0</code>.</li>"
            "<li><i>Sample Proportion:</i> <code>p = x / n</code> (where x = number of successes).</li>"
            "<li><i>Test Statistic:</i> <code>Z_cal = | p - P_0 | / &radic;[ P_0(1 - P_0) / n ]</code>.</li>"
            "<li><i>Veterinary Example:</i> Verifying whether conception rate under AI in a district (p = 0.42, n = 200) conforms to the state standard (P = 0.50).</li>"
            "</ul><br>"
            "<b>IV. TEST FOR DIFFERENCE OF TWO PROPORTIONS:</b>"
            "<ul>"
            "<li><i>Hypothesis:</i> <code>H0: P_1 = P_2</code> vs <code>H1: P_1 &ne; P_2</code>.</li>"
            "<li><i>Pooled Proportion:</i> <code>\\hat{P} = (x_1 + x_2) / (n_1 + n_2)</code>; <code>\\hat{Q} = 1 - \\hat{P}</code>.</li>"
            "<li><i>Test Statistic:</i> <code>Z_cal = | p_1 - p_2 | / &radic;[ \\hat{P}\\hat{Q} &times; (1/n_1 + 1/n_2) ]</code>.</li>"
            "<li><i>Veterinary Example:</i> Comparing cure rates between two antibiotic formulations in bovine mastitis.</li>"
            "</ul><br>"
            "<b>DECISION RULES (TWO-TAILED TEST):</b>"
            "<ol>"
            "<li>If <code>|Z_cal| &lt; 1.96</code>: Accept H0 (P &gt; 0.05, Difference is Non-Significant).</li>"
            "<li>If <code>1.96 &le; |Z_cal| &lt; 2.58</code>: Reject H0 at 5% level (P &lt; 0.05, Significant difference).</li>"
            "<li>If <code>|Z_cal| &ge; 2.58</code>: Reject H0 at 1% level (P &lt; 0.01, Highly Significant difference).</li>"
            "</ol>"
        ),
        "keyPoints": [
            "Applicable when sample size n ≥ 30 (Central Limit Theorem).",
            "Single mean: Z = |X̄ - μ| / (s / √n).",
            "Two means: Z = |X̄1 - X̄2| / √[(s1²/n1) + (s2²/n2)].",
            "Single proportion: Z = |p - P| / √[P(1-P)/n].",
            "Two proportions: Z = |p1 - p2| / √[P̂Q̂(1/n1 + 1/n2)] using pooled proportion P̂.",
            "Decision rule: Critical values 1.96 (5%) and 2.58 (1%).",
            "Does not require Student's t-distribution degrees of freedom."
        ],
        "diagram": "",
        "table": {
            "title": "Master Formulas and Decision Criteria for Large Sample Z-Tests",
            "headers": ["Test Category", "Null Hypothesis (H0)", "Standard Error Formula (SE)", "Test Statistic (Z_cal)", "5% Critical Value"],
            "rows": [
                ["Single Mean", "&mu; = &mu;_0", "s / &radic;n", "|\\bar{X} - &mu;_0| / SE", "1.96"],
                ["Two Independent Means", "&mu;_1 = &mu;_2", "&radic;[ (s_1&sup2;/n_1) + (s_2&sup2;/n_2) ]", "|\\bar{X}_1 - \\bar{X}_2| / SE", "1.96"],
                ["Single Proportion", "P = P_0", "&radic;[ P_0(1 - P_0) / n ]", "|p - P_0| / SE", "1.96"],
                ["Two Proportions", "P_1 = P_2", "&radic;[ \\hat{P}\\hat{Q}(1/n_1 + 1/n_2) ]", "|p_1 - p_2| / SE", "1.96"]
            ]
        },
        "pyq": ["IVRI 2020", "TANUVAS 2021", "WBUAFS 2022", "MAFSU 2023"]
    },
    {
        "id": "u1-q24",
        "type": "long",
        "marks": 12,
        "question": "Give a comprehensive account of the Chi-Square Test (χ²): Principle, Test of Goodness of Fit, Test of Independence in contingency tables, Yates' correction, and mandatory validity conditions.",
        "topicId": "u1-t17",
        "answer": (
            "<b>INTRODUCTION & PRINCIPLE:</b><br>"
            "Developed by Karl Pearson (1900), the <b>Chi-Square (&chi;&sup2;) Test</b> is a non-parametric statistical test used to compare "
            "observed frequencies (<code>O</code>) with theoretically expected frequencies (<code>E</code>) derived under a specific null hypothesis. "
            "It evaluates whether discrepancies between observed counts and theoretical predictions are attributable to random chance sampling fluctuations.<br><br>"
            "<b>GENERAL TEST STATISTIC FORMULA:</b><br>"
            "<code>&chi;&sup2; = &Sigma; [ (O - E)&sup2; / E ]</code><br>"
            "Where: <code>O</code> = Observed Frequency; <code>E</code> = Expected Frequency under H0.<br><br>"
            "<b>I. TEST OF GOODNESS OF FIT (MENDELIAN SEGREGATION):</b>"
            "<ul>"
            "<li>Tests whether sample phenotypic counts conform to theoretical genetic ratios (e.g. 3:1, 9:3:3:1, 1:1).</li>"
            "<li><i>Degrees of Freedom:</i> <code>df = k - 1</code> (where k = number of phenotypic classes).</li>"
            "<li><i>Genetic Example:</i> Testing whether polled vs horned calves from heterozygous matings fit the 3:1 Mendelian expectation.</li>"
            "</ul><br>"
            "<b>II. TEST OF INDEPENDENCE OF ATTRIBUTES (CONTINGENCY TABLES):</b>"
            "<ul>"
            "<li>Tests whether two categorical biological traits (e.g. Breed vs Mastitis incidence; Vaccination vs Disease survival) are independent or statistically associated.</li>"
            "<li><i>Expected Frequency Formula:</i> <code>E_ij = (Row Total_i &times; Column Total_j) / Grand Total (N)</code>.</li>"
            "<li><i>Degrees of Freedom:</i> <code>df = (r - 1) &times; (c - 1)</code> (where r = rows, c = columns).</li>"
            "<li><i>2&times;2 Contingency Table Shortcut:</i><br>"
            "<code>&chi;&sup2; = [ N &times; (ad - bc)&sup2; ] / [ (a + b)(c + d)(a + c)(b + d) ]</code> with <code>df = 1</code>.</li>"
            "</ul><br>"
            "<b>III. YATES' CORRECTION FOR CONTINUITY:</b>"
            "<ul>"
            "<li>Mandatory for <b>2&times;2 tables (df = 1)</b> when any expected cell frequency <code>E &lt; 5</code>.</li>"
            "<li>Formula: <code>&chi;&sup2;_{corr} = [ N &times; (|ad - bc| - N/2)&sup2; ] / [ (a+b)(c+d)(a+c)(b+d) ]</code>.</li>"
            "<li>Prevents over-estimation of significance when approximating discrete binomial data with continuous &chi;&sup2;.</li>"
            "</ul><br>"
            "<b>IV. MANDATORY CONDITIONS FOR VALIDITY:</b>"
            "<ol>"
            "<li>Data must be in raw frequency counts (never percentages or proportions).</li>"
            "<li>Total sample size <code>N</code> should be reasonably large (&ge; 50).</li>"
            "<li>Observations must be mutually exclusive and independently sampled.</li>"
            "<li><b>Minimum Expected Frequency Rule:</b> No expected cell frequency <code>E</code> should be less than 5. If <code>E &lt; 5</code> in tables with df &gt; 1, adjacent classes must be pooled (pooled categories reduce df by 1).</li>"
            "<li>Sum of observed frequencies must equal sum of expected frequencies: <code>&Sigma; O = &Sigma; E = N</code>.</li>"
            "</ol>"
        ),
        "keyPoints": [
            "Formula: χ² = Σ [(O - E)² / E].",
            "Goodness of Fit tests conformance to Mendelian ratios (df = k - 1).",
            "Independence tests attribute association: df = (r - 1)(c - 1).",
            "Expected frequency: E = (Row Total * Column Total) / Grand Total.",
            "2x2 shortcut: χ² = [N(ad - bc)²] / [(a+b)(c+d)(a+c)(b+d)].",
            "Yates' correction: Subtract N/2 from |ad - bc| when df=1 and E < 5.",
            "Validity conditions: N ≥ 50, raw counts only, E ≥ 5 in all cells, ΣO = ΣE.",
            "Critical χ² at df=1: 3.841 (5%) and 6.635 (1%)."
        ],
        "diagram": "",
        "table": {
            "title": "Chi-Square (χ²) Critical Values for Common Degrees of Freedom",
            "headers": ["Degrees of Freedom (df)", "5% Critical Value (P = 0.05)", "1% Critical Value (P = 0.01)", "0.1% Critical Value (P = 0.001)", "Common Veterinary Scenario"],
            "rows": [
                ["1", "3.841", "6.635", "10.828", "Monohybrid 3:1 ratio / 2x2 contingency table"],
                ["2", "5.991", "9.210", "13.816", "Incomplete dominance 1:2:1 ratio / 2x3 table"],
                ["3", "7.815", "11.345", "16.266", "Dihybrid 9:3:3:1 ratio / 2x4 table"],
                ["4", "9.488", "13.277", "18.467", "3x3 Contingency Table (df = 2x2 = 4)"],
                ["5", "11.070", "15.086", "20.515", "Multiple phenotypic allele classes"]
            ]
        },
        "pyq": ["IVRI 2022", "LUVAS 2021", "TANUVAS 2023", "VCI Annual 2022"]
    },
    {
        "id": "u1-q25",
        "type": "long",
        "marks": 12,
        "question": "Explain Analysis of Variance (ANOVA) for Completely Randomized Design (CRD) and Randomized Block Design (RBD): Mathematical models, partitioning of variance, ANOVA tables, F-test, and Critical Difference (CD).",
        "topicId": "u1-t19",
        "answer": (
            "<b>INTRODUCTION & BIOMETRICAL CONCEPT:</b><br>"
            "<b>Analysis of Variance (ANOVA)</b>, developed by Sir Ronald A. Fisher (1925), is a powerful biometrical technique "
            "that partitions the total phenotypic variation in an experiment into identifiable components attributable to specific treatments "
            "and an unassigned experimental error. It overcomes the limitation of the t-test by allowing simultaneous comparison of <b>three or more treatment means</b> "
            "without inflating the Type I error rate.<br><br>"
            "<b>I. COMPLETELY RANDOMIZED DESIGN (CRD — ONE-WAY ANOVA):</b><br>"
            "<ul>"
            "<li><b>Linear Additive Model:</b> <code>Y_{ij} = &mu; + &tau;_i + &epsilon;_{ij}</code>"
            "<br>Where <code>Y_{ij}</code> = observation; <code>&mu;</code> = general mean; <code>&tau;_i</code> = effect of i-th treatment; <code>&epsilon;_{ij}</code> = random experimental error ~ N(0, &sigma;&sup2;_e).</li>"
            "<li><b>Partitioning of Sum of Squares:</b> <code>TSS = TrSS + ESS</code> (Total SS = Treatment SS + Error SS)."
            "<br>&bull; Correction Factor: <code>CF = G&sup2; / N</code>."
            "<br>&bull; Total SS: <code>TSS = &Sigma;&Sigma; Y_{ij}&sup2; - CF</code> (df = N - 1)."
            "<br>&bull; Treatment SS: <code>TrSS = &Sigma; (T_i&sup2; / r_i) - CF</code> (df = k - 1)."
            "<br>&bull; Error SS: <code>ESS = TSS - TrSS</code> (df = N - k).</li>"
            "<li><b>F-Test:</b> <code>F_cal = TrMS / EMS = [ TrSS / (k - 1) ] / [ ESS / (N - k) ]</code>.</li>"
            "</ul><br>"
            "<b>II. RANDOMIZED BLOCK DESIGN (RBD — TWO-WAY ANOVA):</b><br>"
            "<ul>"
            "<li><b>Linear Additive Model:</b> <code>Y_{ij} = &mu; + &tau;_i + &beta;_j + &epsilon;_{ij}</code>"
            "<br>Where <code>&beta;_j</code> = effect of j-th block.</li>"
            "<li><b>Partitioning of Sum of Squares:</b> <code>TSS = TrSS + BSS + ESS</code>."
            "<br>&bull; Block SS: <code>BSS = &Sigma; (B_j&sup2; / k) - CF</code> (df = r - 1)."
            "<br>&bull; Error SS: <code>ESS = TSS - TrSS - BSS</code> with <code>df = (k - 1)(r - 1)</code>.</li>"
            "<li><b>F-Test for Treatments:</b> <code>F_cal = TrMS / EMS</code> with df = (k - 1, (k - 1)(r - 1)).</li>"
            "</ul><br>"
            "<b>III. CRITICAL DIFFERENCE (CD / LSD) FOR MEAN SEPARATION:</b><br>"
            "If the F-test indicates significant treatment differences (<code>P &lt; 0.05</code>), pair-wise comparison of treatment means is conducted using Critical Difference:<br><br>"
            "<code>CD = t_tab(df_{error}, &alpha;) &times; SE_d = t_tab &times; &radic;[ 2 &times; EMS / r ]</code><br><br>"
            "<b>Decision:</b> If <code>| \\bar{Y}_A - \\bar{Y}_B | &gt; CD</code>, Treatment A and Treatment B are declared statistically significantly different at level &alpha;.<br><br>"
            "<b>VETERINARY APPLICATION:</b>"
            "Testing multiple broiler rations (e.g. 0%, 5%, 10%, 15% Azolla meal) on 6-week body weight gains (CRD), or evaluating milk yield under different concentrate feeds across dairy cows blocked by parity (RBD)."
        ),
        "keyPoints": [
            "ANOVA partitions total variation into treatment and experimental error components.",
            "CRD Linear Model: Yij = μ + τi + εij; TSS = TrSS + ESS.",
            "RBD Linear Model: Yij = μ + τi + βj + εij; TSS = TrSS + BSS + ESS.",
            "Correction Factor: CF = G² / N.",
            "F-test statistic: F = TrMS / EMS; tests H0: τ1 = τ2 = ... = τk = 0.",
            "Error df: N - k in CRD; (k - 1)(r - 1) in RBD.",
            "Critical Difference formula: CD = t_tab * √(2 * EMS / r).",
            "If difference between two means exceeds CD, they differ significantly."
        ],
        "diagram": "",
        "table": {
            "title": "Complete Master ANOVA Summary Table for Randomized Block Design (RBD)",
            "headers": ["Source of Variation", "Degrees of Freedom (df)", "Sum of Squares (SS)", "Mean Square (MS)", "F_calculated", "F_tabulated"],
            "rows": [
                ["Replications (Blocks)", "r - 1", "BSS = &Sigma;(Bj²/k) - CF", "BMS = BSS / (r - 1)", "BMS / EMS", "F_tab(r-1, df_e)"],
                ["Treatments", "k - 1", "TrSS = &Sigma;(Ti²/r) - CF", "TrMS = TrSS / (k - 1)", "TrMS / EMS", "F_tab(k-1, df_e)"],
                ["Experimental Error", "(k - 1)(r - 1)", "ESS = TSS - TrSS - BSS", "EMS = ESS / df_e", "—", "—"],
                ["Total", "N - 1 = rk - 1", "TSS = &Sigma;&Sigma;Yij² - CF", "—", "—", "—"]
            ]
        },
        "pyq": ["VCI Annual 2021", "IVRI 2020", "TANUVAS 2022", "GADVASU 2023"]
    }
]
