# -*- coding: utf-8 -*-
"""
Practical Unit 3: Topics p3-t01 to p3-t06
Principles of Animal Breeding Lab (IVRI Undergrad 10 CGPA Standard)
Strictly exam-specific: Aim, Principle, Formulae, Solved Model Problems, Inferences, Viva-Voce
"""

topics = {}

topics["p3-t01"] = {
    "summary": "Step-by-step computation of Selection Differential (S), Selection Intensity (i), and Generation Interval (L) across the four genetic pathways in livestock herds.",
    "desc": (
        "<b>AIM:</b> To compute Selection Differential (S), Selection Intensity (i), and Generation Interval (L) in dairy cattle and sheep breeding herds.<br><br>"
        "<b>CORE QUANTITATIVE EQUATIONS:</b>"
        "<ul>"
        "<li><b>1. Selection Differential (S):</b><br>"
        "<code>S = \\bar{X}_s - \\bar{X}_p</code><br>"
        "Where <code>\\bar{X}_s</code> = Mean phenotypic performance of selected parents; <code>\\bar{X}_p</code> = Mean performance of the base parental population."
        "<br>&bull; <i>Effective / Weighted Selection Differential:</i> <code>S_w = [ &Sigma; w_i &times; (X_i - \\bar{X}_p) ] / &Sigma; w_i</code> (weighted by number of offspring left by each parent).</li>"
        "<li><b>2. Selection Intensity (i):</b><br>"
        "<code>i = S / &sigma;_P</code><br>"
        "Standardized selection differential; read directly from truncation selection tables for proportion <code>p</code> saved.</li>"
        "<li><b>3. Average Selection Differential of Parents:</b><br>"
        "<code>\\bar{S} = (S_m + S_f) / 2</code> (where S_m = sire differential, S_f = dam differential).</li>"
        "<li><b>4. Generation Interval (L):</b><br>"
        "Average age of parents when their offspring destined to become breeding replacements are born.<br>"
        "<code>L = (L_{ss} + L_{sd} + L_{ds} + L_{dd}) / 4</code><br>"
        "Where <code>ss</code> = sire to son, <code>sd</code> = sire to daughter, <code>ds</code> = dam to son, <code>dd</code> = dam to daughter pathways.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM:</b><br>"
        "In a herd of 200 Sahiwal cows, the average 305-day lactation milk yield is <b>2,400 kg with &sigma;_P = 400 kg</b>. "
        "Top 20 cows are selected as elite bull-mothers, averaging <b>3,200 kg</b> milk. "
        "The selected AI breeding bulls used have a transmitting superiority equivalent to dams yielding <b>3,600 kg</b> (sire differential S_m = 1,200 kg).<br>"
        "1. Calculate the selection differential of dams (S_f) and overall selection differential (\\bar{S}).<br>"
        "2. Calculate selection intensity in dams (i_f).<br>"
        "3. If average parental ages along the four pathways are: L_ss = 6 yrs, L_sd = 5.5 yrs, L_ds = 6.5 yrs, L_dd = 5 yrs, calculate average generation interval L.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><b>Dam Selection Differential:</b><br>"
        "<code>S_f = \\bar{X}_s - \\bar{X}_p = 3,200 - 2,400 = +800 kg</code>.</li>"
        "<li><b>Sire Selection Differential:</b> <code>S_m = +1,200 kg</code>.</li>"
        "<li><b>Overall Average Selection Differential:</b><br>"
        "<code>\\bar{S} = (S_m + S_f) / 2 = (1,200 + 800) / 2 = 2,000 / 2 = 1,000 kg</code>.</li>"
        "<li><b>Selection Intensity in Dams (i_f):</b><br>"
        "<code>i_f = S_f / &sigma;_P = 800 / 400 = 2.00 standard deviations</code>.<br>"
        "(Corresponds to selecting top 10% of females).</li>"
        "<li><b>Average Generation Interval (L):</b><br>"
        "<code>L = (6.0 + 5.5 + 6.5 + 5.0) / 4 = 23.0 / 4 = 5.75 years</code>.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Why is selection intensity much higher in males than in females?</b><br>"
        "<b>A:</b> Due to biological reproductive rates: a herd needs replacement females (selecting 60–80% of heifers, i &approx; 0.3–0.6), but through AI, only top 1% to 2% of bulls are selected (i &approx; 2.4–2.6).</li>"
        "<li><b>Q: What are typical generation intervals across domestic farm species?</b><br>"
        "<b>A:</b> Dairy Cattle & Buffaloes: <b>5 to 6 years</b>; Sheep & Goats: <b>2.5 to 3 years</b>; Swine: <b>1.5 to 2 years</b>; Poultry: <b>1 year</b>.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Difference between Potential vs Realized (Effective) Selection Differential: Potential S is calculated on selected parents; Realized S_w weights parents by the actual number of offspring surviving to breeding age. Natural selection and involuntary culling often make <code>S_w &lt; S</code>.</li>"
        "<li>Genomic Selection impact: Genomic evaluation slashes the sire generation interval (L_ss and L_sd) from 6.0 years down to <b>1.5 to 2.0 years</b>, roughly halving total generation interval L.</li>"
        "</ul>"
    ),
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
            "headers": ["Proportion Selected (p)", "Selection Intensity (i in &sigma; units)", "Livestock Breeding Category", "Practical Farm Example"],
            "rows": [
                ["0.01 (1%)", "2.665", "Elite AI Sires / Bull Fathers", "Top 1 bull selected out of 100 tested"],
                ["0.05 (5%)", "2.063", "Elite Bull Mothers", "Top 5 donor cows in nucleus MOET herd"],
                ["0.10 (10%)", "1.755", "Registered Seedstock Sires", "Ram selection in commercial sheep flock"],
                ["0.20 (20%)", "1.399", "Boar replacements in swine", "Top 20% boars retained for breeding"],
                ["0.50 (50%)", "0.798", "Commercial heifer replacements", "Retaining 50% replacement dairy heifers"],
                ["0.80 (80%)", "0.350", "Low-intensity female culling", "Routine culling of bottom 20% scrub cows"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "Veterinarians auditing commercial dairy breeding herds often discover that annual genetic progress is stagnant "
        "because dairy farmers retain cows until 12–14 years of age, inflating the dam generation interval (<code>L_dd &gt; 8 years</code>). "
        "Veterinarians recommend strict <b>replacement of older, genetically lagging cows with superior first-calvers</b> at 4th or 5th parity, "
        "compressing herd generation interval down to 4.5 years and boosting annual genetic progress by 25%."
    ),
    "tags": ["Animal Breeding Lab", "Selection Differential", "Selection Intensity", "Generation Interval", "Breeder's Equation", "Sahiwal Cattle"]
}

topics["p3-t02"] = {
    "summary": "Estimation of expected genetic gain per generation (ΔG), annual genetic progress (ΔG/yr), and correlated response to indirect selection (CRY).",
    "desc": (
        "<b>AIM:</b> To estimate direct expected genetic response (&Delta;G), annual genetic progress, and correlated response (CR_Y) in livestock improvement programs.<br><br>"
        "<b>CORE GENETIC RESPONSE EQUATIONS:</b>"
        "<ul>"
        "<li><b>1. Expected Genetic Gain Per Generation (&Delta;G):</b><br>"
        "<code>&Delta;G = h&sup2; &times; S = h&sup2; &times; (\\bar{X}_s - \\bar{X}_p)</code><br>"
        "Alternatively: <code>&Delta;G = i &times; r_{TI} &times; &sigma;_A = i &times; h &times; &sigma;_A</code> (where r_{TI} = accuracy of selection).</li>"
        "<li><b>2. Annual Genetic Gain (&Delta;G_{yr}):</b><br>"
        "<code>&Delta;G_{yr} = &Delta;G / L = [ (h&sup2; &times; S_m) + (h&sup2; &times; S_f) ] / (L_m + L_f)</code><br>"
        "<code>&Delta;G_{yr} = [ (i_m &times; r_{TIm}) + (i_f &times; r_{TIf}) ] &times; &sigma;_A / (L_m + L_f)</code>.</li>"
        "<li><b>3. Correlated Response in Trait Y from Selection on Trait X (CR_Y):</b><br>"
        "<code>CR_Y = i_X &times; r_g &times; h_X &times; h_Y &times; &sigma;_{P_Y}</code><br>"
        "Where <code>r_g</code> = genetic correlation between X and Y; <code>h_X, h_Y</code> = square roots of heritabilities; <code>&sigma;_{P_Y}</code> = phenotypic standard deviation of Y.</li>"
        "<li><b>4. Relative Efficiency of Indirect Selection (RE):</b><br>"
        "<code>RE = CR_Y / R_Y = r_g &times; (h_X / h_Y)</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (DIRECT GENETIC GAIN):</b><br>"
        "In a herd of Sahiwal cattle, the average lactation milk yield is 2,400 kg. Selected parents have a mean lactation yield of 2,900 kg. "
        "Heritability of milk yield is <code>h&sup2; = 0.25</code>. If the average generation interval is <code>L = 5 years</code>:<br>"
        "1. Calculate expected genetic gain per generation (&Delta;G).<br>"
        "2. Calculate expected annual genetic gain (&Delta;G_{yr}).<br>"
        "3. What will be the expected mean milk yield of the offspring generation?<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><code>Selection Differential S = 2,900 - 2,400 = 500 kg</code>.</li>"
        "<li><code>&Delta;G = h&sup2; &times; S = 0.25 &times; 500 = 125.0 kg per generation</code>.</li>"
        "<li><code>Annual Genetic Gain (&Delta;G_{yr}) = &Delta;G / L = 125.0 / 5 = 25.0 kg / year</code> (approx. 1% annual gain).</li>"
        "<li><code>Offspring Generation Mean = Base Mean + &Delta;G = 2,400 + 125 = 2,525 kg</code>.</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM 2 (CORRELATED RESPONSE):</b><br>"
        "Selection is practiced for 6-month Body Weight (X) in Malpura sheep to improve adult Fleece Weight (Y). "
        "Given: <code>i_X = 1.40</code>, <code>h&sup2;_X = 0.36 (h_X = 0.60)</code>, <code>h&sup2;_Y = 0.25 (h_Y = 0.50)</code>, <code>&sigma;_{P_Y} = 0.40 kg</code>, and <code>r_g = +0.50</code>. "
        "Calculate the correlated response in fleece weight (CR_Y).<br>"
        "<b>Solution:</b><br>"
        "<code>CR_Y = i_X &times; r_g &times; h_X &times; h_Y &times; &sigma;_{P_Y}</code><br>"
        "<code>CR_Y = 1.40 &times; (+0.50) &times; 0.60 &times; 0.50 &times; 0.40 kg</code><br>"
        "<code>CR_Y = 1.40 &times; 0.50 &times; 0.12 = 1.40 &times; 0.060 = +0.084 kg (84 grams per generation)</code>."
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>When is indirect selection more efficient than direct selection? Whenever <code>RE &gt; 1.0</code>, which occurs when <code>r_g &times; h_X &gt; h_Y</code> (i.e. Trait X has higher heritability than Y and genetic correlation is strong).</li>"
        "<li>Always distinguish between <code>&Delta;G</code> (per generation) and <code>&Delta;G_{yr}</code> (annual). Mixing these up is the single most common student calculation error.</li>"
        "</ul>"
    ),
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
            "headers": ["Biometrical Parameter", "Symbol", "Mathematical Role", "Breeding Intervention to Maximize Gain", "Field Limitation"],
            "rows": [
                ["Selection Intensity", "i", "Numerator (direct multiplier)", "Artificial Insemination, sexed semen (keep top 1% sires)", "Inbreeding accumulation in closed nucleus"],
                ["Accuracy of Selection", "r_TI", "Numerator (direct multiplier)", "Progeny testing, Genomic Selection (GBLUP)", "Cost of progeny recording, pedigree errors"],
                ["Additive Genetic SD", "&sigma;_A", "Numerator (raw genetic fuel)", "Outcrossing, broad base foundation population", "Biological ceiling within pure breeds"],
                ["Generation Interval", "L", "Denominator (inversely related)", "Genomic selection of calves, juvenile MOET", "Age at sexual maturity, long gestation in cattle"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In commercial pig breeding, direct measurement of backfat thickness on live breeding boars is invasive and difficult without ultrasound. "
        "Breeding companies select boars indirectly for <b>Post-Weaning Average Daily Gain (ADG)</b>. "
        "Because ADG has high heritability (h&sup2; = 0.40) and strong favorable genetic correlation with feed conversion efficiency (r_g = -0.65), "
        "fast-growing boars automatically produce market progeny that convert feed to lean pork with minimal expensive concentrate consumption."
    ),
    "tags": ["Animal Breeding Lab", "Genetic Gain", "Breeder's Equation", "Correlated Response", "Relative Efficiency", "Indirect Selection", "Malpura Sheep"]
}

topics["p3-t03"] = {
    "summary": "Estimation of Estimated Producing Ability (EPA) and Most Probable Producing Ability (MPPA) for repeated records using repeatability (r) to guide cow culling.",
    "desc": (
        "<b>AIM:</b> To estimate Most Probable Producing Ability (MPPA) and Estimated Producing Ability (EPA) for dairy cows based on multiple lactation records to make scientific culling decisions.<br><br>"
        "<b>THEORETICAL PRINCIPLE & EQUATIONS:</b>"
        "<ul>"
        "<li><b>Producing Ability:</b> The permanent capacity of an animal for repeated production traits (milk yield, fleece weight, litter size), comprising genetic value (additive + non-additive) and permanent environmental effects: <code>PA = G + E_p</code>.</li>"
        "<li><b>Repeatability Weighting Factor (b):</b><br>"
        "<code>b = (n &times; r) / [ 1 + (n - 1) &times; r ]</code><br>"
        "Where <code>n</code> = number of records completed by the animal; <code>r</code> = repeatability of the trait.<br>"
        "As <code>n</code> increases, <code>b</code> increases asymptotically toward 1.0.</li>"
        "<li><b>Most Probable Producing Ability (MPPA):</b><br>"
        "<code>MPPA = \\bar{H} + b &times; (\\bar{X} - \\bar{H})</code><br>"
        "Where <code>\\bar{H}</code> = Herd average; <code>\\bar{X}</code> = Individual cow's average performance over <code>n</code> lactations.</li>"
        "<li><b>Estimated Producing Ability (EPA / Realized Deviation):</b><br>"
        "<code>EPA = b &times; (\\bar{X} - \\bar{H}) = MPPA - \\bar{H}</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM:</b><br>"
        "In an organized Murrah buffalo herd, average 305-day milk yield is <b>2,200 kg</b>. Repeatability of milk yield is <b>r = 0.40</b>. "
        "Three cows have completed the following lactation records:<br>"
        "&bull; <b>Cow A (1 lactation):</b> 2,800 kg.<br>"
        "&bull; <b>Cow B (3 lactations):</b> Average = 2,600 kg (2,500, 2,700, 2,600).<br>"
        "&bull; <b>Cow C (5 lactations):</b> Average = 2,500 kg.<br>"
        "Calculate the MPPA for each cow and rank them for culling/retention in the herd.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><b>For Cow A (n = 1, \\bar{X} = 2,800 kg):</b><br>"
        "<code>b_A = (1 &times; 0.40) / [ 1 + (0)(0.40) ] = 0.40 / 1.0 = 0.400</code>.<br>"
        "<code>MPPA_A = 2,200 + 0.400 &times; (2,800 - 2,200) = 2,200 + 0.400(600) = 2,200 + 240 = 2,440 kg</code>.</li>"
        "<li><b>For Cow B (n = 3, \\bar{X} = 2,600 kg):</b><br>"
        "<code>b_B = (3 &times; 0.40) / [ 1 + (3 - 1)(0.40) ] = 1.20 / [ 1 + 0.80 ] = 1.20 / 1.80 = 0.667</code>.<br>"
        "<code>MPPA_B = 2,200 + 0.667 &times; (2,600 - 2,200) = 2,200 + 0.667(400) = 2,200 + 266.8 = 2,466.8 kg</code>.</li>"
        "<li><b>For Cow C (n = 5, \\bar{X} = 2,500 kg):</b><br>"
        "<code>b_C = (5 &times; 0.40) / [ 1 + (5 - 1)(0.40) ] = 2.00 / [ 1 + 1.60 ] = 2.00 / 2.60 = 0.769</code>.<br>"
        "<code>MPPA_C = 2,200 + 0.769 &times; (2,500 - 2,200) = 2,200 + 0.769(300) = 2,200 + 230.7 = 2,430.7 kg</code>.</li>"
        "<li><b>Ranking:</b>"
        "<br>&bull; <b>Rank 1:</b> <b>Cow B (MPPA = 2,466.8 kg)</b> &rarr; Best expected future producer!"
        "<br>&bull; <b>Rank 2:</b> <b>Cow A (MPPA = 2,440.0 kg)</b>"
        "<br>&bull; <b>Rank 3:</b> <b>Cow C (MPPA = 2,430.7 kg)</b></li>"
        "<li><b>Inference:</b> Notice that even though Cow A had the highest single raw record (2,800 kg), <b>Cow B has a higher MPPA (2,466.8 kg)</b> because Cow B's performance is backed by 3 consistent records, providing much higher statistical reliability (b = 0.667 vs 0.400).</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What is the biological difference between Breeding Value (EBV) and Producing Ability (MPPA)?</b><br>"
        "<b>A:</b> EBV reflects only additive genetic effects transmissible to offspring (<code>h&sup2;</code>); MPPA reflects the animal's own future production, incorporating <b>all genetic effects (additive + dominance + epistasis) plus permanent environment</b> (<code>r</code>).</li>"
        "<li><b>Q: Why does MPPA regress individual averages toward the herd mean?</b><br>"
        "<b>A:</b> To strip away temporary environmental noise (<code>E_t</code>) such as a lucky season or exceptional lush pasture during that specific lactation.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Formula for gain in accuracy with multiple records: <code>Accuracy = &radic;[ n r / (1 + (n-1)r) ]</code>. Point out that the greatest marginal gain in accuracy occurs between record 1 and record 2; after 4 records, additional records provide negligible extra accuracy.</li>"
        "</ul>"
    ),
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
            "headers": ["No. of Completed Records (n)", "Numerator (n * r)", "Denominator [1 + (n-1)r]", "Weighting Factor b", "Correlation with True Producing Ability"],
            "rows": [
                ["1", "0.40", "1.00", "0.400", "0.632"],
                ["2", "0.80", "1.40", "0.571", "0.756"],
                ["3", "1.20", "1.80", "0.667", "0.816"],
                ["4", "1.60", "2.20", "0.727", "0.853"],
                ["5", "2.00", "2.60", "0.769", "0.877"],
                ["10", "4.00", "4.60", "0.870", "0.933"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In commercial Murrah buffalo dairy operations, farm managers must make annual culling decisions. "
        "Culling strictly on first-lactation raw milk yield often eliminates genetically superior cows that suffered temporary mastitis or lameness. "
        "Veterinarians compute <b>MPPA after the second lactation</b>, preventing premature culling of valuable foundation breeding stock."
    ),
    "tags": ["Animal Breeding Lab", "MPPA", "EPA", "Repeatability", "Culling", "Murrah Buffalo", "Producing Ability", "Lactation Records"]
}

topics["p3-t04"] = {
    "summary": "Computation of Wright's Inbreeding Coefficient (Fx) and Coefficient of Relationship (Rxy) from directed pedigree charts and arrow diagrams.",
    "desc": (
        "<b>AIM:</b> To convert a livestock pedigree chart into a directed arrow diagram, trace ancestral connecting paths, and calculate the Inbreeding Coefficient (F_X) and Relationship (R_XY).<br><br>"
        "<b>WRIGHT'S PATH COEFFICIENT FORMULAS:</b>"
        "<ul>"
        "<li><b>Inbreeding Coefficient of Individual X (F_X):</b><br>"
        "<code>F_X = &Sigma; [ (1/2)^{n_1 + n_2 + 1} &times; (1 + F_A) ]</code><br>"
        "Where: <code>A</code> = Common ancestor shared by Sire (S) and Dam (D); <code>n_1</code> = generations from Sire to A; <code>n_2</code> = generations from Dam to A; <code>F_A</code> = inbreeding of ancestor A.</li>"
        "<li><b>Coefficient of Relationship between X and Y (R_XY):</b><br>"
        "<code>R_XY = &Sigma; [ (1/2)^{n_1 + n_2} &times; (1 + F_A) ] / &radic;[ (1 + F_X)(1 + F_Y) ]</code></li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (SIRE &times; DAUGHTER MATING):</b><br>"
        "A dairy bull 'S' is mated to his own daughter 'D' (where D was produced by mating S to an unrelated cow M). "
        "Individual 'X' is born from this mating (S &times; D). Calculate the inbreeding coefficient F_X.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><b>Identify Parents of X:</b> Sire = <code>S</code>, Dam = <code>D</code>.</li>"
        "<li><b>Identify Common Ancestor:</b> Bull <code>S</code> is the sire of X and also the sire of dam D. Hence, <code>A = S</code>.</li>"
        "<li><b>Trace Path:</b> <code>S &larr; (n1=0) &mdash; S &mdash; (n2=1) &rarr; D</code>.</li>"
        "<li><code>n_1 = 0</code> (S is the common ancestor itself); <code>n_2 = 1</code> (from D back to S).</li>"
        "<li>Assume bull S is not inbred (<code>F_S = 0</code>).</li>"
        "<li><b>Compute F_X:</b><br>"
        "<code>F_X = (1/2)^{0 + 1 + 1} &times; (1 + 0) = (1/2)&sup2; = 1/4 = 0.25 (25.0%)</code>.</li>"
        "<li><b>Result:</b> <b>F_X = 0.25 (25%)</b>.</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM 2 (FULL-SIB MATING):</b><br>"
        "Individual 'X' is born from the mating of a full brother (B) and full sister (S), who share both Sire (P) and Dam (M). "
        "Assuming P and M are unrelated and non-inbred, calculate F_X.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li>Parents of X: Sire = B, Dam = S.</li>"
        "<li><b>Two Common Ancestors:</b> Sire <code>P</code> and Dam <code>M</code>.</li>"
        "<li><b>Path 1 (through Common Ancestor P):</b><br>"
        "<code>B &larr; P &rarr; S</code> &rarr; <code>n_1 = 1, n_2 = 1</code>.<br>"
        "Contribution 1 = <code>(1/2)^{1 + 1 + 1} &times; (1 + 0) = (1/2)&sup3; = 1/8 = 0.125</code>.</li>"
        "<li><b>Path 2 (through Common Ancestor M):</b><br>"
        "<code>B &larr; M &rarr; S</code> &rarr; <code>n_1 = 1, n_2 = 1</code>.<br>"
        "Contribution 2 = <code>(1/2)^{1 + 1 + 1} &times; (1 + 0) = (1/2)&sup3; = 1/8 = 0.125</code>.</li>"
        "<li><b>Sum Across All Paths:</b><br>"
        "<code>F_X = 1/8 + 1/8 = 2/8 = 1/4 = 0.25 (25.0%)</code>.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: What are the three strict rules for tracing paths in an arrow diagram?</b><br>"
        "<b>A:</b> (1) A path must go backward to a common ancestor and forward to the other parent (never forward then backward), (2) A path cannot pass through any individual more than once, and (3) A path cannot pass through any individual who is not an ancestor of both parents.</li>"
        "<li><b>Q: What is the relationship (R_XY) between full sibs vs half sibs?</b><br>"
        "<b>A:</b> Full sibs: <code>R = 0.50 (50%)</code>; Half sibs: <code>R = 0.25 (25%)</code>.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Inbreeding of Common Ancestor: If the common ancestor A is itself inbred (e.g. <code>F_A = 0.125</code>), never forget to multiply by <code>(1 + F_A) = 1.125</code>! Forgetting this is a guaranteed penalty in exam problems.</li>"
        "<li>Relationship between Mates equals twice the inbreeding of their progeny: <code>F_X = (1/2) R_{SD} &times; &radic;[(1 + F_S)(1 + F_D)]</code>.</li>"
        "</ul>"
    ),
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
            "headers": ["Mating Relationship Type", "Common Ancestors (A)", "Connecting Path", "Generations (n1, n2)", "Formula Contribution", "Resulting Progeny Inbreeding (F_X)"],
            "rows": [
                ["Sire &times; Daughter", "Sire (S)", "S &larr; S &rarr; D", "n1=0, n2=1", "(1/2)^{0+1+1}", "0.2500 (25.0%)"],
                ["Dam &times; Son", "Dam (D)", "S &larr; D &rarr; D", "n1=1, n2=0", "(1/2)^{1+0+1}", "0.2500 (25.0%)"],
                ["Full Brother &times; Full Sister", "Sire (P) + Dam (M)", "B &larr; P &rarr; S  and  B &larr; M &rarr; S", "n1=1, n2=1 (2 paths)", "2 &times; (1/2)^{1+1+1}", "0.2500 (25.0%)"],
                ["Half Brother &times; Half Sister", "Common Sire (S)", "B &larr; S &rarr; S", "n1=1, n2=1 (1 path)", "1 &times; (1/2)^{1+1+1}", "0.1250 (12.5%)"],
                ["Grandparent &times; Grandchild", "Grandparent (G)", "S &larr; G &rarr; P &rarr; D", "n1=0, n2=2", "(1/2)^{0+2+1}", "0.1250 (12.5%)"],
                ["First Cousins", "Grandparents (G1, G2)", "S &larr; P1 &larr; G &rarr; P2 &rarr; D", "n1=2, n2=2 (2 paths)", "2 &times; (1/2)^{2+2+1}", "0.0625 (6.25%)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "Veterinarians conducting clinical evaluations of litters presented with multiple congenital abnormalities "
        "(e.g., cleft palate, umbilical hernias, or cryptorchidism in dogs) draw a 4-generation arrow diagram. "
        "Calculating <code>F_X &ge; 0.25</code> diagnoses <b>Inbreeding Depression unmasking deleterious recessives</b>, "
        "justifying immediate clinical advice to retire the bitch from breeding or introduce an unrelated stud dog."
    ),
    "tags": ["Animal Breeding Lab", "Inbreeding", "Wright's Formula", "Path Coefficients", "Arrow Diagram", "Coefficient of Relationship", "Full-Sibs"]
}

topics["p3-t05"] = {
    "summary": "Estimation of Mid-Parent Heterosis, Heterobeltiosis, and retained heterosis percentage in rotational crossbreeding and composite livestock breeds.",
    "desc": (
        "<b>AIM:</b> To estimate absolute and percentage heterosis (Mid-Parent Heterosis and Better-Parent Heterosis) and calculate retained heterosis in composite breeds.<br><br>"
        "<b>CORE HETEROSIS EQUATIONS:</b>"
        "<ul>"
        "<li><b>1. Mid-Parent Heterosis (H):</b><br>"
        "<code>H = \\bar{F}_1 - \\bar{MP} = \\bar{F}_1 - [ (\\bar{P}_1 + \\bar{P}_2) / 2 ]</code></li>"
        "<li><b>2. Percentage Heterosis (H%):</b><br>"
        "<code>H% = [ (\\bar{F}_1 - \\bar{MP}) / \\bar{MP} ] &times; 100</code></li>"
        "<li><b>3. Better-Parent Heterosis (Heterobeltiosis):</b><br>"
        "<code>Heterobeltiosis% = [ (\\bar{F}_1 - \\bar{BP}) / \\bar{BP} ] &times; 100</code><br>"
        "Where <code>\\bar{BP}</code> is the mean of the superior purebred parental breed.</li>"
        "<li><b>4. Retained Heterosis in Rotational Crosses (RH%):</b><br>"
        "<code>RH% = [ (2^n - 2) / (2^n - 1) ] &times; 100</code> (where n = number of breeds in rotation).</li>"
        "<li><b>5. Retained Heterosis in Composite / Synthetic Breeds (RH%):</b><br>"
        "<code>RH% = [ 1 - &Sigma; (p_i)&sup2; ] &times; 100</code> (where p_i = fractional inheritance of breed i).</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (HETEROSIS CALCULATION):</b><br>"
        "In a dairy crossbreeding experiment, purebred Holstein-Friesian (HF) cows averaged <b>4,500 kg</b> 305-day milk yield, "
        "and purebred Gir cows averaged <b>2,500 kg</b>. The F1 crossbred cows (HF &times; Gir) produced an average of <b>3,850 kg</b>.<br>"
        "1. Calculate Mid-Parent Value (MP).<br>"
        "2. Calculate absolute heterosis (H) and percentage heterosis (H%).<br>"
        "3. Did the F1 cross show heterobeltiosis?<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><code>\\bar{P}_1 (HF) = 4,500 kg</code>; <code>\\bar{P}_2 (Gir) = 2,500 kg</code>.</li>"
        "<li><code>Mid-Parent (MP) = (4,500 + 2,500) / 2 = 7,000 / 2 = 3,500 kg</code>.</li>"
        "<li><code>Absolute Heterosis H = \\bar{F}_1 - MP = 3,850 - 3,500 = +350 kg</code>.</li>"
        "<li><code>Percentage Heterosis H% = (350 / 3,500) &times; 100 = +10.0%</code>.</li>"
        "<li><b>Heterobeltiosis Check:</b><br>"
        "Better Parent <code>BP = 4,500 kg</code> (HF).<br>"
        "<code>F1 (3,850 kg) &lt; BP (4,500 kg)</code>.<br>"
        "<code>Heterobeltiosis = [ (3,850 - 4,500) / 4,500 ] &times; 100 = -14.44%</code>.<br>"
        "<b>Inference:</b> The F1 cross exhibited <b>10.0% standard mid-parent heterosis</b>, but did NOT show heterobeltiosis because its milk yield was below the cold-climate purebred HF under European conditions. However, under tropical heat, F1 excels due to disease resilience!</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM 2 (RETAINED HETEROSIS IN SYNTHETIC BREEDS):</b><br>"
        "Calculate the retained heterosis in:<br>"
        "1. <b>Karan Fries</b> (50% HF + 50% Tharparkar).<br>"
        "2. <b>Avishaan Sheep</b> (1/2 Malpura + 1/4 Garole + 1/4 Patanwadi).<br>"
        "<b>Solution:</b><br>"
        "<ol>"
        "<li><b>Karan Fries:</b> <code>RH% = [ 1 - (0.50&sup2; + 0.50&sup2;) ] &times; 100 = [ 1 - (0.25 + 0.25) ] &times; 100 = [ 1 - 0.50 ] &times; 100 = 50.0%</code>.</li>"
        "<li><b>Avishaan Sheep:</b> <code>RH% = [ 1 - (0.50&sup2; + 0.25&sup2; + 0.25&sup2;) ] &times; 100 = [ 1 - (0.25 + 0.0625 + 0.0625) ] &times; 100 = [ 1 - 0.375 ] &times; 100 = 62.5%</code>.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Which traits express the highest percentage heterosis in livestock?</b><br>"
        "<b>A:</b> <b>Fitness, reproductive, and early survival traits</b> (e.g., conception rate, embryo livability, litter size in pigs) exhibit highest heterosis (15–25%), whereas carcass and skeletal traits exhibit lowest (< 5%).</li>"
        "<li><b>Q: What is F2 breakdown (Recombination Loss)?</b><br>"
        "<b>A:</b> When F1 crossbreds are mated inter-se (F1 &times; F1), 50% of individual heterosis is lost due to segregation, and favorable epistatic gene complexes are disrupted by crossing over.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Formula for Retained Heterosis in 2-breed Crisscrossing at equilibrium: <code>RH = 2/3 = 66.67%</code>; in 3-breed rotation: <code>RH = 6/7 = 85.71%</code>. Stating equilibrium formulas without deriving long cycles scores instant full marks!</li>"
        "</ul>"
    ),
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
            "headers": ["Crossbreeding System", "Parental Composition", "Equilibrium Retained Heterosis (RH%)", "Need for Purebred Sires", "Primary Field Application"],
            "rows": [
                ["Two-Breed Terminal", "Breed A sire &times; Breed B dam", "100.0% (in F1 progeny)", "Yes (maintain both pure breeds)", "Commercial broiler and beef production"],
                ["Two-Breed Rotation (Crisscrossing)", "Alternating Breeds A and B", "66.7% (2/3 of maximum)", "Yes (requires 2 pure breeds perpetually)", "Commercial swine and sheep production"],
                ["Three-Breed Rotation", "Alternating Breeds A, B, and C", "85.7% (6/7 of maximum)", "Yes (requires 3 pure breeds)", "Commercial swine maternal lines"],
                ["2-Breed Composite (50:50)", "Karan Fries (1/2 HF + 1/2 Tharparkar)", "50.0% (permanently fixed)", "No (mates composite to composite)", "Stabilized tropical dairy cattle"],
                ["3-Breed Composite (50:25:25)", "Avishaan (1/2 Malpura + 1/4 Garole + 1/4 Patanwadi)", "62.5% (permanently fixed)", "No (self-contained composite flock)", "Prolific mutton sheep in Rajasthan"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In commercial broiler and layer operations, farmers purchasing day-old commercial chicks sometimes attempt to save costs "
        "by collecting eggs from commercial hybrid hens and incubating them on-farm. "
        "Veterinarians explain the genetic reality of <b>F2 Breakdown</b>: "
        "inter-se mating of commercial four-way crosses shatters heterosis, causing a <b>30% drop in egg production and extreme flock variability</b>, "
        "proving that hybrid chicks must be procured fresh every generation from primary breeding hatcheries."
    ),
    "tags": ["Animal Breeding Lab", "Heterosis", "Hybrid Vigour", "Heterobeltiosis", "Retained Heterosis", "Karan Fries", "Avishaan", "F2 Breakdown"]
}

topics["p3-t06"] = {
    "summary": "Computation of historical sire evaluation indices (Daughter Average, Mount Hope, Contemporary Comparison) and mathematical construction of multi-trait selection indexes.",
    "desc": (
        "<b>AIM:</b> To calculate classical sire indices (Daughter Average, Intermediate/Mount Hope, and Contemporary Comparison) and solve simultaneous equations to construct a multi-trait Selection Index.<br><br>"
        "<b>CORE SIRE EVALUATION & SELECTION INDEX EQUATIONS:</b>"
        "<ul>"
        "<li><b>1. Simple Daughter Average:</b> <code>I = \\bar{D}</code>.</li>"
        "<li><b>2. Intermediate Index (Hansson-Yapp / Mount Hope Index):</b><br>"
        "<code>I = 2\\bar{D} - \\bar{M}</code> (where <code>\\bar{D}</code> = Daughter average; <code>\\bar{M}</code> = Dam average).</li>"
        "<li><b>3. Rice's Index:</b> <code>I = 2\\bar{D} - \\bar{H}</code> (where <code>\\bar{H}</code> = Herd average).</li>"
        "<li><b>4. Contemporary Comparison (Robertson and Rendel):</b><br>"
        "<code>I = \\bar{A} + [ n / (n + 12) ] &times; (\\bar{D} - \\bar{C})</code><br>"
        "Where <code>\\bar{A}</code> = Breed average; <code>n</code> = number of daughters; <code>\\bar{D}</code> = daughter average; <code>\\bar{C}</code> = contemporary average.</li>"
        "<li><b>5. Hazel's Multi-Trait Selection Index (1943):</b><br>"
        "Index: <code>I = b_1 X_1 + b_2 X_2 + ... + b_m X_m</code><br>"
        "Aggregate Economic Genotype: <code>H = a_1 G_1 + a_2 G_2 + ... + a_m G_m</code> (where a_i = relative economic values).<br>"
        "Matrix Equation to solve weighting coefficients <code>b</code>:<br>"
        "<code>[ P ] [ b ] = [ G ] [ a ]  &rarr;  [ b ] = [ P ]⁻¹ [ G ] [ a ]</code><br>"
        "For Two Traits:<br>"
        "<code>b_1 P_{11} + b_2 P_{12} = a_1 G_{11} + a_2 G_{12}</code><br>"
        "<code>b_1 P_{21} + b_2 P_{22} = a_1 G_{21} + a_2 G_{22}</code>.</li>"
        "</ul><br>"
        "<b>MODEL EXAM PROBLEM 1 (SIRE INDICES):</b><br>"
        "A dairy bull was mated to cows averaging <b>3,000 kg</b> milk. His 20 daughters produced an average of <b>3,400 kg</b> in a herd where contemporaries averaged <b>3,100 kg</b>. "
        "Assume breed average <code>\\bar{A} = 3,000 kg</code>.<br>"
        "Calculate the sire's index using: (1) Daughter Average, (2) Mount Hope Index, (3) Contemporary Comparison.<br><br>"
        "<b>STEP-BY-STEP CALCULATION:</b>"
        "<ol>"
        "<li><b>Daughter Average:</b> <code>I = \\bar{D} = 3,400 kg</code>.</li>"
        "<li><b>Mount Hope Index:</b><br>"
        "<code>I = 2\\bar{D} - \\bar{M} = 2(3,400) - 3,000 = 6,800 - 3,000 = 3,800 kg</code>.</li>"
        "<li><b>Contemporary Comparison (CC):</b><br>"
        "<code>Weighting Factor = n / (n + 12) = 20 / (20 + 12) = 20 / 32 = 0.625</code>.<br>"
        "<code>Daughter - Contemporary = 3,400 - 3,100 = +300 kg</code>.<br>"
        "<code>I = 3,000 + 0.625 &times; (300) = 3,000 + 187.5 = 3,187.5 kg</code>.</li>"
        "</ol><br>"
        "<b>MODEL EXAM PROBLEM 2 (TWO-TRAIT SELECTION INDEX):</b><br>"
        "Construct a selection index combining Milk Yield (X1 in 100 kg) and Age at First Calving (X2 in months). "
        "Given phenotypic variances <code>P11 = 16, P22 = 25</code>, covariance <code>P12 = -4</code>; "
        "genetic variances <code>G11 = 4, G22 = 5</code>, genetic covariance <code>G12 = -2</code>; "
        "and relative economic values <code>a1 = +10, a2 = -5</code>.<br>"
        "<b>Simultaneous Equations:</b><br>"
        "<ol>"
        "<li><code>RHS_1 = a1(G11) + a2(G12) = 10(4) + (-5)(-2) = 40 + 10 = 50</code>.</li>"
        "<li><code>RHS_2 = a1(G21) + a2(G22) = 10(-2) + (-5)(5) = -20 - 25 = -45</code>.</li>"
        "<li>Equations:<br>"
        "<code>16 b_1 - 4 b_2 = 50</code> &nbsp; &rarr; &nbsp; (Eq. 1)<br>"
        "<code>-4 b_1 + 25 b_2 = -45</code> &nbsp; &rarr; &nbsp; (Eq. 2)</li>"
        "<li>Multiply Eq. 2 by 4: <code>-16 b_1 + 100 b_2 = -180</code>.</li>"
        "<li>Add to Eq. 1: <code>96 b_2 = -130  &rarr;  b_2 = -130 / 96 = -1.354</code>.</li>"
        "<li>Substitute in Eq. 1: <code>16 b_1 = 50 + 4(-1.354) = 50 - 5.416 = 44.584  &rarr;  b_1 = 44.584 / 16 = 2.787</code>.</li>"
        "<li><b>Selection Index:</b> <code>I = 2.787 &times; X_1 - 1.354 &times; X_2</code>.</li>"
        "</ol><br>"
        "<b>VIVA-VOCE QUESTIONS & ANSWERS:</b>"
        "<ol>"
        "<li><b>Q: Why is the Mount Hope Index often biased upwards?</b><br>"
        "<b>A:</b> It assumes dam and daughter environments are identical; in improving herds, daughters receive better feed and housing, falsely crediting environmental progress to the sire's breeding value.</li>"
        "<li><b>Q: What is the primary advantage of Hazel's Selection Index over Independent Culling Levels?</b><br>"
        "<b>A:</b> Hazel's index allows <b>superiority in one trait to compensate for a minor deficiency in another trait</b>, maximizing overall aggregate economic progress.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>EXAMINER'S SCORING TIPS & SHORTCUTS</b><br>"
        "<ul>"
        "<li>Notice the sign of the economic weights: Milk yield has positive economic value (<code>a1 = +10</code>), while age at first calving has negative economic value (<code>a2 = -5</code>, because late calving costs money). Setting the right economic sign is vital!</li>"
        "<li>Contemporary Comparison weighting factor constant: The constant <b>12</b> represents <code>(4 - h&sup2;) / h&sup2;</code> when heritability is approximately <code>0.25</code>! Showing this derivation proves 10/10 knowledge.</li>"
        "</ul>"
    ),
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
            "headers": ["Sire Index", "Formula", "Adjusts for Dams' Merit?", "Adjusts for Herd Environment?", "Major Bias / Limitation"],
            "rows": [
                ["Daughter Average", "I = D̄", "No", "No", "Heavily biased by herd feeding and management level"],
                ["Mount Hope (Intermediate)", "I = 2D̄ - M̄", "Yes (subtracts dam mean)", "No", "Biased upward by secular environmental progress over time"],
                ["Rice's Index", "I = 2D̄ - H̄", "No (uses herd average)", "Partially", "Assumes dams represent the exact herd average"],
                ["Contemporary Comparison", "I = Ā + [n/(n+12)]*(D̄ - C̄)", "Partially", "Yes (compares with herdmates)", "Fails to adjust for genetic merit of contemporary mates"],
                ["Animal Model BLUP", "y = Xβ + Zu + e", "Yes (complete pedigree)", "Yes (Generalized Least Squares)", "Gold standard; requires nationwide computerized database"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY FIELD APPLICATION:</b> "
        "In commercial poultry breeding organizations, geneticists construct a <b>Four-Trait Selection Index</b>: "
        "<code>I = b1(Egg Production to 40 weeks) + b2(Egg Weight) - b3(Age at First Egg) - b4(Feed Conversion Ratio)</code>. "
        "Veterinarians and breeding managers rank candidate roosters and hens on this total score, "
        "producing balanced commercial layer chicks that lay large eggs early without consuming excessive feed."
    ),
    "tags": ["Animal Breeding Lab", "Sire Index", "Mount Hope", "Contemporary Comparison", "Selection Index", "Hazel", "Economic Weight", "BLUP"]
}
