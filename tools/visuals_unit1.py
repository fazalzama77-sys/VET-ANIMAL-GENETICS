# -*- coding: utf-8 -*-
"""
tools/visuals_unit1.py
SVG visual definitions for all 22 topics of Unit 1 (Biostatistics).
"""

from build_all_visuals import make_svg_plate

UNIT_1_VISUALS = {}

# u1-t01: Introduction and Importance of Statistics and Biostatistics
UNIT_1_VISUALS["u1-t01"] = {
    "caption": "Foundations of Biometry: From Biological Variation to Genetic Inference and Breeding Values (Sir R.A. Fisher Framework)",
    "svg": make_svg_plate(
        "u1-t01", "UNIT 1 · BIOSTATISTICS", "Foundations of Biometry & Biological Variation",
        "Sir Ronald A. Fisher's Paradigm: From Multifactorial Phenotypic Variance to Genetic Prediction",
        '''
        <!-- 3 Pillars Grid -->
        <g transform="translate(10, 15)">
          <!-- Box 1 -->
          <rect width="230" height="300" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
          <rect width="230" height="36" rx="10" fill="url(#tealGrad)" />
          <text x="115" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. BIOLOGICAL PHENOMENA</text>
          <text x="20" y="65" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">• Inherent Variation</text>
          <text x="30" y="85" fill="#94a3b8" font-family="sans-serif" font-size="11">Even clones/twins differ</text>
          <text x="20" y="115" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">• Multifactorial Causation</text>
          <text x="30" y="135" fill="#94a3b8" font-family="sans-serif" font-size="11">Genes + Feed + Climate</text>
          <text x="20" y="165" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">• Aggregate of Facts</text>
          <text x="30" y="185" fill="#94a3b8" font-family="sans-serif" font-size="11">Deals with herd data, not</text>
          <text x="30" y="200" fill="#94a3b8" font-family="sans-serif" font-size="11">isolated individuals</text>
          <rect x="20" y="230" width="190" height="48" rx="6" fill="#0f172a" stroke="#0d9488" stroke-width="1" />
          <text x="115" y="250" fill="#2dd4bf" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">Phenotypic Variance</text>
          <text x="115" y="268" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">V_P = V_G + V_E</text>
        </g>

        <!-- Arrow 1 -->
        <path d="M 252 165 L 268 165" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)" />

        <!-- Box 2 -->
        <g transform="translate(260, 15)">
          <rect width="230" height="300" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
          <rect width="230" height="36" rx="10" fill="url(#indigoGrad)" />
          <text x="115" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. BIOSTATISTICAL TOOLS</text>
          <text x="20" y="65" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">• Parameter Estimation</text>
          <text x="30" y="85" fill="#94a3b8" font-family="sans-serif" font-size="11">Mean (μ), Variance (σ²)</text>
          <text x="20" y="115" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">• Hypothesis Testing</text>
          <text x="30" y="135" fill="#94a3b8" font-family="sans-serif" font-size="11">Z-test, t-test, ANOVA</text>
          <text x="20" y="165" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">• Genetic Correlation</text>
          <text x="30" y="185" fill="#94a3b8" font-family="sans-serif" font-size="11">r_G across economic traits</text>
          <rect x="20" y="230" width="190" height="48" rx="6" fill="#0f172a" stroke="#6366f1" stroke-width="1" />
          <text x="115" y="250" fill="#a5b4fc" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">Heritability Partitioning</text>
          <text x="115" y="268" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">h² = V_A / V_P</text>
        </g>

        <!-- Arrow 2 -->
        <path d="M 502 165 L 518 165" stroke="#38bdf8" stroke-width="3" />

        <!-- Box 3 -->
        <g transform="translate(510, 15)">
          <rect width="232" height="300" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
          <rect width="232" height="36" rx="10" fill="url(#amberGrad)" />
          <text x="116" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. VETERINARY DECISIONS</text>
          <text x="20" y="65" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">• Sire Proof &amp; BLUP</text>
          <text x="30" y="85" fill="#94a3b8" font-family="sans-serif" font-size="11">Estimated Breeding Values</text>
          <text x="20" y="115" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">• Clinical Drug Efficacy</text>
          <text x="30" y="135" fill="#94a3b8" font-family="sans-serif" font-size="11">P-value &lt; 0.05 vs Control</text>
          <text x="20" y="165" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">• Breed Improvement</text>
          <text x="30" y="185" fill="#94a3b8" font-family="sans-serif" font-size="11">Selection Response (ΔG)</text>
          <rect x="20" y="230" width="192" height="48" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1" />
          <text x="116" y="250" fill="#fde047" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">Expected Genetic Gain</text>
          <text x="116" y="268" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">ΔG = (i · r_TI · σ_A) / L</text>
        </g>
        ''',
        "Sir Francis Galton coined 'Biometry'; Sir R.A. Fisher established modern Biostatistics & ANOVA for quantitative genetic selection."
    )
}

# u1-t02: Classification and Tabulation
UNIT_1_VISUALS["u1-t02"] = {
    "caption": "Classification Framework & Anatomy of a Formal Statistical Table (Stub, Caption, Body, and Headnote)",
    "svg": make_svg_plate(
        "u1-t02", "UNIT 1 · BIOSTATISTICS", "Data Classification & Statistical Table Structure",
        "Systematic Organization of Raw Biological Records into Tabular Matrices",
        '''
        <!-- Left: Classification Bases -->
        <g transform="translate(10, 15)">
          <rect width="320" height="300" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
          <rect width="320" height="34" rx="10" fill="url(#tealGrad)" />
          <text x="160" y="22" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">4 BASES OF DATA CLASSIFICATION</text>
          
          <rect x="15" y="48" width="290" height="52" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="25" y="68" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">1. Geographical (Spatial):</text>
          <text x="25" y="86" fill="#94a3b8" font-family="sans-serif" font-size="11">By regions/states (e.g., Sahiwal in Punjab vs Haryana)</text>

          <rect x="15" y="110" width="290" height="52" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="25" y="130" fill="#a78bfa" font-family="sans-serif" font-size="11" font-weight="700">2. Chronological (Temporal):</text>
          <text x="25" y="148" fill="#94a3b8" font-family="sans-serif" font-size="11">By time intervals (e.g., Annual milk records 2015-2025)</text>

          <rect x="15" y="172" width="290" height="52" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="25" y="192" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700">3. Qualitative (Attribute):</text>
          <text x="25" y="210" fill="#94a3b8" font-family="sans-serif" font-size="11">Descriptive traits (e.g., Polled vs Horned, Healthy vs Sick)</text>

          <rect x="15" y="234" width="290" height="52" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="25" y="254" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700">4. Quantitative (Metric):</text>
          <text x="25" y="272" fill="#94a3b8" font-family="sans-serif" font-size="11">Continuous measurements (e.g., Milk kg: 10-20, 20-30)</text>
        </g>

        <!-- Right: Table Anatomy -->
        <g transform="translate(350, 15)">
          <rect width="392" height="300" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
          <rect width="392" height="34" rx="10" fill="url(#indigoGrad)" />
          <text x="196" y="22" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">ANATOMY OF A STATISTICAL TABLE</text>
          
          <!-- Mock Table -->
          <g transform="translate(16, 48)">
            <text x="180" y="15" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">Table 1: 305-Day Milk Yield Across Breeds [TITLE]</text>
            <text x="180" y="30" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">(Values in Liters ± Standard Error) [HEADNOTE]</text>
            
            <rect y="38" width="360" height="150" fill="#0f172a" stroke="#475569" />
            <!-- Header row -->
            <rect y="38" width="120" height="30" fill="#334155" stroke="#475569" />
            <text x="60" y="58" fill="#e2e8f0" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">BREED [STUB HEAD]</text>

            <rect x="120" y="38" width="240" height="30" fill="#1e293b" stroke="#475569" />
            <text x="240" y="58" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">PARITY RECORDINGS [CAPTION]</text>

            <!-- Data Rows -->
            <rect y="68" width="120" height="40" fill="#1e293b" stroke="#475569" />
            <text x="15" y="93" fill="#cbd5e1" font-family="sans-serif" font-size="11">Sahiwal [STUB]</text>

            <rect x="120" y="68" width="240" height="40" fill="#0f172a" stroke="#475569" />
            <text x="240" y="93" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="600" text-anchor="middle">2,450 ± 85 L [BODY CELL]</text>

            <rect y="108" width="120" height="40" fill="#1e293b" stroke="#475569" />
            <text x="15" y="133" fill="#cbd5e1" font-family="sans-serif" font-size="11">Murrah [STUB]</text>

            <rect x="120" y="108" width="240" height="40" fill="#0f172a" stroke="#475569" />
            <text x="240" y="133" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="600" text-anchor="middle">2,890 ± 110 L [BODY CELL]</text>

            <rect y="148" width="360" height="40" fill="#1e293b" stroke="#475569" />
            <text x="10" y="165" fill="#94a3b8" font-family="sans-serif" font-size="9">* Recorded under ICAR Network Project [FOOTNOTE]</text>
            <text x="10" y="179" fill="#94a3b8" font-family="sans-serif" font-size="9">Source: Annual Dairy Herd Book, Bareilly [SOURCE NOTE]</text>
          </g>
        </g>
        ''',
        "Sturges' Rule defines optimal classes: k = 1 + 3.322 · log₁₀(N). Exclusive method (10-20, 20-30) is standard for continuous data."
    )
}

# u1-t11: Normal Distribution
UNIT_1_VISUALS["u1-t11"] = {
    "caption": "The Standard Normal Distribution (Gaussian Bell Curve) with Empirical 68-95-99.7 Rule and Z-score Scales",
    "svg": make_svg_plate(
        "u1-t11", "UNIT 1 · BIOSTATISTICS", "Standard Normal Curve & Empirical Rule",
        "Bell-Shaped Symmetrical Gaussian Distribution with Mean = Median = Mode",
        '''
        <g transform="translate(40, 20)">
          <!-- Curve Coordinates Area: W: 672, H: 260 -->
          <!-- Background Zones -->
          <!-- 3 Sigma zone (-3 to 3): x 36 to 636 -->
          <path d="M 36 240 Q 236 240 300 130 Q 336 40 372 40 Q 408 40 444 130 Q 508 240 708 240 Z" fill="#1e293b" opacity="0.5" />
          
          <!-- 2 Sigma Zone (-2 to 2): x 148 to 524 -->
          <path d="M 148 240 Q 250 240 310 130 Q 336 40 372 40 Q 408 40 434 130 Q 494 240 596 240 Z" fill="#0f766e" opacity="0.3" />

          <!-- 1 Sigma Zone (-1 to 1): x 260 to 484 -->
          <path d="M 260 240 Q 315 210 336 120 Q 354 40 372 40 Q 390 40 408 120 Q 429 210 484 240 Z" fill="#0d9488" opacity="0.6" />

          <!-- Main Outline Bell Curve -->
          <path d="M 36 240 C 180 240, 290 220, 336 120 C 354 50, 362 40, 372 40 C 382 40, 390 50, 408 120 C 454 220, 564 240, 708 240" fill="none" stroke="#2dd4bf" stroke-width="3.5" />

          <!-- Base Axis -->
          <line x1="20" y1="240" x2="724" y2="240" stroke="#64748b" stroke-width="2" />

          <!-- Vertical Center Line (Mean) -->
          <line x1="372" y1="40" x2="372" y2="240" stroke="#f8fafc" stroke-width="2" stroke-dasharray="4,4" />
          <text x="372" y="30" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">μ (Mean = Median = Mode)</text>

          <!-- Standard Deviation Markings -->
          <!-- -3s -->
          <line x1="60" y1="235" x2="60" y2="245" stroke="#94a3b8" stroke-width="2" />
          <text x="60" y="260" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">-3σ</text>
          <text x="60" y="275" fill="#64748b" font-family="sans-serif" font-size="10" text-anchor="middle">z = -3</text>

          <!-- -2s -->
          <line x1="164" y1="235" x2="164" y2="245" stroke="#94a3b8" stroke-width="2" />
          <text x="164" y="260" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">-2σ</text>
          <text x="164" y="275" fill="#64748b" font-family="sans-serif" font-size="10" text-anchor="middle">z = -2</text>

          <!-- -1s -->
          <line x1="268" y1="235" x2="268" y2="245" stroke="#2dd4bf" stroke-width="2" />
          <text x="268" y="260" fill="#2dd4bf" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">-1σ</text>
          <text x="268" y="275" fill="#64748b" font-family="sans-serif" font-size="10" text-anchor="middle">z = -1</text>

          <!-- 0 -->
          <line x1="372" y1="235" x2="372" y2="245" stroke="#f8fafc" stroke-width="2" />
          <text x="372" y="260" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">μ (0)</text>
          <text x="372" y="275" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">z = 0</text>

          <!-- +1s -->
          <line x1="476" y1="235" x2="476" y2="245" stroke="#2dd4bf" stroke-width="2" />
          <text x="476" y="260" fill="#2dd4bf" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">+1σ</text>
          <text x="476" y="275" fill="#64748b" font-family="sans-serif" font-size="10" text-anchor="middle">z = +1</text>

          <!-- +2s -->
          <line x1="580" y1="235" x2="580" y2="245" stroke="#94a3b8" stroke-width="2" />
          <text x="580" y="260" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">+2σ</text>
          <text x="580" y="275" fill="#64748b" font-family="sans-serif" font-size="10" text-anchor="middle">z = +2</text>

          <!-- +3s -->
          <line x1="684" y1="235" x2="684" y2="245" stroke="#94a3b8" stroke-width="2" />
          <text x="684" y="260" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">+3σ</text>
          <text x="684" y="275" fill="#64748b" font-family="sans-serif" font-size="10" text-anchor="middle">z = +3</text>

          <!-- Percentage Badges -->
          <rect x="322" y="130" width="100" height="26" rx="6" fill="#0f172a" stroke="#2dd4bf" stroke-width="1.5" />
          <text x="372" y="147" fill="#2dd4bf" font-family="sans-serif" font-size="12" font-weight="800" text-anchor="middle">68.27% (±1σ)</text>

          <rect x="232" y="80" width="100" height="24" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
          <text x="282" y="96" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">95.45% (±2σ)</text>

          <rect x="412" y="80" width="100" height="24" rx="5" fill="#0f172a" stroke="#a78bfa" stroke-width="1" />
          <text x="462" y="96" fill="#a78bfa" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">99.73% (±3σ)</text>

          <!-- Inflection point labels -->
          <circle cx="268" cy="120" r="4" fill="#fbbf24" />
          <circle cx="476" cy="120" r="4" fill="#fbbf24" />
          <text x="235" y="125" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="600">Inflection (x - σ)</text>
          <text x="485" y="125" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="600">Inflection (x + σ)</text>
        </g>
        ''',
        "Normal curve: Skewness β₁ = 0, Kurtosis β₂ = 3. Points of inflection occur exactly at μ ± σ. Area = 1.0."
    )
}

# u1-t12: Correlation
UNIT_1_VISUALS["u1-t12"] = {
    "caption": "Scatter Plot Topologies & Pearson's Correlation Coefficients (r) from Perfect Positive to Non-Linear",
    "svg": make_svg_plate(
        "u1-t12", "UNIT 1 · BIOSTATISTICS", "Scatter Plots & Pearson's Correlation (r)",
        "Measuring Direction and Strength of Linear Association Between Metric Biological Variables",
        '''
        <g transform="translate(10, 15)">
          <!-- Quadrant 1: Perfect Positive -->
          <g transform="translate(15, 10)">
            <rect width="165" height="135" rx="8" fill="#1e293b" stroke="#334155" />
            <text x="82" y="22" fill="#2dd4bf" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">r = +1.0 (Perfect +ve)</text>
            <line x1="20" y1="115" x2="145" y2="115" stroke="#64748b" />
            <line x1="20" y1="115" x2="20" y2="35" stroke="#64748b" />
            <line x1="30" y1="105" x2="135" y2="45" stroke="#2dd4bf" stroke-width="2" stroke-dasharray="3,3" />
            <circle cx="30" cy="105" r="3" fill="#2dd4bf" />
            <circle cx="56" cy="90" r="3" fill="#2dd4bf" />
            <circle cx="82" cy="75" r="3" fill="#2dd4bf" />
            <circle cx="108" cy="60" r="3" fill="#2dd4bf" />
            <circle cx="135" cy="45" r="3" fill="#2dd4bf" />
            <text x="82" y="130" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">e.g., Chest Girth vs Weight</text>
          </g>

          <!-- Quadrant 2: High Negative -->
          <g transform="translate(195, 10)">
            <rect width="165" height="135" rx="8" fill="#1e293b" stroke="#334155" />
            <text x="82" y="22" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">r = -0.85 (High -ve)</text>
            <line x1="20" y1="115" x2="145" y2="115" stroke="#64748b" />
            <line x1="20" y1="115" x2="20" y2="35" stroke="#64748b" />
            <line x1="30" y1="45" x2="135" y2="105" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3" />
            <circle cx="32" cy="48" r="3" fill="#f43f5e" />
            <circle cx="58" cy="65" r="3" fill="#f43f5e" />
            <circle cx="80" cy="70" r="3" fill="#f43f5e" />
            <circle cx="110" cy="92" r="3" fill="#f43f5e" />
            <circle cx="132" cy="102" r="3" fill="#f43f5e" />
            <text x="82" y="130" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">e.g., Milk Yield vs Fat %</text>
          </g>

          <!-- Quadrant 3: Zero Correlation -->
          <g transform="translate(375, 10)">
            <rect width="165" height="135" rx="8" fill="#1e293b" stroke="#334155" />
            <text x="82" y="22" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">r = 0.0 (Zero Linear)</text>
            <line x1="20" y1="115" x2="145" y2="115" stroke="#64748b" />
            <line x1="20" y1="115" x2="20" y2="35" stroke="#64748b" />
            <circle cx="45" cy="50" r="3" fill="#94a3b8" />
            <circle cx="75" cy="85" r="3" fill="#94a3b8" />
            <circle cx="120" cy="55" r="3" fill="#94a3b8" />
            <circle cx="55" cy="95" r="3" fill="#94a3b8" />
            <circle cx="105" cy="100" r="3" fill="#94a3b8" />
            <circle cx="85" cy="65" r="3" fill="#94a3b8" />
            <text x="82" y="130" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">Uncorrelated variables</text>
          </g>

          <!-- Quadrant 4: Curvilinear -->
          <g transform="translate(555, 10)">
            <rect width="165" height="135" rx="8" fill="#1e293b" stroke="#334155" />
            <text x="82" y="22" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">r ≈ 0 (Curvilinear)</text>
            <line x1="20" y1="115" x2="145" y2="115" stroke="#64748b" />
            <line x1="20" y1="115" x2="20" y2="35" stroke="#64748b" />
            <path d="M 30 105 Q 82 40 135 105" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3" />
            <circle cx="32" cy="102" r="3" fill="#fbbf24" />
            <circle cx="55" cy="68" r="3" fill="#fbbf24" />
            <circle cx="82" cy="46" r="3" fill="#fbbf24" />
            <circle cx="110" cy="68" r="3" fill="#fbbf24" />
            <circle cx="132" cy="102" r="3" fill="#fbbf24" />
            <text x="82" y="130" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">r tests linear only!</text>
          </g>

          <!-- Formula & Properties Card -->
          <g transform="translate(15, 160)">
            <rect width="705" height="135" rx="8" fill="#0f172a" stroke="#334155" />
            <text x="25" y="30" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700">MATHEMATICAL FORMULA &amp; PROPERTIES:</text>
            <text x="40" y="60" fill="#f8fafc" font-family="sans-serif" font-size="13">r = Cov(X, Y) / [ σ_X · σ_Y ] = Σ(X - X̄)(Y - Ȳ) / √[ Σ(X - X̄)² · Σ(Y - Ȳ)² ]</text>
            <text x="40" y="85" fill="#94a3b8" font-family="sans-serif" font-size="11">• Range: Strictly bounded between -1.0 and +1.0 (-1 ≤ r ≤ +1). Independent of origin and scale.</text>
            <text x="40" y="105" fill="#94a3b8" font-family="sans-serif" font-size="11">• Geometric Mean of Regression Slopes: r = ±√(b_yx · b_xy). Both slopes share the same sign as r.</text>
          </g>
        </g>
        ''',
        "Correlation coefficient r measures linear association only; r = 0 means absence of linear association, not necessarily independence."
    )
}

# u1-t13: Regression
UNIT_1_VISUALS["u1-t13"] = {
    "caption": "Linear Regression Line of Y on X with Least-Squares Residual Minimization and Slope Parameter (b_yx)",
    "svg": make_svg_plate(
        "u1-t13", "UNIT 1 · BIOSTATISTICS", "Linear Regression & Least Squares Principle",
        "Predicting Dependent Response Variable (Y) from Independent Predictor Variable (X)",
        '''
        <g transform="translate(20, 20)">
          <!-- Graph axes -->
          <line x1="50" y1="260" x2="480" y2="260" stroke="#64748b" stroke-width="2" />
          <line x1="50" y1="260" x2="50" y2="20" stroke="#64748b" stroke-width="2" />
          
          <text x="480" y="275" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="600">X (Independent: Chest Girth cm)</text>
          <text x="45" y="15" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="600" text-anchor="end">Y (Body Weight kg)</text>

          <!-- Regression Line: Y = a + bx -->
          <line x1="70" y1="220" x2="450" y2="45" stroke="#38bdf8" stroke-width="3" />
          <text x="455" y="45" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700">Ŷ = a + bX</text>

          <!-- Intercept 'a' -->
          <circle cx="50" cy="229" r="4" fill="#fbbf24" />
          <text x="25" y="233" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="700">a</text>
          <text x="65" y="235" fill="#fbbf24" font-family="sans-serif" font-size="10">Intercept</text>

          <!-- Data points and Residual Lines -->
          <!-- Point 1 -->
          <circle cx="150" cy="150" r="4" fill="#f43f5e" />
          <line x1="150" y1="150" x2="150" y2="183" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="2,2" />
          <text x="156" y="165" fill="#f43f5e" font-family="sans-serif" font-size="10">e₁ = (Y₁ - Ŷ₁)</text>

          <!-- Point 2 -->
          <circle cx="250" cy="155" r="4" fill="#f43f5e" />
          <line x1="250" y1="155" x2="250" y2="137" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="2,2" />
          <text x="256" y="150" fill="#f43f5e" font-family="sans-serif" font-size="10">e₂</text>

          <!-- Point 3 -->
          <circle cx="340" cy="80" r="4" fill="#f43f5e" />
          <line x1="340" y1="80" x2="340" y2="96" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="2,2" />
          <text x="346" y="90" fill="#f43f5e" font-family="sans-serif" font-size="10">e₃</text>

          <!-- Centroid (X̄, Ȳ) -->
          <circle cx="260" cy="132" r="5" fill="#10b981" />
          <text x="260" y="120" fill="#10b981" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">Centroid (X̄, Ȳ)</text>

          <!-- Right: Equations Box -->
          <g transform="translate(510, 15)">
            <rect width="230" height="260" rx="8" fill="#1e293b" stroke="#334155" />
            <rect width="230" height="32" rx="8" fill="url(#tealGrad)" />
            <text x="115" y="21" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">LEAST SQUARES EQUATIONS</text>
            
            <text x="15" y="60" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">Regression Slope (b_yx):</text>
            <text x="15" y="80" fill="#f8fafc" font-family="sans-serif" font-size="11">b_yx = Cov(X,Y) / Var(X)</text>
            <text x="15" y="98" fill="#94a3b8" font-family="sans-serif" font-size="10">= Σ(X-X̄)(Y-Ȳ) / Σ(X-X̄)²</text>
            <text x="15" y="115" fill="#94a3b8" font-family="sans-serif" font-size="10">= r · (σ_Y / σ_X)</text>

            <text x="15" y="145" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700">Intercept (a):</text>
            <text x="15" y="165" fill="#f8fafc" font-family="sans-serif" font-size="11">a = Ȳ - b_yx · X̄</text>

            <text x="15" y="195" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700">Key Property:</text>
            <text x="15" y="215" fill="#94a3b8" font-family="sans-serif" font-size="10">• Always passes through (X̄, Ȳ)</text>
            <text x="15" y="232" fill="#94a3b8" font-family="sans-serif" font-size="10">• Minimizes sum of squared errors: Σe² = min</text>
          </g>
        </g>
        ''',
        "Regression coefficient b_yx has units (unit Y / unit X). Regression lines intersect at the point of means (X̄, Ȳ)."
    )
}

# u1-t19: ANOVA
UNIT_1_VISUALS["u1-t19"] = {
    "caption": "One-Way Analysis of Variance (ANOVA): Partitioning Total Sum of Squares into Treatment vs Error Variance",
    "svg": make_svg_plate(
        "u1-t19", "UNIT 1 · BIOSTATISTICS", "Analysis of Variance (ANOVA) Partitioning",
        "Fisherian Partitioning of Total Biological Variation: Treatment Effect vs Random Error",
        '''
        <g transform="translate(20, 20)">
          <!-- Top Root Block: Total Variation -->
          <g transform="translate(230, 10)">
            <rect width="280" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
            <text x="140" y="26" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="800" text-anchor="middle">TOTAL SUM OF SQUARES (TSS)</text>
            <text x="140" y="45" fill="#f8fafc" font-family="sans-serif" font-size="11" text-anchor="middle">SS_Total = ΣΣ(Y_ij - Ȳ..)²   |   df = N - 1</text>
          </g>

          <!-- Split Connector lines -->
          <path d="M 370 70 L 370 100 L 170 100 L 170 120" stroke="#64748b" stroke-width="2" fill="none" />
          <path d="M 370 100 L 570 100 L 570 120" stroke="#64748b" stroke-width="2" fill="none" />

          <!-- Left Branch: Treatment -->
          <g transform="translate(30, 120)">
            <rect width="280" height="75" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5" />
            <text x="140" y="24" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">BETWEEN TREATMENTS (SST)</text>
            <text x="140" y="44" fill="#f8fafc" font-family="sans-serif" font-size="11" text-anchor="middle">SS_Trt = Σ n_i (Ȳ_i. - Ȳ..)²</text>
            <text x="140" y="62" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">df = k - 1 (k = number of groups)</text>
          </g>

          <!-- Right Branch: Error -->
          <g transform="translate(430, 120)">
            <rect width="280" height="75" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" />
            <text x="140" y="24" fill="#fb7185" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">WITHIN GROUPS / ERROR (SSE)</text>
            <text x="140" y="44" fill="#f8fafc" font-family="sans-serif" font-size="11" text-anchor="middle">SS_Error = ΣΣ(Y_ij - Ȳ_i.)²</text>
            <text x="140" y="62" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">df = N - k (inherent biological error)</text>
          </g>

          <!-- Mean Squares Box -->
          <g transform="translate(30, 215)">
            <rect width="680" height="85" rx="8" fill="#0f172a" stroke="#334155" />
            <text x="340" y="24" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE F-TEST STATISTIC CALCULATION</text>
            
            <text x="140" y="52" fill="#e2e8f0" font-family="sans-serif" font-size="11" text-anchor="middle">MS_Trt = SS_Trt / (k - 1)</text>
            <text x="340" y="52" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="800" text-anchor="middle">F_cal = MS_Trt / MS_Error</text>
            <text x="540" y="52" fill="#e2e8f0" font-family="sans-serif" font-size="11" text-anchor="middle">MS_Error = SS_Error / (N - k)</text>

            <text x="340" y="74" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">If F_cal &gt; F_critical (k-1, N-k at α = 0.05), Reject H₀: Treatment means differ significantly!</text>
          </g>
        </g>
        ''',
        "ANOVA decomposes total variance into additive components. Assumptions: Normality, Homogeneity of variance (Homoscedasticity), Independence."
    )
}

print(f"visuals_unit1.py loaded with {len(UNIT_1_VISUALS)} anchor visuals.")
