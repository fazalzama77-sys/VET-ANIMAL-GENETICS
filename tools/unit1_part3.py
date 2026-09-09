# -*- coding: utf-8 -*-
"""
Unit 1 - Part 3: Topics u1-t15 to u1-t22
Biostatistics & Computer Application (IVRI Undergrad 10 CGPA Standard)
"""

topics = {}

topics["u1-t15"] = {
    "summary": "Hypothesis testing evaluates empirical biological claims against null assumptions, utilizing large-sample Z-tests (n ≥ 30) to test sample means and proportions against theoretical population values.",
    "desc": (
        "<b>LOGIC AND TERMINOLOGY OF HYPOTHESIS TESTING</b><br>"
        "Statistical hypothesis testing provides an objective mathematical framework for deciding whether observed biological differences between treatment groups reflect genuine experimental effects or merely random sampling fluctuations:"
        "<ul>"
        "<li><b>Null Hypothesis (H₀):</b> The hypothesis of 'no difference' or 'no effect' set up for the express purpose of being tested and potentially rejected (e.g., <i>'H₀: Herbal galactagogue feed supplement does not increase daily milk yield in Murrah buffaloes; &mu;₁ = &mu;₂'</i>).</li>"
        "<li><b>Alternative Hypothesis (H₁):</b> The counter-claim accepted when H₀ is rejected based on sample evidence (e.g., <i>'H₁: Herbal supplement significantly increases milk yield; &mu;₁ &gt; &mu;₂'</i>).</li>"
        "<li><b>Two-Tailed versus One-Tailed Tests:</b>"
        "<br>&bull; <i>Two-Tailed Test:</i> Non-directional test where rejection region lies in both tails of the distribution (<code>H₁: &mu; &ne; &mu;₀</code>). Critical Z values: <b>&plusmn;1.96 at 5% level</b> (p &lt; 0.05), and <b>&plusmn;2.58 at 1% level</b> (p &lt; 0.01)."
        "<br>&bull; <i>One-Tailed Test:</i> Directional test where rejection region lies exclusively in one tail (<code>H₁: &mu; &gt; &mu;₀</code> or <code>H₁: &mu; &lt; &mu;₀</code>). Critical Z values: <b>+1.645 (right-tailed at 5%)</b> and <b>+2.33 (right-tailed at 1%)</b>.</li>"
        "<li><b>Decision Errors in Hypothesis Testing:</b>"
        "<br>&bull; <b>Type I Error (&alpha;):</b> Rejecting the null hypothesis when it is actually true (False Positive). The probability of committing a Type I error is the <b>Level of Significance (&alpha;)</b>, conventionally set at 0.05 (5%) or 0.01 (1%)."
        "<br>&bull; <b>Type II Error (&beta;):</b> Failing to reject (accepting) the null hypothesis when it is actually false (False Negative). "
        "<br>&bull; <b>Power of the Test (1 - &beta;):</b> The probability of correctly rejecting a false null hypothesis (true biological discovery).</li>"
        "<li><b>Critical Value & P-value:</b> The critical value defines the boundary of the rejection region. The P-value is the exact probability of obtaining a test statistic as extreme as, or more extreme than, the observed result under H₀. If <code>P &le; &alpha;</code>, reject H₀.</li>"
        "</ul><br>"
        "<b>LARGE SAMPLE TESTS (Z-TESTS: n &ge; 30)</b><br>"
        "By the Central Limit Theorem, when sample size n &ge; 30, the sampling distribution of means or proportions is approximately normal, regardless of the parent population distribution. The test statistic is the <b>Standard Normal Variate (Z)</b>:<br><br>"
        "<b>1. Z-Test for Single Mean:</b>"
        "<br>Tests whether a sample mean (X&#772;) differs significantly from a known population mean (&mu;₀):"
        "<br><code>Z = (X&#772; - &mu;₀) / (&sigma; / &radic;n) &approx; (X&#772; - &mu;₀) / (s / &radic;n)</code><br><br>"
        "<b>2. Z-Test for Difference of Two Independent Means:</b>"
        "<br>Tests whether two large independent samples (sizes n₁, n₂) have significantly different means (X&#772;₁, X&#772;₂):"
        "<br><code>Z = (X&#772;₁ - X&#772;₂) / &radic;[ (&sigma;₁&sup2; / n₁) + (&sigma;₂&sup2; / n₂) ] &approx; (X&#772;₁ - X&#772;₂) / &radic;[ (s₁&sup2; / n₁) + (s₂&sup2; / n₂) ]</code><br><br>"
        "<b>3. Z-Test for Single Proportion:</b>"
        "<br>Tests whether an observed sample proportion (p = x/n) differs significantly from population proportion (P₀):"
        "<br><code>Z = (p - P₀) / &radic;[ P₀ Q₀ / n ]</code>, where Q₀ = 1 - P₀.<br><br>"
        "<b>4. Z-Test for Difference between Two Proportions:</b>"
        "<br>Tests whether two independent sample proportions (p₁, p₂) differ significantly:"
        "<br><code>Z = (p₁ - p₂) / &radic;[ p&#770; q&#770; (1/n₁ + 1/n₂) ]</code>"
        "<br>where pooled proportion: <code>p&#770; = (x₁ + x₂) / (n₁ + n₂)</code> and <code>q&#770; = 1 - p&#770;</code>."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>The Trade-off Between Type I and Type II Errors:</b><br>"
        "For a fixed sample size n, reducing the probability of Type I error &alpha; (e.g., shifting threshold from 0.05 to 0.001) inevitably widens the acceptance region, thereby <b>increasing the probability of Type II error &beta;</b> and diminishing the statistical power (1 - &beta;) of the trial. "
        "The only mathematically viable method to simultaneously reduce both &alpha; and &beta; (i.e., increase statistical power without increasing false positives) is to <b>increase sample size (n)</b>. "
        "In clinical trials, power analysis ensures that sample size is sufficient to achieve at least 80% power (<code>1 - &beta; &ge; 0.80</code>) at &alpha; = 0.05."
    ),
    "keyPoints": [
        "Null hypothesis (H₀) assumes no genuine difference or treatment effect; Alternative (H₁) is the opposite claim.",
        "Type I error (α) is rejecting true H₀ (False Positive); Level of significance is the probability of Type I error.",
        "Type II error (β) is failing to reject false H₀ (False Negative); Power of test is 1 - β.",
        "Two-tailed critical Z values: ±1.96 at 5% significance level, and ±2.58 at 1% significance level.",
        "One-tailed critical Z values (right-tailed): +1.645 at 5% level, and +2.33 at 1% level.",
        "Z-test requires a large sample size (n ≥ 30) based on the Central Limit Theorem.",
        "Z-statistic for single mean: Z = (X̄ - μ₀) / (s / √n).",
        "Z-statistic for difference of two means: Z = (X̄₁ - X̄₂) / √[ s₁²/n₁ + s₂²/n₂ ].",
        "Z-test for single proportion: Z = (p - P₀) / √[ P₀Q₀ / n ].",
        "Z-test for difference of two proportions uses pooled proportion p̂ = (x₁ + x₂) / (n₁ + n₂).",
        "If |Z_calculated| > Z_critical, the null hypothesis is rejected at that significance level."
    ],
    "clinical": (
        "In a clinical trial testing an anthelmintic against Haemonchus contortus in 100 sheep (sample cure rate p = 92%), the observed rate is compared against the national regulatory standard cure rate (P₀ = 85%). The calculated Z-value of +2.18 exceeds the critical Z of 1.96 (p < 0.05), providing statistically conclusive proof of superior clinical efficacy required for drug licensing."
    ),
    "tables": [
        {
            "title": "Decision Matrix and Error Types in Statistical Hypothesis Testing",
            "headers": ["True Biological Reality", "Null Hypothesis (H₀) Not Rejected", "Null Hypothesis (H₀) Rejected"],
            "rows": [
                ["Null Hypothesis (H₀) is TRUE", "Correct Decision (True Negative)<br>Probability = 1 - &alpha; (Confidence)", "Type I Error (&alpha;) (False Positive)<br>Level of Significance"],
                ["Null Hypothesis (H₀) is FALSE", "Type II Error (&beta;) (False Negative)<br>Consumer's Risk", "Correct Decision (True Positive)<br>Power of Test = 1 - &beta;"]
            ]
        },
        {
            "title": "Critical Values of Z for Large Sample Tests",
            "headers": ["Significance Level (&alpha;)", "Two-Tailed Test Critical |Z|", "One-Tailed Test Critical Z (Right / Left)"],
            "rows": [
                ["10% Level (&alpha; = 0.10)", "1.645", "+1.28 / -1.28"],
                ["5% Level (&alpha; = 0.05)", "1.960", "+1.645 / -1.645"],
                ["1% Level (&alpha; = 0.01)", "2.576 &approx; 2.58", "+2.326 &approx; +2.33 / -2.33"],
                ["0.1% Level (&alpha; = 0.001)", "3.291 &approx; 3.29", "+3.090 / -3.09"]
            ]
        }
    ],
    "img": "",
    "tags": ["hypothesis-testing", "z-test", "type-1-error", "type-2-error", "large-samples", "critical-values"]
}

topics["u1-t16"] = {
    "summary": "Student's t-test is the small-sample parametric test (n < 30) for continuous normal data with unknown population variance, applied as one-sample, independent two-sample, and paired t-tests.",
    "desc": (
        "<b>HISTORICAL BACKGROUND AND THE t-DISTRIBUTION</b><br>"
        "Introduced by William Sealy Gosset (1908) under the pen name <b>'Student'</b> while working as a chemist and brewmaster at the Guinness Brewery. "
        "When sample sizes are small (<code>n &lt; 30</code>) and the true population standard deviation (&sigma;) is unknown and estimated by sample standard deviation (s), the ratio <code>(X&#772; - &mu;) / (s / &radic;n)</code> does not follow a normal distribution. Instead, it follows <b>Student's t-distribution</b> with <code>(n - 1)</code> degrees of freedom.<br><br>"
        "<b>Properties of the t-Distribution:</b>"
        "<ul>"
        "<li>Continuous, symmetrical, bell-shaped curve centered at zero (mean = median = mode = 0).</li>"
        "<li>More spread out with fatter, heavier tails than the standard normal Z-curve (leptokurtic relative to normal, variance &gt; 1: <code>Var(t) = df / (df - 2)</code>).</li>"
        "<li>Its exact shape depends entirely on its <b>Degrees of Freedom (df)</b>. As df &rarr; &infin; (or df &ge; 30), the t-distribution converges asymptotically to the standard normal Z-distribution.</li>"
        "</ul><br>"
        "<b>MANDATORY ASSUMPTIONS OF STUDENT'S t-TEST</b>"
        "<ol>"
        "<li>The parent biological population from which the sample is drawn is normally distributed.</li>"
        "<li>Sample observations are random and mutually independent.</li>"
        "<li>Population variance (&sigma;&sup2;) is unknown.</li>"
        "<li>For two-sample t-tests: Homogeneity of variances (homoscedasticity: <code>&sigma;₁&sup2; = &sigma;₂&sup2;</code>).</li>"
        "</ol><br>"
        "<b>THE THREE VARIANTS OF STUDENT'S t-TEST</b><br>"
        "<b>1. One-Sample t-Test:</b>"
        "<br>Tests whether a small sample mean (X&#772;) differs significantly from a specified standard population mean (&mu;₀):"
        "<br><code>t = (X&#772; - &mu;₀) / (s / &radic;n)</code> with <b>df = n - 1</b>."
        "<br>where <code>s = &radic;[ &sum;(X - X&#772;)&sup2; / (n - 1) ]</code>.<br><br>"
        "<b>2. Two-Sample Independent t-Test (Unpaired t-Test):</b>"
        "<br>Tests whether the means of two independent small biological groups (e.g., Treatment vs Control calves) differ significantly:"
        "<br><code>t = (X&#772;₁ - X&#772;₂) / [ s_p &times; &radic;(1/n₁ + 1/n₂) ]</code> with <b>df = n₁ + n₂ - 2</b>."
        "<br>where <code>s_p&sup2;</code> is the <b>Pooled Sample Variance</b>:"
        "<br><code>s_p&sup2; = [ &sum;(X₁ - X&#772;₁)&sup2; + &sum;(X₂ - X&#772;₂)&sup2; ] / [ n₁ + n₂ - 2 ] = [ (n₁ - 1)s₁&sup2; + (n₂ - 1)s₂&sup2; ] / [ n₁ + n₂ - 2 ]</code>.<br><br>"
        "<b>3. Paired t-Test (Dependent Samples):</b>"
        "<br>Applied when observations are naturally paired, correlated, or matched on the <b>same individual animals</b> (e.g., 'Before-Treatment' versus 'After-Treatment' designs, or twin-lamb pairs):"
        "<br>Calculate individual differences: <code>d_i = X_1i - X_2i</code> (for each of the n pairs)."
        "<br>Calculate mean difference: <code>d&#772; = &sum; d / n</code>."
        "<br>Calculate standard deviation of differences: <code>s_d = &radic;[ &sum;(d - d&#772;)&sup2; / (n - 1) ]</code>."
        "<br>Compute test statistic: "
        "<br><code>t = (d&#772; - 0) / (s_d / &radic;n)</code> with <b>df = n - 1</b> (where n is number of pairs)."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Why Paired t-Test is Statistically Superior in Repeated-Measure Trials:</b><br>"
        "In veterinary medicine, animals exhibit substantial baseline heterogeneity (e.g., resting body temperature or blood urea nitrogen varies across cows). "
        "In an unpaired test, this between-animal biological variation inflates the denominator pooled error variance (s_p&sup2;), masking subtle therapeutic effects. "
        "The <b>paired t-test</b> uses each animal as its own internal control, mathematically eliminating all between-animal biological variability from the error term! "
        "The error variance reflects solely within-animal treatment response differences, drastically reducing error variance and yielding vastly greater statistical power. "
        "<br><br>"
        "<b>Welch's t-Test (Unequal Variances):</b><br>"
        "If the assumption of equal variances is violated (tested via Fisher's F-test, <code>s₁&sup2; / s₂&sup2;</code>), the standard pooled t-test is invalid; <b>Welch's t-test</b> with adjusted Satterthwaite degrees of freedom must be used instead."
    ),
    "keyPoints": [
        "Student's t-test was developed by W.S. Gosset (1908) under the pseudonym 'Student'.",
        "Used for small sample sizes (n < 30) where population variance is unknown.",
        "The t-distribution has fatter tails and higher variance than the normal curve: Var(t) = df / (df - 2).",
        "As degrees of freedom increase (df ≥ 30), the t-distribution approaches the standard normal distribution.",
        "One-sample t-test statistic: t = (X̄ - μ₀) / (s / √n) with df = n - 1.",
        "Independent two-sample t-test compares two treatment groups with pooled variance and df = n₁ + n₂ - 2.",
        "Pooled variance formula: s_p² = [ (n₁ - 1)s₁² + (n₂ - 1)s₂² ] / (n₁ + n₂ - 2).",
        "Paired t-test is used for dependent before-and-after observations on the same animal.",
        "Paired t-test statistic: t = d̄ / (s_d / √n) with df = n - 1 (n = number of pairs).",
        "Paired designs eliminate between-animal biological variation, maximizing experimental precision.",
        "If |t_calculated| > t_tabulated at specified df, the difference is declared statistically significant."
    ],
    "clinical": (
        "To test a new antipyretic drug in calves infected with Theileriosis, rectal temperatures are recorded in 12 calves immediately before injection (Mean = 104.8&deg;F) and 4 hours post-injection (Mean = 101.6&deg;F). The clinician conducts a Paired t-test on the 12 within-calf temperature differences (df = 11), confirming that the antipyretic significantly lowers febrile temperature (p < 0.001)."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Unpaired versus Paired Student's t-Test",
            "headers": ["Parameter", "Independent Two-Sample t-Test", "Paired t-Test"],
            "rows": [
                ["Experimental Design", "Two distinct, unrelated groups of animals (e.g., Group A vs Group B)", "Same animals measured twice ('Before vs After') or identical twin pairs"],
                ["Independence of Groups", "Strictly independent samples", "Strictly dependent, correlated paired observations"],
                ["Sample Size Constraint", "Can have unequal sample sizes (n₁ &ne; n₂)", "Must have equal paired counts (exactly n pairs)"],
                ["Degrees of Freedom", "df = n₁ + n₂ - 2", "df = n - 1 (where n is the number of pairs)"],
                ["Control of Animal Variation", "Between-animal biological variation remains in error term", "Between-animal biological variation is completely eliminated"],
                ["Test Statistic Formula", "t = (X&#772;₁ - X&#772;₂) / [ s_p &times; &radic;(1/n₁ + 1/n₂) ]", "t = d&#772; / (s_d / &radic;n)"]
            ]
        }
    ],
    "img": "",
    "tags": ["students-t-test", "gosset", "paired-t-test", "small-samples", "degrees-of-freedom", "pooled-variance"]
}

topics["u1-t17"] = {
    "summary": "The Chi-Square (χ²) test is a versatile non-parametric test developed by Karl Pearson to test the goodness of fit between observed and theoretical Mendelian genetic ratios and the independence of categorical clinical attributes.",
    "desc": (
        "<b>ORIGIN AND MATHEMATICAL DEFINITION</b><br>"
        "Developed by Karl Pearson (1900). The Chi-Square (<code>&chi;&sup2;</code>) test evaluates discrepancies between <b>Observed Frequencies (O)</b> obtained from biological experiments and <b>Expected Frequencies (E)</b> predicted by theoretical models (such as Mendelian laws or null epidemiological hypotheses):"
        "<br><br>"
        "<code>&chi;&sup2; = &sum; [ (O - E)&sup2; / E ]</code>"
        "<br><br>"
        "where O = observed frequency in each class, E = expected frequency under null hypothesis, and the summation &sum; extends over all categories.<br><br>"
        "<b>PROPERTIES OF THE &chi;&sup2; DISTRIBUTION</b><br>"
        "<ul>"
        "<li>It is a continuous, non-symmetric distribution that begins at 0 and extends to +&infin; (it can <b>never be negative</b> because deviations are squared).</li>"
        "<li>Positively skewed for small degrees of freedom; becomes symmetrical and approaches normality as df &rarr; &infin;.</li>"
        "<li><b>Mean of &chi;&sup2; distribution:</b> <code>Mean = df</code>.</li>"
        "<li><b>Variance of &chi;&sup2; distribution:</b> <code>Variance = 2 &times; df</code>.</li>"
        "<li><b>Additive Property:</b> If &chi;₁&sup2; and &chi;₂&sup2; are independent chi-squares with df₁ and df₂, their sum (&chi;₁&sup2; + &chi;₂&sup2;) is distributed as &chi;&sup2; with <code>df = df₁ + df₂</code>.</li>"
        "</ul><br>"
        "<b>PRIMARY VETERINARY APPLICATIONS</b><br>"
        "<b>1. Test of Goodness of Fit (Testing Genetic Ratios):</b>"
        "<br>Evaluates whether experimental breeding progeny conform to Mendelian expectations (e.g., testing whether F₂ generation fits 3:1, 9:3:3:1, or 1:2:1 ratios). "
        "<br><i>Degrees of Freedom:</i> <code>df = k - 1 - m</code>, where k = number of phenotypic classes, and m = number of population parameters estimated from data. For basic Mendelian ratios, <code>df = k - 1</code>.<br><br>"
        "<b>2. Test of Independence of Attributes (Contingency Tables):</b>"
        "<br>Evaluates whether two qualitative attributes are independent or associated (e.g., whether cattle breed is associated with susceptibility to Mastitis in an r &times; c contingency table). "
        "<br>Expected frequency for cell in row i, column j: <code>E_ij = (Row i Total &times; Column j Total) / Grand Total (N)</code>. "
        "<br><i>Degrees of Freedom:</i> <code>df = (r - 1) &times; (c - 1)</code>, where r = number of rows, c = number of columns.<br><br>"
        "<b>3. 2 &times; 2 Contingency Table Shortcut Formula:</b>"
        "<br>For cells arranged as [a, b / c, d] with total N = a + b + c + d: "
        "<br><code>&chi;&sup2; = [ N &times; (ad - bc)&sup2; ] / [ (a + b)(c + d)(a + c)(b + d) ]</code> with <b>df = 1</b>.<br><br>"
        "<b>CONDITIONS FOR VALIDITY OF THE &chi;&sup2; TEST</b>"
        "<ol>"
        "<li>Total sample size N must be reasonably large (<code>N &ge; 50</code>).</li>"
        "<li>The sample observations must be mutually independent (no animal counted twice).</li>"
        "<li>Data must consist of raw counts/frequencies, <b>never percentages, proportions, or means</b>.</li>"
        "<li><b>Minimum Expected Frequency Rule:</b> No expected frequency (E) in any cell should be less than 5. If E &lt; 5, adjacent classes must be pooled ('pooling of frequencies'), or Yates' correction applied.</li>"
        "</ol><br>"
        "<b>YATES' CORRECTION FOR CONTINUITY (FOR 2 &times; 2 TABLES WITH df = 1)</b><br>"
        "Because &chi;&sup2; is a continuous distribution while contingency table frequencies are discrete integers, Frank Yates (1934) proved that when df = 1, the test statistic is artificially inflated. "
        "Yates' continuity correction subtracts 0.5 from the absolute deviation <code>|O - E|</code> before squaring: "
        "<br><code>&chi;&sup2;_corrected = &sum; [ (|O - E| - 0.5)&sup2; / E ] = [ N (|ad - bc| - 0.5N)&sup2; ] / [ (a+b)(c+d)(a+c)(b+d) ]</code>."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Degrees of Freedom Logic in Contingency Tables:</b><br>"
        "Why is df for an r &times; c contingency table exactly <code>(r - 1)(c - 1)</code>? "
        "In an r &times; c table with fixed marginal row totals and column totals, once you freely assign frequencies to (r - 1) rows and (c - 1) columns, the remaining cells are completely fixed and determined mathematically by the row and column sums. "
        "Hence, the system has exactly <code>(r - 1) &times; (c - 1)</code> free, unconstrained mathematical values. "
        "<br><br>"
        "<b>Fisher's Exact Test:</b><br>"
        "When sample sizes in a 2 &times; 2 table are very small (N &lt; 20, or any expected cell E &lt; 5 even after attempted pooling), Chi-square with Yates' correction becomes unreliable. "
        "<b>Fisher's Exact Test</b> computes exact hypergeometric probabilities: <code>P = [(a+b)! (c+d)! (a+c)! (b+d)!] / [N! a! b! c! d!]</code>, bypassing asymptotic approximations completely."
    ),
    "keyPoints": [
        "Chi-Square (χ²) test was developed by Karl Pearson (1900) for categorical frequency data.",
        "Chi-square formula: χ² = Σ [ (O - E)² / E ].",
        "Chi-square values can never be negative (ranges from 0 to +∞).",
        "Mean of the χ² distribution equals its degrees of freedom: Mean = df.",
        "Variance of the χ² distribution equals twice its degrees of freedom: Variance = 2 · df.",
        "For Mendelian goodness of fit tests across k phenotypic classes: df = k - 1.",
        "In an r × c contingency table testing independence: df = (r - 1)(c - 1).",
        "Expected frequency formula: E = (Row Total × Column Total) / Grand Total (N).",
        "Conditions: Total sample N ≥ 50, independent counts (not percentages), and no expected cell frequency E < 5.",
        "Yates' correction for continuity is mandatory for 2 × 2 tables with df = 1 when frequencies are small.",
        "Yates' correction subtracts 0.5 from the absolute difference: (|O - E| - 0.5)² / E.",
        "Fisher's Exact Test is the exact non-parametric method for 2 × 2 tables when sample sizes are too small for χ²."
    ],
    "clinical": (
        "In a clinical cross-sectional study of 200 dairy cattle evaluating Bovine Mastitis resistance across breeds (Sahiwal vs Holstein-Friesian crossbreds), cases are categorized in a 2 &times; 2 table. The calculated &chi;&sup2; statistic is 14.82 (df = 1, p &lt; 0.001), statistically demonstrating that mastitis incidence is highly breed-dependent, with indigenous Sahiwal showing significant resistance."
    ),
    "tables": [
        {
            "title": "Applications of Chi-Square Test in Animal Genetics and Veterinary Medicine",
            "headers": ["Type of Application", "Degrees of Freedom Formula", "Veterinary / Genetic Field Example"],
            "rows": [
                ["Mendelian Goodness of Fit", "df = k - 1 (k = number of phenotypic classes)", "Testing dihybrid F₂ progeny for 9:3:3:1 segregation ratio"],
                ["Test of Independence of Attributes", "df = (r - 1) &times; (c - 1)", "Testing association between cattle breed and Brucellosis sero-positivity"],
                ["Test of Homogeneity", "df = (r - 1) &times; (c - 1)", "Testing if vaccination efficacy rate is homogeneous across 4 districts"],
                ["Linkage Detection", "df = 1 (in backcross/testcross data)", "Testing parental vs recombinant phenotypic combinations for gene linkage"]
            ]
        }
    ],
    "img": "",
    "tags": ["chi-square", "goodness-of-fit", "contingency-table", "yates-correction", "pearson", "mendelian-ratios"]
}

topics["u1-t18"] = {
    "summary": "Experimental designs provide structured layouts to control biological variation and minimize experimental error, built upon the three cardinal principles: Replication, Randomization, and Local Control.",
    "desc": (
        "<b>NEED FOR EXPERIMENTAL DESIGN IN ANIMAL RESEARCH</b><br>"
        "Biological experiments on farm livestock are expensive, ethically sensitive, and subject to massive background environmental and individual variation. "
        "The primary purpose of an <b>Experimental Design</b> (formulated by Sir Ronald A. Fisher) is to arrange experimental units and treatments such that the true treatment effects can be measured with maximum precision while minimizing <b>Experimental Error</b> (uncontrolled variation arising from environmental noise and individual animal differences).<br><br>"
        "<b>THE THREE CARDINAL PRINCIPLES OF EXPERIMENTAL DESIGN</b><br>"
        "<ol>"
        "<li><b>Replication:</b>"
        "<br>The repetition of treatments on two or more experimental units (animals). "
        "<br><i>Functions:</i> (a) Provides the only valid mathematical estimate of experimental error variance; (b) Increases precision by reducing standard error of treatment means (<code>SE = s / &radic;r</code>); (c) Enhances broad applicability of findings.</li>"
        "<li><b>Randomization:</b>"
        "<br>The allocation of experimental animals to treatments purely by chance (e.g., lottery method or random number tables). "
        "<br><i>Functions:</i> (a) Eliminates conscious or subconscious researcher selection bias; (b) Ensures that uncontrolled environmental factors affect all treatment groups equally; (c) Validates the core assumption of independence of errors necessary for ANOVA and F-tests.</li>"
        "<li><b>Local Control (Error Control):</b>"
        "<br>The technique of grouping relatively homogeneous animals into blocks (strata) to balance out known sources of extraneous variation. "
        "<br><i>Functions:</i> Partitions out a known source of variation (e.g., age, body weight, parity) from the experimental error variance, reducing the error sum of squares and increasing the F-statistic sensitivity. (Note: Local control is practiced in RBD and LSD, but <b>NOT in CRD</b>).</li>"
        "</ol><br>"
        "<b>1. COMPLETELY RANDOMIZED DESIGN (CRD)</b><br>"
        "The simplest experimental design, where treatments are assigned to experimental units completely at random across the entire experimental group without any blocking:"
        "<ul>"
        "<li><b>When to Use:</b> When experimental animals are <b>strictly homogeneous</b> in all baseline characteristics (e.g., inbred lab mice of identical age and sex, day-old commercial broiler chicks from the same hatch, or in vitro ruminal culture tubes).</li>"
        "<li><b>Layout & Randomization:</b> If 'v' treatments are to be replicated 'r' times, all <code>N = v &times; r</code> animals are randomized simultaneously.</li>"
        "<li><b>Statistical Model:</b> <code>Y_ij = &mu; + &tau;_i + &epsilon;_ij</code>, where &mu; = general mean, &tau;_i = effect of i-th treatment, &epsilon;_ij = random experimental error ~ NID(0, &sigma;&sup2;).</li>"
        "<li><b>ANOVA Table Partitioning:</b>"
        "<br>&bull; Total df = N - 1"
        "<br>&bull; Treatment df = v - 1"
        "<br>&bull; Error df = N - v = v(r - 1)</li>"
        "<li><b>Merits:</b> Maximum flexibility (any number of treatments and unequal replications); simplest computation; retains maximum degrees of freedom for error.</li>"
        "<li><b>Demerits:</b> Low precision if experimental animals are heterogeneous; extraneous variation directly inflates error variance.</li>"
        "</ul><br>"
        "<b>2. RANDOMIZED BLOCK DESIGN (RBD)</b><br>"
        "The standard design for large livestock trials. The total animal population is partitioned into homogeneous groups called <b>Blocks</b> (or Replications) based on a known extraneous variable (e.g., body weight, parity, initial milk yield). Each block contains all 'v' treatments assigned at random:"
        "<ul>"
        "<li><b>When to Use:</b> When experimental animals exhibit a single gradient of heterogeneity (e.g., 20 dairy cows varying in parity can be grouped into 5 blocks of 4 cows each).</li>"
        "<li><b>Statistical Model:</b> <code>Y_ij = &mu; + &tau;_i + &beta;_j + &epsilon;_ij</code>, where &beta;_j = effect of j-th block.</li>"
        "<li><b>ANOVA Table Partitioning:</b>"
        "<br>&bull; Total df = vr - 1"
        "<br>&bull; Block (Replication) df = r - 1"
        "<br>&bull; Treatment df = v - 1"
        "<br>&bull; Error df = (v - 1)(r - 1)</li>"
        "<li><b>Merits:</b> High precision; partitions out block variance from experimental error; flexible analysis.</li>"
        "<li><b>Demerits:</b> Unsuited if animal numbers per block cannot accommodate all treatments; missing observations complicate analysis.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Efficiency of RBD Relative to CRD:</b><br>"
        "To mathematically prove whether blocking was effective in an animal trial, the <b>Relative Efficiency (RE)</b> of RBD over CRD is computed:"
        "<br><code>RE = [ (r - 1) MS_Block + r(v - 1) MS_Error ] / [ (vr - 1) MS_Error ] &times; 100</code>"
        "<br>If <code>RE &gt; 100%</code> (e.g., 145%), blocking was successful, indicating that running the experiment as a CRD would have required 45% more animals to achieve the same statistical precision. "
        "Examiners frequently test: <i>'Which of the three Fisherian principles is omitted in CRD?'</i> <b>Local Control</b> is completely absent in CRD because no blocking is performed."
    ),
    "keyPoints": [
        "Experimental design arranges experimental units to minimize experimental error and measure true treatment effects.",
        "The three Fisherian principles of experimental design are: Replication, Randomization, and Local Control.",
        "Replication provides a valid estimate of experimental error and reduces standard error of means (s / √r).",
        "Randomization eliminates researcher bias and ensures valid, independent error terms for ANOVA.",
        "Local Control groups units into homogeneous blocks to partition out known extraneous variation.",
        "Completely Randomized Design (CRD) utilizes Replication and Randomization, but lacks Local Control.",
        "CRD is strictly suited for homogeneous experimental material (lab mice, broiler chicks, tissue culture).",
        "CRD Error degrees of freedom: df_error = N - v = v(r - 1).",
        "Randomized Block Design (RBD) utilizes all three principles: Replication, Randomization, and Local Control.",
        "RBD partitions total variance into three sources: Blocks, Treatments, and Error.",
        "RBD Error degrees of freedom: df_error = (v - 1)(r - 1).",
        "Relative Efficiency of RBD over CRD mathematically quantifies the precision gained by blocking."
    ],
    "clinical": (
        "In a nutritional growth trial evaluating 4 bypass-fat dietary rations in 20 growing Murrah buffalo calves varying from 120 kg to 240 kg live weight, a Randomized Block Design (RBD) is implemented. Calves are partitioned into 5 weight-matched blocks of 4 calves each. Blocking removes 68% of baseline weight variation from the error term, enabling clear statistical detection of diet effects."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of CRD versus RBD in Livestock Research",
            "headers": ["Design Parameter", "Completely Randomized Design (CRD)", "Randomized Block Design (RBD)"],
            "rows": [
                ["Principles Applied", "Replication and Randomization only (No Local Control)", "All three principles: Replication, Randomization, Local Control"],
                ["Animal Homogeneity Requirement", "Strictly homogeneous experimental units required", "Heterogeneous units allowed (homogeneous within blocks)"],
                ["Blocking / Stratification", "No blocking performed (whole area is one unit)", "Blocked along one gradient of variation (e.g., weight, parity)"],
                ["Unequal Replications Allowed", "Easily accommodates unequal replications per treatment", "Requires equal replications (every treatment present in each block)"],
                ["Error Degrees of Freedom", "df_error = N - v (Higher error df)", "df_error = (v - 1)(r - 1) (Lower error df)"],
                ["Experimental Precision", "Lower precision if animal variability is present", "Higher precision; block variation partitioned out of error"],
                ["Typical Veterinary Application", "In vitro ruminal digestions, day-old broiler battery cages", "Lactating dairy cattle, sheep grazing trials, pig feeding pens"]
            ]
        }
    ],
    "img": "",
    "tags": ["experimental-design", "crd", "rbd", "replication", "randomization", "local-control", "anova-models"]
}

topics["u1-t19"] = {
    "summary": "Analysis of Variance (ANOVA) partitions total biological phenotypic variance into distinct attributable components, employing Snedecor's F-test to establish treatment significance and Critical Difference for mean separation.",
    "desc": (
        "<b>CONCEPT AND HISTORICAL BACKGROUND OF ANOVA</b><br>"
        "Invented by Sir Ronald A. Fisher in the 1920s. In biological research, testing differences between more than two treatment groups (e.g., comparing 4 nutritional rations A, B, C, D) using repeated pairwise t-tests creates massive <b>Type I error inflation</b> (for k = 4, 6 pairwise tests yield an overall false positive rate of <code>1 - (0.95)⁶ &approx; 26.5%</code> instead of 5%). "
        "<b>Analysis of Variance (ANOVA)</b> resolves this by providing an omnibus test that partitions total phenotypic sum of squares into mutually orthogonal components, testing all treatment means simultaneously using <b>Snedecor's F-test</b>.<br><br>"
        "<b>MANDATORY ASSUMPTIONS OF ANOVA</b>"
        "<ol>"
        "<li><b>Normality:</b> The experimental errors (&epsilon;_ij) in the biological population are normally distributed with mean zero.</li>"
        "<li><b>Independence:</b> All experimental errors are mutually independent (ensured by proper randomization).</li>"
        "<li><b>Homoscedasticity (Homogeneity of Variances):</b> All treatment groups have equal error variance: <code>&sigma;₁&sup2; = &sigma;₂&sup2; = ... = &sigma;_k&sup2; = &sigma;&sup2;</code>.</li>"
        "<li><b>Additivity:</b> Treatment effects and block/environmental effects are additive in the linear model.</li>"
        "</ol><br>"
        "<b>ONE-WAY CLASSIFICATION ANOVA (FOR CRD)</b><br>"
        "Total observations N = v &times; r across v treatments with r replications:"
        "<ul>"
        "<li>Correction Factor: <code>CF = (Grand Total G)&sup2; / N</code></li>"
        "<li>Total Sum of Squares: <code>TSS = &sum;&sum; Y_ij&sup2; - CF</code> (df = N - 1)</li>"
        "<li>Treatment Sum of Squares: <code>TrSS = &sum; (T_i&sup2; / r) - CF</code> (df = v - 1)</li>"
        "<li>Error Sum of Squares: <code>ESS = TSS - TrSS</code> (df = N - v)</li>"
        "<li>Mean Sum of Squares: <code>MS_Tr = TrSS / (v - 1)</code> and <code>MS_Error = ESS / (N - v)</code></li>"
        "<li><b>F-Test Statistic:</b> <code>F_cal = MS_Tr / MS_Error</code> with df = (v - 1, N - v).</li>"
        "</ul><br>"
        "<b>TWO-WAY CLASSIFICATION ANOVA (FOR RBD)</b><br>"
        "Total observations N = v &times; r across v treatments and r blocks:"
        "<ul>"
        "<li>Block Sum of Squares: <code>BSS = &sum; (B_j&sup2; / v) - CF</code> (df = r - 1)</li>"
        "<li>Treatment Sum of Squares: <code>TrSS = &sum; (T_i&sup2; / r) - CF</code> (df = v - 1)</li>"
        "<li>Error Sum of Squares: <code>ESS = TSS - BSS - TrSS</code> (df = (v - 1)(r - 1))</li>"
        "<li><b>F-Test for Treatments:</b> <code>F_Tr = MS_Tr / MS_Error</code> with df = [v - 1, (v - 1)(r - 1)].</li>"
        "<li><b>F-Test for Blocks:</b> <code>F_Block = MS_Block / MS_Error</code> with df = [r - 1, (v - 1)(r - 1)].</li>"
        "</ul><br>"
        "<b>CRITICAL DIFFERENCE (CD / LEAST SIGNIFICANT DIFFERENCE - LSD)</b><br>"
        "When the omnibus F-test is statistically significant (p &lt; 0.05), it proves that at least one treatment mean differs from the others, but does not indicate <i>which specific pairs</i> differ. "
        "Post-hoc pairwise mean comparisons are conducted using <b>Critical Difference (CD)</b>:"
        "<br><br>"
        "<code>Critical Difference (CD) = Standard Error of Difference (SE_d) &times; t_critical(at error df)</code>"
        "<br><br>"
        "where <code>SE_d = &radic;[ (2 &times; MS_Error) / r ]</code>."
        "<br>If the absolute difference between any two treatment means exceeds CD (<code>|X&#772;_i - X&#772;_j| &gt; CD</code>), the difference between those two treatments is declared statistically significant at that significance level."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Mathematical Foundation of Snedecor's F-Distribution:</b><br>"
        "The F-distribution (named by George Snedecor in honor of Sir Ronald Fisher) is the ratio of two independent chi-square variates divided by their respective degrees of freedom: "
        "<br><code>F = (&chi;₁&sup2; / df₁) / (&chi;₂&sup2; / df₂) = s₁&sup2; / s₂&sup2;</code>. "
        "In ANOVA, under the null hypothesis H₀ (all &tau;_i = 0), <code>Expected Value of MS_Tr = &sigma;&sup2;</code> and <code>Expected Value of MS_Error = &sigma;&sup2;</code>, yielding <code>F &approx; 1.0</code>. "
        "Under the alternative hypothesis H₁, <code>E(MS_Tr) = &sigma;&sup2; + r &sum;&tau;_i&sup2; / (v - 1) &gt; &sigma;&sup2;</code>, driving F significantly greater than 1. "
        "Examiners frequently test: <i>'Why is the F-test in ANOVA always one-tailed (right-tailed)?'</i> "
        "Because treatment effects always <i>inflate</i> the numerator MS_Tr, genuine biological differences can only force F into the extreme right tail (F &gt; 1)."
    ),
    "keyPoints": [
        "ANOVA was developed by Sir R. A. Fisher to test differences among three or more group means simultaneously.",
        "Using multiple pairwise t-tests causes Type I error inflation: α_overall = 1 - (1 - α)ᶜ.",
        "ANOVA partitions total sum of squares into Treatment, Block (if RBD), and Error components.",
        "Assumptions of ANOVA: Normality of errors, Independence, Homoscedasticity, and Additivity.",
        "One-way ANOVA (CRD) partitions TSS into Treatment SS (df = v - 1) and Error SS (df = N - v).",
        "Two-way ANOVA (RBD) partitions TSS into Block SS (r - 1), Treatment SS (v - 1), and Error SS ((v-1)(r-1)).",
        "F-statistic is the ratio of Treatment Mean Square to Error Mean Square: F = MS_Tr / MS_Error.",
        "F-distribution is always right-tailed in ANOVA because treatment effects inflate the numerator.",
        "Under null hypothesis H₀, both MS_Tr and MS_Error estimate the same population error variance (σ²).",
        "When F-test is significant, Critical Difference (CD) is used for pairwise mean separation.",
        "Critical Difference formula: CD = √[ 2 · MS_Error / r ] · t_critical(at error df).",
        "If |X̄_i - X̄_j| > CD, the two treatment means are declared significantly different."
    ],
    "clinical": (
        "In a veterinary pharmacological trial evaluating 4 antidiarrheal herbal formulations (v = 4, r = 6 calves each), one-way ANOVA yields F_cal = 8.42 (p < 0.01). The researcher calculates CD = 1.45 days to normal fecal consistency. Formulations B and C resolve diarrhea in 2.1 days compared to 4.8 days for untreated controls (|Diff| = 2.7 > 1.45), confirming clinical superiority."
    ),
    "tables": [
        {
            "title": "Standard ANOVA Table for Randomized Block Design (RBD)",
            "headers": ["Source of Variation", "Degrees of Freedom (df)", "Sum of Squares (SS)", "Mean Sum of Squares (MS)", "Calculated F-Value (F_cal)"],
            "rows": [
                ["Blocks (Replications)", "r - 1", "BSS", "MS_Block = BSS / (r - 1)", "MS_Block / MS_Error"],
                ["Treatments", "v - 1", "TrSS", "MS_Tr = TrSS / (v - 1)", "MS_Tr / MS_Error (Key Test)"],
                ["Experimental Error", "(v - 1)(r - 1)", "ESS", "MS_Error = ESS / [(v-1)(r-1)]", "Denominator baseline"],
                ["Total", "vr - 1", "TSS", "—", "—"]
            ]
        }
    ],
    "img": "",
    "tags": ["anova", "f-test", "snedecor", "critical-difference", "mean-square", "least-significant-difference"]
}

topics["u1-t20"] = {
    "summary": "Non-parametric (distribution-free) tests evaluate biological hypotheses without requiring normality or variance homogeneity, using rank-based methods for ordinal veterinary scores and skewed distributions.",
    "desc": (
        "<b>CONCEPT OF NON-PARAMETRIC (DISTRIBUTION-FREE) TESTS</b><br>"
        "Standard statistical tests (Z-test, Student's t-test, ANOVA) are <b>parametric tests</b>: they assume that sample data are drawn from a specified parent distribution (usually Normal) with defined parameters (&mu;, &sigma;&sup2;) and require variance homogeneity. "
        "In veterinary clinical medicine, however, datasets frequently violate these assumptions: somatic cell counts, parasite egg counts (EPG), lameness locomotion scores (1 to 5), pain scores, and antibody titers exhibit extreme skewness, heavy tails, or ordinal categorical ranking. "
        "<b>Non-Parametric Tests</b> (distribution-free tests) make no assumptions regarding the mathematical form or parameters of the parent population distribution.<br><br>"
        "<b>ADVANTAGES AND DISADVANTAGES OF NON-PARAMETRIC TESTS</b><br>"
        "<b>Advantages:</b>"
        "<ul>"
        "<li>Wide applicability: valid regardless of the shape of the underlying population distribution.</li>"
        "<li>Ideal for ordinal, ranked, or qualitative clinical scoring data (e.g., body condition score, degree of dehydration).</li>"
        "<li>Computations are simple, intuitive, and rely primarily on ranking orders.</li>"
        "<li>Completely immune to distortion by extreme outlier values.</li>"
        "</ul>"
        "<b>Disadvantages:</b>"
        "<ul>"
        "<li>Lower statistical power-efficiency (approx. 90–95%) compared to parametric tests when normality assumptions actually hold true (greater risk of Type II error).</li>"
        "<li>Discards precise metric information by reducing exact numerical values into simple ranks.</li>"
        "<li>Cannot test complex higher-order factorial interactions as elegantly as parametric ANOVA.</li>"
        "</ul><br>"
        "<b>MAJOR NON-PARAMETRIC TESTS IN VETERINARY RESEARCH</b><br>"
        "<ol>"
        "<li><b>Sign Test:</b>"
        "<br>The simplest non-parametric test. Evaluates paired 'Before vs After' qualitative responses by converting raw differences into binary signs: positive (+) or negative (-), ignoring zero ties. Tests H₀: P(+) = P(-) = 0.5 using the Binomial distribution.</li>"
        "<li><b>Wilcoxon Signed-Rank Test (Non-Parametric Paired Test):</b>"
        "<br>The non-parametric analog of the <b>Paired t-test</b>. In addition to the direction of difference (sign), it incorporates the <i>magnitude</i> of differences by ranking absolute differences <code>|d_i|</code> from smallest to largest and assigning original algebraic signs to ranks. "
        "The test statistic <code>T</code> is the smaller sum of like-signed ranks.</li>"
        "<li><b>Mann-Whitney U-Test (Wilcoxon Rank-Sum Test):</b>"
        "<br>The non-parametric analog of the <b>Independent Two-Sample t-test</b>. Tests whether two independent biological groups differ in median. All observations from both groups are combined, ranked jointly from 1 to N, and rank sums (R₁, R₂) computed: "
        "<br><code>U₁ = n₁n₂ + [n₁(n₁+1)/2] - R₁</code> and <code>U₂ = n₁n₂ + [n₂(n₂+1)/2] - R₂</code>. "
        "Test statistic: <code>U = min(U₁, U₂)</code>.</li>"
        "<li><b>Kruskal-Wallis One-Way ANOVA by Ranks (H-Test):</b>"
        "<br>The non-parametric analog of <b>One-Way ANOVA (CRD)</b> for comparing three or more independent groups: "
        "<br><code>H = [ 12 / (N(N+1)) ] &times; &sum; (R_i&sup2; / n_i) - 3(N + 1)</code>"
        "<br>where H follows a Chi-square distribution with <code>df = k - 1</code>.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Asymptotic Relative Efficiency (ARE):</b><br>"
        "The power of a non-parametric test relative to its parametric counterpart is measured by Asymptotic Relative Efficiency (ARE). "
        "Under perfect normality: "
        "<br>&bull; Mann-Whitney U-test has an ARE of <code>3/&pi; &approx; 95.5%</code> relative to the independent Student's t-test. "
        "<br>&bull; Wilcoxon Signed-Rank test has an ARE of <code>&approx; 95.5%</code> relative to the paired t-test. "
        "<br>However, when the parent biological distribution deviates from normality (e.g., Cauchy or exponential distributions common in parasitology), the ARE of the Mann-Whitney test frequently exceeds 100% (often 120–150%), meaning the non-parametric test is actually <b>more powerful</b> than Student's t-test when data are skewed or contain heavy biological outliers."
    ),
    "keyPoints": [
        "Non-parametric tests make no assumptions about the shape or parameters of the parent distribution.",
        "Ideal for ordinal veterinary scores (lameness scores, body condition scores, pain indexes).",
        "Sign Test evaluates paired directional changes using binary (+, -) signs and Binomial distribution.",
        "Wilcoxon Signed-Rank test is the non-parametric counterpart of the Paired Student's t-test.",
        "Wilcoxon Signed-Rank test ranks absolute differences and sums positive and negative ranks.",
        "Mann-Whitney U-test is the non-parametric counterpart of the Independent Two-Sample t-test.",
        "Mann-Whitney U combines and ranks all observations, testing whether one group has higher median values.",
        "Kruskal-Wallis H-test is the non-parametric counterpart of One-Way ANOVA for comparing ≥ 3 groups.",
        "Kruskal-Wallis H statistic follows a Chi-square distribution with df = k - 1.",
        "Non-parametric tests have ~95.5% efficiency under normal conditions, but outperform parametric tests on skewed data."
    ],
    "clinical": (
        "In equine clinical practice evaluating an intra-articular analgesic for osteoarthritis, 10 horses are evaluated on an ordinal AAEP lameness score (0 = sound to 5 = non-weight bearing) before and after therapy. Because lameness scores are ordinal integers with non-normal distribution, the clinician correctly uses the Wilcoxon Signed-Rank test, demonstrating significant pain reduction (p < 0.01)."
    ),
    "tables": [
        {
            "title": "Direct Equivalents: Parametric versus Non-Parametric Statistical Tests",
            "headers": ["Biological Research Design", "Parametric Test (Normal Data)", "Non-Parametric Equivalent (Distribution-Free)"],
            "rows": [
                ["One Sample vs Standard Median", "One-Sample Student's t-test", "Wilcoxon Signed-Rank Test for Single Median"],
                ["Two Dependent Samples (Before/After)", "Paired Student's t-test", "Wilcoxon Signed-Rank Test / Sign Test"],
                ["Two Independent Treatment Groups", "Independent Two-Sample t-test", "Mann-Whitney U-Test (Wilcoxon Rank-Sum)"],
                ["Three or More Independent Groups", "One-Way ANOVA (F-test in CRD)", "Kruskal-Wallis One-Way ANOVA by Ranks (H-test)"],
                ["Bivariate Association / Correlation", "Pearson's Product-Moment (r)", "Spearman's Rank Correlation (&rho;)"]
            ]
        }
    ],
    "img": "",
    "tags": ["non-parametric", "distribution-free", "mann-whitney", "wilcoxon", "kruskal-wallis", "sign-test"]
}

topics["u1-t21"] = {
    "summary": "Computer applications, programming languages, and Database Management Systems (DBMS) form the computational backbone for processing large-scale pedigree, performance, and genomic herd data in modern animal breeding.",
    "desc": (
        "<b>EVOLUTION AND CLASSIFICATION OF PROGRAMMING LANGUAGES</b><br>"
        "Modern animal breeding and veterinary genomics depend on computational power to process millions of animal pedigree records and SNP genotypes. Programming languages provide the structured syntax to command computer hardware:"
        "<ul>"
        "<li><b>Machine Language (First Generation - 1GL):</b> Low-level language composed strictly of binary digits (0s and 1s). Directly executed by CPU hardware without translation; machine-dependent, tedious, and prone to error.</li>"
        "<li><b>Assembly Language (Second Generation - 2GL):</b> Uses alphanumeric mnemonic operation codes (e.g., <code>MOV, ADD, SUB, JMP</code>) instead of binary strings. Requires an <b>Assembler</b> to translate into machine code.</li>"
        "<li><b>High-Level Languages (Third Generation - 3GL):</b> English-like syntax and mathematical notations independent of CPU hardware. Requires a <b>Compiler</b> (translates entire source code at once into object code) or an <b>Interpreter</b> (translates and executes line by line). "
        "<br>&bull; <i>Historical:</i> FORTRAN (Formula Translation - pioneer scientific language widely used in classical animal breeding BLUP software like PEST and VCE), COBOL, BASIC, C, C++. "
        "<br>&bull; <i>Modern 4GL / Scientific:</i> Python, R, SAS, and SQL, now dominant in genomic selection, biostatistics, and bioinformatics.</li>"
        "</ul><br>"
        "<b>SYSTEM SOFTWARE VERSUS APPLICATION SOFTWARE</b><br>"
        "<ul>"
        "<li><b>System Software:</b> Manages computer hardware resources and provides a platform for application software. Includes Operating Systems (Windows, Linux, macOS), device drivers, and system utilities.</li>"
        "<li><b>Application Software:</b> Programs designed to perform specific user-oriented tasks (e.g., MS-Word, MS-Excel, herd management software, bioinformatics packages).</li>"
        "</ul><br>"
        "<b>DATABASE MANAGEMENT SYSTEMS (DBMS)</b><br>"
        "A <b>Database</b> is an organized, integrated collection of logically related data records stored electronically. "
        "A <b>Database Management System (DBMS)</b> is the system software that enables users to define, create, maintain, query, and control access to the database (e.g., Oracle, MySQL, Microsoft SQL Server, PostgreSQL, MS-Access).<br><br>"
        "<b>ADVANTAGES OF DBMS OVER TRADITIONAL FLAT FILE SYSTEMS</b>"
        "<ol>"
        "<li><b>Elimination of Data Redundancy:</b> In flat files, animal details are duplicated across multiple spreadsheets; DBMS centralizes data, eliminating duplication.</li>"
        "<li><b>Data Consistency and Integrity:</b> Updates in one module instantly reflect across the entire system; prevents conflicting records (e.g., an animal marked dead in health records cannot show active milk records).</li>"
        "<li><b>Data Independence:</b> Separation of physical storage structure from logical application software.</li>"
        "<li><b>Concurrent Access and Multi-User Security:</b> Multiple veterinarians and farm managers can access herd records simultaneously with defined access permissions.</li>"
        "<li><b>Data Security, Backup, and Recovery:</b> Automated transaction logging prevents data loss during hardware crashes.</li>"
        "</ol><br>"
        "<b>RELATIONAL DATABASE MANAGEMENT SYSTEM (RDBMS) AND SQL</b><br>"
        "Introduced by E. F. Codd (1970). Data are organized into two-dimensional tables called <b>Relations</b> consisting of <b>Tuples (rows)</b> and <b>Attributes (columns)</b>:"
        "<ul>"
        "<li><b>Primary Key:</b> A unique attribute that unequivocally identifies each record in a table (e.g., <code>Animal_Ear_Tag_No</code> or <code>RFID_UID</code>).</li>"
        "<li><b>Foreign Key:</b> An attribute in one table that links to the primary key of another table, establishing referential integrity (e.g., <code>Sire_ID</code> in a Calf table linking to <code>Bull_ID</code> in the Bull Registry).</li>"
        "<li><b>Structured Query Language (SQL):</b> The universal standard language used to interact with RDBMS: "
        "<br>&bull; <i>DDL (Data Definition Language):</i> <code>CREATE, ALTER, DROP</code>."
        "<br>&bull; <i>DML (Data Manipulation Language):</i> <code>SELECT, INSERT, UPDATE, DELETE</code>. "
        "<br><i>Example Query:</i> <code>SELECT Tag_No, Milk_Yield FROM Cows WHERE Breed = 'Sahiwal' AND Lactation_Yield &gt; 3000;</code></li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Database Normalization in Livestock Information Systems:</b><br>"
        "Normalization is the mathematical process of decomposing complex table structures to eliminate data anomalies (insertion, deletion, and update anomalies):"
        "<ul>"
        "<li><b>First Normal Form (1NF):</b> Every attribute contains strictly atomic (indivisible) values; no repeating groups.</li>"
        "<li><b>Second Normal Form (2NF):</b> Meets 1NF, and all non-key attributes are fully functionally dependent on the entire primary key (eliminates partial dependency).</li>"
        "<li><b>Third Normal Form (3NF):</b> Meets 2NF, and no non-key attribute is transitively dependent on the primary key (<code>X &rarr; Y &rarr; Z</code> eliminated).</li>"
        "</ul>"
        "In modern veterinary national databases like INAPH (Information Network for Animal Productivity and Health) developed by NDDB, strict 3NF ensures that millions of lactation records, ear tag numbers, artificial inseminations, and vaccination certificates are updated with zero referential corruption."
    ),
    "keyPoints": [
        "Machine language (1GL) is binary code (0s and 1s) directly executed by CPU hardware.",
        "Assembly language (2GL) uses mnemonic operation codes and requires an Assembler.",
        "High-level languages (3GL) use English-like mathematical syntax (C, Python, R, FORTRAN).",
        "A Compiler translates an entire high-level source program into machine code at once.",
        "An Interpreter translates and executes high-level source code line-by-line.",
        "DBMS eliminates data redundancy, enforces data integrity, and enables concurrent multi-user access.",
        "In an RDBMS, data are organized into relations (tables) with tuples (rows) and attributes (columns).",
        "A Primary Key uniquely identifies each row in a database table (e.g., Unique Ear Tag ID).",
        "A Foreign Key links a table to the primary key of another table, establishing relationships.",
        "SQL (Structured Query Language) is the standard language for relational database operations.",
        "Core SQL commands include SELECT (query), INSERT (add), UPDATE (modify), and DELETE (remove).",
        "Database normalization (1NF, 2NF, 3NF) systematically eliminates data anomalies and redundancies."
    ],
    "clinical": (
        "India's national digital livestock platform, INAPH (Information Network for Animal Productivity and Health) by NDDB, operates on an enterprise RDBMS. Each animal is tracked via an 8-character unique RFID polyurethane ear tag (primary key), linking pedigree, breeding, AI records, milk recording, and Brucellosis/FMD vaccination histories across 100+ million cattle and buffaloes."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Traditional Flat Files versus Database Management Systems (DBMS)",
            "headers": ["System Criterion", "Traditional Flat File System (Excel / Text)", "Database Management System (DBMS)"],
            "rows": [
                ["Data Redundancy", "Extensive duplication of animal records across separate files", "Centralized storage eliminates duplicate records"],
                ["Data Inconsistency", "High; updating one file leaves older files with stale data", "Zero; single update propagates across all related tables instantly"],
                ["Data Access and Querying", "Tedious manual searching or complex macro programming", "Fast, powerful ad-hoc querying using Structured Query Language (SQL)"],
                ["Data Security & Concurrency", "Poor; single file lock blocks multi-user field entries", "Robust multi-level role-based permissions and concurrent multi-user entry"],
                ["Data Integrity Constraints", "No automated validation; invalid records easily saved", "Automated foreign key constraints prevent invalid or dangling records"]
            ]
        }
    ],
    "img": "",
    "tags": ["dbms", "rdbms", "sql", "programming-languages", "primary-key", "normalization", "inaph"]
}

topics["u1-t22"] = {
    "summary": "MS-Office applications, particularly MS-Excel's Data Analysis ToolPak, provide powerful computational and graphical environments for statistical data analysis, herd records management, and telecommunications in veterinary practice.",
    "desc": (
        "<b>MS-OFFICE SUITE IN VETERINARY PRACTICE AND RESEARCH</b><br>"
        "Microsoft Office provides an integrated suite of desktop applications tailored for clinical documentation, scientific presentation, and biological computation:"
        "<ul>"
        "<li><b>MS-Word:</b> Word processing software used by veterinarians to author clinical case reports, surgical discharge summaries, post-mortem protocols, disease investigation bulletins, and scientific research manuscripts. Supports formatting, tables, references, and template macros.</li>"
        "<li><b>MS-PowerPoint:</b> Presentation graphics software used to present clinical findings, epidemiology outbreak seminars, and genetic improvement strategies. Incorporates photographic lesion documentation, animated diagrams, and video microscopy feeds.</li>"
        "<li><b>MS-Access:</b> Desktop relational database system used for small-to-medium veterinary clinical practice management (patient records, drug inventory, billing, vaccination alerts).</li>"
        "<li><b>MS-Excel:</b> The premier spreadsheet application for compiling, organizing, analyzing, and visualizing biological and livestock experimental data.</li>"
        "</ul><br>"
        "<b>MS-EXCEL ARCHITECTURE AND SPREADSHEET ESSENTIALS</b><br>"
        "An Excel file is a <b>Workbook</b> containing individual <b>Worksheets</b>. A worksheet is a grid of 1,048,576 rows (numbered 1, 2, 3...) and 16,384 columns (lettered A, B, ... Z, AA... XFD). "
        "The intersection of a row and a column is a <b>Cell</b>, identified by its unique cell coordinate (e.g., <code>B4</code>).<br>"
        "<b>Types of Cell Referencing:</b>"
        "<ul>"
        "<li><b>Relative Referencing (e.g., <code>A1</code>):</b> Cell reference changes automatically when the formula is copied to another cell.</li>"
        "<li><b>Absolute Referencing (e.g., <code>$A$1</code>):</b> Dollar signs ($) lock the column and row. Reference remains strictly fixed when copied elsewhere. Crucial when multiplying an entire column of milk yields by a single fat price constant cell.</li>"
        "<li><b>Mixed Referencing (e.g., <code>$A1</code> or <code>A$1</code>):</b> Either the row or column is locked while the other remains relative.</li>"
        "</ul><br>"
        "<b>CORE STATISTICAL FORMULAS IN MS-EXCEL</b><br>"
        "All Excel formulas must begin with an equals sign (<code>=</code>):"
        "<ul>"
        "<li><code>=AVERAGE(A1:A50)</code> &mdash; Computes Arithmetic Mean.</li>"
        "<li><code>=MEDIAN(A1:A50)</code> &mdash; Computes Median.</li>"
        "<li><code>=MODE.SNGL(A1:A50)</code> &mdash; Identifies Mode.</li>"
        "<li><code>=STDEV.S(A1:A50)</code> &mdash; Computes sample Standard Deviation (with n-1 divisor).</li>"
        "<li><code>=VAR.S(A1:A50)</code> &mdash; Computes sample Variance (s²).</li>"
        "<li><code>=CORREL(A1:A50, B1:B50)</code> &mdash; Computes Pearson's Correlation Coefficient (r).</li>"
        "<li><code>=SLOPE(B1:B50, A1:A50)</code> &mdash; Computes Linear Regression slope (b_yx).</li>"
        "<li><code>=INTERCEPT(B1:B50, A1:A50)</code> &mdash; Computes Y-intercept (a).</li>"
        "<li><code>=T.TEST(array1, array2, tails, type)</code> &mdash; Computes Student's t-test p-value (Type: 1=Paired, 2=Two-sample equal variance, 3=Two-sample unequal variance).</li>"
        "<li><code>=CHISQ.TEST(actual_range, expected_range)</code> &mdash; Computes Chi-square p-value.</li>"
        "</ul><br>"
        "<b>EXCEL DATA ANALYSIS TOOLPAK</b><br>"
        "An Excel Add-In that automates comprehensive statistical data analysis:"
        "<ul>"
        "<li><b>Descriptive Statistics:</b> Generates a summary table containing Mean, Standard Error, Median, Mode, Standard Deviation, Sample Variance, Kurtosis, Skewness, Range, Minimum, Maximum, and 95% Confidence Level in one click.</li>"
        "<li><b>Anova: Single Factor:</b> Computes one-way ANOVA table with between-groups and within-groups SS, MS, F-calculated, and exact P-value.</li>"
        "<li><b>Anova: Two-Factor Without Replication:</b> Computes two-way ANOVA table for Randomized Block Designs (RBD).</li>"
        "<li><b>Regression:</b> Fits linear regression models, outputting R², Multiple R, ANOVA table, regression coefficients, standard errors, t-statistics, and P-values.</li>"
        "</ul><br>"
        "<b>COMPUTER NETWORKS, INTERNET, AND E-MAIL IN VETERINARY SCIENCE</b><br>"
        "<ul>"
        "<li><b>Computer Networks:</b> Interconnected computing devices sharing data and resources. Classified by geographical scope: <b>LAN</b> (Local Area Network, within a hospital or clinic), <b>MAN</b> (Metropolitan Area Network), and <b>WAN</b> (Wide Area Network, global like the Internet).</li>"
        "<li><b>Internet & Web Technologies:</b> Global decentralized network operating on TCP/IP protocols. Facilitates tele-veterinary consultations, remote diagnostic image sharing (PACS/DICOM), access to digital biomedical libraries (PubMed, NCBI, IVRI repository).</li>"
        "<li><b>E-Mail Protocols:</b> <b>SMTP</b> (Simple Mail Transfer Protocol) for sending mail; <b>POP3</b> (Post Office Protocol) and <b>IMAP</b> (Internet Message Access Protocol) for retrieving messages from remote mail servers.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Algorithmic Precision and Limitations in Excel:</b><br>"
        "In earlier versions of Excel, variance algorithms utilized a single-pass computational formula <code>&sum;X&sup2; - (&sum;X)&sup2;/n</code>, which suffered catastrophic cancellation errors when analyzing large numbers with tiny variances (common in genomic marker positions). "
        "Modern Excel utilizes a numerically stable two-pass updating algorithm for <code>STDEV.S</code>. "
        "However, for massive genetic datasets exceeding 1,048,576 rows or requiring complex mixed-model REML estimation for BLUP breeding values, Excel reaches memory limits, necessitating hand-off to dedicated biometrical genetics engines like R, SAS, or Python (Pandas/SciPy)."
    ),
    "keyPoints": [
        "MS-Word handles veterinary clinical documentation, post-mortem reports, and scientific manuscripts.",
        "MS-Excel is the primary spreadsheet tool for compiling, summarizing, and analyzing biological data.",
        "Excel worksheet grid contains 1,048,576 rows and 16,384 columns.",
        "Relative cell referencing (A1) changes when copied; Absolute referencing ($A$1) remains locked.",
        "Common Excel formulas: =AVERAGE (Mean), =MEDIAN (Median), =MODE.SNGL (Mode), =STDEV.S (Sample SD).",
        "=T.TEST executes Student's t-test; Type 1 represents Paired t-test, Type 2 represents Two-Sample t-test.",
        "Data Analysis ToolPak provides automated one-click Descriptive Statistics, ANOVA, and Regression analysis.",
        "Computer networks are classified by scale: LAN (Local Area), MAN (Metropolitan), WAN (Wide Area).",
        "The Internet runs on standard TCP/IP networking protocols.",
        "E-mail relies on SMTP for sending messages, and POP3/IMAP for retrieving messages from mail servers.",
        "Tele-veterinary medicine utilizes WAN networks for remote clinical ultrasound and radiographic diagnosis."
    ],
    "clinical": (
        "In modern commercial broiler operations, daily flock performance records (mortality, feed intake, water consumption, room temperature) are compiled in MS-Excel. By executing =AVERAGE, =STDEV.S, and plotting daily FCR charts with trendlines, the production manager instantly detects deviations from the Ross 308 breed standard, identifying ventilation or feed-mill formulation failures within 24 hours."
    ),
    "tables": [
        {
            "title": "Essential Statistical Functions in Microsoft Excel for Veterinary Research",
            "headers": ["Statistical Analysis", "Excel Formula Syntax", "Biological / Veterinary Output"],
            "rows": [
                ["Sample Mean", "=AVERAGE(range)", "Calculates the arithmetic mean of biological measurements"],
                ["Sample Standard Deviation", "=STDEV.S(range)", "Calculates sample standard deviation using (n - 1) divisor"],
                ["Sample Variance", "=VAR.S(range)", "Calculates sample variance (s&sup2;) with Bessel's correction"],
                ["Pearson Correlation", "=CORREL(array1, array2)", "Calculates Pearson correlation coefficient (r) between two traits"],
                ["Student's t-Test", "=T.TEST(array1, array2, tails, type)", "Calculates exact two-tailed or one-tailed t-test P-value"],
                ["Chi-Square Test", "=CHISQ.TEST(actual, expected)", "Calculates exact Pearson Chi-square goodness-of-fit P-value"]
            ]
        }
    ],
    "img": "",
    "tags": ["ms-excel", "ms-office", "data-analysis-toolpak", "statistical-formulas", "cell-referencing", "networking"]
}
