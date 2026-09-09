/* ============================================================
   data-qa.JS  —  Written Exam Question Bank
   Animal Genetics & Breeding (VCI MSVE 2016 Standard)
   2nd Year B.V.Sc. & A.H.
   Total 75 High-Yield Model Q&As:
   - 36 x 2-Mark Definitions
   - 24 x 5-Mark Short Notes / Differences
   - 15 x 12-Mark Long Essays
   ============================================================ */

var qaBank = {
  "unit-1": [
    {
      "id": "u1-q01",
      "type": "define",
      "marks": 2,
      "question": "Define Biostatistics and state its primary scope in veterinary science.",
      "topicId": "u1-t01",
      "answer": "<b>Biostatistics</b> (or Biometry) is the application of statistical principles, methods, and mathematical probability to the collection, compilation, presentation, analysis, and interpretation of biological, medical, and veterinary data.<br><br><b>Scope in Veterinary Medicine:</b><ul><li>Designing clinical vaccine and anthelmintic efficacy trials.</li><li>Evaluating genetic parameters (heritability, breeding values) in livestock improvement.</li><li>Epidemiological disease surveillance and setting normal clinical biochemical reference intervals.</li></ul>",
      "keyPoints": [
        "Definition as application of statistics to biological/veterinary data.",
        "Key scope: Clinical trials, genetic parameter estimation, disease surveillance."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2021",
        "TANUVAS 2022",
        "GADVASU 2023"
      ]
    },
    {
      "id": "u1-q02",
      "type": "define",
      "marks": 2,
      "question": "Define Parameter and Statistic. Give two examples of each.",
      "topicId": "u1-t03",
      "answer": "<ul><li><b>Parameter:</b> Any numerical descriptive measure computed from the <i>entire population</i>. It is a constant, fixed value, typically denoted by Greek letters.<br><i>Examples:</i> Population Mean (<code>&mu;</code>), Population Standard Deviation (<code>&sigma;</code>), Population Variance (<code>&sigma;&sup2;</code>).</li><li><b>Statistic:</b> Any numerical descriptive measure computed from a <i>sample</i> drawn from the population. It is a random variable that varies from sample to sample, denoted by Roman letters.<br><i>Examples:</i> Sample Mean (<code>\\bar{X}</code>), Sample Standard Deviation (<code>s</code>), Sample Variance (<code>s&sup2;</code>).</li></ul>",
      "keyPoints": [
        "Parameter: Characteristic of entire population (constant, Greek letters μ, σ).",
        "Statistic: Characteristic of a sample (variable, Roman letters X̄, s)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2019",
        "WBUAFS 2022"
      ]
    },
    {
      "id": "u1-q03",
      "type": "define",
      "marks": 2,
      "question": "State Sturges' Rule for determining the number of class intervals in a frequency distribution.",
      "topicId": "u1-t02",
      "answer": "<b>Sturges' Rule</b> is an empirical biometrical formula used to determine the optimal number of class intervals (<code>k</code>) when constructing a continuous grouped frequency distribution from <code>N</code> raw observations:<br><br><code>k = 1 + 3.322 &times; log10(N)</code><br><br>Where:<ul><li><code>k</code> = Number of class intervals (rounded to nearest integer).</li><li><code>N</code> = Total number of observations (sample size).</li><li><code>Class Width (h)</code> = <code>Range / k = (X_max - X_min) / k</code>.</li></ul>",
      "keyPoints": [
        "Formula: k = 1 + 3.322 * log10(N).",
        "Class width formula: h = Range / k."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "MAFSU 2020",
        "KVAFSU 2023"
      ]
    },
    {
      "id": "u1-q04",
      "type": "define",
      "marks": 2,
      "question": "Define Cumulative Frequency Curve (Ogive) and state its primary graphical application.",
      "topicId": "u1-t04",
      "answer": "An <b>Ogive</b> is a smooth, S-shaped (sigmoidal) graphical curve obtained by plotting cumulative frequencies against class boundaries.<br><ul><li><b>Less-than Ogive:</b> Plots 'less-than' cumulative frequencies against <i>upper class boundaries</i> (rising curve).</li><li><b>More-than Ogive:</b> Plots 'more-than' cumulative frequencies against <i>lower class boundaries</i> (falling curve).</li></ul><b>Primary Application:</b> The perpendicular dropped to the X-axis from the point where 'Less-than' and 'More-than' ogives intersect determines the <b>Median</b> (as well as quartiles Q1, Q3 and percentiles) graphically.",
      "keyPoints": [
        "Sigmoidal curve plotting cumulative frequency against class boundaries.",
        "Intersection of less-than and more-than ogives gives graphical Median."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "RAJUVAS 2021",
        "SVVU 2022"
      ]
    },
    {
      "id": "u1-q05",
      "type": "define",
      "marks": 2,
      "question": "Define Mode and state the empirical relationship between Mean, Median, and Mode.",
      "topicId": "u1-t05",
      "answer": "<b>Mode</b> is that value of a variable which occurs with the greatest frequency in a distribution (the most common or typical observation).<br><br><b>Empirical Relationship:</b> In a moderately asymmetrical (skewed) biological distribution, the relationship formulated by Karl Pearson is:<br><code>Mode = 3 &times; Median - 2 &times; Mean</code><br>Or: <code>Mean - Mode = 3 &times; (Mean - Median)</code>.",
      "keyPoints": [
        "Mode is the observation occurring with maximum frequency.",
        "Empirical formula: Mode = 3 * Median - 2 * Mean."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2020",
        "LUVAS 2021"
      ]
    },
    {
      "id": "u1-q06",
      "type": "define",
      "marks": 2,
      "question": "Define Coefficient of Variation (CV%) and state why it is preferred over Standard Deviation.",
      "topicId": "u1-t07",
      "answer": "<b>Coefficient of Variation (CV%)</b> is the relative measure of dispersion expressing standard deviation as a percentage of the arithmetic mean:<br><code>CV% = (s / \\bar{X}) &times; 100</code><br><br><b>Why Preferred:</b><ul><li>CV is a <b>pure, unitless number</b> (dimensionless).</li><li>Enables direct comparison of variability between traits with completely different units of measurement (e.g., comparing variability of body weight in kg vs milk yield in liters, or flock uniformity in broilers).</li></ul>",
      "keyPoints": [
        "Formula: CV% = (s / X̄) * 100.",
        "Unitless measure enabling comparison across different traits and units."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2023",
        "NDVSU 2022"
      ]
    },
    {
      "id": "u1-q07",
      "type": "define",
      "marks": 2,
      "question": "Enumerate four essential properties of the Standard Normal Curve.",
      "topicId": "u1-t11",
      "answer": "<ol><li><b>Bell-shaped and Perfectly Symmetrical:</b> Symmetrical about <code>Z = 0</code>; Skewness <code>&beta;_1 = 0</code>, Kurtosis <code>&beta;_2 = 3</code> (Mesokurtic).</li><li><b>Coincident Averages:</b> <code>Mean = Median = Mode = 0</code>; Standard Deviation <code>&sigma; = 1</code>.</li><li><b>Asymptotic Tails:</b> Tails extend infinitely in both directions, approaching but never touching the horizontal axis.</li><li><b>Total Area Unity:</b> Total area under curve is <b>1.0 (100%)</b>; <code>&mu; &plusmn; 1&sigma; = 68.27%</code>, <code>&mu; &plusmn; 2&sigma; = 95.45%</code>, <code>&mu; &plusmn; 3&sigma; = 99.73%</code>.</li></ol>",
      "keyPoints": [
        "Mean = Median = Mode = 0; SD = 1.",
        "Area: μ ± 1σ = 68.27%, μ ± 2σ = 95.45%, μ ± 3σ = 99.73%."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2022",
        "GADVASU 2021"
      ]
    },
    {
      "id": "u1-q08",
      "type": "define",
      "marks": 2,
      "question": "Define Pearson's Correlation Coefficient (r) and state its mathematical range.",
      "topicId": "u1-t12",
      "answer": "<b>Pearson's Product-Moment Correlation Coefficient (r)</b> is a mathematical measure of the degree, strength, and direction of linear association between two continuous quantitative biological variables (X and Y):<br><br><code>r = Cov(X, Y) / [ &sigma;_X &times; &sigma;_Y ] = SP_xy / &radic;(SS_x &times; SS_y)</code><br><br><b>Mathematical Range:</b> Strictly bounded between <b>-1.0 and +1.0</b> (<code>-1 &le; r &le; +1</code>).<br>&bull; <code>r = +1</code>: Perfect positive linear correlation.<br>&bull; <code>r = -1</code>: Perfect negative linear correlation.<br>&bull; <code>r = 0</code>: Zero linear correlation.",
      "keyPoints": [
        "Measures linear relationship: r = Cov(X,Y) / (σX * σY).",
        "Range: -1.0 to +1.0."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2019",
        "WBUAFS 2021"
      ]
    },
    {
      "id": "u1-q09",
      "type": "define",
      "marks": 2,
      "question": "Define Null Hypothesis (H0) and Alternative Hypothesis (H1).",
      "topicId": "u1-t15",
      "answer": "<ul><li><b>Null Hypothesis (H0):</b> A hypothesis of no difference, no effect, or no association formulated for possible rejection. It states that any observed difference between sample statistic and population parameter is purely due to chance sampling error.<br><i>Example:</i> <code>H0: &mu;_1 = &mu;_2</code> (New anthelmintic does not alter mean fecal egg counts).</li><li><b>Alternative Hypothesis (H1):</b> A hypothesis that complements and contradicts H0, accepted when H0 is rejected. It indicates a real, statistically significant biological effect.<br><i>Example:</i> <code>H1: &mu;_1 &ne; &mu;_2</code> (Two-tailed) or <code>H1: &mu;_1 &gt; &mu;_2</code> (One-tailed).</li></ul>",
      "keyPoints": [
        "H0: Hypothesis of no difference/effect, set up for rejection.",
        "H1: Statement of actual biological difference, accepted when H0 rejected."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "RAJUVAS 2022",
        "SVVU 2021"
      ]
    },
    {
      "id": "u1-q10",
      "type": "define",
      "marks": 2,
      "question": "Differentiate between Type I Error and Type II Error in hypothesis testing.",
      "topicId": "u1-t15",
      "answer": "<ul><li><b>Type I Error (&alpha; Error):</b> The error committed by <b>rejecting the null hypothesis (H0) when it is actually TRUE</b>. The probability of committing Type I error is the <b>Level of Significance (&alpha;)</b> (commonly fixed at 0.05 or 0.01).<br><i>Clinical analogy:</i> Falsely declaring a healthy cow to be diseased (False Positive).</li><li><b>Type II Error (&beta; Error):</b> The error committed by <b>accepting (failing to reject) H0 when it is actually FALSE</b>. The probability is denoted by <code>&beta;</code>, and <code>(1 - &beta;)</code> is the <b>Power of the Test</b>.<br><i>Clinical analogy:</i> Falsely clearing a truly infected cow as healthy (False Negative).</li></ul>",
      "keyPoints": [
        "Type I Error (α): Rejecting true H0 (False Positive).",
        "Type II Error (β): Failing to reject false H0 (False Negative); Power = 1 - β."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "LUVAS 2022",
        "TANUVAS 2020"
      ]
    },
    {
      "id": "u1-q11",
      "type": "define",
      "marks": 2,
      "question": "Define Degrees of Freedom (df) in biostatistics and give an example.",
      "topicId": "u1-t16",
      "answer": "<b>Degrees of Freedom (df)</b> is the total number of independent observations or values in a statistical calculation that are free to vary after imposing necessary mathematical restrictions or constraints (such as sample mean or sample total).<br><br><code>df = Total observations (n) - Number of independent constraints (k)</code><br><br><i>Example:</i> In calculating sample variance <code>s&sup2;</code> from <code>n</code> observations, one constraint is imposed because deviations must sum to zero (<code>&Sigma;(X - \\bar{X}) = 0</code>). Hence, <code>df = n - 1</code>.",
      "keyPoints": [
        "Number of independent values free to vary minus number of restrictions.",
        "df = n - 1 in sample variance because one degree of freedom is lost estimating mean."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2022",
        "MAFSU 2021"
      ]
    },
    {
      "id": "u1-q12",
      "type": "define",
      "marks": 2,
      "question": "State the three fundamental principles of experimental design formulated by Sir R.A. Fisher.",
      "topicId": "u1-t18",
      "answer": "<ol><li><b>Replication:</b> Repetition of the experimental treatments under identical conditions to provide an estimate of experimental error and increase precision.</li><li><b>Randomization:</b> Allocation of experimental treatments to experimental units strictly by chance, ensuring unbiased estimates of treatment means and valid error variance.</li><li><b>Local Control:</b> Grouping or blocking heterogeneous experimental units into homogenous blocks (e.g., blocking cows by parity or body weight) to isolate extraneous variation from experimental error.</li></ol>",
      "keyPoints": [
        "Three principles: Replication, Randomization, and Local Control.",
        "Replication estimates error; Randomization eliminates bias; Local Control reduces error."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2021",
        "KVAFSU 2022"
      ]
    },
    {
      "id": "u1-q13",
      "type": "diff",
      "marks": 5,
      "question": "Differentiate between Primary Data and Secondary Data. Explain methods of collecting primary livestock data.",
      "topicId": "u1-t01",
      "answer": "<b>DEFINITION AND CONTRAST:</b><br>Biological and livestock data are classified into Primary and Secondary based on original source and collection agency.<br><br><b>METHODS OF COLLECTING PRIMARY LIVESTOCK DATA:</b><ol><li><b>Direct Personal Observation / Measurement:</b> The veterinarian directly measures animal parameters using calibrated instruments (e.g., weighing calves on platform scales, recording milk yields via flow meters, taking rectal temperatures). Highest accuracy.</li><li><b>Questionnaires & Farmer Interviews:</b> Distributed structured schedules to livestock owners during field surveys (e.g., recording daily feed intake, grazing hours, estrus observations).</li><li><b>Automated Electronic Sensors:</b> Modern IoT sensors such as RFID tags, rumination collars, pedometers, and automated milking system (AMS) computer logs.</li></ol>",
      "keyPoints": [
        "Primary data: First-hand, original data collected directly for specific study.",
        "Secondary data: Pre-existing data compiled from published records/databases.",
        "Collection methods: Direct measurement, farmer questionnaires, RFID/sensor logs."
      ],
      "diagram": "",
      "table": {
        "title": "Comparison Between Primary and Secondary Biological Data",
        "headers": [
          "Parameter / Criterion",
          "Primary Data",
          "Secondary Data"
        ],
        "rows": [
          [
            "Origin",
            "First-hand, original collection by investigator",
            "Second-hand; gathered from pre-existing records"
          ],
          [
            "Collection Cost & Time",
            "High cost, labor-intensive, time-consuming",
            "Low cost, rapid, easily accessible"
          ],
          [
            "Reliability & Accuracy",
            "Highly reliable; investigator controls protocol",
            "Variable; depends on original reporting accuracy"
          ],
          [
            "Veterinary Example",
            "Weighing 50 heifers directly on farm scale",
            "Analyzing 10-year milk yield records from farm registers"
          ]
        ]
      },
      "pyq": [
        "IVRI 2020",
        "TANUVAS 2021",
        "NDVSU 2023"
      ]
    },
    {
      "id": "u1-q14",
      "type": "short",
      "marks": 5,
      "question": "Describe the properties, comparative merits, and demerits of Arithmetic Mean and Median in biological data.",
      "topicId": "u1-t05",
      "answer": "<b>I. ARITHMETIC MEAN (\\bar{X}):</b><ul><li><b>Properties:</b> Rigidly defined; based on all observations; algebraic manipulations possible (<code>&Sigma;(X - \\bar{X}) = 0</code>; Combined Mean formula <code>\\bar{X}_{12} = (n_1 \\bar{X}_1 + n_2 \\bar{X}_2)/(n_1 + n_2)</code>).</li><li><b>Merits:</b> Most stable and reliable average; forms the mathematical engine of advanced biometrics (ANOVA, regression, heritability).</li><li><b>Demerits:</b> Severely distorted by extreme outliers; cannot be calculated for open-ended frequency classes.</li></ul><br><b>II. MEDIAN (M_e):</b><ul><li><b>Properties:</b> Positional average; divides arrayed distribution into two exactly equal halves (50% above, 50% below).</li><li><b>Merits:</b> Completely immune to extreme outliers; can be located graphically via ogives; can be computed for open-ended tables.</li><li><b>Demerits:</b> Not based on all observations; incapable of further algebraic treatment; higher sampling fluctuations.</li></ul><br><b>VETERINARY PREFERENCE RULE:</b> Use <b>Arithmetic Mean</b> for symmetrical livestock traits (body weight, gestation length). Use <b>Median</b> for highly skewed data with extreme outliers (Somatic Cell Count in mastitis, days open, parasite egg counts).",
      "keyPoints": [
        "Mean: Based on all values, mathematically tractable, highly sensitive to outliers.",
        "Median: Positional average, robust against extreme values and open-ended classes.",
        "Biological preference: Mean for normal traits, Median for skewed/parasitological data."
      ],
      "diagram": "",
      "table": {
        "title": "Comparison Between Arithmetic Mean and Median",
        "headers": [
          "Criterion",
          "Arithmetic Mean (\\bar{X})",
          "Median (M_e)"
        ],
        "rows": [
          [
            "Mathematical Basis",
            "Algebraic centroid (&Sigma;X / n)",
            "Positional middle value (N/2)"
          ],
          [
            "Sensitivity to Outliers",
            "Extremely sensitive (distorted by extremes)",
            "Completely robust (unaffected by extremes)"
          ],
          [
            "Further Algebraic Treatment",
            "Fully capable (combined mean, variance, ANOVA)",
            "Not capable of further algebraic manipulation"
          ],
          [
            "Graphical Determination",
            "Cannot be determined graphically",
            "Determined by intersection of Ogives"
          ]
        ]
      },
      "pyq": [
        "GADVASU 2020",
        "VCI Annual 2022"
      ]
    },
    {
      "id": "u1-q15",
      "type": "diff",
      "marks": 5,
      "question": "Differentiate between Standard Deviation (SD) and Standard Error of Mean (SE). Explain their clinical significance.",
      "topicId": "u1-t07",
      "answer": "<b>DEFINITIONS & FORMULAS:</b><ul><li><b>Standard Deviation (s):</b> The positive square root of the arithmetic mean of squared deviations from the mean: <code>s = &radic;[ &Sigma;(X - \\bar{X})&sup2; / (n - 1) ]</code>. Measures biological variation among individual animals.</li><li><b>Standard Error of Mean (SE):</b> The standard deviation of the sampling distribution of sample means: <code>SE_\\bar{x} = s / &radic;n</code>. Measures the precision and reliability of the estimated sample mean.</li></ul><br><b>CLINICAL & SCIENTIFIC SIGNIFICANCE:</b><ul><li><b>When to report SD:</b> When describing biological diversity and reference ranges within a herd (e.g., 'Normal cow rectal temperature = 38.6 &plusmn; 0.5&deg;C').</li><li><b>When to report SE:</b> When publishing experimental trial comparisons and constructing 95% Confidence Intervals: <code>\\bar{X} &plusmn; 1.96 &times; SE</code> (e.g., 'Mean milk yield of bypass-fat group = 14.2 &plusmn; 0.4 kg').</li></ul>",
      "keyPoints": [
        "SD measures individual biological variability within a population: s = √(SS / (n-1)).",
        "SE measures precision of the sample mean estimate: SE = s / √n.",
        "As sample size n increases, SD remains stable while SE decreases toward zero."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Distinction: Standard Deviation vs Standard Error",
        "headers": [
          "Feature / Parameter",
          "Standard Deviation (SD)",
          "Standard Error of Mean (SE)"
        ],
        "rows": [
          [
            "What it Measures",
            "Biological dispersion of individual animals around sample mean",
            "Sampling variability and precision of the sample mean"
          ],
          [
            "Formula",
            "s = &radic;[ &Sigma;(X - \\bar{X})&sup2; / (n - 1) ]",
            "SE_\\bar{x} = s / &radic;n"
          ],
          [
            "Effect of Increasing Sample Size (n)",
            "Remains stable (converges to population &sigma;)",
            "Decreases progressively toward zero (1/&radic;n rate)"
          ],
          [
            "Primary Reporting Purpose",
            "Clinical reference intervals (Mean &plusmn; 2 SD)",
            "Research trial treatment comparisons (Mean &plusmn; SE)"
          ]
        ]
      },
      "pyq": [
        "IVRI 2021",
        "WBUAFS 2023",
        "SVVU 2020"
      ]
    },
    {
      "id": "u1-q16",
      "type": "short",
      "marks": 5,
      "question": "Describe the Poisson Distribution: Mathematical equation, conditions of validity, and biological applications in veterinary medicine.",
      "topicId": "u1-t10",
      "answer": "<b>DEFINITION & PROBABILITY MASS FUNCTION:</b><br>The <b>Poisson Distribution</b>, formulated by Sim&eacute;on Denis Poisson (1837), is a discrete probability distribution for modeling the occurrence of rare biological events in a continuous continuum of time, space, or volume:<br><br><code>P(X = x) = (e^{-&lambda;} &times; &lambda;^x) / x!</code> &nbsp;&nbsp;&nbsp;&nbsp; (for x = 0, 1, 2, ...)<br>Where: <code>&lambda;</code> = Mean rate of occurrence per unit interval; <code>e &approx; 2.71828</code>.<br><br><b>DISTINCTIVE BIOMETRICAL PROPERTIES:</b><ul><li><b>Single Parameter Distribution:</b> Completely defined by a single parameter <code>&lambda;</code>.</li><li><b>Equidispersion Identity:</b> <code>Mean = Variance = &lambda;</code> (Mean equals Variance!).</li></ul><br><b>CONDITIONS OF VALIDITY:</b><ol><li>Number of trials <code>n</code> is very large (<code>n &rarr; &infin;</code>).</li><li>Probability of event occurrence <code>p</code> is extremely small (rare event, <code>p &rarr; 0</code>).</li><li>Their product is a finite constant: <code>np = &lambda;</code>.</li></ol><br><b>VETERINARY BIOLOGICAL EXAMPLES:</b><ul><li>Hemocytometer counts of red/white blood cells per counting chamber grid square.</li><li>Bacterial colony counts (CFU) on agar culture plates.</li><li>Occurrence of rare congenital malformations (e.g., dicephalus calves) in a dairy population.</li><li>Dairy cow twinning rate under natural mating conditions.</li></ul>",
      "keyPoints": [
        "Formula: P(X=x) = (e^-λ * λ^x) / x!.",
        "Single parameter distribution where Mean = Variance = λ.",
        "Applicable for rare events with large n and very small p (np = λ).",
        "Veterinary uses: Hemocytometer blood counts, CFU bacterial plates, congenital birth defects."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "RAJUVAS 2020",
        "TANUVAS 2022"
      ]
    },
    {
      "id": "u1-q17",
      "type": "short",
      "marks": 5,
      "question": "Explain Linear Regression and Regression Coefficients (b_yx and b_xy). State the mathematical relationships between regression and correlation.",
      "topicId": "u1-t13",
      "answer": "<b>DEFINITION:</b><br><b>Regression Analysis</b> estimates the mathematical functional relationship between a dependent variable (Y) and one or more independent variables (X), enabling quantitative prediction of Y from known values of X.<br><br><b>REGRESSION COEFFICIENTS:</b><ul><li><b>Regression Coefficient of Y on X (b_yx):</b> Measures the average unit change in Y per unit increase in X:<br><code>b_yx = SP_xy / SS_x = r &times; (s_y / s_x)</code></li><li><b>Regression Coefficient of X on Y (b_xy):</b> Measures the unit change in X per unit increase in Y:<br><code>b_xy = SP_xy / SS_y = r &times; (s_x / s_y)</code></li></ul><br><b>MATHEMATICAL RELATIONSHIPS (EXAM SCORING RULES):</b><ol><li><b>Geometric Mean Property:</b> The correlation coefficient is the geometric mean of the two regression coefficients:<br><code>r = &plusmn; &radic;(b_yx &times; b_xy)</code>.</li><li><b>Sign Consistency:</b> Both regression coefficients and the correlation coefficient must have the <b>identical algebraic sign</b> (all positive or all negative).</li><li><b>Magnitude Restriction:</b> If one regression coefficient is greater than 1.0, the other must be less than 1.0 (since <code>b_yx &times; b_xy = r&sup2; &le; 1.0</code>).</li><li><b>Intersection Point:</b> The two regression lines always intersect at the point of their means: <code>(\\bar{X}, \\bar{Y})</code>.</li></ol>",
      "keyPoints": [
        "b_yx = SPxy / SSx = r * (sy / sx); measures unit change in Y per unit X.",
        "r = ± √(b_yx * b_xy) (geometric mean property).",
        "Both regression slopes and r share the exact same algebraic sign.",
        "The two regression lines intersect at the coordinates of their means (X̄, Ȳ)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "MAFSU 2022",
        "IVRI 2023",
        "LUVAS 2021"
      ]
    },
    {
      "id": "u1-q18",
      "type": "short",
      "marks": 5,
      "question": "Short note on Student's Paired t-test: Principle, Assumptions, Formula, and Clinical Application.",
      "topicId": "u1-t16",
      "answer": "<b>PRINCIPLE:</b><br>The <b>Paired t-test</b> is applied when two sets of observations are intrinsically paired or matched—most commonly in <b>'Before-and-After' clinical trials</b> conducted on the exact same group of animals. It eliminates inter-animal variation, isolating the true therapeutic drug effect.<br><br><b>ASSUMPTIONS:</b><ol><li>Observations are paired and drawn randomly.</li><li>The differences <code>d_i = X_{after} - X_{before}</code> follow a normal distribution.</li></ol><br><b>FORMULAS & DEGREES OF FREEDOM:</b><ul><li>Individual difference: <code>d_i = X_{2i} - X_{1i}</code>.</li><li>Mean difference: <code>\\bar{d} = (&Sigma; d) / n</code>.</li><li>Standard deviation of differences: <code>s_d = &radic;[ { &Sigma;d&sup2; - (&Sigma;d)&sup2;/n } / (n - 1) ]</code>.</li><li>Standard Error: <code>SE_\\bar{d} = s_d / &radic;n</code>.</li><li><b>Test Statistic:</b> <code>t_cal = | \\bar{d} | / (s_d / &radic;n)</code> with <b>df = n - 1</b> (where n = number of pairs).</li></ul><br><b>CLINICAL APPLICATION:</b>Testing anthelmintic efficacy by comparing fecal egg counts (EPG) in 10 sheep <i>before dosing</i> vs <i>14 days post-dosing</i>; or testing antipyretic drugs by recording rectal temperatures before vs 2 hours post-injection.",
      "keyPoints": [
        "Used for before-and-after trials on the same animals (paired design).",
        "Eliminates inter-animal baseline variation, drastically increasing test sensitivity.",
        "Formula: t = d̄ / (sd / √n) with df = n - 1.",
        "Veterinary uses: Anthelmintic trials (EPG drop), antipyretic drug evaluations."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2021",
        "KVAFSU 2020",
        "VCI Annual 2020"
      ]
    },
    {
      "id": "u1-q19",
      "type": "short",
      "marks": 5,
      "question": "What is Yates' Correction for Continuity in Chi-Square Test? State when and why it is applied.",
      "topicId": "u1-t17",
      "answer": "<b>DEFINITION & CONCEPT:</b><br><b>Yates' Correction for Continuity</b>, introduced by Frank Yates (1934), is a mathematical adjustment applied to the 2&times;2 contingency Chi-Square test to correct for approximating a discrete binomial distribution with a continuous Chi-Square distribution.<br><br><b>FORMULA FOR 2&times;2 CONTINGENCY TABLE:</b><br><code>&chi;&sup2;_{corrected} = [ N &times; ( |ad - bc| - N/2 )&sup2; ] / [ (a + b)(c + d)(a + c)(b + d) ]</code><br>Where <code>a, b, c, d</code> are cell frequencies and <code>N = a + b + c + d</code>.<br><br><b>WHEN TO APPLY (MANDATORY CONDITIONS):</b><ol><li>Applicable <b>strictly when degrees of freedom df = 1</b> (i.e. 2&times;2 contingency tables).</li><li>Applied when any expected cell frequency is small (<b>E &lt; 5</b>) and total sample size N is between 20 and 40.</li></ol><br><b>WHY APPLIED:</b>Without Yates' correction, the uncorrected &chi;&sup2; value is systematically over-estimated (inflated), leading to false rejection of true null hypotheses (Type I error). Subtracting <code>N/2</code> from <code>|ad - bc|</code> reduces the calculated &chi;&sup2;, making the test conservative and statistically valid.",
      "keyPoints": [
        "Yates' correction adjusts for approximating discrete frequencies with a continuous curve.",
        "Formula: χ² = [ N * (|ad - bc| - N/2)² ] / [ (a+b)(c+d)(a+c)(b+d) ].",
        "Mandatory condition: df = 1 (2x2 table) and any expected cell frequency E < 5.",
        "Prevents inflation of test statistic and controls Type I error."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "WBUAFS 2022",
        "IVRI 2022",
        "NDVSU 2021"
      ]
    },
    {
      "id": "u1-q20",
      "type": "diff",
      "marks": 5,
      "question": "Differentiate between Completely Randomized Design (CRD) and Randomized Block Design (RBD).",
      "topicId": "u1-t18",
      "answer": "<b>CORE CONCEPTS:</b><br>CRD and RBD are fundamental agricultural and veterinary experimental designs differing in local control and layout.<br><br><b>PRIMARY DIFFERENCES:</b><ul><li><b>CRD:</b> Treatments are assigned randomly across the entire experimental material without grouping. Relies on only 2 principles: <b>Randomization and Replication</b>. Best suited for homogenous laboratory conditions (broiler chicks of identical age/weight in battery brooders; in-vitro cell culture).</li><li><b>RBD:</b> Experimental units are grouped into homogenous blocks along one known source of variation (e.g., initial body weight, parity, lactation yield). Treatments are randomly assigned within each block. Utilizes all 3 principles: <b>Randomization, Replication, and Local Control</b>. Standard for large animal farm trials (dairy cattle feeding trials).</li></ul>",
      "keyPoints": [
        "CRD uses 2 principles (Randomization, Replication); assumes homogenous units.",
        "RBD uses all 3 principles (adds Local Control via blocking in one direction).",
        "Error df in CRD: N - k; Error df in RBD: (k - 1)(r - 1).",
        "RBD isolates block variation, yielding smaller error variance and higher precision."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Comparison: CRD vs RBD Experimental Designs",
        "headers": [
          "Criterion / Feature",
          "Completely Randomized Design (CRD)",
          "Randomized Block Design (RBD)"
        ],
        "rows": [
          [
            "Principles Applied",
            "2 (Randomization & Replication)",
            "3 (Randomization, Replication & Local Control)"
          ],
          [
            "Experimental Material",
            "Completely homogenous throughout",
            "Heterogeneous in one direction (blocked into homogenous groups)"
          ],
          [
            "Layout & Blocking",
            "Zero blocking; treatments assigned at random",
            "Replications organized into distinct blocks"
          ],
          [
            "Degrees of Freedom for Error",
            "N - k = k(r - 1)",
            "(k - 1)(r - 1)"
          ],
          [
            "Precision & Efficiency",
            "Lower if units are heterogeneous",
            "Higher (isolates block variance from error)"
          ],
          [
            "Field Veterinary Application",
            "Laboratory broiler chick trials / Petrie dishes",
            "Dairy cattle feeding trials (blocked by parity/yield)"
          ]
        ]
      },
      "pyq": [
        "RAJUVAS 2021",
        "TANUVAS 2023",
        "VCI Annual 2019"
      ]
    },
    {
      "id": "u1-q21",
      "type": "long",
      "marks": 12,
      "question": "Describe Measures of Dispersion in biological data: Range, Quartile Deviation, Mean Deviation, Standard Deviation, Variance, and Coefficient of Variation. Discuss their formulas, biological significance, and comparative merits.",
      "topicId": "u1-t06",
      "answer": "<b>INTRODUCTION & DEFINITION:</b><br>Dispersion (or variation) measures the extent of scatter, spread, or deviation of individual observations around a central value (usually the arithmetic mean). Averages alone are inadequate: two herds of dairy cattle may both average 10 kg milk/day, but Herd A (9–11 kg) is highly uniform, while Herd B (2–18 kg) is wildly erratic. Measures of dispersion quantify this variation.<br><br><b>I. ABSOLUTE MEASURES OF DISPERSION:</b><br><ol><li><b>Range (R):</b><br>&bull; <i>Formula:</i> <code>R = X_max - X_min</code>.<br>&bull; <i>Merits:</i> Simplest to calculate and understand.<br>&bull; <i>Demerits:</i> Based on only two extreme values; highly unstable under sampling fluctuations. Used in farm quality control charts.</li><li><b>Quartile Deviation (Semi-Interquartile Range - QD):</b><br>&bull; <i>Formula:</i> <code>QD = (Q_3 - Q_1) / 2</code> (where Q1 = 25th percentile, Q3 = 75th percentile).<br>&bull; <i>Merits:</i> Completely immune to extreme outliers; can be calculated for open-ended frequency distributions.<br>&bull; <i>Demerits:</i> Ignores the central 50% distribution of observations; incapable of further algebraic operations.</li><li><b>Mean Deviation (MD):</b><br>&bull; <i>Formula:</i> <code>MD = &Sigma; |X - \\bar{X}| / n</code> (or about Median).<br>&bull; <i>Demerits:</i> Disregards mathematical algebraic signs (treating negative deviations as positive absolute values), rendering it mathematically non-rigorous.</li><li><b>Variance (s&sup2;) & Standard Deviation (s):</b><br>&bull; Introduced by Karl Pearson (1893); the gold standard of absolute dispersion.<br>&bull; <i>Sample Variance Formula:</i> <code>s&sup2; = [ &Sigma;X&sup2; - (&Sigma;X)&sup2;/n ] / (n - 1)</code> (Uses Bessel's correction <code>n - 1</code> for unbiased estimation).<br>&bull; <i>Standard Deviation:</i> <code>s = &radic;(s&sup2;)</code>.<br>&bull; <i>Merits:</i> Based on all observations; mathematically tractable; squared deviations overcome the sign problem without arbitrary absolute bars; forms the basis of ANOVA and heritability.</li></ol><br><b>II. RELATIVE MEASURES OF DISPERSION (COEFFICIENT OF VARIATION):</b><br><code>CV% = (s / \\bar{X}) &times; 100</code><br><ul><li>Pure, unitless percentage enabling direct comparison between traits with different units (e.g. body weight in kg vs milk yield in liters).</li><li><b>Flock Uniformity Benchmark:</b> In broiler chickens, <code>CV &le; 8%</code> signifies excellent flock uniformity; <code>CV &gt; 14%</code> indicates underlying disease or uneven feed distribution.</li></ul>",
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
        "headers": [
          "Measure",
          "Formula (Sample)",
          "Mathematical Rigor",
          "Sensitivity to Outliers",
          "Primary Veterinary Utility"
        ],
        "rows": [
          [
            "Range",
            "X_max - X_min",
            "Lowest (only 2 values)",
            "Extreme sensitivity",
            "Milk cooling tank temperature monitoring"
          ],
          [
            "Quartile Deviation",
            "(Q_3 - Q_1) / 2",
            "Moderate (positional)",
            "Completely immune",
            "Skewed somatic cell counts / parasite egg counts"
          ],
          [
            "Mean Deviation",
            "&Sigma;|X - \\bar{X}| / n",
            "Low (ignores signs)",
            "Moderate",
            "Economic reporting of livestock sales"
          ],
          [
            "Standard Deviation",
            "&radic;[ &Sigma;(X - \\bar{X})&sup2; / (n-1) ]",
            "Highest (algebraically sound)",
            "Sensitive to extremes",
            "Estimating heritability, Z-tests, t-tests, ANOVA"
          ],
          [
            "Coefficient of Variation",
            "(s / \\bar{X}) &times; 100",
            "Highest (dimensionless)",
            "Reflects SD sensitivity",
            "Broiler flock weight uniformity, trial precision"
          ]
        ]
      },
      "pyq": [
        "IVRI 2019",
        "TANUVAS 2022",
        "VCI Annual 2021",
        "GADVASU 2023"
      ]
    },
    {
      "id": "u1-q22",
      "type": "long",
      "marks": 12,
      "question": "Give a detailed account of the Normal Distribution: Mathematical equation, essential properties of standard normal curve, area under the curve (Empirical Rule), and veterinary clinical applications.",
      "topicId": "u1-t11",
      "answer": "<b>INTRODUCTION & DISCOVERY:</b><br>The <b>Normal Distribution</b> (Gaussian Distribution), discovered by Abraham de Moivre (1733) and developed by Carl Friedrich Gauss (1809), is the most vital continuous probability distribution in biological, medical, and quantitative genetic science. Under the <b>Central Limit Theorem</b>, polygenic quantitative traits (milk yield, body weight, fleece weight) influenced by thousands of small-effect genes and environmental factors naturally follow a normal distribution.<br><br><b>MATHEMATICAL PROBABILITY DENSITY FUNCTION (PDF):</b><br><code>f(X) = [ 1 / (&sigma; &times; &radic;(2&pi;)) ] &times; e^{ - (X - &mu;)&sup2; / (2&sigma;&sup2;) }</code> &nbsp;&nbsp;&nbsp;&nbsp; (-&infin; &lt; X &lt; +&infin;)<br>Where: <code>&mu;</code> = Population Mean; <code>&sigma;</code> = Population Standard Deviation; <code>&pi; &approx; 3.14159</code>; <code>e &approx; 2.71828</code>.<br><br><b>THE STANDARD NORMAL DISTRIBUTION (Z-DISTRIBUTION):</b><br>By substituting the standard normal variate <code>Z = (X - &mu;) / &sigma;</code>, the distribution is transformed into <code>Z ~ N(0, 1)</code> with Mean <code>&mu; = 0</code> and Variance <code>&sigma;&sup2; = 1</code>:<br><code>&phi;(Z) = [ 1 / &radic;(2&pi;) ] &times; e^{ - Z&sup2; / 2 }</code>.<br><br><b>ESSENTIAL BIOMETRICAL PROPERTIES:</b><ol><li><b>Unimodal and Bell-Shaped:</b> Symmetrical about the vertical axis passing through <code>Z = 0</code>.</li><li><b>Coincidence of Central Tendencies:</b> <code>Mean = Median = Mode = &mu;</code>.</li><li><b>Skewness & Kurtosis:</b> Skewness coefficient <code>&beta;_1 = 0</code> (unskewed); Kurtosis <code>&beta;_2 = 3</code> (Mesokurtic).</li><li><b>Points of Inflexion:</b> The curvature changes from convex to concave at exactly <code>X = &mu; &plusmn; &sigma;</code>.</li><li><b>Total Probability Area:</b> Total area under the curve is exactly <b>1.0 (100%)</b>.</li></ol><br><b>THE EMPIRICAL RULE (AREA UNDER THE CURVE):</b><ul><li><code>&mu; &plusmn; 1&sigma;</code> encloses <b>68.27%</b> of all biological observations (approx. 2/3 of herd).</li><li><code>&mu; &plusmn; 1.96&sigma;</code> encloses <b>95.00%</b> (95% Confidence Interval boundaries).</li><li><code>&mu; &plusmn; 2&sigma;</code> encloses <b>95.45%</b> (Clinical reference interval limits).</li><li><code>&mu; &plusmn; 2.58&sigma;</code> encloses <b>99.00%</b>.</li><li><code>&mu; &plusmn; 3&sigma;</code> encloses <b>99.73%</b> (Practically the entire population).</li></ul><br><b>VETERINARY & CLINICAL APPLICATIONS:</b><ol><li><b>Establishing Clinical Reference Intervals:</b> In clinical biochemistry, normal physiological ranges (e.g. serum calcium 9.0–11.5 mg/dl, blood urea nitrogen, total protein) are established as <code>&mu; &plusmn; 2&sigma;</code> in healthy animal cohorts.</li><li><b>Livestock Selection Thresholds:</b> Calculating truncation selection points to identify top 1%, 5%, or 10% elite breeding sires.</li><li><b>Statistical Inference Engine:</b> Forms the mathematical foundation for large-sample Z-tests, Student's t-test, F-test, and ANOVA.</li></ol>",
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
        "headers": [
          "Z-Score Range",
          "Area Enclosed (%)",
          "Area in Both Tails (%)",
          "Veterinary Biological Application"
        ],
        "rows": [
          [
            "&mu; &plusmn; 1.00 &sigma;",
            "68.27%",
            "31.73%",
            "Typical average herd performance zone"
          ],
          [
            "&mu; &plusmn; 1.645 &sigma;",
            "90.00%",
            "10.00% (5% each tail)",
            "One-tailed 5% significance threshold"
          ],
          [
            "&mu; &plusmn; 1.96 &sigma;",
            "95.00%",
            "5.00% (2.5% each tail)",
            "Two-tailed 5% significance & 95% Confidence Interval"
          ],
          [
            "&mu; &plusmn; 2.00 &sigma;",
            "95.45%",
            "4.55%",
            "Standard Clinical Pathology Reference Interval"
          ],
          [
            "&mu; &plusmn; 2.58 &sigma;",
            "99.00%",
            "1.00% (0.5% each tail)",
            "Two-tailed 1% significance threshold (Highly Significant)"
          ],
          [
            "&mu; &plusmn; 3.00 &sigma;",
            "99.73%",
            "0.27%",
            "Natural biological variation limits in livestock"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2020",
        "IVRI 2021",
        "RAJUVAS 2022",
        "KVAFSU 2023"
      ]
    },
    {
      "id": "u1-q23",
      "type": "long",
      "marks": 12,
      "question": "Discuss Large Sample Tests (Z-test) in biological research: Single Mean, Difference of Two Means, Single Proportion, and Difference Between Two Proportions. Detail hypotheses, test statistics, and decision rules.",
      "topicId": "u1-t15",
      "answer": "<b>INTRODUCTION & LARGE SAMPLE THEORY:</b><br>When the sample size is large (<b>n &ge; 30</b>), the sampling distribution of means and proportions approaches a normal distribution regardless of the shape of the parent population (<b>Central Limit Theorem</b>). Furthermore, the sample standard deviation (<code>s</code>) becomes a very close approximation of population standard deviation (<code>&sigma;</code>). Hence, the <b>Standard Normal Z-test</b> is applied.<br><br><b>I. TEST FOR A SINGLE MEAN:</b><ul><li><i>Hypothesis:</i> <code>H0: &mu; = &mu;_0</code> vs <code>H1: &mu; &ne; &mu;_0</code>.</li><li><i>Test Statistic:</i> <code>Z_cal = | \\bar{X} - &mu;_0 | / (s / &radic;n)</code>.</li><li><i>Veterinary Example:</i> Testing whether a sample of 50 Sahiwal cows with mean lactation yield 2,650 kg differs significantly from the breed standard of 2,500 kg.</li></ul><br><b>II. TEST FOR DIFFERENCE OF TWO INDEPENDENT MEANS:</b><ul><li><i>Hypothesis:</i> <code>H0: &mu;_1 = &mu;_2</code> vs <code>H1: &mu;_1 &ne; &mu;_2</code>.</li><li><i>Standard Error of Difference:</i> <code>SE = &radic;[ (s_1&sup2; / n_1) + (s_2&sup2; / n_2) ]</code>.</li><li><i>Test Statistic:</i> <code>Z_cal = | \\bar{X}_1 - \\bar{X}_2 | / &radic;[ (s_1&sup2; / n_1) + (s_2&sup2; / n_2) ]</code>.</li><li><i>Veterinary Example:</i> Comparing daily milk yield between bypass-fat fed buffaloes (n1=50) and control buffaloes (n2=50).</li></ul><br><b>III. TEST FOR A SINGLE PROPORTION:</b><ul><li><i>Hypothesis:</i> <code>H0: P = P_0</code> vs <code>H1: P &ne; P_0</code>.</li><li><i>Sample Proportion:</i> <code>p = x / n</code> (where x = number of successes).</li><li><i>Test Statistic:</i> <code>Z_cal = | p - P_0 | / &radic;[ P_0(1 - P_0) / n ]</code>.</li><li><i>Veterinary Example:</i> Verifying whether conception rate under AI in a district (p = 0.42, n = 200) conforms to the state standard (P = 0.50).</li></ul><br><b>IV. TEST FOR DIFFERENCE OF TWO PROPORTIONS:</b><ul><li><i>Hypothesis:</i> <code>H0: P_1 = P_2</code> vs <code>H1: P_1 &ne; P_2</code>.</li><li><i>Pooled Proportion:</i> <code>\\hat{P} = (x_1 + x_2) / (n_1 + n_2)</code>; <code>\\hat{Q} = 1 - \\hat{P}</code>.</li><li><i>Test Statistic:</i> <code>Z_cal = | p_1 - p_2 | / &radic;[ \\hat{P}\\hat{Q} &times; (1/n_1 + 1/n_2) ]</code>.</li><li><i>Veterinary Example:</i> Comparing cure rates between two antibiotic formulations in bovine mastitis.</li></ul><br><b>DECISION RULES (TWO-TAILED TEST):</b><ol><li>If <code>|Z_cal| &lt; 1.96</code>: Accept H0 (P &gt; 0.05, Difference is Non-Significant).</li><li>If <code>1.96 &le; |Z_cal| &lt; 2.58</code>: Reject H0 at 5% level (P &lt; 0.05, Significant difference).</li><li>If <code>|Z_cal| &ge; 2.58</code>: Reject H0 at 1% level (P &lt; 0.01, Highly Significant difference).</li></ol>",
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
        "headers": [
          "Test Category",
          "Null Hypothesis (H0)",
          "Standard Error Formula (SE)",
          "Test Statistic (Z_cal)",
          "5% Critical Value"
        ],
        "rows": [
          [
            "Single Mean",
            "&mu; = &mu;_0",
            "s / &radic;n",
            "|\\bar{X} - &mu;_0| / SE",
            "1.96"
          ],
          [
            "Two Independent Means",
            "&mu;_1 = &mu;_2",
            "&radic;[ (s_1&sup2;/n_1) + (s_2&sup2;/n_2) ]",
            "|\\bar{X}_1 - \\bar{X}_2| / SE",
            "1.96"
          ],
          [
            "Single Proportion",
            "P = P_0",
            "&radic;[ P_0(1 - P_0) / n ]",
            "|p - P_0| / SE",
            "1.96"
          ],
          [
            "Two Proportions",
            "P_1 = P_2",
            "&radic;[ \\hat{P}\\hat{Q}(1/n_1 + 1/n_2) ]",
            "|p_1 - p_2| / SE",
            "1.96"
          ]
        ]
      },
      "pyq": [
        "IVRI 2020",
        "TANUVAS 2021",
        "WBUAFS 2022",
        "MAFSU 2023"
      ]
    },
    {
      "id": "u1-q24",
      "type": "long",
      "marks": 12,
      "question": "Give a comprehensive account of the Chi-Square Test (χ²): Principle, Test of Goodness of Fit, Test of Independence in contingency tables, Yates' correction, and mandatory validity conditions.",
      "topicId": "u1-t17",
      "answer": "<b>INTRODUCTION & PRINCIPLE:</b><br>Developed by Karl Pearson (1900), the <b>Chi-Square (&chi;&sup2;) Test</b> is a non-parametric statistical test used to compare observed frequencies (<code>O</code>) with theoretically expected frequencies (<code>E</code>) derived under a specific null hypothesis. It evaluates whether discrepancies between observed counts and theoretical predictions are attributable to random chance sampling fluctuations.<br><br><b>GENERAL TEST STATISTIC FORMULA:</b><br><code>&chi;&sup2; = &Sigma; [ (O - E)&sup2; / E ]</code><br>Where: <code>O</code> = Observed Frequency; <code>E</code> = Expected Frequency under H0.<br><br><b>I. TEST OF GOODNESS OF FIT (MENDELIAN SEGREGATION):</b><ul><li>Tests whether sample phenotypic counts conform to theoretical genetic ratios (e.g. 3:1, 9:3:3:1, 1:1).</li><li><i>Degrees of Freedom:</i> <code>df = k - 1</code> (where k = number of phenotypic classes).</li><li><i>Genetic Example:</i> Testing whether polled vs horned calves from heterozygous matings fit the 3:1 Mendelian expectation.</li></ul><br><b>II. TEST OF INDEPENDENCE OF ATTRIBUTES (CONTINGENCY TABLES):</b><ul><li>Tests whether two categorical biological traits (e.g. Breed vs Mastitis incidence; Vaccination vs Disease survival) are independent or statistically associated.</li><li><i>Expected Frequency Formula:</i> <code>E_ij = (Row Total_i &times; Column Total_j) / Grand Total (N)</code>.</li><li><i>Degrees of Freedom:</i> <code>df = (r - 1) &times; (c - 1)</code> (where r = rows, c = columns).</li><li><i>2&times;2 Contingency Table Shortcut:</i><br><code>&chi;&sup2; = [ N &times; (ad - bc)&sup2; ] / [ (a + b)(c + d)(a + c)(b + d) ]</code> with <code>df = 1</code>.</li></ul><br><b>III. YATES' CORRECTION FOR CONTINUITY:</b><ul><li>Mandatory for <b>2&times;2 tables (df = 1)</b> when any expected cell frequency <code>E &lt; 5</code>.</li><li>Formula: <code>&chi;&sup2;_{corr} = [ N &times; (|ad - bc| - N/2)&sup2; ] / [ (a+b)(c+d)(a+c)(b+d) ]</code>.</li><li>Prevents over-estimation of significance when approximating discrete binomial data with continuous &chi;&sup2;.</li></ul><br><b>IV. MANDATORY CONDITIONS FOR VALIDITY:</b><ol><li>Data must be in raw frequency counts (never percentages or proportions).</li><li>Total sample size <code>N</code> should be reasonably large (&ge; 50).</li><li>Observations must be mutually exclusive and independently sampled.</li><li><b>Minimum Expected Frequency Rule:</b> No expected cell frequency <code>E</code> should be less than 5. If <code>E &lt; 5</code> in tables with df &gt; 1, adjacent classes must be pooled (pooled categories reduce df by 1).</li><li>Sum of observed frequencies must equal sum of expected frequencies: <code>&Sigma; O = &Sigma; E = N</code>.</li></ol>",
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
        "headers": [
          "Degrees of Freedom (df)",
          "5% Critical Value (P = 0.05)",
          "1% Critical Value (P = 0.01)",
          "0.1% Critical Value (P = 0.001)",
          "Common Veterinary Scenario"
        ],
        "rows": [
          [
            "1",
            "3.841",
            "6.635",
            "10.828",
            "Monohybrid 3:1 ratio / 2x2 contingency table"
          ],
          [
            "2",
            "5.991",
            "9.210",
            "13.816",
            "Incomplete dominance 1:2:1 ratio / 2x3 table"
          ],
          [
            "3",
            "7.815",
            "11.345",
            "16.266",
            "Dihybrid 9:3:3:1 ratio / 2x4 table"
          ],
          [
            "4",
            "9.488",
            "13.277",
            "18.467",
            "3x3 Contingency Table (df = 2x2 = 4)"
          ],
          [
            "5",
            "11.070",
            "15.086",
            "20.515",
            "Multiple phenotypic allele classes"
          ]
        ]
      },
      "pyq": [
        "IVRI 2022",
        "LUVAS 2021",
        "TANUVAS 2023",
        "VCI Annual 2022"
      ]
    },
    {
      "id": "u1-q25",
      "type": "long",
      "marks": 12,
      "question": "Explain Analysis of Variance (ANOVA) for Completely Randomized Design (CRD) and Randomized Block Design (RBD): Mathematical models, partitioning of variance, ANOVA tables, F-test, and Critical Difference (CD).",
      "topicId": "u1-t19",
      "answer": "<b>INTRODUCTION & BIOMETRICAL CONCEPT:</b><br><b>Analysis of Variance (ANOVA)</b>, developed by Sir Ronald A. Fisher (1925), is a powerful biometrical technique that partitions the total phenotypic variation in an experiment into identifiable components attributable to specific treatments and an unassigned experimental error. It overcomes the limitation of the t-test by allowing simultaneous comparison of <b>three or more treatment means</b> without inflating the Type I error rate.<br><br><b>I. COMPLETELY RANDOMIZED DESIGN (CRD — ONE-WAY ANOVA):</b><br><ul><li><b>Linear Additive Model:</b> <code>Y_{ij} = &mu; + &tau;_i + &epsilon;_{ij}</code><br>Where <code>Y_{ij}</code> = observation; <code>&mu;</code> = general mean; <code>&tau;_i</code> = effect of i-th treatment; <code>&epsilon;_{ij}</code> = random experimental error ~ N(0, &sigma;&sup2;_e).</li><li><b>Partitioning of Sum of Squares:</b> <code>TSS = TrSS + ESS</code> (Total SS = Treatment SS + Error SS).<br>&bull; Correction Factor: <code>CF = G&sup2; / N</code>.<br>&bull; Total SS: <code>TSS = &Sigma;&Sigma; Y_{ij}&sup2; - CF</code> (df = N - 1).<br>&bull; Treatment SS: <code>TrSS = &Sigma; (T_i&sup2; / r_i) - CF</code> (df = k - 1).<br>&bull; Error SS: <code>ESS = TSS - TrSS</code> (df = N - k).</li><li><b>F-Test:</b> <code>F_cal = TrMS / EMS = [ TrSS / (k - 1) ] / [ ESS / (N - k) ]</code>.</li></ul><br><b>II. RANDOMIZED BLOCK DESIGN (RBD — TWO-WAY ANOVA):</b><br><ul><li><b>Linear Additive Model:</b> <code>Y_{ij} = &mu; + &tau;_i + &beta;_j + &epsilon;_{ij}</code><br>Where <code>&beta;_j</code> = effect of j-th block.</li><li><b>Partitioning of Sum of Squares:</b> <code>TSS = TrSS + BSS + ESS</code>.<br>&bull; Block SS: <code>BSS = &Sigma; (B_j&sup2; / k) - CF</code> (df = r - 1).<br>&bull; Error SS: <code>ESS = TSS - TrSS - BSS</code> with <code>df = (k - 1)(r - 1)</code>.</li><li><b>F-Test for Treatments:</b> <code>F_cal = TrMS / EMS</code> with df = (k - 1, (k - 1)(r - 1)).</li></ul><br><b>III. CRITICAL DIFFERENCE (CD / LSD) FOR MEAN SEPARATION:</b><br>If the F-test indicates significant treatment differences (<code>P &lt; 0.05</code>), pair-wise comparison of treatment means is conducted using Critical Difference:<br><br><code>CD = t_tab(df_{error}, &alpha;) &times; SE_d = t_tab &times; &radic;[ 2 &times; EMS / r ]</code><br><br><b>Decision:</b> If <code>| \\bar{Y}_A - \\bar{Y}_B | &gt; CD</code>, Treatment A and Treatment B are declared statistically significantly different at level &alpha;.<br><br><b>VETERINARY APPLICATION:</b>Testing multiple broiler rations (e.g. 0%, 5%, 10%, 15% Azolla meal) on 6-week body weight gains (CRD), or evaluating milk yield under different concentrate feeds across dairy cows blocked by parity (RBD).",
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
        "headers": [
          "Source of Variation",
          "Degrees of Freedom (df)",
          "Sum of Squares (SS)",
          "Mean Square (MS)",
          "F_calculated",
          "F_tabulated"
        ],
        "rows": [
          [
            "Replications (Blocks)",
            "r - 1",
            "BSS = &Sigma;(Bj²/k) - CF",
            "BMS = BSS / (r - 1)",
            "BMS / EMS",
            "F_tab(r-1, df_e)"
          ],
          [
            "Treatments",
            "k - 1",
            "TrSS = &Sigma;(Ti²/r) - CF",
            "TrMS = TrSS / (k - 1)",
            "TrMS / EMS",
            "F_tab(k-1, df_e)"
          ],
          [
            "Experimental Error",
            "(k - 1)(r - 1)",
            "ESS = TSS - TrSS - BSS",
            "EMS = ESS / df_e",
            "—",
            "—"
          ],
          [
            "Total",
            "N - 1 = rk - 1",
            "TSS = &Sigma;&Sigma;Yij² - CF",
            "—",
            "—",
            "—"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2021",
        "IVRI 2020",
        "TANUVAS 2022",
        "GADVASU 2023"
      ]
    }
  ],
  "unit-2": [
    {
      "id": "u2-q01",
      "type": "define",
      "marks": 2,
      "question": "State Mendel's Law of Segregation (First Law of Inheritance) and give its physical basis.",
      "topicId": "u2-t01",
      "answer": "<b>Mendel's Law of Segregation (Law of Purity of Gametes):</b><br>Alleles of a gene exist in pairs within somatic cells of an individual. During gametogenesis (meiosis), the two alleles segregate from each other cleanly without blending, such that each gamete receives only one allele of the pair with equal probability (50%).<br><br><b>Physical Basis:</b> The disjunction and separation of homologous chromosomes during Anaphase I of meiosis.",
      "keyPoints": [
        "Alleles exist in pairs and separate cleanly during gamete formation without blending.",
        "Each gamete carries only one allele of the pair (purity of gametes).",
        "Cytological basis: Disjunction of homologous chromosomes at Anaphase I."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2021",
        "KVASU 2022",
        "IVRI 2023"
      ]
    },
    {
      "id": "u2-q02",
      "type": "define",
      "marks": 2,
      "question": "State Mendel's Law of Independent Assortment and state when it fails.",
      "topicId": "u2-t01",
      "answer": "<b>Law of Independent Assortment (Mendel's Second Law):</b><br>When two or more pairs of independent, non-allelic genes are segregating simultaneously in a cross, the assortment or distribution of alleles of one gene pair into gametes is entirely independent of the distribution of alleles of any other gene pair.<br><br><b>Condition of Failure:</b> The law fails when genes are located close together on the same chromosome (i.e., genetically linked genes with complete or partial <b>linkage</b>).",
      "keyPoints": [
        "Independent distribution of different non-allelic gene pairs into gametes.",
        "Produces standard 9:3:3:1 dihybrid phenotypic ratio.",
        "Fails in presence of genetic linkage (syntenic genes on the same chromosome)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "GADVASU 2020",
        "RAJUVAS 2022",
        "MAFSU 2023"
      ]
    },
    {
      "id": "u2-q03",
      "type": "define",
      "marks": 2,
      "question": "Define Pleiotropy and give one authentic livestock example.",
      "topicId": "u2-t03",
      "answer": "<b>Pleiotropy:</b><br>A genetic phenomenon wherein a single gene or locus influences multiple, seemingly unrelated phenotypic traits or organ systems simultaneously.<br><br><b>Livestock Example:</b><br><ul><li><b>Merle gene (M) in Dogs:</b> Causes attractive mottled coat pigmentation, but in homozygous condition (<code>MM</code>) leads to microphthalmia, deafness, and ocular coloboma.</li><li><b>Polled gene (P) in Goats:</b> Dominant polledness allele is pleiotropically linked to recessive intersexuality / female pseudohermaphroditism in polled female goats (<code>PP</code>).</li></ul>",
      "keyPoints": [
        "Single gene influencing two or more distinct, unrelated phenotypic characteristics.",
        "Example: Polledness-intersexuality syndrome in goats or Merle coat/deafness in canines."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2019",
        "LUVAS 2021",
        "KVAFSU 2023"
      ]
    },
    {
      "id": "u2-q04",
      "type": "define",
      "marks": 2,
      "question": "Define Penetrance and Expressivity. Differentiate between complete and incomplete penetrance.",
      "topicId": "u2-t03",
      "answer": "<ul><li><b>Penetrance:</b> The percentage of individuals carrying a particular genotype who actually exhibit the corresponding phenotype (all-or-none statistical measure: <code>(Number showing phenotype / Number with genotype) &times; 100</code>). If less than 100%, it is termed <i>incomplete penetrance</i> (e.g., polydactyly in chickens).</li><li><b>Expressivity:</b> The degree or severity to which a penetrant gene is phenotypically expressed in an individual (qualitative/quantitative variation, e.g., variable spotting patterns in Holstein Friesian cattle).</li></ul>",
      "keyPoints": [
        "Penetrance: Percentage of genotype carriers showing the phenotype (all-or-none).",
        "Expressivity: Degree/intensity of phenotypic expression in penetrant individuals.",
        "Complete (100%) vs Incomplete (<100%) penetrance."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2020",
        "WBUAFS 2022"
      ]
    },
    {
      "id": "u2-q05",
      "type": "define",
      "marks": 2,
      "question": "What is Dosage Compensation? State Lyon's Hypothesis.",
      "topicId": "u2-t05",
      "answer": "<b>Dosage Compensation:</b> The genetic regulatory mechanism that equalizes the expression of X-linked genes between homogametic females (<code>XX</code>) having two doses and heterogametic males (<code>XY</code>) having only one dose.<br><br><b>Lyon's Hypothesis (Mary Lyon, 1961):</b><ul><li>In mammalian female somatic cells, one of the two X chromosomes is randomly and permanently inactivated during early embryonic development.</li><li>The inactivated X chromosome condenses into dense heterochromatin visible in interphase nuclei as a <b>Barr body</b> (sex chromatin).</li><li>Explains calico/tortoiseshell coat patterning in female cats (heterozygous <code>X<sup>B</sup>X<sup>O</sup></code>).</li></ul>",
      "keyPoints": [
        "Equalization of X-linked gene product levels between XX females and XY males.",
        "Random, permanent transcriptional inactivation of one X chromosome in female mammalian cells.",
        "Forms Barr body (condensed heterochromatin); causes cellular mosaicism."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "GADVASU 2021",
        "IVRI 2022",
        "DUVASU 2023"
      ]
    },
    {
      "id": "u2-q06",
      "type": "define",
      "marks": 2,
      "question": "Define Robertsonian Translocation (Centric Fusion) and cite its clinical impact in cattle.",
      "topicId": "u2-t10",
      "answer": "<b>Robertsonian Translocation (Centric Fusion):</b><br>A structural chromosomal rearrangement resulting from the whole-arm fusion of two acrocentric chromosomes at or near their centromeres, producing a single large bi-armed (metacentric or sub-metacentric) chromosome. The chromosome number is reduced by one (<code>2n - 1</code> in heterozygotes), but the fundamental arm number (NF) remains conserved.<br><br><b>Clinical Impact:</b> <b>rob(1;29) translocation</b> in cattle (especially Swedish Red, Simmental, and indigenous breeds) causes 5–10% embryonic mortality and reduced fertility in heterozygous carriers due to unbalanced gametes formed during meiotic segregation.",
      "keyPoints": [
        "Centric fusion of two acrocentric chromosomes into a single metacentric chromosome.",
        "Reduces diploid chromosome number (2n) while arm number (NF) remains unchanged.",
        "Example: rob(1;29) in cattle leading to repeat breeding and embryonic death."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2019",
        "IVRI 2021",
        "KVASU 2023"
      ]
    },
    {
      "id": "u2-q07",
      "type": "define",
      "marks": 2,
      "question": "State the Hardy-Weinberg Law and write its mathematical equation for a two-allele locus.",
      "topicId": "u2-t19",
      "answer": "<b>Hardy-Weinberg Law (G.H. Hardy & W. Weinberg, 1908):</b><br>In a large, randomly mating (panmictic) diploid population, both gene (allele) frequencies and genotypic frequencies remain constant from generation to generation, in the absence of disturbing evolutionary forces namely mutation, migration, selection, and random genetic drift.<br><br><b>Mathematical Equation:</b><br>If allele frequencies are <code>p</code> (for allele <i>A</i>) and <code>q</code> (for allele <i>a</i>), where <code>p + q = 1</code>:<br><code>p&sup2; (AA) + 2pq (Aa) + q&sup2; (aa) = 1.0</code>",
      "keyPoints": [
        "Gene and genotypic frequencies remain constant generation after generation.",
        "Assumptions: Large population, panmixia, no mutation, migration, drift, or selection.",
        "Binomial expansion: p² + 2pq + q² = 1 where p + q = 1."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2018",
        "RAJUVAS 2021",
        "LUVAS 2023"
      ]
    },
    {
      "id": "u2-q08",
      "type": "define",
      "marks": 2,
      "question": "Define Genetic Drift (Sewall Wright Effect) and explain its biological consequences.",
      "topicId": "u2-t21",
      "answer": "<b>Genetic Drift (Sewall Wright Effect):</b><br>The random fluctuation in allele frequencies from one generation to the next occurring purely by chance (sampling errors in gamete sampling) in small, finite populations.<br><br><b>Biological Consequences:</b><ul><li>Leads to random fixation (frequency = 1.0) or loss (frequency = 0.0) of alleles independent of their selective advantage.</li><li>Reduces genetic variation (heterozygosity) within small isolated herds.</li><li>Leads to genetic divergence among isolated sub-populations.</li></ul>",
      "keyPoints": [
        "Random changes in allele frequency due to sampling errors in small populations.",
        "Independent of natural or artificial selection.",
        "Results in fixation/loss of alleles and progressive loss of heterozygosity."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "MAFSU 2020",
        "IVRI 2022",
        "GADVASU 2023"
      ]
    },
    {
      "id": "u2-q09",
      "type": "define",
      "marks": 2,
      "question": "Define Breeding Value (Additive Genetic Value) and state its relationship to Progeny Difference.",
      "topicId": "u2-t24",
      "answer": "<b>Breeding Value (BV or A):</b><br>The value of an individual as a genetic parent. Mathematically, it is defined as twice the expected deviation of an individual's progeny mean from the population mean when mated at random to a representative sample of the population:<br><code>BV = 2 &times; (Progeny Mean - Population Mean)</code><br><br><b>Relationship to Progeny Difference (Transmitting Ability):</b><br>A parent transmits only a sample half of its genes (and breeding value) to each offspring through gametes. Hence:<br><code>Progeny Difference (PD) = Predicted Transmitting Ability (PTA) = &frac12; BV</code>",
      "keyPoints": [
        "Value of an individual as a genetic parent judged by progeny performance.",
        "Formula: BV = 2 * (Progeny Mean - Population Mean).",
        "Transmitting Ability (PTA) = 1/2 of Breeding Value."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2021",
        "KVASU 2022",
        "GADVASU 2023"
      ]
    },
    {
      "id": "u2-q10",
      "type": "define",
      "marks": 2,
      "question": "Define Heritability in Narrow Sense (h²) and Broad Sense (H²).",
      "topicId": "u2-t25",
      "answer": "<ul><li><b>Narrow-Sense Heritability (<code>h&sup2;</code>):</b> The proportion of total phenotypic variance (<code>V<sub>P</sub></code>) that is attributable to <i>additive genetic variance</i> (<code>V<sub>A</sub></code>):<br><code>h&sup2; = V<sub>A</sub> / V<sub>P</sub> = V<sub>A</sub> / (V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub> + V<sub>E</sub>)</code><br><i>Significance:</i> Determines the degree of resemblance between relatives and governs response to mass selection.</li><li><b>Broad-Sense Heritability (<code>H&sup2;</code>):</b> The proportion of total phenotypic variance attributable to total genetic variance (<code>V<sub>G</sub></code>):<br><code>H&sup2; = V<sub>G</sub> / V<sub>P</sub> = (V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub>) / V<sub>P</sub></code></li></ul>",
      "keyPoints": [
        "Narrow sense: h² = V_A / V_P (ratio of additive genetic variance to phenotypic variance).",
        "Broad sense: H² = V_G / V_P (ratio of total genetic variance to phenotypic variance).",
        "Narrow sense determines response to selection (R = h² * S)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2019",
        "IVRI 2021",
        "LUVAS 2022"
      ]
    },
    {
      "id": "u2-q11",
      "type": "define",
      "marks": 2,
      "question": "Define Repeatability (r) and state its mathematical relationship with Heritability.",
      "topicId": "u2-t26",
      "answer": "<b>Repeatability (r):</b><br>The intraclass correlation coefficient between repeated phenotypic records (e.g., successive lactations, fleece weights, litter sizes) of the same individual over time or environmental conditions:<br><code>r = (V<sub>G</sub> + V<sub>Eg</sub>) / V<sub>P</sub> = (V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub> + V<sub>Eg</sub>) / V<sub>P</sub></code><br>where <code>V<sub>Eg</sub></code> is permanent environmental variance.<br><br><b>Relationship with Heritability:</b><br>Repeatability includes both total genetic variance and permanent environmental variance. Therefore, repeatability sets the <b>upper mathematical limit of heritability</b>:<br><code>r &ge; h&sup2;</code>",
      "keyPoints": [
        "Correlation between repeated records of the same animal over time/space.",
        "Formula: r = (V_G + V_Eg) / V_P.",
        "Always equal to or greater than heritability (r >= h²)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2020",
        "RAJUVAS 2022",
        "KVAFSU 2023"
      ]
    },
    {
      "id": "u2-q12",
      "type": "define",
      "marks": 2,
      "question": "Define Genetic Correlation (rG) and state its physiological causes.",
      "topicId": "u2-t27",
      "answer": "<b>Genetic Correlation (<code>r<sub>G</sub></code>):</b><br>The measure of linear association between the additive breeding values of two different traits in the same individual:<br><code>r<sub>G</sub> = Cov<sub>A(XY)</sub> / &radic;(V<sub>A(X)</sub> &times; V<sub>A(Y)</sub>)</code><br>Its value ranges from <code>-1.0</code> to <code>+1.0</code>.<br><br><b>Physiological Causes:</b><ul><li><b>Pleiotropy (Primary cause):</b> A single gene simultaneously influencing both traits (e.g., milk yield and butterfat percentage, <code>r<sub>G</sub> &approx; -0.30</code>).</li><li><b>Linkage disequilibrium (Transient cause):</b> Genes influencing both traits located closely on the same chromosome; can be broken by crossing over.</li></ul>",
      "keyPoints": [
        "Correlation between additive breeding values of two traits.",
        "Formula: r_G = Cov_A(XY) / sqrt(V_A(X) * V_A(Y)).",
        "Primary cause is pleiotropy; secondary transient cause is genetic linkage."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2020",
        "GADVASU 2022",
        "WBUAFS 2023"
      ]
    },
    {
      "id": "u2-q13",
      "type": "diff",
      "marks": 5,
      "question": "Differentiate between Mitosis and Meiosis in farm animals. Discuss the genetic significance of meiosis.",
      "topicId": "u2-t06",
      "answer": "<b>Comparison between Mitosis and Meiosis:</b><br>Both are fundamental nuclear division processes in domestic animals, but they serve distinct biological purposes.<br><br><b>Genetic Significance of Meiosis:</b><ul><li><b>Conservation of Species Chromosome Number:</b> Halves chromosome number from diploid (<code>2n</code>) to haploid (<code>n</code>), preventing doubling in each generation upon fertilization.</li><li><b>Generation of Genetic Variation:</b> Produces novel recombinant gametes through crossing over (chiasma formation in Pachytene) and random independent assortment of maternal and paternal chromosomes in Anaphase I.</li><li><b>Physical Basis of Mendelian Genetics:</b> Segregation of alleles corresponds precisely to Anaphase I homologous disjunction.</li></ul>",
      "keyPoints": [
        "Site of occurrence: Somatic cells (mitosis) vs germ cells (meiosis).",
        "Divisions & daughter cells: One division / 2 identical diploid cells vs two divisions / 4 diverse haploid cells.",
        "Synapsis & Crossing over: Absent in mitosis; occurs in Pachytene of Meiosis I.",
        "Genetic significance: Maintains constant 2n number across generations and generates new genetic combinations via recombination."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Differences Between Mitosis and Meiosis",
        "headers": [
          "Feature",
          "Mitosis (Equational Division)",
          "Meiosis (Reductional Division)"
        ],
        "rows": [
          [
            "Site of Occurrence",
            "Somatic tissues throughout body for growth & repair",
            "Gonadal germ cells (testes/ovaries) during gametogenesis"
          ],
          [
            "Number of Nuclear Divisions",
            "Single equational division",
            "Two successive divisions (Meiosis I reductional, Meiosis II equational)"
          ],
          [
            "Daughter Cells Produced",
            "2 genetically identical diploid (2n) daughter cells",
            "4 genetically unique haploid (n) gametes"
          ],
          [
            "Synapsis & Chiasmata",
            "Completely absent; no pairing of homologues",
            "Present during Zygotene/Pachytene; crossing over occurs"
          ],
          [
            "Centromere Division",
            "Centromeres divide synchronously at Anaphase",
            "Centromeres do NOT divide at Anaphase I; divide at Anaphase II"
          ],
          [
            "Biological Role",
            "Tissue regeneration, asexual cell renewal, growth",
            "Production of haploid spermatozoa/ova, genetic recombination"
          ]
        ]
      },
      "pyq": [
        "TANUVAS 2019",
        "IVRI 2021",
        "KVASU 2023"
      ]
    },
    {
      "id": "u2-q14",
      "type": "diff",
      "marks": 5,
      "question": "Differentiate between Incomplete Dominance and Codominance with authentic farm animal examples.",
      "topicId": "u2-t02",
      "answer": "<b>Incomplete Dominance vs Codominance:</b><br>Both represent non-Mendelian allelic interactions where the classic 3:1 phenotypic ratio in F2 is modified into a <b>1:2:1</b> ratio coinciding directly with the genotypic ratio. However, their molecular mechanisms differ fundamentally.<br><br><b>Classic Animal Examples:</b><ul><li><b>Incomplete Dominance (Andalusian Fowl):</b> Cross between pure Black (<code>BB</code>) and Splash White (<code>bb</code>) produces an intermediate Blue phenotype (<code>Bb</code>) due to partial dosage of eumelanin. Selfing <code>Bb &times; Bb</code> yields 1 Black : 2 Blue : 1 Splash White.</li><li><b>Codominance (Shorthorn Cattle):</b> Cross between homozygous Red (<code>C<sup>R</sup>C<sup>R</sup></code>) and White (<code>C<sup>W</sup>C<sup>W</sup></code>) produces <b>Roan</b> coat (<code>C<sup>R</sup>C<sup>W</sup></code>). Individual hairs are completely red or completely white intermixed, as both alleles are fully expressed without blending. F2 yields 1 Red : 2 Roan : 1 White.</li><li><b>Codominance (Blood Groups):</b> Bovine blood group systems (e.g., A, B, C systems) and human ABO system (<code>I<sup>A</sup>I<sup>B</sup></code> = AB phenotype) where both antigens are simultaneously expressed on erythrocyte membranes.</li></ul>",
      "keyPoints": [
        "Incomplete dominance produces an intermediate phenotype (quantitative dosage effect).",
        "Codominance produces simultaneous, distinct expression of both alleles without blending.",
        "Both exhibit 1:2:1 phenotypic and genotypic ratio in F2 generation.",
        "Authentic examples: Blue Andalusian fowl (incomplete) vs Roan Shorthorn cattle / AB blood group (codominance)."
      ],
      "diagram": "",
      "table": {
        "title": "Comparison Between Incomplete Dominance and Codominance",
        "headers": [
          "Feature",
          "Incomplete Dominance",
          "Codominance"
        ],
        "rows": [
          [
            "Phenotypic Outcome in Heterozygote",
            "Intermediate phenotype blended between both homozygous parental types",
            "Both parental phenotypes expressed simultaneously without intermediate blending"
          ],
          [
            "Gene Product Expression",
            "Quantitative dosage effect; single active allele produces inadequate enzyme level",
            "Both alleles produce distinct, fully active functional proteins/antigens"
          ],
          [
            "F2 Phenotypic Ratio",
            "1 : 2 : 1 (e.g., 1 Black : 2 Blue : 1 White)",
            "1 : 2 : 1 (e.g., 1 Red : 2 Roan : 1 White)"
          ],
          [
            "Microscopic/Cellular Basis",
            "Uniformly intermediate pigmentation across cells",
            "Mosaic of distinct red hairs and pure white hairs intermixed"
          ],
          [
            "Classic Livestock Examples",
            "Blue Andalusian fowl; sheep ear notch trait",
            "Roan coat in Shorthorn cattle; erythrocyte blood group antigens"
          ]
        ]
      },
      "pyq": [
        "GADVASU 2020",
        "IVRI 2022",
        "LUVAS 2023"
      ]
    },
    {
      "id": "u2-q15",
      "type": "diff",
      "marks": 5,
      "question": "Distinguish between Sex-Linked, Sex-Limited, and Sex-Influenced Traits with livestock examples.",
      "topicId": "u2-t04",
      "answer": "<b>Comparison of Sex-Related Patterns of Inheritance:</b><br>Genes showing non-autosomal or sex-differential expression are grouped into three distinct categories based on their chromosomal location and endocrine regulation.<br><br><b>Key Examples in Farm Animals:</b><ul><li><b>Sex-Linked:</b> <i>Barred plumage (B)</i> in poultry located on Z chromosome. Mating non-barred rooster (<code>ZbZb</code>) with barred hen (<code>ZBW</code>) produces barred cockerels (<code>ZBZb</code>) and non-barred pullets (<code>ZbW</code>), allowing 100% accurate commercial day-old chick auto-sexing.</li><li><b>Sex-Limited:</b> <i>Milk production</i> in dairy cattle, <i>egg production</i> in layers, and <i>cryptorchidism</i> in stallions/rams. Autosomal genes carried by both sexes but expressed exclusively in one sex due to anatomical/endocrine limits.</li><li><b>Sex-Influenced:</b> <i>Horns in Dorset &times; Suffolk sheep</i>. Heterozygote (<code>Hh</code>) is horned in males (testosterone promotes expression) but polled in females (estrogen suppresses expression).</li></ul>",
      "keyPoints": [
        "Sex-Linked: Gene located on sex chromosomes (X/Z); exhibits criss-cross inheritance and sex differences in reciprocal crosses.",
        "Sex-Limited: Gene on autosomes; expressed exclusively in one sex due to anatomical/hormonal prerequisites (e.g. milk yield, egg laying).",
        "Sex-Influenced: Gene on autosomes; expressed in both sexes but dominance relationship is reversed by sex hormones (e.g. sheep horns)."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Comparison of Sex-Related Traits",
        "headers": [
          "Characteristic",
          "Sex-Linked Traits",
          "Sex-Limited Traits",
          "Sex-Influenced Traits"
        ],
        "rows": [
          [
            "Chromosomal Location",
            "Located on Sex Chromosomes (X/Z, Y/W)",
            "Located on Autosomes",
            "Located on Autosomes"
          ],
          [
            "Reciprocal Cross Results",
            "Yield completely different phenotypic distributions in progeny",
            "Yield identical genotypic distributions in both sexes",
            "Yield identical genotypic distributions in both sexes"
          ],
          [
            "Expression in Sexes",
            "Expressed in both sexes (dosage/criss-cross differences)",
            "Expressed in ONE sex only (penetrance zero in opposite sex)",
            "Expressed in BOTH sexes, but with different frequencies/dominance"
          ],
          [
            "Role of Sex Hormones",
            "No direct endocrine modulation of allelic dominance",
            "Hormones provide anatomical/physiological prerequisite for expression",
            "Testosterone/estrogen alters dominance of heterozygote"
          ],
          [
            "Livestock Examples",
            "Barred plumage in fowl (Z-linked); Haemophilia A in dogs",
            "Milk yield in cattle; egg production in poultry; cryptorchidism",
            "Horns in sheep (dominant in rams, recessive in ewes); pattern baldness"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2019",
        "TANUVAS 2021",
        "KVASU 2022"
      ]
    },
    {
      "id": "u2-q16",
      "type": "short",
      "marks": 5,
      "question": "Describe the types of Structural Chromosomal Aberrations and their reproductive consequences in livestock.",
      "topicId": "u2-t10",
      "answer": "<b>Structural Chromosomal Aberrations:</b><br>Alterations in the physical architecture and linear gene sequence of chromosomes arising from chromosomal breakage followed by abnormal reunion or loss.<br><br><b>Four Major Categories:</b><ul><li><b>1. Deletion (Deficiency):</b> Loss of a chromosomal segment. Can be terminal or interstitial. Leads to loss of vital genes; homozygous deletions are usually lethal, while heterozygous deletions cause phenotypic anomalies and pseudodominance (e.g., Cri-du-chat syndrome).</li><li><b>2. Duplication:</b> Presence of an extra chromosomal segment, creating redundant gene copies (e.g., tandem or reverse duplication). Generally less harmful than deletions, but alters gene dosage and can cause embryonic mortality or phenotypic malformations.</li><li><b>3. Inversion:</b> A 180&deg; rotation of an internal chromosomal segment following two breaks. Categorized into <b>Paracentric</b> (excluding centromere) and <b>Pericentric</b> (including centromere). Inversion heterozygotes form an <i>inversion loop</i> at pachytene; crossing over within the loop yields dicentric/acentric fragments (paracentric) or duplications/deletions (pericentric), causing gametic sterility (50% reduction in fertility).</li><li><b>4. Translocation:</b> Transfer of a chromosomal segment to a non-homologous chromosome. Includes <b>Reciprocal translocation</b> (mutual exchange) and <b>Robertsonian translocation</b> (centric fusion of two acrocentrics). Forms cross-shaped tetravalent figures at meiotic metaphase I, causing unbalanced gametes, repeat breeding, and early embryonic death in dairy cattle (e.g., 1/29 translocation).</li></ul>",
      "keyPoints": [
        "Deletion: Loss of chromosome segment; causes pseudodominance and lethality.",
        "Duplication: Extra chromosomal material; disrupts gene dosage.",
        "Inversion: 180° rotation; paracentric (no centromere) vs pericentric (includes centromere); forms inversion loops and subfertility.",
        "Translocation: Exchange between non-homologous chromosomes; forms tetravalents and unbalanced gametes."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2020",
        "GADVASU 2022",
        "MAFSU 2023"
      ]
    },
    {
      "id": "u2-q17",
      "type": "short",
      "marks": 5,
      "question": "Explain the Gene Counting Method and Square Root Method for estimating allele frequencies in animal populations with numerical illustrations.",
      "topicId": "u2-t18",
      "answer": "<b>Methods of Estimating Allele Frequencies:</b><br><br><b>1. Gene Counting Method (Direct Counting):</b><br>Applicable when all genotypes can be phenotypically identified (e.g., codominance or incomplete dominance).<br>For a population of size <code>N</code> with numbers <code>D</code> (AA), <code>H</code> (Aa), and <code>R</code> (aa):<br>Total alleles = <code>2N = 2(D + H + R)</code>.<br><code>p (freq of A) = (2D + H) / (2N) = P + &frac12; H</code><br><code>q (freq of a) = (2R + H) / (2N) = Q + &frac12; H</code><br><i>Illustration:</i> In 100 Shorthorn cattle: 49 Red (CRCR), 42 Roan (CRCW), 9 White (CWCW).<br><code>p (C<sup>R</sup>) = (2 &times; 49 + 42) / 200 = 140 / 200 = 0.70</code><br><code>q (C<sup>W</sup>) = (2 &times; 9 + 42) / 200 = 60 / 200 = 0.30</code> (Check: 0.70 + 0.30 = 1.0).<br><br><b>2. Square Root Method:</b><br>Applicable when one allele shows complete dominance over another (heterozygotes Aa indistinguishable from homozygotes AA). Assumes population is in Hardy-Weinberg equilibrium.<br>Recessive homozygotes (aa) represent <code>q&sup2;</code>.<br><code>q = &radic;(Number of recessive individuals / Total population N)</code><br><code>p = 1 - q</code><br><i>Illustration:</i> In 200 Black Angus cattle, 18 red calves (recessive bb) are born.<br><code>q&sup2; = 18 / 200 = 0.09 &rArr; q (freq of b) = &radic;0.09 = 0.30</code><br><code>p (freq of B) = 1 - 0.30 = 0.70</code><br>Carrier frequency (Bb) = <code>2pq = 2 &times; 0.70 &times; 0.30 = 0.42 (42%)</code>.",
      "keyPoints": [
        "Gene Counting: For codominant loci where all genotypes are distinct; p = (2D + H) / 2N.",
        "Square Root: For complete dominance assuming HWE; q = sqrt(R / N), p = 1 - q.",
        "Carrier frequency estimation: 2pq = 2 * p * q.",
        "Formulas and step-by-step numerical examples included."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2021",
        "KVASU 2022",
        "LUVAS 2023"
      ]
    },
    {
      "id": "u2-q18",
      "type": "short",
      "marks": 5,
      "question": "Explain the principle and steps of Polymerase Chain Reaction (PCR). Describe its application in screening breeding bulls for BLAD and CVM.",
      "topicId": "u2-t15",
      "answer": "<b>Polymerase Chain Reaction (PCR - Kary Mullis, 1983):</b><br>An in vitro molecular technique for the enzymatic amplification of a specific target DNA sequence by several million-fold through repeated thermal cycles.<br><br><b>Three Fundamental Thermal Steps in Each Cycle:</b><ul><li><b>1. Denaturation (94&ndash;95&deg;C, 30&ndash;60s):</b> High temperature disrupts hydrogen bonds between complementary bases, separating double-stranded DNA into single template strands.</li><li><b>2. Primer Annealing (50&ndash;65&deg;C, 30&ndash;60s):</b> Sequence-specific forward and reverse oligonucleotide primers bind to complementary regions flanking the target sequence.</li><li><b>3. Primer Extension (72&deg;C, 1 min/kb):</b> Thermostable <i>Taq</i> DNA polymerase synthesizes nascent complementary DNA strands using dNTPs in the 5'&rarr;3' direction.</li></ul><b>Application in Sire Screening for Lethal Recessive Genetic Defects:</b><ul><li><b>Bovine Leukocyte Adhesion Deficiency (BLAD):</b> A fatal autosomal recessive disease in Holstein cattle caused by an A&rarr;G point mutation at position 383 of the CD18 gene (aspartic acid &rarr; glycine substitution), abolishing a <i>TaqI</i> restriction site. PCR-RFLP accurately detects heterozygous carrier sires (normal <code>TL</code> vs carrier <code>BL</code>), preventing the spread of lethal alleles via semen distribution.</li><li><b>Complex Vertebral Malformation (CVM):</b> Lethal defect caused by a G&rarr;T mutation in the SLC35A3 gene in Holsteins; diagnosed via PCR-RFLP or allele-specific PCR to certify artificial insemination (AI) sires as disease-free (<code>TV</code>).</li></ul>",
      "keyPoints": [
        "PCR principle: In vitro exponential DNA amplification using Taq polymerase and thermal cycling.",
        "3 steps: Denaturation (94-95°C), Annealing (50-65°C), Extension (72°C).",
        "Screening of breeding bulls: BLAD (CD18 point mutation) and CVM (SLC35A3 mutation) via PCR-RFLP.",
        "Prevents dissemination of lethal alleles across thousands of daughters via AI."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2021",
        "GADVASU 2022",
        "KVAFSU 2023"
      ]
    },
    {
      "id": "u2-q19",
      "type": "short",
      "marks": 5,
      "question": "Explain the partitioning of Phenotypic Variance into its genetic and environmental components. What is the significance of Additive Genetic Variance?",
      "topicId": "u2-t24",
      "answer": "<b>Partitioning of Phenotypic Variance (V<sub>P</sub>):</b><br>In quantitative genetics, the observed total variance in a polygenic metric trait (<code>V<sub>P</sub></code>) is partitioned into underlying causal components according to Falconer's model:<br><code>V<sub>P</sub> = V<sub>G</sub> + V<sub>E</sub> + V<sub>GE</sub> + 2 Cov<sub>GE</sub></code><br>Assuming random distribution of genotypes across environments (<code>Cov<sub>GE</sub> = 0</code> and negligible <code>V<sub>GE</sub></code>):<br><code>V<sub>P</sub> = V<sub>G</sub> + V<sub>E</sub></code><br><br><b>Sub-partitioning of Genetic Variance (V<sub>G</sub>):</b><ul><li><b>Additive Genetic Variance (<code>V<sub>A</sub></code>):</b> Variance due to average additive effects of individual genes across loci. Transmissible directly from parents to offspring.</li><li><b>Dominance Variance (<code>V<sub>D</sub></code>):</b> Variance due to non-additive intra-locus allelic interactions (masking/dominance). Broken up during meiosis; cannot be fixed by pure breeding.</li><li><b>Epistatic / Interaction Variance (<code>V<sub>I</sub></code>):</b> Variance due to non-additive inter-locus gene interactions (<code>V<sub>AA</sub> + V<sub>AD</sub> + V<sub>DD</sub></code>).</li></ul><b>Sub-partitioning of Environmental Variance (V<sub>E</sub>):</b><ul><li><b>Permanent Environmental Variance (<code>V<sub>Eg</sub></code>):</b> Non-genetic factors affecting all records of an animal (e.g., calfhood mastitis permanently damaging an udder quarter).</li><li><b>Temporary Environmental Variance (<code>V<sub>Es</sub></code>):</b> Transient factors affecting only a single measurement (e.g., daily feeding, ambient temperature).</li></ul><code>V<sub>P</sub> = V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub> + V<sub>Eg</sub> + V<sub>Es</sub></code><br><br><b>Crucial Significance of Additive Genetic Variance (V<sub>A</sub>):</b><br><code>V<sub>A</sub></code> is the chief genetic determinant of narrow-sense heritability (<code>h&sup2; = V<sub>A</sub>/V<sub>P</sub></code>) and governs the response to mass selection (<code>R = h&sup2;S</code>). It represents permanent, cumulative genetic progress.",
      "keyPoints": [
        "Full equation: V_P = V_A + V_D + V_I + V_Eg + V_Es.",
        "Genetic components: Additive (V_A), Dominance (V_D), Epistatic (V_I).",
        "Environmental components: Permanent (V_Eg) and Temporary (V_Es).",
        "Significance of V_A: Chief transmissible component from parents to progeny; governs selection response (R = h² * S)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2020",
        "TANUVAS 2022",
        "DUVASU 2023"
      ]
    },
    {
      "id": "u2-q20",
      "type": "short",
      "marks": 5,
      "question": "Compare Paternal Half-Sib Correlation and Parent-Offspring Regression methods for estimating Heritability.",
      "topicId": "u2-t25",
      "answer": "<b>Comparison of Heritability Estimation Methods:</b><br>Heritability is estimated from the degree of phenotypic resemblance between related individuals. The two most common biometrical methods used in livestock populations are Parent-Offspring Regression and Paternal Half-Sib Analysis of Variance (ANOVA).<br><br><b>Mathematical Bases:</b><ul><li><b>Offspring-Parent Regression (<code>b<sub>OP</sub></code>):</b> Covariance between one parent and offspring equals <code>&frac12; V<sub>A</sub></code>. Hence:<br><code>h&sup2; = 2 &times; b<sub>OP</sub></code> (single parent), or <code>h&sup2; = b<sub>O(MP)</sub></code> (mid-parent regression). Free from dominance variance.</li><li><b>Paternal Half-Sib Correlation (<code>t</code>):</b> Sires are mated randomly to different dams, producing paternal half-sibs. Covariance between half-sibs equals <code>&frac14; V<sub>A</sub> + 1/16 V<sub>AA</sub></code>. Hence:<br><code>h&sup2; = 4 &times; t = 4 &times; [&sigma;<sub>s</sub>&sup2; / (&sigma;<sub>s</sub>&sup2; + &sigma;<sub>e</sub>&sup2;)]</code>. Best suited for dairy cattle where bulls have hundreds of daughters across different herds.</li></ul>",
      "keyPoints": [
        "Paternal Half-Sib: h² = 4 * t; based on sire variance component in one-way ANOVA.",
        "Offspring-Parent: h² = 2 * b_OP (single parent) or h² = b_O(MP) (mid-parent).",
        "Suitability: Half-sib is ideal for sex-limited traits (milk yield) with AI sires; Parent-offspring requires records on both generations.",
        "Half-sib is free from maternal environmental effects when dams are randomly assigned."
      ],
      "diagram": "",
      "table": {
        "title": "Comparison Between Paternal Half-Sib ANOVA and Parent-Offspring Regression",
        "headers": [
          "Feature",
          "Paternal Half-Sib Correlation",
          "Parent-Offspring Regression"
        ],
        "rows": [
          [
            "Statistical Model",
            "One-way ANOVA (Between Sires and Within Sires / Between Progeny)",
            "Linear Regression (Offspring on Single Parent or Mid-Parent)"
          ],
          [
            "Heritability Formula",
            "h² = 4 * t = 4 * [σ_s² / (σ_s² + σ_e²)]",
            "h² = 2 * b_OP (Single Parent) OR h² = b_O(MP) (Mid-Parent)"
          ],
          [
            "Genetic Covariance Utilized",
            "Cov(HS) = 1/4 V_A + 1/16 V_AA",
            "Cov(OP) = 1/2 V_A + 1/4 V_AA"
          ],
          [
            "Environmental Bias Risk",
            "Minimised if dams and herds are randomly assigned to sires",
            "Risk of maternal environmental correlation if dam-offspring used"
          ],
          [
            "Application in Livestock",
            "Standard method for dairy cattle & poultry with large AI sire families",
            "Applicable for growth traits in sheep/swine/beef cattle where both sexes express trait"
          ],
          [
            "Sex-Limited Traits",
            "Highly efficient (evaluates bulls using daughter records)",
            "Cannot use sire-daughter regression directly for sex-limited traits like milk yield"
          ]
        ]
      },
      "pyq": [
        "IVRI 2019",
        "RAJUVAS 2021",
        "KVASU 2023"
      ]
    },
    {
      "id": "u2-q21",
      "type": "long",
      "marks": 12,
      "question": "Define Epistasis. Describe the various types of non-allelic gene interactions that modify the classical Mendelian dihybrid ratio (9:3:3:1) into modified ratios (9:3:4, 12:3:1, 13:3, 9:7, 15:1, 9:6:1). Illustrate each with its underlying biochemical or genetic mechanism and animal examples.",
      "topicId": "u2-t03",
      "answer": "<b>1. Introduction and Definition of Epistasis:</b><br><b>Epistasis</b> (William Bateson, 1909) is a form of non-allelic gene interaction wherein an allele at one gene locus masks, alters, or suppresses the phenotypic expression of alleles at another, distinct gene locus. The gene that exerts the masking effect is termed <b>epistatic</b>, while the gene whose phenotypic expression is concealed is termed <b>hypostatic</b>.<br>In classical Mendelian dihybrid inheritance, independent assortment of two heterozygous loci (<code>AaBb &times; AaBb</code>) produces four distinct phenotypic classes in a <b>9:3:3:1</b> ratio [<code>9 A_B_ : 3 A_bb : 3 aaB_ : 1 aabb</code>]. Epistatic interactions modify this ratio into various combinations depending on the biochemical pathway involved.<br><br><b>2. Detailed Classification of Epistatic Interactions:</b><br><br><b>A. Supplementary Epistasis / Recessive Epistasis (9 : 3 : 4):</b><br><ul><li><b>Mechanism:</b> The homozygous recessive genotype at the epistatic locus (<code>aa</code>) completely suppresses the expression of the second locus (<code>B_</code> or <code>bb</code>). When dominant allele <code>A</code> is present, <code>B</code> supplements it to produce a third phenotype.</li><li><b>Biochemical Model:</b> Precursor (Colorless) &mdash;[Enzyme A]&rarr; Intermediate Pigment &mdash;[Enzyme B]&rarr; Final Pigment.</li><li><b>Animal Example:</b> Coat color in Labrador Retrievers. Locus <i>B</i> determines pigment color (<code>B_</code> black, <code>bb</code> chocolate brown). Locus <i>E</i> controls pigment deposition in hair shafts. Homozygous recessive <code>ee</code> prevents any eumelanin deposition regardless of B locus, producing <b>Yellow Labrador</b>. Cross of dihybrid blacks (<code>BbEe &times; BbEe</code>) yields: <b>9 Black (B_E_) : 3 Chocolate (bbE_) : 4 Yellow (_ _ee)</b>.</li></ul><br><b>B. Dominant Epistasis / Masking Epistasis (12 : 3 : 1):</b><br><ul><li><b>Mechanism:</b> A single dominant allele at the epistatic locus (<code>A_</code>) completely masks the phenotypic expression of the hypostatic locus (<code>B_</code> or <code>bb</code>). The hypostatic alleles are expressed only when the epistatic locus is homozygous recessive (<code>aa</code>).</li><li><b>Animal Example:</b> Dominant White plumage in White Leghorn poultry. Locus <i>C</i> produces colored plumage (<code>C_</code> pigmented, <code>cc</code> white). Locus <i>I</i> is a dominant inhibitor of melanin synthesis. Whenever dominant <code>I_</code> is present, plumage is pure white regardless of C genotype. Only <code>iiC_</code> chickens develop colored plumage, while <code>iicc</code> is white. Cross <code>IiCc &times; IiCc</code> yields: <b>12 White (9 I_C_ + 3 I_cc) : 3 Colored (iiC_) : 1 White (iicc)</b> = <b>12 White : 3 Colored : 1 White</b> (net 12 White : 3 Colored : 1 White).</li></ul><br><b>C. Inhibitory Gene Interaction / Dominant & Recessive Epistasis (13 : 3):</b><br><ul><li><b>Mechanism:</b> A dominant allele at one locus (<code>A_</code>) inhibits the expression of a dominant allele at another locus (<code>B_</code>), while the homozygous recessive of the second locus (<code>bb</code>) independently produces the same blank phenotype.</li><li><b>Outcome:</b> Classes <code>9 A_B_ + 3 A_bb + 1 aabb = 13</code> show the inhibitory/white phenotype, while only <code>3 aaB_</code> show the colored phenotype, generating a <b>13 : 3</b> ratio.</li></ul><br><b>D. Complementary Epistasis / Duplicate Recessive Epistasis (9 : 7):</b><br><ul><li><b>Mechanism:</b> Dominant alleles at both loci (<code>A_B_</code>) are mutually required to complete a multi-step biochemical pathway and produce the functional phenotype. Homozygosity for recessive alleles at either locus (<code>A_bb</code>, <code>aaB_</code>, or <code>aabb</code>) halts the pathway, giving identical null phenotypes.</li><li><b>Biochemical Basis:</b> Substrate &mdash;[Enzyme A]&rarr; Intermediate &mdash;[Enzyme B]&rarr; Chromophore.</li><li><b>Outcome:</b> <b>9 Expressed (A_B_) : 7 Unexpressed (3 A_bb + 3 aaB_ + 1 aabb)</b>. Example: Deaf-mutism in animals/humans; anthocyanin synthesis.</li></ul><br><b>E. Duplicate Dominant Epistasis / Duplicate Genes (15 : 1):</b><br><ul><li><b>Mechanism:</b> Either dominant allele (<code>A_</code> or <code>B_</code>) is fully sufficient on its own to produce the complete trait phenotype. Only the double homozygous recessive (<code>aabb</code>) exhibits the mutant/alternative phenotype.</li><li><b>Animal Example:</b> Feathered shanks in chickens. Presence of either dominant allele <code>F1</code> or <code>F2</code> produces feathered legs. Shank feathers absent only in double recessive <code>f1f1 f2f2</code>. F2 cross yields <b>15 Feathered : 1 Clean shank</b>.</li></ul><br><b>F. Duplicate Genes with Cumulative Effect (9 : 6 : 1):</b><br><ul><li><b>Mechanism:</b> Dominant alleles at both loci individually produce identical intermediate phenotypes, but when present together (<code>A_B_</code>), they act cumulatively to produce an enhanced phenotype. The double recessive (<code>aabb</code>) produces a third distinct phenotype.</li><li><b>Outcome:</b> <b>9 Enhanced (A_B_) : 6 Intermediate (3 A_bb + 3 aaB_) : 1 Null (aabb)</b>.</li></ul>",
      "keyPoints": [
        "Clear definition of epistasis (epistatic vs hypostatic gene loci).",
        "Biochemical pathway foundation for departure from 9:3:3:1.",
        "Recessive Epistasis (9:3:4) with Labrador retriever coat color (B and E loci).",
        "Dominant Epistasis (12:3:1) with White Leghorn poultry plumage (I and C loci).",
        "Inhibitory Epistasis (13:3) and Complementary Epistasis (9:7).",
        "Duplicate Dominant Epistasis (15:1) with feathered shanks in fowl.",
        "Comprehensive comparative summary table of all epistatic ratios."
      ],
      "diagram": "",
      "table": {
        "title": "Master Summary of Modified Mendelian Dihybrid Epistatic Ratios",
        "headers": [
          "Type of Interaction",
          "Modified F2 Ratio",
          "A_B_ (9)",
          "A_bb (3)",
          "aaB_ (3)",
          "aabb (1)",
          "Classic Animal Example"
        ],
        "rows": [
          [
            "Classical Dihybrid Cross",
            "9 : 3 : 3 : 1",
            "Phenotype 1",
            "Phenotype 2",
            "Phenotype 3",
            "Phenotype 4",
            "Mendelian independent assortment"
          ],
          [
            "Recessive Epistasis",
            "9 : 3 : 4",
            "Black (9)",
            "Chocolate (3)",
            "Yellow (3)",
            "Yellow (1)",
            "Coat color in Labrador Retrievers (B/E loci)"
          ],
          [
            "Dominant Epistasis",
            "12 : 3 : 1",
            "White (9)",
            "White (3)",
            "Colored (3)",
            "White (1)",
            "Plumage color in White Leghorn fowl (I/C loci)"
          ],
          [
            "Inhibitory Epistasis",
            "13 : 3",
            "Inhibited (9)",
            "Inhibited (3)",
            "Expressed (3)",
            "Inhibited (1)",
            "Feather color inhibition in poultry"
          ],
          [
            "Complementary Epistasis",
            "9 : 7",
            "Colored (9)",
            "White (3)",
            "White (3)",
            "White (1)",
            "Purple/White flower color; congenital deafness"
          ],
          [
            "Duplicate Dominant Epistasis",
            "15 : 1",
            "Feathered (9)",
            "Feathered (3)",
            "Feathered (3)",
            "Clean (1)",
            "Feathered vs Clean shanks in domestic fowl"
          ],
          [
            "Cumulative Duplicate Genes",
            "9 : 6 : 1",
            "Disc/Deep (9)",
            "Spherical (3)",
            "Spherical (3)",
            "Long/Elongate (1)",
            "Fruit shape in summer squash / metric traits"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2018",
        "TANUVAS 2020",
        "IVRI 2021",
        "KVASU 2023"
      ]
    },
    {
      "id": "u2-q22",
      "type": "long",
      "marks": 12,
      "question": "Define Cytogenetics and Karyotyping. Describe in detail the standard protocol for peripheral blood lymphocyte karyotyping in cattle. Provide a comprehensive comparative table of diploid chromosome numbers, morphological types, and sex chromosomes in domestic animals. Discuss the economic significance of chromosomal abnormalities in livestock breeding.",
      "topicId": "u2-t07",
      "answer": "<b>1. Definitions:</b><br><ul><li><b>Cytogenetics:</b> The branch of genetics that correlates cellular structure and behavior, particularly the morphology, structural organization, number, and meiotic/mitotic dynamics of <b>chromosomes</b>, with the principles of heredity and phenotypic expression.</li><li><b>Karyotype & Idiogram:</b> A <i>karyotype</i> is the systematic photographic or diagrammatic representation of the complete chromosomal complement of an individual somatic cell, arranged in descending order of size and grouped by centromeric position. An <i>idiogram</i> is a formalized, standardized diagrammatic mapping of the karyotype showing diagnostic G-banding patterns.</li></ul><br><b>2. Standard Protocol for Peripheral Blood Lymphocyte Culture (Moorhead et al., modified):</b><ol><li><b>Aseptic Blood Collection:</b> Collect 5&ndash;10 mL of venous blood from the jugular vein into a sterile vacutainer containing preservative-free sodium heparin (20 IU/mL). Invert gently to prevent clotting.</li><li><b>Culture Inoculation:</b> In a laminar airflow cabinet, add 0.5&ndash;1.0 mL of whole heparinized blood to a sterile culture vessel containing 8&ndash;10 mL of RPMI-1640 or Ham's F-10 medium supplemented with 15&ndash;20% fetal bovine serum (FBS), antibiotics (penicillin 100 IU/mL, streptomycin 100 &mu;g/mL), and <b>Phytohaemagglutinin (PHA-M / PHA-P, 5&ndash;10 &mu;g/mL)</b>. PHA acts as a potent mitogen that stimulates resting non-dividing T-lymphocytes to dedifferentiate, enter blastogenesis, and begin mitotic division.</li><li><b>Incubation:</b> Incubate at 37.5&deg;C in a 5% CO<sub>2</sub> humidified incubator for <b>70 to 72 hours</b>.</li><li><b>Mitotic Arrest (Colchicine / Colcemid):</b> At 70 hours (2 hours prior to harvest), add <b>Colcemid (0.05&ndash;0.1 &mu;g/mL final concentration)</b>. Colcemid binds tubulin dimers, disrupting spindle microtubule assembly, thereby arresting dividing lymphocytes at <b>metaphase</b> where chromosomes are maximally condensed.</li><li><b>Hypotonic Swelling:</b> Centrifuge at 1200 rpm for 10 min. Discard supernatant. Resuspend pellet in pre-warmed (37&deg;C) <b>hypotonic solution (0.075 M KCl or 0.8% sodium citrate)</b> for 15&ndash;20 minutes. The hypotonic osmotic influx swells the cytoplasm, dispersing metaphase chromosomes widely to eliminate overlapping.</li><li><b>Fixation:</b> Add 2 mL of freshly prepared, ice-cold <b>Carnoy's fixative (3 parts absolute methanol : 1 part glacial acetic acid)</b>. Mix gently, centrifuge, discard supernatant, and repeat washing 3&ndash;4 times until the cell pellet becomes crisp, clean, and chalky white.</li><li><b>Slide Preparation & Ageing:</b> Drop the concentrated cell suspension from a height of 1&ndash;2 feet onto clean, chilled, wet glass slides. Flame-dry gently or air-dry to spread chromosomes. Bake slides at 60&deg;C for 24 hours.</li><li><b>Staining & Banding:</b> Stain with 4% Giemsa (for conventional solid karyotyping) or treat with 0.025% Trypsin followed by Giemsa for <b>GTG-banding (G-bands by Trypsin using Giemsa)</b> to produce diagnostic alternating light and dark transverse bands.</li></ol><br><b>3. Economic Significance of Chromosomal Abnormalities in Livestock Breeding:</b><ul><li><b>1/29 Robertsonian Translocation in Cattle [rob(1;29)]:</b> Centric fusion of autosomes 1 and 29. Heterozygous carrier bulls are phenotypically normal and produce normal semen volume and motility, but produce unbalanced secondary spermatocytes (nullisomic and disomic gametes). Causes <b>5&ndash;10% reduction in conception rates</b>, repeat breeding, and early embryonic death in mated cows. Mandatory karyotypic screening eliminates carriers from AI bull stations.</li><li><b>Bovine Freemartinism:</b> Vascular anastomoses between heterosexual twin bovine fetuses (male-female twins) allow exchange of anti-Müllerian hormone (AMH) and testosterone, along with fetal hematopoetic stem cells. The female co-twin becomes an infertile <b>freemartin</b> with masculinized non-functional ovaries, hypoplastic uterus, and blind vagina. Cytogenetically diagnosed via <b>XX/XY leukocyte chimerism</b> (leukocyte karyotyping shows both 60,XX and 60,XY metaphases). Early karyotypic culling saves calf rearing costs.</li><li><b>Reciprocal Translocations in Pigs:</b> Reduces litter size by 30&ndash;50% due to high peri-implantation embryonic mortality caused by unbalanced gametes.</li></ul>",
      "keyPoints": [
        "Definitions of Cytogenetics, Karyotype, and Idiogram.",
        "Complete 8-step lymphocyte culture protocol (Heparin, PHA-M mitogen, 72h incubation, Colcemid metaphase arrest, 0.075M KCl hypotonic swelling, Carnoy fixative, GTG-banding).",
        "Comprehensive table of 2n numbers, autosome morphology, and sex chromosomes across cattle, buffalo, sheep, goat, pig, horse, and chicken.",
        "Economic impacts: rob(1;29) fertility reduction in cattle, Freemartinism (XX/XY chimerism), swine translocations."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Chromosomal Profiles of Farm Animals and Poultry",
        "headers": [
          "Species",
          "2n",
          "Autosome Morphology",
          "X Chromosome",
          "Y Chromosome",
          "Fundamental Arm Number (NF)"
        ],
        "rows": [
          [
            "Cattle (Bos taurus / Bos indicus)",
            "60",
            "All 58 autosomes are Acrocentric",
            "Large Sub-metacentric",
            "Small Metacentric (B. taurus) / Acrocentric (B. indicus)",
            "60 (excluding sex chromosomes)"
          ],
          [
            "River Buffalo (Bubalus bubalis)",
            "50",
            "5 pairs Sub-metacentric / Metacentric, 19 pairs Acrocentric",
            "Largest Acrocentric",
            "Small Acrocentric",
            "60"
          ],
          [
            "Swamp Buffalo (Bubalus carabanensis)",
            "48",
            "6 pairs Bi-armed, 17 pairs Acrocentric",
            "Largest Acrocentric",
            "Small Acrocentric",
            "60"
          ],
          [
            "Goat (Capra hircus)",
            "60",
            "All 58 autosomes are Acrocentric",
            "Large Acrocentric",
            "Minute Acrocentric / Dot-like",
            "60"
          ],
          [
            "Sheep (Ovis aries)",
            "54",
            "3 pairs large Metacentric, 23 pairs Acrocentric",
            "Largest Acrocentric",
            "Small Metacentric",
            "60"
          ],
          [
            "Pig (Sus scrofa domesticus)",
            "38",
            "12 pairs Bi-armed (Meta/Submeta), 6 pairs Acrocentric",
            "Medium Metacentric",
            "Small Metacentric",
            "64"
          ],
          [
            "Horse (Equus caballus)",
            "64",
            "13 pairs Bi-armed, 18 pairs Acrocentric",
            "Large Sub-metacentric",
            "Small Acrocentric",
            "94"
          ],
          [
            "Domestic Fowl (Gallus domesticus)",
            "78",
            "10 pairs Macrochromosomes, 28 pairs Microchromosomes",
            "Z: 4th largest Metacentric",
            "W: Small Sub-metacentric (Female heterogametic ZW)",
            "~108"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2017",
        "IVRI 2020",
        "TANUVAS 2021",
        "GADVASU 2022",
        "LUVAS 2023"
      ]
    },
    {
      "id": "u2-q23",
      "type": "long",
      "marks": 12,
      "question": "Describe the molecular architecture of the DNA Double Helix according to the Watson-Crick model. Explain the Central Dogma of Molecular Genetics, detailing the stages of Transcription and Translation. Discuss the practical applications of recombinant DNA technology and Marker-Assisted Selection (MAS) in livestock improvement.",
      "topicId": "u2-t12",
      "answer": "<b>1. Molecular Architecture of DNA (Watson and Crick Model, 1953):</b><ul><li><b>Double-Helical Structure:</b> DNA consists of two right-handed antiparallel polynucleotide chains wound around a central axis (one running 5'&rarr;3', the other 3'&rarr;5').</li><li><b>Sugar-Phosphate Backbone:</b> Hydrophilic deoxyribose sugars linked by 3'&ndash;5' phosphodiester bonds form the external structural backbone, while hydrophobic purine and pyrimidine bases project perpendicularly inward into the core.</li><li><b>Complementary Base Pairing (Chargaff's Rules):</b> Adenine pairs specifically with Thymine via <b>two hydrogen bonds</b> (<code>A = T</code>), and Guanine pairs with Cytosine via <b>three hydrogen bonds</b> (<code>G &equiv; C</code>). Consequently, Purines = Pyrimidines (<code>A + G = T + C</code>), though <code>(A+T)/(G+C)</code> ratio varies across species.</li><li><b>Helical Dimensions:</b> Diameter = <b>2.0 nm (20 &Aring;)</b>; complete helical turn = <b>3.4 nm (34 &Aring;)</b> containing exactly <b>10.4 to 10.5 base pairs</b> (pitch); distance between adjacent base pairs = <b>0.34 nm (3.4 &Aring;)</b>. Forms alternating Major (2.2 nm) and Minor (1.2 nm) grooves for regulatory protein interaction.</li></ul><br><b>2. The Central Dogma of Molecular Biology (Francis Crick, 1958):</b><br>The unidirectional flow of genetic information: <b>DNA &mdash;[Replication]&rarr; DNA &mdash;[Transcription]&rarr; mRNA &mdash;[Translation]&rarr; Functional Polypeptide/Protein</b>.<br><br><b>A. Transcription (DNA to mRNA):</b><ul><li><b>Initiation:</b> RNA Polymerase II holoenzyme binds to the gene promoter region (TATA box at -25 bp, CAAT box at -75 bp) assisted by general transcription factors (TFIID, TFIIB). DNA unzips to form an open transcription bubble.</li><li><b>Elongation:</b> RNA polymerase synthesizes single-stranded mRNA in the 5'&rarr;3' direction by reading the antisense (template) DNA strand 3'&rarr;5', incorporating ribonucleotides (ATP, UTP, GTP, CTP).</li><li><b>Termination:</b> Reaches a polyadenylation signal sequence (<code>AAUAAA</code>), cleaved 10&ndash;30 nucleotides downstream.</li><li><b>Post-Transcriptional Processing in Eukaryotes:</b> (i) 5'-capping with 7-methylguanosine; (ii) 3'-polyadenylation (150&ndash;250 A-residues); (iii) Splicing by spliceosomes (removal of non-coding introns and ligation of coding exons).</li></ul><br><b>B. Translation (mRNA to Functional Protein):</b><ul><li><b>Genetic Code:</b> Triplet codons, non-overlapping, commaless, degenerate (64 codons: 61 sense codons coding 20 amino acids, 3 nonsense stop codons: <code>UAA, UAG, UGA</code>; universal start codon: <code>AUG</code> coding for Methionine).</li><li><b>Activation & Charging:</b> Amino acid is activated by aminoacyl-tRNA synthetase via ATP to form aminoacyl-AMP, then transferred to the 3'-CCA end of cognate tRNA.</li><li><b>Ribosomal Assembly:</b> Small 40S subunit binds mRNA at 5' cap and scans for AUG; initiator Met-tRNA binds at the P-site; large 60S subunit joins to form active 80S ribosome.</li><li><b>Elongation & Peptide Bond Formation:</b> Incoming aminoacyl-tRNA enters A-site (assisted by EF-1&alpha;); peptidyl transferase (28S rRNA ribozyme) catalyzes peptide bond between P-site amino acid and A-site amino acid; ribosome translocates 3 nucleotides along mRNA via EF-2.</li><li><b>Termination:</b> Stop codon enters A-site; release factors (eRF1, eRF3) trigger hydrolysis and release of the nascent polypeptide chain.</li></ul><br><b>3. Livestock Applications: Marker-Assisted Selection (MAS) & Gene Diagnostics:</b><ul><li><b>Screening for Genetic Diseases:</b> Routine diagnostic PCR-RFLP screens out fatal alleles such as BLAD, CVM, Citrullinaemia, and DUMPS in dairy sires.</li><li><b>Marker-Assisted Selection for Quantitative Traits:</b> Direct selection for desirable allelic variants: (i) <b>Kappa-casein (CSN3) B allele</b> in dairy cattle associated with superior cheese yield, firmer curd, and higher milk protein content; (ii) <b>DGAT1 K232A polymorphism</b> for elevated milk fat percentage; (iii) <b>Booroola fecundity gene (FecB)</b> in sheep, which increases ovulation rate and litter size by 1.0&ndash;1.5 lambs per ewe.</li><li><b>Genomic Selection:</b> High-density SNP genotyping arrays (e.g., Bovine 50K and 777K HD BeadChips) predict Genomic Estimated Breeding Values (GEBVs) at calfhood, shortening the generation interval from 5 years to 1.5 years.</li></ul>",
      "keyPoints": [
        "Watson-Crick DNA structure: Double helix, antiparallel, 2.0 nm diameter, 3.4 nm pitch (10.5 bp/turn), complementary hydrogen bonding (A=T 2 bonds, G≡C 3 bonds).",
        "Central Dogma flow: DNA -> RNA -> Protein.",
        "Transcription stages (Initiation, Elongation, Termination, 5' cap, poly-A tail, splicing).",
        "Translation mechanism (Genetic code properties, 80S ribosome, P and A sites, peptidyl transferase, peptide bond).",
        "Livestock applications: BLAD/CVM screening, CSN3 B allele for cheese yield, DGAT1, FecB gene in sheep, and high-density SNP genomic selection."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2018",
        "TANUVAS 2020",
        "GADVASU 2021",
        "KVASU 2022",
        "MAFSU 2023"
      ]
    },
    {
      "id": "u2-q24",
      "type": "long",
      "marks": 12,
      "question": "State the Hardy-Weinberg Law of Population Genetics. Derive the mathematical formulation of genotype frequencies for a two-allele locus. Detail the five fundamental assumptions required for the law to hold true. Explain how a population is tested for Hardy-Weinberg Equilibrium using Chi-square test (df = 1). Discuss the four evolutionary forces that disturb genetic equilibrium in domestic livestock populations.",
      "topicId": "u2-t19",
      "answer": "<b>1. Statement of the Hardy-Weinberg Law (G.H. Hardy & Wilhelm Weinberg, 1908):</b><br>In a large, randomly mating diploid population, both gene (allele) frequencies and genotypic frequencies remain constant and in stable equilibrium from generation to generation, provided there are no disturbing influences of mutation, migration, selection, and random genetic drift.<br><br><b>2. Mathematical Derivation for a Two-Allele Locus:</b><br>Consider an autosomal locus with two alleles, <i>A</i> and <i>a</i>.<br>Let frequency of allele <i>A</i> = <code>p</code>, and frequency of allele <i>a</i> = <code>q</code>, such that <code>p + q = 1.0</code>.<br>In random mating (panmixia), the probability of union between male and female gametes is the mathematical product of their independent allele frequencies:<br><ul><li>Union of sperm <i>A</i> (prob <code>p</code>) and ovum <i>A</i> (prob <code>p</code>) &rarr; Genotype <code>AA</code> = <code>p &times; p = p&sup2;</code></li><li>Union of sperm <i>A</i> (prob <code>p</code>) and ovum <i>a</i> (prob <code>q</code>) &rarr; Genotype <code>Aa</code> = <code>p &times; q = pq</code></li><li>Union of sperm <i>a</i> (prob <code>q</code>) and ovum <i>A</i> (prob <code>p</code>) &rarr; Genotype <code>aA</code> = <code>q &times; p = pq</code></li><li>Union of sperm <i>a</i> (prob <code>q</code>) and ovum <i>a</i> (prob <code>q</code>) &rarr; Genotype <code>aa</code> = <code>q &times; q = q&sup2;</code></li></ul>Combining heterozygous classes (<code>pq + pq = 2pq</code>), the expected zygotic genotypic distribution is the binomial expansion:<br><code>(p + q)&sup2; = p&sup2; (AA) + 2pq (Aa) + q&sup2; (aa) = 1.0</code><br><br><b>Proof of Stability Across Generations:</b><br>Allele frequency of <i>A</i> in the next generation:<br><code>p' = Freq(AA) + &frac12; Freq(Aa) = p&sup2; + &frac12;(2pq) = p&sup2; + pq = p(p + q) = p(1) = p</code>.<br>Thus, gene frequencies and genotypic frequencies reach permanent equilibrium after a single generation of random mating.<br><br><b>3. Fundamental Assumptions of Hardy-Weinberg Law:</b><ol><li><b>Infinitely Large Population Size:</b> Eliminates random gamete sampling errors (no genetic drift).</li><li><b>Random Mating (Panmixia):</b> Every individual has an equal probability of mating with any individual of opposite sex; no assortative mating or inbreeding.</li><li><b>No Mutation:</b> Forward and reverse mutation rates must be zero or in exact dynamic balance.</li><li><b>No Migration (Gene Flow):</b> Population is strictly closed to introduction of genes from outside or selective emigration.</li><li><b>No Selection:</b> All genotypes (AA, Aa, aa) have equal reproductive viability and fertility (fitness coefficient <code>w = 1.0</code>, selection coefficient <code>s = 0</code>).</li></ol><br><b>4. Testing for Hardy-Weinberg Equilibrium using Chi-Square (&chi;&sup2;) Test:</b><ol><li>Step 1: Calculate observed allele frequencies (<code>p</code> and <code>q</code>) from sample genotype counts (<code>N</code>) using gene counting.</li><li>Step 2: Calculate expected numbers for each genotype:<br><code>E(AA) = p&sup2; &times; N</code>, <code>E(Aa) = 2pq &times; N</code>, <code>E(aa) = q&sup2; &times; N</code>.</li><li>Step 3: Compute Chi-square statistic: <code>&chi;&sup2; = &sum; [(O - E)&sup2; / E]</code>.</li><li>Step 4: Degrees of Freedom: <code>df = k - 1 - m</code>, where <code>k</code> = number of phenotypic classes (3), and <code>m</code> = number of independent parameters estimated from data (1, since p was estimated and q=1-p).<br>Therefore, <b><code>df = 3 - 1 - 1 = 1</code></b> (Always 1 degree of freedom for a 2-allele locus!).</li><li>Step 5: Compare calculated &chi;&sup2; with table value at 5% level of significance (&chi;&sup2;<sub>crit</sub> = 3.841). If &chi;&sup2;<sub>calc</sub> &le; 3.841, null hypothesis is accepted: population is in HWE.</li></ol><br><b>5. Evolutionary Forces Altering Gene Frequencies in Livestock:</b><ul><li><b>A. Selection (Artificial and Natural):</b> The primary tool of the animal breeder. Selection acts by differential reproductive success. Directional selection against recessive homozygotes (<code>aa</code> with selection coefficient <code>s</code>) reduces <code>q</code> over generations:<br><code>&Delta;q = -sq&sup2;(1 - q) / (1 - sq&sup2;)</code>. Complete culling (<code>s = 1.0</code>) changes <code>q<sub>1</sub> = q<sub>0</sub> / (1 + q<sub>0</sub>)</code>.</li><li><b>B. Migration (Gene Flow):</b> Introduction of breeding animals from an outside donor population. If migrant proportion is <code>m</code> with allele frequency <code>q<sub>m</sub></code>, and native frequency is <code>q<sub>0</sub></code>:<br><code>q<sub>1</sub> = m &times; q<sub>m</sub> + (1 - m) &times; q<sub>0</sub> &rArr; &Delta;q = m(q<sub>m</sub> - q<sub>0</sub>)</code>. (e.g., crossbreeding local cattle with exotic HF bulls).</li><li><b>C. Mutation:</b> Spontaneous chemical alteration of nucleotide sequence. If forward mutation <i>A &rarr; a</i> occurs at rate <code>u</code>, and reverse <i>a &rarr; A</i> at rate <code>v</code>, equilibrium frequency is reached at: <code>q_hat = u / (u + v)</code>. Because mutation rates are very low (<code>10<sup>-5</sup> to 10<sup>-6</sup></code>), mutation alone causes negligible change per generation.</li><li><b>D. Genetic Drift:</b> Random sampling fluctuations in finite populations (effective population size <code>N<sub>e</sub></code>). Variance of change in allele frequency per generation is: <code>&sigma;<sub>&Delta;q</sub>&sup2; = pq / (2N<sub>e</sub>)</code>. Causes random loss or fixation of alleles in small closed herds.</li></ul>",
      "keyPoints": [
        "Complete statement and historical attribution (Hardy and Weinberg, 1908).",
        "Mathematical derivation of p² + 2pq + q² = 1 with gametic union probabilities and proof of generational stability.",
        "5 explicit assumptions (infinite size, panmixia, no mutation, no migration, no selection).",
        "Goodness of fit testing with Chi-square, explicitly deriving df = 1 (k - 1 - m = 3 - 1 - 1 = 1) and critical value 3.841.",
        "Detailed quantitative analysis of 4 disturbing forces: Selection (formula for Δq), Migration (formula for Δq), Mutation (u, v balance), and Genetic Drift (sampling variance pq/2Ne)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2017",
        "IVRI 2019",
        "TANUVAS 2020",
        "RAJUVAS 2021",
        "GADVASU 2022",
        "KVASU 2023"
      ]
    },
    {
      "id": "u2-q25",
      "type": "long",
      "marks": 12,
      "question": "Define Heritability (h²) and Repeatability (r). Describe the Paternal Half-Sib Analysis of Variance (ANOVA) method for estimating heritability, including the statistical model, ANOVA table layout, variance components, heritability formula, and standard error. Explain how repeatability is estimated and how it is used to calculate the Most Probable Producing Ability (MPPA) of a dairy cow. Discuss the practical breeding applications of heritability and repeatability in livestock improvement.",
      "topicId": "u2-t25",
      "answer": "<b>1. Fundamental Concepts & Definitions:</b><ul><li><b>Heritability in Narrow Sense (<code>h&sup2;</code>):</b> The proportion of total phenotypic variance (<code>V<sub>P</sub></code>) that is attributable to <i>additive genetic variance</i> (<code>V<sub>A</sub></code>):<br><code>h&sup2; = V<sub>A</sub> / V<sub>P</sub></code> (Ranges from <code>0.0 to 1.0</code>).<br>It measures the extent to which offspring resemble their parents and dictates the efficiency of mass selection.</li><li><b>Repeatability (<code>r</code>):</b> The intraclass correlation coefficient between repeated measurements of the same trait expressed multiple times in the lifetime of an individual (e.g., successive 305-day lactation yields, egg weight, fleece yield):<br><code>r = (V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub> + V<sub>Eg</sub>) / V<sub>P</sub> = (V<sub>G</sub> + V<sub>Eg</sub>) / V<sub>P</sub></code>.<br>Because it includes both permanent environmental variance (<code>V<sub>Eg</sub></code>) and non-additive genetic variance, <b>repeatability sets the upper biological limit for heritability (<code>r &ge; h&sup2;</code>)</b>.</li></ul><br><b>2. Estimation of Heritability by Paternal Half-Sib Correlation (One-Way Nested ANOVA):</b><br>This is the most standard biometrical method in dairy cattle and poultry where multiple sires are mated to random, distinct groups of dams, each dam producing one recorded daughter.<br><br><b>Statistical Model:</b><br><code>Y<sub>ij</sub> = &mu; + s<sub>i</sub> + e<sub>ij</sub></code><br>where: <code>Y<sub>ij</sub></code> = phenotypic observation on the <i>j</i>-th progeny of the <i>i</i>-th sire;<br><code>&mu;</code> = general population mean;<br><code>s<sub>i</sub></code> = random effect of <i>i</i>-th sire ~ <code>NID(0, &sigma;<sub>s</sub>&sup2;)</code>;<br><code>e<sub>ij</sub></code> = random residual error associated with <i>j</i>-th progeny within <i>i</i>-th sire ~ <code>NID(0, &sigma;<sub>e</sub>&sup2;)</code>.<br><br><b>ANOVA Table Layout (for <code>S</code> sires, each having <code>k</code> progeny, total <code>N = S &times; k</code>):</b><ul><li><b>Between Sires:</b> Degrees of Freedom = <code>S - 1</code>; Mean Square = <code>MS<sub>S</sub></code>; Expected Mean Square = <code>E(MS<sub>S</sub>) = &sigma;<sub>e</sub>&sup2; + k &times; &sigma;<sub>s</sub>&sup2;</code></li><li><b>Within Sires (Between Progeny):</b> Degrees of Freedom = <code>N - S</code>; Mean Square = <code>MS<sub>W</sub></code>; Expected Mean Square = <code>E(MS<sub>W</sub>) = &sigma;<sub>e</sub>&sup2;</code></li></ul><i>Note:</i> For unequal family sizes, the coefficient <code>k</code> is replaced by:<br><code>k* = [1 / (S - 1)] &times; [N - (&sum; n<sub>i</sub>&sup2; / N)]</code>.<br><br><b>Computation of Variance Components:</b><br><code>&sigma;<sub>e</sub>&sup2; = MS<sub>W</sub></code><br><code>&sigma;<sub>s</sub>&sup2; = (MS<sub>S</sub> - MS<sub>W</sub>) / k*</code><br>Total Phenotypic Variance = <code>&sigma;<sub>P</sub>&sup2; = &sigma;<sub>s</sub>&sup2; + &sigma;<sub>e</sub>&sup2;</code>.<br><br><b>Intraclass Correlation (<code>t</code>) & Heritability Formulation:</b><br>The intraclass correlation among paternal half-sibs is: <code>t = &sigma;<sub>s</sub>&sup2; / (&sigma;<sub>s</sub>&sup2; + &sigma;<sub>e</sub>&sup2;)</code>.<br>Genetically, covariance among paternal half-sibs equals <code>&frac14; V<sub>A</sub></code>. Thus, the sire component <code>&sigma;<sub>s</sub>&sup2; = &frac14; V<sub>A</sub></code>.<br>Therefore:<br><b><code>h&sup2; = 4 &times; t = 4 &times; &sigma;<sub>s</sub>&sup2; / (&sigma;<sub>s</sub>&sup2; + &sigma;<sub>e</sub>&sup2;)</code></b>.<br><br><b>Standard Error of Heritability:</b><br><code>SE(h&sup2;) &approx; 4 &times; &radic;[ {2(1 - t)&sup2; &times; [1 + (k* - 1)t]&sup2;} / {k*(k* - 1)(S - 1)} ]</code>.<br><br><b>3. Estimation of Repeatability and Most Probable Producing Ability (MPPA):</b><br>Repeatability is estimated via one-way ANOVA across repeated lactation records of <code>N</code> cows (Between Cows and Within Cows across lactations):<br><code>r = &sigma;<sub>c</sub>&sup2; / (&sigma;<sub>c</sub>&sup2; + &sigma;<sub>w</sub>&sup2;)</code>.<br><br><b>Most Probable Producing Ability (MPPA):</b><br>MPPA predicts an animal's future production based on <code>n</code> past records, taking into account herd average (<code>&mu;</code>):<br><b><code>MPPA = &mu; + [ (n &times; r) / (1 + (n - 1)r) ] &times; (X_bar - &mu;)</code></b><br>where: <code>n</code> = number of completed lactations, <code>r</code> = repeatability of lactation yield (~0.40), <code>X_bar</code> = cow's average milk yield, <code>&mu;</code> = herd average.<br><i>Application:</i> Enables accurate culling of cows with poor future milk yield after 1 or 2 lactations.<br><br><b>4. Practical Applications in Livestock Breeding:</b><ul><li><b>Predicting Selection Response:</b> Genetic gain per generation is directly proportional to heritability: <code>R = h&sup2; &times; S = i &times; h &times; &sigma;<sub>A</sub></code>.</li><li><b>Choice of Selection Method:</b><ul><li><i>High h² (>0.40, e.g., Body weight at yearling, fat percentage):</i> Individual (mass) selection is highly effective.</li><li><i>Moderate h² (0.20–0.40, e.g., 305-day milk yield):</i> Pedigree and progeny testing combined with individual selection.</li><li><i>Low h² (<0.10, e.g., Calving interval, service period, fertility traits):</i> Individual selection is ineffective; family selection, progeny testing, and management/environmental interventions are required.</li></ul></li><li><b>Culling Decisions:</b> High repeatability (>0.50) justifies culling low-producing females based on their very first lactation record, because future performance will closely mirror past records.</li><li><b>Multiple Records Efficiency:</b> The gain in accuracy of estimating breeding value from <code>n</code> records is: <code>&radic;[n / {1 + (n - 1)r}]</code>. Diminishing returns occur beyond 3 lactations when <code>r &approx; 0.40</code>.</li></ul>",
      "keyPoints": [
        "Definitions and biological limits of h² and r (r >= h²).",
        "Paternal half-sib model: Y_ij = μ + s_i + e_ij.",
        "Complete ANOVA table with df, MS, EMS (σ_e² + k*σ_s²), and derivation of h² = 4t.",
        "Standard error of heritability formula.",
        "Repeatability formula and MPPA derivation: MPPA = μ + [nr / (1 + (n-1)r)] * (X̄ - μ).",
        "Livestock breeding applications: Selection method choice based on h² magnitude, culling based on r, predicting genetic response R = h²S."
      ],
      "diagram": "",
      "table": {
        "title": "One-Way Nested ANOVA Table for Paternal Half-Sib Heritability Estimation",
        "headers": [
          "Source of Variation",
          "Degrees of Freedom (df)",
          "Sum of Squares (SS)",
          "Mean Square (MS)",
          "Expected Mean Square [E(MS)]"
        ],
        "rows": [
          [
            "Between Sires",
            "S - 1",
            "SS_S = Σ (Y_i.² / n_i) - (Y_..² / N)",
            "MS_S = SS_S / (S - 1)",
            "σ_e² + k* σ_s²"
          ],
          [
            "Within Sires (Residual Progeny)",
            "N - S",
            "SS_W = SS_Total - SS_S",
            "MS_W = SS_W / (N - S)",
            "σ_e²"
          ],
          [
            "Total",
            "N - 1",
            "SS_Total = ΣΣ Y_ij² - (Y_..² / N)",
            "-",
            "-"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2018",
        "TANUVAS 2019",
        "IVRI 2020",
        "GADVASU 2021",
        "KVASU 2022",
        "LUVAS 2023"
      ]
    }
  ],
  "unit-3": [
    {
      "id": "u3-q01",
      "type": "define",
      "marks": 2,
      "question": "Define Selection Differential (S) and state its mathematical formula.",
      "topicId": "u3-t01",
      "answer": "<b>Selection Differential (S):</b><br>The difference between the average phenotypic value of the selected individuals chosen as breeding parents (<code>X_bar<sub>s</sub></code>) and the average phenotypic value of the entire unselected parental generation from which they were selected (<code>X_bar<sub>p</sub></code>):<br><code>S = X_bar<sub>s</sub> - X_bar<sub>p</sub></code><br><br>It measures the phenotypic superiority of the selected parents and is expressed in the actual units of the trait.",
      "keyPoints": [
        "Difference between mean of selected parents and mean of parental population.",
        "Formula: S = X̄_s - X̄_p.",
        "Expressed in actual physical units of measurement (kg milk, grams gain)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2020",
        "TANUVAS 2021",
        "KVASU 2022"
      ]
    },
    {
      "id": "u3-q02",
      "type": "define",
      "marks": 2,
      "question": "Define Selection Intensity (i) and state its relationship with Selection Differential.",
      "topicId": "u3-t01",
      "answer": "<b>Selection Intensity (i):</b><br>The selection differential expressed in units of standard deviation of the phenotypic trait (standardized selection differential):<br><code>i = S / &sigma;<sub>P</sub></code> &rArr; <code>S = i &times; &sigma;<sub>P</sub></code><br><br>It is a dimensionless quantity that depends strictly on the proportion of animals selected (<code>p</code>) from a normally distributed herd, obtained as the ordinate height (<code>z</code>) of the standard normal curve divided by <code>p</code>: <code>i = z / p</code>.",
      "keyPoints": [
        "Standardized selection differential: i = S / σ_P.",
        "Dimensionless value depending solely on the proportion selected (p).",
        "Relationship: S = i * σ_P."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "GADVASU 2019",
        "LUVAS 2021",
        "MAFSU 2023"
      ]
    },
    {
      "id": "u3-q03",
      "type": "define",
      "marks": 2,
      "question": "Define Generation Interval (L) and cite typical values for cattle, sheep, and poultry.",
      "topicId": "u3-t01",
      "answer": "<b>Generation Interval (L):</b><br>The average age of the parents when their replacement offspring (which become parents in the next generation) are born.<br>Mathematically computed as the average of four pathways: <code>L = (L<sub>SS</sub> + L<sub>SD</sub> + L<sub>DS</sub> + L<sub>DD</sub>) / 4</code> (Sire to Son, Sire to Daughter, Dam to Son, Dam to Daughter).<br><br><b>Typical Values in Domestic Animals:</b><ul><li><b>Dairy Cattle & Buffaloes:</b> 4.5 &ndash; 5.5 years (long interval slows annual genetic gain: <code>&Delta;G/year = R / L</code>).</li><li><b>Sheep & Goats:</b> 2.0 &ndash; 3.0 years.</li><li><b>Swine:</b> 1.5 &ndash; 2.0 years.</li><li><b>Poultry:</b> 1.0 &ndash; 1.2 years (allowing very rapid annual genetic progress).</li></ul>",
      "keyPoints": [
        "Average age of parents when replacement offspring are born.",
        "Four reproductive pathways (L_SS, L_SD, L_DS, L_DD).",
        "Values: Cattle 4.5-5.5 yrs, Sheep 2-3 yrs, Poultry ~1 yr.",
        "Inversely proportional to annual genetic response (ΔG/yr = R / L)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2019",
        "TANUVAS 2021",
        "DUVASU 2023"
      ]
    },
    {
      "id": "u3-q04",
      "type": "define",
      "marks": 2,
      "question": "Define Inbreeding Coefficient (FX) according to Sewall Wright and Gustave Malécot.",
      "topicId": "u3-t10",
      "answer": "<b>Inbreeding Coefficient (F<sub>X</sub>):</b><br><ul><li><b>Wright's Definition (1921):</b> The correlation coefficient between the uniting gametes that formed the individual, measuring the relative reduction in heterozygosity compared to a base population.</li><li><b>Malécot's Definition (1948):</b> The probability that two homologous alleles at any given autosomal locus in an individual are <b>identical by descent (autozygous)</b>, having been inherited from a common ancestor.</li></ul><b>Wright's Formula:</b> <code>F<sub>X</sub> = &sum; [ (&frac12;)<sup>n1 + n2 + 1</sup> &times; (1 + F<sub>A</sub>) ]</code>",
      "keyPoints": [
        "Wright: Correlation between uniting gametes; proportional decrease in heterozygosity.",
        "Malécot: Probability that two alleles at a locus are identical by descent (IBD).",
        "Wright's formula: F_X = Σ [(1/2)^(n1 + n2 + 1) * (1 + F_A)]."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2020",
        "RAJUVAS 2022",
        "KVAFSU 2023"
      ]
    },
    {
      "id": "u3-q05",
      "type": "define",
      "marks": 2,
      "question": "Define Coefficient of Relationship (RXY) and state its values for parent-offspring and full-sibs.",
      "topicId": "u3-t10",
      "answer": "<b>Coefficient of Relationship (R<sub>XY</sub>):</b><br>The measure of the pedigree degree of genetic relationship between two individuals <i>X</i> and <i>Y</i>; defined as the expected fraction of their genes that are identical by descent (IBD) from one or more common ancestors:<br><code>R<sub>XY</sub> = [ &sum; (&frac12;)<sup>n1 + n2</sup> &times; (1 + F<sub>A</sub>) ] / &radic;[ (1 + F<sub>X</sub>)(1 + F<sub>Y</sub>) ]</code><br><br><b>Standard Relationship Values in Non-inbred Populations (F = 0):</b><ul><li><b>Parent & Offspring:</b> <code>R = 0.50 (50%)</code></li><li><b>Full-Sibs:</b> <code>R = 0.50 (50%)</code></li><li><b>Half-Sibs:</b> <code>R = 0.25 (25%)</code></li><li><b>First Cousins:</b> <code>R = 0.125 (12.5%)</code></li></ul>",
      "keyPoints": [
        "Fraction of genes shared between two individuals identical by descent.",
        "Formula: R_XY = Σ [(1/2)^(n1+n2) * (1+F_A)] / sqrt((1+F_X)(1+F_Y)).",
        "Values: Parent-offspring = 0.50, Full-sibs = 0.50, Half-sibs = 0.25."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "GADVASU 2021",
        "KVASU 2022",
        "WBUAFS 2023"
      ]
    },
    {
      "id": "u3-q06",
      "type": "define",
      "marks": 2,
      "question": "Define Prepotency and state the genetic basis underlying prepotent sires.",
      "topicId": "u3-t12",
      "answer": "<b>Prepotency:</b><br>The distinct ability of an individual parent (especially a breeding sire) to stamp its own characteristics upon its offspring with such uniformity that the progeny closely resemble the parent and each other, regardless of the genetic constitution of the dams to which it is mated.<br><br><b>Genetic Basis:</b><ul><li>Presence of a high degree of <b>homozygosity for dominant genes</b> controlling the desired traits.</li><li>Because the sire is homozygous dominant (<code>AA, BB, CC</code>), all his gametes carry dominant alleles, ensuring dominance over recessive alleles contributed by diverse dams.</li><li>Often achieved through deliberate <b>linebreeding</b> to a superior ancestor.</li></ul>",
      "keyPoints": [
        "Ability of a sire to transmit traits uniformly to offspring regardless of dam's genotype.",
        "Genetic basis: High homozygosity for dominant favorable alleles.",
        "Produces exceptional uniformity in progeny; promoted by linebreeding."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2019",
        "TANUVAS 2020",
        "LUVAS 2022"
      ]
    },
    {
      "id": "u3-q07",
      "type": "define",
      "marks": 2,
      "question": "Define Grading Up and calculate the exotic/superior inheritance in the 4th generation (G4).",
      "topicId": "u3-t15",
      "answer": "<b>Grading Up:</b><br>A system of continuous outcrossing in which purebred sires of an established, superior breed are mated successively generation after generation to nondescript, unimproved indigenous scrub females and their female descendants.<br><br><b>Inheritance in 4th Generation (G4):</b><br>The fraction of improved/exotic breed inheritance increases in successive backcross generations according to the formula: <code>1 - (&frac12;)<sup>n</sup></code>.<br><ul><li>G1 (F1): <code>&frac12; = 50.0%</code> superior inheritance</li><li>G2: <code>&frac34; = 75.0%</code> superior inheritance</li><li>G3: <code>7/8 = 87.5%</code> superior inheritance</li><li><b>G4: <code>15/16 = 93.75%</code> superior inheritance</b></li></ul>By the 5th generation (31/32 or 96.88%), the graded population is practically indistinguishable from the purebred sire breed.",
      "keyPoints": [
        "Mating purebred superior sires to nondescript scrub females over successive generations.",
        "Formula for generation n: 1 - (1/2)^n.",
        "G4 inheritance = 15/16 = 93.75% superior inheritance."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2018",
        "TANUVAS 2021",
        "KVASU 2023"
      ]
    },
    {
      "id": "u3-q08",
      "type": "define",
      "marks": 2,
      "question": "Define Heterobeltiosis and differentiate it from Mid-Parent Heterosis.",
      "topicId": "u3-t14",
      "answer": "<ul><li><b>Heterobeltiosis (Better-Parent Heterosis):</b> The superiority of the crossbred (F1) hybrid over the <i>better (superior) of the two parental purebred lines</i> for a given trait:<br><code>Heterobeltiosis (%) = [ (F1 - Better Parent) / Better Parent ] &times; 100</code><br><i>Significance:</i> Critical benchmark in commercial breeding; crossbreeding is economically worthwhile only when F1 surpasses the better purebred parent.</li><li><b>Mid-Parent Heterosis:</b> The superiority of the F1 hybrid over the <i>arithmetic average of the two parental lines</i>:<br><code>Mid-Parent Heterosis (%) = [ (F1 - Mid-Parent) / Mid-Parent ] &times; 100</code></li></ul>",
      "keyPoints": [
        "Heterobeltiosis: Superiority of F1 hybrid over the better parent: [(F1 - BP) / BP] * 100.",
        "Mid-parent heterosis: Superiority of F1 over the mean of both parents: [(F1 - MP) / MP] * 100.",
        "Commercial importance: Validates whether crossbreeding outyields the best pure breed."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2021",
        "GADVASU 2022",
        "MAFSU 2023"
      ]
    },
    {
      "id": "u3-q09",
      "type": "define",
      "marks": 2,
      "question": "Distinguish between General Combining Ability (GCA) and Specific Combining Ability (SCA).",
      "topicId": "u3-t14",
      "answer": "<ul><li><b>General Combining Ability (GCA):</b> The average performance of a particular inbred line or parent across a wide series of crosses with other lines.<br><i>Genetic Basis:</i> Controlled primarily by <b>additive gene action (<code>V<sub>A</sub></code>)</b>.<br><i>Breeding Role:</i> Used to identify superior pure lines to be maintained for recurrent selection.</li><li><b>Specific Combining Ability (SCA):</b> Cases where certain specific crosses perform significantly better or worse than expected based on the average GCA of the parental lines.<br><i>Genetic Basis:</i> Controlled by <b>non-additive gene action (dominance <code>V<sub>D</sub></code> and epistasis <code>V<sub>I</sub></code>)</b>.<br><i>Breeding Role:</i> Exploited in commercial terminal 2-way and 4-way poultry and swine crosses.</li></ul>",
      "keyPoints": [
        "GCA: Average crossbred performance across multiple lines; governed by additive gene action (V_A).",
        "SCA: Deviation of a specific cross from GCA expectation; governed by non-additive gene action (V_D + V_I).",
        "GCA used in purebred selection; SCA exploited in hybrid broiler/layer production."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2020",
        "RAJUVAS 2021",
        "LUVAS 2023"
      ]
    },
    {
      "id": "u3-q10",
      "type": "define",
      "marks": 2,
      "question": "What is Open Nucleus Breeding System (ONBS)? State its main advantage over Closed Nucleus System.",
      "topicId": "u3-t07",
      "answer": "<b>Open Nucleus Breeding System (ONBS):</b><br>A hierarchical breeding structure comprising a central high-merit <b>Nucleus herd</b> and surrounding commercial <b>Multiplier / Base herds</b>, where gene flow is <b>bidirectional</b>: superior elite females identified in the base herds are continuously introduced ('screened') into the nucleus, while elite sires born in the nucleus are disseminated down to the base herds.<br><br><b>Main Advantages over Closed Nucleus:</b><ul><li><b>Controls Inbreeding:</b> Gene inflow from the base expands effective population size, keeping the rate of inbreeding (<code>&Delta;F</code>) significantly lower.</li><li><b>Accelerates Genetic Gain:</b> Increases selection intensity by tapping exceptional outlier animals from the large commercial base population.</li></ul>",
      "keyPoints": [
        "Hierarchical nucleus-base system with two-way gene flow (upward elite females, downward elite sires).",
        "Overcomes inbreeding depression seen in small closed nucleus herds.",
        "Higher selection intensity by screening superior females from the broad base."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "GADVASU 2020",
        "IVRI 2022",
        "KVASU 2023"
      ]
    },
    {
      "id": "u3-q11",
      "type": "define",
      "marks": 2,
      "question": "Define Mean Kinship (MK) and state its role in conservation of endangered livestock breeds.",
      "topicId": "u3-t25",
      "answer": "<b>Mean Kinship (MK):</b><br>The average coefficient of kinship (kinship coefficient <code>f<sub>ij</sub></code>) between a given individual and all living members of the current population (including itself):<br><code>MK<sub>i</sub> = [ &sum;<sub>j=1</sub><sup>N</sup> f<sub>ij</sub> ] / N</code><br><br><b>Role in Conservation Breeding Programs:</b><ul><li>Measures how genetically representative and closely related an animal is to the entire herd.</li><li><b>Selection Criterion:</b> Animals with the <b>lowest Mean Kinship</b> possess the rarest, most unique alleles. Prioritizing low-MK individuals for breeding maximizes retained gene diversity and minimizes long-term inbreeding rates in endangered indigenous breeds (e.g., Punganur cattle, Toda buffalo).</li></ul>",
      "keyPoints": [
        "Average kinship coefficient of an individual with all animals in the population: MK_i = (Σ f_ij) / N.",
        "Inverse indicator of genetic uniqueness.",
        "Breeding low-MK animals preserves maximum allelic diversity and minimizes population inbreeding."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2021",
        "KVASU 2022",
        "DUVASU 2023"
      ]
    },
    {
      "id": "u3-q12",
      "type": "define",
      "marks": 2,
      "question": "Define Effective Population Size (Ne) and state Wright's formula for unequal sex ratios.",
      "topicId": "u3-t25",
      "answer": "<b>Effective Population Size (N<sub>e</sub>):</b><br>The size of an ideal, panmictic population that would experience the same rate of inbreeding (<code>&Delta;F</code>) or the same rate of random genetic drift (allelic variance) as the actual census population under study.<br><br><b>Wright's Formula for Unequal Number of Breeding Males (N<sub>m</sub>) and Females (N<sub>f</sub>):</b><br><b><code>N<sub>e</sub> = (4 &times; N<sub>m</sub> &times; N<sub>f</sub>) / (N<sub>m</sub> + N<sub>f</sub>)</code></b><br><br><i>Breeding Implication:</i> Because <code>N<sub>m</sub></code> is very small in artificial insemination programs (e.g., 5 bulls mated to 500 cows), <code>N<sub>e</sub></code> is overwhelmingly constrained by the number of breeding males: <code>N<sub>e</sub> &approx; 4 N<sub>m</sub> = 20</code>, resulting in rapid inbreeding accumulation despite hundreds of cows.",
      "keyPoints": [
        "Size of an idealized population having identical inbreeding rate / drift as the actual population.",
        "Formula: Ne = (4 * N_m * N_f) / (N_m + N_f).",
        "Heavily constrained by the rarer sex (breeding bulls in AI programs)."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "IVRI 2020",
        "GADVASU 2021",
        "LUVAS 2022",
        "KVAFSU 2023"
      ]
    },
    {
      "id": "u3-q13",
      "type": "diff",
      "marks": 5,
      "question": "Compare Tandem Selection, Independent Culling Levels, and Selection Index methods for multi-trait selection in livestock.",
      "topicId": "u3-t09",
      "answer": "<b>Comparison of Multi-Trait Selection Methods (Hazel & Lush, 1942):</b><br>In commercial livestock breeding, animals must be improved simultaneously for several economically important traits (e.g., milk yield, fat percentage, age at first calving, and mastitis resistance). Three methods are available.<br><br><b>Relative Genetic Efficiency (Hazel and Lush):</b><br>Assuming traits are uncorrelated and equally important, relative efficiency is:<br><b>Selection Index (1.00) &gt; Independent Culling Levels (0.70&ndash;0.80) &gt; Tandem Selection (1 / &radic;n)</b>.<br>When selecting for 4 traits (<code>n = 4</code>), tandem selection is only half as efficient (<code>1/&radic;4 = 0.50</code>) as an index.",
      "keyPoints": [
        "Tandem: Selects one trait at a time; least efficient; genetic regression in unselected traits due to negative correlations.",
        "Independent Culling: Establishes minimum cutoff for each trait; culls animals failing any threshold regardless of excellence in others.",
        "Selection Index: Total net merit score I = Σ b_i X_i; most efficient; compensates weakness in one trait with superiority in another."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Comparison of Multi-Trait Selection Methods",
        "headers": [
          "Feature",
          "Tandem Selection",
          "Independent Culling Levels (ICL)",
          "Selection Index (Hazel, 1943)"
        ],
        "rows": [
          [
            "Selection Approach",
            "Selects for one trait at a time over generations until target is achieved, then switches to next trait",
            "Establishes independent minimum threshold standards for all traits simultaneously",
            "Combines all traits into a single aggregate economic score: I = b1*X1 + b2*X2 + ... + bn*Xn"
          ],
          [
            "Compensation Among Traits",
            "Zero compensation (only one trait evaluated per phase)",
            "Zero compensation; exceptional merit in one trait cannot compensate failure in another",
            "Complete compensation; exceptional merit in one trait balances slight deficiency in another"
          ],
          [
            "Relative Efficiency",
            "Least efficient: 1 / √n (where n = number of traits)",
            "Intermediate efficiency (~70-80% of index efficiency)",
            "Most efficient mathematically and economically (100% benchmark)"
          ],
          [
            "Impact of Negative Correlations",
            "High risk; selecting for milk yield severely deteriorates fat percentage during that phase",
            "Moderate; may cull too many animals if antagonistic traits are selected together",
            "Optimal; economic weights and genetic covariances directly account for negative correlations"
          ],
          [
            "Practical Application",
            "Rarely used commercially; historical method",
            "Widely used at culling gates (e.g., culling bulls failing semen motility standards)",
            "Standard tool in modern dairy, swine, and poultry genetic evaluation (e.g., TPI, NM$)"
          ]
        ]
      },
      "pyq": [
        "IVRI 2019",
        "TANUVAS 2021",
        "KVASU 2022",
        "GADVASU 2023"
      ]
    },
    {
      "id": "u3-q14",
      "type": "diff",
      "marks": 5,
      "question": "Differentiate between Close Breeding and Linebreeding with animal pedigree examples and breeding goals.",
      "topicId": "u3-t12",
      "answer": "<b>Comparison between Close Breeding and Linebreeding:</b><br>Both are forms of inbreeding (mating of individuals more closely related than the average of the population), but they differ sharply in their degree of relationship, intensity of inbreeding, and breeding objectives.<br><br><b>Breeding Goals:</b><ul><li><b>Close Breeding:</b> Used experimentally to rapidly uncover and purge lethal recessive genes, create homozygous inbred lines for heterosis in crossbreeding, and establish laboratory animal lines.</li><li><b>Linebreeding:</b> Used commercially by master breeders to concentrate the genetic contribution (high relationship <code>R</code>) of an outstanding, proven ancestral sire or dam across generations while keeping the inbreeding coefficient (<code>F</code>) low and safe.</li></ul>",
      "keyPoints": [
        "Close breeding: Matings between first-degree relatives (sire-daughter, brother-sister); F >= 0.25; high risk of inbreeding depression.",
        "Linebreeding: Matings aimed at maintaining high relationship (R) to an admired ancestor while keeping F < 0.10.",
        "Close breeding purges deleterious recessives; Linebreeding preserves prepotency and elite ancestral germplasm."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Differences Between Close Breeding and Linebreeding",
        "headers": [
          "Feature",
          "Close Breeding",
          "Linebreeding"
        ],
        "rows": [
          [
            "Pedigree Mating Type",
            "Mating of first-degree relatives: Full brother x Full sister, Sire x Daughter, Dam x Son",
            "Mating of more distant relatives: Grandson x Granddaughter, Half-sib x Half-sib, Cousin x Cousin directed towards an elite ancestor"
          ],
          [
            "Inbreeding Coefficient (F)",
            "Increases very rapidly (F >= 0.25 or 25% in a single generation)",
            "Maintained at a low, controlled level (typically F < 0.10 or 10%)"
          ],
          [
            "Relationship to Common Ancestor",
            "General relationship to multiple recent ancestors",
            "Concentrates genetic relationship (R >= 0.25 to 0.50) specifically to one outstanding admired ancestor"
          ],
          [
            "Risk of Inbreeding Depression",
            "Extremely high risk of juvenile mortality, reduced fertility, and lethal anomalies",
            "Minimal to mild risk; allows continuous culling of slight abnormalities"
          ],
          [
            "Primary Breeding Objective",
            "Purging lethal recessives; generating homozygous parental inbred lines for hybrid vigor",
            "Conserving elite sire/dam genes; fixing type and prepotency in a registered pedigree herd"
          ],
          [
            "Suitability for Commercial Farmers",
            "Strongly discouraged in commercial farm stock",
            "Recommended for elite pedigree seedstock breeders with rigorous culling"
          ]
        ]
      },
      "pyq": [
        "TANUVAS 2020",
        "IVRI 2021",
        "KVASU 2023"
      ]
    },
    {
      "id": "u3-q15",
      "type": "short",
      "marks": 5,
      "question": "Describe the Genetic and Phenotypic Consequences of Inbreeding Depression in Dairy Livestock. How can it be managed?",
      "topicId": "u3-t11",
      "answer": "<b>Inbreeding Depression in Dairy Livestock:</b><br>The reduction in phenotypic mean performance, biological fitness, vigor, and fertility resulting from the mating of related individuals.<br><br><b>1. Genetic Consequences:</b><ul><li><b>Increase in Homozygosity:</b> Rate of increase in homozygosity equals <code>F</code>. Alleles become fixed (<code>AA</code> or <code>aa</code>).</li><li><b>Uncovering Deleterious Recessive Alleles:</b> Recessive lethal or sub-lethal alleles previously masked in heterozygous state (<code>Aa</code>) are expressed as homozygotes (<code>aa</code>) (e.g., BLAD, CVM, Mule foot, dwarfism).</li><li><b>Decline in Heterozygote Advantage:</b> Loss of overdominance at loci where heterozygotes are biologically superior.</li></ul><b>2. Phenotypic Consequences on Dairy Production and Fitness:</b><ul><li><b>Milk Production:</b> For every 1% increase in inbreeding (<code>&Delta;F = 0.01</code>), 305-day lactation milk yield declines by <b>15 to 25 kg</b>, and lifetime production declines by over 200 kg.</li><li><b>Reproduction & Fertility:</b> Calving interval increases, service period prolongs, age at first calving increases, and embryonic mortality rises significantly.</li><li><b>Calf Survivability & Vigor:</b> Birth weight decreases by 0.5 kg per 1% F; pre-weaning calf mortality increases due to suppressed immunocompetence.</li></ul><b>3. Remedial Management Strategies:</b><ul><li><b>Outcrossing / Line Crossing:</b> Mating inbred females to unrelated purebred sires completely restores vigor and eliminates inbreeding depression in a single generation.</li><li><b>Pedigree Mating Allocation Software:</b> Utilizing computerized mating programs (e.g., minimum kinship mating) to ensure planned matings maintain <code>F &le; 6.25%</code> in commercial herds.</li><li><b>Expanding Effective Sire Base:</b> Avoiding over-reliance on a single popular AI sire family.</li></ul>",
      "keyPoints": [
        "Definition: Decline in fitness and vigor due to mating related individuals.",
        "Genetic basis: Proportional increase in homozygosity and exposure of deleterious recessives.",
        "Phenotypic losses: 15-25 kg milk loss per 1% F, delayed puberty, poor conception, calf mortality.",
        "Remedies: Outcrossing, computerized mating allocation to cap F < 6.25%, rotating AI sire lines."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2019",
        "GADVASU 2021",
        "LUVAS 2022",
        "MAFSU 2023"
      ]
    },
    {
      "id": "u3-q16",
      "type": "diff",
      "marks": 5,
      "question": "Explain the Genetic Theories of Heterosis (Hybrid Vigor): Dominance Hypothesis vs Overdominance Hypothesis.",
      "topicId": "u3-t14",
      "answer": "<b>Theories of Heterosis (Hybrid Vigor):</b><br>Heterosis is the phenotypic superiority of crossbred F1 progeny over the average of their purebred parental lines. Two primary genetic hypotheses explain this phenomenon.<br><br><b>Reconciliation (Modern Consensus):</b><br>Extensive quantitative and molecular QTL studies demonstrate that <b>both mechanisms operate simultaneously</b>: the Dominance mechanism accounts for the major share of heterosis across polygenic production traits through the masking of thousands of mildly deleterious recessives, while Overdominance operates decisively at specific immune and regulatory loci (e.g., Major Histocompatibility Complex MHC/BoLA loci conferring enhanced disease resistance in crossbreds).",
      "keyPoints": [
        "Dominance Hypothesis (Davenport, Bruce, Keeble & Pellew): Superiority due to masking of deleterious recessives by favorable dominant alleles.",
        "Overdominance Hypothesis (East & Shull): Superiority due to physiological heterozygote advantage (Aa > AA or aa).",
        "Dominance predicts heterosis could theoretically be fixed in pure homozygotes; Overdominance states it can never be fixed in homozygotes.",
        "Modern consensus: Both mechanisms contribute, with dominance predominant in yield traits and overdominance prominent in immune/fitness traits."
      ],
      "diagram": "",
      "table": {
        "title": "Comparison Between Dominance and Overdominance Theories of Heterosis",
        "headers": [
          "Feature",
          "Dominance Hypothesis (Davenport 1908, Bruce 1910)",
          "Overdominance Hypothesis (East 1908, Shull 1908)"
        ],
        "rows": [
          [
            "Basic Premise",
            "Heterosis results from the masking of unfavorable recessive alleles by favorable dominant alleles at multiple loci (AAbbCCdd x aaBBccDD -> AaBbCcDd)",
            "Heterosis results from superior intrinsic physiological/biochemical activity of the heterozygous genotype itself (Aa > AA and Aa > aa)"
          ],
          [
            "Gene Action Involved",
            "Additive and intra-locus complete/partial dominance (V_A and V_D)",
            "Intra-locus overdominance / single-gene heterosis"
          ],
          [
            "Number of Genes Required",
            "Requires multiple complementary loci with linked dominant alleles",
            "Can occur at a single heterozygous gene locus"
          ],
          [
            "Can Heterosis be Fixed in Purebreds?",
            "Theoretically YES, if an individual homozygous for all dominant alleles (AABBCCDD) could be synthesized (hindered only by linkage)",
            "Theoretically IMPOSSIBLE; segregation in subsequent generations inevitably breaks up heterozygosity"
          ],
          [
            "Explanation for F2 Breakdown",
            "Segregation and recombination separates favorable dominant alleles into different gametes",
            "Reduction of heterozygosity by 50% in F2 directly halves the overdominant advantage"
          ],
          [
            "Classic Biological Evidence",
            "Complementary gene action in polygenic growth and yield traits",
            "Sickle cell anemia resistance to malaria in humans; MHC/BoLA heterozygote disease resistance in cattle"
          ]
        ]
      },
      "pyq": [
        "IVRI 2018",
        "TANUVAS 2020",
        "GADVASU 2022",
        "KVASU 2023"
      ]
    },
    {
      "id": "u3-q17",
      "type": "short",
      "marks": 5,
      "question": "Describe the concept and operational 3-year cycle of Reciprocal Recurrent Selection (RRS). Why is it superior to Recurrent Selection?",
      "topicId": "u3-t14",
      "answer": "<b>Reciprocal Recurrent Selection (RRS - Comstock, Robinson & Harvey, 1949):</b><br>A cyclic breeding system designed to improve two genetically distinct populations (Line A and Line B) simultaneously based on their crossbred progeny performance (A &times; B), effectively exploiting <b>both General Combining Ability (GCA - additive variance) and Specific Combining Ability (SCA - non-additive dominance and epistatic variance)</b>.<br><br><b>Operational 3-Year Cycle in Poultry / Swine:</b><ul><li><b>Year 1 (Test Crossing):</b> Sires and dams of Line A are mated to individuals of Line B (A &times; B), and reciprocally sires and dams of Line B are mated to Line A (B &times; A). Simultaneously, purebred lines are reproduced or pure semen/stock preserved.</li><li><b>Year 2 (Crossbred Performance Testing):</b> The resulting crossbred progeny (AB and BA) are tested under commercial field conditions for economic traits (e.g., egg number, feed conversion ratio, broiler body weight). Line A and Line B parents are evaluated based on the performance of their crossbred progeny.</li><li><b>Year 3 (Purebred Multiplication of Selected Elite):</b> High-performing parents (or their purebred progeny) from Line A are inter-se mated to reproduce pure Line A. Similarly, elite Line B individuals are mated to reproduce pure Line B. The cycle then repeats.</li></ul><b>Superiority over Simple Recurrent Selection:</b><br>In simple recurrent selection, a single tester is used (only one line is improved). In RRS, <b>each population acts as the tester for the other</b>, ensuring mutual, reciprocal genetic divergence and maximizing commercial crossbred heterosis in every subsequent cycle.",
      "keyPoints": [
        "Concept: Simultaneous improvement of two distinct lines based on crossbred performance.",
        "Exploits both GCA (additive) and SCA (non-additive dominance/epistasis).",
        "3-year cycle: Year 1 test-cross (A x B and B x A); Year 2 evaluate crossbred progeny; Year 3 inter-se mate best purebred parents within each line.",
        "Superior to recurrent selection because both lines improve reciprocally and become increasingly complementary."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "TANUVAS 2019",
        "IVRI 2021",
        "KVAFSU 2023"
      ]
    },
    {
      "id": "u3-q18",
      "type": "diff",
      "marks": 5,
      "question": "Compare Contemporary Comparison (Daughter-Dam Comparison) and Animal Model BLUP for sire evaluation in dairy cattle.",
      "topicId": "u3-t06",
      "answer": "<b>Comparison of Sire Evaluation Methods:</b><br>Evaluating the genetic merit of dairy bulls is the cornerstone of dairy genetic improvement. Over the past century, methodology has evolved from phenotypic daughter comparisons to advanced statistical linear models.<br><br><b>Why Animal Model BLUP is Superior:</b><ul><li>Uses the <b>numerator relationship matrix (A-matrix)</b> incorporating all pedigree relatives (parents, sibs, progeny) simultaneously.</li><li>Simultaneously evaluates cows and bulls on the exact same scale, eliminating dam merit bias and preferential mating.</li><li>Accounts for non-random herd-year-season (HYS) contemporary group effects and adjusts for genetic trends across generations.</li></ul>",
      "keyPoints": [
        "Contemporary Comparison: Compares daughters against herdmates; ignores non-random mating and genetic merit of dams.",
        "BLUP (Best Linear Unbiased Prediction - C.R. Henderson): Matrix-based mixed model (y = Xb + Zu + e); incorporates numerator relationship matrix (A).",
        "BLUP accounts for fixed environmental effects (HYS), genetic trend, and unequal mating merit of dams."
      ],
      "diagram": "",
      "table": {
        "title": "Comparison Between Contemporary Comparison and Animal Model BLUP",
        "headers": [
          "Feature",
          "Contemporary Comparison (Herdmate Comparison)",
          "Animal Model BLUP (Henderson, 1973)"
        ],
        "rows": [
          [
            "Statistical Model",
            "Simple phenotypic difference: Daughter Mean - Herdmate Contemporary Mean",
            "Mixed Linear Model: y = Xb + Zu + e (b = fixed effects, u = random breeding values)"
          ],
          [
            "Pedigree Information",
            "Uses only daughter records; ignores all collateral relatives and ancestry",
            "Incorporate complete pedigree information via Numerator Relationship Matrix (A^-1)"
          ],
          [
            "Dam Genetic Merit",
            "Assumes all dams are of average genetic merit; biased by preferential mating",
            "Directly accounts for dam merit; completely unbiased by preferential mating of elite cows to top bulls"
          ],
          [
            "Environmental Adjustment",
            "Corrects roughly for herd average, but sensitive to small contemporary group size",
            "Simultaneously estimates fixed herd-year-season (HYS) effects and random genetic effects"
          ],
          [
            "Genetic Trend Handling",
            "Cannot adjust for genetic progress over time; older sires unfairly compared to younger sires",
            "Completely adjusts for genetic trends, allowing fair comparison across generations"
          ],
          [
            "Current Status",
            "Obsolete; used historically prior to 1980s",
            "Global gold standard for national dairy cattle genetic evaluations worldwide"
          ]
        ]
      },
      "pyq": [
        "IVRI 2020",
        "GADVASU 2021",
        "KVASU 2022",
        "LUVAS 2023"
      ]
    },
    {
      "id": "u3-q19",
      "type": "short",
      "marks": 5,
      "question": "Describe the hormonal protocol and operational steps of Multiple Ovulation and Embryo Transfer (MOET) in cattle.",
      "topicId": "u3-t26",
      "answer": "<b>Multiple Ovulation and Embryo Transfer (MOET):</b><br>A reproductive biotechnology whereby a genetically superior donor cow is superovulated with exogenous gonadotropins, inseminated with elite sire semen, and the resulting viable blastocysts are non-surgically recovered (flushed) and transferred to synchronized recipient surrogate mothers.<br><br><b>Step-by-Step Bovine Protocol:</b><ol><li><b>Selection of Donor and Recipient Females:</b> Donor: Top 1&ndash;5% genetic merit, regular estrous cycles, free from reproductive disease. Recipients: Healthy, cycling, fertile cows/heifers.</li><li><b>Superovulation of Donor:</b> On Day 9&ndash;11 of the estrous cycle (mid-luteal phase), administer <b>porcine Pituitary FSH (pFSH, total dose 200&ndash;400 mg)</b> in 8 declining doses given intramuscularly twice daily over 4 consecutive days (e.g., 50/50, 40/40, 30/30, 20/20 mg).</li><li><b>Luteolysis (PGF2&alpha;):</b> Concurrently with the 5th or 6th injection of FSH (on Day 3 of protocol), inject a luteolytic dose of <b>PGF2&alpha; (e.g., Cloprostenol 500 &mu;g)</b> to induce rapid luteolysis of the corpus luteum and induce estrus within 40&ndash;48 hours.</li><li><b>Insemination:</b> Inseminate donor at 12, 24, and 36 hours after standing heat onset using high-quality semen (often 2 doses per insemination) to ensure fertilization of all ovulated ova.</li><li><b>Non-Surgical Embryo Flushing (Day 7):</b> Exactly <b>Day 7 post-estrus</b> (when embryos are in morula or early blastocyst stage residing in the uterine horns), introduce a sterile two-way or three-way Foley catheter into the uterine horn. Inflate balloon (10&ndash;15 mL) to seal cervix. Infuse Dulbecco's Phosphate Buffered Saline (DPBS) supplemented with 1% BSA or fetal calf serum, flushing 500&ndash;1000 mL per horn into an embryo filter.</li><li><b>Embryo Evaluation & Transfer:</b> Screen filter under stereomicroscope. Grade embryos according to IETS standards (Code 1 Excellent/Good, Code 2 Fair, Code 3 Poor, Code 4 Degenerate). Transfer Stage 4&ndash;6 embryos into the ipsilateral uterine horn of recipient cows synchronized to within &plusmn;24 hours of donor estrus, or cryopreserve in 1.5 M ethylene glycol in liquid nitrogen (-196&deg;C).</li></ol>",
      "keyPoints": [
        "Definition of MOET as superovulation, AI, flushing, and transfer to recipients.",
        "pFSH protocol: 8 declining doses twice daily starting Day 9-11 of cycle.",
        "Luteolysis on Day 3 of protocol using PGF2α (cloprostenol).",
        "Day 7 non-surgical flushing with Foley catheter using DPBS.",
        "IETS embryo grading and transfer to synchronized recipients (±24h estrus match) or cryopreservation."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2019",
        "IVRI 2021",
        "TANUVAS 2022",
        "KVASU 2023"
      ]
    },
    {
      "id": "u3-q20",
      "type": "diff",
      "marks": 5,
      "question": "Differentiate between In-situ and Ex-situ conservation of Animal Genetic Resources (AnGR) with Indian livestock examples.",
      "topicId": "u3-t24",
      "answer": "<b>Conservation of Animal Genetic Resources (AnGR):</b><br>India possesses immense indigenous animal genetic diversity (212 registered indigenous breeds recognized by ICAR-NBAGR). To prevent the extinction of threatened native germplasm (e.g., Punganur, Red Sindhi, Toda, Nilgiri), two conservation strategies are implemented.<br><br><b>FAO Recommendation for AnGR:</b><br>In-situ and Ex-situ conservation should be implemented in an integrated, complementary manner: In-situ maintains the living, evolving population in pastoral communities, while Ex-situ (Cryoconservation in the National Gene Bank at NBAGR Karnal) provides a permanent safety backup against catastrophic disease outbreaks or climatic disasters.",
      "keyPoints": [
        "In-situ: Conservation within natural ecological habitat where animals evolved (live breeding herds in farmers' fields).",
        "Ex-situ in vivo: Maintaining live animals outside native tract (state farms, universities, zoos).",
        "Ex-situ in vitro: Cryopreservation of germplasm (semen, embryos, somatic cells, DNA) at -196°C in gene banks (NBAGR Karnal).",
        "Dynamic evolutionary adaptation (in-situ) vs frozen static insurance (ex-situ)."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Differences Between In-situ and Ex-situ Conservation of AnGR",
        "headers": [
          "Feature",
          "In-situ Conservation",
          "Ex-situ Conservation (In vivo & In vitro)"
        ],
        "rows": [
          [
            "Definition & Location",
            "Maintenance of live populations in their natural production environments where they evolved and adapted",
            "Maintenance of live animals outside native tract (in vivo) OR cryopreserved germplasm at -196°C (in vitro)"
          ],
          [
            "Dynamic Adaptation & Evolution",
            "Continuous evolutionary adaptation to changing climatic pathogens and local forage resources",
            "Evolution is halted (in vitro cryopreservation freezes genetic change at sampling point)"
          ],
          [
            "Operational Cost",
            "Relatively low public capital cost; supported by livestock owners who generate livelihood from animals",
            "High initial capital and maintenance costs for liquid nitrogen infrastructure, cryo-tanks, and state livestock farms"
          ],
          [
            "Utilization & Livelihoods",
            "Provides active economic products (milk, draught, meat, dung) and cultural value to rural pastoral communities",
            "Animals or germplasm remain largely non-productive storage backups until reconstituted"
          ],
          [
            "Risk of Disease / Disasters",
            "Vulnerable to local epidemics (FMD, Anthrax, Lumpy Skin Disease), droughts, and civil strife",
            "Secure from local environmental disasters; housed in biosecure repositories"
          ],
          [
            "Indian Examples",
            "Community breeding tracts of Toda buffaloes in Nilgiris; Kangayam cattle in Tamil Nadu pastoral systems",
            "National Gene Bank at ICAR-NBAGR Karnal (cryopreserved semen doses of 50+ indigenous breeds); institutional nucleus herds"
          ]
        ]
      },
      "pyq": [
        "TANUVAS 2020",
        "IVRI 2021",
        "GADVASU 2022",
        "DUVASU 2023"
      ]
    },
    {
      "id": "u3-q21",
      "type": "long",
      "marks": 12,
      "question": "Describe the various Bases of Selection used in domestic livestock improvement: Individual (Mass) Selection, Pedigree Selection, Collateral / Sib Selection, and Progeny Testing. Compare their principles, accuracy of estimating breeding value (r_AI), advantages, limitations, and suitability for different livestock traits. Present a comprehensive comparative summary table.",
      "topicId": "u3-t02",
      "answer": "<b>1. Introduction to Bases of Selection:</b><br>Selection is the non-random process that determines which individuals become parents of the next generation and how many offspring they produce. The effectiveness of selection depends on the <b>accuracy of predicting an individual's true additive breeding value (r<sub>AI</sub>)</b>. Animal breeders utilize information from four primary sources: the individual's own phenotype, ancestral pedigree records, collateral relatives (sibs), and progeny performance.<br><br><b>2. Detailed Analysis of Each Selection Base:</b><br><br><b>A. Individual (Mass) Selection:</b><ul><li><b>Principle:</b> Animals are evaluated and selected purely on their own individual phenotypic record, regardless of relatives.</li><li><b>Accuracy:</b> <code>r<sub>AI</sub> = h = &radic;(h&sup2;)</code> (The square root of narrow-sense heritability).</li><li><b>Advantages:</b> Simplest, lowest cost; does not require pedigree maintenance; allows high selection intensity and short generation interval.</li><li><b>Limitations:</b> Highly inaccurate for low-heritability traits (<code>h&sup2; &lt; 0.15</code>); completely inapplicable for <b>sex-limited traits</b> in the non-expressing sex (e.g., selecting bulls for milk yield or roosters for egg production); useless for carcass traits requiring slaughter.</li><li><b>Trait Suitability:</b> Growth rate, yearling body weight in sheep/swine/beef cattle, fleece weight, and backfat thickness measured by ultrasound.</li></ul><br><b>B. Pedigree Selection:</b><ul><li><b>Principle:</b> Selection based on the phenotypic performance of ancestors (parents, grandparents).</li><li><b>Accuracy:</b> Based on single parent: <code>r<sub>AI</sub> = &frac12; h</code>; based on mid-parent: <code>r<sub>AI</sub> = h &times; &radic;[1 / (2 - h&sup2;)]</code> (Maximum theoretical accuracy from parents alone cannot exceed <code>1/&radic;2 = 0.71</code> even if <code>h&sup2; = 1.0</code>).</li><li><b>Advantages:</b> Allows selection at an extremely young age (at birth or calfhood), minimizing generation interval; useful for sex-limited traits.</li><li><b>Limitations:</b> Lower accuracy than individual selection for high-h² traits; cannot evaluate Mendelian sampling variance (variation among full sibs with identical parents). Over-reliance leads to inbreeding.</li><li><b>Trait Suitability:</b> Preliminary screening of young dairy bulls and replacement heifers prior to maturity.</li></ul><br><b>C. Collateral / Sib Selection (Half-Sibs & Full-Sibs):</b><ul><li><b>Principle:</b> Selection based on the performance of collateral relatives of the same generation (brothers, sisters, half-sibs). Categorized into <b>Full-sib selection</b> (information from full-brothers/sisters) and <b>Half-sib selection</b>.</li><li><b>Accuracy for <code>n</code> half-sibs:</b> <code>r<sub>AI</sub> = &frac14; n h&sup2; / &radic;[ n &times; (1 + (n - 1) &times; &frac14; h&sup2;) ]</code>. As <code>n &rarr; &infin;</code>, maximum accuracy reaches <code>0.50</code>.</li><li><b>Advantages:</b> Essential for <b>carcass traits</b> (dressing percentage, meat tenderness, intramuscular marbling) where candidate breeding animals cannot be slaughtered themselves; valuable for sex-limited traits.</li><li><b>Limitations:</b> Half-sib accuracy capped at 0.50; full-sibs share common maternal environment (<code>c&sup2;</code>), which can bias genetic estimates.</li><li><b>Trait Suitability:</b> Carcass quality in pigs, broilers, and feedlot cattle.</li></ul><br><b>D. Progeny Testing:</b><ul><li><b>Principle:</b> Selection of breeding parents (particularly sires) based on the average phenotypic performance of a representative, randomly distributed sample of their daughters/offspring.</li><li><b>Accuracy for <code>n</code> progeny:</b> <code>r<sub>AI</sub> = &radic;[ n / {n + (4 - h&sup2;) / h&sup2;} ]</code>.<br>As progeny number <code>n &rarr; &infin;</code>, <b>accuracy approaches 1.00 (100% certainty)</b> regardless of heritability! With 50 daughters, accuracy exceeds <code>0.85</code> even for traits with <code>h&sup2; = 0.20</code>.</li><li><b>Advantages:</b> Highest possible accuracy; the definitive gold standard for sex-limited traits (milk yield in dairy bulls) and low-heritability fitness traits.</li><li><b>Limitations:</b> <b>Severely prolongs generation interval (L)</b>: in dairy bulls, testing requires ~5 to 6 years (conception, gestation, calf rearing, daughter pregnancy, 305-day lactation), which drastically reduces annual genetic gain (<code>&Delta;G/year = R / L</code>); very expensive and requires extensive field artificial insemination recording.</li><li><b>Trait Suitability:</b> National dairy sire evaluation schemes (e.g., Murrah buffalo and HF/Jersey crossbred bulls in India).</li></ul>",
      "keyPoints": [
        "Introduction: Selection defined; accuracy r_AI measures correlation between estimated and true breeding value.",
        "Individual Selection: r_AI = h; simple and short generation interval; fails for sex-limited and carcass traits.",
        "Pedigree Selection: r_AI <= 0.71; enables early calfhood screening; ignores Mendelian sampling.",
        "Sib Selection: Indispensable for carcass quality and meat traits requiring slaughter.",
        "Progeny Testing: r_AI approaches 1.00 as n -> inf; ultimate accuracy for sex-limited traits; drawback is prolonged generation interval (5-6 years) and high cost.",
        "Comprehensive comparative evaluation table."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Comparison of Bases of Selection in Farm Animals",
        "headers": [
          "Selection Base",
          "Information Source",
          "Accuracy Formula (r_AI)",
          "Max Accuracy",
          "Generation Interval (L)",
          "Best Suited Traits"
        ],
        "rows": [
          [
            "Individual (Mass)",
            "Individual's own phenotype",
            "r_AI = √h² = h",
            "1.00 (if h²=1)",
            "Short (evaluated at maturity)",
            "High h² traits expressed in both sexes (body weight, fleece weight, backfat)"
          ],
          [
            "Pedigree",
            "Ancestors (sire, dam, grandparents)",
            "r_AI = 0.5 * h (one parent)",
            "0.71 (mid-parent)",
            "Very Short (evaluated at birth/weaning)",
            "Early screening of young dairy bulls & heifers prior to production"
          ],
          [
            "Sib Selection",
            "Collateral relatives (full-sibs or half-sibs)",
            "r_AI = (1/4 n h²) / √[n (1 + (n-1) 1/4 h²)]",
            "0.50 (half-sibs) / 0.71 (full-sibs)",
            "Intermediate (same generation)",
            "Carcass traits requiring slaughter (dressing %, meat quality) in swine/poultry"
          ],
          [
            "Progeny Testing",
            "Daughters / Offspring performance",
            "r_AI = √[n / (n + (4-h²)/h²)]",
            "Approaches 1.00 as n -> ∞",
            "Very Long (5-6 yrs in dairy cattle)",
            "Sex-limited traits (milk yield) and low h² fertility/fitness traits in dairy sires"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2017",
        "IVRI 2019",
        "TANUVAS 2020",
        "GADVASU 2021",
        "KVASU 2022",
        "LUVAS 2023"
      ]
    },
    {
      "id": "u3-q22",
      "type": "long",
      "marks": 12,
      "question": "Define and classify Systems of Mating in livestock. Describe Inbreeding, detailing Wright's Path Coefficient method for calculating Inbreeding Coefficient (FX) and Coefficient of Relationship (RXY). Describe Outbreeding systems: Outcrossing, Crossbreeding (Two-way, Three-way, Rotational/Criss-crossing, and Terminal crossing), and Grading Up. Construct a table showing the recovery of superior germplasm across five generations of Grading Up.",
      "topicId": "u3-t10",
      "answer": "<b>1. Definition and Classification of Systems of Mating:</b><br>Mating systems refer to the planned rules according to which selected males and females are paired for reproduction. Unlike selection (which changes gene frequencies), <b>mating systems alter genotypic frequencies</b> by reorganizing genes into homozygous or heterozygous combinations.<br><br><b>Classification of Mating Systems:</b><ul><li><b>1. Random Mating (Panmixia):</b> Each male has an equal probability of mating with any female in the population (maintains Hardy-Weinberg equilibrium).</li><li><b>2. Assortative Mating:</b> Non-random pairing based on phenotypic resemblance:<ul><li><i>Positive Assortative:</i> Mating 'like to like' (best to best) &rarr; increases phenotypic variance and extremes.</li><li><i>Negative Assortative (Disassortative):</i> Mating 'unlike to unlike' (e.g., large bull to small cow) &rarr; reduces variance, promotes uniformity.</li></ul></li><li><b>3. Inbreeding:</b> Mating of individuals more closely related to each other than the average relationship of the population (increases homozygosity).</li><li><b>4. Outbreeding:</b> Mating of individuals less closely related than the population average (increases heterozygosity and induces heterosis).</li></ul><br><b>2. Inbreeding & Wright's Path Coefficient Method:</b><br><b>Sewall Wright's Formula for Inbreeding Coefficient (F<sub>X</sub>):</b><br><b><code>F<sub>X</sub> = &sum; [ (&frac12;)<sup>n1 + n2 + 1</sup> &times; (1 + F<sub>A</sub>) ]</code></b><br>where: <code>n1</code> = number of generations from Sire (S) back to common ancestor (A);<br><code>n2</code> = number of generations from Dam (D) back to common ancestor (A);<br><code>F<sub>A</sub></code> = inbreeding coefficient of the common ancestor <i>A</i>.<br><br><b>Coefficient of Relationship between two individuals X and Y (R<sub>XY</sub>):</b><br><b><code>R<sub>XY</sub> = [ &sum; (&frac12;)<sup>n1 + n2</sup> &times; (1 + F<sub>A</sub>) ] / &radic;[ (1 + F<sub>X</sub>)(1 + F<sub>Y</sub>) ]</code></b><br><br><i>Path Analysis Protocol:</i><ol><li>Convert arrow pedigree into a clean path diagram showing common ancestors connecting sire and dam.</li><li>Identify all independent common ancestors.</li><li>Trace all non-repeating paths from sire up to common ancestor and down to dam: <code>S &larr; ... &larr; A &rarr; ... &rarr; D</code>.</li><li>Sum <code>(&frac12;)<sup>n</sup></code> across all independent paths.</li></ol><br><b>3. Outbreeding Systems in Domestic Livestock:</b><ul><li><b>A. Outcrossing:</b> Mating of unrelated purebred animals within the same registered breed (no common ancestor in first 4&ndash;6 generations). Main tool to introduce fresh vigor and avoid inbreeding in purebred dairy herds.</li><li><b>B. Crossbreeding:</b> Mating of animals of two or more distinct established breeds. Exploits breed complementarity and heterosis:</li><ul><li><i>Two-Way Cross (Single Cross):</i> Breed A &times; Breed B &rarr; F1 crossbred (e.g., Karan Swiss: Sahiwal &times; Brown Swiss; Karan Fries: Tharparkar &times; Holstein Friesian).</li><li><i>Three-Way Cross:</i> Crossbred F1 females (A &times; B) are mated to a third distinct purebred terminal sire breed (C) &rarr; Progeny [50% C, 25% A, 25% B]. Combines maternal heterosis of F1 dams with individual heterosis in market stock (standard in commercial pigs and market lambs).</li><li><i>Criss-Crossing (Two-Breed Rotational Cross):</i> F1 crossbred cows are mated to purebred Sire of Breed A. Their female progeny are mated to purebred Sire of Breed B, alternating sire breeds in each generation. Maintains ~67% of maximum possible heterosis continuously without buying replacement females.</li><li><i>Terminal Crossing:</i> All crossbred male and female offspring are sold for slaughter/meat; zero females are retained as breeding replacements (e.g., commercial broilers and terminal beef crossbreeding).</li></ul><li><b>C. Grading Up:</b> Mating purebred superior sires of a recognized breed to nondescript indigenous scrub females and their female descendants generation after generation. It is the fastest, cheapest method to transform a low-producing nondescript population into a high-grade productive herd.</li></ul>",
      "keyPoints": [
        "Classification: Panmixia, assortative mating, inbreeding (increases homozygosity), and outbreeding (increases heterozygosity).",
        "Wright's formula for inbreeding (F_X) and relationship (R_XY) with path analysis rules.",
        "Outbreeding types: Outcrossing, Crossbreeding (Two-way, Three-way, Rotational/Criss-crossing, Terminal crossing), and Grading Up.",
        "Table showing progressive recovery of superior germplasm across 5 generations of Grading Up (50%, 75%, 87.5%, 93.75%, 96.88%)."
      ],
      "diagram": "",
      "table": {
        "title": "Grading Up: Progressive Recovery of Superior Purebred Inheritance Across Generations",
        "headers": [
          "Generation",
          "Mating Type (Sire x Dam)",
          "Superior / Improved Breed Inheritance",
          "Nondescript / Scrub Inheritance"
        ],
        "rows": [
          [
            "Generation 1 (G1 / F1)",
            "Purebred Sire (100%) x Nondescript Dam (0%)",
            "1/2 = 50.00%",
            "1/2 = 50.00%"
          ],
          [
            "Generation 2 (G2)",
            "Purebred Sire (100%) x G1 Female (50%)",
            "3/4 = 75.00%",
            "1/4 = 25.00%"
          ],
          [
            "Generation 3 (G3)",
            "Purebred Sire (100%) x G2 Female (75%)",
            "7/8 = 87.50%",
            "1/8 = 12.50%"
          ],
          [
            "Generation 4 (G4)",
            "Purebred Sire (100%) x G3 Female (87.5%)",
            "15/16 = 93.75%",
            "1/16 = 6.25%"
          ],
          [
            "Generation 5 (G5)",
            "Purebred Sire (100%) x G4 Female (93.75%)",
            "31/32 = 96.88%",
            "1/32 = 3.12%"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2018",
        "TANUVAS 2019",
        "IVRI 2020",
        "GADVASU 2021",
        "KVASU 2022",
        "MAFSU 2023"
      ]
    },
    {
      "id": "u3-q23",
      "type": "long",
      "marks": 12,
      "question": "Discuss the National Breeding Policies and Strategies for the Genetic Improvement of Dairy Cattle and Buffaloes in India. Detail: (a) Selective breeding in indigenous cattle breeds; (b) Crossbreeding policy with exotic germplasm, including the rationale for maintaining 50% to 62.5% exotic inheritance; (c) Problems of F2 breakdown and inter-se mating; (d) Grading up of nondescript buffaloes with Murrah / Nili-Ravi; and (e) Modern Progeny Testing and Field Progeny Testing (PT) schemes under the National Dairy Plan.",
      "topicId": "u3-t17",
      "answer": "<b>1. Overview of Indian Dairy Production Environment:</b><br>India is the world's largest milk producer (>230 million tonnes), characterized by a tropical climate with high heat/humidity, prevalence of tropical vector-borne diseases (tick-borne haemoparasites like Theileriosis, Babesiosis), low-to-medium quality crop residue feeding, and smallholder production systems. Hence, the National Breeding Policy balances high milk production with thermal tolerance, disease resistance, and reproductive longevity.<br><br><b>2. Key Strategic Pillars of Cattle & Buffalo Improvement:</b><br><br><b>A. Selective Breeding in Defined Indigenous Cattle Breeds:</b><ul><li>Recognized milch breeds (<b>Gir, Sahiwal, Red Sindhi, Tharparkar</b>) and dual-purpose breeds (<b>Kankrej, Hariana, Ongole</b>) possess superior thermotolerance (sweat gland density, slick coat), resistance to tropical haemoprotozoans, and high butterfat (A2 beta-casein allele).</li><li>Policy mandates <b>pure selective breeding</b> in their native breeding tracts: identifying elite bull mothers, producing pedigree bulls, and conducting progeny testing/genomic evaluation without introducing exotic genes.</li></ul><br><b>B. Crossbreeding Policy with Exotic Germplasm & The 50&ndash;62.5% Optimum Level:</b><ul><li>Implemented for nondescript (scrub) zebu cattle in areas with adequate feed and veterinary support using <b>Holstein Friesian (HF)</b> in temperate/irrigated belts and <b>Jersey</b> in hot-humid/hilly coastal regions.</li><li><b>Why Maintain 50% to 62.5% Exotic Inheritance?</b><ul><li><i>At 50% Exotic Level (F1 Crossbred):</i> Perfect balance: 50% exotic milk production genetics combined with 50% zebu tropical adaptability and <b>100% individual heterosis</b>. Yield increases 3 to 4 fold (from 800 kg to 2800&ndash;3200 kg per lactation), age at first calving drops from 45 months to 28&ndash;30 months.</li><li><i>Beyond 62.5% Exotic Inheritance:</i> Severe deterioration occurs: tropical heat distress (rectal temperature rises, panting), high susceptibility to theileriosis, mastitis, repeat breeding, and high mortality under Indian climatic conditions.</li><li><i>Below 50% Exotic Level:</i> Milk production drops substantially, failing to satisfy economic returns.</li></ul></li></ul><br><b>C. Problems of F2 Breakdown and Inter-Se Mating Challenges:</b><ul><li>When F1 crossbreds are inter-se mated (<code>F1 &times; F1 &rarr; F2</code>), crossbred performance drops by <b>15&ndash;25%</b>.</li><li><b>Genetic Causes of F2 Breakdown:</b> (i) <b>Loss of 50% heterosis</b> due to segregation; (ii) Breakup of favorable epistatic gene complexes (linkage disequilibrium breakdown) through meiotic recombination; (iii) Wide phenotypic segregation producing huge variability in coat type, body size, and productivity.</li><li><b>Management of Inter-se Mating:</b> Handled by rigorous progeny testing of crossbred bulls and multi-breed composite synthesis (e.g., Frieswal = 62.5% HF + 37.5% Sahiwal, developed by ICAR-CIRC and Military Farms).</li></ul><br><b>D. Grading Up of Nondescript Buffaloes with Murrah / Nili-Ravi:</b><ul><li>Buffaloes contribute >50% of total national milk production and the majority of high-fat milk.</li><li>Nondescript riverine buffaloes across central and peninsular India are systematically <b>graded up using frozen semen of pedigreed Murrah or Nili-Ravi bulls</b>.</li><li>By G4/G5 generations (93.75&ndash;96.88% Murrah inheritance), buffaloes produce >2000 kg milk per lactation with 7&ndash;8% fat, transforming rural dairy economies.</li></ul><br><b>E. Progeny Testing (PT) and Pedigree Selection under National Dairy Plan (NDP):</b><ul><li>Under Rashtriya Gokul Mission and NDP-I (implemented by NDDB), large-scale <b>Field Progeny Testing (FPT)</b> programs are operational for Murrah, Mehsana, Gir, Sahiwal, and CB Frieswal.</li><li>Young bulls (minimum 25&ndash;50 bulls/batch) are test-mated to thousands of registered farmer cows via AI; first-lactation milk records of 80&ndash;100 daughters per bull are recorded under field conditions using Animal Information Network (INAPH / Pashu Aadhaar). Top 10% proven bulls are selected for semen production.</li></ul>",
      "keyPoints": [
        "National breeding policy context: Balancing tropical resilience (A2 milk, heat tolerance) with productivity.",
        "Selective breeding for indigenous milch breeds (Gir, Sahiwal, Red Sindhi, Tharparkar).",
        "Crossbreeding with HF and Jersey: Scientific justification for maintaining 50% to 62.5% exotic inheritance limit.",
        "F2 breakdown analysis: Loss of 50% heterosis, recombination loss of epistatic complexes, increased segregation variance; Frieswal composite solution.",
        "Grading up nondescript buffaloes with Murrah/Nili-Ravi.",
        "Field Progeny Testing (FPT) and Pedigree Selection under NDDB/RGM using INAPH ear-tag tracking."
      ],
      "diagram": "",
      "table": null,
      "pyq": [
        "VCI Annual 2017",
        "IVRI 2019",
        "TANUVAS 2020",
        "GADVASU 2021",
        "KVASU 2022",
        "LUVAS 2023"
      ]
    },
    {
      "id": "u3-q24",
      "type": "long",
      "marks": 12,
      "question": "Describe the Commercial Poultry Breeding Structure for the production of Hybrid Commercial Broilers and Egg Layers. Detail: (a) The 4-Way Cross Breeding Hierarchy (GGP, GP, Parent Stock, Commercial Hybrid); (b) Trait selection criteria for Male (Sire) vs Female (Dam) lines; (c) Role of sex-linked genes (rapid/slow feathering, silver/gold) in Day-Old Chick Auto-Sexing; and (d) Development of Rural / Backyard Poultry varieties in India (Vanaraja, Gramapriya, Giriraja).",
      "topicId": "u3-t21",
      "answer": "<b>1. Commercial Poultry Breeding Hierarchy (The 4-Way Cross Pyramid):</b><br>Modern commercial poultry production is the most sophisticated and mathematically optimized sector in animal agriculture. Commercial birds are never purebreds; they are <b>four-line terminal crossbred hybrids</b> developed through a strict four-tier pyramid:<br><ul><li><b>Tier 1: Pedigree / Great-Grandparent (GGP) Lines:</b> Maintained as closed pure lines (Line A, B, C, D) under intense biosecurity. Selected via Reciprocal Recurrent Selection (RRS), family selection, and individual selection with very high selection intensity (top 1&ndash;5%).</li><li><b>Tier 2: Grandparent (GP) Stock:</b> Crosses made within sire side (<code>A &male; &times; B &female; &rarr; AB</code>) and within dam side (<code>C &male; &times; D &female; &rarr; CD</code>).</li><li><b>Tier 3: Parent Stock (PS):</b> Crossbred Parent females (<code>CD</code>) and Parent males (<code>AB</code>) distributed to commercial franchised hatcheries. Exploit maternal heterosis (CD dams produce maximum fertile hatching eggs).</li><li><b>Tier 4: Commercial End-Products:</b> Mating of Parent male &times; Parent female: <code>AB &male; &times; CD &female; &rarr; ABCD Commercial Hybrid</code> (Broiler or Layer). Expresses maximum four-way individual and maternal heterosis (100% uniformity and vigor).</li></ul><br><b>2. Trait Selection Criteria: Sire Line vs Dam Line:</b><ul><li><b>Male / Sire Line (Lines A & B):</b> Heavy emphasis on rapid juvenile growth rate, breast meat yield, Feed Conversion Ratio (FCR), livability, and skeletal conformation. In layers: early sexual maturity and egg size.</li><li><b>Female / Dam Line (Lines C & D):</b> Heavy emphasis on female reproductive fitness: total egg production, peak egg production persistency, hatchability, shell quality, fertility, and maternal feed efficiency.</li></ul><br><b>3. Day-Old Chick Auto-Sexing Using Sex-Linked Genes:</b><br>In commercial hatcheries, determining sex at day-old is critical (cockerels in layers are discarded; broilers can be reared sex-separate). Vent sexing is slow and expensive. <b>Sex-linked auto-sexing</b> enables instant, 100% accurate visual sexing by non-technical labor.<br><br><b>A. Rapid vs Slow Feathering (K / k locus on Z chromosome):</b><br><ul><li>Slow feathering allele (<code>K</code>) is dominant over rapid feathering (<code>k</code>). In birds, males are homogametic (<code>ZZ</code>) and females heterogametic (<code>ZW</code>).</li><li><b>Mating Design:</b> Rapid feathering Male (<code>k k</code>) &times; Slow feathering Female (<code>K W</code>):</li><li><b>Female Chicks (Pullets):</b> Inherit Z from sire &rarr; <b><code>k W</code> (Rapid feathering)</b>: Primary wing covert feathers are distinctly longer than under-coverts at hatch.</li><li><b>Male Chicks (Cockerels):</b> Inherit Z from dam &rarr; <b><code>K k</code> (Slow feathering)</b>: Primary wing feathers are the same length or shorter than covert feathers.</li></ul><br><b>B. Silver vs Gold Plumage (S / s locus on Z chromosome):</b><br><ul><li>Silver (<code>S</code>) is dominant over Gold/Red (<code>s</code>).</li><li><b>Mating Design:</b> Gold Male (<code>s s</code>, e.g., Rhode Island Red) &times; Silver Female (<code>S W</code>, e.g., White Wyandotte):</li><li><b>Female Pullets:</b> <b><code>s W</code> (Gold / Brown down)</b>.</li><li><b>Male Cockerels:</b> <b><code>S s</code> (Silver / Creamy White down)</b>. Instant sorting by down color.</li></ul><br><b>4. Rural & Backyard Poultry Development in India:</b><br>To uplift rural tribal livelihoods and provide nutritional security, ICAR institutions developed hardy, multi-colored dual-purpose crossbred chicken varieties that thrive under scavenged backyard scavenging without commercial feed:<ul><li><b>Vanaraja (ICAR-DPR, Hyderabad):</b> Multi-colored dual-purpose cross bred for free-range rural farming. Body weight: 1.5&ndash;1.8 kg at 12 weeks; produces 100&ndash;110 large brown eggs/year under scavenging. High immune competence against Ranikhet disease.</li><li><b>Gramapriya (ICAR-DPR, Hyderabad):</b> Layer-type rural crossbred producing 200&ndash;220 tinted brown eggs/year with low feed input; excellent camouflage plumage protecting from predatory birds.</li><li><b>Giriraja (KVAFSU, Bengaluru):</b> Multi-colored broiler-cum-egg bird with rapid growth (2.0 kg at 10 weeks) and 130&ndash;150 eggs/year.</li><li><b>Srinidhi, Cari-Nirbheek, Pratapdhan:</b> Adapted backyard crosses incorporating native germplasm (Aseel, Kadaknath) for broodiness, escape agility, and high market preference for pigmented meat and brown eggs.</li></ul>",
      "keyPoints": [
        "4-Way Cross breeding structure (GGP -> GP -> PS -> Commercial 4-way ABCD hybrid).",
        "Sire line selection (growth, breast yield, FCR) vs Dam line selection (egg numbers, fertility, hatchability).",
        "Auto-sexing genetics: Female heterogamety (ZW) exploited via Z-linked slow feathering (K/k) and Silver/Gold (S/s) crosses.",
        "Indian backyard poultry breeds: Vanaraja (DPR Hyderabad), Gramapriya, Giriraja (KVAFSU), Pratapdhan for rural livelihood."
      ],
      "diagram": "",
      "table": {
        "title": "Selection Trait Priorities in Commercial Layer vs Broiler Breeding Programs",
        "headers": [
          "Breeding Segment",
          "Primary Selection Traits",
          "Target Commercial Benchmark",
          "Genetic Architecture"
        ],
        "rows": [
          [
            "Commercial Hybrid Layers",
            "Annual egg number (hen-housed), egg weight (58-62g), shell breaking strength, early sexual maturity (18-19 wks), feed efficiency per dozen eggs",
            "320 - 340 eggs per year; FCR 1.9 - 2.1 kg feed/kg egg mass",
            "Moderate to high h² for egg size; low h² for egg numbers (exploits heterosis)"
          ],
          [
            "Commercial Hybrid Broilers",
            "Body weight at 35-42 days, feed conversion ratio (FCR), breast meat yield, livability, ascites/skeletal defect resistance",
            "2.2 - 2.5 kg at 35 days; FCR 1.45 - 1.55; breast yield >22%",
            "Moderate to high h² (0.30 - 0.45) for growth rate and body composition"
          ],
          [
            "Layer Dam Line (Lines C & D)",
            "High peak egg production, persistency (>90% production across 40 weeks), low adult body weight (reduces maintenance feed cost)",
            "92% peak hatchability; low maintenance cost",
            "Negative genetic correlation between egg number and body weight handled via index"
          ],
          [
            "Broiler Dam Line (Lines C & D)",
            "Hatching egg production, fertility, hatchability under skip-a-day feed restriction",
            "175 - 185 hatching eggs per hen housed",
            "Requires strict feed restriction during rearing to prevent obesity and ovarian disorders"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2018",
        "TANUVAS 2019",
        "IVRI 2020",
        "GADVASU 2021",
        "KVASU 2022",
        "LUVAS 2023"
      ]
    },
    {
      "id": "u3-q25",
      "type": "long",
      "marks": 12,
      "question": "Describe the Modern Reproductive and Biotechnological Tools in Animal Breeding: Artificial Insemination (AI), Sex-Sorted Semen, Ovum Pick-Up and In Vitro Fertilization (OPU-IVF), and Genomic Selection. Compare Traditional Progeny Testing with Genomic Selection (GBLUP/ssGBLUP), explaining how Genomic Selection dramatically shortens the generation interval. Outline its implementation in Indian dairy breeds.",
      "topicId": "u3-t26",
      "answer": "<b>1. Advanced Reproductive Technologies in Animal Breeding:</b><ul><li><b>A. Artificial Insemination (AI) with Frozen Semen:</b> The foundational multiplier biotechnology. A single elite bull produces 40,000&ndash;60,000 semen doses annually (diluted in tris-egg yolk-glycerol extender and frozen at -196&deg;C in liquid nitrogen), enabling the widespread dissemination of proven genetic merit across millions of cows while preventing venereal disease transmission.</li><li><b>B. Sex-Sorted Semen Technology:</b> Based on flow-cytometric cell sorting (Beltsville sperm sorting technology). Bovine X-chromosome bearing spermatozoa contain <b>3.8% more DNA</b> than Y-spermatozoa. Sperm are stained with fluorochrome Hoechst 33342, excited by UV laser, and sorted electrostatically at 90% accuracy into X-bearing or Y-bearing fractions. Insemination of heifers with X-sorted semen produces >90% female calves, revolutionizing heifer replacement and eliminating unwanted stray male calves.</li><li><b>C. Ovum Pick-Up and In Vitro Fertilization (OPU-IVF):</b> Transvaginal ultrasound-guided aspiration of immature cumulus-oocyte complexes (COCs) from live donor ovaries, followed by in vitro maturation (IVM), in vitro fertilization (IVF) with sexed semen, and in vitro culture (IVC) to blastocyst stage (Day 7). Overcomes the limitations of MOET: can be performed twice weekly on pregnant cows and prepubertal heifers, yielding 50&ndash;100 embryos per cow annually without hormone depletion.</li></ul><br><b>2. Genomic Selection (Theo Meuwissen, Hayes & Goddard, 2001):</b><br>A paradigm shift in animal breeding where <b>Genomic Estimated Breeding Values (GEBVs)</b> are calculated directly from genome-wide dense Single Nucleotide Polymorphism (SNP) markers spanning the entire livestock genome (e.g., Bovine 50K BeadChip).<br><br><b>Operational Methodology:</b><ol><li><b>Reference Population:</b> A large cohort of thousands of historic sires and cows with both high-density SNP genotypes and verified phenotypic progeny records. Marker effects across all 50,000 SNPs are estimated simultaneously using Genomic BLUP (GBLUP) or Bayesian regression methods.</li><li><b>Candidate Population (Calves):</b> Newborn calves are genotyped at birth using hair follicle or blood DNA.</li><li><b>GEBV Prediction:</b> Calf's GEBV is calculated by summing the estimated allelic effects of all its inherited SNP alleles: <code>GEBV = &sum; (X<sub>i</sub> &times; &beta;^<sub>i</sub>)</code>.</li></ol><br><b>3. Traditional Progeny Testing vs. Genomic Selection:</b><br>The fundamental formula governing annual rate of genetic progress is Rendel and Robertson's equation:<br><b><code>&Delta;G / year = (i &times; r<sub>AI</sub> &times; &sigma;<sub>A</sub>) / L</code></b><br>Genomic selection revolutionized this dynamic by drastically reducing the denominator <b>Generation Interval (L)</b> while maintaining high accuracy (<code>r<sub>AI</sub> &approx; 0.70&ndash;0.80</code>):<ul><li>In traditional progeny testing, a dairy bull's breeding value can only be established after daughters complete their first 305-day lactation: <b>L = 5.5 to 6.0 years</b>.</li><li>In genomic selection, GEBV is predicted with 75% accuracy <b>on the day the calf is born (L = 1.5 to 2.0 years)</b>. Semen collection begins at 12&ndash;14 months.</li><li><b>Result:</b> Annual genetic progress (<code>&Delta;G/year</code>) <b>doubles (100% to 150% increase)</b> compared to traditional progeny testing, with massive savings in rearing costs for unselected candidate bulls.</li></ul><br><b>4. Genomic Selection Implementation in Indian Dairy Livestock:</b><ul><li><b>National Dairy Development Board (NDDB) & Rashtriya Gokul Mission (RGM):</b> Developed custom indigenous genomic chips (e.g., <b>INDUSCHIP</b>, a 55K SNP custom BeadChip optimized for zebu cattle, and <b>BUFFCHIP</b> optimized for water buffaloes).</li><li><b>Single-Step GBLUP (ssGBLUP):</b> Integrates pedigree, genotypes, and phenotypes simultaneously using the <code>H-matrix</code> (combining relationship matrix <i>A</i> with genomic relationship matrix <i>G</i>), enabling accurate evaluation of non-genotyped smallholder cows alongside genotyped AI breeding bulls.</li><li>Used to screen and select young indigenous Gir, Sahiwal, Kankrej, and Murrah bulls at 6 months of age for national semen stations.</li></ul>",
      "keyPoints": [
        "AI and Cryopreservation (-196°C) as foundation multiplier biotechnology.",
        "Sex-sorted semen: 3.8% DNA difference, flow-cytometry sorting (90% female calf accuracy).",
        "OPU-IVF: Twice-weekly ovum pickup from live donors, 50-100 embryos/yr.",
        "Genomic selection principle (Meuwissen et al. 2001): Reference population, SNP BeadChips, GEBV prediction.",
        "Mathematical comparison: Rendel-Robertson equation (ΔG/yr = i * r * σ_A / L); L reduced from 5.5 yrs to 1.5 yrs, doubling genetic gain.",
        "Indian implementation: INDUSCHIP (zebu) and BUFFCHIP (buffalo) under NDDB/RGM with single-step GBLUP (H-matrix)."
      ],
      "diagram": "",
      "table": {
        "title": "Comprehensive Comparison Between Traditional Progeny Testing and Genomic Selection",
        "headers": [
          "Feature",
          "Traditional Progeny Testing (PT)",
          "Genomic Selection (GS / ssGBLUP)"
        ],
        "rows": [
          [
            "Age at Final Genetic Evaluation",
            "5.5 - 6.0 years (requires waiting for daughter lactation)",
            "At birth (1 - 2 weeks of age from blood/hair DNA)"
          ],
          [
            "Generation Interval (L)",
            "Sire-to-son interval is 5.5 - 6.5 years",
            "Sire-to-son interval reduced to 1.5 - 2.0 years (70% reduction)"
          ],
          [
            "Accuracy of Breeding Value (r_AI)",
            "0.85 - 0.90 (with 50 - 80 recorded daughters)",
            "0.70 - 0.80 at birth (based on dense SNP markers)"
          ],
          [
            "Annual Genetic Gain (ΔG/year)",
            "Standard baseline (1.0x)",
            "Doubled (2.0x to 2.5x standard rate due to dramatic L reduction)"
          ],
          [
            "Bull Maintenance Cost",
            "Enormous; hundreds of unproven bulls housed for 5+ years awaiting daughter records",
            "Very low; only top genomically ranked young calves are retained"
          ],
          [
            "Evaluation of Traits Hard to Measure",
            "Difficult and costly for health, fertility, feed efficiency, and longevity",
            "Highly effective; reference population records allow GEBV prediction for all recorded traits"
          ],
          [
            "Indian Tool / Implementation",
            "Field Progeny Testing (FPT) under NDP",
            "INDUSCHIP (Cattle) & BUFFCHIP (Buffalo) via NDDB/INAPH ssGBLUP"
          ]
        ]
      },
      "pyq": [
        "VCI Annual 2019",
        "TANUVAS 2020",
        "IVRI 2021",
        "GADVASU 2022",
        "KVASU 2023"
      ]
    }
  ]
};
