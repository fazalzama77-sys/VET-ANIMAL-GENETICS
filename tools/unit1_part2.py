# -*- coding: utf-8 -*-
"""
Unit 1 - Part 2: Topics u1-t09 to u1-t14
Biostatistics & Computer Application (IVRI Undergrad 10 CGPA Standard)
"""

topics = {}

topics["u1-t09"] = {
    "summary": "Probability theory provides mathematical models for quantifying uncertainty and predicting the likelihood of random biological events, governed by the classical addition and multiplication theorems.",
    "desc": (
        "<b>FUNDAMENTAL TERMINOLOGY IN PROBABILITY THEORY</b><br>"
        "In biological and veterinary research, events cannot be predicted with absolute certainty due to stochastic physiological processes:"
        "<ul>"
        "<li><b>Random Experiment:</b> An experiment whose outcomes cannot be predicted with certainty in advance, but the totality of all possible outcomes is completely known (e.g., breeding two heterozygous polled cattle <code>Pp &times; Pp</code>).</li>"
        "<li><b>Sample Space (S):</b> The set of all possible exhaustive outcomes of a random experiment. In Mendelian dihybrid inheritance, <code>S = {9 A_B_, 3 A_bb, 3 aaB_, 1 aabb}</code> (total 16 gametic combinations).</li>"
        "<li><b>Event (E):</b> A defined sub-set of the sample space (e.g., event of obtaining a horned calf, <code>pp</code>).</li>"
        "<li><b>Mutually Exclusive Events:</b> Two or more events that cannot possibly happen simultaneously in a single trial (i.e., <code>P(A &cap; B) = 0</code>). (e.g., A newborn calf cannot be simultaneously male and female).</li>"
        "<li><b>Independent Events:</b> The occurrence or non-occurrence of event A has absolutely no influence on the probability of occurrence of event B (i.e., <code>P(A &cap; B) = P(A) &times; P(B)</code>). (e.g., The sex of a cow's first calf does not influence the sex of her second calf).</li>"
        "<li><b>Exhaustive Events:</b> The totality of events considers all possible outcomes such that at least one is guaranteed to occur (sum of probabilities = 1).</li>"
        "</ul><br>"
        "<b>DEFINITIONS OF PROBABILITY</b><br>"
        "<ul>"
        "<li><b>Classical (A Priori / Mathematical) Definition:</b> If a trial can result in <code>n</code> mutually exclusive, equally likely, and exhaustive outcomes, and <code>m</code> of them are favorable to event E, then: "
        "<br><code>P(E) = m / n</code> (where 0 &le; P(E) &le; 1).</li>"
        "<li><b>Empirical (Relative Frequency / A Posteriori) Definition:</b> If an experiment is repeated N times under identical conditions, and event E occurs f times: "
        "<br><code>P(E) = lim (N &rarr; &infin;) [f / N]</code>. (e.g., determining the field conception rate of semen doses).</li>"
        "<li><b>Axiomatic Definition (Kolmogorov, 1933):</b> Probability P is a real-valued function satisfying: "
        "<br>1. Non-negativity: <code>P(A) &ge; 0</code>"
        "<br>2. Total certainty: <code>P(S) = 1</code>"
        "<br>3. Countable additivity for mutually disjoint sets: <code>P(A &cup; B) = P(A) + P(B)</code>.</li>"
        "</ul><br>"
        "<b>THE TWO FUNDAMENTAL THEOREMS OF PROBABILITY</b><br>"
        "<b>1. Addition Theorem (Total Probability):</b>"
        "<ul>"
        "<li><i>For Mutually Exclusive Events:</i> If A and B cannot occur together: "
        "<br><code>P(A &cup; B) = P(A or B) = P(A) + P(B)</code>. "
        "<br><i>Livestock Example:</i> In a cross of <code>Aa &times; Aa</code>, probability of obtaining a homozygous dominant (<code>AA</code>, p=1/4) OR a homozygous recessive (<code>aa</code>, p=1/4) is: 1/4 + 1/4 = 2/4 = 0.50.</li>"
        "<li><i>For Non-Mutually Exclusive Events:</i> If A and B can occur simultaneously: "
        "<br><code>P(A &cup; B) = P(A) + P(B) - P(A &cap; B)</code>, where <code>P(A &cap; B)</code> is the joint probability.</li>"
        "</ul><br>"
        "<b>2. Multiplication Theorem (Compound Probability):</b>"
        "<ul>"
        "<li><i>For Independent Events:</i> If occurrence of A does not affect B: "
        "<br><code>P(A &cap; B) = P(A and B) = P(A) &times; P(B)</code>. "
        "<br><i>Livestock Example:</i> Probability of a cow delivering three consecutive female calves: <code>(1/2) &times; (1/2) &times; (1/2) = 1/8 = 0.125</code>.</li>"
        "<li><i>For Dependent Events (Conditional Probability):</i> "
        "<br><code>P(A &cap; B) = P(A) &times; P(B|A)</code>, where <code>P(B|A)</code> is the conditional probability of event B occurring given that event A has already occurred: <code>P(B|A) = P(A &cap; B) / P(A)</code>.</li>"
        "</ul><br>"
        "<b>BAYES' THEOREM (INVERSE PROBABILITY)</b><br>"
        "Used in veterinary diagnostics to calculate the predictive value of a test: <code>P(Disease|Positive Test) = [P(Positive|Disease) &times; P(Disease)] / P(Positive Test)</code>."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "In veterinary diagnostics, Bayes' Theorem exposes the dramatic impact of <b>disease prevalence</b> on the <b>Positive Predictive Value (PPV)</b> of a diagnostic screening assay. "
        "Even if an ELISA for Bovine Brucellosis boasts 99% sensitivity (true positive rate) and 99% specificity (true negative rate), if the herd disease prevalence is only 0.1% (1 in 1000 cows), the probability that a test-positive cow is truly infected is: "
        "<br><code>PPV = (0.99 &times; 0.001) / [(0.99 &times; 0.001) + (0.01 &times; 0.999)] = 0.00099 / 0.01098 &approx; 9.0%</code>! "
        "Over 90% of test-positive animals are false positives! This mathematical reality proves why high-specificity confirmatory tests (e.g., PCR or Complement Fixation Test) are mandatory before culling valuable pedigree breeding stock."
    ),
    "keyPoints": [
        "A random experiment has known possible outcomes but cannot be predicted with certainty in advance.",
        "Mutually exclusive events cannot occur simultaneously in a single trial: P(A ∩ B) = 0.",
        "Independent events do not influence each other's occurrence: P(A ∩ B) = P(A) × P(B).",
        "Classical probability formula: P(E) = m / n (favorable outcomes / total equally likely outcomes).",
        "Axioms of probability: 0 ≤ P(E) ≤ 1; P(Sample Space) = 1; P(Complement) = 1 - P(E).",
        "Addition Theorem for mutually exclusive events: P(A or B) = P(A) + P(B).",
        "Addition Theorem for non-mutually exclusive events: P(A or B) = P(A) + P(B) - P(A ∩ B).",
        "Multiplication Theorem for independent events: P(A and B) = P(A) × P(B).",
        "Conditional probability formula: P(B|A) = P(A ∩ B) / P(A).",
        "Bayes' Theorem calculates inverse conditional probabilities, determining diagnostic predictive values in veterinary epidemiology."
    ],
    "clinical": (
        "When evaluating a rapid pen-side diagnostic test for Canine Distemper Virus (CDV), applying Bayes' rule demonstrates that testing clinically normal dogs in an area with near-zero prevalence produces an unacceptably high rate of false-positive results, risking unnecessary euthanasia of healthy puppies."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Addition versus Multiplication Theorems",
            "headers": ["Parameter", "Addition Theorem of Probability", "Multiplication Theorem of Probability"],
            "rows": [
                ["Conjunctive Operator", "Expressed by 'OR' (Union: A &cup; B)", "Expressed by 'AND' (Intersection: A &cap; B)"],
                ["Primary Condition", "Events occur alternatively in a single trial", "Events occur together or consecutively across trials"],
                ["Formula (Independent / Mutually Exclusive)", "P(A &cup; B) = P(A) + P(B)", "P(A &cap; B) = P(A) &times; P(B)"],
                ["Adjustment for Joint Occurrence", "Subtract joint probability: - P(A &cap; B)", "Use conditional probability: P(A) &times; P(B|A)"],
                ["Classical Genetics Example", "Probability of an F₂ offspring being AA OR Aa (3/4)", "Probability of obtaining a double recessive aabb (1/4 &times; 1/4 = 1/16)"]
            ]
        }
    ],
    "img": "",
    "tags": ["probability", "addition-theorem", "multiplication-theorem", "bayes-theorem", "mendelian-probability"]
}

topics["u1-t10"] = {
    "summary": "Binomial and Poisson distributions are discrete probability distributions modeling countable biological events, with Binomial applying to repeated independent binary trials and Poisson governing rare biological occurrences.",
    "desc": (
        "<b>1. BINOMIAL DISTRIBUTION (BERNOULLI DISTRIBUTION)</b><br>"
        "Discovered by Swiss mathematician Jakob Bernoulli (1713). It models the number of successes (x) in a fixed number (n) of identical, independent trials where each trial has only two mutually exclusive outcomes: <b>Success (p)</b> and <b>Failure (q = 1 - p)</b>.<br><br>"
        "<b>Conditions / Assumptions for Binomial Distribution:</b>"
        "<ul>"
        "<li>The number of trials (n) is fixed and finite.</li>"
        "<li>Each trial has only two possible outcomes: Success or Failure (e.g., Male vs Female calf; Survived vs Died; Diseased vs Healthy).</li>"
        "<li>The probability of success (p) remains constant from trial to trial.</li>"
        "<li>All trials are mutually independent (the outcome of one trial does not affect any other).</li>"
        "</ul><br>"
        "<b>Probability Mass Function (PMF):</b><br>"
        "<code>P(X = x) = &supn;C_x &times; p^x &times; q^(n - x) = [n! / (x!(n - x)!)] &times; p^x &times; (1 - p)^(n - x)</code>"
        "<br>where x = 0, 1, 2, ..., n.<br><br>"
        "<b>Mathematical Properties of Binomial Distribution:</b>"
        "<ul>"
        "<li><b>Mean:</b> <code>&mu; = n &times; p</code></li>"
        "<li><b>Variance:</b> <code>&sigma;&sup2; = n &times; p &times; q</code></li>"
        "<li><b>Standard Deviation:</b> <code>&sigma; = &radic;(n p q)</code></li>"
        "<li><b>Fundamental Property:</b> In a Binomial distribution, <b>Mean is ALWAYS greater than Variance</b> (since q &lt; 1, <code>np &gt; npq</code>).</li>"
        "<li><b>Shape:</b> Symmetrical if <code>p = q = 0.5</code>; positively skewed if <code>p &lt; 0.5</code>; negatively skewed if <code>p &gt; 0.5</code>.</li>"
        "</ul><br>"
        "<b>2. POISSON DISTRIBUTION</b><br>"
        "Developed by French mathematician Sim&eacute;on Denis Poisson (1837). It is a discrete distribution used for modeling the number of times a <b>rare event</b> occurs within a specified continuum of time, space, volume, or area.<br><br>"
        "<b>Conditions / Assumptions (Poisson as Limiting Case of Binomial):</b>"
        "<ul>"
        "<li>The number of trials is extremely large: <code>n &rarr; &infin;</code>.</li>"
        "<li>The probability of success in any single trial is extremely small (rare event): <code>p &rarr; 0</code>.</li>"
        "<li>The product <code>n &times; p = &lambda;</code> (average rate) remains a finite, positive constant.</li>"
        "<li>Events occur independently at a constant average rate.</li>"
        "</ul><br>"
        "<b>Probability Mass Function (PMF):</b><br>"
        "<code>P(X = x) = (e^(-&lambda;) &times; &lambda;^x) / x!</code>"
        "<br>where x = 0, 1, 2, 3, ... (&infin;); &lambda; is the mean parameter, and e &approx; 2.71828 (base of natural logarithms).<br><br>"
        "<b>Mathematical Properties of Poisson Distribution:</b>"
        "<ul>"
        "<li><b>Mean:</b> <code>&mu; = &lambda;</code></li>"
        "<li><b>Variance:</b> <code>&sigma;&sup2; = &lambda;</code></li>"
        "<li><b>Unique Property:</b> In a Poisson distribution, <b>Mean is EXACTLY EQUAL to Variance</b> (<code>Mean = Variance = &lambda;</code>).</li>"
        "<li><b>Standard Deviation:</b> <code>&sigma; = &radic;&lambda;</code></li>"
        "<li><b>Livestock Applications:</b> Modeling rare veterinary phenomena: number of spontaneous genetic mutations per generation, annual incidence of rabies in a vaccinated county, twinning frequency in dairy cattle herds, count of bacterial colonies per hemocytometer grid square.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Mathematical Proof that Mean = Variance in Poisson:</b><br>"
        "In Binomial distribution: <code>Mean = np</code> and <code>Variance = npq = np(1 - p)</code>. "
        "Taking the Poisson limit where <code>n &rarr; &infin;</code> and <code>p &rarr; 0</code> such that <code>np = &lambda;</code>: "
        "<br><code>Variance = lim(p &rarr; 0) [np(1 - p)] = &lambda; &times; (1 - 0) = &lambda; = Mean</code>. "
        "<br><br>"
        "<b>Index of Dispersion Test for Poisson Fit:</b><br>"
        "To test whether field biological count data conform to a Poisson distribution, the <b>Index of Dispersion (D)</b> is computed: <code>D = s&sup2; / X&#772;</code>. "
        "<br>&bull; If <code>D = 1</code> (s&sup2; &approx; X&#772;): Poisson distribution (random spatial dispersion). "
        "<br>&bull; If <code>D &gt; 1</code> (s&sup2; &gt; X&#772;): Negative binomial distribution (over-dispersion / contagious aggregated clustering, common in tick and worm counts on grazing livestock). "
        "<br>&bull; If <code>D &lt; 1</code> (s&sup2; &lt; X&#772;): Binomial distribution (under-dispersion / uniform spacing)."
    ),
    "keyPoints": [
        "Binomial distribution models the number of successes in n independent binary trials.",
        "Binomial PMF: P(X = x) = ⁿCₓ · pˣ · qⁿ⁻ˣ, where p + q = 1.",
        "Binomial Mean = np; Variance = npq; Standard Deviation = √(npq).",
        "In the Binomial distribution, the Mean is always strictly greater than the Variance (np > npq).",
        "Binomial distribution is perfectly symmetrical when p = 0.5.",
        "Poisson distribution is the limiting form of Binomial distribution when n → ∞, p → 0, and np = λ.",
        "Poisson PMF: P(X = x) = (e⁻ᵞ · λˣ) / x!.",
        "A hallmark property of the Poisson distribution is that Mean equals Variance (Mean = Variance = λ).",
        "Poisson distribution has only a single parameter (λ).",
        "Poisson distribution is universally applied to rare biological events (mutations, twin births in cows, hemocytometer counts)."
    ],
    "clinical": (
        "In a herd of 1,000 dairy cows where the baseline twinning rate is a rare p = 0.004 (&lambda; = 4 twins/year), the herd veterinarian uses the Poisson distribution to calculate the probability of observing &ge; 8 twin births in a single year, detecting whether an experimental superovulation hormone protocol caused unintended iatrogenic twinning."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Binomial versus Poisson Distributions",
            "headers": ["Parameter", "Binomial Distribution", "Poisson Distribution"],
            "rows": [
                ["Nature of Events", "Frequent binary events (Success vs Failure)", "Extremely rare, isolated events over continuous space/time"],
                ["Number of Trials (n)", "Finite and fixed (n is small or moderate)", "Infinitely large (n &rarr; &infin;)"],
                ["Probability of Success (p)", "Substantial and constant across trials", "Infinitesimally small (p &rarr; 0)"],
                ["Number of Parameters", "Two parameters: n and p", "One parameter: &lambda; (&lambda; = np)"],
                ["Mean Formula", "Mean = np", "Mean = &lambda;"],
                ["Variance Formula", "Variance = npq", "Variance = &lambda;"],
                ["Mean vs Variance Relationship", "Mean &gt; Variance (np &gt; npq always)", "Mean = Variance (&lambda; = &lambda; exactly)"],
                ["Livestock Example", "Sex of calves in 10 calvings (p = 0.5)", "Spontaneous lethal dwarfism mutations per 100,000 calves"]
            ]
        }
    ],
    "img": "",
    "tags": ["binomial-distribution", "poisson-distribution", "discrete-distribution", "rare-events", "index-of-dispersion"]
}

topics["u1-t11"] = {
    "summary": "The Normal (Gaussian) distribution is a continuous, bell-shaped, symmetrical probability distribution central to quantitative genetics, defined by its mean and variance and standardized into the Z-distribution.",
    "desc": (
        "<b>HISTORICAL ORIGIN AND VETERINARY IMPORTANCE</b><br>"
        "Discovered by Abraham de Moivre (1733) and independently developed by Carl Friedrich Gauss (1809). "
        "The Normal distribution is the undisputed queen of statistical distributions. "
        "In animal genetics and veterinary science, virtually all economically vital quantitative traits (305-day milk yield, birth weight, weaning weight, carcass dressing percentage, serum enzyme levels) are governed by polygenic inheritance and environmental effects that naturally manifest as a Normal distribution under the Central Limit Theorem.<br><br>"
        "<b>PROBABILITY DENSITY FUNCTION (PDF)</b><br>"
        "The mathematical equation of the normal curve is: "
        "<br><br>"
        "<code>f(X) = [ 1 / (&sigma; &radic;(2&pi;)) ] &times; e^[ - (X - &mu;)&sup2; / (2&sigma;&sup2;) ]</code>"
        "<br><br>"
        "where <code>&mu;</code> = population mean (-&infin; &lt; &mu; &lt; &infin;), <code>&sigma;</code> = population standard deviation (&sigma; &gt; 0), <code>&pi; &approx; 3.14159</code>, <code>e &approx; 2.71828</code>, and X is a continuous random variable (-&infin; &lt; X &lt; &infin;).<br><br>"
        "<b>KEY MATHEMATICAL AND GEOMETRIC PROPERTIES</b><br>"
        "<ol>"
        "<li><b>Perfect Bilateral Symmetry:</b> The curve is completely symmetrical about the vertical ordinate at <code>X = &mu;</code>. Skewness is zero (<code>&beta;₁ = 0, &gamma;₁ = 0</code>).</li>"
        "<li><b>Coincidence of Averages:</b> At the central peak, <b>Mean = Median = Mode = &mu;</b>.</li>"
        "<li><b>Bell-Shaped and Unimodal:</b> Rises smoothly to a single central maximum at <code>X = &mu;</code> where height is <code>1 / (&sigma;&radic;(2&pi;)) &approx; 0.3989 / &sigma;</code>.</li>"
        "<li><b>Asymptotic to the X-Axis:</b> The two tails extend infinitely in both directions, approaching the horizontal X-axis closely but never actually touching it (tangent at infinity).</li>"
        "<li><b>Total Area Under the Curve:</b> The total area beneath the normal curve and above the X-axis is exactly <b>1.00</b> (or 100%). Exactly 50% lies to the left of &mu; and 50% to the right.</li>"
        "<li><b>Points of Inflection:</b> The curve changes from concave downward to convex upward at exact distances of one standard deviation on either side of the mean: <code>X = &mu; &plusmn; &sigma;</code>.</li>"
        "<li><b>Mesokurtic:</b> The kurtosis coefficient is exactly 3 (<code>&beta;₂ = 3</code>, excess kurtosis <code>&gamma;₂ = 0</code>).</li>"
        "<li><b>Linear Combination Property:</b> The sum or difference of independent normally distributed variables is itself normally distributed.</li>"
        "</ol><br>"
        "<b>THE EMPIRICAL (68-95-99.7) AREA RULE</b><br>"
        "The area under the normal curve between defined standard deviation limits is constant across all biological species:"
        "<ul>"
        "<li><code>&mu; &plusmn; 1&sigma;</code> encloses <b>68.27%</b> of all biological observations (approx. 2/3 of the herd).</li>"
        "<li><code>&mu; &plusmn; 1.96&sigma;</code> encloses <b>95.00%</b> of all biological observations (standard 95% clinical reference range).</li>"
        "<li><code>&mu; &plusmn; 2&sigma;</code> encloses <b>95.45%</b> of all biological observations.</li>"
        "<li><code>&mu; &plusmn; 2.58&sigma;</code> encloses <b>99.00%</b> of all biological observations.</li>"
        "<li><code>&mu; &plusmn; 3&sigma;</code> encloses <b>99.73%</b> of all biological observations (virtually the entire population).</li>"
        "</ul><br>"
        "<b>THE STANDARD NORMAL DISTRIBUTION (Z-DISTRIBUTION)</b><br>"
        "To allow calculation of probabilities for any normal distribution without solving complex integration, the raw variable X is transformed into the <b>Standard Normal Variate (Z)</b>:"
        "<br><br>"
        "<code>Z = (X - &mu;) / &sigma;</code>"
        "<br><br>"
        "The standard normal distribution has a <b>Mean of 0</b> and a <b>Variance / Standard Deviation of 1</b>: <code>Z &sim; N(0, 1)</code>. "
        "The standard normal curve has the equation: <code>&phi;(z) = (1 / &radic;(2&pi;)) &times; e^(-z&sup2; / 2)</code>. Probabilities are read directly from Standard Normal Z-tables."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>The Central Limit Theorem (CLT) — The Biological Engine of Normality:</b><br>"
        "The Central Limit Theorem states that if independent random variables X₁, X₂, ..., X_n are drawn from <i>any</i> arbitrary population distribution with mean &mu; and finite variance &sigma;&sup2;, the sampling distribution of their sum or mean (X&#772;) approaches a Normal Distribution with mean &mu; and variance &sigma;&sup2;/n as sample size n &rarr; &infin; (typically n &ge; 30). "
        "<br><br>"
        "<b>Why Quantitative Animal Traits are Normally Distributed:</b><br>"
        "A quantitative trait like 305-day milk yield in Sahiwal cows is controlled by hundreds of infinitesimal Mendelian genes (polygenes), each contributing a tiny additive effect (+d or -d), coupled with thousands of micro-environmental factors (feed intake, ruminal digestion efficiency, temperature variations). "
        "By the Central Limit Theorem, the summation of these hundreds of independent genetic and non-genetic forces automatically collapses into a normal Gaussian distribution, providing the theoretical foundation of quantitative genetics."
    ),
    "keyPoints": [
        "Normal distribution is a continuous, bell-shaped, symmetrical probability distribution.",
        "Normal curve is governed by two parameters: Mean (μ) and Standard Deviation (σ).",
        "In a normal curve, Mean = Median = Mode, and Skewness is zero (β₁ = 0).",
        "The curve is unimodal and asymptotic to the horizontal axis (tails never touch the X-axis).",
        "The total area beneath the normal curve is exactly equal to 1.00 (100%).",
        "Points of inflection occur at exactly X = μ ± 1σ.",
        "The kurtosis coefficient of a normal curve is β₂ = 3 (mesokurtic, γ₂ = 0).",
        "Empirical rule: μ ± 1σ contains 68.27%; μ ± 2σ contains 95.45%; μ ± 3σ contains 99.73% of data.",
        "Clinical reference intervals in veterinary pathology are defined by μ ± 1.96σ (95% limits).",
        "Standard Normal Variate formula: Z = (X - μ) / σ, which follows N(0, 1) with Mean = 0 and SD = 1.",
        "Central Limit Theorem explains why polygenic livestock traits exhibit normal distributions."
    ],
    "clinical": (
        "In veterinary clinical pathology, the reference range for serum total calcium in adult Sahiwal cattle is established as 8.5 to 10.5 mg/dL. This range is statistically constructed from a healthy population with &mu; = 9.5 mg/dL and &sigma; = 0.5 mg/dL using the <code>&mu; &plusmn; 1.96&sigma;</code> normal curve boundaries, identifying cows with &lt; 8.5 mg/dL as clinically hypocalcemic."
    ),
    "tables": [
        {
            "title": "Standard Normal Curve Area Percentages Under Defined Z Limits",
            "headers": ["Z-Score Range", "Exact Mathematical Area Covered", "Biological / Examination Interpretation"],
            "rows": [
                ["&mu; &plusmn; 0.6745 &sigma;", "50.00% (0.5000)", "Encloses the exact Interquartile Range (between Q₁ and Q₃)"],
                ["&mu; &plusmn; 1.00 &sigma;", "68.27% (0.6827)", "Approximately two-thirds of the herd population"],
                ["&mu; &plusmn; 1.96 &sigma;", "95.00% (0.9500)", "Exact boundaries for two-tailed 95% clinical reference intervals"],
                ["&mu; &plusmn; 2.00 &sigma;", "95.45% (0.9545)", "Standard two-sigma empirical boundary"],
                ["&mu; &plusmn; 2.58 &sigma;", "99.00% (0.9900)", "Exact boundaries for 99% high-confidence clinical intervals"],
                ["&mu; &plusmn; 3.00 &sigma;", "99.73% (0.9973)", "Three-sigma quality control limit; less than 0.27% outliers fall outside"]
            ]
        }
    ],
    "img": "",
    "tags": ["normal-distribution", "gaussian-curve", "standard-normal-variate", "z-score", "central-limit-theorem", "empirical-rule"]
}

topics["u1-t12"] = {
    "summary": "Correlation analysis measures the direction and strength of mutual linear association between two quantitative biological variables, evaluated through Karl Pearson's coefficient (r) or Spearman's rank coefficient (ρ).",
    "desc": (
        "<b>CONCEPT OF BIVARIATE BIOLOGICAL DATA</b><br>"
        "When two quantitative characteristics are recorded simultaneously on the same individual animal (e.g., heart girth and body weight in Murrah heifers, or age and egg production in layers), the data form a <b>bivariate distribution</b>. "
        "<b>Correlation</b> is the statistical technique used to measure the degree, strength, and direction of the linear relationship between two variables.<br><br>"
        "<b>TYPES OF CORRELATION</b><br>"
        "<ul>"
        "<li><b>Positive (Direct) Correlation:</b> Both variables move in the same direction; an increase in X is associated with an increase in Y (e.g., heart girth and body weight; daily dry matter intake and milk yield).</li>"
        "<li><b>Negative (Inverse) Correlation:</b> Variables move in opposite directions; an increase in X is accompanied by a decrease in Y (e.g., ambient heat stress temperature and milk yield; lactation milk yield and milk fat percentage).</li>"
        "<li><b>Zero / No Correlation:</b> No systematic linear relationship exists (e.g., coat color shade and lactation length).</li>"
        "<li><b>Linear versus Non-Linear (Curvilinear) Correlation:</b> Linear if the ratio of change is constant (forms a straight line); non-linear if the ratio of change varies (forms a curved plot).</li>"
        "</ul><br>"
        "<b>METHODS OF STUDYING CORRELATION</b><br>"
        "<b>1. Scatter Diagram Method:</b>"
        "<br>A visual graphical plot of paired (X, Y) points on Cartesian coordinates. "
        "<br>&bull; If points form a tight upward band from lower-left to upper-right: Strong Positive Correlation."
        "<br>&bull; If points form a downward band from upper-left to lower-right: Strong Negative Correlation."
        "<br>&bull; If points form a diffuse, circular cloud: Zero Correlation.<br><br>"
        "<b>2. Karl Pearson's Product-Moment Correlation Coefficient (r):</b>"
        "<br>The standard mathematical measure of linear association for continuous quantitative data: "
        "<br><br>"
        "<code>r = Cov(X, Y) / [ &sigma;_x &times; &sigma;_y ] = [ &sum;(X - X&#772;)(Y - Y&#772;) ] / &radic;[ &sum;(X - X&#772;)&sup2; &times; &sum;(Y - Y&#772;)&sup2; ]</code>"
        "<br><br>"
        "<i>Computational Raw-Score Formula:</i>"
        "<br><code>r = [ n &sum;XY - (&sum;X)(&sum;Y) ] / &radic;[ [ n &sum;X&sup2; - (&sum;X)&sup2; ] [ n &sum;Y&sup2; - (&sum;Y)&sup2; ] ]</code>"
        "<br><br>"
        "<b>Properties of Pearson's Correlation Coefficient:</b>"
        "<ul>"
        "<li><b>Strict Range:</b> <code>-1 &le; r &le; +1</code>. (r = +1: perfect positive correlation; r = -1: perfect negative correlation; r = 0: no linear correlation).</li>"
        "<li><b>Pure Number:</b> It is a dimensionless ratio independent of physical units of measurement.</li>"
        "<li><b>Invariance:</b> It is completely independent of change of origin and change of scale: <code>r_xy = r_uv</code> where <code>u = (X - a)/c</code> and <code>v = (Y - b)/d</code> (provided c and d have identical algebraic signs).</li>"
        "<li><b>Symmetry:</b> Correlation between X and Y is identical to correlation between Y and X: <code>r_xy = r_yx</code>.</li>"
        "</ul><br>"
        "<b>3. Spearman's Rank Correlation Coefficient (&rho;):</b>"
        "<br>Developed by Charles Spearman (1904) for qualitative data, ordinal scores, or ranked biological attributes (e.g., breed conformation judging scores, herd temperament ranks):"
        "<br><br>"
        "<code>&rho; = 1 - [ (6 &sum; D&sup2;) / (n(n&sup2; - 1)) ]</code>"
        "<br><br>"
        "where D = difference between paired ranks (<code>R_x - R_y</code>), and n = number of paired animals. "
        "When tied ranks occur, an adjustment factor <code>m(m&sup2; - 1) / 12</code> is added to &sum; D&sup2; for each tie group of size m."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Significance Testing of Correlation Coefficient:</b><br>"
        "To test the null hypothesis H₀: &rho; = 0 (no correlation in population) against H₁: &rho; &ne; 0 using a small sample (n &lt; 30), Student's t-test is applied:"
        "<br><code>t = [ r &times; &radic;(n - 2) ] / &radic;(1 - r&sup2;)</code> with <b>degrees of freedom df = n - 2</b>."
        "<br><br>"
        "<b>Examiner Warning — Correlation does NOT Imply Causation:</b><br>"
        "A high correlation coefficient indicates numerical co-variation, but never proves direct biological cause and effect. "
        "A high correlation may arise from a common underlying third variable (e.g., both milk yield and body weight increase with cow age/parity) or represent complete nonsense/spurious correlation. "
        "Furthermore, <b>Coefficient of Determination (r&sup2;)</b>: represents the exact proportion of total variation in Y that is explained by its linear relationship with X (e.g., if r = 0.80 between heart girth and body weight, <code>r&sup2; = 0.64</code>, meaning 64% of body weight variation is directly explained by heart girth, while 36% remains unexplained residual variation)."
    ),
    "keyPoints": [
        "Correlation measures the strength and direction of mutual linear association between two variables.",
        "Positive correlation means variables move in same direction; negative correlation means opposite directions.",
        "Scatter diagram is a visual plot of paired data points on coordinate axes.",
        "Karl Pearson's coefficient (r) is the covariance divided by the product of individual standard deviations.",
        "The range of Pearson's correlation coefficient is strictly bounded between -1 and +1 (-1 ≤ r ≤ +1).",
        "Pearson's r is independent of both change of origin and change of scale.",
        "Correlation is symmetric: r_xy = r_yx.",
        "Spearman's rank correlation formula: ρ = 1 - [ 6 Σ D² / (n(n² - 1)) ].",
        "Spearman's rank correlation is ideal for ordinal qualitative judging, rankings, and non-normal data.",
        "Test of significance for Pearson's r: t = [ r √(n - 2) ] / √(1 - r²) with df = n - 2.",
        "Coefficient of Determination (r²) represents the proportion of total variation in Y explained by X.",
        "Correlation does not imply biological causation."
    ],
    "clinical": (
        "In field veterinary practice where animal weighbridges are unavailable, Pearson's correlation between chest heart girth (cm) and body weight (kg) in adult Gir cattle is established as r = +0.92 (r² = 0.846). This robust linear association allows the field veterinarian to reliably predict live body weight for calculating accurate anthelmintic and anesthetic dosages."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Pearson's Product-Moment versus Spearman's Rank Correlation",
            "headers": ["Criterion", "Pearson's Correlation (r)", "Spearman's Rank Correlation (&rho;)"],
            "rows": [
                ["Data Type Required", "Continuous quantitative metric data on an interval or ratio scale", "Qualitative ordinal data, ranked scores, or non-normal metric data"],
                ["Underlying Distribution", "Assumes bivariate normal distribution for significance testing", "Distribution-free (non-parametric; requires no normality assumption)"],
                ["Sensitivity to Outliers", "Highly sensitive; single extreme outliers can distort r drastically", "Extremely robust; relies only on relative rank orders"],
                ["Computational Formula", "r = &sum;(X - X&#772;)(Y - Y&#772;) / [ &radic;&sum;(X - X&#772;)&sup2; &radic;&sum;(Y - Y&#772;)&sup2; ]", "&rho; = 1 - [ 6 &sum;D&sup2; / (n(n&sup2; - 1)) ]"],
                ["Veterinary Application", "Heart girth vs body weight; serum calcium vs phosphorus", "Breed show judging scores; herd temperament docility ranking"]
            ]
        }
    ],
    "img": "",
    "tags": ["correlation", "pearson-r", "spearman-rank", "scatter-diagram", "coefficient-of-determination", "bivariate-data"]
}

topics["u1-t13"] = {
    "summary": "Regression analysis estimates the mathematical functional relationship between a dependent outcome variable and an independent predictor, allowing accurate prediction through the principle of least squares.",
    "desc": (
        "<b>CONCEPT OF REGRESSION ANALYSIS</b><br>"
        "The term <i>Regression</i> (meaning 'stepping back' or 'returning') was coined by Sir Francis Galton (1877) in his classic study on the inheritance of seed size and human stature, observing that tall parents produce offspring who tend to 'regress' toward the general population mean. "
        "While correlation merely measures the strength of association between two variables, <b>Regression</b> models the mathematical functional relationship, designating one variable as the <b>Independent variable (Predictor / Regressor, X)</b> and the other as the <b>Dependent variable (Response / Outcome, Y)</b> to allow prediction of unknown Y from known X.<br><br>"
        "<b>THE PRINCIPLE OF LEAST SQUARES</b><br>"
        "The line of best fit through bivariate data points is mathematically determined such that the sum of the squared vertical deviations of the observed points from the fitted line is a minimum: <code>&sum;(Y - &Ycirc;)&sup2; = Minimum</code>.<br><br>"
        "<b>THE TWO LINEAR REGRESSION EQUATIONS</b><br>"
        "For any bivariate distribution, two distinct regression lines exist:"
        "<ul>"
        "<li><b>Regression Line of Y on X:</b> Used to estimate/predict Y for a given value of X: "
        "<br><code>Y - Y&#772; = b_yx (X - X&#772;)</code> &nbsp;&rArr;&nbsp; <code>Y = a + b_yx &times; X</code>"
        "<br>where <code>b_yx</code> is the regression coefficient of Y on X, and <code>a = Y&#772; - b_yx X&#772;</code> is the Y-intercept.</li>"
        "<li><b>Regression Line of X on Y:</b> Used to estimate/predict X for a given value of Y: "
        "<br><code>X - X&#772; = b_xy (Y - Y&#772;)</code> &nbsp;&rArr;&nbsp; <code>X = a' + b_xy &times; Y</code>"
        "<br>where <code>b_xy</code> is the regression coefficient of X on Y.</li>"
        "</ul><br>"
        "<b>REGRESSION COEFFICIENTS AND THEIR MATHEMATICAL FORMULAS</b><br>"
        "The regression coefficient <code>b_yx</code> measures the expected change in dependent variable Y per unit change in independent variable X (the slope of the line):"
        "<ul>"
        "<li><code>b_yx = Cov(X, Y) / Var(X) = [ &sum;(X - X&#772;)(Y - Y&#772;) ] / &sum;(X - X&#772;)&sup2;</code></li>"
        "<li><code>b_xy = Cov(X, Y) / Var(Y) = [ &sum;(X - X&#772;)(Y - Y&#772;) ] / &sum;(Y - Y&#772;)&sup2;</code></li>"
        "<li><i>Relationship with Correlation Coefficient (r):</i>"
        "<br><code>b_yx = r &times; (&sigma;_y / &sigma;_x)</code> &nbsp;&nbsp;and&nbsp;&nbsp; <code>b_xy = r &times; (&sigma;_x / &sigma;_y)</code></li>"
        "</ul><br>"
        "<b>CRITICAL MATHEMATICAL PROPERTIES OF REGRESSION COEFFICIENTS</b><br>"
        "<ol>"
        "<li><b>Geometric Mean Property:</b> The correlation coefficient (r) is the geometric mean of the two regression coefficients: "
        "<br><code>r = &plusmn; &radic;(b_yx &times; b_xy)</code>.</li>"
        "<li><b>Identical Signs Property:</b> Both regression coefficients (b_yx, b_xy) and the correlation coefficient (r) must have the <b>exact same algebraic sign</b> (all positive or all negative). If b_yx is negative, b_xy and r must be negative.</li>"
        "<li><b>Magnitude Limitation:</b> If one regression coefficient is greater than 1 (in absolute value), the other must be less than 1 (since <code>b_yx &times; b_xy = r&sup2; &le; 1</code>).</li>"
        "<li><b>Arithmetic Mean Property:</b> The arithmetic mean of the two regression coefficients is greater than or equal to the correlation coefficient: <code>(b_yx + b_xy) / 2 &ge; r</code>.</li>"
        "<li><b>Scale and Origin Property:</b> Regression coefficients are independent of change of origin, but <b>dependent on change of scale</b>.</li>"
        "<li><b>Intersection of Regression Lines:</b> The two regression lines always intersect at the point of their means: <code>(X&#772;, Y&#772;)</code>.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Why are there TWO Regression Lines?</b><br>"
        "Examiners frequently ask why a single bivariate dataset yields two different regression lines instead of one. "
        "The line of Y on X minimizes the sum of squared <i>vertical</i> residuals: <code>&sum;(Y - &Ycirc;)&sup2;</code> (assuming X is measured without error). "
        "The line of X on Y minimizes the sum of squared <i>horizontal</i> residuals: <code>&sum;(X - X&circ;)&sup2;</code> (assuming Y is measured without error). "
        "<br>&bull; If <code>r = &plusmn; 1</code> (perfect correlation): the two regression lines coincide into a single identical line."
        "<br>&bull; If <code>r = 0</code> (zero correlation): the two regression lines are completely perpendicular (90&deg; angle), intersecting at <code>(X&#772;, Y&#772;)</code> parallel to the X and Y axes. "
        "<br>The angle &theta; between the two regression lines is given by: <code>tan &theta; = [(1 - r&sup2;) / |r|] &times; [ &sigma;_x &sigma;_y / (&sigma;_x&sup2; + &sigma;_y&sup2;) ]</code>."
    ),
    "keyPoints": [
        "Regression was introduced by Sir Francis Galton to study the inheritance of stature regressing to the mean.",
        "Regression models the directional dependency of variable Y on independent predictor X.",
        "The Principle of Least Squares minimizes the sum of squared residuals: Σ(Y - Ŷ)² = Minimum.",
        "Regression equation of Y on X: Y - Ȳ = b_yx (X - X̄).",
        "Regression coefficient formula: b_yx = Cov(X, Y) / Var(X) = r · (σ_y / σ_x).",
        "Correlation coefficient is the geometric mean of the two regression coefficients: r = ± √(b_yx · b_xy).",
        "Both regression coefficients and the correlation coefficient always share the identical algebraic sign.",
        "If b_yx > 1, then b_xy must be < 1 because their product r² cannot exceed 1.",
        "The arithmetic mean of the two regression coefficients is always greater than or equal to r: (b_yx + b_xy) / 2 ≥ r.",
        "The two regression lines always intersect at the coordinate point of their means (X̄, Ȳ).",
        "If r = ±1, the two regression lines coincide; if r = 0, the two regression lines are perpendicular.",
        "In animal breeding, parent-offspring regression (b_OP) directly estimates narrow-sense heritability (h² = 2 b_OP)."
    ],
    "clinical": (
        "In field dairy development, Shaeffer's formula represents a practical empirical regression equation predicting body weight in kg from heart girth (H in inches) and body length (L in inches): <code>Body Weight (lbs) = (H&sup2; &times; L) / 300</code>. This least-squares regression model provides the field veterinarian with immediate dose calculations for general anesthesia without transport to a cattle scale."
    ),
    "tables": [
        {
            "title": "Comprehensive Distinction between Correlation and Regression",
            "headers": ["Criterion", "Correlation Analysis", "Regression Analysis"],
            "rows": [
                ["Fundamental Purpose", "Measures the degree and direction of mutual linear co-association", "Estimates the mathematical functional dependence and predicts unknown values"],
                ["Variable Roles", "Symmetrical; no distinction between dependent and independent variables", "Asymmetrical; clear distinction between Independent (X) and Dependent (Y)"],
                ["Symmetry of Metric", "Symmetric: r_xy = r_yx", "Asymmetric: b_yx &ne; b_xy (different slopes unless &sigma;_x = &sigma;_y)"],
                ["Measurement Units", "Dimensionless pure number (no units)", "Expressed in physical ratio units (units of Y per unit of X)"],
                ["Change of Scale", "Independent of both change of origin and change of scale", "Independent of change of origin, but strictly dependent on change of scale"],
                ["Range of Values", "Strictly bounded between -1.00 and +1.00", "Unbounded; can assume any real value from -&infin; to +&infin;"]
            ]
        }
    ],
    "img": "",
    "tags": ["regression", "least-squares", "regression-coefficient", "prediction", "galton", "slope-intercept"]
}

topics["u1-t14"] = {
    "summary": "Sampling methods define rigorous statistical protocols for selecting representative subsets from animal populations, categorized into probability sampling (random, stratified, systematic, cluster) and non-probability sampling designs.",
    "desc": (
        "<b>CENSUS VERSUS SAMPLE SURVEY IN VETERINARY SCIENCE</b><br>"
        "A <b>Census</b> involves the complete enumeration of every individual unit in the entire population (e.g., the official 5-yearly All India Livestock Census). While it provides absolute counts, a census demands massive financial resources, vast manpower, prolonged time, and remains vulnerable to non-sampling errors. "
        "A <b>Sample Survey</b> evaluates a scientifically selected representative sub-set. It saves time, lowers costs, allows intensive measurements (e.g., blood biochemistry, milk component analysis), and yields known margins of sampling error.<br><br>"
        "<b>LAWS UNDERLYING SAMPLING THEORY</b><br>"
        "<ul>"
        "<li><b>Law of Statistical Regularity:</b> A moderately large sample chosen at random from a population will, on average, possess the characteristics and parameters of the parent population.</li>"
        "<li><b>Law of Inertia of Large Numbers:</b> Other things being equal, larger samples exhibit greater stability, consistency, and lesser sampling variability than smaller samples.</li>"
        "</ul><br>"
        "<b>PROBABILITY SAMPLING METHODS (RANDOM SAMPLING)</b><br>"
        "Every unit in the population has a known, non-zero probability of inclusion in the sample, eliminating investigator selection bias:<br>"
        "<ol>"
        "<li><b>Simple Random Sampling (SRS):</b>"
        "<br>Every unit in the population has an equal and independent chance of being selected."
        "<br>&bull; <i>SRS Without Replacement (SRSWOR):</i> Selected unit is not returned to population before drawing the next (standard in animal studies; probability = 1/N, 1/(N-1)...). Higher statistical precision."
        "<br>&bull; <i>SRS With Replacement (SRSWR):</i> Selected unit is returned to the pool (probability remains 1/N)."
        "<br>&bull; <i>Selection Techniques:</i> Lottery method or Tippett's Random Number Tables / computer pseudo-random generators.</li>"
        "<li><b>Stratified Random Sampling:</b>"
        "<br>Used when the parent population is heterogeneous. The population of size N is divided into non-overlapping homogeneous sub-populations called <b>strata</b> (e.g., stratifying cattle by breed: Sahiwal, Gir, Crossbred; or by lactation stage: early, mid, late). A random sample is then drawn independently from each stratum."
        "<br>&bull; <i>Proportional Allocation:</i> Sample size from each stratum is proportional to stratum size: <code>n_i = n &times; (N_i / N)</code>."
        "<br>&bull; <i>Optimum (Neyman) Allocation:</i> Sample size accounts for both stratum size and within-stratum standard deviation (&sigma;_i): <code>n_i &prop; N_i &sigma;_i</code>. Most precise sampling method in biological research.</li>"
        "<li><b>Systematic Sampling (Quasi-Random Sampling):</b>"
        "<br>Units are selected at equal numerical intervals from an ordered sampling frame. "
        "Calculate sampling interval: <code>k = N / n</code>. Select the first unit (r) randomly between 1 and k. Subsequent units are: <code>r, r+k, r+2k, r+3k, ...</code>. "
        "(e.g., inspecting every 10th sheep entering a dipping vat or every 5th carcass on a slaughterhouse conveyor line). <i>Risk:</i> Periodic hidden cycles matching k create severe sampling bias.</li>"
        "<li><b>Cluster Sampling:</b>"
        "<br>Used when a complete list of individual animals is unavailable, but animals naturally group into clusters (e.g., villages, herds, poultry houses). The clusters (not individual animals) are randomly sampled, and <b>every animal within selected clusters</b> is examined. Cost-effective for field epidemiology over wide geographical terrains.</li>"
        "<li><b>Multi-Stage Sampling:</b> Sampling carried out in successive stages (e.g., Stage 1: Districts &rarr; Stage 2: Tehsils &rarr; Stage 3: Villages &rarr; Stage 4: Individual livestock holdings).</li>"
        "</ol><br>"
        "<b>NON-PROBABILITY SAMPLING METHODS</b><br>"
        "Subject to investigator bias; sampling error cannot be mathematically computed:"
        "<ul>"
        "<li><b>Purposive (Judgment) Sampling:</b> Units deliberately chosen based on the researcher's clinical judgment.</li>"
        "<li><b>Convenience (Accidental) Sampling:</b> Units selected simply because they are easily accessible (e.g., sampling only animals brought to an IVRI clinic).</li>"
        "<li><b>Quota Sampling:</b> Non-random stratified quota filling based on convenience.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Mathematical Proof of Efficiency in Stratified Sampling:</b><br>"
        "In sampling theory, comparing the variances of the sample mean under different designs demonstrates the mathematical hierarchy of precision: "
        "<br><code>Var(X&#772;)_opt &le; Var(X&#772;)_prop &le; Var(X&#772;)_srs</code>. "
        "<br>Stratified random sampling with optimum allocation achieves the lowest possible sampling variance because it eliminates <b>between-strata variation</b> from the sampling error, leaving only within-strata variation. "
        "Stratification is most effective when variance <i>between</i> strata is maximized (heterogeneous strata), while variance <i>within</i> each stratum is minimized (homogeneous units within strata)."
    ),
    "keyPoints": [
        "A census investigates all population units; a sample survey examines a scientifically chosen representative sub-set.",
        "Law of Statistical Regularity states a random sample reflects the parent population characteristics on average.",
        "Law of Inertia of Large Numbers states larger samples exhibit greater stability and smaller sampling error.",
        "Simple Random Sampling gives every population unit an equal and independent chance of selection (1/N).",
        "SRSWOR (without replacement) yields smaller sampling variance and higher precision than SRSWR.",
        "Stratified random sampling divides a heterogeneous population into homogeneous strata before sampling.",
        "In Proportional Allocation, stratum sample size is proportional to stratum size: n_i = n · (N_i / N).",
        "Neyman's Optimum Allocation minimizes sample variance by accounting for stratum variability: n_i ∝ N_i · σ_i.",
        "Systematic sampling selects every k-th unit after a random start between 1 and k (k = N / n).",
        "Cluster sampling randomly selects natural groupings (herds, villages) and tests all animals within them.",
        "Multi-stage sampling selects units through successive hierarchical stages (Districts → Villages → Farms).",
        "Non-probability sampling (convenience, purposive) cannot quantify sampling error or construct confidence intervals."
    ],
    "clinical": (
        "In conducting a state-wide seroprevalence survey for Bovine Viral Diarrhoea (BVD) in Uttar Pradesh, stratified multi-stage cluster sampling is applied: districts form primary strata, villages form secondary clusters, and herds within villages form sampling units. This epidemiological design ensures statistically unbiased prevalence estimation across agro-climatic zones with optimal operational budget."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Probability Sampling Designs",
            "headers": ["Sampling Method", "Structural Design Protocol", "Primary Advantage", "Primary Risk / Limitation"],
            "rows": [
                ["Simple Random (SRS)", "Lottery or random number tables from full list", "Completely unbiased; simplest mathematical theory", "Requires complete exhaustive list (frame) of all animals"],
                ["Stratified Random", "Divide into homogeneous strata; sample each stratum", "Highest precision; guarantees representation of rare breeds", "Requires prior accurate knowledge of stratum characteristics"],
                ["Systematic Sampling", "Select every k-th unit after random start r", "Rapid execution; easy for field technicians in chutes", "Periodic cyclical trends in animal order cause massive bias"],
                ["Cluster Sampling", "Randomly pick whole herds/villages; test all within", "Greatly reduces travel and logistical field expenses", "Higher sampling variance if animals within clusters are alike"]
            ]
        }
    ],
    "img": "",
    "tags": ["sampling-methods", "simple-random-sampling", "stratified-sampling", "cluster-sampling", "systematic-sampling", "neyman-allocation"]
}
