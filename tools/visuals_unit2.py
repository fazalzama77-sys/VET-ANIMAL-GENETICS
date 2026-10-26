# -*- coding: utf-8 -*-
"""
tools/visuals_unit2.py
SVG visual definitions for Unit 2 (Genetics, Bacterial Recombination, Molecular Genes, Chromosomes).
"""

from build_all_visuals import make_svg_plate

UNIT_2_VISUALS = {}

# u2-t18: Bacterial Genetics (Transformation, Conjugation, Transduction)
UNIT_2_VISUALS["u2-t18"] = {
    "caption": "The Three Mechanisms of Horizontal Gene Transfer and Recombination in Bacteria: Transformation, Conjugation, and Transduction",
    "svg": make_svg_plate(
        "u2-t18", "UNIT 2 · GENETICS", "Bacterial Recombination Mechanisms",
        "Horizontal Gene Transfer in Bacteria: Transformation, Conjugation, and Transduction",
        '''
        <g transform="translate(10, 15)">
          <!-- Panel 1: Transformation -->
          <g transform="translate(15, 10)">
            <rect width="220" height="295" rx="10" fill="#1e293b" stroke="#0d9488" stroke-width="1.5" />
            <rect width="220" height="34" rx="10" fill="url(#tealGrad)" />
            <text x="110" y="22" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">1. TRANSFORMATION</text>
            
            <!-- Cell & Naked DNA diagram -->
            <ellipse cx="110" cy="95" rx="75" ry="40" fill="#0f172a" stroke="#2dd4bf" stroke-width="2" />
            <path d="M 60 95 Q 85 75 110 95 T 160 95" fill="none" stroke="#64748b" stroke-width="2.5" />
            <text x="110" y="100" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">Recipient Chromosome</text>

            <!-- Naked DNA fragment entering -->
            <path d="M 110 38 L 110 65" stroke="#f43f5e" stroke-width="3" stroke-dasharray="3,3" />
            <text x="110" y="52" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">Naked DNA &darr;</text>

            <text x="15" y="155" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">• Mechanism:</text>
            <text x="25" y="172" fill="#cbd5e1" font-family="sans-serif" font-size="10">Uptake of free, naked extracellular</text>
            <text x="25" y="186" fill="#cbd5e1" font-family="sans-serif" font-size="10">DNA by a competent bacterial cell.</text>

            <text x="15" y="210" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700">• Key Experiments:</text>
            <text x="25" y="227" fill="#cbd5e1" font-family="sans-serif" font-size="10">Griffith (1928): S vs R strains</text>
            <text x="25" y="242" fill="#cbd5e1" font-family="sans-serif" font-size="10">Avery, MacLeod &amp; McCarty (1944):</text>
            <text x="25" y="257" fill="#cbd5e1" font-family="sans-serif" font-size="10">Proved DNA is Transforming Principle</text>
          </g>

          <!-- Panel 2: Conjugation -->
          <g transform="translate(255, 10)">
            <rect width="220" height="295" rx="10" fill="#1e293b" stroke="#6366f1" stroke-width="1.5" />
            <rect width="220" height="34" rx="10" fill="url(#indigoGrad)" />
            <text x="110" y="22" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">2. CONJUGATION</text>
            
            <!-- Two cells connected by pilus -->
            <!-- Donor F+ -->
            <ellipse cx="60" cy="95" rx="40" ry="32" fill="#0f172a" stroke="#818cf8" stroke-width="2" />
            <circle cx="60" cy="85" r="10" fill="none" stroke="#f59e0b" stroke-width="2.5" />
            <text x="60" y="115" fill="#818cf8" font-family="sans-serif" font-size="9" font-weight="700" text-anchor="middle">Donor F⁺</text>

            <!-- Pilus bridge -->
            <rect x="98" y="90" width="24" height="8" rx="3" fill="#a78bfa" />
            <text x="110" y="85" fill="#a78bfa" font-family="sans-serif" font-size="8" text-anchor="middle">Pilus</text>

            <!-- Recipient F- -->
            <ellipse cx="160" cy="95" rx="40" ry="32" fill="#0f172a" stroke="#94a3b8" stroke-width="2" />
            <text x="160" y="115" fill="#94a3b8" font-family="sans-serif" font-size="9" font-weight="700" text-anchor="middle">Recip F⁻</text>

            <text x="15" y="155" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">• Mechanism:</text>
            <text x="25" y="172" fill="#cbd5e1" font-family="sans-serif" font-size="10">Direct physical cell-to-cell contact</text>
            <text x="25" y="186" fill="#cbd5e1" font-family="sans-serif" font-size="10">via sex pilus; rolling-circle transfer.</text>

            <text x="15" y="210" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700">• Key Strains:</text>
            <text x="25" y="227" fill="#cbd5e1" font-family="sans-serif" font-size="10">Lederberg &amp; Tatum (1946)</text>
            <text x="25" y="242" fill="#cbd5e1" font-family="sans-serif" font-size="10">F⁺ × F⁻ &rarr; both become F⁺</text>
            <text x="25" y="257" fill="#cbd5e1" font-family="sans-serif" font-size="10">Hfr: F-plasmid integrated in main loop</text>
          </g>

          <!-- Panel 3: Transduction -->
          <g transform="translate(495, 10)">
            <rect width="220" height="295" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
            <rect width="220" height="34" rx="10" fill="url(#amberGrad)" />
            <text x="110" y="22" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">3. TRANSDUCTION</text>
            
            <!-- Bacteriophage attaching to cell -->
            <!-- Phage head -->
            <polygon points="110,48 122,58 118,74 102,74 98,58" fill="#f59e0b" stroke="#ffffff" stroke-width="1" />
            <line x1="110" y1="74" x2="110" y2="88" stroke="#f59e0b" stroke-width="2" />
            <!-- Tail fibers -->
            <line x1="110" y1="88" x2="98" y2="98" stroke="#f59e0b" stroke-width="1.5" />
            <line x1="110" y1="88" x2="122" y2="98" stroke="#f59e0b" stroke-width="1.5" />

            <!-- Bacterium -->
            <ellipse cx="110" cy="115" rx="60" ry="24" fill="#0f172a" stroke="#94a3b8" stroke-width="1.5" />
            <text x="110" y="118" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">Bacterial Cell</text>

            <text x="15" y="155" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">• Mechanism:</text>
            <text x="25" y="172" fill="#cbd5e1" font-family="sans-serif" font-size="10">Bacteriophage virus serves as a</text>
            <text x="25" y="186" fill="#cbd5e1" font-family="sans-serif" font-size="10">vector transferring bacterial DNA.</text>

            <text x="15" y="210" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700">• Two Main Types:</text>
            <text x="25" y="227" fill="#cbd5e1" font-family="sans-serif" font-size="10">Zinder &amp; Lederberg (1952)</text>
            <text x="25" y="242" fill="#cbd5e1" font-family="sans-serif" font-size="10">Generalized: Lytic (any gene)</text>
            <text x="25" y="257" fill="#cbd5e1" font-family="sans-serif" font-size="10">Specialized: Lysogenic (adjacent genes)</text>
          </g>
        </g>
        ''',
        "Transformation = Free DNA; Conjugation = Direct sex pilus contact (F+/Hfr); Transduction = Bacteriophage viral vector."
    )
}

# u2-t16: DNA Structure
UNIT_2_VISUALS["u2-t16"] = {
    "caption": "Watson-Crick B-DNA Double Helix Model: Structural Dimensions, Antiparallel 5' to 3' Polarity, and Hydrogen-Bonded Base Pairs",
    "svg": make_svg_plate(
        "u2-t16", "UNIT 2 · GENETICS", "DNA Double Helix Molecular Architecture",
        "Watson-Crick B-DNA Model: Dimensions, Base Pairing Rules (Chargaff), and Antiparallel Strands",
        '''
        <g transform="translate(15, 15)">
          <!-- Left: Diagram of Double Helix & Base pairs -->
          <g transform="translate(20, 10)">
            <rect width="360" height="295" rx="10" fill="#1e293b" stroke="#334155" />
            
            <!-- Helix Ribbon Schematics -->
            <path d="M 60 30 Q 140 90 60 150 Q -20 210 60 270" fill="none" stroke="#38bdf8" stroke-width="5" />
            <path d="M 160 30 Q 80 90 160 150 Q 240 210 160 270" fill="none" stroke="#818cf8" stroke-width="5" />

            <!-- Polarity Labels -->
            <text x="50" y="25" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">5'</text>
            <text x="65" y="285" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">3'</text>
            <text x="165" y="25" fill="#818cf8" font-family="sans-serif" font-size="11" font-weight="700">3'</text>
            <text x="150" y="285" fill="#818cf8" font-family="sans-serif" font-size="11" font-weight="700">5'</text>

            <!-- Base Pair Rungs -->
            <line x1="85" y1="50" x2="135" y2="50" stroke="#10b981" stroke-width="3" />
            <text x="110" y="45" fill="#34d399" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">A = T (2 H-bonds)</text>

            <line x1="105" y1="90" x2="115" y2="90" stroke="#f59e0b" stroke-width="4" />

            <line x1="85" y1="130" x2="135" y2="130" stroke="#f43f5e" stroke-width="3" />
            <text x="110" y="125" fill="#fb7185" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">G &equiv; C (3 H-bonds)</text>

            <line x1="85" y1="170" x2="135" y2="170" stroke="#10b981" stroke-width="3" />
            <text x="110" y="165" fill="#34d399" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">T = A</text>

            <line x1="85" y1="210" x2="135" y2="210" stroke="#f43f5e" stroke-width="3" />
            <text x="110" y="205" fill="#fb7185" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">C &equiv; G</text>

            <!-- Dimension callouts -->
            <!-- Helix Diameter -->
            <line x1="210" y1="50" x2="260" y2="50" stroke="#fbbf24" stroke-width="1.5" />
            <line x1="210" y1="45" x2="210" y2="55" stroke="#fbbf24" stroke-width="1.5" />
            <line x1="260" y1="45" x2="260" y2="55" stroke="#fbbf24" stroke-width="1.5" />
            <text x="270" y="54" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700">2.0 nm (20 &Aring;)</text>
            <text x="270" y="67" fill="#94a3b8" font-family="sans-serif" font-size="9">Helix Diameter</text>

            <!-- Complete Turn Pitch -->
            <line x1="210" y1="90" x2="210" y2="210" stroke="#a78bfa" stroke-width="1.5" />
            <line x1="205" y1="90" x2="215" y2="90" stroke="#a78bfa" stroke-width="1.5" />
            <line x1="205" y1="210" x2="215" y2="210" stroke="#a78bfa" stroke-width="1.5" />
            <text x="225" y="145" fill="#a78bfa" font-family="sans-serif" font-size="11" font-weight="700">3.4 nm (34 &Aring;)</text>
            <text x="225" y="160" fill="#94a3b8" font-family="sans-serif" font-size="9">Pitch / 1 Turn (10 bp)</text>
            <text x="225" y="178" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="600">0.34 nm distance/bp</text>
          </g>

          <!-- Right: Rules & Properties -->
          <g transform="translate(400, 10)">
            <rect width="345" height="295" rx="10" fill="#1e293b" stroke="#334155" />
            <rect width="345" height="34" rx="10" fill="url(#tealGrad)" />
            <text x="172" y="22" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">CHARGAFF'S RULES &amp; MOLECULAR LAWS</text>
            
            <g transform="translate(16, 48)">
              <rect width="313" height="60" rx="6" fill="#0f172a" stroke="#0d9488" />
              <text x="15" y="24" fill="#2dd4bf" font-family="sans-serif" font-size="12" font-weight="700">Chargaff's Equivalence Rule:</text>
              <text x="15" y="44" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="700">A = T  and  G = C   &rarr;   (A + G) = (T + C)</text>
              <text x="240" y="44" fill="#94a3b8" font-family="sans-serif" font-size="10">(Purines = Pyrimidines)</text>
            </g>

            <g transform="translate(16, 118)">
              <text x="0" y="18" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">• Right-Handed B-DNA:</text>
              <text x="10" y="34" fill="#cbd5e1" font-family="sans-serif" font-size="11">Standard physiological form in livestock &amp; cells.</text>
              
              <text x="0" y="60" fill="#a78bfa" font-family="sans-serif" font-size="11" font-weight="700">• Major &amp; Minor Grooves:</text>
              <text x="10" y="76" fill="#cbd5e1" font-family="sans-serif" font-size="11">Major groove provides binding sites for regulatory</text>
              <text x="10" y="90" fill="#cbd5e1" font-family="sans-serif" font-size="11">transcription factor proteins.</text>

              <text x="0" y="116" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="700">• Stability &amp; Denaturation (Tm):</text>
              <text x="10" y="132" fill="#cbd5e1" font-family="sans-serif" font-size="11">Higher G≡C content increases melting temperature (Tm)</text>
              <text x="10" y="146" fill="#cbd5e1" font-family="sans-serif" font-size="11">because triple hydrogen bonds require higher thermal energy.</text>
            </g>
          </g>
        </g>
        ''',
        "B-DNA: 10 base pairs per turn (3.4 nm); diameter 2.0 nm; antiparallel 5'-to-3' strands; A=T (2 H-bonds), G≡C (3 H-bonds)."
    )
}

# u2-t03: Chromosome Morphology
UNIT_2_VISUALS["u2-t03"] = {
    "caption": "Morphological Classification of Chromosomes by Centromere Position and Karyotype Arm Ratios (Levan et al.)",
    "svg": make_svg_plate(
        "u2-t03", "UNIT 2 · GENETICS", "Chromosome Structure & Morphological Types",
        "Classification by Centromere Position: Metacentric, Submetacentric, Acrocentric, and Telocentric",
        '''
        <g transform="translate(15, 15)">
          <!-- 4 Chromosome Morphology Columns -->
          <!-- Col 1: Metacentric -->
          <g transform="translate(10, 10)">
            <rect width="170" height="295" rx="8" fill="#1e293b" stroke="#334155" />
            <text x="85" y="24" fill="#2dd4bf" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">METACENTRIC</text>
            <text x="85" y="38" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">Centromere: Median</text>
            
            <!-- Drawing: V-shape chromatids -->
            <!-- p arm -->
            <rect x="78" y="55" width="14" height="60" rx="7" fill="#0d9488" stroke="#2dd4bf" />
            <!-- Centromere -->
            <circle cx="85" cy="120" r="8" fill="#fbbf24" stroke="#ffffff" stroke-width="1.5" />
            <!-- q arm -->
            <rect x="78" y="125" width="14" height="60" rx="7" fill="#0d9488" stroke="#2dd4bf" />
            
            <text x="100" y="85" fill="#2dd4bf" font-family="sans-serif" font-size="10" font-weight="600">p arm</text>
            <text x="100" y="160" fill="#2dd4bf" font-family="sans-serif" font-size="10" font-weight="600">q arm</text>

            <rect x="15" y="195" width="140" height="90" rx="6" fill="#0f172a" />
            <text x="25" y="215" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="700">• Arm Ratio: p ≈ q (1:1)</text>
            <text x="25" y="233" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="700">• Anaphase: V-shape</text>
            <text x="25" y="253" fill="#38bdf8" font-family="sans-serif" font-size="10">• Sheep autosomes</text>
            <text x="35" y="268" fill="#94a3b8" font-family="sans-serif" font-size="9">Pairs 1, 2, and 3 (2n=54)</text>
          </g>

          <!-- Col 2: Submetacentric -->
          <g transform="translate(195, 10)">
            <rect width="170" height="295" rx="8" fill="#1e293b" stroke="#334155" />
            <text x="85" y="24" fill="#818cf8" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">SUBMETACENTRIC</text>
            <text x="85" y="38" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">Centromere: Sub-median</text>
            
            <!-- p arm (shorter) -->
            <rect x="78" y="70" width="14" height="40" rx="7" fill="#4f46e5" stroke="#818cf8" />
            <!-- Centromere -->
            <circle cx="85" cy="115" r="8" fill="#fbbf24" stroke="#ffffff" stroke-width="1.5" />
            <!-- q arm (longer) -->
            <rect x="78" y="120" width="14" height="75" rx="7" fill="#4f46e5" stroke="#818cf8" />

            <text x="100" y="90" fill="#818cf8" font-family="sans-serif" font-size="10" font-weight="600">p (short)</text>
            <text x="100" y="160" fill="#818cf8" font-family="sans-serif" font-size="10" font-weight="600">q (long)</text>

            <rect x="15" y="195" width="140" height="90" rx="6" fill="#0f172a" />
            <text x="25" y="215" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="700">• Arm Ratio: p &lt; q</text>
            <text x="25" y="233" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="700">• Anaphase: L / J-shape</text>
            <text x="25" y="253" fill="#38bdf8" font-family="sans-serif" font-size="10">• River Buffalo (5 pairs)</text>
            <text x="35" y="268" fill="#94a3b8" font-family="sans-serif" font-size="9">Bovine X chromosome</text>
          </g>

          <!-- Col 3: Acrocentric -->
          <g transform="translate(380, 10)">
            <rect width="170" height="295" rx="8" fill="#1e293b" stroke="#334155" />
            <text x="85" y="24" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">ACROCENTRIC</text>
            <text x="85" y="38" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">Centromere: Sub-terminal</text>
            
            <!-- p arm (tiny knob) -->
            <rect x="80" y="92" width="10" height="12" rx="4" fill="#d97706" stroke="#fbbf24" />
            <!-- Centromere -->
            <circle cx="85" cy="110" r="8" fill="#fbbf24" stroke="#ffffff" stroke-width="1.5" />
            <!-- q arm (very long) -->
            <rect x="78" y="115" width="14" height="85" rx="7" fill="#d97706" stroke="#fbbf24" />

            <text x="98" y="100" fill="#fbbf24" font-family="sans-serif" font-size="9" font-weight="600">p (knob)</text>
            <text x="100" y="160" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="600">q (main)</text>

            <rect x="15" y="195" width="140" height="90" rx="6" fill="#0f172a" />
            <text x="25" y="215" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="700">• Arm Ratio: p &lt;&lt; q</text>
            <text x="25" y="233" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="700">• Anaphase: i / rod</text>
            <text x="25" y="253" fill="#38bdf8" font-family="sans-serif" font-size="10">• Cattle &amp; Goat (2n=60)</text>
            <text x="35" y="268" fill="#94a3b8" font-family="sans-serif" font-size="9">All 29 autosome pairs</text>
          </g>

          <!-- Col 4: Telocentric -->
          <g transform="translate(565, 10)">
            <rect width="170" height="295" rx="8" fill="#1e293b" stroke="#334155" />
            <text x="85" y="24" fill="#f43f5e" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">TELOCENTRIC</text>
            <text x="85" y="38" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">Centromere: Strictly Terminal</text>
            
            <!-- Centromere at absolute tip -->
            <circle cx="85" cy="95" r="8" fill="#fbbf24" stroke="#ffffff" stroke-width="1.5" />
            <!-- single q arm -->
            <rect x="78" y="102" width="14" height="95" rx="7" fill="#e11d48" stroke="#f43f5e" />

            <text x="100" y="160" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="600">q only</text>

            <rect x="15" y="195" width="140" height="90" rx="6" fill="#0f172a" />
            <text x="25" y="215" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="700">• Single visible arm</text>
            <text x="25" y="233" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="700">• p arm absent</text>
            <text x="25" y="253" fill="#38bdf8" font-family="sans-serif" font-size="10">• House Mouse (Mus)</text>
            <text x="35" y="268" fill="#94a3b8" font-family="sans-serif" font-size="9">Rare in farm livestock</text>
          </g>
        </g>
        ''',
        "Cattle autosomes are strictly acrocentric (2n=60); River buffalo has 5 submetacentric + 19 acrocentric pairs (2n=50)."
    )
}

# u2-t06: Epistasis Ratios
UNIT_2_VISUALS["u2-t06"] = {
    "caption": "The Six Classical Modified Dihybrid Epistatic Ratios Resulting from Multi-Step Biochemical Interactions",
    "svg": make_svg_plate(
        "u2-t06", "UNIT 2 · GENETICS", "The Classical Epistatic Dihybrid Ratios",
        "Non-Allelic Gene Interactions Modifying Mendel's 9:3:3:1 Proportions",
        '''
        <g transform="translate(15, 15)">
          <!-- Epistatic Table Matrix -->
          <rect width="740" height="300" rx="10" fill="#1e293b" stroke="#334155" />
          
          <!-- Header -->
          <rect width="740" height="34" rx="10" fill="url(#indigoGrad)" />
          <text x="140" y="22" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700">TYPE OF EPISTASIS</text>
          <text x="320" y="22" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">MODIFIED RATIO</text>
          <text x="430" y="22" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700">GENOTYPIC GROUPINGS</text>
          <text x="630" y="22" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700">CLASSICAL ANIMAL EXAMPLE</text>

          <!-- Row 1: Dominant Epistasis -->
          <g transform="translate(15, 45)">
            <text x="0" y="18" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">1. Dominant Epistasis</text>
            <rect x="260" y="4" width="70" height="22" rx="4" fill="#0f172a" stroke="#0d9488" />
            <text x="295" y="19" fill="#2dd4bf" font-family="sans-serif" font-size="11" font-weight="800" text-anchor="middle">12 : 3 : 1</text>
            <text x="380" y="18" fill="#cbd5e1" font-family="sans-serif" font-size="11">(9 A_B_ + 3 A_bb) : 3 aaB_ : 1 aabb</text>
            <text x="560" y="18" fill="#94a3b8" font-family="sans-serif" font-size="10">Dog coat color (I inhibitor); Squash</text>
          </g>
          <line x1="15" y1="75" x2="725" y2="75" stroke="#334155" />

          <!-- Row 2: Recessive Epistasis -->
          <g transform="translate(15, 85)">
            <text x="0" y="18" fill="#a78bfa" font-family="sans-serif" font-size="11" font-weight="700">2. Recessive Epistasis (Supplementary)</text>
            <rect x="260" y="4" width="70" height="22" rx="4" fill="#0f172a" stroke="#6366f1" />
            <text x="295" y="19" fill="#a5b4fc" font-family="sans-serif" font-size="11" font-weight="800" text-anchor="middle">9 : 3 : 4</text>
            <text x="380" y="18" fill="#cbd5e1" font-family="sans-serif" font-size="11">9 B_E_ : 3 bbE_ : 4 (--ee)</text>
            <text x="560" y="18" fill="#94a3b8" font-family="sans-serif" font-size="10">Labrador coat (Black, Choc, Yellow)</text>
          </g>
          <line x1="15" y1="115" x2="725" y2="115" stroke="#334155" />

          <!-- Row 3: Duplicate Dominant -->
          <g transform="translate(15, 125)">
            <text x="0" y="18" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700">3. Duplicate Dominant Epistasis</text>
            <rect x="260" y="4" width="70" height="22" rx="4" fill="#0f172a" stroke="#10b981" />
            <text x="295" y="19" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="800" text-anchor="middle">15 : 1</text>
            <text x="380" y="18" fill="#cbd5e1" font-family="sans-serif" font-size="11">(9 A_B_ + 3 A_bb + 3 aaB_) : 1 aabb</text>
            <text x="560" y="18" fill="#94a3b8" font-family="sans-serif" font-size="10">Feathered vs Clean shanks in fowl</text>
          </g>
          <line x1="15" y1="155" x2="725" y2="155" stroke="#334155" />

          <!-- Row 4: Duplicate Recessive (Complementary) -->
          <g transform="translate(15, 165)">
            <text x="0" y="18" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700">4. Duplicate Recessive (Complementary)</text>
            <rect x="260" y="4" width="70" height="22" rx="4" fill="#0f172a" stroke="#f59e0b" />
            <text x="295" y="19" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="800" text-anchor="middle">9 : 7</text>
            <text x="380" y="18" fill="#cbd5e1" font-family="sans-serif" font-size="11">9 A_B_ : (3 A_bb + 3 aaB_ + 1 aabb)</text>
            <text x="560" y="18" fill="#94a3b8" font-family="sans-serif" font-size="10">Sweet pea flower color; Deaf-mutism</text>
          </g>
          <line x1="15" y1="195" x2="725" y2="195" stroke="#334155" />

          <!-- Row 5: Duplicate Genes with Cumulative Effect -->
          <g transform="translate(15, 205)">
            <text x="0" y="18" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="700">5. Polymeric Genes (Cumulative Effect)</text>
            <rect x="260" y="4" width="70" height="22" rx="4" fill="#0f172a" stroke="#e11d48" />
            <text x="295" y="19" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="800" text-anchor="middle">9 : 6 : 1</text>
            <text x="380" y="18" fill="#cbd5e1" font-family="sans-serif" font-size="11">9 A_B_ : (3 A_bb + 3 aaB_) : 1 aabb</text>
            <text x="560" y="18" fill="#94a3b8" font-family="sans-serif" font-size="10">Duroc-Jersey swine coat (Red, Sandy)</text>
          </g>
          <line x1="15" y1="235" x2="725" y2="235" stroke="#334155" />

          <!-- Row 6: Inhibitory Gene -->
          <g transform="translate(15, 245)">
            <text x="0" y="18" fill="#e2e8f0" font-family="sans-serif" font-size="11" font-weight="700">6. Dominant &amp; Recessive (Inhibitory)</text>
            <rect x="260" y="4" width="70" height="22" rx="4" fill="#0f172a" stroke="#94a3b8" />
            <text x="295" y="19" fill="#e2e8f0" font-family="sans-serif" font-size="11" font-weight="800" text-anchor="middle">13 : 3</text>
            <text x="380" y="18" fill="#cbd5e1" font-family="sans-serif" font-size="11">(9 I_C_ + 3 I_cc + 1 iicc) : 3 iiC_</text>
            <text x="560" y="18" fill="#94a3b8" font-family="sans-serif" font-size="10">White Leghorn plumage (I inhibitor)</text>
          </g>
        </g>
        ''',
        "Epistasis modifies phenotypic ratios without altering the underlying 1:2:1:2:4:2:1:2:1 Mendelian genotypic segregation."
    )
}

# u2-t21: Hardy-Weinberg
UNIT_2_VISUALS["u2-t21"] = {
    "caption": "The Hardy-Weinberg Equilibrium Law: Parabolic Genotypic Frequencies (p², 2pq, q²) across Allele Frequencies (p + q = 1)",
    "svg": make_svg_plate(
        "u2-t21", "UNIT 2 · GENETICS", "Hardy-Weinberg Equilibrium Parabolic Model",
        "Genotypic Frequencies (p², 2pq, q²) as a Function of Gene Frequencies (p + q = 1)",
        '''
        <g transform="translate(20, 20)">
          <!-- Graph Area: W: 450, H: 250 -->
          <line x1="50" y1="250" x2="480" y2="250" stroke="#64748b" stroke-width="2" />
          <line x1="50" y1="250" x2="50" y2="20" stroke="#64748b" stroke-width="2" />
          
          <text x="480" y="265" fill="#94a3b8" font-family="sans-serif" font-size="11">Gene Frequency of 'A' (p)</text>
          <text x="45" y="15" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="end">Genotypic Frequency</text>

          <!-- Ticks on X axis: 0, 0.5, 1.0 -->
          <text x="50" y="270" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">p = 0.0</text>
          <text x="265" y="270" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">p = 0.5</text>
          <text x="470" y="270" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">p = 1.0</text>

          <!-- Ticks on Y axis: 0, 0.5, 1.0 -->
          <text x="40" y="255" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="end">0.0</text>
          <text x="40" y="140" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="end">0.5</text>
          <text x="40" y="30" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="end">1.0</text>

          <!-- Curves -->
          <!-- p² (AA): starts at 0, goes to 1.0 at p=1.0 -->
          <path d="M 50 250 Q 265 240 470 30" fill="none" stroke="#2dd4bf" stroke-width="3" />
          <text x="475" y="30" fill="#2dd4bf" font-family="sans-serif" font-size="12" font-weight="700">p² (AA)</text>

          <!-- q² (aa): starts at 1.0 at p=0, goes to 0 at p=1.0 -->
          <path d="M 50 30 Q 255 240 470 250" fill="none" stroke="#f43f5e" stroke-width="3" />
          <text x="50" y="20" fill="#f43f5e" font-family="sans-serif" font-size="12" font-weight="700">q² (aa)</text>

          <!-- 2pq (Aa): Parabola, peak at 0.5 (height 0.5 = y: 140) -->
          <path d="M 50 250 Q 260 30 470 250" fill="none" stroke="#fbbf24" stroke-width="3.5" />
          <text x="260" y="115" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="800" text-anchor="middle">2pq (Aa) Peak = 0.5</text>

          <!-- Peak dot at p=0.5 -->
          <circle cx="260" cy="140" r="5" fill="#fbbf24" />
          <line x1="260" y1="140" x2="260" y2="250" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,3" />

          <!-- Right Card: Assumptions -->
          <g transform="translate(505, 15)">
            <rect width="235" height="260" rx="8" fill="#1e293b" stroke="#334155" />
            <rect width="235" height="32" rx="8" fill="url(#tealGrad)" />
            <text x="117" y="21" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">5 HARDY-WEINBERG ASSUMPTIONS</text>
            
            <g transform="translate(15, 45)">
              <text x="0" y="16" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700">1. Large Population:</text>
              <text x="10" y="32" fill="#94a3b8" font-family="sans-serif" font-size="10">Negligible random genetic drift.</text>

              <text x="0" y="54" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700">2. Random Mating (Panmixia):</text>
              <text x="10" y="70" fill="#94a3b8" font-family="sans-serif" font-size="10">Equal probability of union.</text>

              <text x="0" y="92" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700">3. No Selection:</text>
              <text x="10" y="108" fill="#94a3b8" font-family="sans-serif" font-size="10">All genotypes have equal fitness.</text>

              <text x="0" y="130" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700">4. No Mutation:</text>
              <text x="10" y="146" fill="#94a3b8" font-family="sans-serif" font-size="10">No conversion of A &harr; a alleles.</text>

              <text x="0" y="168" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700">5. No Migration:</text>
              <text x="10" y="184" fill="#94a3b8" font-family="sans-serif" font-size="10">Closed genetic population.</text>
            </g>
          </g>
        </g>
        ''',
        "Hardy-Weinberg equation: p² + 2pq + q² = 1. Maximum frequency of heterozygotes (2pq = 0.5) occurs strictly when p = q = 0.5."
    )
}

print(f"visuals_unit2.py loaded with {len(UNIT_2_VISUALS)} anchor visuals.")
