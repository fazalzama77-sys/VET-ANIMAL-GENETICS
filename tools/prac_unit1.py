# -*- coding: utf-8 -*-
"""
Practical Unit 1: Topics p1-t01 to p1-t11
Biostatistics and Computer Application Lab (IVRI Undergrad 10 CGPA Standard)
Strictly exam-specific: Aim, Principle, Formulae, Solved Model Problems, Inferences, Viva-Voce
"""

topics = {}

topics["p1-t01"] = {
    "summary": "Practical exercise on primary and secondary biological data collection, constructing frequency distribution tables using Sturges' rule, and compiling livestock farm records.",
    "desc": (
        "<b>AIM:</b> To collect, compile, classify, and present raw livestock production records into a continuous grouped frequency distribution table.<br><br>"
        "<b>PRINCIPLE & STATISTICAL RULES:</b>"
        "<ul>"
        "<li><b>Range (R):</b> <code>R = X_max - X_min</code> (Difference between highest and lowest observation).</li>"
        "<li><b>Number of Classes (k) — Sturges' Rule:</b> <code>k = 1 + 3.322 &times; log10(N)</code> (where N = total sample size).</li>"
        "<li><b>Class Width / Interval (h or c):</b> <code>h = Range / k</code> (rounded up to a convenient integer).</li>"
        "<li><b>Tally Mark Method:</b> Observations are tallied in bunches of five (four vertical strokes and a diagonal strike) into mutually exclusive class intervals.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM:</b><br>"
        "The following are the daily milk yields (kg) of 30 Sahiwal cows recorded on an organized dairy farm:<br>"
        "<code>8.2, 10.5, 12.0, 7.5, 9.4, 11.2, 13.8, 6.5, 10.0, 8.8, 14.2, 9.0, 11.5, 7.8, 10.8, 12.5, 8.0, 9.6, 13.0, 11.0, 10.2, 8.5, 7.0, 12.2, 9.8, 10.6, 11.8, 6.8, 13.5, 10.4</code>.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><code>X_min = 6.5</code> kg, <code>X_max = 14.2</code> kg.</li>"
        "<li><code>Range = 14.2 - 6.5 = 7.7</code> kg.</li>"
        "<li><code>k = 1 + 3.322 &times; log10(30) = 1 + 3.322(1.4771) = 1 + 4.907 = 5.91 &approx; 6 classes</code>.</li>"
        "<li><code>Class Interval (h) = 7.7 / 6 = 1.28 &approx; 1.5</code> kg (or convenient width of 1.5 or 2.0). Using class width = 1.5 kg with starting class 6.0–7.5.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What is the difference between discrete and continuous frequency distribution?</b><br>"
        "<b>A:</b> Discrete distributions count integer variables without fractional values (e.g., litter size, parity); continuous distributions measure parameters capable of taking any fractional real value within an interval (e.g., milk yield, body weight).</li>"
        "<li><b>Q: What are exclusive vs inclusive class intervals?</b><br>"
        "<b>A:</b> In exclusive intervals (e.g., 6–8, 8–10), the upper limit is excluded and counted in the next class; in inclusive intervals (e.g., 6–7.9, 8–9.9), both limits are included in the same class.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Always verify that <code>&Sigma; f_i = N</code>. Missing a single tally mark leads to immediate marks deduction in practical exams.</li>"
        "<li>Calculate both <b>'Less than'</b> and <b>'More than'</b> cumulative frequencies in your examination table as examiners specifically check for cumulative boundary alignment.</li>"
        "<li>Mid-value formula: <code>x_i = (Lower Limit + Upper Limit) / 2</code>. State mid-values explicitly for use in subsequent mean/SD calculations.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Range is the difference between maximum and minimum values: R = Xmax - Xmin.",
        "Sturges' formula determines optimal class intervals: k = 1 + 3.322 * log10(N).",
        "Class interval width is calculated as: h = Range / k.",
        "Tally marks are grouped in clusters of five (four vertical, one diagonal strike).",
        "Exclusive class intervals (e.g., 10-12, 12-14) are mandatory for continuous biological data.",
        "Class mark (mid-value) is (Lower Limit + Upper Limit) / 2.",
        "Cumulative frequency (cf) is obtained by successive running addition of frequencies.",
        "Total frequency Σf must exactly equal total sample size N.",
        "Frequency density is frequency divided by class width (f / h).",
        "Relative frequency is individual class frequency divided by total sample size (f / N)."
    ],
    "tables": [
        {
            "title": "Grouped Frequency Distribution Table for Sahiwal Daily Milk Yields (N = 30)",
            "headers": ["Parameter / Class Interval (kg)", "Class Mid-Value (x_i)", "Tally Marks", "Frequency (f_i)", "Less-than Cumulative Freq (cf)", "Relative Frequency (f/N)"],
            "rows": [
                ["6.0 – 7.5", "6.75", "||||", "4", "4", "0.133"],
                ["7.5 – 9.0", "8.25", "|||| |", "6", "10", "0.200"],
                ["9.0 – 10.5", "9.75", "|||| ||", "7", "17", "0.233"],
                ["10.5 – 12.0", "11.25", "|||| |", "6", "23", "0.200"],
                ["12.0 – 13.5", "12.75", "||||", "4", "27", "0.133"],
                ["13.5 – 15.0", "14.25", "|||", "3", "30", "0.100"],
                ["Total", "—", "—", "N = 30", "—", "1.000"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "At commercial dairy farms and gaushalas, compilation of daily milking records into grouped frequency tables identifies the herd production profile, "
        "enabling veterinarians to segregate high-yielders (> 12 kg/day) for elite challenge feeding from low-yielders (< 7.5 kg/day) slated for reproductive evaluation."
    ),
    "tags": ["Biostatistics Lab", "Frequency Distribution", "Sturges' Rule", "Tally Marks", "Tabulation", "Sahiwal Milk Yield"]
}

topics["p1-t02"] = {
    "summary": "Construction and graphical presentation of biological data using histograms, frequency polygons, frequency curves, and cumulative ogives to locate partition values.",
    "desc": (
        "<b>AIM:</b> To plot Histogram, Frequency Polygon, and Cumulative Frequency Ogives ('Less-than' and 'More-than') for livestock data and determine median graphically.<br><br>"
        "<b>PRINCIPLES & GRAPHICAL RULES:</b>"
        "<ul>"
        "<li><b>Histogram:</b> Rectangles erected on continuous class boundaries along the X-axis, with height proportional to class frequency (or frequency density if class intervals are unequal).</li>"
        "<li><b>Frequency Polygon:</b> Obtained by joining the midpoints of the tops of histogram rectangles with straight lines, anchored to the X-axis at midpoints of adjacent imaginary zero-frequency classes.</li>"
        "<li><b>Ogives (Cumulative Curves):</b>"
        "<br>&bull; <i>Less-than Ogive:</i> Plot less-than cumulative frequencies against upper class boundaries (S-shaped rising curve)."
        "<br>&bull; <i>More-than Ogive:</i> Plot more-than cumulative frequencies against lower class boundaries (descending curve)."
        "<br>&bull; <i>Graphical Median:</i> The X-coordinate of the point where 'Less-than' and 'More-than' ogives intersect corresponds exactly to the <b>Median</b> (or the value corresponding to <code>N/2</code> on the Y-axis of a single ogive).</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM:</b><br>"
        "From the grouped frequency distribution of Murrah buffalo body weights (kg):<br>"
        "<code>400–450 (f=6), 450–500 (f=14), 500–550 (f=20), 550–600 (f=8), 600–650 (f=2)</code>; Total N = 50.<br>"
        "Plot less-than cumulative frequencies and determine median graphically.<br><br>"
        "<b>STEP-BY-STEP PROCEDURE:</b>"
        "<ol>"
        "<li>Construct Upper Class Boundaries: 450, 500, 550, 600, 650.</li>"
        "<li>Compute Less-than cf: 6, 20, 40, 48, 50.</li>"
        "<li>Calculate <code>N/2 = 50 / 2 = 25</code>.</li>"
        "<li>Locate 25 on the cumulative frequency (Y) axis; project horizontally to intersect the Less-than ogive; drop a vertical line to the X-axis.</li>"
        "<li><b>Result:</b> The vertical drop hits <b>512.5 kg</b> (Median body weight).</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Why cannot a frequency polygon be drawn without class midpoints?</b><br>"
        "<b>A:</b> A frequency polygon requires a single representative coordinate per class; the mathematical centroid of a continuous interval is its midpoint (class mark).</li>"
        "<li><b>Q: How is Mode determined graphically from a Histogram?</b><br>"
        "<b>A:</b> In the modal (tallest) rectangle, draw a line from the top-left corner to the top-left of the next right bar, and from top-right corner to top-right of the next left bar. The intersection point dropped perpendicularly to the X-axis gives the Mode.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Always mention axes labels and scale on graph sheets: e.g., 'X-axis: 1 cm = 50 kg; Y-axis: 1 cm = 5 buffaloes'. Missing scale deducts 1 to 2 marks immediately.</li>"
        "<li>Remember: If class intervals are unequal, histogram heights must represent <b>Frequency Density = Frequency / Class Width</b>, NOT raw frequency.</li>"
        "<li>The intersection of less-than and more-than ogives gives <code>(Median, N/2)</code>. This is a classic 2-mark viva question.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Histograms plot continuous class boundaries on X-axis and frequency on Y-axis.",
        "Adjacent bars in a histogram must touch with zero spacing for continuous variables.",
        "Frequency polygon joins midpoints of histogram tops and anchors to base at both ends.",
        "Less-than ogive plots cumulative frequency against upper class boundaries.",
        "More-than ogive plots cumulative frequency against lower class boundaries.",
        "The intersection point of less-than and more-than ogives yields the exact Median on X-axis.",
        "Mode is located graphically inside the tallest rectangle of a histogram.",
        "For unequal class intervals, bar height must equal frequency density (f / h).",
        "Ogives are sigmoidal (S-shaped) curves used to read quartiles, deciles, and percentiles.",
        "N/2 projected from Y-axis to ogive and dropped to X-axis gives graphical median."
    ],
    "tables": [
        {
            "title": "Cumulative Frequency Table for Ogive Construction in Murrah Buffaloes (N = 50)",
            "headers": ["Parameter / Class Interval", "Lower Boundary", "Upper Boundary", "Frequency (f)", "Less-than cf (Plot on Upper)", "More-than cf (Plot on Lower)"],
            "rows": [
                ["400 – 450 kg", "400", "450", "6", "6", "50"],
                ["450 – 500 kg", "450", "500", "14", "20", "44"],
                ["500 – 550 kg", "500", "550", "20", "40", "30"],
                ["550 – 600 kg", "550", "600", "8", "48", "10"],
                ["600 – 650 kg", "600", "650", "2", "50", "2"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "Veterinarians utilize cumulative frequency ogives in commercial poultry broiler farms to evaluate flock weight uniformity. "
        "Plotting broiler weights against standard breed curves quickly reveals whether the 25th percentile (Q1) or 75th percentile (Q3) deviates, "
        "diagnosing stocking density overcrowding or inadequate feeder space."
    ),
    "tags": ["Biostatistics Lab", "Histogram", "Frequency Polygon", "Ogive", "Median", "Mode", "Graphical Presentation"]
}

topics["p1-t03"] = {
    "summary": "Step-by-step computation of Arithmetic Mean, Median, and Mode for ungrouped and continuous grouped livestock data with model exam solutions.",
    "desc": (
        "<b>AIM:</b> To compute Arithmetic Mean, Median, and Mode from grouped livestock production data using standard biometrical formulas.<br><br>"
        "<b>FORMULAS & CALCULATION RULES:</b>"
        "<ul>"
        "<li><b>Arithmetic Mean (\\bar{X}):</b>"
        "<br>&bull; Direct Method: <code>\\bar{X} = (&Sigma; f_i x_i) / N</code>"
        "<br>&bull; Short-cut (Assumed Mean) Method: <code>\\bar{X} = A + [ (&Sigma; f_i d_i) / N ] &times; h</code>, where <code>d_i = (x_i - A) / h</code>.</li>"
        "<li><b>Median (M_e):</b>"
        "<br>Find Median Class where cumulative frequency <code>cf &ge; N / 2</code>."
        "<br><code>Median = L + [ (N/2 - m) / f ] &times; h</code>"
        "<br>Where: <code>L</code> = Lower limit of median class; <code>m</code> = cumulative frequency of preceding class; <code>f</code> = frequency of median class; <code>h</code> = class width.</li>"
        "<li><b>Mode (M_o):</b>"
        "<br>Identify Modal Class having highest frequency (<code>f_1</code>)."
        "<br><code>Mode = L + [ (f_1 - f_0) / (2 f_1 - f_0 - f_2) ] &times; h</code>"
        "<br>Where: <code>f_0</code> = frequency of preceding class; <code>f_2</code> = frequency of succeeding class.</li>"
        "<li><b>Empirical Relationship:</b> <code>Mode = 3 &times; Median - 2 &times; Mean</code> (for moderately skewed distributions).</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM:</b><br>"
        "Calculate Mean, Median, and Mode for 305-day lactation yields (hundred kg) of 40 crossbred dairy cows:<br>"
        "<code>20–25 (f=5), 25–30 (f=8), 30–35 (f=15), 35–40 (f=8), 40–45 (f=4)</code>; Total N = 40.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><b>Mean:</b> Let assumed mean <code>A = 32.5</code>, <code>h = 5</code>."
        "<br>&Sigma; f_i d_i = 5(-2) + 8(-1) + 15(0) + 8(+1) + 4(+2) = -10 - 8 + 0 + 8 + 8 = -2."
        "<br><code>\\bar{X} = 32.5 + (-2 / 40) &times; 5 = 32.5 - 0.25 = 32.25</code> (i.e. 3,225 kg).</li>"
        "<li><b>Median:</b> <code>N/2 = 40 / 2 = 20</code>. Preceding cf before 30–35 class is 13. Median class = 30–35."
        "<br><code>L = 30, m = 13, f = 15, h = 5</code>."
        "<br><code>Median = 30 + [ (20 - 13) / 15 ] &times; 5 = 30 + (7/15 &times; 5) = 30 + 2.33 = 32.33</code> (3,233 kg).</li>"
        "<li><b>Mode:</b> Modal class = 30–35 (highest f = 15)."
        "<br><code>L = 30, f_1 = 15, f_0 = 8, f_2 = 8, h = 5</code>."
        "<br><code>Mode = 30 + [ (15 - 8) / (2(15) - 8 - 8) ] &times; 5 = 30 + [ 7 / (30 - 16) ] &times; 5 = 30 + (7/14 &times; 5) = 30 + 2.50 = 32.50</code> (3,250 kg).</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Which average is best for skewed biological data like somatic cell counts or parasite egg counts?</b><br>"
        "<b>A:</b> <b>Median</b>, because it is unaffected by extreme outliers.</li>"
        "<li><b>Q: What happens to mean, median, and mode in a perfectly symmetrical normal distribution?</b><br>"
        "<b>A:</b> They are identical and coincide: <code>Mean = Median = Mode</code>.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Check consistency via empirical rule: <code>Mode &approx; 3(32.33) - 2(32.25) = 96.99 - 64.50 = 32.49</code> (matches calculated 32.50 perfectly!). Showing this cross-check in practical answer booklets guarantees full marks.</li>"
        "<li>Always state the units (kg, days, grams). Leaving answers as bare numbers without units loses 0.5 to 1 mark.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Arithmetic mean formula: X̄ = Σ(fi * xi) / N.",
        "Short-cut assumed mean formula: X̄ = A + [Σ(fi * di) / N] * h.",
        "Median class is identified by cumulative frequency cf ≥ N / 2.",
        "Median formula: L + [(N/2 - m) / f] * h.",
        "Modal class is the class with maximum frequency (f1).",
        "Mode formula: L + [(f1 - f0) / (2f1 - f0 - f2)] * h.",
        "Empirical relationship: Mode = 3 * Median - 2 * Mean.",
        "Arithmetic mean is mathematically rigorous but sensitive to extreme outliers.",
        "Median is positional and robust against skewed data.",
        "Mode represents the most frequent and typical observation."
    ],
    "tables": [
        {
            "title": "Computation Table for Mean, Median, and Mode of 305-Day Milk Yield (N = 40)",
            "headers": ["Class Interval (100 kg)", "Mid-value (x_i)", "Frequency (f_i)", "d_i = (x_i - 32.5)/5", "f_i * d_i", "Cumulative Freq (cf)"],
            "rows": [
                ["20 – 25", "22.5", "5", "-2", "-10", "5"],
                ["25 – 30", "27.5", "8", "-1", "-8", "13 (m)"],
                ["30 – 35 (Median/Modal)", "32.5 (A)", "15 (f_1)", "0", "0", "28"],
                ["35 – 40", "37.5", "8 (f_2)", "+1", "+8", "36"],
                ["40 – 45", "42.5", "4", "+2", "+8", "40"],
                ["Total", "—", "N = 40", "—", "&Sigma; f_i d_i = -2", "—"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "When analyzing herd calving-to-conception intervals (days open), a few problem cows with uterine infections take > 300 days to conceive. "
        "The mean is severely inflated by these outliers, making herd fertility look poor. "
        "Veterinarians report the <b>Median Days Open</b> as the true clinical indicator of herd reproductive health."
    ),
    "tags": ["Biostatistics Lab", "Arithmetic Mean", "Median", "Mode", "Central Tendency", "Assumed Mean", "Grouping Method"]
}

topics["p1-t04"] = {
    "summary": "Estimation of Range, Variance, Standard Deviation, Standard Error of Mean, and Coefficient of Variation for livestock phenotypic traits with full model calculation.",
    "desc": (
        "<b>AIM:</b> To calculate Variance (s&sup2;), Standard Deviation (s), Standard Error of Mean (SE_\\bar{x}), and Coefficient of Variation (CV%) from sample livestock records.<br><br>"
        "<b>FORMULAS & EQUATIONS:</b>"
        "<ul>"
        "<li><b>Sample Variance (s&sup2;):</b>"
        "<br><code>s&sup2; = [ &Sigma; x&sup2; - (&Sigma; x)&sup2; / n ] / (n - 1)</code> (Raw data, using Bessel's correction with n-1 degrees of freedom).</li>"
        "<li><b>Grouped Data Variance:</b>"
        "<br><code>s&sup2; = h&sup2; &times; [ { &Sigma; f d&sup2; - (&Sigma; f d)&sup2; / N } / (N - 1) ]</code></li>"
        "<li><b>Standard Deviation (s):</b> <code>s = &radic;(s&sup2;)</code></li>"
        "<li><b>Standard Error of Mean (SE_\\bar{x}):</b> <code>SE_\\bar{x} = s / &radic;n</code></li>"
        "<li><b>Coefficient of Variation (CV%):</b> <code>CV% = (s / \\bar{X}) &times; 100</code></li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM:</b><br>"
        "The body weights (kg) of 8 Beetal kids at 3 months of age were recorded as:<br>"
        "<code>12, 15, 14, 11, 16, 13, 15, 18</code>.<br>"
        "Calculate Mean, Standard Deviation, Standard Error, and CV%.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><code>n = 8</code></li>"
        "<li><code>&Sigma; x = 12 + 15 + 14 + 11 + 16 + 13 + 15 + 18 = 114</code> kg.</li>"
        "<li><code>Mean (\\bar{X}) = 114 / 8 = 14.25</code> kg.</li>"
        "<li><code>&Sigma; x&sup2; = 12&sup2; + 15&sup2; + 14&sup2; + 11&sup2; + 16&sup2; + 13&sup2; + 15&sup2; + 18&sup2; = 144 + 225 + 196 + 121 + 256 + 169 + 225 + 324 = 1660</code>.</li>"
        "<li><code>Correction Factor (CF) = (&Sigma; x)&sup2; / n = (114)&sup2; / 8 = 12996 / 8 = 1624.5</code>.</li>"
        "<li><code>Sum of Squares (SS) = &Sigma; x&sup2; - CF = 1660 - 1624.5 = 35.5</code>.</li>"
        "<li><code>Sample Variance (s&sup2;) = SS / (n - 1) = 35.5 / (8 - 1) = 35.5 / 7 = 5.071</code> kg&sup2;.</li>"
        "<li><code>Standard Deviation (s) = &radic;5.071 = 2.252</code> kg.</li>"
        "<li><code>Standard Error (SE) = s / &radic;n = 2.252 / &radic;8 = 2.252 / 2.828 = 0.796</code> kg.</li>"
        "<li><code>CV% = (2.252 / 14.25) &times; 100 = 15.80%</code>.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Why do we divide by (n - 1) instead of n when computing sample variance?</b><br>"
        "<b>A:</b> Dividing by (n - 1) is <b>Bessel's correction</b>; it provides an <b>unbiased estimate</b> of the true population variance (&sigma;&sup2;) because one degree of freedom is lost estimating the sample mean.</li>"
        "<li><b>Q: What is the biological significance of CV%?</b><br>"
        "<b>A:</b> CV is unitless and allows direct comparison of variability between traits with different units (e.g., comparing variability of body weight in kg vs milk yield in liters).</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Express reporting format: Always write final answer as: <code>Mean &plusmn; SE = 14.25 &plusmn; 0.80 kg (CV = 15.80%)</code>. This is the exact scientific format expected by external examiners.</li>"
        "<li>Remember: Variance has squared units (kg&sup2;), SD has original units (kg), and CV has percentage (%) or no units. Writing wrong units leads to immediate point loss.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Sample variance uses Bessel's correction: s² = SS / (n - 1).",
        "Sum of Squares (SS) formula: SS = Σx² - (Σx)² / n.",
        "Standard deviation is the positive square root of variance: s = √(s²).",
        "Standard error of mean measures sample mean reliability: SE = s / √n.",
        "Coefficient of Variation is relative variability: CV% = (s / X̄) * 100.",
        "CV is dimensionless, enabling comparison of traits measured in different units.",
        "Bessel's correction (n - 1) ensures the sample variance is an unbiased estimator.",
        "Scientific presentation of livestock data: Mean ± SE.",
        "Low CV (< 10%) indicates high flock/herd phenotypic uniformity.",
        "High CV (> 25%) provides abundant additive genetic variance for selection."
    ],
    "tables": [
        {
            "title": "Individual Deviations and Sum of Squares Computation Table (N = 8)",
            "headers": ["Individual Kid No.", "Body Weight x (kg)", "Deviation (x - X̄)", "(x - X̄)²", "Raw Square (x²)"],
            "rows": [
                ["1", "12", "-2.25", "5.0625", "144"],
                ["2", "15", "+0.75", "0.5625", "225"],
                ["3", "14", "-0.25", "0.0625", "196"],
                ["4", "11", "-3.25", "10.5625", "121"],
                ["5", "16", "+1.75", "3.0625", "256"],
                ["6", "13", "-1.25", "1.5625", "169"],
                ["7", "15", "+0.75", "0.5625", "225"],
                ["8", "18", "+3.75", "14.0625", "324"],
                ["Total (&Sigma;)", "114", "0.00", "SS = 35.50", "&Sigma;x² = 1660"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In commercial poultry broiler production, flock uniformity is judged by CV% at 35 days of age. "
        "A <b>CV &le; 8%</b> indicates exceptional flock uniformity, allowing automated processing line slaughter without carcass jamming. "
        "A <b>CV > 14%</b> signals uneven feeding, subclinical coccidiosis, or poor ventilation distribution."
    ),
    "tags": ["Biostatistics Lab", "Standard Deviation", "Variance", "Standard Error", "CV%", "Bessel's Correction", "Sum of Squares"]
}

topics["p1-t05"] = {
    "summary": "Practical numerical problem solving on additive/multiplicative probability rules and finding probabilities under the Standard Normal Curve (Z-distribution).",
    "desc": (
        "<b>AIM:</b> To solve practical numerical problems on livestock probability and compute probabilities of performance traits using Standard Normal Z-tables.<br><br>"
        "<b>CORE PRINCIPLES & FORMULAS:</b>"
        "<ul>"
        "<li><b>Addition Rule:</b> <code>P(A &cup; B) = P(A) + P(B) - P(A &cap; B)</code> (for mutually exclusive events, <code>P(A &cap; B) = 0</code>).</li>"
        "<li><b>Multiplication Rule:</b> <code>P(A &cap; B) = P(A) &times; P(B)</code> (for independent events).</li>"
        "<li><b>Standard Normal Variate (Z):</b>"
        "<br><code>Z = (X - &mu;) / &sigma;</code>"
        "<br>Transforms any normal distribution <code>N(&mu;, &sigma;&sup2;)</code> into standard normal distribution <code>Z ~ N(0, 1)</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (PROBABILITY):</b><br>"
        "A dairy herd has 60% Holstein crossbreds and 40% Jersey crossbreds. The probability of conception at first AI is 0.50 in Holsteins and 0.65 in Jerseys. "
        "If a randomly selected cow is inseminated, find the probability that she conceives.<br>"
        "<b>Solution:</b> By Law of Total Probability:<br>"
        "<code>P(Conception) = P(H) &times; P(C|H) + P(J) &times; P(C|J) = (0.60 &times; 0.50) + (0.40 &times; 0.65) = 0.30 + 0.26 = 0.56 (56%)</code>.<br><br>"
        "<b>MODEL EXAM PROBLEM 2 (NORMAL DISTRIBUTION):</b><br>"
        "In a population of 1,000 Sahiwal cows, 305-day lactation milk yield is normally distributed with mean <code>&mu; = 2,500 kg</code> and standard deviation <code>&sigma; = 400 kg</code>.<br>"
        "1. What percentage of cows yield more than 3,100 kg?<br>"
        "2. How many cows are expected to yield between 2,100 kg and 2,900 kg?<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><b>For X = 3,100 kg:</b>"
        "<br><code>Z = (3100 - 2500) / 400 = 600 / 400 = +1.50</code>."
        "<br>From Z-table, area from 0 to 1.50 = 0.4332."
        "<br>Area in upper tail <code>P(Z &gt; 1.50) = 0.5000 - 0.4332 = 0.0668 (6.68%)</code>."
        "<br><b>Answer 1:</b> <b>6.68%</b> of cows yield > 3,100 kg.</li>"
        "<li><b>For X between 2,100 kg and 2,900 kg:</b>"
        "<br><code>Z_1 = (2100 - 2500) / 400 = -400 / 400 = -1.00</code>."
        "<br><code>Z_2 = (2900 - 2500) / 400 = +400 / 400 = +1.00</code>."
        "<br>Area for Z = 1.00 from mean is 0.3413."
        "<br>Total Area between -1.00 and +1.00 = <code>0.3413 + 0.3413 = 0.6826 (68.26%)</code>."
        "<br>Expected number of cows = <code>1000 &times; 0.6826 = 682.6 &approx; 683 cows</code>."
        "<br><b>Answer 2:</b> <b>683 cows</b> yield between 2,100 kg and 2,900 kg.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What are the parameters of a Standard Normal Curve?</b><br>"
        "<b>A:</b> Mean <code>&mu; = 0</code> and Standard Deviation <code>&sigma; = 1</code> (Variance &sigma;&sup2; = 1).</li>"
        "<li><b>Q: What percentage of data falls within &mu; &plusmn; 1&sigma;, &mu; &plusmn; 2&sigma;, and &mu; &plusmn; 3&sigma;?</b><br>"
        "<b>A:</b> <b>68.27%</b> falls within &plusmn;1&sigma;, <b>95.45%</b> falls within &plusmn;2&sigma;, and <b>99.73%</b> falls within &plusmn;3&sigma; (Empirical Rule).</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Always draw a small bell-shaped curve sketch showing the shaded area in your answer sheet. Examiners award full marks for proper visual representation.</li>"
        "<li>Check table direction: Ensure whether the provided Z-table gives area from <code>0 to Z</code> (0.3413 for Z=1) or cumulative from <code>-&infin; to Z</code> (0.8413 for Z=1).</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Standard Normal Variate formula: Z = (X - μ) / σ.",
        "Total area under the Standard Normal Curve is exactly 1.0 (100%).",
        "The standard normal curve is symmetrical around Z = 0; mean = median = mode = 0.",
        "Area between μ ± 1σ is 68.27%; between μ ± 2σ is 95.45%; between μ ± 3σ is 99.73%.",
        "Law of Total Probability: P(A) = Σ P(B_i) * P(A | B_i).",
        "Multiplication rule for independent events: P(A ∩ B) = P(A) * P(B).",
        "Standard normal distribution has mean = 0 and standard deviation = 1.",
        "Negative Z-values indicate observations below the population mean.",
        "Upper tail probability for Z > 0 is calculated as: 0.5000 - Area(0 to Z).",
        "Expected frequency of animals is calculated as: N * P(Z1 < Z < Z2)."
    ],
    "tables": [
        {
            "title": "Standard Normal Distribution (Z) Area Reference Values for Common Exam Problems",
            "headers": ["Z-Score (Standard Deviations)", "Area from Mean to Z", "Two-Tailed Area (Within &plusmn; Z)", "Upper Tail Area (Z &gt; z)", "Livestock Selection Percentile"],
            "rows": [
                ["0.50", "0.1915", "0.3829 (38.29%)", "0.3085 (30.85%)", "69.15th percentile"],
                ["1.00", "0.3413", "0.6827 (68.27%)", "0.1587 (15.87%)", "84.13th percentile"],
                ["1.28", "0.3997", "0.7995 (80.00%)", "0.1000 (10.00%)", "Top 10% replacement heifers"],
                ["1.50", "0.4332", "0.8664 (86.64%)", "0.0668 (6.68%)", "Top 6.7% elite donor cows"],
                ["1.645", "0.4500", "0.9000 (90.00%)", "0.0500 (5.00%)", "5% significance critical value"],
                ["1.96", "0.4750", "0.9500 (95.00%)", "0.0250 (2.50%)", "95% confidence interval bound"],
                ["2.33", "0.4901", "0.9802 (98.02%)", "0.0099 (1.00%)", "Top 1% elite AI breeding sires"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "Veterinary clinical pathology laboratories establish serum biochemical reference intervals (e.g., serum calcium 9.0–11.5 mg/dl) "
        "as <code>&mu; &plusmn; 2&sigma;</code> (enclosing 95% of healthy cows). "
        "Any transition cow testing below <code>Z = -2.0</code> (serum Ca < 8.0 mg/dl) is diagnosed with clinical or subclinical hypocalcemia (milk fever) "
        "and immediately infused with intravenous calcium borogluconate."
    ),
    "tags": ["Biostatistics Lab", "Normal Distribution", "Z-Score", "Probability", "Standard Normal Curve", "Z-Table", "Milk Yield"]
}

topics["p1-t06"] = {
    "summary": "Computation of Pearson's Correlation Coefficient (r) and linear regression equations (Y on X) from animal experimental data with full test of significance.",
    "desc": (
        "<b>AIM:</b> To estimate Pearson's product-moment correlation coefficient (r) and fit a linear regression equation (Y on X) to predict body weight from heart girth in livestock.<br><br>"
        "<b>FORMULAS & EQUATIONS:</b>"
        "<ul>"
        "<li><b>Pearson's Correlation Coefficient (r):</b><br>"
        "<code>r = [ &Sigma;xy - (&Sigma;x &times; &Sigma;y) / n ] / &radic;[ { &Sigma;x&sup2; - (&Sigma;x)&sup2; / n } &times; { &Sigma;y&sup2; - (&Sigma;y)&sup2; / n } ]</code><br>"
        "<code>r = SP_xy / &radic;(SS_x &times; SS_y)</code>.</li>"
        "<li><b>Regression Coefficient of Y on X (b_yx):</b><br>"
        "<code>b_yx = SP_xy / SS_x = r &times; (s_y / s_x)</code></li>"
        "<li><b>Regression Line Equation (Y on X):</b><br>"
        "<code>(Y - \\bar{Y}) = b_yx &times; (X - \\bar{X})  &rarr;  Y = a + b_yx &times; X</code><br>"
        "Where intercept <code>a = \\bar{Y} - b_yx &times; \\bar{X}</code>.</li>"
        "<li><b>Test of Significance for r (t-test):</b><br>"
        "<code>t = [ r &times; &radic;(n - 2) ] / &radic;(1 - r&sup2;)</code> with <code>df = n - 2</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM:</b><br>"
        "Data on Heart Girth (X, cm) and Body Weight (Y, kg) recorded in 6 crossbred calves:<br>"
        "<code>X: 80, 85, 90, 95, 100, 105</code><br>"
        "<code>Y: 65, 72, 80, 88, 98, 107</code><br>"
        "Calculate 'r', derive the prediction equation, and predict weight for a calf with 110 cm girth.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><code>n = 6</code></li>"
        "<li><code>&Sigma;X = 555</code>, <code>\\bar{X} = 92.5</code> cm.</li>"
        "<li><code>&Sigma;Y = 510</code>, <code>\\bar{Y} = 85.0</code> kg.</li>"
        "<li><code>&Sigma;X&sup2; = 80&sup2; + 85&sup2; + 90&sup2; + 95&sup2; + 100&sup2; + 105&sup2; = 51,775</code>.</li>"
        "<li><code>SS_x = 51,775 - (555)&sup2; / 6 = 51,775 - 51,337.5 = 437.5</code>.</li>"
        "<li><code>&Sigma;Y&sup2; = 65&sup2; + 72&sup2; + 80&sup2; + 88&sup2; + 98&sup2; + 107&sup2; = 44,546</code>.</li>"
        "<li><code>SS_y = 44,546 - (510)&sup2; / 6 = 44,546 - 43,350 = 1,196.0</code>.</li>"
        "<li><code>&Sigma;XY = (80&times;65) + (85&times;72) + (90&times;80) + (95&times;88) + (100&times;98) + (105&times;107) = 5,200 + 6,120 + 7,200 + 8,360 + 9,800 + 11,235 = 47,915</code>.</li>"
        "<li><code>SP_xy = 47,915 - (555 &times; 510) / 6 = 47,915 - 47,175 = 740.0</code>.</li>"
        "<li><b>Correlation Coefficient (r):</b><br>"
        "<code>r = 740.0 / &radic;(437.5 &times; 1196.0) = 740.0 / &radic;523,250 = 740.0 / 723.36 = +0.9953</code> (Strong positive correlation).</li>"
        "<li><b>Regression Coefficient (b_yx):</b><br>"
        "<code>b_yx = SP_xy / SS_x = 740.0 / 437.5 = 1.6914</code> kg/cm.</li>"
        "<li><b>Intercept (a):</b><br>"
        "<code>a = \\bar{Y} - b_yx &times; \\bar{X} = 85.0 - (1.6914 &times; 92.5) = 85.0 - 156.455 = -71.455</code>.</li>"
        "<li><b>Regression Equation:</b> <code>Y = -71.455 + 1.6914 &times; X</code>.</li>"
        "<li><b>Prediction for X = 110 cm:</b><br>"
        "<code>Y = -71.455 + 1.6914(110) = -71.455 + 186.054 = 114.60 kg</code>.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What is the range of values for r and can it be negative?</b><br>"
        "<b>A:</b> Correlation coefficient <code>r</code> ranges from <b>-1.0 to +1.0</b>. Negative <code>r</code> means an increase in X leads to a proportional decrease in Y.</li>"
        "<li><b>Q: What is the Coefficient of Determination (r&sup2;)?</b><br>"
        "<b>A:</b> <code>r&sup2; = (0.9953)&sup2; = 0.9906 (99.06%)</code>; indicates that 99.06% of the total variation in body weight is directly explained by variation in heart girth!</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Remember the fundamental identity: <code>b_yx &times; b_xy = r&sup2;</code>. Both regression coefficients must always have the same mathematical sign as <code>r</code>!</li>"
        "<li>Degrees of freedom for testing correlation significance is always <code>n - 2</code>, NOT n - 1.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Pearson's correlation coefficient r measures the strength and direction of linear association.",
        "The range of r is -1.0 to +1.0; r = 0 indicates no linear association.",
        "Sum of Products (SPxy) formula: SPxy = ΣXY - (ΣX * ΣY) / n.",
        "Regression coefficient of Y on X: b_yx = SPxy / SSx.",
        "Linear regression prediction equation: Y = a + b_yx * X.",
        "Intercept formula: a = Ȳ - b_yx * X̄.",
        "Coefficient of determination r² measures proportion of variance explained.",
        "Significance of r is tested by Student's t-test with df = n - 2.",
        "Both regression slopes (b_yx and b_xy) must have the exact same algebraic sign as r.",
        "Heart girth is the most reliable single biometric predictor of cattle body weight."
    ],
    "tables": [
        {
            "title": "Computation Table for Correlation and Regression Between Heart Girth (X) and Body Weight (Y)",
            "headers": ["Calf No.", "Heart Girth X (cm)", "Body Weight Y (kg)", "X²", "Y²", "XY"],
            "rows": [
                ["1", "80", "65", "6400", "4225", "5200"],
                ["2", "85", "72", "7225", "5184", "6120"],
                ["3", "90", "80", "8100", "6400", "7200"],
                ["4", "95", "88", "9025", "7744", "8360"],
                ["5", "100", "98", "10000", "9604", "9800"],
                ["6", "105", "107", "11025", "11449", "11235"],
                ["Total (&Sigma;)", "555", "510", "51775", "44546", "47915"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In rural Indian veterinary practice, weighing balances for heavy cattle and buffaloes are unavailable. "
        "Veterinarians utilize derived regression formulas (such as <b>Shaeffer's formula: Body Weight (lbs) = (Heart Girth &times; Length) / 300</b>) "
        "to accurately estimate patient body weight for calculating correct therapeutic doses of general anesthetics, anthelmintics, and antibiotics."
    ),
    "tags": ["Biostatistics Lab", "Correlation", "Regression", "Pearson r", "Heart Girth", "Body Weight", "Prediction Equation"]
}

topics["p1-t07"] = {
    "summary": "Application of Large Sample Z-tests for testing the significance of single mean, difference between two means, single proportion, and difference between two proportions.",
    "desc": (
        "<b>AIM:</b> To apply Large Sample Z-tests (sample size N &ge; 30) for testing hypotheses concerning livestock means and proportions.<br><br>"
        "<b>TEST STATISTIC FORMULAS:</b>"
        "<ul>"
        "<li><b>Case 1: Single Mean Z-test:</b><br>"
        "<code>Z_cal = | \\bar{X} - &mu; | / (s / &radic;n)</code></li>"
        "<li><b>Case 2: Difference of Two Means Z-test:</b><br>"
        "<code>Z_cal = | \\bar{X}_1 - \\bar{X}_2 | / &radic;[ (s_1&sup2; / n_1) + (s_2&sup2; / n_2) ]</code></li>"
        "<li><b>Case 3: Single Proportion Z-test:</b><br>"
        "<code>Z_cal = | p - P | / &radic;[ P(1 - P) / n ]</code></li>"
        "<li><b>Case 4: Difference of Two Proportions Z-test:</b><br>"
        "<code>Z_cal = | p_1 - p_2 | / &radic;[ \\hat{P}(1 - \\hat{P}) &times; (1/n_1 + 1/n_2) ]</code><br>"
        "Where pooled proportion <code>\\hat{P} = (x_1 + x_2) / (n_1 + n_2)</code>.</li>"
        "<li><b>Decision Rule:</b>"
        "<br>&bull; If <code>|Z_cal| &gt; 1.96</code> &rarr; Reject H0 at <b>5% level of significance</b> (P &lt; 0.05, Significant)."
        "<br>&bull; If <code>|Z_cal| &gt; 2.58</code> &rarr; Reject H0 at <b>1% level of significance</b> (P &lt; 0.01, Highly Significant).</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM (DIFFERENCE OF TWO MEANS):</b><br>"
        "A field trial was conducted on 50 Murrah buffaloes fed a bypass-fat supplement and 50 control buffaloes. "
        "The supplement group averaged 11.2 kg milk/day with SD = 1.8 kg. The control group averaged 10.1 kg milk/day with SD = 2.0 kg. "
        "Test whether bypass-fat significantly increased milk yield.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><b>Hypotheses:</b>"
        "<br>Null Hypothesis H0: <code>&mu;_1 = &mu;_2</code> (Bypass-fat has no effect on milk yield)."
        "<br>Alternative Hypothesis H1: <code>&mu;_1 &ne; &mu;_2</code> (Two-tailed) or <code>&mu;_1 &gt; &mu;_2</code>.</li>"
        "<li><code>n_1 = 50, \\bar{X}_1 = 11.2, s_1 = 1.8</code></li>"
        "<li><code>n_2 = 50, \\bar{X}_2 = 10.1, s_2 = 2.0</code></li>"
        "<li><b>Standard Error of Difference:</b><br>"
        "<code>SE = &radic;[ (s_1&sup2; / n_1) + (s_2&sup2; / n_2) ] = &radic;[ (1.8&sup2; / 50) + (2.0&sup2; / 50) ] = &radic;[ (3.24 / 50) + (4.00 / 50) ] = &radic;[ 0.0648 + 0.0800 ] = &radic;0.1448 = 0.3805 kg</code>.</li>"
        "<li><b>Calculate Z:</b><br>"
        "<code>Z_cal = (11.2 - 10.1) / 0.3805 = 1.1 / 0.3805 = 2.891</code>.</li>"
        "<li><b>Conclusion:</b> Since <code>Z_cal = 2.891 &gt; 2.58</code> (critical value at 1%), the null hypothesis H0 is <b>rejected at P &lt; 0.01</b>."
        "<br><i>Inference:</i> Bypass-fat supplementation produced a <b>highly significant (P &lt; 0.01) increase</b> in daily milk yield.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What sample size qualifies as a 'Large Sample' in biostatistics?</b><br>"
        "<b>A:</b> A sample size of <code>n &ge; 30</code> is classified as a large sample, as the sampling distribution of the mean approaches normality under the Central Limit Theorem.</li>"
        "<li><b>Q: Why do we not need degrees of freedom in Z-tests?</b><br>"
        "<b>A:</b> Because for large samples (n &ge; 30), the sample standard deviation (s) is an extremely accurate estimate of the population standard deviation (&sigma;), so the distribution is standard normal with infinite degrees of freedom.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Memorize critical Z-table values: Two-tailed 5% = <b>1.96</b>; 1% = <b>2.58</b>; 0.1% = <b>3.29</b>. One-tailed 5% = <b>1.645</b>; 1% = <b>2.33</b>.</li>"
        "<li>Always state H0 and H1 explicitly at the beginning of your answer to secure the mandatory 1-mark hypothesis formulation allotment.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Z-test is applicable when sample size n ≥ 30 (Large Sample Theory).",
        "Based on the Central Limit Theorem where sampling distribution is normal.",
        "Test for single mean: Z = |X̄ - μ| / (s / √n).",
        "Test for difference of two means: Z = |X̄1 - X̄2| / √[(s1²/n1) + (s2²/n2)].",
        "Two-tailed critical Z-value at 5% significance level is 1.96.",
        "Two-tailed critical Z-value at 1% significance level is 2.58.",
        "One-tailed critical Z-value at 5% is 1.645; at 1% is 2.33.",
        "Null hypothesis H0 assumes zero treatment difference or zero deviation.",
        "Z_cal > Z_tab results in rejection of H0 and acceptance of statistical significance.",
        "Large sample test for proportions uses pooled P̂ = (x1 + x2) / (n1 + n2)."
    ],
    "tables": [
        {
            "title": "Standard Z-Test Critical Values and Decision Matrix",
            "headers": ["Significance Level (&alpha;)", "Test Type", "Critical Z-value (Z_tab)", "Decision Rule", "Statistical Inference"],
            "rows": [
                ["5% (P = 0.05)", "Two-tailed", "1.96", "Reject H0 if |Z_cal| &gt; 1.96", "Significant difference (P &lt; 0.05)"],
                ["1% (P = 0.01)", "Two-tailed", "2.58", "Reject H0 if |Z_cal| &gt; 2.58", "Highly significant difference (P &lt; 0.01)"],
                ["0.1% (P = 0.001)", "Two-tailed", "3.29", "Reject H0 if |Z_cal| &gt; 3.29", "Very highly significant (P &lt; 0.001)"],
                ["5% (P = 0.05)", "One-tailed (Directional)", "1.645", "Reject H0 if Z_cal &gt; +1.645", "Significant directional superiority"],
                ["1% (P = 0.01)", "One-tailed (Directional)", "2.33", "Reject H0 if Z_cal &gt; +2.33", "Highly significant directional gain"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In state livestock vaccination campaigns, veterinarians use large-sample proportion Z-tests to verify vaccine efficacy. "
        "If 85 out of 100 vaccinated calves show protective antibody titers compared to only 40 out of 100 unvaccinated controls, "
        "a Z-test on proportions confirms that the vaccine confers statistically significant protection against clinical infection."
    ),
    "tags": ["Biostatistics Lab", "Z-Test", "Large Sample", "Significance Testing", "Null Hypothesis", "Murrah Buffalo", "Bypass Fat"]
}

topics["p1-t08"] = {
    "summary": "Student's t-test applications for small samples (n < 30): One-sample t-test, Independent Two-sample t-test (equal variance), and Paired t-test for before-and-after clinical trials.",
    "desc": (
        "<b>AIM:</b> To apply Student's t-test for small samples (n &lt; 30) across independent and paired clinical veterinary investigations.<br><br>"
        "<b>CORE STATISTICAL FORMULAS:</b>"
        "<ul>"
        "<li><b>1. Independent Two-Sample t-test (Equal Variances):</b><br>"
        "<code>t_cal = | \\bar{X}_1 - \\bar{X}_2 | / [ s_p &times; &radic;(1/n_1 + 1/n_2) ]</code><br>"
        "Where Pooled Variance <code>s_p&sup2; = [ (n_1 - 1)s_1&sup2; + (n_2 - 1)s_2&sup2; ] / (n_1 + n_2 - 2)</code> with <code>df = n_1 + n_2 - 2</code>.</li>"
        "<li><b>2. Paired t-test (Before & After Trial on Same Animals):</b><br>"
        "<code>t_cal = | \\bar{d} | / (s_d / &radic;n)</code><br>"
        "Where <code>d_i = X_{after} - X_{before}</code>, <code>\\bar{d} = (&Sigma; d) / n</code>, and <code>s_d&sup2; = [ &Sigma;d&sup2; - (&Sigma;d)&sup2;/n ] / (n - 1)</code> with <code>df = n - 1</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM (PAIRED t-TEST):</b><br>"
        "A novel herbal anthelmintic was evaluated in 6 sheep naturally infected with <i>Haemonchus contortus</i>. "
        "Fecal Egg Counts (EPG in hundreds) before and 14 days after treatment were:<br>"
        "<code>Before: 28, 35, 42, 30, 25, 38</code><br>"
        "<code>After : 10, 12, 18, 14,  8, 16</code><br>"
        "Test whether the anthelmintic significantly reduced fecal egg counts (t_tab at df=5 for 5% = 2.571, for 1% = 4.032).<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><b>Compute Differences <code>d_i = Before - After</code>:</b>"
        "<br>Sheep 1: <code>28 - 10 = 18</code>"
        "<br>Sheep 2: <code>35 - 12 = 23</code>"
        "<br>Sheep 3: <code>42 - 18 = 24</code>"
        "<br>Sheep 4: <code>30 - 14 = 16</code>"
        "<br>Sheep 5: <code>25 -  8 = 17</code>"
        "<br>Sheep 6: <code>38 - 16 = 22</code></li>"
        "<li><code>n = 6</code>, <code>&Sigma; d = 18 + 23 + 24 + 16 + 17 + 22 = 120</code>.</li>"
        "<li><code>Mean Difference (\\bar{d}) = 120 / 6 = 20.0</code>.</li>"
        "<li><code>&Sigma; d&sup2; = 18&sup2; + 23&sup2; + 24&sup2; + 16&sup2; + 17&sup2; + 22&sup2; = 324 + 529 + 576 + 256 + 289 + 484 = 2,458</code>.</li>"
        "<li><code>SS_d = 2,458 - (120)&sup2; / 6 = 2,458 - 2,400 = 58.0</code>.</li>"
        "<li><code>s_d&sup2; = 58.0 / (6 - 1) = 58.0 / 5 = 11.6</code>; <code>s_d = &radic;11.6 = 3.406</code>.</li>"
        "<li><code>SE_\\bar{d} = 3.406 / &radic;6 = 3.406 / 2.4495 = 1.3905</code>.</li>"
        "<li><b>Calculate t:</b><br>"
        "<code>t_cal = 20.0 / 1.3905 = 14.383</code>.</li>"
        "<li><b>Degrees of Freedom:</b> <code>df = 6 - 1 = 5</code>.</li>"
        "<li><b>Inference:</b> Since <code>t_cal = 14.383 &gt; t_tab(5, 0.01) = 4.032</code>, H0 is rejected at <b>P &lt; 0.001 (Very Highly Significant)</b>."
        "<br><i>Conclusion:</i> The herbal anthelmintic produced a dramatic and highly significant reduction in EPG.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Who developed the t-test and why was it published under the pseudonym 'Student'?</b><br>"
        "<b>A:</b> Developed by <b>William Sealy Gosset (1908)</b> while working at the Guinness Brewery, which prohibited employees from publishing scientific papers under their real names.</li>"
        "<li><b>Q: What are the three core assumptions of Student's t-test?</b><br>"
        "<b>A:</b> (a) The parent population is normally distributed, (b) Samples are randomly drawn, and (c) In independent samples, population variances are equal (&sigma;1&sup2; = &sigma;2&sup2; - homoscedasticity).</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>In independent two-sample t-tests, verify equality of variances using Fisher's F-test: <code>F = s1&sup2; / s2&sup2;</code> before pooling! If variances are unequal, standard pooling is invalid (Behrens-Fisher problem).</li>"
        "<li>Degrees of freedom must be stated explicitly: <code>df = n1 + n2 - 2</code> for two-sample; <code>df = n - 1</code> for paired t-test.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Student's t-test was developed by W.S. Gosset (1908) for small samples (n < 30).",
        "Assumes normal distribution of the underlying biological population.",
        "Independent two-sample t-test requires equal variances and has df = n1 + n2 - 2.",
        "Pooled variance formula: sp² = [(n1 - 1)s1² + (n2 - 1)s2²] / (n1 + n2 - 2).",
        "Paired t-test compares the same animals before and after treatment.",
        "Paired t-test degrees of freedom: df = n - 1 (where n = number of pairs).",
        "Paired t-test removes inter-animal baseline variability, drastically increasing test power.",
        "Test statistic for paired t-test: t = d̄ / (sd / √n).",
        "Critical t-value is looked up at specific degrees of freedom in the Student's t-table.",
        "If t_cal > t_tab, reject H0 and declare the treatment effect statistically significant."
    ],
    "tables": [
        {
            "title": "Paired t-Test Computation Table for Sheep Anthelmintic Trial (N = 6)",
            "headers": ["Sheep ID", "Pre-treatment EPG (x1)", "Post-treatment EPG (x2)", "Difference d = x1 - x2", "Deviation (d - d̄)", "(d - d̄)²"],
            "rows": [
                ["1", "28", "10", "18", "-2", "4"],
                ["2", "35", "12", "23", "+3", "9"],
                ["3", "42", "18", "24", "+4", "16"],
                ["4", "30", "14", "16", "-4", "16"],
                ["5", "25", "8", "17", "-3", "9"],
                ["6", "38", "16", "22", "+2", "4"],
                ["Total (&Sigma;)", "198", "78", "&Sigma;d = 120", "0", "SS_d = 58"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "Veterinary surgeons use paired t-tests in clinical trials evaluating post-operative analgesics or antipyretics. "
        "Measuring body temperature or pain scores in the same dogs <b>before administration (Hour 0) and 2 hours after administration</b> "
        "controls for individual physiological differences, reliably isolating the true drug efficacy."
    ),
    "tags": ["Biostatistics Lab", "Student's t-Test", "Paired t-Test", "Small Sample", "Haemonchus", "Anthelmintic", "Degrees of Freedom"]
}

topics["p1-t09"] = {
    "summary": "Chi-Square (χ²) test applications in animal genetics: Test of Goodness of Fit for Mendelian ratios, 2x2 contingency tables, test of independence, and Yates' correction for continuity.",
    "desc": (
        "<b>AIM:</b> To apply Chi-Square (&chi;&sup2;) tests for verifying Mendelian phenotypic ratios (Goodness of Fit) and testing independence of clinical attributes in 2&times;2 contingency tables.<br><br>"
        "<b>CORE STATISTICAL FORMULAS:</b>"
        "<ul>"
        "<li><b>General Chi-Square Formula:</b><br>"
        "<code>&chi;&sup2; = &Sigma; [ (O - E)&sup2; / E ]</code><br>"
        "Where <code>O</code> = Observed Frequency; <code>E</code> = Expected Frequency; <code>df = k - 1</code> (where k = number of phenotypic classes).</li>"
        "<li><b>Expected Frequency for Contingency Table:</b><br>"
        "<code>E_ij = (Row Total_i &times; Column Total_j) / Grand Total (N)</code></li>"
        "<li><b>Short-cut Formula for 2&times;2 Contingency Table:</b><br>"
        "<code>&chi;&sup2; = [ N &times; (ad - bc)&sup2; ] / [ (a + b)(c + d)(a + c)(b + d) ]</code> with <code>df = (2 - 1)(2 - 1) = 1</code>.</li>"
        "<li><b>Yates' Correction for Continuity (Mandatory when df = 1 and any cell E &lt; 5):</b><br>"
        "<code>&chi;&sup2;_{corrected} = [ N &times; (|ad - bc| - N/2)&sup2; ] / [ (a + b)(c + d)(a + c)(b + d) ]</code></li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (GOODNESS OF FIT):</b><br>"
        "In a sheep breeding experiment involving cross of heterozygous polled rams with horned ewes, the offspring showed <b>115 polled and 85 horned lambs</b>. "
        "Test whether this segregates according to the expected 1:1 Mendelian test-cross ratio (&chi;&sup2;_tab at df=1 for 5% = 3.841).<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li>Null Hypothesis H0: The data conforms to the theoretical 1:1 ratio.</li>"
        "<li>Total lambs <code>N = 115 + 85 = 200</code>.</li>"
        "<li>Expected frequency of Polled = <code>200 &times; (1/2) = 100</code>.</li>"
        "<li>Expected frequency of Horned = <code>200 &times; (1/2) = 100</code>.</li>"
        "<li><code>&chi;&sup2; = [ (115 - 100)&sup2; / 100 ] + [ (85 - 100)&sup2; / 100 ] = [ (15)&sup2; / 100 ] + [ (-15)&sup2; / 100 ] = 225/100 + 225/100 = 2.25 + 2.25 = 4.50</code>.</li>"
        "<li><code>df = k - 1 = 2 - 1 = 1</code>.</li>"
        "<li><b>Inference:</b> Since <code>&chi;&sup2;_cal = 4.50 &gt; &chi;&sup2;_tab = 3.841</code>, H0 is <b>rejected at 5% significance level</b>."
        "<br><i>Conclusion:</i> The observed phenotypic ratio deviates significantly from the Mendelian 1:1 expectation.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: When is Yates' Correction for continuity strictly applied?</b><br>"
        "<b>A:</b> Strictly applied in <b>2&times;2 contingency tables (df = 1)</b> when any expected cell frequency is small (&lt; 5), subtracting N/2 from |ad - bc| to adjust for approximating a discrete binomial with a continuous chi-square curve.</li>"
        "<li><b>Q: What are the two mandatory conditions for validity of Chi-Square test?</b><br>"
        "<b>A:</b> (a) Total sample size N should be reasonably large (&ge; 50), and (b) No expected cell frequency should be less than 5 (if &lt; 5, combine adjacent classes).</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Always verify that <code>&Sigma; O = &Sigma; E = N</code>. If total expected does not match total observed, the calculation is wrong.</li>"
        "<li>Memorize the critical &chi;&sup2; values: df=1 &rarr; <b>3.841</b> (5%) & <b>6.635</b> (1%); df=2 &rarr; <b>5.991</b>; df=3 &rarr; <b>7.815</b>.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Chi-Square test statistic formula: χ² = Σ [(O - E)² / E].",
        "Goodness of Fit tests whether observed data conforms to expected Mendelian ratios.",
        "Degrees of freedom for Goodness of Fit is df = k - 1 (k = number of classes).",
        "Degrees of freedom for an r x c contingency table is df = (r - 1) * (c - 1).",
        "Expected frequency for contingency cells: E = (Row Total * Column Total) / Grand Total.",
        "2x2 contingency shortcut: χ² = [ N * (ad - bc)² ] / [ (a+b)(c+d)(a+c)(b+d) ].",
        "Yates' correction is mandatory for df = 1 when any expected cell frequency E < 5.",
        "Total observed frequency ΣO must exactly equal total expected frequency ΣE.",
        "Critical χ² at df=1: 3.841 at 5% level; 6.635 at 1% level.",
        "If χ²_cal > χ²_tab, reject H0 and conclude that attributes are significantly associated."
    ],
    "tables": [
        {
            "title": "Chi-Square Test of Independence for Breed vs Bovine Mastitis Incidence",
            "headers": ["Breed Class", "Mastitis Positive (a, c)", "Mastitis Negative (b, d)", "Row Total (R_i)", "Expected Positive (E)", "Cell &chi;&sup2; = (O - E)&sup2;/E"],
            "rows": [
                ["Exotic Crossbreds (HF)", "40 (O1)", "60 (O2)", "100", "25.0", "(40 - 25)&sup2; / 25 = 9.00"],
                ["Indigenous Zebu (Gir)", "10 (O3)", "90 (O4)", "100", "25.0", "(10 - 25)&sup2; / 25 = 9.00"],
                ["Column Total (C_j)", "50", "150", "N = 200", "—", "&chi;&sup2; = 18.00 + 6.00 = 24.00"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "Veterinary epidemiologists utilize 2&times;2 Chi-Square contingency tables to establish risk factor associations. "
        "Testing <b>Breed (Crossbred vs Indigenous) against Clinical Mastitis occurrence</b> (&chi;&sup2; = 24.00, P &lt; 0.001) "
        "statistically confirms that exotic crossbred cows possess significantly higher vulnerability to clinical udder infections than indigenous Zebu cows."
    ),
    "tags": ["Biostatistics Lab", "Chi-Square Test", "Goodness of Fit", "Contingency Table", "Yates' Correction", "Mendelian Ratio", "Mastitis"]
}

topics["p1-t10"] = {
    "summary": "Analysis of Variance (ANOVA) for Completely Randomized Design (CRD) and Randomized Block Design (RBD) with Sums of Squares, F-test, and Critical Difference (CD).",
    "desc": (
        "<b>AIM:</b> To perform one-way ANOVA for Completely Randomized Design (CRD) and two-way ANOVA for Randomized Block Design (RBD), test treatment significance using F-test, and calculate Critical Difference (CD).<br><br>"
        "<b>ANOVA COMPUTATION STEPS (CRD - ONE WAY):</b>"
        "<ol>"
        "<li><b>Correction Factor (CF):</b> <code>CF = G&sup2; / N</code> (where G = Grand Total, N = total observations).</li>"
        "<li><b>Total Sum of Squares (TSS):</b> <code>TSS = &Sigma; &Sigma; X_{ij}&sup2; - CF</code> (with <code>df = N - 1</code>).</li>"
        "<li><b>Treatment Sum of Squares (TrSS):</b> <code>TrSS = &Sigma; (T_i&sup2; / n_i) - CF</code> (with <code>df = k - 1</code>, where k = treatments).</li>"
        "<li><b>Error Sum of Squares (ESS):</b> <code>ESS = TSS - TrSS</code> (with <code>df = N - k</code>).</li>"
        "<li><b>Mean Sum of Squares:</b> <code>TrMS = TrSS / (k - 1)</code>; <code>EMS = ESS / (N - k)</code>.</li>"
        "<li><b>F-Statistic:</b> <code>F_cal = TrMS / EMS</code> with <code>df = (k - 1, N - k)</code>.</li>"
        "<li><b>Critical Difference (CD):</b> <code>CD = t_tab &times; &radic;(2 &times; EMS / r)</code> (where r = replications per treatment).</li>"
        "</ol><br>"
        "<b>RBD (TWO-WAY ANOVA) EXTENSION:</b>"
        "<ul>"
        "<li>Block Sum of Squares (BSS): <code>BSS = &Sigma; (B_j&sup2; / k) - CF</code> (with <code>df = r - 1</code>).</li>"
        "<li>Error Sum of Squares in RBD: <code>ESS = TSS - TrSS - BSS</code> with <code>df = (k - 1)(r - 1)</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM (CRD):</b><br>"
        "Three rations (A, B, C) were fed to 4 broiler chicks each. The 6-week body weight gains (hundred grams) were:<br>"
        "<code>Ration A: 12, 14, 11, 15 (T_A = 52)</code><br>"
        "<code>Ration B: 16, 18, 15, 19 (T_B = 68)</code><br>"
        "<code>Ration C: 20, 22, 19, 23 (T_C = 84)</code><br>"
        "Perform ANOVA and calculate CD (F_tab at df=2,9 for 5% = 4.26).<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><code>k = 3, r = 4, N = 12</code>.</li>"
        "<li><code>G = 52 + 68 + 84 = 204</code>.</li>"
        "<li><code>CF = (204)&sup2; / 12 = 41,616 / 12 = 3,468</code>.</li>"
        "<li><code>&Sigma;&Sigma; X&sup2; = (12&sup2;+14&sup2;+11&sup2;+15&sup2;) + (16&sup2;+18&sup2;+15&sup2;+19&sup2;) + (20&sup2;+22&sup2;+19&sup2;+23&sup2;) = 686 + 1,166 + 1,774 = 3,626</code>.</li>"
        "<li><code>TSS = 3,626 - 3,468 = 158.0</code> (df = 11).</li>"
        "<li><code>TrSS = [ (52&sup2; + 68&sup2; + 84&sup2;) / 4 ] - 3,468 = [ (2704 + 4624 + 7056) / 4 ] - 3,468 = [ 14,384 / 4 ] - 3,468 = 3,596 - 3,468 = 128.0</code> (df = 2).</li>"
        "<li><code>ESS = TSS - TrSS = 158.0 - 128.0 = 30.0</code> (df = 9).</li>"
        "<li><code>TrMS = 128.0 / 2 = 64.0</code>.</li>"
        "<li><code>EMS = 30.0 / 9 = 3.333</code>.</li>"
        "<li><code>F_cal = TrMS / EMS = 64.0 / 3.333 = 19.20</code>.</li>"
        "<li><b>Conclusion:</b> Since <code>F_cal = 19.20 &gt; F_tab(2, 9) = 4.26</code>, the ration treatments differ <b>highly significantly (P &lt; 0.01)</b>.</li>"
        "<li><b>Critical Difference:</b> <code>SE_d = &radic;(2 &times; 3.333 / 4) = &radic;1.666 = 1.291</code>. For df=9 at 5%, <code>t = 2.262</code>.<br>"
        "<code>CD = 2.262 &times; 1.291 = 2.92</code> (i.e. 292 g).</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What are the three fundamental principles of experimental design?</b><br>"
        "<b>A:</b> (1) <b>Randomization</b> (eliminates investigator bias), (2) <b>Replication</b> (provides error estimate), and (3) <b>Local Control</b> (reduces experimental error by blocking).</li>"
        "<li><b>Q: How does RBD differ from CRD in local control?</b><br>"
        "<b>A:</b> CRD uses only 2 principles (Randomization and Replication) for completely homogenous experimental units; RBD uses all 3 principles (Local Control via blocking along one gradient).</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Construct the complete ANOVA Summary Table with Columns: <code>Source of Variation | Degrees of Freedom | Sum of Squares | Mean Square | F_calculated | F_tabulated</code>. Missing this formatted table loses 2 marks.</li>"
        "<li>Mean Comparison Ranking: State pair-wise differences: <code>Mean C (21) - Mean B (17) = 4.0 &gt; CD (2.92)</code> &rarr; Ration C is significantly superior to Ration B!</li>"
        "</ul>"
    ),
    "keyPoints": [
        "ANOVA partitions total variance into explained (treatment) and unexplained (error) parts.",
        "Correction Factor formula: CF = G² / N (Grand total squared divided by total observations).",
        "Total Sum of Squares: TSS = ΣX² - CF with df = N - 1.",
        "Treatment Sum of Squares: TrSS = Σ(Ti² / ri) - CF with df = k - 1.",
        "Error Sum of Squares: ESS = TSS - TrSS with df = N - k (in CRD).",
        "F-statistic is the ratio of Treatment Mean Square to Error Mean Square: F = TrMS / EMS.",
        "RBD adds Block Sum of Squares (BSS) with df = r - 1 to isolate environmental gradients.",
        "Critical Difference (CD) formula: CD = t_tab * √(2 * EMS / r).",
        "If the difference between two treatment means exceeds CD, they differ significantly.",
        "Three principles of experimental design: Randomization, Replication, and Local Control."
    ],
    "tables": [
        {
            "title": "Complete One-Way ANOVA Summary Table for Broiler Ration Trial (CRD)",
            "headers": ["Source of Variation", "Degrees of Freedom (df)", "Sum of Squares (SS)", "Mean Square (MS)", "F_calculated", "F_tabulated (5%)"],
            "rows": [
                ["Ration Treatments", "k - 1 = 2", "128.00", "64.00", "19.20**", "4.26"],
                ["Experimental Error", "N - k = 9", "30.00", "3.33", "—", "—"],
                ["Total", "N - 1 = 11", "158.00", "—", "—", "—"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In veterinary animal nutrition trials, researchers use RBD to test different protein supplementation levels in dairy cattle. "
        "Cows are blocked based on initial milk yield or parity into homogenous blocks (High, Medium, Low yielders) before assigning diets, "
        "ensuring differences in milk output are strictly attributable to feed protein rather than initial lactation potential."
    ),
    "tags": ["Biostatistics Lab", "ANOVA", "CRD", "RBD", "F-Test", "Critical Difference", "Broiler Rations", "Sum of Squares"]
}

topics["p1-t11"] = {
    "summary": "Practical execution of livestock data entry, statistical formula syntax, descriptive statistics, correlation, and ANOVA using MS-Excel in veterinary bio-computing.",
    "desc": (
        "<b>AIM:</b> To enter livestock records into MS-Excel, apply statistical formulas, and execute automated Data Analysis Toolpak functions for descriptive statistics, correlation, and ANOVA.<br><br>"
        "<b>STANDARD MS-EXCEL STATISTICAL FORMULAS (EXAM SPECIFIC):</b>"
        "<ul>"
        "<li><b>Mean:</b> <code>=AVERAGE(A2:A31)</code></li>"
        "<li><b>Median:</b> <code>=MEDIAN(A2:A31)</code></li>"
        "<li><b>Mode:</b> <code>=MODE.SNGL(A2:A31)</code></li>"
        "<li><b>Sample Standard Deviation:</b> <code>=STDEV.S(A2:A31)</code> (Uses n - 1 Bessel's correction).</li>"
        "<li><b>Sample Variance:</b> <code>=VAR.S(A2:A31)</code></li>"
        "<li><b>Standard Error:</b> <code>=STDEV.S(A2:A31)/SQRT(COUNT(A2:A31))</code></li>"
        "<li><b>Coefficient of Variation (CV%):</b> <code>=(STDEV.S(A2:A31)/AVERAGE(A2:A31))*100</code></li>"
        "<li><b>Pearson Correlation:</b> <code>=CORREL(A2:A31, B2:B31)</code></li>"
        "<li><b>Linear Regression Slope:</b> <code>=SLOPE(known_y's, known_x's)</code></li>"
        "<li><b>Linear Regression Intercept:</b> <code>=INTERCEPT(known_y's, known_x's)</code></li>"
        "<li><b>Student's t-test:</b> <code>=T.TEST(array1, array2, tails, type)</code> (Type: 1 = Paired; 2 = Two-sample equal variance).</li>"
        "</ul><br>"
        "<b>PROCEDURE FOR AUTOMATED DATA ANALYSIS TOOLPAK:</b>"
        "<ol>"
        "<li>Enable Toolpak: <code>File &rarr; Options &rarr; Add-Ins &rarr; Excel Add-ins (Go) &rarr; Check 'Analysis ToolPak' &rarr; OK</code>.</li>"
        "<li>Navigate to <code>Data Tab &rarr; Data Analysis</code>.</li>"
        "<li><b>For Descriptive Statistics:</b> Select 'Descriptive Statistics' &rarr; Select Input Range &rarr; Check 'Labels in first row' &rarr; Check 'Summary statistics' &rarr; Click OK.</li>"
        "<li><b>For ANOVA:</b> Select 'Anova: Single Factor' (for CRD) or 'Anova: Two-Factor Without Replication' (for RBD) &rarr; Select data table range &rarr; Alpha = 0.05 &rarr; OK.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What is the difference between =STDEV.P and =STDEV.S in Excel?</b><br>"
        "<b>A:</b> <code>=STDEV.P</code> divides by <code>N</code> (assumes data is the entire population); <code>=STDEV.S</code> divides by <code>n - 1</code> (sample standard deviation with Bessel's correction). Veterinarians must always use <code>=STDEV.S</code> for sample trials!</li>"
        "<li><b>Q: How do you add a linear trendline and regression equation on a scatter plot in Excel?</b><br>"
        "<b>A:</b> Right-click data points on scatter plot &rarr; Select 'Add Trendline' &rarr; Choose 'Linear' &rarr; Check 'Display Equation on chart' and 'Display R-squared value on chart'.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>In practical computer exams, always verify cell references: use absolute referencing <code>$A$2:$A$31</code> when dragging formulas across columns to prevent range shifts.</li>"
        "<li>Excel ANOVA Single Factor output produces both <code>F</code> and <code>P-value</code>: if <code>P-value &lt; 0.05</code>, declare treatment significant immediately without checking F-critical tables.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Arithmetic mean in Excel: =AVERAGE(range).",
        "Sample standard deviation with Bessel's correction: =STDEV.S(range).",
        "Population standard deviation: =STDEV.P(range).",
        "Standard Error formula: =STDEV.S(range)/SQRT(COUNT(range)).",
        "Pearson correlation formula: =CORREL(array1, array2).",
        "Regression slope formula: =SLOPE(known_y's, known_x's).",
        "Regression intercept formula: =INTERCEPT(known_y's, known_x's).",
        "T-test formula: =T.TEST(array1, array2, tails, type); Type 1 is paired, Type 2 is independent.",
        "Analysis ToolPak provides automated one-click Descriptive Statistics and ANOVA.",
        "Anova: Single Factor in Excel executes Completely Randomized Design (CRD)."
    ],
    "tables": [
        {
            "title": "Essential MS-Excel Formulas for Livestock Data Analysis",
            "headers": ["Statistical Parameter", "Excel Function / Formula Syntax", "Input Argument Types", "Interpretation / Output"],
            "rows": [
                ["Sample Mean", "=AVERAGE(B2:B51)", "Continuous numeric cells", "Arithmetic average of livestock trait"],
                ["Sample Std Dev", "=STDEV.S(B2:B51)", "Sample data range", "Sample standard deviation (s) with df = n - 1"],
                ["Standard Error", "=STDEV.S(B2:B51)/SQRT(COUNT(B2:B51))", "Formula combination", "SE of the mean for scientific reports"],
                ["Pearson Correlation", "=CORREL(B2:B51, C2:C51)", "Two matched data arrays", "r value (-1.0 to +1.0)"],
                ["Paired t-Test", "=T.TEST(B2:B20, C2:C20, 2, 1)", "Pre & post arrays, 2-tailed, type 1", "Direct P-value of paired comparison"],
                ["One-Way ANOVA", "Data Analysis &rarr; Anova: Single Factor", "Grouped column ranges", "Complete ANOVA table with SS, MS, F and P-value"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "Veterinary officers managing district polyclinics maintain MS-Excel spreadsheets to log surgical cases, artificial inseminations, and rabies vaccinations. "
        "Using pivot tables and automated =AVERAGE and =STDEV.S formulas allows monthly generation of Disease Surveillance Reports (DSR) "
        "submitted directly to the State Department of Animal Husbandry."
    ),
    "tags": ["Biostatistics Lab", "MS-Excel", "Bio-Computing", "STDEV.S", "AVERAGE", "CORREL", "ANOVA Toolpak", "Data Analysis"]
}
