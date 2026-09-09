# tools/unit1_data.py
# Unit 1: Biostatistics and Computer Application
# 180 questions: 90 MCQs, 45 True/False, 45 Fill in the Blanks
# Exactly 18 MCQs, 9 T/F, 9 FIB per sub-section across u1-s1 to u1-s5

unit1_mcq = [
    # ============================================================
    # u1-s1: Data Classification, Central Tendency & Dispersion (18 MCQs)
    # ============================================================
    {
        "q": "Who is recognized as the pioneer of correlation and regression analysis and coined the term 'Biometry'?",
        "o": ["Sir Francis Galton", "Karl Pearson", "Sir Ronald A. Fisher", "Gregor Mendel"],
        "a": 0,
        "e": "Sir Francis Galton coined the term 'Biometry' and pioneered the mathematical concepts of correlation and regression.",
        "topicId": "u1-t01",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "Which of the following characteristics is an inherent feature of biological data compared to physical data?",
        "o": ["Deterministic replication", "Absence of variation", "Inherent biological variation", "Zero sampling error"],
        "a": 2,
        "e": "Living organisms possess inherent biological variation due to genetic diversity and micro-environmental influences.",
        "topicId": "u1-t01",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "Classification of biological data according to geographical location or region is known as:",
        "o": ["Chronological classification", "Spatial / Geographical classification", "Qualitative classification", "Quantitative classification"],
        "a": 1,
        "e": "Spatial or geographical classification arranges biological data according to geographical areas, zones, or administrative regions.",
        "topicId": "u1-t02",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "In a statistical frequency distribution table, the upper boundary of each class is excluded from that class in:",
        "o": ["Exclusive series", "Inclusive series", "Cumulative series", "Discrete series"],
        "a": 0,
        "e": "In an exclusive class interval (e.g., 10-20, 20-30), the upper limit is excluded and counted in the next succeeding class.",
        "topicId": "u1-t02",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "A numerical descriptive measure computed from an entire biological population is termed a:",
        "o": ["Statistic", "Parameter", "Variable", "Estimate"],
        "a": 1,
        "e": "A parameter is a fixed numerical characteristic of a population (e.g., population mean μ), whereas a statistic is calculated from a sample.",
        "topicId": "u1-t03",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "Which graphic representation is specifically used to locate the median of a continuous frequency distribution?",
        "o": ["Histogram", "Frequency polygon", "Ogive curve (cumulative frequency curve)", "Pie diagram"],
        "a": 2,
        "e": "The median can be determined graphically from the intersection point of the 'less than' and 'more than' ogives (or at N/2 on cumulative frequency axis).",
        "topicId": "u1-t04",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "A bar chart where adjacent vertical rectangles touch each other with area proportional to frequency is called a:",
        "o": ["Histogram", "Bar diagram", "Line graph", "Cartogram"],
        "a": 0,
        "e": "A histogram consists of contiguous rectangles where the area of each bar is directly proportional to the frequency of that class.",
        "topicId": "u1-t04",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "What is the algebraic sum of deviations of a set of observations from their arithmetic mean?",
        "o": ["Always 1", "Always 0", "Equal to standard deviation", "Equal to variance"],
        "a": 1,
        "e": "By mathematical definition, Σ(X - X_bar) = 0. The sum of deviations of values from their arithmetic mean is always zero.",
        "topicId": "u1-t05",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "Which measure of central tendency is the most suitable average for qualitative data or categorical breed preferences?",
        "o": ["Arithmetic mean", "Geometric mean", "Mode", "Harmonic mean"],
        "a": 2,
        "e": "The mode represents the most frequently occurring observation and is the only measure of central tendency applicable to nominal/categorical data.",
        "topicId": "u1-t05",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "In a moderately asymmetrical distribution, the empirical relationship between mean, median, and mode is:",
        "o": ["Mode = 3 Median - 2 Mean", "Mean = 3 Median - 2 Mode", "Median = 3 Mode - 2 Mean", "Mode = 2 Median - 3 Mean"],
        "a": 0,
        "e": "Karl Pearson's empirical formula states: Mode = 3 Median - 2 Mean (or Mean - Mode = 3(Mean - Median)).",
        "topicId": "u1-t05",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "The measure of dispersion that is defined as half the difference between the third and first quartiles is:",
        "o": ["Mean deviation", "Quartile deviation (Semi-interquartile range)", "Standard deviation", "Variance"],
        "a": 1,
        "e": "Quartile Deviation (QD) = (Q3 - Q1) / 2. It is also known as the semi-interquartile range.",
        "topicId": "u1-t06",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "The positive square root of the arithmetic mean of the squared deviations from the mean is called:",
        "o": ["Standard deviation", "Variance", "Mean deviation", "Range"],
        "a": 0,
        "e": "Standard deviation (SD or σ) is defined as the positive square root of variance: σ = sqrt(Σ(X - μ)² / N).",
        "topicId": "u1-t06",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "If every observation in a lactation dataset is multiplied by a constant factor of 3, the standard deviation will:",
        "o": ["Remain unchanged", "Increase by 3", "Become 3 times the original SD", "Become 9 times the original SD"],
        "a": 2,
        "e": "Standard deviation is affected by change of scale. Multiplying every observation by constant c multiplies the SD by |c| (so 3 * SD). Variance increases 9-fold.",
        "topicId": "u1-t06",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "Which relative measure of dispersion is used to compare variability between two biological groups with different units or means?",
        "o": ["Variance", "Standard error", "Coefficient of Variation (CV)", "Mean deviation"],
        "a": 2,
        "e": "Coefficient of Variation (CV = (SD / Mean) * 100) is a unitless percentage used to compare dispersion across different traits or populations.",
        "topicId": "u1-t07",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "What is the formula for the Standard Error of the sample mean (SE_mean)?",
        "o": ["σ / sqrt(n)", "σ / n", "σ² / n", "n / sqrt(σ)"],
        "a": 0,
        "e": "The standard error of the mean evaluates the precision of a sample mean and is calculated as SE = s / sqrt(n).",
        "topicId": "u1-t07",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "For any frequency distribution, the first central moment (μ₁) is always equal to:",
        "o": ["1", "0", "Mean", "Variance"],
        "a": 1,
        "e": "The first moment about the mean μ₁ = Σ(X - X_bar) / N = 0, because the sum of deviations from the mean is always zero.",
        "topicId": "u1-t08",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "In a positively skewed biological distribution, the relationship among the three averages is:",
        "o": ["Mean > Median > Mode", "Mode > Median > Mean", "Mean = Median = Mode", "Median > Mean > Mode"],
        "a": 0,
        "e": "In a right-skewed (positively skewed) curve, the long tail extends to the right, pulling Mean > Median > Mode.",
        "topicId": "u1-t08",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "For a standard normal distribution, the value of kurtosis coefficient β₂ is equal to:",
        "o": ["0", "1", "3", "-3"],
        "a": 2,
        "e": "A normal mesokurtic distribution has β₂ = 3 (and excess kurtosis γ₂ = β₂ - 3 = 0). Leptokurtic curves have β₂ > 3, platykurtic β₂ < 3.",
        "topicId": "u1-t08",
        "subSection": "u1-s1",
        "diff": 2
    },

    # ============================================================
    # u1-s2: Probability & Distributions (18 MCQs)
    # ============================================================
    {
        "q": "If two events A and B are mutually exclusive, the probability of both occurring together P(A ∩ B) is:",
        "o": ["1", "0", "P(A) * P(B)", "P(A) + P(B)"],
        "a": 1,
        "e": "Mutually exclusive events cannot occur simultaneously, hence their joint probability P(A ∩ B) = 0.",
        "topicId": "u1-t09",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "The probability of drawing a black cow from a herd where 40% are black and 60% are red is:",
        "o": ["0.60", "0.40", "0.24", "1.00"],
        "a": 1,
        "e": "Probability P = favorable cases / total cases = 40 / 100 = 0.40.",
        "topicId": "u1-t09",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "According to the addition theorem of probability, for any two non-mutually exclusive events A and B:",
        "o": ["P(A ∪ B) = P(A) + P(B) - P(A ∩ B)", "P(A ∪ B) = P(A) * P(B)", "P(A ∪ B) = P(A) + P(B)", "P(A ∪ B) = P(A) / P(B)"],
        "a": 0,
        "e": "For general events, P(A or B) = P(A) + P(B) - P(A and B) to avoid double counting the intersection.",
        "topicId": "u1-t09",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "What are the two parameters that define a Binomial distribution?",
        "o": ["μ and σ", "n and p", "λ and e", "n and λ"],
        "a": 1,
        "e": "A Binomial distribution B(n, p) is completely characterized by two parameters: n (number of independent trials) and p (probability of success in each trial).",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "In a Binomial distribution, the mean and variance are given respectively by:",
        "o": ["np and npq", "np and sqrt(npq)", "nq and np", "λ and λ"],
        "a": 0,
        "e": "For a binomial distribution, Mean = np, and Variance = npq (where q = 1 - p). Notice variance < mean.",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "Which discrete probability distribution is known as the 'law of rare events'?",
        "o": ["Binomial distribution", "Poisson distribution", "Normal distribution", "Uniform distribution"],
        "a": 1,
        "e": "The Poisson distribution models rare biological events (e.g., rare genetic mutations, hemophilia cases) where n is very large and p is extremely small.",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "In a Poisson distribution with parameter λ, which property is uniquely true?",
        "o": ["Mean > Variance", "Mean < Variance", "Mean = Variance = λ", "Mean = λ²"],
        "a": 2,
        "e": "A hallmark of the Poisson distribution is that its mean and variance are identical and equal to the parameter λ.",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "The total area under the standard normal distribution curve is equal to:",
        "o": ["0.5", "1.0", "3.0", "100"],
        "a": 1,
        "e": "The total area under any valid probability density function, including the normal curve, is exactly 1.0 (or 100%).",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "The normal distribution curve is symmetrical about which central value?",
        "o": ["Mean only", "Median only", "Mode only", "Mean = Median = Mode"],
        "a": 3,
        "e": "In a perfectly symmetrical bell-shaped normal curve, the Mean, Median, and Mode coincide at the center (X = μ).",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "What percentage of observations lie within μ ± 1σ in a normal distribution?",
        "o": ["50.00%", "68.27%", "95.45%", "99.73%"],
        "a": 1,
        "e": "Under the empirical rule of the normal curve: μ ± 1σ covers 68.27%, μ ± 2σ covers 95.45%, and μ ± 3σ covers 99.73% of all values.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "In a normal distribution, what percentage of observations fall within the range μ ± 1.96σ?",
        "o": ["90%", "95%", "99%", "99.73%"],
        "a": 1,
        "e": "Exactly 95% of the total area under a normal curve lies between Z = -1.96 and Z = +1.96 (leaving 2.5% in each tail).",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "The points of inflection of the standard normal distribution curve occur at:",
        "o": ["X = μ ± σ", "X = μ ± 2σ", "X = μ ± 3σ", "X = μ only"],
        "a": 0,
        "e": "The normal curve changes its curvature from concave downward to convex downward at distance of one standard deviation on either side of the mean (μ ± σ).",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 3
    },
    {
        "q": "The transformation Z = (X - μ) / σ converts any normal variate X into a standard normal variate Z with:",
        "o": ["Mean = 1, Variance = 0", "Mean = 0, Variance = 1", "Mean = 0, Variance = 0", "Mean = 1, Variance = 1"],
        "a": 1,
        "e": "The standard normal distribution Z ~ N(0, 1) has mean zero (μ = 0) and standard deviation/variance equal to one (σ = 1).",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "If a dairy cow has a 305-day milk yield with Z-score = +2.0 in a herd with mean 3000 kg and SD 250 kg, her actual yield is:",
        "o": ["3250 kg", "3500 kg", "2500 kg", "3750 kg"],
        "a": 1,
        "e": "X = μ + Z*σ = 3000 + (2.0 * 250) = 3000 + 500 = 3500 kg.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "Which theorem states that the distribution of sample means approaches normality as sample size increases, regardless of population shape?",
        "o": ["Bayes' theorem", "Central Limit Theorem", "Chebyshev's theorem", "Hardy-Weinberg theorem"],
        "a": 1,
        "e": "The Central Limit Theorem (CLT) proves that for large n (n ≥ 30), the sampling distribution of sample means is approximately normal.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "In a binomial distribution with n = 100 and p = 0.2, what is the standard deviation?",
        "o": ["20", "16", "4", "2"],
        "a": 2,
        "e": "Variance = npq = 100 * 0.2 * 0.8 = 16. Standard deviation = sqrt(16) = 4.",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "If the probability of a calf being female is 0.5, what is the probability that all 3 calves born are female?",
        "o": ["0.5", "0.25", "0.125", "0.0625"],
        "a": 2,
        "e": "Since calf sex events are independent: P(3 females) = (0.5)³ = 0.125 (or 1/8).",
        "topicId": "u1-t09",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "The skewness of a normal distribution (γ₁) is:",
        "o": ["0", "1", "3", "Undefined"],
        "a": 0,
        "e": "Because the normal distribution is perfectly symmetric around its mean, its skewness γ₁ = 0.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },

    # ============================================================
    # u1-s3: Correlation, Regression & Sampling (18 MCQs)
    # ============================================================
    {
        "q": "The numerical value of Karl Pearson's correlation coefficient (r) always lies in the range:",
        "o": ["0 to +1", "-1 to +1", "-∞ to +∞", "0 to 100"],
        "a": 1,
        "e": "Pearson's correlation coefficient r is bounded strictly between -1.0 and +1.0 (-1 ≤ r ≤ +1).",
        "topicId": "u1-t12",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "If two biological traits have a correlation coefficient of r = 0, this indicates:",
        "o": ["Perfect linear relationship", "Zero linear relationship", "Inverse relationship", "Direct relationship"],
        "a": 1,
        "e": "An r = 0 indicates the complete absence of any linear association between the two continuous variables.",
        "topicId": "u1-t12",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Karl Pearson's coefficient of correlation is independent of:",
        "o": ["Change of origin only", "Change of scale only", "Both change of origin and change of scale", "Neither origin nor scale"],
        "a": 2,
        "e": "Correlation coefficient r is a pure dimensionless number, invariant to both shift of origin (adding/subtracting) and change of scale (multiplying/dividing).",
        "topicId": "u1-t12",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "Spearman's rank correlation coefficient (ρ) formula is given by:",
        "o": ["1 - [6 Σ d² / (n(n² - 1))]", "1 - [Σ d² / n]", "6 Σ d² / (n² - 1)", "[6 Σ d² / n(n - 1)] - 1"],
        "a": 0,
        "e": "Spearman's rank correlation formula is ρ = 1 - [6 Σ d² / (n(n² - 1))], where d is difference in ranks.",
        "topicId": "u1-t12",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "The geometric mean of the two regression coefficients b_yx and b_xy is equal to:",
        "o": ["Variance", "Correlation coefficient (r)", "Covariance", "Standard error"],
        "a": 1,
        "e": "By mathematical rule: r = ± sqrt(b_yx * b_xy). The geometric mean of the regression coefficients equals correlation coefficient r.",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "If regression coefficient b_yx = 0.8 and b_xy = 0.45, what is the correlation coefficient r?",
        "o": ["0.36", "0.60", "0.80", "0.18"],
        "a": 1,
        "e": "r = sqrt(b_yx * b_xy) = sqrt(0.8 * 0.45) = sqrt(0.36) = 0.60.",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "If one regression coefficient is greater than 1, the other regression coefficient must be:",
        "o": ["Greater than 1", "Equal to 1", "Less than 1", "Negative"],
        "a": 2,
        "e": "Since r² = b_yx * b_xy ≤ 1, if one regression coefficient exceeds 1, the other must be less than 1.",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 3
    },
    {
        "q": "The two regression lines of Y on X and X on Y intersect each other at the point:",
        "o": ["(0, 0)", "(X_bar, Y_bar)", "(1, 1)", "(σx, σy)"],
        "a": 1,
        "e": "Both regression lines always pass through the mean values of the two variables, intersecting at (X_bar, Y_bar).",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "If the two regression lines are perpendicular to each other, the correlation coefficient r between them is:",
        "o": ["+1", "-1", "0", "0.5"],
        "a": 2,
        "e": "When r = 0, the two regression lines are mutually perpendicular (at 90°). When r = ±1, the two regression lines coincide.",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "The proportion of total variation in Y explained by variation in X is measured by the:",
        "o": ["Correlation coefficient (r)", "Coefficient of determination (r²)", "Regression slope (b)", "Covariance"],
        "a": 1,
        "e": "The coefficient of determination (r²) measures the percentage of total variance in the dependent variable explained by the independent variable.",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "Sampling in which each individual in the population has a known and equal chance of being selected is:",
        "o": ["Simple random sampling", "Purposive sampling", "Quota sampling", "Judgment sampling"],
        "a": 0,
        "e": "In Simple Random Sampling (SRS), every sampling unit has an equal and independent probability of inclusion.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Which sampling technique divides a heterogeneous livestock population into homogeneous sub-groups before sampling?",
        "o": ["Cluster sampling", "Stratified random sampling", "Systematic sampling", "Convenience sampling"],
        "a": 1,
        "e": "Stratified random sampling divides a heterogeneous population into internally homogeneous groups (strata, e.g. age or breed) and samples from each.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Selecting every k-th animal from a numbered herd register after a random start is known as:",
        "o": ["Cluster sampling", "Stratified sampling", "Systematic sampling", "Multistage sampling"],
        "a": 2,
        "e": "Systematic sampling selects units at fixed intervals k = N/n after picking the first unit at random.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "In cluster sampling, the sampling units inside each selected cluster should ideally be:",
        "o": ["Homogeneous within, heterogeneous between", "Heterogeneous within, homogeneous between", "Identical in phenotype", "From a single family"],
        "a": 1,
        "e": "Ideally, clusters should be internally heterogeneous (mini-populations) while being homogeneous among different clusters.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "Sampling errors can be minimized by:",
        "o": ["Decreasing sample size", "Increasing sample size", "Biased selection", "Omitting non-respondents"],
        "a": 1,
        "e": "Sampling error is inversely proportional to the square root of sample size (SE = s / sqrt(n)), hence increasing n reduces sampling error.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Non-sampling errors can occur in:",
        "o": ["Sample surveys only", "Complete census only", "Both sample surveys and complete census", "Neither surveys nor census"],
        "a": 2,
        "e": "Non-sampling errors (data entry errors, faulty instruments, non-response) arise in both sample surveys and complete population enumerations.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "The regression coefficient of Y on X (b_yx) represents the:",
        "o": ["Value of Y when X is zero", "Average change in Y per unit change in X", "Ratio of means", "Total variation"],
        "a": 1,
        "e": "b_yx is the slope of the regression line, indicating the expected change in dependent variable Y for every one unit increase in independent variable X.",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "If r = -0.90 between parasite egg count and daily body weight gain in lambs, the association is:",
        "o": ["Weak positive", "Strong positive", "Strong negative (inverse)", "No association"],
        "a": 2,
        "e": "An r = -0.90 demonstrates a very strong negative linear relationship: higher parasite burden corresponds to significantly lower weight gain.",
        "topicId": "u1-t12",
        "subSection": "u1-s3",
        "diff": 1
    },

    # ============================================================
    # u1-s4: Hypothesis Testing & Experimental Designs (18 MCQs)
    # ============================================================
    {
        "q": "A hypothesis that asserts there is no significant difference between treatments or groups is called the:",
        "o": ["Alternative hypothesis (H₁)", "Null hypothesis (H₀)", "Composite hypothesis", "Simple hypothesis"],
        "a": 1,
        "e": "The Null Hypothesis (H₀) is the hypothesis of no difference or no treatment effect, tested for possible rejection.",
        "topicId": "u1-t15",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "Rejecting a true null hypothesis (H₀) constitutes which type of statistical error?",
        "o": ["Type I error (α)", "Type II error (β)", "Sampling error", "Standard error"],
        "a": 0,
        "e": "Type I error (probability α) occurs when the researcher rejects H₀ when it is actually true (false positive).",
        "topicId": "u1-t15",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "The power of a statistical test is defined mathematically as:",
        "o": ["1 - α", "1 - β", "α + β", "β / α"],
        "a": 1,
        "e": "Power of a test = 1 - β (where β is the probability of committing a Type II error, i.e., failing to reject a false null hypothesis).",
        "topicId": "u1-t15",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "For a two-tailed Z-test at the 5% level of significance, the critical value is:",
        "o": ["1.645", "1.96", "2.58", "3.00"],
        "a": 1,
        "e": "For a standard normal Z-test, the critical value for a two-tailed test at 5% (α = 0.05) is ±1.96; at 1% it is ±2.58.",
        "topicId": "u1-t15",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "Student's t-test was developed in 1908 by which scientist under the pseudonym 'Student'?",
        "o": ["Karl Pearson", "Sir Ronald A. Fisher", "William Sealy Gosset", "P. C. Mahalanobis"],
        "a": 2,
        "e": "William Sealy Gosset, a chemist and statistician at Guinness Brewery in Dublin, published the t-test under the pen name 'Student'.",
        "topicId": "u1-t16",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "Student's t-test is generally applied when the population variance is unknown and sample size n is:",
        "o": ["Greater than 100", "Equal to 50", "Small (n < 30)", "Infinite"],
        "a": 2,
        "e": "Student's t-test is specifically designed for small samples (n < 30) where the population standard deviation σ is unknown.",
        "topicId": "u1-t16",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "What are the degrees of freedom for a two-sample independent Student's t-test with sample sizes n₁ and n₂?",
        "o": ["n₁ + n₂", "n₁ + n₂ - 1", "n₁ + n₂ - 2", "(n₁ - 1)(n₂ - 1)"],
        "a": 2,
        "e": "For two independent samples, df = (n₁ - 1) + (n₂ - 1) = n₁ + n₂ - 2.",
        "topicId": "u1-t16",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "To test the efficacy of an anthelmintic drug by comparing fecal egg counts in the same 12 sheep before and after treatment, which test is appropriate?",
        "o": ["Unpaired t-test", "Paired t-test", "Z-test for proportions", "Chi-square test of homogeneity"],
        "a": 1,
        "e": "The paired t-test is used for dependent / repeated measurements on the same biological subjects (before vs after), with df = n - 1 = 11.",
        "topicId": "u1-t16",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "Who developed the Chi-Square (χ²) test of goodness of fit in the year 1900?",
        "o": ["Sir Francis Galton", "Karl Pearson", "W. S. Gosset", "Sewall Wright"],
        "a": 1,
        "e": "Karl Pearson developed the Chi-Square test in 1900 to test whether observed frequencies conform to theoretical expected frequencies.",
        "topicId": "u1-t17",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "In a 2 × 2 contingency table, the degrees of freedom for the Chi-Square test of independence is:",
        "o": ["1", "2", "3", "4"],
        "a": 0,
        "e": "Degrees of freedom for an r × c contingency table = (r - 1)(c - 1). For a 2 × 2 table: (2 - 1)(2 - 1) = 1 * 1 = 1.",
        "topicId": "u1-t17",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "Yates' continuity correction is applied to a 2 × 2 Chi-Square contingency table when:",
        "o": ["Degrees of freedom > 5", "Any expected cell frequency is less than 5", "Total sample size exceeds 500", "All frequencies are equal"],
        "a": 1,
        "e": "Yates' correction for continuity is mandatory in a 2 × 2 table (df = 1) whenever an expected cell frequency is small (less than 5).",
        "topicId": "u1-t17",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "What are the three fundamental principles of experimental design formulated by Sir Ronald A. Fisher?",
        "o": ["Randomization, Replication, Local Control", "Selection, Migration, Mutation", "Mean, Variance, Covariance", "Hypothesis, Experiment, Conclusion"],
        "a": 0,
        "e": "Fisher's three cardinal principles of experimental design are: Randomization (validity), Replication (precision/error estimation), and Local Control (error reduction).",
        "topicId": "u1-t18",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "Which experimental design does NOT utilize the principle of Local Control?",
        "o": ["Randomized Block Design (RBD)", "Completely Randomized Design (CRD)", "Latin Square Design (LSD)", "Split Plot Design"],
        "a": 1,
        "e": "In a Completely Randomized Design (CRD), experimental units are homogeneous (e.g. lab animals), so blocking (local control) is not applied.",
        "topicId": "u1-t18",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "In a Randomized Block Design (RBD) with 5 treatments and 4 replications (blocks), what is the error degrees of freedom?",
        "o": ["12", "15", "19", "20"],
        "a": 0,
        "e": "For RBD: Treatment df = t - 1 = 4; Block df = b - 1 = 3; Error df = (t - 1)(b - 1) = 4 * 3 = 12.",
        "topicId": "u1-t18",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "In Analysis of Variance (ANOVA), the F-statistic is computed as the ratio of:",
        "o": ["Total Sum of Squares to Error Sum of Squares", "Treatment Mean Square to Error Mean Square", "Error Mean Square to Treatment Mean Square", "Treatment Sum of Squares to Total df"],
        "a": 1,
        "e": "F = MS_treatment / MS_error. It tests whether variance between treatments is significantly greater than error variance within treatments.",
        "topicId": "u1-t19",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "Which non-parametric test is the distribution-free analogue of the two-sample independent Student's t-test?",
        "o": ["Wilcoxon signed-rank test", "Mann-Whitney U test", "Kruskal-Wallis H test", "Chi-square test"],
        "a": 1,
        "e": "The Mann-Whitney U test (Wilcoxon rank-sum test) compares two independent groups without assuming normal distribution.",
        "topicId": "u1-t20",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "Which non-parametric test is used as an alternative to one-way ANOVA for comparing three or more independent groups?",
        "o": ["Kruskal-Wallis H test", "Mann-Whitney U test", "Wilcoxon signed-rank test", "Sign test"],
        "a": 0,
        "e": "The Kruskal-Wallis one-way analysis of variance by ranks is the non-parametric analogue to one-way ANOVA.",
        "topicId": "u1-t20",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "In an experiment testing 4 diets across 20 broiler chicks in a CRD, the treatment degrees of freedom and error degrees of freedom are:",
        "o": ["3 and 16", "4 and 20", "3 and 19", "4 and 16"],
        "a": 0,
        "e": "Total df = N - 1 = 19; Treatment df = t - 1 = 4 - 1 = 3; Error df = N - t = 20 - 4 = 16.",
        "topicId": "u1-t18",
        "subSection": "u1-s4",
        "diff": 2
    },

    # ============================================================
    # u1-s5: Computer Applications & Data Analysis (18 MCQs)
    # ============================================================
    {
        "q": "Which component of the Central Processing Unit (CPU) performs arithmetic and logical calculations?",
        "o": ["Control Unit (CU)", "Arithmetic and Logic Unit (ALU)", "Cache Memory", "Hard Disk Drive"],
        "a": 1,
        "e": "The Arithmetic and Logic Unit (ALU) is responsible for executing all mathematical additions, subtractions, and logical comparison operations.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "Which type of computer memory is volatile and loses its stored contents when power is turned off?",
        "o": ["ROM (Read Only Memory)", "RAM (Random Access Memory)", "Hard Disk", "Flash Drive"],
        "a": 1,
        "e": "RAM is primary volatile memory; all data held in RAM is lost as soon as the system power supply is interrupted.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "A program that translates an entire high-level source code program into machine language object code in one single pass is called a:",
        "o": ["Interpreter", "Compiler", "Assembler", "Operating system"],
        "a": 1,
        "e": "A compiler translates the complete source code into machine-readable object code at once, unlike an interpreter which translates line by line.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In a Relational Database Management System (RDBMS), a table row is formally termed a:",
        "o": ["Attribute", "Tuple (or Record)", "Domain", "Relation"],
        "a": 1,
        "e": "In relational database theory, a row in a table is called a Tuple or Record, while a column is called an Attribute.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "An attribute or set of attributes that uniquely identifies every record in a veterinary database table is the:",
        "o": ["Foreign Key", "Primary Key", "Candidate Key", "Secondary Key"],
        "a": 1,
        "e": "A Primary Key uniquely identifies each row (e.g. Unique Animal Ear Tag Number or Microchip ID) in an RDBMS table without nulls.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "Which SQL command is utilized to retrieve specific records from a livestock database table?",
        "o": ["UPDATE", "INSERT", "SELECT", "DELETE"],
        "a": 2,
        "e": "The SELECT statement in SQL is used to query and retrieve data from one or more database tables.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In MS-Excel, an absolute cell reference is designated by prefixing the column letter and row number with:",
        "o": ["#", "$", "%", "@"],
        "a": 1,
        "e": "The dollar sign ($) creates an absolute reference (e.g., $A$1) that prevents the cell coordinates from changing when copied across rows or columns.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "Which MS-Excel function computes the sample standard deviation of a dataset of body weights?",
        "o": ["=STDEV.S()", "=STDEV.P()", "=VAR.S()", "=DEV.SQ()"],
        "a": 0,
        "e": "=STDEV.S() computes sample standard deviation using (n - 1) in the denominator, whereas =STDEV.P() uses N for the entire population.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 2
    },
    {
        "q": "Which MS-Excel function is used to calculate Pearson's correlation coefficient between weaning weight and yearling weight?",
        "o": ["=CORREL()", "=COVAR()", "=SLOPE()", "=INTERCEPT()"],
        "a": 0,
        "e": "The =CORREL(array1, array2) or =PEARSON(array1, array2) function returns Pearson's correlation coefficient r.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 2
    },
    {
        "q": "To perform a Student's t-test in MS-Excel comparing treatment vs control milk yields, which formula is entered?",
        "o": ["=T.TEST()", "=F.TEST()", "=Z.TEST()", "=CHISQ.TEST()"],
        "a": 0,
        "e": "=T.TEST(array1, array2, tails, type) returns the probability associated with a Student's t-test.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 2
    },
    {
        "q": "Which Excel chart type is the standard choice for displaying a scatter plot and fitting a linear regression trendline?",
        "o": ["Pie Chart", "Line Chart", "X Y (Scatter) Chart", "Column Chart"],
        "a": 2,
        "e": "The X Y (Scatter) chart plots paired numerical coordinates and allows adding linear trendlines and showing R² equations.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "The MS-Excel add-in that provides advanced statistical tools including ANOVA, F-test, and regression analysis is:",
        "o": ["Solver Add-in", "Data Analysis ToolPak", "Power Pivot", "VBA Macro"],
        "a": 1,
        "e": "The Data Analysis ToolPak provides ready-to-use statistical procedures including Descriptive Statistics, ANOVA, Regression, and t-tests.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "How many bytes make up one Kilobyte (KB) in binary computing?",
        "o": ["1000 bytes", "1024 bytes", "512 bytes", "2048 bytes"],
        "a": 1,
        "e": "In binary computer storage, 1 Kilobyte (KB) = 2¹⁰ bytes = 1024 bytes.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "Which generation of computers introduced integrated circuits (ICs) and semiconductors?",
        "o": ["First generation", "Second generation", "Third generation", "Fourth generation"],
        "a": 2,
        "e": "First generation used vacuum tubes, second used transistors, and third generation introduced Integrated Circuits (ICs).",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 2
    },
    {
        "q": "The primary key of one table placed into another table to establish a relational link between them is called a:",
        "o": ["Foreign Key", "Candidate Key", "Composite Key", "Alternate Key"],
        "a": 0,
        "e": "A Foreign Key is an attribute in a child table that matches the Primary Key of a parent table, establishing referential integrity.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 2
    },
    {
        "q": "Which MS-Excel function calculates the median of lactation lengths stored in cells A1 through A50?",
        "o": ["=MEDIAN(A1:A50)", "=AVERAGE(A1:A50)", "=MODE(A1:A50)", "=MID(A1:A50)"],
        "a": 0,
        "e": "=MEDIAN(A1:A50) calculates the 50th percentile (median) of the values in the specified cell range.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "What will the formula =AVERAGE(10, 20, 30) return in MS-Excel?",
        "o": ["60", "20", "30", "15"],
        "a": 1,
        "e": "The arithmetic mean of 10, 20, and 30 is (10 + 20 + 30) / 3 = 60 / 3 = 20.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "An operating system (e.g. Windows, Linux) is an example of:",
        "o": ["Application software", "System software", "Database software", "Hardware"],
        "a": 1,
        "e": "Operating systems are system software that manage hardware resources and provide common services for application programs.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    }
]

unit1_tf = [
    # ============================================================
    # u1-s1: Data Classification, Central Tendency & Dispersion (9 T/F)
    # ============================================================
    {
        "q": "Sir Ronald A. Fisher is considered the father of modern statistics and invented Analysis of Variance (ANOVA).",
        "a": True,
        "e": "Sir R. A. Fisher invented ANOVA, the F-distribution, and formulated the fundamental principles of experimental design.",
        "topicId": "u1-t01",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "Statistical laws are deterministic and hold true for isolated individual animals with mathematical certainty.",
        "a": False,
        "e": "Statistical laws are stochastic and probabilistic; they hold true on average and in the long run across aggregates of individuals.",
        "topicId": "u1-t01",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "A statistic is a fixed numerical characteristic of an entire biological population.",
        "a": False,
        "e": "A parameter is a characteristic of a population; a statistic is calculated from sample data.",
        "topicId": "u1-t03",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "The median of a continuous frequency distribution can be determined graphically from Ogive curves.",
        "a": True,
        "e": "The intersection of less-than and more-than ogives directly gives the median on the horizontal axis.",
        "topicId": "u1-t04",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "The sum of the absolute deviations of observations is minimum when measured from their median.",
        "a": True,
        "e": "A mathematical property of the median is that Σ|X - Median| is smaller than deviations taken from any other value.",
        "topicId": "u1-t05",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "The standard deviation is independent of change of scale.",
        "a": False,
        "e": "Standard deviation is independent of change of origin (addition/subtraction), but is directly affected by change of scale (multiplication/division).",
        "topicId": "u1-t06",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "The coefficient of variation is a dimensionless relative measure of dispersion expressed as a percentage.",
        "a": True,
        "e": "CV = (Standard Deviation / Mean) * 100. It is a unitless percentage used to compare relative variability.",
        "topicId": "u1-t07",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "For any symmetrical distribution, the third central moment (μ₃) is zero.",
        "a": True,
        "e": "Because positive and negative deviations from the mean cancel out in odd powers, all odd central moments (μ₁, μ₃, μ₅) equal zero in a symmetrical distribution.",
        "topicId": "u1-t08",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "A leptokurtic distribution curve is flatter-topped than a normal curve.",
        "a": False,
        "e": "A leptokurtic curve is more peaked with heavier tails (β₂ > 3). A platykurtic curve is flatter-topped (β₂ < 3).",
        "topicId": "u1-t08",
        "subSection": "u1-s1",
        "diff": 2
    },

    # ============================================================
    # u1-s2: Probability & Distributions (9 T/F)
    # ============================================================
    {
        "q": "The probability of an impossible event is zero, while the probability of a certain event is one.",
        "a": True,
        "e": "By Kolmogorov's probability axioms, 0 ≤ P(E) ≤ 1. P(Impossible) = 0 and P(Certain) = 1.",
        "topicId": "u1-t09",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "In a Binomial distribution, the variance is always greater than the mean.",
        "a": False,
        "e": "In a Binomial distribution, Mean = np and Variance = npq. Since q < 1, variance is always strictly LESS than the mean.",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "In a Poisson distribution, the mean and the variance are equal.",
        "a": True,
        "e": "A distinctive mathematical property of the Poisson distribution is that Mean = Variance = λ.",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "The normal distribution curve is asymptotic to the horizontal X-axis on both sides.",
        "a": True,
        "e": "The tails of the normal curve extend indefinitely in both directions (-∞ to +∞), approaching but never actually touching the horizontal axis.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "Approximately 95.45% of the total observations in a normal distribution lie within μ ± 2σ.",
        "a": True,
        "e": "Under the normal curve: μ ± 1σ contains 68.27%, μ ± 2σ contains 95.45%, and μ ± 3σ contains 99.73% of values.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "The standard normal distribution has a mean of 1 and a standard deviation of 0.",
        "a": False,
        "e": "The standard normal distribution has a mean of zero (μ = 0) and standard deviation of one (σ = 1).",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "The Poisson distribution can be derived as a limiting case of the Binomial distribution when n is very large and p is very small.",
        "a": True,
        "e": "As n → ∞ and p → 0 such that np = λ (a finite constant), the Binomial distribution tends to the Poisson distribution.",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "The normal curve is bimodal, possessing two distinct peak values.",
        "a": False,
        "e": "The normal curve is strictly unimodal, possessing a single central peak where Mean = Median = Mode.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "If two events A and B are independent, P(A ∩ B) = P(A) * P(B).",
        "a": True,
        "e": "By the multiplication rule of probability, for independent events, the joint probability is the product of their individual probabilities.",
        "topicId": "u1-t09",
        "subSection": "u1-s2",
        "diff": 1
    },

    # ============================================================
    # u1-s3: Correlation, Regression & Sampling (9 T/F)
    # ============================================================
    {
        "q": "Karl Pearson's correlation coefficient can take values greater than +1 for strong relationships.",
        "a": False,
        "e": "The correlation coefficient r is mathematically bounded between -1.0 and +1.0. It can never exceed +1 or fall below -1.",
        "topicId": "u1-t12",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Both regression coefficients b_yx and b_xy must always have the same algebraic sign.",
        "a": True,
        "e": "Since r = ± sqrt(b_yx * b_xy), both regression coefficients must share the same sign as the correlation coefficient r (both positive or both negative).",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "The coefficient of determination r² can take negative values when correlation is negative.",
        "a": False,
        "e": "Since r² is the square of r, it is always non-negative, ranging from 0 to 1 (0% to 100% explained variance).",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "Stratified random sampling provides more representative samples than simple random sampling when the population is heterogeneous.",
        "a": True,
        "e": "By dividing heterogeneous populations into homogeneous strata, stratified sampling reduces sampling variance and ensures all subgroups are represented.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "The two regression lines coincide into a single line when r = 0.",
        "a": False,
        "e": "When r = 0, the two regression lines are perpendicular to each other. They coincide into a single line when r = +1 or r = -1.",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "Sampling error increases as sample size increases.",
        "a": False,
        "e": "Sampling error decreases as sample size increases, because SE = s / sqrt(n). Larger samples provide more precise population estimates.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Non-sampling errors can occur even in a complete population census.",
        "a": True,
        "e": "Non-sampling errors arise from measurement faults, non-response, and recording errors, which exist in both sample surveys and complete censuses.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Spearman's rank correlation is a non-parametric method suitable for ranked or qualitative ordinal data.",
        "a": True,
        "e": "Spearman's rank correlation does not assume a normal distribution and evaluates monotonic relationships between ranked variables.",
        "topicId": "u1-t12",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "The intersection point of the two regression lines gives the mean values (X_bar, Y_bar).",
        "a": True,
        "e": "Both regression lines of Y on X and X on Y pass through the point of means (X_bar, Y_bar).",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 1
    },

    # ============================================================
    # u1-s4: Hypothesis Testing & Experimental Designs (9 T/F)
    # ============================================================
    {
        "q": "Type I error is the error committed by failing to reject a false null hypothesis.",
        "a": False,
        "e": "Type I error is rejecting a true null hypothesis (α). Failing to reject a false null hypothesis is Type II error (β).",
        "topicId": "u1-t15",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "A large sample Z-test is applicable when the sample size n is 30 or greater.",
        "a": True,
        "e": "By convention in biostatistics, sample sizes n ≥ 30 are considered large samples where the Z-test is valid under the Central Limit Theorem.",
        "topicId": "u1-t15",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "In a paired t-test with 10 pairs of observations, the degrees of freedom is 9.",
        "a": True,
        "e": "For a paired t-test on n differences, degrees of freedom df = n - 1 = 10 - 1 = 9.",
        "topicId": "u1-t16",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "The Chi-Square test can be used to test the goodness of fit of Mendelian genetic ratios.",
        "a": True,
        "e": "Karl Pearson's Chi-Square test is standardly used to test whether observed phenotypic counts fit theoretical Mendelian expectations (e.g. 3:1 or 9:3:3:1).",
        "topicId": "u1-t17",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "In a Completely Randomized Design (CRD), local control is exercised by grouping units into homogeneous blocks.",
        "a": False,
        "e": "CRD does not use local control (blocking); treatments are allocated completely at random to all homogeneous experimental units.",
        "topicId": "u1-t18",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "The F-test in ANOVA is a two-tailed test in standard agricultural and veterinary trials.",
        "a": False,
        "e": "The F-test in ANOVA is an upper one-tailed (right-tailed) test because the null hypothesis is rejected only when MS_treatment is significantly greater than MS_error.",
        "topicId": "u1-t19",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "The Mann-Whitney U test requires the assumption that the biological data are normally distributed.",
        "a": False,
        "e": "Mann-Whitney U is a non-parametric (distribution-free) test and does not assume a normal distribution.",
        "topicId": "u1-t20",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "Randomization eliminates subjective investigator bias in allocating treatments to experimental animals.",
        "a": True,
        "e": "Randomization ensures that every experimental unit has an equal chance of receiving any treatment, satisfying statistical independence.",
        "topicId": "u1-t18",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "In a 2 × 2 contingency table, the degrees of freedom for the Chi-Square test is 2.",
        "a": False,
        "e": "In a 2 × 2 contingency table, df = (2 - 1)(2 - 1) = 1 * 1 = 1.",
        "topicId": "u1-t17",
        "subSection": "u1-s4",
        "diff": 1
    },

    # ============================================================
    # u1-s5: Computer Applications & Data Analysis (9 T/F)
    # ============================================================
    {
        "q": "ROM (Read Only Memory) is non-volatile memory that retains its data even after power is switched off.",
        "a": True,
        "e": "ROM permanently stores startup firmware (BIOS) and is non-volatile, retaining information without power.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "Machine language consists of binary 0s and 1s that can be directly executed by the computer processor without translation.",
        "a": True,
        "e": "Machine language is the fundamental native binary language (0s and 1s) directly understood and executed by the CPU.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "A Primary Key in an RDBMS table can contain duplicate values and null entries.",
        "a": False,
        "e": "A Primary Key must contain strictly unique, non-null values for every record to guarantee unique entity identification.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In MS-Excel, the formula =AVERAGE(A1:A10) ignores text cells and empty cells in the specified range.",
        "a": True,
        "e": "=AVERAGE() automatically ignores blank cells and text strings, averaging only numerical values.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 2
    },
    {
        "q": "An interpreter translates high-level programming code line-by-line during program execution.",
        "a": True,
        "e": "An interpreter executes instructions line by line, pausing whenever an error is encountered, unlike a compiler which translates the entire file.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In MS-Excel, $B$4 represents a relative cell reference.",
        "a": False,
        "e": "$B$4 is an absolute cell reference. A relative cell reference has no dollar signs (e.g. B4).",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "SQL stands for Structured Query Language.",
        "a": True,
        "e": "SQL (Structured Query Language) is the standardized language for defining, querying, and updating relational database systems.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In MS-Excel, =VAR.P() calculates the variance based on a sample rather than an entire population.",
        "a": False,
        "e": "=VAR.P() computes population variance using N. The function =VAR.S() calculates sample variance using (n - 1).",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 2
    },
    {
        "q": "The Data Analysis ToolPak is a built-in add-in in MS-Excel that provides advanced statistical procedures like ANOVA and t-tests.",
        "a": True,
        "e": "The Analysis ToolPak is an Excel add-in providing statistical analysis tools including ANOVA, regression, correlation, and t-tests.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    }
]

unit1_fib = [
    # ============================================================
    # u1-s1: Data Classification, Central Tendency & Dispersion (9 FIB)
    # ============================================================
    {
        "q": "The term 'Biometry' was coined by Sir Francis ______.",
        "a": ["Galton", "Francis Galton"],
        "a_display": "Galton",
        "e": "Sir Francis Galton coined the term 'Biometry' and established early biometric methods in heredity.",
        "topicId": "u1-t01",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "A numerical characteristic computed from a sample to estimate a population value is called a ______.",
        "a": ["statistic"],
        "a_display": "Statistic",
        "e": "A statistic is a function of observable sample values (e.g., sample mean x̄), whereas a parameter belongs to the whole population.",
        "topicId": "u1-t03",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "The cumulative frequency curve used to locate the median graphically is known as an ______.",
        "a": ["ogive", "ogive curve"],
        "a_display": "Ogive",
        "e": "An ogive (cumulative frequency polygon) is plotted to determine medians and quartiles graphically.",
        "topicId": "u1-t04",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "The algebraic sum of deviations of a set of observations from their arithmetic mean is always equal to ______.",
        "a": ["0", "zero"],
        "a_display": "0 (zero)",
        "e": "Σ(X - X_bar) is mathematically always equal to zero.",
        "topicId": "u1-t05",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "According to Karl Pearson's empirical formula, Mode = 3 Median - 2 ______.",
        "a": ["mean", "arithmetic mean"],
        "a_display": "Mean",
        "e": "The empirical relationship for moderately skewed data is: Mode = 3 Median - 2 Mean.",
        "topicId": "u1-t05",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "The positive square root of variance is called the ______ deviation.",
        "a": ["standard", "standard deviation"],
        "a_display": "Standard",
        "e": "Standard deviation (SD or σ) is the positive square root of the variance.",
        "topicId": "u1-t06",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "The formula for Coefficient of Variation (CV) is (Standard Deviation / Mean) multiplied by ______.",
        "a": ["100"],
        "a_display": "100",
        "e": "CV = (SD / Mean) * 100, which expresses dispersion as a percentage of the mean.",
        "topicId": "u1-t07",
        "subSection": "u1-s1",
        "diff": 1
    },
    {
        "q": "The first central moment (μ₁) about the arithmetic mean is always equal to ______.",
        "a": ["0", "zero"],
        "a_display": "0 (zero)",
        "e": "The first moment about the mean μ₁ is always equal to 0.",
        "topicId": "u1-t08",
        "subSection": "u1-s1",
        "diff": 2
    },
    {
        "q": "A frequency distribution curve that is more peaked than the normal curve is termed ______.",
        "a": ["leptokurtic"],
        "a_display": "Leptokurtic",
        "e": "A distribution with β₂ > 3 has a sharper peak and heavier tails, termed leptokurtic.",
        "topicId": "u1-t08",
        "subSection": "u1-s1",
        "diff": 2
    },

    # ============================================================
    # u1-s2: Probability & Distributions (9 FIB)
    # ============================================================
    {
        "q": "If two events cannot occur simultaneously in a single trial, they are called mutually ______ events.",
        "a": ["exclusive", "mutually exclusive"],
        "a_display": "Exclusive",
        "e": "Mutually exclusive (disjoint) events cannot happen at the same time: P(A ∩ B) = 0.",
        "topicId": "u1-t09",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "In a Binomial distribution B(n, p), the formula for the mean is ______.",
        "a": ["np", "n*p"],
        "a_display": "np",
        "e": "The expected value (mean) of a binomial distribution is the product of n and p.",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "In a Poisson distribution, the mean and the variance are both equal to the parameter ______.",
        "a": ["lambda", "λ", "m"],
        "a_display": "λ (lambda)",
        "e": "For a Poisson distribution, Mean = Variance = λ.",
        "topicId": "u1-t10",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "The total area under the standard normal probability curve is equal to ______.",
        "a": ["1", "1.0", "one"],
        "a_display": "1.0",
        "e": "The integral of the normal probability density function over all real numbers equals 1.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "In a normal distribution, approximately ______ percent of total observations lie within the interval μ ± 1σ.",
        "a": ["68.27", "68.27%", "68.3", "68"],
        "a_display": "68.27%",
        "e": "The area under a normal curve between μ - σ and μ + σ is approximately 68.27%.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "The standard normal variate has a mean of 0 and a standard deviation of ______.",
        "a": ["1", "one"],
        "a_display": "1",
        "e": "Z = (X - μ) / σ follows N(0, 1) with mean 0 and variance/SD equal to 1.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },
    {
        "q": "The points of inflection of a normal distribution curve occur at X = μ ± ______.",
        "a": ["sigma", "σ", "1 sigma", "1σ", "s"],
        "a_display": "σ (sigma)",
        "e": "The inflection points of a normal curve occur at one standard deviation on either side of the mean (μ ± σ).",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "The theorem stating that sample means approach normality as sample size increases is the Central ______ Theorem.",
        "a": ["limit", "central limit"],
        "a_display": "Limit",
        "e": "The Central Limit Theorem provides the foundation for using normal theory on large biological samples.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 2
    },
    {
        "q": "The measure of skewness (γ₁) for a normal distribution curve is equal to ______.",
        "a": ["0", "zero"],
        "a_display": "0 (zero)",
        "e": "Because the normal distribution is perfectly symmetrical, its skewness γ₁ = 0.",
        "topicId": "u1-t11",
        "subSection": "u1-s2",
        "diff": 1
    },

    # ============================================================
    # u1-s3: Correlation, Regression & Sampling (9 FIB)
    # ============================================================
    {
        "q": "The value of Karl Pearson's correlation coefficient r ranges between -1 and ______.",
        "a": ["+1", "1", "+1.0", "1.0"],
        "a_display": "+1",
        "e": "The correlation coefficient r is mathematically constrained between -1 and +1.",
        "topicId": "u1-t12",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "If two variables have a correlation coefficient of r = 0, there is zero ______ relationship between them.",
        "a": ["linear"],
        "a_display": "Linear",
        "e": "An r of 0 specifically implies the absence of any linear relationship (a non-linear relationship may still exist).",
        "topicId": "u1-t12",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "The geometric mean of the two regression coefficients b_yx and b_xy is equal to the ______ coefficient.",
        "a": ["correlation", "correlation coefficient", "r"],
        "a_display": "Correlation",
        "e": "r = sqrt(b_yx * b_xy). The correlation coefficient is the geometric mean of the two regression coefficients.",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "The two regression lines intersect at the point of their ______ (X_bar, Y_bar).",
        "a": ["means", "mean values", "mean"],
        "a_display": "Means",
        "e": "The coordinates of the intersection of both regression lines are the sample means (X_bar, Y_bar).",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "When the correlation coefficient r = 0, the two regression lines are ______ to each other.",
        "a": ["perpendicular", "at right angles", "at 90 degrees"],
        "a_display": "Perpendicular",
        "e": "When r = 0, the angle between the two regression lines is 90 degrees (perpendicular).",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 2
    },
    {
        "q": "The square of the correlation coefficient (r²) is known as the coefficient of ______.",
        "a": ["determination"],
        "a_display": "Determination",
        "e": "r² is the Coefficient of Determination, representing the proportion of variance explained by the model.",
        "topicId": "u1-t13",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Selecting every k-th element from an ordered sampling frame is called ______ sampling.",
        "a": ["systematic", "systematic sampling"],
        "a_display": "Systematic",
        "e": "Systematic sampling selects units at regular intervals k = N/n after a random starting point.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Dividing a heterogeneous population into homogeneous sub-populations before sampling is called ______ random sampling.",
        "a": ["stratified", "stratified random sampling"],
        "a_display": "Stratified",
        "e": "Stratified random sampling ensures that all distinct subgroups (strata) are proportionately represented.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },
    {
        "q": "Sampling error can be reduced by ______ the sample size.",
        "a": ["increasing", "raising", "enlarging"],
        "a_display": "Increasing",
        "e": "Since standard error is inversely proportional to sqrt(n), increasing the sample size reduces sampling error.",
        "topicId": "u1-t14",
        "subSection": "u1-s3",
        "diff": 1
    },

    # ============================================================
    # u1-s4: Hypothesis Testing & Experimental Designs (9 FIB)
    # ============================================================
    {
        "q": "The hypothesis of 'no difference' between treatment groups is called the ______ hypothesis.",
        "a": ["null", "null hypothesis"],
        "a_display": "Null",
        "e": "The Null Hypothesis (H₀) posits that observed sample differences are purely due to chance.",
        "topicId": "u1-t15",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "Rejecting a true null hypothesis constitutes a Type ______ error.",
        "a": ["I", "1", "one", "type I"],
        "a_display": "I",
        "e": "Type I error (α) is rejecting H₀ when it is actually true (false positive).",
        "topicId": "u1-t15",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "For a two-tailed Z-test at the 5% significance level, the critical value is ± ______.",
        "a": ["1.96"],
        "a_display": "1.96",
        "e": "Z = ±1.96 cuts off 2.5% of the area in each tail (5% total).",
        "topicId": "u1-t15",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "Student's t-test was developed by William Sealy ______ in 1908.",
        "a": ["Gosset", "William Gosset", "W. S. Gosset"],
        "a_display": "Gosset",
        "e": "William Sealy Gosset invented the t-distribution while working for Guinness Brewery, writing under the pen name 'Student'.",
        "topicId": "u1-t16",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "In a paired t-test with n pairs of observations, the degrees of freedom is n - ______.",
        "a": ["1", "one"],
        "a_display": "1",
        "e": "The paired t-test operates on n paired differences, yielding df = n - 1.",
        "topicId": "u1-t16",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "The Chi-Square test was introduced in 1900 by Karl ______.",
        "a": ["Pearson", "Karl Pearson"],
        "a_display": "Pearson",
        "e": "Karl Pearson developed the Chi-Square test of goodness of fit and independence of attributes.",
        "topicId": "u1-t17",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "The continuity correction applied to a 2 × 2 contingency table when cell frequencies are small is ______' correction.",
        "a": ["Yates'", "Yates", "Yates's"],
        "a_display": "Yates'",
        "e": "Frank Yates introduced Yates' correction for continuity to improve the Chi-Square approximation for 1 df with small expected numbers.",
        "topicId": "u1-t17",
        "subSection": "u1-s4",
        "diff": 2
    },
    {
        "q": "The three principles of experimental design are Randomization, Replication, and Local ______.",
        "a": ["control"],
        "a_display": "Control",
        "e": "Fisher's three principles are Randomization, Replication, and Local Control (blocking).",
        "topicId": "u1-t18",
        "subSection": "u1-s4",
        "diff": 1
    },
    {
        "q": "In ANOVA, the variance ratio test statistic is denoted by the letter ______.",
        "a": ["F", "f"],
        "a_display": "F",
        "e": "The F-statistic (named in honor of Sir Ronald A. Fisher) equals MS_treatment / MS_error.",
        "topicId": "u1-t19",
        "subSection": "u1-s4",
        "diff": 1
    },

    # ============================================================
    # u1-s5: Computer Applications & Data Analysis (9 FIB)
    # ============================================================
    {
        "q": "The central hardware unit that performs arithmetic calculations and logical decisions in a computer is the ______.",
        "a": ["ALU", "Arithmetic Logic Unit", "Arithmetic and Logic Unit"],
        "a_display": "ALU",
        "e": "The ALU (Arithmetic and Logic Unit) executes math and boolean logic operations within the CPU.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "Computer memory that loses its content when electrical power is switched off is called ______ memory.",
        "a": ["volatile", "RAM"],
        "a_display": "Volatile",
        "e": "RAM is volatile memory because its electrical states vanish when power is lost.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "A program that translates an entire high-level program into machine code all at once is called a ______.",
        "a": ["compiler"],
        "a_display": "Compiler",
        "e": "A compiler scans and translates the complete source code file into executable machine language.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In a relational database, a column representing a specific data property is called an ______.",
        "a": ["attribute", "field"],
        "a_display": "Attribute",
        "e": "Columns are called attributes (or fields), while rows are called tuples (or records).",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "The unique field that prevents duplicate records in an RDBMS table is called the ______ Key.",
        "a": ["primary", "primary key"],
        "a_display": "Primary",
        "e": "The Primary Key uniquely identifies each row in a relational database table.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In MS-Excel, an absolute cell reference is indicated by placing the ______ symbol before column and row identifiers.",
        "a": ["$", "dollar", "dollar sign"],
        "a_display": "$",
        "e": "Placing a $ sign (e.g. $A$1) locks the cell reference during copy-paste operations.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In MS-Excel, the function to calculate the sample standard deviation is =STDEV.______().",
        "a": ["S", "s"],
        "a_display": "S",
        "e": "=STDEV.S() calculates sample standard deviation using n - 1 degrees of freedom.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In MS-Excel, the function used to compute Pearson's correlation coefficient is =______().",
        "a": ["CORREL", "PEARSON", "correl", "pearson"],
        "a_display": "CORREL",
        "e": "The =CORREL() function returns the Pearson correlation coefficient between two cell arrays.",
        "topicId": "u1-t22",
        "subSection": "u1-s5",
        "diff": 1
    },
    {
        "q": "In binary computer storage, one Kilobyte (KB) is equal to ______ bytes.",
        "a": ["1024"],
        "a_display": "1024",
        "e": "In binary 2¹⁰ = 1024 bytes = 1 KB.",
        "topicId": "u1-t21",
        "subSection": "u1-s5",
        "diff": 1
    }
]
