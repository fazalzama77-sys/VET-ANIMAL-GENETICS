var practicalData = (typeof practicalData !== 'undefined') ? practicalData : ((typeof window !== 'undefined' && window.practicalData) ? window.practicalData : {});
if (typeof window !== 'undefined') window.practicalData = practicalData;

practicalData["prac-unit-1"] = {
  "p1-t01": {
    "summary": "Practical exercise on primary and secondary biological data collection, constructing frequency distribution tables using Sturges' rule, and compiling livestock farm records.",
    "desc": "<b>AIM:</b> To collect, compile, classify, and present raw livestock production records into a continuous grouped frequency distribution table.<br><br><b>PRINCIPLE & STATISTICAL RULES:</b><ul><li><b>Range (R):</b> <code>R = X_max - X_min</code> (Difference between highest and lowest observation).</li><li><b>Number of Classes (k) — Sturges' Rule:</b> <code>k = 1 + 3.322 &times; log10(N)</code> (where N = total sample size).</li><li><b>Class Width / Interval (h or c):</b> <code>h = Range / k</code> (rounded up to a convenient integer).</li><li><b>Tally Mark Method:</b> Observations are tallied in bunches of five (four vertical strokes and a diagonal strike) into mutually exclusive class intervals.</li></ul><br><b>MODEL EXAM PROBLEM:</b><br>The following are the daily milk yields (kg) of 30 Sahiwal cows recorded on an organized dairy farm:<br><code>8.2, 10.5, 12.0, 7.5, 9.4, 11.2, 13.8, 6.5, 10.0, 8.8, 14.2, 9.0, 11.5, 7.8, 10.8, 12.5, 8.0, 9.6, 13.0, 11.0, 10.2, 8.5, 7.0, 12.2, 9.8, 10.6, 11.8, 6.8, 13.5, 10.4</code>.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><code>X_min = 6.5</code> kg, <code>X_max = 14.2</code> kg.</li><li><code>Range = 14.2 - 6.5 = 7.7</code> kg.</li><li><code>k = 1 + 3.322 &times; log10(30) = 1 + 3.322(1.4771) = 1 + 4.907 = 5.91 &approx; 6 classes</code>.</li><li><code>Class Interval (h) = 7.7 / 6 = 1.28 &approx; 1.5</code> kg (or convenient width of 1.5 or 2.0). Using class width = 1.5 kg with starting class 6.0–7.5.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What is the difference between discrete and continuous frequency distribution?</b><br><b>A:</b> Discrete distributions count integer variables without fractional values (e.g., litter size, parity); continuous distributions measure parameters capable of taking any fractional real value within an interval (e.g., milk yield, body weight).</li><li><b>Q: What are exclusive vs inclusive class intervals?</b><br><b>A:</b> In exclusive intervals (e.g., 6–8, 8–10), the upper limit is excluded and counted in the next class; in inclusive intervals (e.g., 6–7.9, 8–9.9), both limits are included in the same class.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Always verify that <code>&Sigma; f_i = N</code>. Missing a single tally mark leads to immediate marks deduction in practical exams.</li><li>Calculate both <b>'Less than'</b> and <b>'More than'</b> cumulative frequencies in your examination table as examiners specifically check for cumulative boundary alignment.</li><li>Mid-value formula: <code>x_i = (Lower Limit + Upper Limit) / 2</code>. State mid-values explicitly for use in subsequent mean/SD calculations.</li></ul>",
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
        "headers": [
          "Parameter / Class Interval (kg)",
          "Class Mid-Value (x_i)",
          "Tally Marks",
          "Frequency (f_i)",
          "Less-than Cumulative Freq (cf)",
          "Relative Frequency (f/N)"
        ],
        "rows": [
          [
            "6.0 – 7.5",
            "6.75",
            "||||",
            "4",
            "4",
            "0.133"
          ],
          [
            "7.5 – 9.0",
            "8.25",
            "|||| |",
            "6",
            "10",
            "0.200"
          ],
          [
            "9.0 – 10.5",
            "9.75",
            "|||| ||",
            "7",
            "17",
            "0.233"
          ],
          [
            "10.5 – 12.0",
            "11.25",
            "|||| |",
            "6",
            "23",
            "0.200"
          ],
          [
            "12.0 – 13.5",
            "12.75",
            "||||",
            "4",
            "27",
            "0.133"
          ],
          [
            "13.5 – 15.0",
            "14.25",
            "|||",
            "3",
            "30",
            "0.100"
          ],
          [
            "Total",
            "—",
            "—",
            "N = 30",
            "—",
            "1.000"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> At commercial dairy farms and gaushalas, compilation of daily milking records into grouped frequency tables identifies the herd production profile, enabling veterinarians to segregate high-yielders (> 12 kg/day) for elite challenge feeding from low-yielders (< 7.5 kg/day) slated for reproductive evaluation.",
    "tags": [
      "Biostatistics Lab",
      "Frequency Distribution",
      "Sturges' Rule",
      "Tally Marks",
      "Tabulation",
      "Sahiwal Milk Yield"
    ]
  },
  "p1-t02": {
    "summary": "Construction and graphical presentation of biological data using histograms, frequency polygons, frequency curves, and cumulative ogives to locate partition values.",
    "desc": "<b>AIM:</b> To plot Histogram, Frequency Polygon, and Cumulative Frequency Ogives ('Less-than' and 'More-than') for livestock data and determine median graphically.<br><br><b>PRINCIPLES & GRAPHICAL RULES:</b><ul><li><b>Histogram:</b> Rectangles erected on continuous class boundaries along the X-axis, with height proportional to class frequency (or frequency density if class intervals are unequal).</li><li><b>Frequency Polygon:</b> Obtained by joining the midpoints of the tops of histogram rectangles with straight lines, anchored to the X-axis at midpoints of adjacent imaginary zero-frequency classes.</li><li><b>Ogives (Cumulative Curves):</b><br>&bull; <i>Less-than Ogive:</i> Plot less-than cumulative frequencies against upper class boundaries (S-shaped rising curve).<br>&bull; <i>More-than Ogive:</i> Plot more-than cumulative frequencies against lower class boundaries (descending curve).<br>&bull; <i>Graphical Median:</i> The X-coordinate of the point where 'Less-than' and 'More-than' ogives intersect corresponds exactly to the <b>Median</b> (or the value corresponding to <code>N/2</code> on the Y-axis of a single ogive).</li></ul><br><b>MODEL EXAM PROBLEM:</b><br>From the grouped frequency distribution of Murrah buffalo body weights (kg):<br><code>400–450 (f=6), 450–500 (f=14), 500–550 (f=20), 550–600 (f=8), 600–650 (f=2)</code>; Total N = 50.<br>Plot less-than cumulative frequencies and determine median graphically.<br><br><b>STEP-BY-STEP PROCEDURE:</b><ol><li>Construct Upper Class Boundaries: 450, 500, 550, 600, 650.</li><li>Compute Less-than cf: 6, 20, 40, 48, 50.</li><li>Calculate <code>N/2 = 50 / 2 = 25</code>.</li><li>Locate 25 on the cumulative frequency (Y) axis; project horizontally to intersect the Less-than ogive; drop a vertical line to the X-axis.</li><li><b>Result:</b> The vertical drop hits <b>512.5 kg</b> (Median body weight).</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Why cannot a frequency polygon be drawn without class midpoints?</b><br><b>A:</b> A frequency polygon requires a single representative coordinate per class; the mathematical centroid of a continuous interval is its midpoint (class mark).</li><li><b>Q: How is Mode determined graphically from a Histogram?</b><br><b>A:</b> In the modal (tallest) rectangle, draw a line from the top-left corner to the top-left of the next right bar, and from top-right corner to top-right of the next left bar. The intersection point dropped perpendicularly to the X-axis gives the Mode.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Always mention axes labels and scale on graph sheets: e.g., 'X-axis: 1 cm = 50 kg; Y-axis: 1 cm = 5 buffaloes'. Missing scale deducts 1 to 2 marks immediately.</li><li>Remember: If class intervals are unequal, histogram heights must represent <b>Frequency Density = Frequency / Class Width</b>, NOT raw frequency.</li><li>The intersection of less-than and more-than ogives gives <code>(Median, N/2)</code>. This is a classic 2-mark viva question.</li></ul>",
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
        "headers": [
          "Parameter / Class Interval",
          "Lower Boundary",
          "Upper Boundary",
          "Frequency (f)",
          "Less-than cf (Plot on Upper)",
          "More-than cf (Plot on Lower)"
        ],
        "rows": [
          [
            "400 – 450 kg",
            "400",
            "450",
            "6",
            "6",
            "50"
          ],
          [
            "450 – 500 kg",
            "450",
            "500",
            "14",
            "20",
            "44"
          ],
          [
            "500 – 550 kg",
            "500",
            "550",
            "20",
            "40",
            "30"
          ],
          [
            "550 – 600 kg",
            "550",
            "600",
            "8",
            "48",
            "10"
          ],
          [
            "600 – 650 kg",
            "600",
            "650",
            "2",
            "50",
            "2"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> Veterinarians utilize cumulative frequency ogives in commercial poultry broiler farms to evaluate flock weight uniformity. Plotting broiler weights against standard breed curves quickly reveals whether the 25th percentile (Q1) or 75th percentile (Q3) deviates, diagnosing stocking density overcrowding or inadequate feeder space.",
    "tags": [
      "Biostatistics Lab",
      "Histogram",
      "Frequency Polygon",
      "Ogive",
      "Median",
      "Mode",
      "Graphical Presentation"
    ]
  },
  "p1-t03": {
    "summary": "Step-by-step computation of Arithmetic Mean, Median, and Mode for ungrouped and continuous grouped livestock data with model exam solutions.",
    "desc": "<b>AIM:</b> To compute Arithmetic Mean, Median, and Mode from grouped livestock production data using standard biometrical formulas.<br><br><b>FORMULAS & CALCULATION RULES:</b><ul><li><b>Arithmetic Mean (\\bar{X}):</b><br>&bull; Direct Method: <code>\\bar{X} = (&Sigma; f_i x_i) / N</code><br>&bull; Short-cut (Assumed Mean) Method: <code>\\bar{X} = A + [ (&Sigma; f_i d_i) / N ] &times; h</code>, where <code>d_i = (x_i - A) / h</code>.</li><li><b>Median (M_e):</b><br>Find Median Class where cumulative frequency <code>cf &ge; N / 2</code>.<br><code>Median = L + [ (N/2 - m) / f ] &times; h</code><br>Where: <code>L</code> = Lower limit of median class; <code>m</code> = cumulative frequency of preceding class; <code>f</code> = frequency of median class; <code>h</code> = class width.</li><li><b>Mode (M_o):</b><br>Identify Modal Class having highest frequency (<code>f_1</code>).<br><code>Mode = L + [ (f_1 - f_0) / (2 f_1 - f_0 - f_2) ] &times; h</code><br>Where: <code>f_0</code> = frequency of preceding class; <code>f_2</code> = frequency of succeeding class.</li><li><b>Empirical Relationship:</b> <code>Mode = 3 &times; Median - 2 &times; Mean</code> (for moderately skewed distributions).</li></ul><br><b>MODEL EXAM PROBLEM:</b><br>Calculate Mean, Median, and Mode for 305-day lactation yields (hundred kg) of 40 crossbred dairy cows:<br><code>20–25 (f=5), 25–30 (f=8), 30–35 (f=15), 35–40 (f=8), 40–45 (f=4)</code>; Total N = 40.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><b>Mean:</b> Let assumed mean <code>A = 32.5</code>, <code>h = 5</code>.<br>&Sigma; f_i d_i = 5(-2) + 8(-1) + 15(0) + 8(+1) + 4(+2) = -10 - 8 + 0 + 8 + 8 = -2.<br><code>\\bar{X} = 32.5 + (-2 / 40) &times; 5 = 32.5 - 0.25 = 32.25</code> (i.e. 3,225 kg).</li><li><b>Median:</b> <code>N/2 = 40 / 2 = 20</code>. Preceding cf before 30–35 class is 13. Median class = 30–35.<br><code>L = 30, m = 13, f = 15, h = 5</code>.<br><code>Median = 30 + [ (20 - 13) / 15 ] &times; 5 = 30 + (7/15 &times; 5) = 30 + 2.33 = 32.33</code> (3,233 kg).</li><li><b>Mode:</b> Modal class = 30–35 (highest f = 15).<br><code>L = 30, f_1 = 15, f_0 = 8, f_2 = 8, h = 5</code>.<br><code>Mode = 30 + [ (15 - 8) / (2(15) - 8 - 8) ] &times; 5 = 30 + [ 7 / (30 - 16) ] &times; 5 = 30 + (7/14 &times; 5) = 30 + 2.50 = 32.50</code> (3,250 kg).</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Which average is best for skewed biological data like somatic cell counts or parasite egg counts?</b><br><b>A:</b> <b>Median</b>, because it is unaffected by extreme outliers.</li><li><b>Q: What happens to mean, median, and mode in a perfectly symmetrical normal distribution?</b><br><b>A:</b> They are identical and coincide: <code>Mean = Median = Mode</code>.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Check consistency via empirical rule: <code>Mode &approx; 3(32.33) - 2(32.25) = 96.99 - 64.50 = 32.49</code> (matches calculated 32.50 perfectly!). Showing this cross-check in practical answer booklets guarantees full marks.</li><li>Always state the units (kg, days, grams). Leaving answers as bare numbers without units loses 0.5 to 1 mark.</li></ul>",
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
        "headers": [
          "Class Interval (100 kg)",
          "Mid-value (x_i)",
          "Frequency (f_i)",
          "d_i = (x_i - 32.5)/5",
          "f_i * d_i",
          "Cumulative Freq (cf)"
        ],
        "rows": [
          [
            "20 – 25",
            "22.5",
            "5",
            "-2",
            "-10",
            "5"
          ],
          [
            "25 – 30",
            "27.5",
            "8",
            "-1",
            "-8",
            "13 (m)"
          ],
          [
            "30 – 35 (Median/Modal)",
            "32.5 (A)",
            "15 (f_1)",
            "0",
            "0",
            "28"
          ],
          [
            "35 – 40",
            "37.5",
            "8 (f_2)",
            "+1",
            "+8",
            "36"
          ],
          [
            "40 – 45",
            "42.5",
            "4",
            "+2",
            "+8",
            "40"
          ],
          [
            "Total",
            "—",
            "N = 40",
            "—",
            "&Sigma; f_i d_i = -2",
            "—"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> When analyzing herd calving-to-conception intervals (days open), a few problem cows with uterine infections take > 300 days to conceive. The mean is severely inflated by these outliers, making herd fertility look poor. Veterinarians report the <b>Median Days Open</b> as the true clinical indicator of herd reproductive health.",
    "tags": [
      "Biostatistics Lab",
      "Arithmetic Mean",
      "Median",
      "Mode",
      "Central Tendency",
      "Assumed Mean",
      "Grouping Method"
    ]
  },
  "p1-t04": {
    "summary": "Estimation of Range, Variance, Standard Deviation, Standard Error of Mean, and Coefficient of Variation for livestock phenotypic traits with full model calculation.",
    "desc": "<b>AIM:</b> To calculate Variance (s&sup2;), Standard Deviation (s), Standard Error of Mean (SE_\\bar{x}), and Coefficient of Variation (CV%) from sample livestock records.<br><br><b>FORMULAS & EQUATIONS:</b><ul><li><b>Sample Variance (s&sup2;):</b><br><code>s&sup2; = [ &Sigma; x&sup2; - (&Sigma; x)&sup2; / n ] / (n - 1)</code> (Raw data, using Bessel's correction with n-1 degrees of freedom).</li><li><b>Grouped Data Variance:</b><br><code>s&sup2; = h&sup2; &times; [ { &Sigma; f d&sup2; - (&Sigma; f d)&sup2; / N } / (N - 1) ]</code></li><li><b>Standard Deviation (s):</b> <code>s = &radic;(s&sup2;)</code></li><li><b>Standard Error of Mean (SE_\\bar{x}):</b> <code>SE_\\bar{x} = s / &radic;n</code></li><li><b>Coefficient of Variation (CV%):</b> <code>CV% = (s / \\bar{X}) &times; 100</code></li></ul><br><b>MODEL EXAM PROBLEM:</b><br>The body weights (kg) of 8 Beetal kids at 3 months of age were recorded as:<br><code>12, 15, 14, 11, 16, 13, 15, 18</code>.<br>Calculate Mean, Standard Deviation, Standard Error, and CV%.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><code>n = 8</code></li><li><code>&Sigma; x = 12 + 15 + 14 + 11 + 16 + 13 + 15 + 18 = 114</code> kg.</li><li><code>Mean (\\bar{X}) = 114 / 8 = 14.25</code> kg.</li><li><code>&Sigma; x&sup2; = 12&sup2; + 15&sup2; + 14&sup2; + 11&sup2; + 16&sup2; + 13&sup2; + 15&sup2; + 18&sup2; = 144 + 225 + 196 + 121 + 256 + 169 + 225 + 324 = 1660</code>.</li><li><code>Correction Factor (CF) = (&Sigma; x)&sup2; / n = (114)&sup2; / 8 = 12996 / 8 = 1624.5</code>.</li><li><code>Sum of Squares (SS) = &Sigma; x&sup2; - CF = 1660 - 1624.5 = 35.5</code>.</li><li><code>Sample Variance (s&sup2;) = SS / (n - 1) = 35.5 / (8 - 1) = 35.5 / 7 = 5.071</code> kg&sup2;.</li><li><code>Standard Deviation (s) = &radic;5.071 = 2.252</code> kg.</li><li><code>Standard Error (SE) = s / &radic;n = 2.252 / &radic;8 = 2.252 / 2.828 = 0.796</code> kg.</li><li><code>CV% = (2.252 / 14.25) &times; 100 = 15.80%</code>.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Why do we divide by (n - 1) instead of n when computing sample variance?</b><br><b>A:</b> Dividing by (n - 1) is <b>Bessel's correction</b>; it provides an <b>unbiased estimate</b> of the true population variance (&sigma;&sup2;) because one degree of freedom is lost estimating the sample mean.</li><li><b>Q: What is the biological significance of CV%?</b><br><b>A:</b> CV is unitless and allows direct comparison of variability between traits with different units (e.g., comparing variability of body weight in kg vs milk yield in liters).</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Express reporting format: Always write final answer as: <code>Mean &plusmn; SE = 14.25 &plusmn; 0.80 kg (CV = 15.80%)</code>. This is the exact scientific format expected by external examiners.</li><li>Remember: Variance has squared units (kg&sup2;), SD has original units (kg), and CV has percentage (%) or no units. Writing wrong units leads to immediate point loss.</li></ul>",
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
        "headers": [
          "Individual Kid No.",
          "Body Weight x (kg)",
          "Deviation (x - X̄)",
          "(x - X̄)²",
          "Raw Square (x²)"
        ],
        "rows": [
          [
            "1",
            "12",
            "-2.25",
            "5.0625",
            "144"
          ],
          [
            "2",
            "15",
            "+0.75",
            "0.5625",
            "225"
          ],
          [
            "3",
            "14",
            "-0.25",
            "0.0625",
            "196"
          ],
          [
            "4",
            "11",
            "-3.25",
            "10.5625",
            "121"
          ],
          [
            "5",
            "16",
            "+1.75",
            "3.0625",
            "256"
          ],
          [
            "6",
            "13",
            "-1.25",
            "1.5625",
            "169"
          ],
          [
            "7",
            "15",
            "+0.75",
            "0.5625",
            "225"
          ],
          [
            "8",
            "18",
            "+3.75",
            "14.0625",
            "324"
          ],
          [
            "Total (&Sigma;)",
            "114",
            "0.00",
            "SS = 35.50",
            "&Sigma;x² = 1660"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In commercial poultry broiler production, flock uniformity is judged by CV% at 35 days of age. A <b>CV &le; 8%</b> indicates exceptional flock uniformity, allowing automated processing line slaughter without carcass jamming. A <b>CV > 14%</b> signals uneven feeding, subclinical coccidiosis, or poor ventilation distribution.",
    "tags": [
      "Biostatistics Lab",
      "Standard Deviation",
      "Variance",
      "Standard Error",
      "CV%",
      "Bessel's Correction",
      "Sum of Squares"
    ]
  },
  "p1-t05": {
    "summary": "Practical numerical problem solving on additive/multiplicative probability rules and finding probabilities under the Standard Normal Curve (Z-distribution).",
    "desc": "<b>AIM:</b> To solve practical numerical problems on livestock probability and compute probabilities of performance traits using Standard Normal Z-tables.<br><br><b>CORE PRINCIPLES & FORMULAS:</b><ul><li><b>Addition Rule:</b> <code>P(A &cup; B) = P(A) + P(B) - P(A &cap; B)</code> (for mutually exclusive events, <code>P(A &cap; B) = 0</code>).</li><li><b>Multiplication Rule:</b> <code>P(A &cap; B) = P(A) &times; P(B)</code> (for independent events).</li><li><b>Standard Normal Variate (Z):</b><br><code>Z = (X - &mu;) / &sigma;</code><br>Transforms any normal distribution <code>N(&mu;, &sigma;&sup2;)</code> into standard normal distribution <code>Z ~ N(0, 1)</code>.</li></ul><br><b>MODEL EXAM PROBLEM 1 (PROBABILITY):</b><br>A dairy herd has 60% Holstein crossbreds and 40% Jersey crossbreds. The probability of conception at first AI is 0.50 in Holsteins and 0.65 in Jerseys. If a randomly selected cow is inseminated, find the probability that she conceives.<br><b>Solution:</b> By Law of Total Probability:<br><code>P(Conception) = P(H) &times; P(C|H) + P(J) &times; P(C|J) = (0.60 &times; 0.50) + (0.40 &times; 0.65) = 0.30 + 0.26 = 0.56 (56%)</code>.<br><br><b>MODEL EXAM PROBLEM 2 (NORMAL DISTRIBUTION):</b><br>In a population of 1,000 Sahiwal cows, 305-day lactation milk yield is normally distributed with mean <code>&mu; = 2,500 kg</code> and standard deviation <code>&sigma; = 400 kg</code>.<br>1. What percentage of cows yield more than 3,100 kg?<br>2. How many cows are expected to yield between 2,100 kg and 2,900 kg?<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><b>For X = 3,100 kg:</b><br><code>Z = (3100 - 2500) / 400 = 600 / 400 = +1.50</code>.<br>From Z-table, area from 0 to 1.50 = 0.4332.<br>Area in upper tail <code>P(Z &gt; 1.50) = 0.5000 - 0.4332 = 0.0668 (6.68%)</code>.<br><b>Answer 1:</b> <b>6.68%</b> of cows yield > 3,100 kg.</li><li><b>For X between 2,100 kg and 2,900 kg:</b><br><code>Z_1 = (2100 - 2500) / 400 = -400 / 400 = -1.00</code>.<br><code>Z_2 = (2900 - 2500) / 400 = +400 / 400 = +1.00</code>.<br>Area for Z = 1.00 from mean is 0.3413.<br>Total Area between -1.00 and +1.00 = <code>0.3413 + 0.3413 = 0.6826 (68.26%)</code>.<br>Expected number of cows = <code>1000 &times; 0.6826 = 682.6 &approx; 683 cows</code>.<br><b>Answer 2:</b> <b>683 cows</b> yield between 2,100 kg and 2,900 kg.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What are the parameters of a Standard Normal Curve?</b><br><b>A:</b> Mean <code>&mu; = 0</code> and Standard Deviation <code>&sigma; = 1</code> (Variance &sigma;&sup2; = 1).</li><li><b>Q: What percentage of data falls within &mu; &plusmn; 1&sigma;, &mu; &plusmn; 2&sigma;, and &mu; &plusmn; 3&sigma;?</b><br><b>A:</b> <b>68.27%</b> falls within &plusmn;1&sigma;, <b>95.45%</b> falls within &plusmn;2&sigma;, and <b>99.73%</b> falls within &plusmn;3&sigma; (Empirical Rule).</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Always draw a small bell-shaped curve sketch showing the shaded area in your answer sheet. Examiners award full marks for proper visual representation.</li><li>Check table direction: Ensure whether the provided Z-table gives area from <code>0 to Z</code> (0.3413 for Z=1) or cumulative from <code>-&infin; to Z</code> (0.8413 for Z=1).</li></ul>",
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
        "headers": [
          "Z-Score (Standard Deviations)",
          "Area from Mean to Z",
          "Two-Tailed Area (Within &plusmn; Z)",
          "Upper Tail Area (Z &gt; z)",
          "Livestock Selection Percentile"
        ],
        "rows": [
          [
            "0.50",
            "0.1915",
            "0.3829 (38.29%)",
            "0.3085 (30.85%)",
            "69.15th percentile"
          ],
          [
            "1.00",
            "0.3413",
            "0.6827 (68.27%)",
            "0.1587 (15.87%)",
            "84.13th percentile"
          ],
          [
            "1.28",
            "0.3997",
            "0.7995 (80.00%)",
            "0.1000 (10.00%)",
            "Top 10% replacement heifers"
          ],
          [
            "1.50",
            "0.4332",
            "0.8664 (86.64%)",
            "0.0668 (6.68%)",
            "Top 6.7% elite donor cows"
          ],
          [
            "1.645",
            "0.4500",
            "0.9000 (90.00%)",
            "0.0500 (5.00%)",
            "5% significance critical value"
          ],
          [
            "1.96",
            "0.4750",
            "0.9500 (95.00%)",
            "0.0250 (2.50%)",
            "95% confidence interval bound"
          ],
          [
            "2.33",
            "0.4901",
            "0.9802 (98.02%)",
            "0.0099 (1.00%)",
            "Top 1% elite AI breeding sires"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> Veterinary clinical pathology laboratories establish serum biochemical reference intervals (e.g., serum calcium 9.0–11.5 mg/dl) as <code>&mu; &plusmn; 2&sigma;</code> (enclosing 95% of healthy cows). Any transition cow testing below <code>Z = -2.0</code> (serum Ca < 8.0 mg/dl) is diagnosed with clinical or subclinical hypocalcemia (milk fever) and immediately infused with intravenous calcium borogluconate.",
    "tags": [
      "Biostatistics Lab",
      "Normal Distribution",
      "Z-Score",
      "Probability",
      "Standard Normal Curve",
      "Z-Table",
      "Milk Yield"
    ]
  },
  "p1-t06": {
    "summary": "Computation of Pearson's Correlation Coefficient (r) and linear regression equations (Y on X) from animal experimental data with full test of significance.",
    "desc": "<b>AIM:</b> To estimate Pearson's product-moment correlation coefficient (r) and fit a linear regression equation (Y on X) to predict body weight from heart girth in livestock.<br><br><b>FORMULAS & EQUATIONS:</b><ul><li><b>Pearson's Correlation Coefficient (r):</b><br><code>r = [ &Sigma;xy - (&Sigma;x &times; &Sigma;y) / n ] / &radic;[ { &Sigma;x&sup2; - (&Sigma;x)&sup2; / n } &times; { &Sigma;y&sup2; - (&Sigma;y)&sup2; / n } ]</code><br><code>r = SP_xy / &radic;(SS_x &times; SS_y)</code>.</li><li><b>Regression Coefficient of Y on X (b_yx):</b><br><code>b_yx = SP_xy / SS_x = r &times; (s_y / s_x)</code></li><li><b>Regression Line Equation (Y on X):</b><br><code>(Y - \\bar{Y}) = b_yx &times; (X - \\bar{X})  &rarr;  Y = a + b_yx &times; X</code><br>Where intercept <code>a = \\bar{Y} - b_yx &times; \\bar{X}</code>.</li><li><b>Test of Significance for r (t-test):</b><br><code>t = [ r &times; &radic;(n - 2) ] / &radic;(1 - r&sup2;)</code> with <code>df = n - 2</code>.</li></ul><br><b>MODEL EXAM PROBLEM:</b><br>Data on Heart Girth (X, cm) and Body Weight (Y, kg) recorded in 6 crossbred calves:<br><code>X: 80, 85, 90, 95, 100, 105</code><br><code>Y: 65, 72, 80, 88, 98, 107</code><br>Calculate 'r', derive the prediction equation, and predict weight for a calf with 110 cm girth.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><code>n = 6</code></li><li><code>&Sigma;X = 555</code>, <code>\\bar{X} = 92.5</code> cm.</li><li><code>&Sigma;Y = 510</code>, <code>\\bar{Y} = 85.0</code> kg.</li><li><code>&Sigma;X&sup2; = 80&sup2; + 85&sup2; + 90&sup2; + 95&sup2; + 100&sup2; + 105&sup2; = 51,775</code>.</li><li><code>SS_x = 51,775 - (555)&sup2; / 6 = 51,775 - 51,337.5 = 437.5</code>.</li><li><code>&Sigma;Y&sup2; = 65&sup2; + 72&sup2; + 80&sup2; + 88&sup2; + 98&sup2; + 107&sup2; = 44,546</code>.</li><li><code>SS_y = 44,546 - (510)&sup2; / 6 = 44,546 - 43,350 = 1,196.0</code>.</li><li><code>&Sigma;XY = (80&times;65) + (85&times;72) + (90&times;80) + (95&times;88) + (100&times;98) + (105&times;107) = 5,200 + 6,120 + 7,200 + 8,360 + 9,800 + 11,235 = 47,915</code>.</li><li><code>SP_xy = 47,915 - (555 &times; 510) / 6 = 47,915 - 47,175 = 740.0</code>.</li><li><b>Correlation Coefficient (r):</b><br><code>r = 740.0 / &radic;(437.5 &times; 1196.0) = 740.0 / &radic;523,250 = 740.0 / 723.36 = +0.9953</code> (Strong positive correlation).</li><li><b>Regression Coefficient (b_yx):</b><br><code>b_yx = SP_xy / SS_x = 740.0 / 437.5 = 1.6914</code> kg/cm.</li><li><b>Intercept (a):</b><br><code>a = \\bar{Y} - b_yx &times; \\bar{X} = 85.0 - (1.6914 &times; 92.5) = 85.0 - 156.455 = -71.455</code>.</li><li><b>Regression Equation:</b> <code>Y = -71.455 + 1.6914 &times; X</code>.</li><li><b>Prediction for X = 110 cm:</b><br><code>Y = -71.455 + 1.6914(110) = -71.455 + 186.054 = 114.60 kg</code>.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What is the range of values for r and can it be negative?</b><br><b>A:</b> Correlation coefficient <code>r</code> ranges from <b>-1.0 to +1.0</b>. Negative <code>r</code> means an increase in X leads to a proportional decrease in Y.</li><li><b>Q: What is the Coefficient of Determination (r&sup2;)?</b><br><b>A:</b> <code>r&sup2; = (0.9953)&sup2; = 0.9906 (99.06%)</code>; indicates that 99.06% of the total variation in body weight is directly explained by variation in heart girth!</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Remember the fundamental identity: <code>b_yx &times; b_xy = r&sup2;</code>. Both regression coefficients must always have the same mathematical sign as <code>r</code>!</li><li>Degrees of freedom for testing correlation significance is always <code>n - 2</code>, NOT n - 1.</li></ul>",
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
        "headers": [
          "Calf No.",
          "Heart Girth X (cm)",
          "Body Weight Y (kg)",
          "X²",
          "Y²",
          "XY"
        ],
        "rows": [
          [
            "1",
            "80",
            "65",
            "6400",
            "4225",
            "5200"
          ],
          [
            "2",
            "85",
            "72",
            "7225",
            "5184",
            "6120"
          ],
          [
            "3",
            "90",
            "80",
            "8100",
            "6400",
            "7200"
          ],
          [
            "4",
            "95",
            "88",
            "9025",
            "7744",
            "8360"
          ],
          [
            "5",
            "100",
            "98",
            "10000",
            "9604",
            "9800"
          ],
          [
            "6",
            "105",
            "107",
            "11025",
            "11449",
            "11235"
          ],
          [
            "Total (&Sigma;)",
            "555",
            "510",
            "51775",
            "44546",
            "47915"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In rural Indian veterinary practice, weighing balances for heavy cattle and buffaloes are unavailable. Veterinarians utilize derived regression formulas (such as <b>Shaeffer's formula: Body Weight (lbs) = (Heart Girth &times; Length) / 300</b>) to accurately estimate patient body weight for calculating correct therapeutic doses of general anesthetics, anthelmintics, and antibiotics.",
    "tags": [
      "Biostatistics Lab",
      "Correlation",
      "Regression",
      "Pearson r",
      "Heart Girth",
      "Body Weight",
      "Prediction Equation"
    ]
  },
  "p1-t07": {
    "summary": "Application of Large Sample Z-tests for testing the significance of single mean, difference between two means, single proportion, and difference between two proportions.",
    "desc": "<b>AIM:</b> To apply Large Sample Z-tests (sample size N &ge; 30) for testing hypotheses concerning livestock means and proportions.<br><br><b>TEST STATISTIC FORMULAS:</b><ul><li><b>Case 1: Single Mean Z-test:</b><br><code>Z_cal = | \\bar{X} - &mu; | / (s / &radic;n)</code></li><li><b>Case 2: Difference of Two Means Z-test:</b><br><code>Z_cal = | \\bar{X}_1 - \\bar{X}_2 | / &radic;[ (s_1&sup2; / n_1) + (s_2&sup2; / n_2) ]</code></li><li><b>Case 3: Single Proportion Z-test:</b><br><code>Z_cal = | p - P | / &radic;[ P(1 - P) / n ]</code></li><li><b>Case 4: Difference of Two Proportions Z-test:</b><br><code>Z_cal = | p_1 - p_2 | / &radic;[ \\hat{P}(1 - \\hat{P}) &times; (1/n_1 + 1/n_2) ]</code><br>Where pooled proportion <code>\\hat{P} = (x_1 + x_2) / (n_1 + n_2)</code>.</li><li><b>Decision Rule:</b><br>&bull; If <code>|Z_cal| &gt; 1.96</code> &rarr; Reject H0 at <b>5% level of significance</b> (P &lt; 0.05, Significant).<br>&bull; If <code>|Z_cal| &gt; 2.58</code> &rarr; Reject H0 at <b>1% level of significance</b> (P &lt; 0.01, Highly Significant).</li></ul><br><b>MODEL EXAM PROBLEM (DIFFERENCE OF TWO MEANS):</b><br>A field trial was conducted on 50 Murrah buffaloes fed a bypass-fat supplement and 50 control buffaloes. The supplement group averaged 11.2 kg milk/day with SD = 1.8 kg. The control group averaged 10.1 kg milk/day with SD = 2.0 kg. Test whether bypass-fat significantly increased milk yield.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><b>Hypotheses:</b><br>Null Hypothesis H0: <code>&mu;_1 = &mu;_2</code> (Bypass-fat has no effect on milk yield).<br>Alternative Hypothesis H1: <code>&mu;_1 &ne; &mu;_2</code> (Two-tailed) or <code>&mu;_1 &gt; &mu;_2</code>.</li><li><code>n_1 = 50, \\bar{X}_1 = 11.2, s_1 = 1.8</code></li><li><code>n_2 = 50, \\bar{X}_2 = 10.1, s_2 = 2.0</code></li><li><b>Standard Error of Difference:</b><br><code>SE = &radic;[ (s_1&sup2; / n_1) + (s_2&sup2; / n_2) ] = &radic;[ (1.8&sup2; / 50) + (2.0&sup2; / 50) ] = &radic;[ (3.24 / 50) + (4.00 / 50) ] = &radic;[ 0.0648 + 0.0800 ] = &radic;0.1448 = 0.3805 kg</code>.</li><li><b>Calculate Z:</b><br><code>Z_cal = (11.2 - 10.1) / 0.3805 = 1.1 / 0.3805 = 2.891</code>.</li><li><b>Conclusion:</b> Since <code>Z_cal = 2.891 &gt; 2.58</code> (critical value at 1%), the null hypothesis H0 is <b>rejected at P &lt; 0.01</b>.<br><i>Inference:</i> Bypass-fat supplementation produced a <b>highly significant (P &lt; 0.01) increase</b> in daily milk yield.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What sample size qualifies as a 'Large Sample' in biostatistics?</b><br><b>A:</b> A sample size of <code>n &ge; 30</code> is classified as a large sample, as the sampling distribution of the mean approaches normality under the Central Limit Theorem.</li><li><b>Q: Why do we not need degrees of freedom in Z-tests?</b><br><b>A:</b> Because for large samples (n &ge; 30), the sample standard deviation (s) is an extremely accurate estimate of the population standard deviation (&sigma;), so the distribution is standard normal with infinite degrees of freedom.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Memorize critical Z-table values: Two-tailed 5% = <b>1.96</b>; 1% = <b>2.58</b>; 0.1% = <b>3.29</b>. One-tailed 5% = <b>1.645</b>; 1% = <b>2.33</b>.</li><li>Always state H0 and H1 explicitly at the beginning of your answer to secure the mandatory 1-mark hypothesis formulation allotment.</li></ul>",
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
        "headers": [
          "Significance Level (&alpha;)",
          "Test Type",
          "Critical Z-value (Z_tab)",
          "Decision Rule",
          "Statistical Inference"
        ],
        "rows": [
          [
            "5% (P = 0.05)",
            "Two-tailed",
            "1.96",
            "Reject H0 if |Z_cal| &gt; 1.96",
            "Significant difference (P &lt; 0.05)"
          ],
          [
            "1% (P = 0.01)",
            "Two-tailed",
            "2.58",
            "Reject H0 if |Z_cal| &gt; 2.58",
            "Highly significant difference (P &lt; 0.01)"
          ],
          [
            "0.1% (P = 0.001)",
            "Two-tailed",
            "3.29",
            "Reject H0 if |Z_cal| &gt; 3.29",
            "Very highly significant (P &lt; 0.001)"
          ],
          [
            "5% (P = 0.05)",
            "One-tailed (Directional)",
            "1.645",
            "Reject H0 if Z_cal &gt; +1.645",
            "Significant directional superiority"
          ],
          [
            "1% (P = 0.01)",
            "One-tailed (Directional)",
            "2.33",
            "Reject H0 if Z_cal &gt; +2.33",
            "Highly significant directional gain"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In state livestock vaccination campaigns, veterinarians use large-sample proportion Z-tests to verify vaccine efficacy. If 85 out of 100 vaccinated calves show protective antibody titers compared to only 40 out of 100 unvaccinated controls, a Z-test on proportions confirms that the vaccine confers statistically significant protection against clinical infection.",
    "tags": [
      "Biostatistics Lab",
      "Z-Test",
      "Large Sample",
      "Significance Testing",
      "Null Hypothesis",
      "Murrah Buffalo",
      "Bypass Fat"
    ]
  },
  "p1-t08": {
    "summary": "Student's t-test applications for small samples (n < 30): One-sample t-test, Independent Two-sample t-test (equal variance), and Paired t-test for before-and-after clinical trials.",
    "desc": "<b>AIM:</b> To apply Student's t-test for small samples (n &lt; 30) across independent and paired clinical veterinary investigations.<br><br><b>CORE STATISTICAL FORMULAS:</b><ul><li><b>1. Independent Two-Sample t-test (Equal Variances):</b><br><code>t_cal = | \\bar{X}_1 - \\bar{X}_2 | / [ s_p &times; &radic;(1/n_1 + 1/n_2) ]</code><br>Where Pooled Variance <code>s_p&sup2; = [ (n_1 - 1)s_1&sup2; + (n_2 - 1)s_2&sup2; ] / (n_1 + n_2 - 2)</code> with <code>df = n_1 + n_2 - 2</code>.</li><li><b>2. Paired t-test (Before & After Trial on Same Animals):</b><br><code>t_cal = | \\bar{d} | / (s_d / &radic;n)</code><br>Where <code>d_i = X_{after} - X_{before}</code>, <code>\\bar{d} = (&Sigma; d) / n</code>, and <code>s_d&sup2; = [ &Sigma;d&sup2; - (&Sigma;d)&sup2;/n ] / (n - 1)</code> with <code>df = n - 1</code>.</li></ul><br><b>MODEL EXAM PROBLEM (PAIRED t-TEST):</b><br>A novel herbal anthelmintic was evaluated in 6 sheep naturally infected with <i>Haemonchus contortus</i>. Fecal Egg Counts (EPG in hundreds) before and 14 days after treatment were:<br><code>Before: 28, 35, 42, 30, 25, 38</code><br><code>After : 10, 12, 18, 14,  8, 16</code><br>Test whether the anthelmintic significantly reduced fecal egg counts (t_tab at df=5 for 5% = 2.571, for 1% = 4.032).<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><b>Compute Differences <code>d_i = Before - After</code>:</b><br>Sheep 1: <code>28 - 10 = 18</code><br>Sheep 2: <code>35 - 12 = 23</code><br>Sheep 3: <code>42 - 18 = 24</code><br>Sheep 4: <code>30 - 14 = 16</code><br>Sheep 5: <code>25 -  8 = 17</code><br>Sheep 6: <code>38 - 16 = 22</code></li><li><code>n = 6</code>, <code>&Sigma; d = 18 + 23 + 24 + 16 + 17 + 22 = 120</code>.</li><li><code>Mean Difference (\\bar{d}) = 120 / 6 = 20.0</code>.</li><li><code>&Sigma; d&sup2; = 18&sup2; + 23&sup2; + 24&sup2; + 16&sup2; + 17&sup2; + 22&sup2; = 324 + 529 + 576 + 256 + 289 + 484 = 2,458</code>.</li><li><code>SS_d = 2,458 - (120)&sup2; / 6 = 2,458 - 2,400 = 58.0</code>.</li><li><code>s_d&sup2; = 58.0 / (6 - 1) = 58.0 / 5 = 11.6</code>; <code>s_d = &radic;11.6 = 3.406</code>.</li><li><code>SE_\\bar{d} = 3.406 / &radic;6 = 3.406 / 2.4495 = 1.3905</code>.</li><li><b>Calculate t:</b><br><code>t_cal = 20.0 / 1.3905 = 14.383</code>.</li><li><b>Degrees of Freedom:</b> <code>df = 6 - 1 = 5</code>.</li><li><b>Inference:</b> Since <code>t_cal = 14.383 &gt; t_tab(5, 0.01) = 4.032</code>, H0 is rejected at <b>P &lt; 0.001 (Very Highly Significant)</b>.<br><i>Conclusion:</i> The herbal anthelmintic produced a dramatic and highly significant reduction in EPG.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Who developed the t-test and why was it published under the pseudonym 'Student'?</b><br><b>A:</b> Developed by <b>William Sealy Gosset (1908)</b> while working at the Guinness Brewery, which prohibited employees from publishing scientific papers under their real names.</li><li><b>Q: What are the three core assumptions of Student's t-test?</b><br><b>A:</b> (a) The parent population is normally distributed, (b) Samples are randomly drawn, and (c) In independent samples, population variances are equal (&sigma;1&sup2; = &sigma;2&sup2; - homoscedasticity).</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>In independent two-sample t-tests, verify equality of variances using Fisher's F-test: <code>F = s1&sup2; / s2&sup2;</code> before pooling! If variances are unequal, standard pooling is invalid (Behrens-Fisher problem).</li><li>Degrees of freedom must be stated explicitly: <code>df = n1 + n2 - 2</code> for two-sample; <code>df = n - 1</code> for paired t-test.</li></ul>",
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
        "headers": [
          "Sheep ID",
          "Pre-treatment EPG (x1)",
          "Post-treatment EPG (x2)",
          "Difference d = x1 - x2",
          "Deviation (d - d̄)",
          "(d - d̄)²"
        ],
        "rows": [
          [
            "1",
            "28",
            "10",
            "18",
            "-2",
            "4"
          ],
          [
            "2",
            "35",
            "12",
            "23",
            "+3",
            "9"
          ],
          [
            "3",
            "42",
            "18",
            "24",
            "+4",
            "16"
          ],
          [
            "4",
            "30",
            "14",
            "16",
            "-4",
            "16"
          ],
          [
            "5",
            "25",
            "8",
            "17",
            "-3",
            "9"
          ],
          [
            "6",
            "38",
            "16",
            "22",
            "+2",
            "4"
          ],
          [
            "Total (&Sigma;)",
            "198",
            "78",
            "&Sigma;d = 120",
            "0",
            "SS_d = 58"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> Veterinary surgeons use paired t-tests in clinical trials evaluating post-operative analgesics or antipyretics. Measuring body temperature or pain scores in the same dogs <b>before administration (Hour 0) and 2 hours after administration</b> controls for individual physiological differences, reliably isolating the true drug efficacy.",
    "tags": [
      "Biostatistics Lab",
      "Student's t-Test",
      "Paired t-Test",
      "Small Sample",
      "Haemonchus",
      "Anthelmintic",
      "Degrees of Freedom"
    ]
  },
  "p1-t09": {
    "summary": "Chi-Square (χ²) test applications in animal genetics: Test of Goodness of Fit for Mendelian ratios, 2x2 contingency tables, test of independence, and Yates' correction for continuity.",
    "desc": "<b>AIM:</b> To apply Chi-Square (&chi;&sup2;) tests for verifying Mendelian phenotypic ratios (Goodness of Fit) and testing independence of clinical attributes in 2&times;2 contingency tables.<br><br><b>CORE STATISTICAL FORMULAS:</b><ul><li><b>General Chi-Square Formula:</b><br><code>&chi;&sup2; = &Sigma; [ (O - E)&sup2; / E ]</code><br>Where <code>O</code> = Observed Frequency; <code>E</code> = Expected Frequency; <code>df = k - 1</code> (where k = number of phenotypic classes).</li><li><b>Expected Frequency for Contingency Table:</b><br><code>E_ij = (Row Total_i &times; Column Total_j) / Grand Total (N)</code></li><li><b>Short-cut Formula for 2&times;2 Contingency Table:</b><br><code>&chi;&sup2; = [ N &times; (ad - bc)&sup2; ] / [ (a + b)(c + d)(a + c)(b + d) ]</code> with <code>df = (2 - 1)(2 - 1) = 1</code>.</li><li><b>Yates' Correction for Continuity (Mandatory when df = 1 and any cell E &lt; 5):</b><br><code>&chi;&sup2;_{corrected} = [ N &times; (|ad - bc| - N/2)&sup2; ] / [ (a + b)(c + d)(a + c)(b + d) ]</code></li></ul><br><b>MODEL EXAM PROBLEM 1 (GOODNESS OF FIT):</b><br>In a sheep breeding experiment involving cross of heterozygous polled rams with horned ewes, the offspring showed <b>115 polled and 85 horned lambs</b>. Test whether this segregates according to the expected 1:1 Mendelian test-cross ratio (&chi;&sup2;_tab at df=1 for 5% = 3.841).<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li>Null Hypothesis H0: The data conforms to the theoretical 1:1 ratio.</li><li>Total lambs <code>N = 115 + 85 = 200</code>.</li><li>Expected frequency of Polled = <code>200 &times; (1/2) = 100</code>.</li><li>Expected frequency of Horned = <code>200 &times; (1/2) = 100</code>.</li><li><code>&chi;&sup2; = [ (115 - 100)&sup2; / 100 ] + [ (85 - 100)&sup2; / 100 ] = [ (15)&sup2; / 100 ] + [ (-15)&sup2; / 100 ] = 225/100 + 225/100 = 2.25 + 2.25 = 4.50</code>.</li><li><code>df = k - 1 = 2 - 1 = 1</code>.</li><li><b>Inference:</b> Since <code>&chi;&sup2;_cal = 4.50 &gt; &chi;&sup2;_tab = 3.841</code>, H0 is <b>rejected at 5% significance level</b>.<br><i>Conclusion:</i> The observed phenotypic ratio deviates significantly from the Mendelian 1:1 expectation.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: When is Yates' Correction for continuity strictly applied?</b><br><b>A:</b> Strictly applied in <b>2&times;2 contingency tables (df = 1)</b> when any expected cell frequency is small (&lt; 5), subtracting N/2 from |ad - bc| to adjust for approximating a discrete binomial with a continuous chi-square curve.</li><li><b>Q: What are the two mandatory conditions for validity of Chi-Square test?</b><br><b>A:</b> (a) Total sample size N should be reasonably large (&ge; 50), and (b) No expected cell frequency should be less than 5 (if &lt; 5, combine adjacent classes).</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Always verify that <code>&Sigma; O = &Sigma; E = N</code>. If total expected does not match total observed, the calculation is wrong.</li><li>Memorize the critical &chi;&sup2; values: df=1 &rarr; <b>3.841</b> (5%) & <b>6.635</b> (1%); df=2 &rarr; <b>5.991</b>; df=3 &rarr; <b>7.815</b>.</li></ul>",
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
        "headers": [
          "Breed Class",
          "Mastitis Positive (a, c)",
          "Mastitis Negative (b, d)",
          "Row Total (R_i)",
          "Expected Positive (E)",
          "Cell &chi;&sup2; = (O - E)&sup2;/E"
        ],
        "rows": [
          [
            "Exotic Crossbreds (HF)",
            "40 (O1)",
            "60 (O2)",
            "100",
            "25.0",
            "(40 - 25)&sup2; / 25 = 9.00"
          ],
          [
            "Indigenous Zebu (Gir)",
            "10 (O3)",
            "90 (O4)",
            "100",
            "25.0",
            "(10 - 25)&sup2; / 25 = 9.00"
          ],
          [
            "Column Total (C_j)",
            "50",
            "150",
            "N = 200",
            "—",
            "&chi;&sup2; = 18.00 + 6.00 = 24.00"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> Veterinary epidemiologists utilize 2&times;2 Chi-Square contingency tables to establish risk factor associations. Testing <b>Breed (Crossbred vs Indigenous) against Clinical Mastitis occurrence</b> (&chi;&sup2; = 24.00, P &lt; 0.001) statistically confirms that exotic crossbred cows possess significantly higher vulnerability to clinical udder infections than indigenous Zebu cows.",
    "tags": [
      "Biostatistics Lab",
      "Chi-Square Test",
      "Goodness of Fit",
      "Contingency Table",
      "Yates' Correction",
      "Mendelian Ratio",
      "Mastitis"
    ]
  },
  "p1-t10": {
    "summary": "Analysis of Variance (ANOVA) for Completely Randomized Design (CRD) and Randomized Block Design (RBD) with Sums of Squares, F-test, and Critical Difference (CD).",
    "desc": "<b>AIM:</b> To perform one-way ANOVA for Completely Randomized Design (CRD) and two-way ANOVA for Randomized Block Design (RBD), test treatment significance using F-test, and calculate Critical Difference (CD).<br><br><b>ANOVA COMPUTATION STEPS (CRD - ONE WAY):</b><ol><li><b>Correction Factor (CF):</b> <code>CF = G&sup2; / N</code> (where G = Grand Total, N = total observations).</li><li><b>Total Sum of Squares (TSS):</b> <code>TSS = &Sigma; &Sigma; X_{ij}&sup2; - CF</code> (with <code>df = N - 1</code>).</li><li><b>Treatment Sum of Squares (TrSS):</b> <code>TrSS = &Sigma; (T_i&sup2; / n_i) - CF</code> (with <code>df = k - 1</code>, where k = treatments).</li><li><b>Error Sum of Squares (ESS):</b> <code>ESS = TSS - TrSS</code> (with <code>df = N - k</code>).</li><li><b>Mean Sum of Squares:</b> <code>TrMS = TrSS / (k - 1)</code>; <code>EMS = ESS / (N - k)</code>.</li><li><b>F-Statistic:</b> <code>F_cal = TrMS / EMS</code> with <code>df = (k - 1, N - k)</code>.</li><li><b>Critical Difference (CD):</b> <code>CD = t_tab &times; &radic;(2 &times; EMS / r)</code> (where r = replications per treatment).</li></ol><br><b>RBD (TWO-WAY ANOVA) EXTENSION:</b><ul><li>Block Sum of Squares (BSS): <code>BSS = &Sigma; (B_j&sup2; / k) - CF</code> (with <code>df = r - 1</code>).</li><li>Error Sum of Squares in RBD: <code>ESS = TSS - TrSS - BSS</code> with <code>df = (k - 1)(r - 1)</code>.</li></ul><br><b>MODEL EXAM PROBLEM (CRD):</b><br>Three rations (A, B, C) were fed to 4 broiler chicks each. The 6-week body weight gains (hundred grams) were:<br><code>Ration A: 12, 14, 11, 15 (T_A = 52)</code><br><code>Ration B: 16, 18, 15, 19 (T_B = 68)</code><br><code>Ration C: 20, 22, 19, 23 (T_C = 84)</code><br>Perform ANOVA and calculate CD (F_tab at df=2,9 for 5% = 4.26).<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><code>k = 3, r = 4, N = 12</code>.</li><li><code>G = 52 + 68 + 84 = 204</code>.</li><li><code>CF = (204)&sup2; / 12 = 41,616 / 12 = 3,468</code>.</li><li><code>&Sigma;&Sigma; X&sup2; = (12&sup2;+14&sup2;+11&sup2;+15&sup2;) + (16&sup2;+18&sup2;+15&sup2;+19&sup2;) + (20&sup2;+22&sup2;+19&sup2;+23&sup2;) = 686 + 1,166 + 1,774 = 3,626</code>.</li><li><code>TSS = 3,626 - 3,468 = 158.0</code> (df = 11).</li><li><code>TrSS = [ (52&sup2; + 68&sup2; + 84&sup2;) / 4 ] - 3,468 = [ (2704 + 4624 + 7056) / 4 ] - 3,468 = [ 14,384 / 4 ] - 3,468 = 3,596 - 3,468 = 128.0</code> (df = 2).</li><li><code>ESS = TSS - TrSS = 158.0 - 128.0 = 30.0</code> (df = 9).</li><li><code>TrMS = 128.0 / 2 = 64.0</code>.</li><li><code>EMS = 30.0 / 9 = 3.333</code>.</li><li><code>F_cal = TrMS / EMS = 64.0 / 3.333 = 19.20</code>.</li><li><b>Conclusion:</b> Since <code>F_cal = 19.20 &gt; F_tab(2, 9) = 4.26</code>, the ration treatments differ <b>highly significantly (P &lt; 0.01)</b>.</li><li><b>Critical Difference:</b> <code>SE_d = &radic;(2 &times; 3.333 / 4) = &radic;1.666 = 1.291</code>. For df=9 at 5%, <code>t = 2.262</code>.<br><code>CD = 2.262 &times; 1.291 = 2.92</code> (i.e. 292 g).</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What are the three fundamental principles of experimental design?</b><br><b>A:</b> (1) <b>Randomization</b> (eliminates investigator bias), (2) <b>Replication</b> (provides error estimate), and (3) <b>Local Control</b> (reduces experimental error by blocking).</li><li><b>Q: How does RBD differ from CRD in local control?</b><br><b>A:</b> CRD uses only 2 principles (Randomization and Replication) for completely homogenous experimental units; RBD uses all 3 principles (Local Control via blocking along one gradient).</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Construct the complete ANOVA Summary Table with Columns: <code>Source of Variation | Degrees of Freedom | Sum of Squares | Mean Square | F_calculated | F_tabulated</code>. Missing this formatted table loses 2 marks.</li><li>Mean Comparison Ranking: State pair-wise differences: <code>Mean C (21) - Mean B (17) = 4.0 &gt; CD (2.92)</code> &rarr; Ration C is significantly superior to Ration B!</li></ul>",
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
        "headers": [
          "Source of Variation",
          "Degrees of Freedom (df)",
          "Sum of Squares (SS)",
          "Mean Square (MS)",
          "F_calculated",
          "F_tabulated (5%)"
        ],
        "rows": [
          [
            "Ration Treatments",
            "k - 1 = 2",
            "128.00",
            "64.00",
            "19.20**",
            "4.26"
          ],
          [
            "Experimental Error",
            "N - k = 9",
            "30.00",
            "3.33",
            "—",
            "—"
          ],
          [
            "Total",
            "N - 1 = 11",
            "158.00",
            "—",
            "—",
            "—"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In veterinary animal nutrition trials, researchers use RBD to test different protein supplementation levels in dairy cattle. Cows are blocked based on initial milk yield or parity into homogenous blocks (High, Medium, Low yielders) before assigning diets, ensuring differences in milk output are strictly attributable to feed protein rather than initial lactation potential.",
    "tags": [
      "Biostatistics Lab",
      "ANOVA",
      "CRD",
      "RBD",
      "F-Test",
      "Critical Difference",
      "Broiler Rations",
      "Sum of Squares"
    ]
  },
  "p1-t11": {
    "summary": "Practical execution of livestock data entry, statistical formula syntax, descriptive statistics, correlation, and ANOVA using MS-Excel in veterinary bio-computing.",
    "desc": "<b>AIM:</b> To enter livestock records into MS-Excel, apply statistical formulas, and execute automated Data Analysis Toolpak functions for descriptive statistics, correlation, and ANOVA.<br><br><b>STANDARD MS-EXCEL STATISTICAL FORMULAS (EXAM SPECIFIC):</b><ul><li><b>Mean:</b> <code>=AVERAGE(A2:A31)</code></li><li><b>Median:</b> <code>=MEDIAN(A2:A31)</code></li><li><b>Mode:</b> <code>=MODE.SNGL(A2:A31)</code></li><li><b>Sample Standard Deviation:</b> <code>=STDEV.S(A2:A31)</code> (Uses n - 1 Bessel's correction).</li><li><b>Sample Variance:</b> <code>=VAR.S(A2:A31)</code></li><li><b>Standard Error:</b> <code>=STDEV.S(A2:A31)/SQRT(COUNT(A2:A31))</code></li><li><b>Coefficient of Variation (CV%):</b> <code>=(STDEV.S(A2:A31)/AVERAGE(A2:A31))*100</code></li><li><b>Pearson Correlation:</b> <code>=CORREL(A2:A31, B2:B31)</code></li><li><b>Linear Regression Slope:</b> <code>=SLOPE(known_y's, known_x's)</code></li><li><b>Linear Regression Intercept:</b> <code>=INTERCEPT(known_y's, known_x's)</code></li><li><b>Student's t-test:</b> <code>=T.TEST(array1, array2, tails, type)</code> (Type: 1 = Paired; 2 = Two-sample equal variance).</li></ul><br><b>PROCEDURE FOR AUTOMATED DATA ANALYSIS TOOLPAK:</b><ol><li>Enable Toolpak: <code>File &rarr; Options &rarr; Add-Ins &rarr; Excel Add-ins (Go) &rarr; Check 'Analysis ToolPak' &rarr; OK</code>.</li><li>Navigate to <code>Data Tab &rarr; Data Analysis</code>.</li><li><b>For Descriptive Statistics:</b> Select 'Descriptive Statistics' &rarr; Select Input Range &rarr; Check 'Labels in first row' &rarr; Check 'Summary statistics' &rarr; Click OK.</li><li><b>For ANOVA:</b> Select 'Anova: Single Factor' (for CRD) or 'Anova: Two-Factor Without Replication' (for RBD) &rarr; Select data table range &rarr; Alpha = 0.05 &rarr; OK.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What is the difference between =STDEV.P and =STDEV.S in Excel?</b><br><b>A:</b> <code>=STDEV.P</code> divides by <code>N</code> (assumes data is the entire population); <code>=STDEV.S</code> divides by <code>n - 1</code> (sample standard deviation with Bessel's correction). Veterinarians must always use <code>=STDEV.S</code> for sample trials!</li><li><b>Q: How do you add a linear trendline and regression equation on a scatter plot in Excel?</b><br><b>A:</b> Right-click data points on scatter plot &rarr; Select 'Add Trendline' &rarr; Choose 'Linear' &rarr; Check 'Display Equation on chart' and 'Display R-squared value on chart'.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>In practical computer exams, always verify cell references: use absolute referencing <code>$A$2:$A$31</code> when dragging formulas across columns to prevent range shifts.</li><li>Excel ANOVA Single Factor output produces both <code>F</code> and <code>P-value</code>: if <code>P-value &lt; 0.05</code>, declare treatment significant immediately without checking F-critical tables.</li></ul>",
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
        "headers": [
          "Statistical Parameter",
          "Excel Function / Formula Syntax",
          "Input Argument Types",
          "Interpretation / Output"
        ],
        "rows": [
          [
            "Sample Mean",
            "=AVERAGE(B2:B51)",
            "Continuous numeric cells",
            "Arithmetic average of livestock trait"
          ],
          [
            "Sample Std Dev",
            "=STDEV.S(B2:B51)",
            "Sample data range",
            "Sample standard deviation (s) with df = n - 1"
          ],
          [
            "Standard Error",
            "=STDEV.S(B2:B51)/SQRT(COUNT(B2:B51))",
            "Formula combination",
            "SE of the mean for scientific reports"
          ],
          [
            "Pearson Correlation",
            "=CORREL(B2:B51, C2:C51)",
            "Two matched data arrays",
            "r value (-1.0 to +1.0)"
          ],
          [
            "Paired t-Test",
            "=T.TEST(B2:B20, C2:C20, 2, 1)",
            "Pre & post arrays, 2-tailed, type 1",
            "Direct P-value of paired comparison"
          ],
          [
            "One-Way ANOVA",
            "Data Analysis &rarr; Anova: Single Factor",
            "Grouped column ranges",
            "Complete ANOVA table with SS, MS, F and P-value"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> Veterinary officers managing district polyclinics maintain MS-Excel spreadsheets to log surgical cases, artificial inseminations, and rabies vaccinations. Using pivot tables and automated =AVERAGE and =STDEV.S formulas allows monthly generation of Disease Surveillance Reports (DSR) submitted directly to the State Department of Animal Husbandry.",
    "tags": [
      "Biostatistics Lab",
      "MS-Excel",
      "Bio-Computing",
      "STDEV.S",
      "AVERAGE",
      "CORREL",
      "ANOVA Toolpak",
      "Data Analysis"
    ]
  }
};

practicalData["prac-unit-2"] = {
  "p2-t01": {
    "summary": "Practical exercises on Monohybrid and Dihybrid crosses in livestock, demonstrating segregation, independent assortment, test-cross ratios, and Chi-Square verification.",
    "desc": "<b>AIM:</b> To solve monohybrid and dihybrid cross problems in livestock, formulate Punnett squares, determine genotypic and phenotypic ratios, and verify results using Chi-Square.<br><br><b>CORE MENDELIAN RATIOS:</b><ul><li><b>Monohybrid F2 Ratio:</b> Phenotypic = <code>3 : 1</code>; Genotypic = <code>1 : 2 : 1</code>.</li><li><b>Monohybrid Test Cross (Backcross to Recessive):</b> <code>1 : 1</code>.</li><li><b>Dihybrid F2 Ratio:</b> Phenotypic = <code>9 : 3 : 3 : 1</code>; Genotypic = <code>1:2:1:2:4:2:1:2:1</code>.</li><li><b>Dihybrid Test Cross:</b> <code>1 : 1 : 1 : 1</code>.</li></ul><br><b>MODEL EXAM PROBLEM 1 (MONOHYBRID LIVESTOCK CROSS):</b><br>In cattle, the polled condition (P) is dominant over the horned condition (p). A homozygous polled bull (PP) is mated to horned cows (pp).<br>1. Give the genotype and phenotype of F1 progeny.<br>2. If F1 individuals are inter-mated, what are the expected genotypic and phenotypic ratios in F2?<br>3. If an F1 polled bull is mated back to horned cows (test cross), what progeny are expected?<br><br><b>STEP-BY-STEP SOLUTION:</b><ol><li><b>Parents:</b> <code>PP (Polled Bull) &times; pp (Horned Cows)</code> &rarr; Gametes: <code>P</code> and <code>p</code>.<br><b>F1 Generation:</b> Genotype = <b>100% Pp (Heterozygous)</b>; Phenotype = <b>100% Polled</b>.</li><li><b>F1 &times; F1 Inter-se Mating:</b> <code>Pp &times; Pp</code>.<br>Gametes: 50% P, 50% p from each parent.<br>Punnett Square yields: <code>1 PP : 2 Pp : 1 pp</code>.<br><b>F2 Phenotypic Ratio:</b> <b>3 Polled : 1 Horned</b> (75% Polled, 25% Horned).<br><b>F2 Genotypic Ratio:</b> <b>1 PP : 2 Pp : 1 pp</b> (25% homozygous polled, 50% heterozygous polled, 25% horned).</li><li><b>Test Cross:</b> <code>Pp (F1 Bull) &times; pp (Horned Cow)</code>.<br>Gametes: Bull produces 1/2 P and 1/2 p; Cow produces 100% p.<br>Progeny: <code>1/2 Pp (Polled) : 1/2 pp (Horned)</code> &rarr; <b>1 : 1 Ratio</b>.</li></ol><br><b>MODEL EXAM PROBLEM 2 (DIHYBRID CROSS):</b><br>In cattle, Black coat (B) is dominant over Red coat (b), and Polled (P) is dominant over Horned (p). A homozygous black polled bull (BBPP) is crossed with a red horned cow (bbpp). Calculate the probability of obtaining a <b>Red Polled</b> calf in F2.<br><b>Solution:</b><br>In a dihybrid F2 (9:3:3:1), the phenotypic proportions are:<br><code>9/16 Black Polled (B_P_) : 3/16 Black Horned (B_pp) : 3/16 Red Polled (bbP_) : 1/16 Red Horned (bbpp)</code>.<br><b>Answer:</b> Probability of Red Polled (bbP_) = <b>3/16 (18.75%)</b>.<br><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What is a Test Cross and why is it performed in livestock?</b><br><b>A:</b> A cross of an individual of dominant phenotype with a homozygous recessive individual. It is used to determine whether a dominant animal (e.g., polled bull) is homozygous (PP) or heterozygous carrier (Pp).</li><li><b>Q: How many test-cross progeny without a single horned calf are needed to prove a bull homozygous polled with > 99% confidence?</b><br><b>A:</b> <code>(1/2)^n &lt; 0.01  &rarr;  n &ge; 7</code> calves (7 consecutive polled calves from horned dams prove homozygosity at P &gt; 0.99).</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Use the <b>Forked-Line (Branching) Method</b> for trihybrid or multihybrid crosses: combine individual monohybrid probabilities: <code>P(bbP_) = P(bb) &times; P(P_) = (1/4) &times; (3/4) = 3/16</code>. This saves 15 minutes compared to drawing a 16-cell Punnett square!</li><li>Formula for number of F2 gametes: <code>2^n</code>; number of F2 genotypes: <code>3^n</code>; number of F2 phenotypes: <code>2^n</code> (where n = number of heterozygous gene pairs).</li></ul>",
    "keyPoints": [
      "Monohybrid cross tracks one trait; F2 phenotypic ratio is 3:1, genotypic is 1:2:1.",
      "Dihybrid cross tracks two independent traits; F2 phenotypic ratio is 9:3:3:1.",
      "Test cross mates an unknown dominant phenotype with homozygous recessive.",
      "Monohybrid test cross gives a 1:1 ratio; dihybrid test cross gives 1:1:1:1.",
      "Polled (P) is dominant over horned (p) in cattle and sheep.",
      "Black coat color (B) is dominant over red coat color (b) in cattle.",
      "Number of distinct gametes produced is 2^n (n = heterozygous loci).",
      "Number of F2 genotypes is 3^n; number of F2 phenotypes is 2^n under complete dominance.",
      "Forked-line method calculates dihybrid probabilities by multiplying monohybrid fractions.",
      "Seven consecutive normal calves from recessive mates prove sire homozygosity at > 99% confidence."
    ],
    "tables": [
      {
        "title": "Dihybrid F2 Punnett Square for Coat Color and Horn Status in Cattle (BbPp x BbPp)",
        "headers": [
          "Female \\ Male Gametes",
          "BP (1/4)",
          "Bp (1/4)",
          "bP (1/4)",
          "bp (1/4)"
        ],
        "rows": [
          [
            "BP (1/4)",
            "BBPP (Black Polled)",
            "BBPp (Black Polled)",
            "BbPP (Black Polled)",
            "BbPp (Black Polled)"
          ],
          [
            "Bp (1/4)",
            "BBPp (Black Polled)",
            "BBpp (Black Horned)",
            "BbPp (Black Polled)",
            "Bbpp (Black Horned)"
          ],
          [
            "bP (1/4)",
            "BbPP (Black Polled)",
            "BbPp (Black Polled)",
            "bbPP (Red Polled)",
            "bbPp (Red Polled)"
          ],
          [
            "bp (1/4)",
            "BbPp (Black Polled)",
            "Bbpp (Black Horned)",
            "bbPp (Red Polled)",
            "bbpp (Red Horned)"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In dairy cattle breeding, horned cattle cause traumatic udder injuries, bruising, and handler danger in loose housing. Veterinarians conduct <b>Progeny Test Matings of candidate AI bulls with horned cows (pp)</b>. If a single horned calf is born, the bull is immediately identified as a heterozygous carrier (Pp) and disqualified from being marketed as a homozygous polled sire.",
    "tags": [
      "Genetics Lab",
      "Mendelian Cross",
      "Monohybrid",
      "Dihybrid",
      "Punnett Square",
      "Test Cross",
      "Polled Gene",
      "Coat Color"
    ]
  },
  "p2-t02": {
    "summary": "Numerical problem solving on modified Mendelian ratios (incomplete dominance, codominance, lethals), epistasis interactions, and sex-linked crisscross inheritance in poultry and livestock.",
    "desc": "<b>AIM:</b> To identify and solve problems on non-Mendelian modifications, epistasis ratios, and sex-linked inheritance in poultry and livestock.<br><br><b>CLASSICAL MODIFIED RATIOS CHEAT-SHEET:</b><ul><li><b>Incomplete Dominance / Codominance:</b> <code>1 : 2 : 1</code> (Roan coat in Shorthorn; Andalusian blue fowl).</li><li><b>Recessive Lethal Gene:</b> <code>2 : 1</code> (Yellow coat in mice; Creeper fowl; Bulldog calf in Dexter cattle).</li><li><b>Recessive Epistasis:</b> <code>9 : 3 : 4</code> (Coat color in Labrador Retrievers).</li><li><b>Dominant Epistasis:</b> <code>12 : 3 : 1</code> (Coat color in dogs; plumage in poultry).</li><li><b>Duplicate Dominant Epistasis:</b> <code>15 : 1</code> (Feathered shanks).</li><li><b>Duplicate Recessive (Complementary):</b> <code>9 : 7</code> (Comb type interaction).</li><li><b>Dominant & Recessive Interaction (Inhibitory Gene):</b> <code>13 : 3</code> (White plumage in Leghorn vs colored).</li><li><b>Duplicate Genes with Cumulative Effect:</b> <code>9 : 6 : 1</code>.</li></ul><br><b>MODEL EXAM PROBLEM 1 (RECESSIVE EPISTASIS IN LABRADORS):</b><br>In Labrador Retrievers, Black (B) is dominant to Chocolate (b). A second epistatic locus (E) controls pigment deposition: <code>E_</code> permits pigment, whereas homozygous recessive <code>ee</code> prevents pigment deposition, resulting in Yellow coat regardless of B/b.<br>Cross two dihybrid Black Labradors (<code>BbEe &times; BbEe</code>) and determine the phenotypic ratio.<br><br><b>SOLUTION:</b><br>Dihybrid segregation yields:<br><code>9 B_E_ (Black) : 3 bbE_ (Chocolate) : 3 B_ee (Yellow) : 1 bbee (Yellow)</code>.<br>Combining the yellow genotypes: <code>3 B_ee + 1 bbee = 4 Yellow</code>.<br><b>Resulting F2 Ratio:</b> <b>9 Black : 3 Chocolate : 4 Yellow</b> (Recessive Epistasis).<br><br><b>MODEL EXAM PROBLEM 2 (SEX-LINKED CRISSCROSS INHERITANCE IN POULTRY):</b><br>In poultry, the barred plumage pattern (B) is sex-linked dominant over non-barred black plumage (b) on the Z chromosome (Females are ZW, Males are ZZ). A non-barred black rooster (<code>Z^b Z^b</code>) is mated to a barred hen (<code>Z^B W</code>).<br>Predict the phenotypes of male and female offspring.<br><br><b>SOLUTION:</b><br><ul><li>Rooster gametes: 100% <code>Z^b</code>.</li><li>Hen gametes: 50% <code>Z^B</code>, 50% <code>W</code>.</li><li><b>Male Progeny (ZZ):</b> <code>Z^b</code> (from sire) + <code>Z^B</code> (from dam) = <b>Z^B Z^b (100% Barred Males)</b>.</li><li><b>Female Progeny (ZW):</b> <code>Z^b</code> (from sire) + <code>W</code> (from dam) = <b>Z^b W (100% Non-barred Black Females)</b>.</li><li><b>Inference:</b> Perfect <b>Crisscross Inheritance</b>! The male transmits his character to daughters, and the female transmits her sex-linked trait to sons. Day-old chicks can be sexed 100% accurately at hatch (auto-sexing).</li></ul><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Why do recessive lethal alleles produce a 2:1 ratio instead of 3:1?</b><br><b>A:</b> Because the homozygous dominant (or homozygous recessive) genotype dies in utero or before hatching (e.g., Dexter bulldog calves), removing 1/4 of the expected progeny.</li><li><b>Q: Which sex is heterogametic in birds vs mammals?</b><br><b>A:</b> Mammalian females are homogametic (XX) and males heterogametic (XY); avian females are <b>heterogametic (ZW)</b> and avian males are <b>homogametic (ZZ)</b>.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Whenever an exam question presents an F2 ratio that sums to <b>16</b> (e.g. 9:3:4, 12:3:1, 13:3, 15:1, 9:7), immediately identify it as a <b>Two-Gene Epistatic Interaction</b>!</li><li>Whenever a reciprocal cross gives different phenotypic distributions between sexes, immediately identify it as <b>Sex-Linked (Z-linked or X-linked)</b> inheritance.</li></ul>",
    "keyPoints": [
      "Incomplete dominance and codominance produce a 1:2:1 phenotypic ratio in F2.",
      "Recessive lethal alleles alter the monohybrid F2 ratio to 2:1 due to embryonic death.",
      "Recessive epistasis produces a 9:3:4 ratio (e.g., coat color in Labrador Retrievers).",
      "Dominant epistasis produces a 12:3:1 ratio.",
      "Dominant and recessive interaction (inhibitory gene) produces a 13:3 ratio.",
      "Duplicate recessive (complementary) epistasis produces a 9:7 ratio.",
      "Duplicate dominant epistasis produces a 15:1 ratio.",
      "Avian females are heterogametic (ZW); avian males are homogametic (ZZ).",
      "Sex-linked recessive traits show crisscross inheritance: sire to daughter, dam to son.",
      "Sex-linked barring (B) and feathering (K) enable 100% accurate auto-sexing of day-old chicks."
    ],
    "tables": [
      {
        "title": "Master Summary Table of Epistatic Gene Interactions (Summing to 16 in F2)",
        "headers": [
          "Type of Gene Interaction",
          "F2 Phenotypic Ratio",
          "Classical Biological Example",
          "Genetic Mechanism"
        ],
        "rows": [
          [
            "Recessive Epistasis",
            "9 : 3 : 4",
            "Labrador Retriever coat color",
            "Homozygous recessive 'ee' masks B/b locus"
          ],
          [
            "Dominant Epistasis",
            "12 : 3 : 1",
            "Dog coat color (Dominant Black)",
            "Dominant allele at one locus masks both alleles of second"
          ],
          [
            "Inhibitory Gene Interaction",
            "13 : 3",
            "White Leghorn plumage color",
            "Dominant inhibitor 'I' suppresses color gene 'C'"
          ],
          [
            "Complementary (Duplicate Recessive)",
            "9 : 7",
            "Comb types / Flower color",
            "Homozygous recessives at either locus produce same mutant phenotype"
          ],
          [
            "Duplicate Dominant",
            "15 : 1",
            "Feathered shanks in poultry",
            "Dominant allele at either locus produces the trait"
          ],
          [
            "Duplicate Genes with Cumulative Effect",
            "9 : 6 : 1",
            "Pork quality / Grain shape",
            "Two dominants produce extreme, single dominant intermediate"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In canine pedigree practice, mating two <b>Merle-coated Australian Shepherds or Great Danes</b> (heterozygous <code>Mm</code>) produces 25% 'Double Merle' pups (<code>MM</code>). Veterinarians advise breeders against Merle-to-Merle matings because double merles suffer from microphthalmia, complete congenital deafness, and night blindness.",
    "tags": [
      "Genetics Lab",
      "Epistasis",
      "Modified Mendelian Ratio",
      "Labrador Coat Color",
      "Crisscross Inheritance",
      "Sex-Linkage",
      "Auto-Sexing"
    ]
  },
  "p2-t03": {
    "summary": "Estimation of linkage, recombination frequency (RF), construction of genetic chromosome maps, and calculation of Coefficient of Coincidence and Interference.",
    "desc": "<b>AIM:</b> To estimate recombination frequency from two-point and three-point test-cross progeny, construct genetic linkage maps, and calculate Coefficient of Coincidence and Interference.<br><br><b>FORMULAS & EQUATIONS:</b><ul><li><b>Recombination Frequency (RF%):</b><br><code>RF% = (Total Number of Recombinants / Total Progeny) &times; 100</code></li><li><b>Map Distance:</b> <code>1% Recombination Frequency = 1 Map Unit (mu) = 1 centiMorgan (cM)</code>.</li><li><b>Coefficient of Coincidence (C):</b><br><code>C = Observed Frequency of Double Crossovers / Expected Frequency of Double Crossovers</code><br>Where <code>Expected DCO = RF_1 &times; RF_2</code>.</li><li><b>Interference (I):</b><br><code>I = 1 - C</code><br>If <code>I &gt; 0</code>: Positive interference (one crossover inhibits adjacent crossovers); If <code>I = 1</code>: Complete interference (zero DCO observed).</li></ul><br><b>MODEL EXAM PROBLEM (TWO-POINT TEST CROSS):</b><br>In a test-cross of a heterozygous female for two linked genes (A and B in coupling phase) with a double recessive male (<code>aabb</code>), the following 1,000 progeny were obtained:<br><code>Parental Types: AB (420), ab (430)</code><br><code>Recombinant Types: Ab (78), aB (72)</code><br>Calculate the recombination frequency and map distance between genes A and B.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li>Total progeny <code>N = 420 + 430 + 78 + 72 = 1,000</code>.</li><li>Total parental progeny = <code>420 + 430 = 850 (85%)</code>.</li><li>Total recombinant progeny = <code>78 + 72 = 150</code>.</li><li><b>Recombination Frequency (RF):</b><br><code>RF% = (150 / 1000) &times; 100 = 15.0%</code>.</li><li><b>Map Distance:</b> Since 1% RF = 1 cM, the genetic distance between locus A and locus B is <b>15.0 cM (or 15 map units)</b>.</li></ol><br><b>MODEL EXAM PROBLEM 2 (INTERFERENCE & COINCIDENCE):</b><br>If the map distance between gene A and B is 10 cM (RF1 = 0.10) and between B and C is 20 cM (RF2 = 0.20), and in a sample of 2,000 progeny, <b>24 double crossovers</b> were observed, calculate Interference.<br><b>Solution:</b><br><ol><li><code>Expected DCO fraction = 0.10 &times; 0.20 = 0.02 (2%)</code>.</li><li><code>Expected DCO count = 0.02 &times; 2,000 = 40 progeny</code>.</li><li><code>Coefficient of Coincidence (C) = 24 / 40 = 0.60</code>.</li><li><code>Interference (I) = 1 - C = 1 - 0.60 = 0.40 (40%)</code>.</li><li><b>Inference:</b> Positive interference exists; the occurrence of the first crossover reduced expected crossing over in the adjacent region by 40%.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What is the theoretical maximum limit of recombination frequency between two linked genes?</b><br><b>A:</b> <b>50%</b>. At or above 50% recombination, linked genes segregate identically to unlinked genes obeying independent assortment.</li><li><b>Q: What are coupling (cis) and repulsion (trans) linkage phases?</b><br><b>A:</b> In <b>Coupling (cis)</b>, two dominant alleles are on one homolog (<code>AB / ab</code>); in <b>Repulsion (trans)</b>, one dominant and one recessive allele are on each homolog (<code>Ab / aB</code>).</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>In three-point test crosses, the <b>two least frequent phenotypic classes</b> are always the <b>Double Crossovers (DCO)</b>, and the <b>two most frequent classes</b> are the <b>Parental types</b>. Comparing DCO with Parentals immediately identifies the <b>middle gene</b>!</li><li>Haldane's mapping function correction: <code>m = - (1/2) ln(1 - 2r)</code> adjusts for unobserved multiple crossovers over large map distances (> 20 cM).</li></ul>",
    "keyPoints": [
      "Recombination Frequency formula: RF% = (Total Recombinants / Total Progeny) * 100.",
      "One map unit (1 mu) or 1 centiMorgan (cM) equals 1% recombination frequency.",
      "Maximum theoretical recombination frequency between two genes is 50%.",
      "Parental combinations always appear with highest frequency in linkage test crosses.",
      "Double crossovers appear with lowest frequency in three-point test crosses.",
      "The gene that differs between parentals and double crossovers is located in the middle.",
      "Coefficient of Coincidence: C = Observed DCO / Expected DCO.",
      "Interference formula: I = 1 - C.",
      "Positive interference (I > 0) means one chiasma inhibits adjacent chiasma formation.",
      "Coupling phase has dominant alleles on same chromosome; repulsion phase on opposites."
    ],
    "tables": [
      {
        "title": "Three-Point Test-Cross Phenotypic Progeny Classes and Linkage Analysis Table",
        "headers": [
          "Progeny Phenotypic Class",
          "Observed Progeny Count",
          "Crossover Classification",
          "Region Involved",
          "Calculation Formula"
        ],
        "rows": [
          [
            "A B C (Parental 1)",
            "385",
            "Non-crossover (NCO)",
            "None",
            "Parental linkage arrangement"
          ],
          [
            "a b c (Parental 2)",
            "395",
            "Non-crossover (NCO)",
            "None",
            "Parental linkage arrangement"
          ],
          [
            "A B c (Single Crossover)",
            "85",
            "Single crossover (SCO-2)",
            "Region II (B - C)",
            "Included in Region II RF"
          ],
          [
            "a b C (Single Crossover)",
            "75",
            "Single crossover (SCO-2)",
            "Region II (B - C)",
            "Included in Region II RF"
          ],
          [
            "A b c (Single Crossover)",
            "25",
            "Single crossover (SCO-1)",
            "Region I (A - B)",
            "Included in Region I RF"
          ],
          [
            "a B C (Single Crossover)",
            "23",
            "Single crossover (SCO-1)",
            "Region I (A - B)",
            "Included in Region I RF"
          ],
          [
            "A b C (Double Crossover)",
            "6",
            "Double crossover (DCO)",
            "Both Regions",
            "Lowest observed frequency"
          ],
          [
            "a B c (Double Crossover)",
            "6",
            "Double crossover (DCO)",
            "Both Regions",
            "Lowest observed frequency"
          ],
          [
            "Total Progeny (N)",
            "1,000",
            "—",
            "—",
            "Map Dist = (SCO + DCO)/N * 100"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In commercial swine breeding, the malignant hyperthermia halothane gene (<i>RYR1</i>) is tightly linked to the <i>GPI</i> (glucosephosphate isomerase) marker locus. Historically, before direct PCR tests were invented, veterinarians utilized linkage analysis of GPI blood protein polymorphisms to track and cull carrier breeding boars prone to fatal Porcine Stress Syndrome (PSS).",
    "tags": [
      "Genetics Lab",
      "Linkage",
      "Recombination Frequency",
      "Map Distance",
      "centiMorgan",
      "Interference",
      "Coincidence",
      "Three-Point Cross"
    ]
  },
  "p2-t04": {
    "summary": "Laboratory protocol for peripheral blood sampling, lymphocyte culture, Colchicine metaphase arrest, hypotonic shock, slide preparation, GTG-banding, and karyotyping in livestock.",
    "desc": "<b>AIM:</b> To demonstrate peripheral blood sampling, set up short-term lymphocyte culture, harvest metaphase chromosomes, prepare Giemsa-stained slides, and construct livestock karyotypes.<br><br><b>STEP-BY-STEP LABORATORY PROTOCOL:</b><ol><li><b>Aseptic Blood Collection:</b><br>&bull; Collect 5 ml venous blood from the external jugular vein under strict sterile conditions into a sterile vacutainer containing <b>Sodium Heparin (15–20 IU/ml)</b>. (Never use EDTA, as it chelates divalent cations and kills lymphocytes!).</li><li><b>Culture Inoculation:</b><br>&bull; In a laminar airflow hood, add <b>0.5 to 0.8 ml of whole blood</b> to a sterile culture vial containing <b>8 ml RPMI-1640</b> (or Ham's F-10) culture medium supplemented with:<br>&nbsp;&nbsp;&bull; 15% Fetal Bovine Serum (FBS) (provides growth factors).<br>&nbsp;&nbsp;&bull; 1% Antibiotic-Antimycotic solution (Penicillin-Streptomycin-Amphotericin B).<br>&nbsp;&nbsp;&bull; <b>0.1 ml Phytohemagglutinin-M (PHA-M):</b> Mitogenic lectin extracted from <i>Phaseolus vulgaris</i>; selectively stimulates mature T-lymphocytes to dedifferentiate and divide.</li><li><b>Incubation:</b> Incubate culture tubes at <b>37.5&deg;C with 5% CO2 for 72 hours</b> in a humidified bacteriological/CO2 incubator. Gently invert tubes twice daily.</li><li><b>Metaphase Arrest (71st hour):</b><br>&bull; Add <b>0.1 ml of Colchicine (or Colcemid, 0.05 &mu;g/ml)</b> 1 to 1.5 hours prior to harvesting.<br>&bull; <i>Mechanism:</i> Binds to tubulin dimers, inhibits mitotic spindle microtubule assembly, and arrests dividing lymphoblasts at <b>Metaphase</b>.</li><li><b>Hypotonic Treatment:</b><br>&bull; Centrifuge culture at 1,000 rpm for 10 minutes; discard supernatant.<br>&bull; Resuspend cell pellet in <b>pre-warmed (37&deg;C) 0.075 M Potassium Chloride (KCl)</b> for <b>15 to 20 minutes</b>.<br>&bull; <i>Principle:</i> Hypotonic solution forces water into cells by osmosis, swelling the fragile cytoplasm and separating crowded chromosomes.</li><li><b>Fixation (Carnoy's Fixative):</b><br>&bull; Add 1 ml of freshly prepared, chilled <b>Carnoy's fixative (3 parts Methanol : 1 part Glacial Acetic Acid)</b>.<br>&bull; Centrifuge, discard supernatant, and repeat washing with fixative 3 to 4 times until the pellet is chalky white.</li><li><b>Slide Casting & Air-Drying:</b><br>&bull; Drop 2–3 drops of cell suspension from a height of 1 to 2 feet onto a pre-cleaned, ice-chilled, wet glass slide held at a 45&deg; angle. Air-dry rapidly over a gentle warm flame or hotplate (45&deg;C).</li><li><b>Staining / GTG Banding:</b><br>&bull; Stain with 4% Giemsa in phosphate buffer (pH 6.8) for 15 minutes, or treat briefly with 0.05% Trypsin followed by Giemsa for <b>G-banding (GTG)</b>.</li></ol><br><b>DIPLOID CHROMOSOME NUMBERS (2n) FOR VIVA:</b><ul><li><b>Cattle (<i>Bos indicus / Bos taurus</i>):</b> <code>2n = 60</code> (All 29 autosome pairs are acrocentric; X is large submetacentric, Y is small metacentric in taurine / small acrocentric in indicine).</li><li><b>River Buffalo (<i>Bubalus bubalis</i>):</b> <code>2n = 50</code> (5 submetacentric autosome pairs + 19 acrocentric autosome pairs + acrocentric X and Y).</li><li><b>Swamp Buffalo:</b> <code>2n = 48</code>.</li><li><b>Sheep (<i>Ovis aries</i>):</b> <code>2n = 54</code> (3 metacentric pairs + 23 acrocentric autosome pairs).</li><li><b>Goat (<i>Capra hircus</i>):</b> <code>2n = 60</code> (All autosomes acrocentric).</li><li><b>Pig (<i>Sus scrofa</i>):</b> <code>2n = 38</code>.</li><li><b>Horse (<i>Equus caballus</i>):</b> <code>2n = 64</code>.</li><li><b>Dog (<i>Canis familiaris</i>):</b> <code>2n = 78</code>.</li><li><b>Chicken (<i>Gallus domesticus</i>):</b> <code>2n = 78</code> (9 macrochromosome pairs + 30 microchromosome pairs).</li></ul>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Why Sodium Heparin and NOT EDTA? EDTA irreversibly chelates Ca&sup2;&plus; and Mg&sup2;&plus;, halting lymphocyte cell division. Stating this secures full marks in viva.</li><li>Diagnosing Robertsonian Translocation: The <code>rob(1;29)</code> centric fusion in cattle reduces chromosome count from 60 to <b>59 (heterozygote)</b> or <b>58 (homozygote)</b>, producing a massive dicentric submetacentric chromosome.</li></ul>",
    "keyPoints": [
      "Peripheral blood must be collected in Sodium Heparin vacutainers (never EDTA).",
      "Phytohemagglutinin (PHA) is the T-lymphocyte mitogen initiating mitosis in vitro.",
      "Lymphocyte culture is incubated at 37.5°C in RPMI-1640 medium for 72 hours.",
      "Colchicine inhibits spindle microtubule formation, arresting dividing cells at metaphase.",
      "Hypotonic 0.075 M KCl treatment swells cells by osmosis to spread chromosomes.",
      "Carnoy's fixative consists of 3 parts absolute methanol and 1 part glacial acetic acid.",
      "Cattle chromosome number: 2n = 60 (29 pairs acrocentric autosomes).",
      "River buffalo: 2n = 50 (5 pairs submetacentric, 19 pairs acrocentric).",
      "Swamp buffalo has 2n = 48 chromosomes due to tandem fusion.",
      "GTG banding uses trypsin digestion followed by Giemsa staining to visualize G-bands."
    ],
    "tables": [
      {
        "title": "Comparative Cytogenetic Features and Karyotypic Profiles of Farm Animals",
        "headers": [
          "Species",
          "Scientific Name",
          "Diploid No. (2n)",
          "Autosome Morphology",
          "Sex Chromosomes (X / Y)"
        ],
        "rows": [
          [
            "Cattle (Zebu / Taurine)",
            "Bos indicus / Bos taurus",
            "2n = 60",
            "All 58 autosomes are Acrocentric",
            "X: Large Submetacentric; Y: Small Acrocentric (Zebu) / Metacentric (HF)"
          ],
          [
            "River Buffalo",
            "Bubalus bubalis",
            "2n = 50",
            "Pairs 1–5: Submetacentric; Pairs 6–24: Acrocentric",
            "X: Largest Acrocentric; Y: Small Acrocentric"
          ],
          [
            "Swamp Buffalo",
            "Bubalus bubalis carabanesis",
            "2n = 48",
            "Pairs 1–5: Submetacentric; Pairs 6–23: Acrocentric",
            "X: Large Acrocentric; Y: Small Acrocentric"
          ],
          [
            "Sheep",
            "Ovis aries",
            "2n = 54",
            "Pairs 1–3: Metacentric; Pairs 4–26: Acrocentric",
            "X: Large Acrocentric; Y: Minute Metacentric"
          ],
          [
            "Goat",
            "Capra hircus",
            "2n = 60",
            "All 58 autosomes are Acrocentric",
            "X: Large Acrocentric; Y: Small Acrocentric"
          ],
          [
            "Pig (Swine)",
            "Sus scrofa",
            "2n = 38",
            "Metacentric, Submetacentric & Telocentric",
            "X: Metacentric; Y: Small Metacentric"
          ],
          [
            "Dog",
            "Canis familiaris",
            "2n = 78",
            "All 76 autosomes are Acrocentric",
            "X: Large Submetacentric; Y: Small Metacentric"
          ],
          [
            "Chicken",
            "Gallus domesticus",
            "2n = 78",
            "9 pairs Macrochromosomes + 30 pairs Microchromosomes",
            "ZZ: Metacentric (Male); ZW: Z-Metacentric, W-Microchromosome (Female)"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> Under statutory breeding regulations, all breeding bulls stationed at Artificial Insemination centers across India must be certified cytogenetically free of <b>Robertsonian rob(1;29) translocations</b>. Bulls carrying rob(1;29) appear phenotypically normal and produce normal sperm motility, but cause a <b>10–15% drop in herd conception rates</b> due to monosomy and trisomy embryonic lethality in early blastocysts.",
    "tags": [
      "Genetics Lab",
      "Karyotyping",
      "Lymphocyte Culture",
      "Colchicine",
      "PHA",
      "Hypotonic KCl",
      "Carnoy's Fixative",
      "2n Numbers",
      "rob(1;29)"
    ]
  },
  "p2-t05": {
    "summary": "Step-by-step calculation of gene and genotypic frequencies in livestock populations for codominant systems (gene counting) and dominant systems (square root method).",
    "desc": "<b>AIM:</b> To estimate gene (allelic) and genotypic frequencies from livestock population data using the Gene Counting Method and Square Root Method.<br><br><b>CORE FORMULAS:</b><ul><li><b>Genotypic Frequency:</b><br><code>P = D = N_AA / N</code>; <code>H = N_Aa / N</code>; <code>Q = R = N_aa / N</code><br>Where <code>P + H + Q = 1.0</code>.</li><li><b>1. Gene Counting Method (Codominant Loci):</b><br><code>p = Frequency of allele A = (2 &times; N_AA + N_Aa) / (2N) = P + (1/2)H</code><br><code>q = Frequency of allele a = (2 &times; N_aa + N_Aa) / (2N) = Q + (1/2)H</code><br>Check: <code>p + q = 1.0</code>.</li><li><b>2. Square Root Method (Complete Dominance Systems):</b><br>Under assumption of Hardy-Weinberg equilibrium:<br>Recessive genotype frequency: <code>q&sup2; = N_aa / N</code><br><code>q = &radic;(N_aa / N)</code><br><code>p = 1 - q</code>.</li></ul><br><b>MODEL EXAM PROBLEM 1 (CODOMINANT BLOOD GROUP SYSTEM):</b><br>In a herd of 200 Hariana cattle, hemoglobin typing revealed the following genotypes:<br><code>Hb-AA = 98</code>, <code>Hb-AB = 84</code>, <code>Hb-BB = 18</code>.<br>Calculate the genotypic frequencies and gene frequencies of alleles A and B.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><code>Total cattle N = 98 + 84 + 18 = 200</code>. Total alleles = <code>2 &times; 200 = 400</code>.</li><li><b>Genotypic Frequencies:</b><br><code>Freq(AA) = 98 / 200 = 0.490 (49%)</code><br><code>Freq(AB) = 84 / 200 = 0.420 (42%)</code><br><code>Freq(BB) = 18 / 200 = 0.090 (9%)</code><br>Check: <code>0.490 + 0.420 + 0.090 = 1.000</code>.</li><li><b>Gene Frequencies (Gene Counting Method):</b><br><code>p = Freq(A) = [ (2 &times; 98) + 84 ] / 400 = (196 + 84) / 400 = 280 / 400 = 0.70</code>.<br><code>q = Freq(B) = [ (2 &times; 18) + 84 ] / 400 = (36 + 84) / 400 = 120 / 400 = 0.30</code>.<br>Alternatively: <code>p = P + (1/2)H = 0.49 + (1/2)(0.42) = 0.49 + 0.21 = 0.70</code>.<br>Check: <code>p + q = 0.70 + 0.30 = 1.00</code>.</li></ol><br><b>MODEL EXAM PROBLEM 2 (SQUARE ROOT METHOD FOR DOMINANCE):</b><br>In a flock of 500 sheep, 455 are white (dominant, W_) and 45 are black (recessive, ww). Assuming Hardy-Weinberg equilibrium, calculate the gene frequencies of W and w, and the number of heterozygous carriers.<br><b>Solution:</b><br><ol><li><code>q&sup2; = Freq(ww) = 45 / 500 = 0.09</code>.</li><li><code>q = &radic;0.09 = 0.30</code> (Frequency of recessive allele w).</li><li><code>p = 1 - q = 1 - 0.30 = 0.70</code> (Frequency of dominant allele W).</li><li>Frequency of heterozygotes <code>2pq = 2 &times; (0.70) &times; (0.30) = 0.42 (42%)</code>.</li><li>Expected number of heterozygous carriers = <code>500 &times; 0.42 = 210 sheep</code>.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Why is the Gene Counting Method superior to the Square Root Method?</b><br><b>A:</b> The Gene Counting method directly counts actual biological alleles without requiring the assumption of Hardy-Weinberg equilibrium; the Square Root method strictly depends on the assumption of random mating equilibrium.</li><li><b>Q: Can gene frequency be negative or greater than 1.0?</b><br><b>A:</b> No, gene frequency is a proportion and must strictly lie between <b>0.0 and 1.0</b>.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Multiple Alleles Shortcut (Bernstein's Method for ABO Blood Groups):<br><code>r = &radic;(Freq O)</code>; <code>p = 1 - &radic;(Freq B + Freq O)</code>; <code>q = 1 - &radic;(Freq A + Freq O)</code>.</li><li>Always round gene frequencies to two or three decimal places and demonstrate that <code>p + q = 1.0</code>.</li></ul>",
    "keyPoints": [
      "Genotypic frequency is the proportion of a specific genotype in the population.",
      "Gene (allelic) frequency is the proportion of a specific allele among total alleles.",
      "Gene counting method for codominance: p = P + (1/2)H; q = Q + (1/2)H.",
      "Gene counting directly counts alleles: p = (2*NAA + NAa) / 2N.",
      "Square root method calculates recessive allele frequency as q = √(Naa / N).",
      "The square root method strictly assumes the population is in Hardy-Weinberg equilibrium.",
      "The sum of all allelic frequencies at a locus must equal 1.0: p + q = 1.0.",
      "Heterozygote frequency under HWE is 2pq.",
      "Most deleterious recessive alleles are hidden in heterozygous carriers (2pq >> q²).",
      "Bernstein's method estimates allele frequencies for tri-allelic blood group systems."
    ],
    "tables": [
      {
        "title": "Computation of Gene and Genotypic Frequencies for Hemoglobin Types in Hariana Cattle (N = 200)",
        "headers": [
          "Genotype",
          "Observed Count",
          "Genotypic Frequency",
          "No. of 'A' Alleles Contributed",
          "No. of 'B' Alleles Contributed"
        ],
        "rows": [
          [
            "Hb-AA (Homozygous A)",
            "98",
            "0.490",
            "98 &times; 2 = 196",
            "0"
          ],
          [
            "Hb-AB (Heterozygous)",
            "84",
            "0.420",
            "84 &times; 1 = 84",
            "84 &times; 1 = 84"
          ],
          [
            "Hb-BB (Homozygous B)",
            "18",
            "0.090",
            "0",
            "18 &times; 2 = 36"
          ],
          [
            "Total",
            "N = 200",
            "1.000",
            "Total A = 280",
            "Total B = 120"
          ],
          [
            "Gene Frequencies",
            "—",
            "—",
            "p = 280 / 400 = 0.70",
            "q = 120 / 400 = 0.30"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In indigenous dairy cattle conservation programs, veterinarians type milk beta-casein alleles (A1 vs A2). Calculating gene frequencies across 500 Gir cattle reveals <code>p(A2) = 0.98</code> and <code>q(A1) = 0.02</code>, enabling state breeding federations to certify Gir cattle herds as <b>100% pure A2 milk producers</b>, commanding premium market prices.",
    "tags": [
      "Population Genetics Lab",
      "Gene Frequency",
      "Genotypic Frequency",
      "Gene Counting",
      "Square Root Method",
      "Hardy-Weinberg",
      "Hariana Cattle",
      "Hemoglobin"
    ]
  },
  "p2-t06": {
    "summary": "Testing animal populations for Hardy-Weinberg Equilibrium using Chi-Square Goodness of Fit test with degrees of freedom df = k - 1 - m.",
    "desc": "<b>AIM:</b> To test whether an observed livestock population conforms to the Hardy-Weinberg Law of Equilibrium using the Chi-Square Goodness of Fit test.<br><br><b>MATHEMATICAL PROCEDURE & EQUATIONS:</b><ol><li><b>Step 1:</b> Calculate sample gene frequencies <code>p</code> and <code>q</code> via Gene Counting.</li><li><b>Step 2:</b> Calculate theoretical expected genotype frequencies under HWE:<br><code>Expected Freq(AA) = p&sup2;</code><br><code>Expected Freq(Aa) = 2pq</code><br><code>Expected Freq(aa) = q&sup2;</code></li><li><b>Step 3:</b> Calculate expected numbers of animals:<br><code>E_AA = N &times; p&sup2;</code>; <code>E_Aa = N &times; 2pq</code>; <code>E_aa = N &times; q&sup2;</code>.</li><li><b>Step 4:</b> Compute Chi-Square statistic:<br><code>&chi;&sup2; = &Sigma; [ (O - E)&sup2; / E ]</code></li><li><b>Step 5: Degrees of Freedom (df):</b><br><code>df = k - 1 - m</code><br>Where <code>k = 3</code> (genotypic classes); <code>m = 1</code> (independent gene frequency <code>p</code> estimated from sample).<br>Therefore, <code>df = 3 - 1 - 1 = 1</code>! (Always 1 df for a two-allele locus!).</li><li><b>Decision Rule:</b> Critical &chi;&sup2; at <code>df = 1, &alpha; = 0.05</code> is <b>3.841</b>. If &chi;&sup2;_cal &le; 3.841 &rarr; Accept H0 (Population is in HWE).</li></ol><br><b>MODEL EXAM PROBLEM:</b><br>In a flock of 400 Garole sheep, Transferrin (Tf) blood protein typing revealed:<br><code>Tf-AA = 210</code>, <code>Tf-AB = 140</code>, <code>Tf-BB = 50</code>.<br>Test whether this flock is in Hardy-Weinberg equilibrium (&chi;&sup2;_tab at df=1 for 5% = 3.841).<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><code>N = 400</code>.</li><li><code>p = Freq(A) = [ (2 &times; 210) + 140 ] / 800 = (420 + 140) / 800 = 560 / 800 = 0.70</code>.</li><li><code>q = Freq(B) = 1 - 0.70 = 0.30</code>.</li><li><b>Expected Genotypic Numbers:</b><br><code>E_AA = N &times; p&sup2; = 400 &times; (0.70)&sup2; = 400 &times; 0.49 = 196</code>.<br><code>E_AB = N &times; 2pq = 400 &times; 2(0.70)(0.30) = 400 &times; 0.42 = 168</code>.<br><code>E_BB = N &times; q&sup2; = 400 &times; (0.30)&sup2; = 400 &times; 0.09 = 36</code>.<br>Check: <code>&Sigma; E = 196 + 168 + 36 = 400 = N</code>.</li><li><b>Compute Chi-Square:</b><br>Class AA: <code>(210 - 196)&sup2; / 196 = (14)&sup2; / 196 = 196 / 196 = 1.000</code><br>Class AB: <code>(140 - 168)&sup2; / 168 = (-28)&sup2; / 168 = 784 / 168 = 4.667</code><br>Class BB: <code>(50 - 36)&sup2; / 36 = (14)&sup2; / 36 = 196 / 36 = 5.444</code><br><code>&chi;&sup2;_cal = 1.000 + 4.667 + 5.444 = 11.111</code>.</li><li><b>Inference:</b> <code>&chi;&sup2;_cal = 11.111 &gt; &chi;&sup2;_tab(1, 0.05) = 3.841</code>. Null hypothesis H0 is <b>rejected (P &lt; 0.01)</b>.<br><i>Conclusion:</i> The Garole sheep flock is <b>NOT in Hardy-Weinberg equilibrium</b>. (Notice the marked deficit of heterozygotes: 140 observed vs 168 expected, indicating significant inbreeding or positive assortative mating!).</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Why is df = 1 and NOT 2 when testing HWE for a 3-genotype system?</b><br><b>A:</b> Although there are 3 classes (k = 3), we use 1 degree of freedom to fix the sample size N, and a second degree of freedom is lost because the gene frequency <code>p</code> was estimated directly from the sample data: <code>df = 3 - 1 - 1 = 1</code>.</li><li><b>Q: What factors cause an animal population to deviate from Hardy-Weinberg equilibrium?</b><br><b>A:</b> Small population size (genetic drift), non-random mating (inbreeding/assortative mating), artificial selection, migration (introduction of breeding sires), and mutation.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Heterozygote Deficit Indicator (Wright's Fixation Index F_IS):<br><code>F_IS = 1 - (Observed Heterozygotes / Expected Heterozygotes) = 1 - (140 / 168) = 1 - 0.833 = +0.167</code>.<br>A positive F_IS confirms inbreeding within the subpopulation. Citing F_IS in your answer proves top-tier biometrical mastery!</li></ul>",
    "keyPoints": [
      "Hardy-Weinberg equilibrium states gene and genotypic frequencies remain constant under panmixia.",
      "Expected genotype frequencies under HWE are: p², 2pq, and q².",
      "Degrees of freedom for testing HWE at a bi-allelic locus is strictly df = 1 (df = k - 1 - m).",
      "Expected numbers: E(AA) = N*p², E(Aa) = N*2pq, E(aa) = N*q².",
      "Chi-square test statistic: χ² = Σ [(O - E)² / E].",
      "Critical χ² value at df = 1 for 5% significance level is 3.841.",
      "If χ²_cal > 3.841, the population deviates significantly from Hardy-Weinberg equilibrium.",
      "Deficit of observed heterozygotes compared to expected indicates inbreeding or positive assortative mating.",
      "Excess of observed heterozygotes indicates overdominance selection or outbreeding.",
      "Wright's Fixation Index F_IS = 1 - (H_obs / H_exp) quantifies inbreeding deviation."
    ],
    "tables": [
      {
        "title": "Testing Hardy-Weinberg Equilibrium in Garole Sheep Transferrin Locus (N = 400)",
        "headers": [
          "Genotype",
          "Observed (O)",
          "HWE Expected Frequency",
          "Expected Number (E)",
          "(O - E)",
          "Cell &chi;&sup2; = (O - E)&sup2;/E"
        ],
        "rows": [
          [
            "Tf-AA",
            "210",
            "p&sup2; = 0.49",
            "196.0",
            "+14.0",
            "196 / 196.0 = 1.000"
          ],
          [
            "Tf-AB",
            "140",
            "2pq = 0.42",
            "168.0",
            "-28.0",
            "784 / 168.0 = 4.667"
          ],
          [
            "Tf-BB",
            "50",
            "q&sup2; = 0.09",
            "36.0",
            "+14.0",
            "196 / 36.0 = 5.444"
          ],
          [
            "Total",
            "N = 400",
            "1.00",
            "&Sigma;E = 400.0",
            "0.0",
            "&chi;&sup2;_cal = 11.111** (df=1)"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In closed nucleus breeding herds of Sahiwal cattle, veterinarians periodically perform Chi-Square HWE tests on molecular markers. A statistically significant deviation with an acute deficit of heterozygotes alerts the farm geneticist that <b>inbreeding has reached dangerous levels</b>, mandating immediate introduction of unrelated pedigreed breeding bulls from other state farms.",
    "tags": [
      "Population Genetics Lab",
      "Hardy-Weinberg",
      "Chi-Square Test",
      "Goodness of Fit",
      "Degrees of Freedom",
      "Garole Sheep",
      "Transferrin",
      "Fixation Index"
    ]
  },
  "p2-t07": {
    "summary": "Mathematical calculation of directional changes in gene frequency (Δq) driven by Mutation, Migration, Artificial Selection, and Random Genetic Drift.",
    "desc": "<b>AIM:</b> To calculate changes in gene frequency (&Delta;q) under the deterministic forces of mutation, migration, and selection, and predict variance under genetic drift.<br><br><b>GOVERNING EQUATIONS FOR EVOLUTIONARY FORCES:</b><ul><li><b>1. Recurrent Mutation:</b><br>Forward mutation (A &rarr; a) at rate <code>u</code>; Reverse mutation (a &rarr; A) at rate <code>v</code>.<br><code>&Delta;q = u(1 - q) - vq = u &times; p - v &times; q</code>.<br>Equilibrium gene frequency: <code>\\hat{q} = u / (u + v)</code>.</li><li><b>2. Migration (Gene Flow):</b><br>Immigrants enter population with frequency <code>q_m</code> at migration rate <code>m</code>.<br>New gene frequency: <code>q_1 = m &times; q_m + (1 - m) &times; q_0</code>.<br>Change in gene frequency: <code>&Delta;q = m &times; (q_m - q_0)</code>.</li><li><b>3. Artificial Selection Against Recessive Homozygote (aa):</b><br>Selection coefficient = <code>s</code> (Fitness of aa = <code>1 - s</code>).<br><code>&Delta;q = -s &times; p &times; q&sup2; / (1 - s &times; q&sup2;)</code>.<br>For <b>Complete Selection (s = 1)</b> (Culling all recessives):<br><code>q_t = q_0 / (1 + t &times; q_0)</code> (where t = generations of selection).<br>Number of generations to reduce frequency from q_0 to q_t: <code>t = (1 / q_t) - (1 / q_0)</code>.</li><li><b>4. Random Genetic Drift:</b><br>Variance in gene frequency per generation: <code>&sigma;&sup2;_{&Delta;q} = p &times; q / (2 N_e)</code>.</li></ul><br><b>MODEL EXAM PROBLEM 1 (SELECTION AGAINST LETHAL RECESSIVE):</b><br>In a dairy herd, the frequency of a lethal recessive allele (e.g. BLAD, 'a') is <code>q_0 = 0.20</code>. If complete selection is practiced by culling all homozygous recessive calves (s = 1):<br>1. What will be the gene frequency after 4 generations?<br>2. How many generations are required to reduce the frequency from 0.20 to 0.05?<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><b>Gene frequency after t = 4 generations:</b><br><code>q_4 = q_0 / (1 + t &times; q_0) = 0.20 / [ 1 + (4 &times; 0.20) ] = 0.20 / (1 + 0.80) = 0.20 / 1.80 = 0.1111</code>.<br><b>Answer 1:</b> Gene frequency after 4 generations = <b>0.111 (11.1%)</b>.</li><li><b>Generations to reduce from q_0 = 0.20 to q_t = 0.05:</b><br><code>t = (1 / q_t) - (1 / q_0) = (1 / 0.05) - (1 / 0.20) = 20 - 5 = 15 generations</code>.<br><b>Answer 2:</b> It takes <b>15 generations</b> of complete culling to reduce gene frequency to 0.05.</li></ol><br><b>MODEL EXAM PROBLEM 2 (MIGRATION):</b><br>A native cattle population with black coat allele frequency <code>q_0 = 0.80</code> receives 20% breeding bulls (<code>m = 0.20</code>) from a population where <code>q_m = 0.30</code>. Calculate the new gene frequency and &Delta;q.<br><b>Solution:</b><br><code>&Delta;q = m(q_m - q_0) = 0.20 &times; (0.30 - 0.80) = 0.20 &times; (-0.50) = -0.10</code>.<br><code>q_1 = q_0 + &Delta;q = 0.80 - 0.10 = 0.70</code>.",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Why does selection become inefficient at low gene frequency? Explain that when <code>q</code> is small (e.g. 0.01), <code>q&sup2; = 0.0001</code> (only 1 in 10,000 animals expresses the defect), while <code>2pq &approx; 0.02</code> (99% of mutant alleles are hidden harmlessly in heterozygous carriers!). Culling recessives alone can never eliminate the allele completely.</li></ul>",
    "keyPoints": [
      "Four evolutionary forces change gene frequencies: Mutation, Migration, Selection, Genetic Drift.",
      "Equilibrium gene frequency under mutation: q̂ = u / (u + v).",
      "Change in gene frequency due to migration: Δq = m * (qm - q0).",
      "Change in gene frequency under complete recessive selection: Δq = -q² / (1 + q).",
      "Formula for gene frequency after t generations of complete selection: qt = q0 / (1 + t * q0).",
      "Number of generations required to reduce recessive frequency: t = (1 / qt) - (1 / q0).",
      "Selection against recessives becomes progressively slower as q decreases.",
      "At low gene frequencies, almost all recessive alleles are sheltered in heterozygotes (2pq).",
      "Variance of gene frequency under random drift: σ² = pq / (2Ne).",
      "Genetic drift causes random fixation or loss of alleles, accelerating in small populations."
    ],
    "tables": [
      {
        "title": "Decline in Recessive Gene Frequency (q) Under Complete Selection (s = 1.0) Over Generations",
        "headers": [
          "Generation (t)",
          "Recessive Gene Freq (q)",
          "Dominant Gene Freq (p)",
          "Homozygous Defective (q²)",
          "Heterozygous Carrier (2pq)",
          "Fraction of Alleles in Carriers"
        ],
        "rows": [
          [
            "0 (Start)",
            "0.5000",
            "0.5000",
            "0.2500 (25.0%)",
            "0.5000 (50.0%)",
            "50.0%"
          ],
          [
            "1",
            "0.3333",
            "0.6667",
            "0.1111 (11.1%)",
            "0.4444 (44.4%)",
            "66.7%"
          ],
          [
            "2",
            "0.2500",
            "0.7500",
            "0.0625 (6.25%)",
            "0.3750 (37.5%)",
            "75.0%"
          ],
          [
            "4",
            "0.1667",
            "0.8333",
            "0.0278 (2.78%)",
            "0.2778 (27.8%)",
            "83.3%"
          ],
          [
            "10",
            "0.0833",
            "0.9167",
            "0.0069 (0.69%)",
            "0.1528 (15.3%)",
            "91.7%"
          ],
          [
            "50",
            "0.0192",
            "0.9808",
            "0.0004 (0.04%)",
            "0.0377 (3.77%)",
            "98.0%"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> Veterinarians advising breed associations battling genetic defects like <b>CVM (Complex Vertebral Malformation)</b> in dairy cattle explain to breeders why merely culling deformed calves fails to eradicate the disease. To achieve rapid genetic elimination, modern breeding programs mandate <b>DNA marker genotyping of breeding bulls</b>, culling all heterozygous carriers (<code>Pp</code>) directly, which slashes allele frequency to near zero in a single generation.",
    "tags": [
      "Population Genetics Lab",
      "Forces Changing Gene Frequency",
      "Selection",
      "Mutation",
      "Migration",
      "Genetic Drift",
      "BLAD",
      "CVM"
    ]
  },
  "p2-t08": {
    "summary": "Estimation of Heritability (h²) via Paternal Half-Sib analysis, Repeatability (r) via intraclass correlation, Breeding Value (EBV), and Genetic Correlation.",
    "desc": "<b>AIM:</b> To estimate Heritability (h&sup2;) from Paternal Half-Sib Analysis of Variance, Repeatability (r) across multiple lactations, and predict Estimated Breeding Value (EBV).<br><br><b>CORE QUANTITATIVE GENETICS FORMULAS:</b><ul><li><b>1. Paternal Half-Sib Heritability (One-Way ANOVA):</b><br>Sires (<code>s</code>) mated to multiple dams, each producing <code>k</code> daughters.<br>Sire Mean Square (<code>MS_s</code>) and Within-Sire Mean Square (<code>MS_w</code>).<br>Sire Variance Component: <code>&sigma;&sup2;_s = (MS_s - MS_w) / k</code>.<br>Within-Sire Error Variance: <code>&sigma;&sup2;_w = MS_w</code>.<br>Intraclass Correlation: <code>t = &sigma;&sup2;_s / (&sigma;&sup2;_s + &sigma;&sup2;_w)</code>.<br><b>Heritability:</b> <code>h&sup2; = 4 &times; t = 4 &times; &sigma;&sup2;_s / (&sigma;&sup2;_s + &sigma;&sup2;_w)</code>.</li><li><b>2. Offspring-Parent Regression Heritability:</b><br>Offspring on Single Parent: <code>h&sup2; = 2 &times; b_{OP}</code>.<br>Offspring on Mid-Parent Average: <code>h&sup2; = b_{O\\bar{P}}</code>.</li><li><b>3. Repeatability (r):</b><br>Between-Animal Variance (<code>&sigma;&sup2;_a</code>) and Within-Animal Variance (<code>&sigma;&sup2;_e</code>):<br><code>r = &sigma;&sup2;_a / (&sigma;&sup2;_a + &sigma;&sup2;_e)</code>.</li><li><b>4. Estimated Breeding Value (EBV):</b><br>Based on Individual Phenotype: <code>EBV = h&sup2; &times; (P - \\bar{P})</code>.<br>Based on Progeny Average (n daughters): <code>EBV = [ (2n &times; h&sup2;) / (4 + (n - 1)h&sup2;) ] &times; (\\bar{D} - \\bar{P})</code>.</li></ul><br><b>MODEL EXAM PROBLEM (PATERNAL HALF-SIB HERITABILITY):</b><br>An analysis of 305-day milk yield was conducted on 40 daughters belonging to 5 sires (8 daughters per sire, k = 8). The ANOVA yielded: <code>Between-Sire SS = 1,400,000</code> and <code>Within-Sire SS = 2,800,000</code>. Calculate the heritability of milk yield.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><code>Sires s = 5</code> &rarr; <code>df_s = 5 - 1 = 4</code>.</li><li><code>Total daughters N = 40</code> &rarr; <code>df_w = 40 - 5 = 35</code>.</li><li><code>MS_s = 1,400,000 / 4 = 350,000</code>.</li><li><code>MS_w = 2,800,000 / 35 = 80,000</code>.</li><li><code>&sigma;&sup2;_w = MS_w = 80,000</code>.</li><li><code>&sigma;&sup2;_s = (MS_s - MS_w) / k = (350,000 - 80,000) / 8 = 270,000 / 8 = 33,750</code>.</li><li>Total Phenotypic Variance: <code>&sigma;&sup2;_P = &sigma;&sup2;_s + &sigma;&sup2;_w = 33,750 + 80,000 = 113,750</code>.</li><li>Intraclass Correlation: <code>t = 33,750 / 113,750 = 0.2967</code>.</li><li><b>Heritability:</b> <code>h&sup2; = 4 &times; t = 4 &times; 0.2967 = 1.1868 &rarr; 0.2967 &times; 4</code>.<br>(Note: When sampling variance produces h&sup2; &gt; 1.0, report calculated value and explain sampling error; here if MS_s was 240,000, <code>&sigma;&sup2;_s = 20,000</code>, <code>t = 0.20</code>, <code>h&sup2; = 0.80</code>).</li></ol><br><b>MODEL EXAM PROBLEM 2 (BREEDING VALUE):</b><br>A Sahiwal cow produces 3,200 kg milk in a herd averaging 2,500 kg. If heritability of milk yield is <code>h&sup2; = 0.30</code>, calculate her Estimated Breeding Value (EBV).<br><b>Solution:</b><br><code>EBV = h&sup2; &times; (P - \\bar{P}) = 0.30 &times; (3200 - 2500) = 0.30 &times; 700 = +210 kg</code>.<br>Expected Transmitting Ability (ETA) = <code>(1/2) &times; EBV = +105 kg</code>.",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Why do we multiply by 4 in paternal half-sibs? Because paternal half-sibs share <b>1/4 of their additive genetic variance</b>: <code>Cov(PHS) = (1/4)&sigma;&sup2;_A = &sigma;&sup2;_s</code>. Therefore, <code>&sigma;&sup2;_A = 4 &times; &sigma;&sup2;_s</code>!</li><li>Why is maternal half-sib analysis biased? Because maternal half-sibs share common maternal environmental effects (c&sup2;), inflating heritability estimates: <code>Cov(MHS) = (1/4)&sigma;&sup2;_A + &sigma;&sup2;_Ec</code>.</li></ul>",
    "keyPoints": [
      "Paternal half-sibs share 1/4 of additive genetic variance: Cov(PHS) = (1/4)σ²A.",
      "Heritability from paternal half-sibs: h² = 4 * σ²s / (σ²s + σ²w).",
      "Sire variance component formula: σ²s = (MS_s - MS_w) / k.",
      "Heritability from single-parent regression: h² = 2 * b_OP.",
      "Heritability from mid-parent regression: h² = b_ŌP.",
      "Repeatability is the upper limit of heritability: r = (σ²A + σ²Eg) / σ²P.",
      "Intraclass correlation for repeatability: r = σ²a / (σ²a + σ²e).",
      "Individual Estimated Breeding Value: EBV = h² * (P - P̄).",
      "Predicted Transmitting Ability (PTA) is half of breeding value: PTA = (1/2) * EBV.",
      "Paternal half-sib design is free from maternal environmental bias (c²)."
    ],
    "tables": [
      {
        "title": "Paternal Half-Sib Analysis of Variance (ANOVA) Design Table for Heritability",
        "headers": [
          "Source of Variation",
          "Degrees of Freedom (df)",
          "Mean Square (MS)",
          "Expected Mean Square E(MS)",
          "Variance Component Isolated"
        ],
        "rows": [
          [
            "Between Sires",
            "s - 1",
            "MS_s",
            "&sigma;&sup2;_w + k &times; &sigma;&sup2;_s",
            "&sigma;&sup2;_s = (MS_s - MS_w) / k = (1/4)&sigma;&sup2;_A"
          ],
          [
            "Within Sires (Daughters)",
            "s(k - 1) = N - s",
            "MS_w",
            "&sigma;&sup2;_w",
            "&sigma;&sup2;_w = (3/4)&sigma;&sup2;_A + &sigma;&sup2;_D + &sigma;&sup2;_E"
          ],
          [
            "Total",
            "N - 1",
            "—",
            "—",
            "&sigma;&sup2;_P = &sigma;&sup2;_s + &sigma;&sup2;_w"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In commercial dairy breeding, sires are ranked using <b>Genomic Estimated Breeding Value (GEBV)</b>. Veterinarians advise farmers on sire catalogs by interpreting PTA values. A bull with <code>PTA Milk = +400 kg</code> mated to an average cow is expected to produce daughters that yield <b>400 kg more milk per lactation</b> than the national herd average under identical management.",
    "tags": [
      "Quantitative Genetics Lab",
      "Heritability",
      "Repeatability",
      "Breeding Value",
      "EBV",
      "Paternal Half-Sib",
      "ANOVA",
      "PTA"
    ]
  }
};

practicalData["prac-unit-3"] = {
  "p3-t01": {
    "summary": "Step-by-step computation of Selection Differential (S), Selection Intensity (i), and Generation Interval (L) across the four genetic pathways in livestock herds.",
    "desc": "<b>AIM:</b> To compute Selection Differential (S), Selection Intensity (i), and Generation Interval (L) in dairy cattle and sheep breeding herds.<br><br><b>CORE QUANTITATIVE EQUATIONS:</b><ul><li><b>1. Selection Differential (S):</b><br><code>S = \\bar{X}_s - \\bar{X}_p</code><br>Where <code>\\bar{X}_s</code> = Mean phenotypic performance of selected parents; <code>\\bar{X}_p</code> = Mean performance of the base parental population.<br>&bull; <i>Effective / Weighted Selection Differential:</i> <code>S_w = [ &Sigma; w_i &times; (X_i - \\bar{X}_p) ] / &Sigma; w_i</code> (weighted by number of offspring left by each parent).</li><li><b>2. Selection Intensity (i):</b><br><code>i = S / &sigma;_P</code><br>Standardized selection differential; read directly from truncation selection tables for proportion <code>p</code> saved.</li><li><b>3. Average Selection Differential of Parents:</b><br><code>\\bar{S} = (S_m + S_f) / 2</code> (where S_m = sire differential, S_f = dam differential).</li><li><b>4. Generation Interval (L):</b><br>Average age of parents when their offspring destined to become breeding replacements are born.<br><code>L = (L_{ss} + L_{sd} + L_{ds} + L_{dd}) / 4</code><br>Where <code>ss</code> = sire to son, <code>sd</code> = sire to daughter, <code>ds</code> = dam to son, <code>dd</code> = dam to daughter pathways.</li></ul><br><b>MODEL EXAM PROBLEM:</b><br>In a herd of 200 Sahiwal cows, the average 305-day lactation milk yield is <b>2,400 kg with &sigma;_P = 400 kg</b>. Top 20 cows are selected as elite bull-mothers, averaging <b>3,200 kg</b> milk. The selected AI breeding bulls used have a transmitting superiority equivalent to dams yielding <b>3,600 kg</b> (sire differential S_m = 1,200 kg).<br>1. Calculate the selection differential of dams (S_f) and overall selection differential (\\bar{S}).<br>2. Calculate selection intensity in dams (i_f).<br>3. If average parental ages along the four pathways are: L_ss = 6 yrs, L_sd = 5.5 yrs, L_ds = 6.5 yrs, L_dd = 5 yrs, calculate average generation interval L.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><b>Dam Selection Differential:</b><br><code>S_f = \\bar{X}_s - \\bar{X}_p = 3,200 - 2,400 = +800 kg</code>.</li><li><b>Sire Selection Differential:</b> <code>S_m = +1,200 kg</code>.</li><li><b>Overall Average Selection Differential:</b><br><code>\\bar{S} = (S_m + S_f) / 2 = (1,200 + 800) / 2 = 2,000 / 2 = 1,000 kg</code>.</li><li><b>Selection Intensity in Dams (i_f):</b><br><code>i_f = S_f / &sigma;_P = 800 / 400 = 2.00 standard deviations</code>.<br>(Corresponds to selecting top 10% of females).</li><li><b>Average Generation Interval (L):</b><br><code>L = (6.0 + 5.5 + 6.5 + 5.0) / 4 = 23.0 / 4 = 5.75 years</code>.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Why is selection intensity much higher in males than in females?</b><br><b>A:</b> Due to biological reproductive rates: a herd needs replacement females (selecting 60–80% of heifers, i &approx; 0.3–0.6), but through AI, only top 1% to 2% of bulls are selected (i &approx; 2.4–2.6).</li><li><b>Q: What are typical generation intervals across domestic farm species?</b><br><b>A:</b> Dairy Cattle & Buffaloes: <b>5 to 6 years</b>; Sheep & Goats: <b>2.5 to 3 years</b>; Swine: <b>1.5 to 2 years</b>; Poultry: <b>1 year</b>.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Difference between Potential vs Realized (Effective) Selection Differential: Potential S is calculated on selected parents; Realized S_w weights parents by the actual number of offspring surviving to breeding age. Natural selection and involuntary culling often make <code>S_w &lt; S</code>.</li><li>Genomic Selection impact: Genomic evaluation slashes the sire generation interval (L_ss and L_sd) from 6.0 years down to <b>1.5 to 2.0 years</b>, roughly halving total generation interval L.</li></ul>",
    "keyPoints": [
      "Selection Differential S = X̄s - X̄p (mean of selected parents minus herd mean).",
      "Weighted selection differential Sw accounts for unequal progeny numbers per parent.",
      "Selection Intensity is the standardized differential: i = S / σP.",
      "Average parental selection differential: S̄ = (Sm + Sf) / 2.",
      "Generation Interval L is the average age of parents when replacement offspring are born.",
      "Four genetic pathways determine L: Sire-to-Son, Sire-to-Daughter, Dam-to-Son, Dam-to-Daughter.",
      "Average generation interval formula: L = (Lss + Lsd + Lds + Ldd) / 4.",
      "Selection intensity is much higher in males (top 1-2%) than females (top 60-80%).",
      "Generation interval is ~5.5-6 years in dairy cattle, ~2.5 years in sheep, ~1 year in poultry.",
      "Reducing generation interval directly accelerates annual genetic progress: ΔG/yr = ΔG / L."
    ],
    "tables": [
      {
        "title": "Standard Selection Intensity (i) Values for Different Proportions of Selected Animals (p)",
        "headers": [
          "Proportion Selected (p)",
          "Selection Intensity (i in &sigma; units)",
          "Livestock Breeding Category",
          "Practical Farm Example"
        ],
        "rows": [
          [
            "0.01 (1%)",
            "2.665",
            "Elite AI Sires / Bull Fathers",
            "Top 1 bull selected out of 100 tested"
          ],
          [
            "0.05 (5%)",
            "2.063",
            "Elite Bull Mothers",
            "Top 5 donor cows in nucleus MOET herd"
          ],
          [
            "0.10 (10%)",
            "1.755",
            "Registered Seedstock Sires",
            "Ram selection in commercial sheep flock"
          ],
          [
            "0.20 (20%)",
            "1.399",
            "Boar replacements in swine",
            "Top 20% boars retained for breeding"
          ],
          [
            "0.50 (50%)",
            "0.798",
            "Commercial heifer replacements",
            "Retaining 50% replacement dairy heifers"
          ],
          [
            "0.80 (80%)",
            "0.350",
            "Low-intensity female culling",
            "Routine culling of bottom 20% scrub cows"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> Veterinarians auditing commercial dairy breeding herds often discover that annual genetic progress is stagnant because dairy farmers retain cows until 12–14 years of age, inflating the dam generation interval (<code>L_dd &gt; 8 years</code>). Veterinarians recommend strict <b>replacement of older, genetically lagging cows with superior first-calvers</b> at 4th or 5th parity, compressing herd generation interval down to 4.5 years and boosting annual genetic progress by 25%.",
    "tags": [
      "Animal Breeding Lab",
      "Selection Differential",
      "Selection Intensity",
      "Generation Interval",
      "Breeder's Equation",
      "Sahiwal Cattle"
    ]
  },
  "p3-t02": {
    "summary": "Estimation of expected genetic gain per generation (ΔG), annual genetic progress (ΔG/yr), and correlated response to indirect selection (CRY).",
    "desc": "<b>AIM:</b> To estimate direct expected genetic response (&Delta;G), annual genetic progress, and correlated response (CR_Y) in livestock improvement programs.<br><br><b>CORE GENETIC RESPONSE EQUATIONS:</b><ul><li><b>1. Expected Genetic Gain Per Generation (&Delta;G):</b><br><code>&Delta;G = h&sup2; &times; S = h&sup2; &times; (\\bar{X}_s - \\bar{X}_p)</code><br>Alternatively: <code>&Delta;G = i &times; r_{TI} &times; &sigma;_A = i &times; h &times; &sigma;_A</code> (where r_{TI} = accuracy of selection).</li><li><b>2. Annual Genetic Gain (&Delta;G_{yr}):</b><br><code>&Delta;G_{yr} = &Delta;G / L = [ (h&sup2; &times; S_m) + (h&sup2; &times; S_f) ] / (L_m + L_f)</code><br><code>&Delta;G_{yr} = [ (i_m &times; r_{TIm}) + (i_f &times; r_{TIf}) ] &times; &sigma;_A / (L_m + L_f)</code>.</li><li><b>3. Correlated Response in Trait Y from Selection on Trait X (CR_Y):</b><br><code>CR_Y = i_X &times; r_g &times; h_X &times; h_Y &times; &sigma;_{P_Y}</code><br>Where <code>r_g</code> = genetic correlation between X and Y; <code>h_X, h_Y</code> = square roots of heritabilities; <code>&sigma;_{P_Y}</code> = phenotypic standard deviation of Y.</li><li><b>4. Relative Efficiency of Indirect Selection (RE):</b><br><code>RE = CR_Y / R_Y = r_g &times; (h_X / h_Y)</code>.</li></ul><br><b>MODEL EXAM PROBLEM 1 (DIRECT GENETIC GAIN):</b><br>In a herd of Sahiwal cattle, the average lactation milk yield is 2,400 kg. Selected parents have a mean lactation yield of 2,900 kg. Heritability of milk yield is <code>h&sup2; = 0.25</code>. If the average generation interval is <code>L = 5 years</code>:<br>1. Calculate expected genetic gain per generation (&Delta;G).<br>2. Calculate expected annual genetic gain (&Delta;G_{yr}).<br>3. What will be the expected mean milk yield of the offspring generation?<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><code>Selection Differential S = 2,900 - 2,400 = 500 kg</code>.</li><li><code>&Delta;G = h&sup2; &times; S = 0.25 &times; 500 = 125.0 kg per generation</code>.</li><li><code>Annual Genetic Gain (&Delta;G_{yr}) = &Delta;G / L = 125.0 / 5 = 25.0 kg / year</code> (approx. 1% annual gain).</li><li><code>Offspring Generation Mean = Base Mean + &Delta;G = 2,400 + 125 = 2,525 kg</code>.</li></ol><br><b>MODEL EXAM PROBLEM 2 (CORRELATED RESPONSE):</b><br>Selection is practiced for 6-month Body Weight (X) in Malpura sheep to improve adult Fleece Weight (Y). Given: <code>i_X = 1.40</code>, <code>h&sup2;_X = 0.36 (h_X = 0.60)</code>, <code>h&sup2;_Y = 0.25 (h_Y = 0.50)</code>, <code>&sigma;_{P_Y} = 0.40 kg</code>, and <code>r_g = +0.50</code>. Calculate the correlated response in fleece weight (CR_Y).<br><b>Solution:</b><br><code>CR_Y = i_X &times; r_g &times; h_X &times; h_Y &times; &sigma;_{P_Y}</code><br><code>CR_Y = 1.40 &times; (+0.50) &times; 0.60 &times; 0.50 &times; 0.40 kg</code><br><code>CR_Y = 1.40 &times; 0.50 &times; 0.12 = 1.40 &times; 0.060 = +0.084 kg (84 grams per generation)</code>.",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>When is indirect selection more efficient than direct selection? Whenever <code>RE &gt; 1.0</code>, which occurs when <code>r_g &times; h_X &gt; h_Y</code> (i.e. Trait X has higher heritability than Y and genetic correlation is strong).</li><li>Always distinguish between <code>&Delta;G</code> (per generation) and <code>&Delta;G_{yr}</code> (annual). Mixing these up is the single most common student calculation error.</li></ul>",
    "keyPoints": [
      "Expected genetic gain per generation: ΔG = h² * S.",
      "Expected offspring mean: Ȳ_offspring = Ȳ_base + ΔG.",
      "Annual genetic progress formula: ΔG_yr = ΔG / L.",
      "Four factors in Breeder's Equation: Intensity (i), Accuracy (r_TI), Genetic SD (σA), Interval (L).",
      "Correlated response formula: CRY = iX * rg * hX * hY * σPY.",
      "Relative efficiency of indirect selection: RE = rg * (hX / hY).",
      "Indirect selection is preferred when target trait Y is sex-limited, costly, or expressed late in life.",
      "A positive genetic correlation produces favorable simultaneous progress in both traits.",
      "An unfavorable genetic correlation (e.g., milk yield vs mastitis resistance) causes antagonistic declines.",
      "Annual genetic progress in well-managed dairy herds typically ranges from 1.0% to 1.5% of herd mean."
    ],
    "tables": [
      {
        "title": "Components of the Breeder's Equation and Their Direct Impact on Genetic Gain (&Delta;G)",
        "headers": [
          "Biometrical Parameter",
          "Symbol",
          "Mathematical Role",
          "Breeding Intervention to Maximize Gain",
          "Field Limitation"
        ],
        "rows": [
          [
            "Selection Intensity",
            "i",
            "Numerator (direct multiplier)",
            "Artificial Insemination, sexed semen (keep top 1% sires)",
            "Inbreeding accumulation in closed nucleus"
          ],
          [
            "Accuracy of Selection",
            "r_TI",
            "Numerator (direct multiplier)",
            "Progeny testing, Genomic Selection (GBLUP)",
            "Cost of progeny recording, pedigree errors"
          ],
          [
            "Additive Genetic SD",
            "&sigma;_A",
            "Numerator (raw genetic fuel)",
            "Outcrossing, broad base foundation population",
            "Biological ceiling within pure breeds"
          ],
          [
            "Generation Interval",
            "L",
            "Denominator (inversely related)",
            "Genomic selection of calves, juvenile MOET",
            "Age at sexual maturity, long gestation in cattle"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In commercial pig breeding, direct measurement of backfat thickness on live breeding boars is invasive and difficult without ultrasound. Breeding companies select boars indirectly for <b>Post-Weaning Average Daily Gain (ADG)</b>. Because ADG has high heritability (h&sup2; = 0.40) and strong favorable genetic correlation with feed conversion efficiency (r_g = -0.65), fast-growing boars automatically produce market progeny that convert feed to lean pork with minimal expensive concentrate consumption.",
    "tags": [
      "Animal Breeding Lab",
      "Genetic Gain",
      "Breeder's Equation",
      "Correlated Response",
      "Relative Efficiency",
      "Indirect Selection",
      "Malpura Sheep"
    ]
  },
  "p3-t03": {
    "summary": "Estimation of Estimated Producing Ability (EPA) and Most Probable Producing Ability (MPPA) for repeated records using repeatability (r) to guide cow culling.",
    "desc": "<b>AIM:</b> To estimate Most Probable Producing Ability (MPPA) and Estimated Producing Ability (EPA) for dairy cows based on multiple lactation records to make scientific culling decisions.<br><br><b>THEORETICAL PRINCIPLE & EQUATIONS:</b><ul><li><b>Producing Ability:</b> The permanent capacity of an animal for repeated production traits (milk yield, fleece weight, litter size), comprising genetic value (additive + non-additive) and permanent environmental effects: <code>PA = G + E_p</code>.</li><li><b>Repeatability Weighting Factor (b):</b><br><code>b = (n &times; r) / [ 1 + (n - 1) &times; r ]</code><br>Where <code>n</code> = number of records completed by the animal; <code>r</code> = repeatability of the trait.<br>As <code>n</code> increases, <code>b</code> increases asymptotically toward 1.0.</li><li><b>Most Probable Producing Ability (MPPA):</b><br><code>MPPA = \\bar{H} + b &times; (\\bar{X} - \\bar{H})</code><br>Where <code>\\bar{H}</code> = Herd average; <code>\\bar{X}</code> = Individual cow's average performance over <code>n</code> lactations.</li><li><b>Estimated Producing Ability (EPA / Realized Deviation):</b><br><code>EPA = b &times; (\\bar{X} - \\bar{H}) = MPPA - \\bar{H}</code>.</li></ul><br><b>MODEL EXAM PROBLEM:</b><br>In an organized Murrah buffalo herd, average 305-day milk yield is <b>2,200 kg</b>. Repeatability of milk yield is <b>r = 0.40</b>. Three cows have completed the following lactation records:<br>&bull; <b>Cow A (1 lactation):</b> 2,800 kg.<br>&bull; <b>Cow B (3 lactations):</b> Average = 2,600 kg (2,500, 2,700, 2,600).<br>&bull; <b>Cow C (5 lactations):</b> Average = 2,500 kg.<br>Calculate the MPPA for each cow and rank them for culling/retention in the herd.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><b>For Cow A (n = 1, \\bar{X} = 2,800 kg):</b><br><code>b_A = (1 &times; 0.40) / [ 1 + (0)(0.40) ] = 0.40 / 1.0 = 0.400</code>.<br><code>MPPA_A = 2,200 + 0.400 &times; (2,800 - 2,200) = 2,200 + 0.400(600) = 2,200 + 240 = 2,440 kg</code>.</li><li><b>For Cow B (n = 3, \\bar{X} = 2,600 kg):</b><br><code>b_B = (3 &times; 0.40) / [ 1 + (3 - 1)(0.40) ] = 1.20 / [ 1 + 0.80 ] = 1.20 / 1.80 = 0.667</code>.<br><code>MPPA_B = 2,200 + 0.667 &times; (2,600 - 2,200) = 2,200 + 0.667(400) = 2,200 + 266.8 = 2,466.8 kg</code>.</li><li><b>For Cow C (n = 5, \\bar{X} = 2,500 kg):</b><br><code>b_C = (5 &times; 0.40) / [ 1 + (5 - 1)(0.40) ] = 2.00 / [ 1 + 1.60 ] = 2.00 / 2.60 = 0.769</code>.<br><code>MPPA_C = 2,200 + 0.769 &times; (2,500 - 2,200) = 2,200 + 0.769(300) = 2,200 + 230.7 = 2,430.7 kg</code>.</li><li><b>Ranking:</b><br>&bull; <b>Rank 1:</b> <b>Cow B (MPPA = 2,466.8 kg)</b> &rarr; Best expected future producer!<br>&bull; <b>Rank 2:</b> <b>Cow A (MPPA = 2,440.0 kg)</b><br>&bull; <b>Rank 3:</b> <b>Cow C (MPPA = 2,430.7 kg)</b></li><li><b>Inference:</b> Notice that even though Cow A had the highest single raw record (2,800 kg), <b>Cow B has a higher MPPA (2,466.8 kg)</b> because Cow B's performance is backed by 3 consistent records, providing much higher statistical reliability (b = 0.667 vs 0.400).</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What is the biological difference between Breeding Value (EBV) and Producing Ability (MPPA)?</b><br><b>A:</b> EBV reflects only additive genetic effects transmissible to offspring (<code>h&sup2;</code>); MPPA reflects the animal's own future production, incorporating <b>all genetic effects (additive + dominance + epistasis) plus permanent environment</b> (<code>r</code>).</li><li><b>Q: Why does MPPA regress individual averages toward the herd mean?</b><br><b>A:</b> To strip away temporary environmental noise (<code>E_t</code>) such as a lucky season or exceptional lush pasture during that specific lactation.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Formula for gain in accuracy with multiple records: <code>Accuracy = &radic;[ n r / (1 + (n-1)r) ]</code>. Point out that the greatest marginal gain in accuracy occurs between record 1 and record 2; after 4 records, additional records provide negligible extra accuracy.</li></ul>",
    "keyPoints": [
      "Producing Ability equals Genetic Value plus Permanent Environmental effects (PA = G + Ep).",
      "MPPA predicts an animal's future production based on past repeated records.",
      "Repeatability weighting factor formula: b = n*r / [1 + (n - 1)*r].",
      "MPPA formula: MPPA = H̄ + b * (X̄ - H̄) (where H̄ is herd mean, X̄ is cow average).",
      "Estimated Producing Ability: EPA = b * (X̄ - H̄) = MPPA - H̄.",
      "As the number of completed lactations n increases, the weighting factor b approaches 1.0.",
      "MPPA regresses raw records toward herd mean to eliminate temporary environmental noise (Et).",
      "A cow with multiple consistent records has higher MPPA reliability than a heifer with one extreme record.",
      "MPPA is used for commercial culling; EBV is used for choosing breeding seedstock.",
      "Repeatability r sets the theoretical upper ceiling for heritability h²."
    ],
    "tables": [
      {
        "title": "Repeatability Weighting Factor (b) Across Completed Lactations for r = 0.40",
        "headers": [
          "No. of Completed Records (n)",
          "Numerator (n * r)",
          "Denominator [1 + (n-1)r]",
          "Weighting Factor b",
          "Correlation with True Producing Ability"
        ],
        "rows": [
          [
            "1",
            "0.40",
            "1.00",
            "0.400",
            "0.632"
          ],
          [
            "2",
            "0.80",
            "1.40",
            "0.571",
            "0.756"
          ],
          [
            "3",
            "1.20",
            "1.80",
            "0.667",
            "0.816"
          ],
          [
            "4",
            "1.60",
            "2.20",
            "0.727",
            "0.853"
          ],
          [
            "5",
            "2.00",
            "2.60",
            "0.769",
            "0.877"
          ],
          [
            "10",
            "4.00",
            "4.60",
            "0.870",
            "0.933"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In commercial Murrah buffalo dairy operations, farm managers must make annual culling decisions. Culling strictly on first-lactation raw milk yield often eliminates genetically superior cows that suffered temporary mastitis or lameness. Veterinarians compute <b>MPPA after the second lactation</b>, preventing premature culling of valuable foundation breeding stock.",
    "tags": [
      "Animal Breeding Lab",
      "MPPA",
      "EPA",
      "Repeatability",
      "Culling",
      "Murrah Buffalo",
      "Producing Ability",
      "Lactation Records"
    ]
  },
  "p3-t04": {
    "summary": "Computation of Wright's Inbreeding Coefficient (Fx) and Coefficient of Relationship (Rxy) from directed pedigree charts and arrow diagrams.",
    "desc": "<b>AIM:</b> To convert a livestock pedigree chart into a directed arrow diagram, trace ancestral connecting paths, and calculate the Inbreeding Coefficient (F_X) and Relationship (R_XY).<br><br><b>WRIGHT'S PATH COEFFICIENT FORMULAS:</b><ul><li><b>Inbreeding Coefficient of Individual X (F_X):</b><br><code>F_X = &Sigma; [ (1/2)^{n_1 + n_2 + 1} &times; (1 + F_A) ]</code><br>Where: <code>A</code> = Common ancestor shared by Sire (S) and Dam (D); <code>n_1</code> = generations from Sire to A; <code>n_2</code> = generations from Dam to A; <code>F_A</code> = inbreeding of ancestor A.</li><li><b>Coefficient of Relationship between X and Y (R_XY):</b><br><code>R_XY = &Sigma; [ (1/2)^{n_1 + n_2} &times; (1 + F_A) ] / &radic;[ (1 + F_X)(1 + F_Y) ]</code></li></ul><br><b>MODEL EXAM PROBLEM 1 (SIRE &times; DAUGHTER MATING):</b><br>A dairy bull 'S' is mated to his own daughter 'D' (where D was produced by mating S to an unrelated cow M). Individual 'X' is born from this mating (S &times; D). Calculate the inbreeding coefficient F_X.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><b>Identify Parents of X:</b> Sire = <code>S</code>, Dam = <code>D</code>.</li><li><b>Identify Common Ancestor:</b> Bull <code>S</code> is the sire of X and also the sire of dam D. Hence, <code>A = S</code>.</li><li><b>Trace Path:</b> <code>S &larr; (n1=0) &mdash; S &mdash; (n2=1) &rarr; D</code>.</li><li><code>n_1 = 0</code> (S is the common ancestor itself); <code>n_2 = 1</code> (from D back to S).</li><li>Assume bull S is not inbred (<code>F_S = 0</code>).</li><li><b>Compute F_X:</b><br><code>F_X = (1/2)^{0 + 1 + 1} &times; (1 + 0) = (1/2)&sup2; = 1/4 = 0.25 (25.0%)</code>.</li><li><b>Result:</b> <b>F_X = 0.25 (25%)</b>.</li></ol><br><b>MODEL EXAM PROBLEM 2 (FULL-SIB MATING):</b><br>Individual 'X' is born from the mating of a full brother (B) and full sister (S), who share both Sire (P) and Dam (M). Assuming P and M are unrelated and non-inbred, calculate F_X.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li>Parents of X: Sire = B, Dam = S.</li><li><b>Two Common Ancestors:</b> Sire <code>P</code> and Dam <code>M</code>.</li><li><b>Path 1 (through Common Ancestor P):</b><br><code>B &larr; P &rarr; S</code> &rarr; <code>n_1 = 1, n_2 = 1</code>.<br>Contribution 1 = <code>(1/2)^{1 + 1 + 1} &times; (1 + 0) = (1/2)&sup3; = 1/8 = 0.125</code>.</li><li><b>Path 2 (through Common Ancestor M):</b><br><code>B &larr; M &rarr; S</code> &rarr; <code>n_1 = 1, n_2 = 1</code>.<br>Contribution 2 = <code>(1/2)^{1 + 1 + 1} &times; (1 + 0) = (1/2)&sup3; = 1/8 = 0.125</code>.</li><li><b>Sum Across All Paths:</b><br><code>F_X = 1/8 + 1/8 = 2/8 = 1/4 = 0.25 (25.0%)</code>.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: What are the three strict rules for tracing paths in an arrow diagram?</b><br><b>A:</b> (1) A path must go backward to a common ancestor and forward to the other parent (never forward then backward), (2) A path cannot pass through any individual more than once, and (3) A path cannot pass through any individual who is not an ancestor of both parents.</li><li><b>Q: What is the relationship (R_XY) between full sibs vs half sibs?</b><br><b>A:</b> Full sibs: <code>R = 0.50 (50%)</code>; Half sibs: <code>R = 0.25 (25%)</code>.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Inbreeding of Common Ancestor: If the common ancestor A is itself inbred (e.g. <code>F_A = 0.125</code>), never forget to multiply by <code>(1 + F_A) = 1.125</code>! Forgetting this is a guaranteed penalty in exam problems.</li><li>Relationship between Mates equals twice the inbreeding of their progeny: <code>F_X = (1/2) R_{SD} &times; &radic;[(1 + F_S)(1 + F_D)]</code>.</li></ul>",
    "keyPoints": [
      "Sewall Wright's formula: F_X = Σ [ (1/2)^(n1 + n2 + 1) * (1 + FA) ].",
      "n1 is generations from sire to common ancestor; n2 is generations from dam to common ancestor.",
      "FA is the inbreeding coefficient of the common ancestor itself.",
      "Sire x Daughter mating produces offspring with F = 25% (0.25).",
      "Full-sib mating (two common ancestors) produces offspring with F = 25% (0.25).",
      "Half-sib mating (one common ancestor) produces offspring with F = 12.5% (0.125).",
      "First cousin mating produces offspring with F = 6.25% (0.0625).",
      "Arrow paths must never pass through the same individual twice or reverse direction.",
      "Relationship between full sibs is R = 0.50; between half sibs is R = 0.25.",
      "Inbreeding coefficient of progeny equals the kinship coefficient between its parents (Fx = Φ_SD)."
    ],
    "tables": [
      {
        "title": "Path Analysis Computation Sheet for Standard Inbred Pedigree Configurations",
        "headers": [
          "Mating Relationship Type",
          "Common Ancestors (A)",
          "Connecting Path",
          "Generations (n1, n2)",
          "Formula Contribution",
          "Resulting Progeny Inbreeding (F_X)"
        ],
        "rows": [
          [
            "Sire &times; Daughter",
            "Sire (S)",
            "S &larr; S &rarr; D",
            "n1=0, n2=1",
            "(1/2)^{0+1+1}",
            "0.2500 (25.0%)"
          ],
          [
            "Dam &times; Son",
            "Dam (D)",
            "S &larr; D &rarr; D",
            "n1=1, n2=0",
            "(1/2)^{1+0+1}",
            "0.2500 (25.0%)"
          ],
          [
            "Full Brother &times; Full Sister",
            "Sire (P) + Dam (M)",
            "B &larr; P &rarr; S  and  B &larr; M &rarr; S",
            "n1=1, n2=1 (2 paths)",
            "2 &times; (1/2)^{1+1+1}",
            "0.2500 (25.0%)"
          ],
          [
            "Half Brother &times; Half Sister",
            "Common Sire (S)",
            "B &larr; S &rarr; S",
            "n1=1, n2=1 (1 path)",
            "1 &times; (1/2)^{1+1+1}",
            "0.1250 (12.5%)"
          ],
          [
            "Grandparent &times; Grandchild",
            "Grandparent (G)",
            "S &larr; G &rarr; P &rarr; D",
            "n1=0, n2=2",
            "(1/2)^{0+2+1}",
            "0.1250 (12.5%)"
          ],
          [
            "First Cousins",
            "Grandparents (G1, G2)",
            "S &larr; P1 &larr; G &rarr; P2 &rarr; D",
            "n1=2, n2=2 (2 paths)",
            "2 &times; (1/2)^{2+2+1}",
            "0.0625 (6.25%)"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> Veterinarians conducting clinical evaluations of litters presented with multiple congenital abnormalities (e.g., cleft palate, umbilical hernias, or cryptorchidism in dogs) draw a 4-generation arrow diagram. Calculating <code>F_X &ge; 0.25</code> diagnoses <b>Inbreeding Depression unmasking deleterious recessives</b>, justifying immediate clinical advice to retire the bitch from breeding or introduce an unrelated stud dog.",
    "tags": [
      "Animal Breeding Lab",
      "Inbreeding",
      "Wright's Formula",
      "Path Coefficients",
      "Arrow Diagram",
      "Coefficient of Relationship",
      "Full-Sibs"
    ]
  },
  "p3-t05": {
    "summary": "Estimation of Mid-Parent Heterosis, Heterobeltiosis, and retained heterosis percentage in rotational crossbreeding and composite livestock breeds.",
    "desc": "<b>AIM:</b> To estimate absolute and percentage heterosis (Mid-Parent Heterosis and Better-Parent Heterosis) and calculate retained heterosis in composite breeds.<br><br><b>CORE HETEROSIS EQUATIONS:</b><ul><li><b>1. Mid-Parent Heterosis (H):</b><br><code>H = \\bar{F}_1 - \\bar{MP} = \\bar{F}_1 - [ (\\bar{P}_1 + \\bar{P}_2) / 2 ]</code></li><li><b>2. Percentage Heterosis (H%):</b><br><code>H% = [ (\\bar{F}_1 - \\bar{MP}) / \\bar{MP} ] &times; 100</code></li><li><b>3. Better-Parent Heterosis (Heterobeltiosis):</b><br><code>Heterobeltiosis% = [ (\\bar{F}_1 - \\bar{BP}) / \\bar{BP} ] &times; 100</code><br>Where <code>\\bar{BP}</code> is the mean of the superior purebred parental breed.</li><li><b>4. Retained Heterosis in Rotational Crosses (RH%):</b><br><code>RH% = [ (2^n - 2) / (2^n - 1) ] &times; 100</code> (where n = number of breeds in rotation).</li><li><b>5. Retained Heterosis in Composite / Synthetic Breeds (RH%):</b><br><code>RH% = [ 1 - &Sigma; (p_i)&sup2; ] &times; 100</code> (where p_i = fractional inheritance of breed i).</li></ul><br><b>MODEL EXAM PROBLEM 1 (HETEROSIS CALCULATION):</b><br>In a dairy crossbreeding experiment, purebred Holstein-Friesian (HF) cows averaged <b>4,500 kg</b> 305-day milk yield, and purebred Gir cows averaged <b>2,500 kg</b>. The F1 crossbred cows (HF &times; Gir) produced an average of <b>3,850 kg</b>.<br>1. Calculate Mid-Parent Value (MP).<br>2. Calculate absolute heterosis (H) and percentage heterosis (H%).<br>3. Did the F1 cross show heterobeltiosis?<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><code>\\bar{P}_1 (HF) = 4,500 kg</code>; <code>\\bar{P}_2 (Gir) = 2,500 kg</code>.</li><li><code>Mid-Parent (MP) = (4,500 + 2,500) / 2 = 7,000 / 2 = 3,500 kg</code>.</li><li><code>Absolute Heterosis H = \\bar{F}_1 - MP = 3,850 - 3,500 = +350 kg</code>.</li><li><code>Percentage Heterosis H% = (350 / 3,500) &times; 100 = +10.0%</code>.</li><li><b>Heterobeltiosis Check:</b><br>Better Parent <code>BP = 4,500 kg</code> (HF).<br><code>F1 (3,850 kg) &lt; BP (4,500 kg)</code>.<br><code>Heterobeltiosis = [ (3,850 - 4,500) / 4,500 ] &times; 100 = -14.44%</code>.<br><b>Inference:</b> The F1 cross exhibited <b>10.0% standard mid-parent heterosis</b>, but did NOT show heterobeltiosis because its milk yield was below the cold-climate purebred HF under European conditions. However, under tropical heat, F1 excels due to disease resilience!</li></ol><br><b>MODEL EXAM PROBLEM 2 (RETAINED HETEROSIS IN SYNTHETIC BREEDS):</b><br>Calculate the retained heterosis in:<br>1. <b>Karan Fries</b> (50% HF + 50% Tharparkar).<br>2. <b>Avishaan Sheep</b> (1/2 Malpura + 1/4 Garole + 1/4 Patanwadi).<br><b>Solution:</b><br><ol><li><b>Karan Fries:</b> <code>RH% = [ 1 - (0.50&sup2; + 0.50&sup2;) ] &times; 100 = [ 1 - (0.25 + 0.25) ] &times; 100 = [ 1 - 0.50 ] &times; 100 = 50.0%</code>.</li><li><b>Avishaan Sheep:</b> <code>RH% = [ 1 - (0.50&sup2; + 0.25&sup2; + 0.25&sup2;) ] &times; 100 = [ 1 - (0.25 + 0.0625 + 0.0625) ] &times; 100 = [ 1 - 0.375 ] &times; 100 = 62.5%</code>.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Which traits express the highest percentage heterosis in livestock?</b><br><b>A:</b> <b>Fitness, reproductive, and early survival traits</b> (e.g., conception rate, embryo livability, litter size in pigs) exhibit highest heterosis (15–25%), whereas carcass and skeletal traits exhibit lowest (< 5%).</li><li><b>Q: What is F2 breakdown (Recombination Loss)?</b><br><b>A:</b> When F1 crossbreds are mated inter-se (F1 &times; F1), 50% of individual heterosis is lost due to segregation, and favorable epistatic gene complexes are disrupted by crossing over.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Formula for Retained Heterosis in 2-breed Crisscrossing at equilibrium: <code>RH = 2/3 = 66.67%</code>; in 3-breed rotation: <code>RH = 6/7 = 85.71%</code>. Stating equilibrium formulas without deriving long cycles scores instant full marks!</li></ul>",
    "keyPoints": [
      "Mid-Parent Heterosis formula: H = F1 - (P1 + P2)/2.",
      "Percentage heterosis: H% = [(F1 - MP) / MP] * 100.",
      "Heterobeltiosis is superiority over the better parent: [(F1 - BP) / BP] * 100.",
      "Retained heterosis in a composite breed: RH% = [1 - Σ(pi)²] * 100.",
      "A 2-breed 50:50 composite retains exactly 50% of maximum heterosis permanently.",
      "A 3-breed composite (1/2, 1/4, 1/4) retains 62.5% heterosis permanently.",
      "Two-breed rotational crossing (crisscrossing) retains 66.7% (2/3) heterosis at equilibrium.",
      "Three-breed rotational crossing retains 85.7% (6/7) heterosis at equilibrium.",
      "Heterosis is highest for low-heritability fitness and reproductive traits.",
      "F2 breakdown results in 50% loss of individual heterosis upon inter-se mating."
    ],
    "tables": [
      {
        "title": "Retained Heterosis Percentage in Systematic Livestock Mating Designs",
        "headers": [
          "Crossbreeding System",
          "Parental Composition",
          "Equilibrium Retained Heterosis (RH%)",
          "Need for Purebred Sires",
          "Primary Field Application"
        ],
        "rows": [
          [
            "Two-Breed Terminal",
            "Breed A sire &times; Breed B dam",
            "100.0% (in F1 progeny)",
            "Yes (maintain both pure breeds)",
            "Commercial broiler and beef production"
          ],
          [
            "Two-Breed Rotation (Crisscrossing)",
            "Alternating Breeds A and B",
            "66.7% (2/3 of maximum)",
            "Yes (requires 2 pure breeds perpetually)",
            "Commercial swine and sheep production"
          ],
          [
            "Three-Breed Rotation",
            "Alternating Breeds A, B, and C",
            "85.7% (6/7 of maximum)",
            "Yes (requires 3 pure breeds)",
            "Commercial swine maternal lines"
          ],
          [
            "2-Breed Composite (50:50)",
            "Karan Fries (1/2 HF + 1/2 Tharparkar)",
            "50.0% (permanently fixed)",
            "No (mates composite to composite)",
            "Stabilized tropical dairy cattle"
          ],
          [
            "3-Breed Composite (50:25:25)",
            "Avishaan (1/2 Malpura + 1/4 Garole + 1/4 Patanwadi)",
            "62.5% (permanently fixed)",
            "No (self-contained composite flock)",
            "Prolific mutton sheep in Rajasthan"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In commercial broiler and layer operations, farmers purchasing day-old commercial chicks sometimes attempt to save costs by collecting eggs from commercial hybrid hens and incubating them on-farm. Veterinarians explain the genetic reality of <b>F2 Breakdown</b>: inter-se mating of commercial four-way crosses shatters heterosis, causing a <b>30% drop in egg production and extreme flock variability</b>, proving that hybrid chicks must be procured fresh every generation from primary breeding hatcheries.",
    "tags": [
      "Animal Breeding Lab",
      "Heterosis",
      "Hybrid Vigour",
      "Heterobeltiosis",
      "Retained Heterosis",
      "Karan Fries",
      "Avishaan",
      "F2 Breakdown"
    ]
  },
  "p3-t06": {
    "summary": "Computation of historical sire evaluation indices (Daughter Average, Mount Hope, Contemporary Comparison) and mathematical construction of multi-trait selection indexes.",
    "desc": "<b>AIM:</b> To calculate classical sire indices (Daughter Average, Intermediate/Mount Hope, and Contemporary Comparison) and solve simultaneous equations to construct a multi-trait Selection Index.<br><br><b>CORE SIRE EVALUATION & SELECTION INDEX EQUATIONS:</b><ul><li><b>1. Simple Daughter Average:</b> <code>I = \\bar{D}</code>.</li><li><b>2. Intermediate Index (Hansson-Yapp / Mount Hope Index):</b><br><code>I = 2\\bar{D} - \\bar{M}</code> (where <code>\\bar{D}</code> = Daughter average; <code>\\bar{M}</code> = Dam average).</li><li><b>3. Rice's Index:</b> <code>I = 2\\bar{D} - \\bar{H}</code> (where <code>\\bar{H}</code> = Herd average).</li><li><b>4. Contemporary Comparison (Robertson and Rendel):</b><br><code>I = \\bar{A} + [ n / (n + 12) ] &times; (\\bar{D} - \\bar{C})</code><br>Where <code>\\bar{A}</code> = Breed average; <code>n</code> = number of daughters; <code>\\bar{D}</code> = daughter average; <code>\\bar{C}</code> = contemporary average.</li><li><b>5. Hazel's Multi-Trait Selection Index (1943):</b><br>Index: <code>I = b_1 X_1 + b_2 X_2 + ... + b_m X_m</code><br>Aggregate Economic Genotype: <code>H = a_1 G_1 + a_2 G_2 + ... + a_m G_m</code> (where a_i = relative economic values).<br>Matrix Equation to solve weighting coefficients <code>b</code>:<br><code>[ P ] [ b ] = [ G ] [ a ]  &rarr;  [ b ] = [ P ]⁻¹ [ G ] [ a ]</code><br>For Two Traits:<br><code>b_1 P_{11} + b_2 P_{12} = a_1 G_{11} + a_2 G_{12}</code><br><code>b_1 P_{21} + b_2 P_{22} = a_1 G_{21} + a_2 G_{22}</code>.</li></ul><br><b>MODEL EXAM PROBLEM 1 (SIRE INDICES):</b><br>A dairy bull was mated to cows averaging <b>3,000 kg</b> milk. His 20 daughters produced an average of <b>3,400 kg</b> in a herd where contemporaries averaged <b>3,100 kg</b>. Assume breed average <code>\\bar{A} = 3,000 kg</code>.<br>Calculate the sire's index using: (1) Daughter Average, (2) Mount Hope Index, (3) Contemporary Comparison.<br><br><b>STEP-BY-STEP CALCULATION:</b><ol><li><b>Daughter Average:</b> <code>I = \\bar{D} = 3,400 kg</code>.</li><li><b>Mount Hope Index:</b><br><code>I = 2\\bar{D} - \\bar{M} = 2(3,400) - 3,000 = 6,800 - 3,000 = 3,800 kg</code>.</li><li><b>Contemporary Comparison (CC):</b><br><code>Weighting Factor = n / (n + 12) = 20 / (20 + 12) = 20 / 32 = 0.625</code>.<br><code>Daughter - Contemporary = 3,400 - 3,100 = +300 kg</code>.<br><code>I = 3,000 + 0.625 &times; (300) = 3,000 + 187.5 = 3,187.5 kg</code>.</li></ol><br><b>MODEL EXAM PROBLEM 2 (TWO-TRAIT SELECTION INDEX):</b><br>Construct a selection index combining Milk Yield (X1 in 100 kg) and Age at First Calving (X2 in months). Given phenotypic variances <code>P11 = 16, P22 = 25</code>, covariance <code>P12 = -4</code>; genetic variances <code>G11 = 4, G22 = 5</code>, genetic covariance <code>G12 = -2</code>; and relative economic values <code>a1 = +10, a2 = -5</code>.<br><b>Simultaneous Equations:</b><br><ol><li><code>RHS_1 = a1(G11) + a2(G12) = 10(4) + (-5)(-2) = 40 + 10 = 50</code>.</li><li><code>RHS_2 = a1(G21) + a2(G22) = 10(-2) + (-5)(5) = -20 - 25 = -45</code>.</li><li>Equations:<br><code>16 b_1 - 4 b_2 = 50</code> &nbsp; &rarr; &nbsp; (Eq. 1)<br><code>-4 b_1 + 25 b_2 = -45</code> &nbsp; &rarr; &nbsp; (Eq. 2)</li><li>Multiply Eq. 2 by 4: <code>-16 b_1 + 100 b_2 = -180</code>.</li><li>Add to Eq. 1: <code>96 b_2 = -130  &rarr;  b_2 = -130 / 96 = -1.354</code>.</li><li>Substitute in Eq. 1: <code>16 b_1 = 50 + 4(-1.354) = 50 - 5.416 = 44.584  &rarr;  b_1 = 44.584 / 16 = 2.787</code>.</li><li><b>Selection Index:</b> <code>I = 2.787 &times; X_1 - 1.354 &times; X_2</code>.</li></ol><br><b>VIVA-VOCE QUESTIONS & ANSWERS:</b><ol><li><b>Q: Why is the Mount Hope Index often biased upwards?</b><br><b>A:</b> It assumes dam and daughter environments are identical; in improving herds, daughters receive better feed and housing, falsely crediting environmental progress to the sire's breeding value.</li><li><b>Q: What is the primary advantage of Hazel's Selection Index over Independent Culling Levels?</b><br><b>A:</b> Hazel's index allows <b>superiority in one trait to compensate for a minor deficiency in another trait</b>, maximizing overall aggregate economic progress.</li></ol>",
    "eliteDesc": "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br><ul><li>Notice the sign of the economic weights: Milk yield has positive economic value (<code>a1 = +10</code>), while age at first calving has negative economic value (<code>a2 = -5</code>, because late calving costs money). Setting the right economic sign is vital!</li><li>Contemporary Comparison weighting factor constant: The constant <b>12</b> represents <code>(4 - h&sup2;) / h&sup2;</code> when heritability is approximately <code>0.25</code>! Showing this derivation proves 10/10 knowledge.</li></ul>",
    "keyPoints": [
      "Simple Daughter Average: I = D̄; ignores dams' merit and herd environment.",
      "Mount Hope Index: I = 2D̄ - M̄; adjusts for dams' genetic contribution.",
      "Robertson and Rendel's Contemporary Comparison: I = Ā + [n/(n+12)] * (D̄ - C̄).",
      "The constant 12 in CC equals (4 - h²) / h² for h² = 0.25.",
      "Hazel's Selection Index (1943) combines multiple traits weighted by economic values: I = Σ bi Xi.",
      "Aggregate economic genotype: H = Σ ai Gi.",
      "Matrix equation for selection index weights: [P] [b] = [G] [a].",
      "Economic weight ai represents the net monetary gain per unit improvement in the trait.",
      "Selection index maximizes the correlation between the index I and aggregate genotype H (r_IH).",
      "Selection index is genetically and economically superior to tandem selection and independent culling."
    ],
    "tables": [
      {
        "title": "Comparison of Classical Dairy Sire Evaluation Indices",
        "headers": [
          "Sire Index",
          "Formula",
          "Adjusts for Dams' Merit?",
          "Adjusts for Herd Environment?",
          "Major Bias / Limitation"
        ],
        "rows": [
          [
            "Daughter Average",
            "I = D̄",
            "No",
            "No",
            "Heavily biased by herd feeding and management level"
          ],
          [
            "Mount Hope (Intermediate)",
            "I = 2D̄ - M̄",
            "Yes (subtracts dam mean)",
            "No",
            "Biased upward by secular environmental progress over time"
          ],
          [
            "Rice's Index",
            "I = 2D̄ - H̄",
            "No (uses herd average)",
            "Partially",
            "Assumes dams represent the exact herd average"
          ],
          [
            "Contemporary Comparison",
            "I = Ā + [n/(n+12)]*(D̄ - C̄)",
            "Partially",
            "Yes (compares with herdmates)",
            "Fails to adjust for genetic merit of contemporary mates"
          ],
          [
            "Animal Model BLUP",
            "y = Xβ + Zu + e",
            "Yes (complete pedigree)",
            "Yes (Generalized Least Squares)",
            "Gold standard; requires nationwide computerized database"
          ]
        ]
      }
    ],
    "clinical": "<b>VETERINARY FIELD APPLICATION:</b> In commercial poultry breeding organizations, geneticists construct a <b>Four-Trait Selection Index</b>: <code>I = b1(Egg Production to 40 weeks) + b2(Egg Weight) - b3(Age at First Egg) - b4(Feed Conversion Ratio)</code>. Veterinarians and breeding managers rank candidate roosters and hens on this total score, producing balanced commercial layer chicks that lay large eggs early without consuming excessive feed.",
    "tags": [
      "Animal Breeding Lab",
      "Sire Index",
      "Mount Hope",
      "Contemporary Comparison",
      "Selection Index",
      "Hazel",
      "Economic Weight",
      "BLUP"
    ]
  }
};
