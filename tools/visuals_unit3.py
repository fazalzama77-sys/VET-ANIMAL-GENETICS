# -*- coding: utf-8 -*-
"""
tools/visuals_unit3.py
SVG visual definitions for Unit 3 (Applied Animal Breeding).
"""

from build_all_visuals import make_svg_plate

UNIT_3_VISUALS = {}

# u3-t04: Selection & Genetic Gain
UNIT_3_VISUALS["u3-t04"] = {
    "caption": "Truncation Selection Model: Selection Differential (S), Proportion Saved (p), and Expected Genetic Response (ΔG)",
    "svg": make_svg_plate(
        "u3-t04", "UNIT 3 · ANIMAL BREEDING", "Truncation Selection & Genetic Response (ΔG)",
        "The Breeder's Equation: Translating Phenotypic Superiority into Transmissible Progeny Gain",
        '''
        <g transform="translate(20, 20)">
          <!-- Graph Area: W: 450, H: 260 -->
          <!-- Base Axis -->
          <line x1="30" y1="240" x2="460" y2="240" stroke="#64748b" stroke-width="2" />
          
          <!-- Parent Population Bell Curve -->
          <!-- Normal Curve Outline -->
          <path d="M 40 240 C 120 240, 180 200, 210 120 C 225 70, 235 50, 245 50 C 255 50, 265 70, 280 120 C 310 200, 370 240, 450 240" fill="none" stroke="#64748b" stroke-width="2.5" />

          <!-- Selected Right Tail Truncated Region (Shaded) -->
          <path d="M 290 240 L 290 100 Q 330 180 450 240 Z" fill="#0d9488" opacity="0.6" />
          <line x1="290" y1="40" x2="290" y2="240" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="4,4" />
          <text x="290" y="30" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">Truncation Point (culling boundary)</text>

          <!-- Means: Population Mean (μ), Selected Parents (X̄_s) -->
          <!-- Pop Mean line -->
          <line x1="245" y1="50" x2="245" y2="240" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3" />
          <text x="245" y="260" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">μ (Base Pop Mean)</text>

          <!-- Selected Parents Mean line -->
          <line x1="345" y1="120" x2="345" y2="240" stroke="#2dd4bf" stroke-width="1.5" stroke-dasharray="3,3" />
          <text x="345" y="260" fill="#2dd4bf" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">X̄_s (Selected Parents)</text>

          <!-- Selection Differential (S) Bracket -->
          <line x1="245" y1="210" x2="345" y2="210" stroke="#fbbf24" stroke-width="2" />
          <line x1="245" y1="205" x2="245" y2="215" stroke="#fbbf24" stroke-width="2" />
          <line x1="345" y1="205" x2="345" y2="215" stroke="#fbbf24" stroke-width="2" />
          <text x="295" y="200" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="800" text-anchor="middle">S = (X̄_s - μ)</text>
          <text x="295" y="185" fill="#fbbf24" font-family="sans-serif" font-size="9" text-anchor="middle">Selection Differential</text>

          <!-- Selected Tail Label -->
          <text x="375" y="150" fill="#2dd4bf" font-family="sans-serif" font-size="11" font-weight="700">Selected (p %)</text>
          <text x="375" y="166" fill="#cbd5e1" font-family="sans-serif" font-size="10">Saved for Breeding</text>

          <!-- Right Card: Breeder's Equations -->
          <g transform="translate(480, 15)">
            <rect width="260" height="260" rx="8" fill="#1e293b" stroke="#334155" />
            <rect width="260" height="32" rx="8" fill="url(#tealGrad)" />
            <text x="130" y="21" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">THE BREEDER'S EQUATIONS</text>
            
            <g transform="translate(15, 45)">
              <text x="0" y="16" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">1. Basic Breeder's Equation:</text>
              <text x="10" y="36" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="800">ΔG = h² · S</text>
              <text x="10" y="54" fill="#94a3b8" font-family="sans-serif" font-size="10">(Response = Heritability × Selection Diff)</text>

              <text x="0" y="85" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="700">2. Annual Rate of Genetic Gain:</text>
              <text x="10" y="108" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="800">ΔG / yr = (i · r_TI · σ_A) / L</text>
              
              <text x="10" y="132" fill="#cbd5e1" font-family="sans-serif" font-size="10">• i = Selection intensity (from p %)</text>
              <text x="10" y="148" fill="#cbd5e1" font-family="sans-serif" font-size="10">• r_TI = Accuracy of selection</text>
              <text x="10" y="164" fill="#cbd5e1" font-family="sans-serif" font-size="10">• σ_A = Additive genetic standard dev</text>
              <text x="10" y="180" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="700">• L = Generation interval (in years)</text>
            </g>
          </g>
        </g>
        ''',
        "Annual genetic gain ΔG/yr increases with selection intensity (i), accuracy (r_TI), and diversity (σ_A), but decreases with generation interval (L)."
    )
}

# u3-t14: Indigenous Cattle & Buffalo Breeds
UNIT_3_VISUALS["u3-t14"] = {
    "caption": "Profiles of Premier Indian Dairy Cattle (Sahiwal & Gir) and Riverine Buffalo Breeds (Murrah & Bhadawari)",
    "svg": make_svg_plate(
        "u3-t14", "UNIT 3 · ANIMAL BREEDING", "Premier Indian Dairy Cattle & Buffalo Breeds",
        "Phenotypic Hallmarks, Breeding Tracts, and Production Norms of Elite Indigenous Germplasm",
        '''
        <g transform="translate(15, 15)">
          <!-- 4 Breed Cards: 2 Cattle, 2 Buffalo -->
          <!-- Card 1: Sahiwal -->
          <g transform="translate(10, 10)">
            <rect width="170" height="295" rx="8" fill="#1e293b" stroke="#d97706" stroke-width="1.5" />
            <rect width="170" height="32" rx="8" fill="url(#amberGrad)" />
            <text x="85" y="21" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">SAHIWAL (Cattle)</text>
            
            <text x="12" y="55" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="700">Origin / Tract:</text>
            <text x="12" y="70" fill="#f8fafc" font-family="sans-serif" font-size="10">Montgomery (Pakistan),</text>
            <text x="12" y="84" fill="#94a3b8" font-family="sans-serif" font-size="9">Punjab &amp; Rajasthan border</text>

            <text x="12" y="110" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="700">Physical Hallmarks:</text>
            <text x="12" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Reddish-dun coat</text>
            <text x="12" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Loose skin ('Lola')</text>
            <text x="12" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Voluminous dewlap</text>
            <text x="12" y="170" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Stumpy horns</text>

            <rect x="10" y="195" width="150" height="85" rx="6" fill="#0f172a" />
            <text x="16" y="215" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="700">Performance:</text>
            <text x="16" y="232" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="800">2,000 - 3,200 kg</text>
            <text x="16" y="248" fill="#94a3b8" font-family="sans-serif" font-size="9">Best tropical zebu milch;</text>
            <text x="16" y="262" fill="#94a3b8" font-family="sans-serif" font-size="9">Tick &amp; heat resistant</text>
          </g>

          <!-- Card 2: Gir -->
          <g transform="translate(195, 10)">
            <rect width="170" height="295" rx="8" fill="#1e293b" stroke="#0d9488" stroke-width="1.5" />
            <rect width="170" height="32" rx="8" fill="url(#tealGrad)" />
            <text x="85" y="21" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">GIR (Cattle)</text>
            
            <text x="12" y="55" fill="#2dd4bf" font-family="sans-serif" font-size="10" font-weight="700">Origin / Tract:</text>
            <text x="12" y="70" fill="#f8fafc" font-family="sans-serif" font-size="10">Gir Hills, Saurashtra</text>
            <text x="12" y="84" fill="#94a3b8" font-family="sans-serif" font-size="9">Gujarat (Junagadh)</text>

            <text x="12" y="110" fill="#2dd4bf" font-family="sans-serif" font-size="10" font-weight="700">Physical Hallmarks:</text>
            <text x="12" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Ultra-convex forehead</text>
            <text x="12" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Long pendulous ears</text>
            <text x="12" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="10">  (leaf-like folded tip)</text>
            <text x="12" y="170" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Half-moon curved horns</text>

            <rect x="10" y="195" width="150" height="85" rx="6" fill="#0f172a" />
            <text x="16" y="215" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="700">Performance:</text>
            <text x="16" y="232" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="800">1,800 - 2,800 kg</text>
            <text x="16" y="248" fill="#94a3b8" font-family="sans-serif" font-size="9">Exported to Brazil (Gyr);</text>
            <text x="16" y="262" fill="#94a3b8" font-family="sans-serif" font-size="9">Docile dairy zebu</text>
          </g>

          <!-- Card 3: Murrah -->
          <g transform="translate(380, 10)">
            <rect width="170" height="295" rx="8" fill="#1e293b" stroke="#6366f1" stroke-width="1.5" />
            <rect width="170" height="32" rx="8" fill="url(#indigoGrad)" />
            <text x="85" y="21" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">MURRAH (Buffalo)</text>
            
            <text x="12" y="55" fill="#818cf8" font-family="sans-serif" font-size="10" font-weight="700">Origin / Tract:</text>
            <text x="12" y="70" fill="#f8fafc" font-family="sans-serif" font-size="10">Rohtak, Hisar, Jind</text>
            <text x="12" y="84" fill="#94a3b8" font-family="sans-serif" font-size="9">Haryana &amp; Delhi tract</text>

            <text x="12" y="110" fill="#818cf8" font-family="sans-serif" font-size="10" font-weight="700">Physical Hallmarks:</text>
            <text x="12" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Jet-black body color</text>
            <text x="12" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Tightly curled horns</text>
            <text x="12" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Wedge-shaped barrel</text>
            <text x="12" y="170" fill="#cbd5e1" font-family="sans-serif" font-size="10">• 'Black Gold of India'</text>

            <rect x="10" y="195" width="150" height="85" rx="6" fill="#0f172a" />
            <text x="16" y="215" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="700">Performance:</text>
            <text x="16" y="232" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="800">2,200 - 3,500 kg</text>
            <text x="16" y="248" fill="#94a3b8" font-family="sans-serif" font-size="9">Fat: 7 - 8%</text>
            <text x="16" y="262" fill="#94a3b8" font-family="sans-serif" font-size="9">World premier dairy buffalo</text>
          </g>

          <!-- Card 4: Bhadawari -->
          <g transform="translate(565, 10)">
            <rect width="170" height="295" rx="8" fill="#1e293b" stroke="#e11d48" stroke-width="1.5" />
            <rect width="170" height="32" rx="8" fill="url(#roseGrad)" />
            <text x="85" y="21" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">BHADAWARI (Buffalo)</text>
            
            <text x="12" y="55" fill="#fb7185" font-family="sans-serif" font-size="10" font-weight="700">Origin / Tract:</text>
            <text x="12" y="70" fill="#f8fafc" font-family="sans-serif" font-size="10">Agra &amp; Etawah (UP),</text>
            <text x="12" y="84" fill="#94a3b8" font-family="sans-serif" font-size="9">Bhind &amp; Morena (MP)</text>

            <text x="12" y="110" fill="#fb7185" font-family="sans-serif" font-size="10" font-weight="700">Physical Hallmarks:</text>
            <text x="12" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Copper-colored coat</text>
            <text x="12" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Two white neck lines</text>
            <text x="12" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="10">  ('Chevron' / 'Kanthi')</text>
            <text x="12" y="170" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Light yellow legs</text>

            <rect x="10" y="195" width="150" height="85" rx="6" fill="#0f172a" />
            <text x="16" y="215" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="700">Performance:</text>
            <text x="16" y="232" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="800">Fat: 8 - 13% !</text>
            <text x="16" y="248" fill="#94a3b8" font-family="sans-serif" font-size="9">Highest milk fat breed;</text>
            <text x="16" y="262" fill="#94a3b8" font-family="sans-serif" font-size="9">Ravine grazing resilience</text>
          </g>
        </g>
        ''',
        "Sahiwal has loose skin (Lola); Gir has convex forehead and pendulous ears; Murrah has curled horns; Bhadawari has copper coat and up to 13% milk fat."
    )
}

# u3-t22: Biotechnology & MOET
UNIT_3_VISUALS["u3-t22"] = {
    "caption": "Step-by-Step Reproductive Biotechnology Pipeline: From Artificial Insemination (AI) to Superovulation and MOET in Dairy Cattle",
    "svg": make_svg_plate(
        "u3-t22", "UNIT 3 · ANIMAL BREEDING", "Multiple Ovulation & Embryo Transfer (MOET)",
        "Accelerating Female Genetic Selection: Superovulation, Insemination, Non-Surgical Flushing, and Transfer",
        '''
        <g transform="translate(15, 15)">
          <!-- 5-Step Pipeline Flow -->
          <!-- Step 1: Donor Selection -->
          <g transform="translate(10, 20)">
            <rect width="135" height="180" rx="8" fill="#1e293b" stroke="#334155" />
            <circle cx="67" cy="35" r="20" fill="url(#amberGrad)" />
            <text x="67" y="40" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="800" text-anchor="middle">1</text>
            <text x="67" y="75" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">DONOR COW</text>
            <text x="12" y="100" fill="#94a3b8" font-family="sans-serif" font-size="10">• Top 5% dairy merit</text>
            <text x="12" y="118" fill="#94a3b8" font-family="sans-serif" font-size="10">• Sound pedigree</text>
            <text x="12" y="136" fill="#94a3b8" font-family="sans-serif" font-size="10">• High fertility history</text>
            <text x="12" y="154" fill="#94a3b8" font-family="sans-serif" font-size="10">• Free of diseases</text>
          </g>

          <path d="M 150 110 L 165 110" stroke="#38bdf8" stroke-width="2.5" />

          <!-- Step 2: Superovulation -->
          <g transform="translate(160, 20)">
            <rect width="135" height="180" rx="8" fill="#1e293b" stroke="#334155" />
            <circle cx="67" cy="35" r="20" fill="url(#tealGrad)" />
            <text x="67" y="40" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="800" text-anchor="middle">2</text>
            <text x="67" y="75" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">SUPEROVULATION</text>
            <text x="12" y="100" fill="#2dd4bf" font-family="sans-serif" font-size="10" font-weight="700">• FSH Injections:</text>
            <text x="18" y="116" fill="#94a3b8" font-family="sans-serif" font-size="9">Twice daily for 4 d</text>
            <text x="12" y="134" fill="#2dd4bf" font-family="sans-serif" font-size="10" font-weight="700">• PGF2α Luteolysis:</text>
            <text x="18" y="150" fill="#94a3b8" font-family="sans-serif" font-size="9">Induces synchronized estrus</text>
            <text x="12" y="168" fill="#38bdf8" font-family="sans-serif" font-size="10">Produces 6-12 ova</text>
          </g>

          <path d="M 300 110 L 315 110" stroke="#38bdf8" stroke-width="2.5" />

          <!-- Step 3: Insemination -->
          <g transform="translate(310, 20)">
            <rect width="135" height="180" rx="8" fill="#1e293b" stroke="#334155" />
            <circle cx="67" cy="35" r="20" fill="url(#indigoGrad)" />
            <text x="67" y="40" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="800" text-anchor="middle">3</text>
            <text x="67" y="75" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">INSEMINATION</text>
            <text x="12" y="100" fill="#a78bfa" font-family="sans-serif" font-size="10" font-weight="700">• Elite Bull Semen:</text>
            <text x="18" y="116" fill="#94a3b8" font-family="sans-serif" font-size="9">High BV proven bull</text>
            <text x="12" y="134" fill="#a78bfa" font-family="sans-serif" font-size="10" font-weight="700">• Multiple AI Doses:</text>
            <text x="18" y="150" fill="#94a3b8" font-family="sans-serif" font-size="9">12h &amp; 24h after estrus</text>
            <text x="12" y="168" fill="#38bdf8" font-family="sans-serif" font-size="10">High fertilization rate</text>
          </g>

          <path d="M 450 110 L 465 110" stroke="#38bdf8" stroke-width="2.5" />

          <!-- Step 4: Flushing -->
          <g transform="translate(460, 20)">
            <rect width="135" height="180" rx="8" fill="#1e293b" stroke="#334155" />
            <circle cx="67" cy="35" r="20" fill="url(#amberGrad)" />
            <text x="67" y="40" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="800" text-anchor="middle">4</text>
            <text x="67" y="75" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">FLUSHING (Day 7)</text>
            <text x="12" y="100" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="700">• Foley Catheter:</text>
            <text x="18" y="116" fill="#94a3b8" font-family="sans-serif" font-size="9">Non-surgical uterine flush</text>
            <text x="12" y="134" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="700">• Blastocyst Stage:</text>
            <text x="18" y="150" fill="#94a3b8" font-family="sans-serif" font-size="9">Graded under microscope</text>
            <text x="12" y="168" fill="#38bdf8" font-family="sans-serif" font-size="10">Cryopreserve or transfer</text>
          </g>

          <path d="M 600 110 L 615 110" stroke="#38bdf8" stroke-width="2.5" />

          <!-- Step 5: Transfer -->
          <g transform="translate(610, 20)">
            <rect width="135" height="180" rx="8" fill="#1e293b" stroke="#334155" />
            <circle cx="67" cy="35" r="20" fill="url(#roseGrad)" />
            <text x="67" y="40" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="800" text-anchor="middle">5</text>
            <text x="67" y="75" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">RECIPIENTS</text>
            <text x="12" y="100" fill="#fb7185" font-family="sans-serif" font-size="10" font-weight="700">• Synchronized Recip:</text>
            <text x="18" y="116" fill="#94a3b8" font-family="sans-serif" font-size="9">Exact Day 7 cycle match</text>
            <text x="12" y="134" fill="#fb7185" font-family="sans-serif" font-size="10" font-weight="700">• Ipsilateral Horn:</text>
            <text x="18" y="150" fill="#94a3b8" font-family="sans-serif" font-size="9">Adjacent to active CL</text>
            <text x="12" y="168" fill="#34d399" font-family="sans-serif" font-size="10">Produces elite calves</text>
          </g>

          <!-- Bottom Summary Box -->
          <g transform="translate(10, 215)">
            <rect width="735" height="85" rx="8" fill="#0f172a" stroke="#334155" />
            <text x="367" y="24" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">GENETIC ADVANTAGE OF MOET &amp; IVF PIPELINE</text>
            <text x="25" y="48" fill="#cbd5e1" font-family="sans-serif" font-size="11">• An elite cow naturally yields 4-8 calves in her lifetime; MOET allows 20-50 calves per year through surrogacy.</text>
            <text x="25" y="68" fill="#94a3b8" font-family="sans-serif" font-size="11">• Multiplies female selection intensity and enables juvenile in-vitro embryo transfer (JIVET) to reduce generation interval (L).</text>
          </g>
        </g>
        ''',
        "MOET flushes blastocyst embryos on Day 7 non-surgically using Foley catheter; transferred into synchronized Day 7 recipients."
    )
}

print(f"visuals_unit3.py loaded with {len(UNIT_3_VISUALS)} anchor visuals.")
