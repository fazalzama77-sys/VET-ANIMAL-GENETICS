# -*- coding: utf-8 -*-
"""
Unit 3 - Part 4: Topics u3-t22 to u3-t28
Principles of Animal Breeding (IVRI Undergrad 10 CGPA Standard)
"""

topics = {}

topics["u3-t22"] = {
    "summary": "Reproductive and biotechnological tools—Artificial Insemination, sexed semen, MOET, in-vitro fertilization, and Genomic Selection—exponentially amplify selection intensity, expand accuracy, and slash generation intervals in livestock breeding.",
    "desc": (
        "<b>I. ARTIFICIAL INSEMINATION (AI) AND CRYOPRESERVATION</b><br>"
        "Artificial Insemination is the manual deposition of viable male spermatozoa into the female reproductive tract using specialized instruments:"
        "<ul>"
        "<li><b>Breeding Impact:</b> AI is the single greatest biotechnological multiplier of male genetic merit in history. "
        "A superior dairy bull under natural service sires 40–60 calves per year; through AI, his semen can be diluted and extended into <b>30,000 to 50,000 frozen doses annually</b>, siring over 100,000 lifetime daughters across continents!</li>"
        "<li><b>Technical Protocol in Bovines:</b>"
        "<br>&bull; <i>Semen Collection:</i> Artificial Vagina (AV) method at 42–45&deg;C with a teaser animal."
        "<br>&bull; <i>Semen Evaluation:</i> Volume (4–8 ml), mass activity (0 to +++), progressive individual forward motility (&ge; 70%), sperm concentration (1,000–1,500 million/ml), live-dead differential staining (Eosin-Nigrosin), and acrosomal integrity."
        "<br>&bull; <i>Extenders / Dilutors:</i> Tris-egg yolk-citrate or soy-lecithin extender containing <b>6.4–7.0% glycerol as cryoprotectant</b> to prevent ice crystal rupture."
        "<br>&bull; <i>Packaging & Storage:</i> Packaged in French mini (0.25 ml) or medium (0.50 ml) straws (containing minimum 20 million spermatozoa before freezing, ensuring &ge; 10 million post-thaw motile sperms). Plunged and stored perpetually in liquid nitrogen (<b>-196&deg;C</b>)."
        "<br>&bull; <i>Insemination:</i> Performed during mid-to-late estrus using the <b>Rectovaginal Technique</b>, depositing semen precisely into the body of the uterus just past the internal cervical os.</li>"
        "<li><b>Sex-Sorted Semen Technology:</b>"
        "<br>&bull; Developed by USDA and commercialized via flow cytometric cell sorting."
        "<br>&bull; <i>Principle:</i> Bovine X-chromosome is physically larger than Y, possessing <b>3.8% more DNA</b> in cattle (4.0% in buffaloes). Spermatozoa are stained with fluorescent dye Hoechst 33342; a high-speed laser flow cytometer detects differential fluorescence and applies electrostatic deflection charges."
        "<br>&bull; Produces straws with <b>&ge; 90% purity of X-bearing spermatozoa</b>, guaranteeing > 90% female calf births.</li>"
        "</ul><br>"
        "<b>II. MULTIPLE OVULATION AND EMBRYO TRANSFER (MOET)</b><br>"
        "MOET amplifies the genetic contribution of elite females, who normally produce only 4–8 calves in a lifetime:"
        "<ul>"
        "<li><b>Step-by-Step Protocol:</b>"
        "<br>1. <b>Donor Superovulation:</b> High-genetic merit donor cow injected with exogenous gonadotropins (<b>FSH in declining doses over 4 days</b> or a single dose of eCG) around Day 9–11 of the estrous cycle to rescue multiple antral follicles from atresia."
        "<br>2. <b>Luteolysis:</b> Prostaglandin F2&alpha; (PGF2&alpha;) administered on Day 3 of FSH regimen to induce synchronized estrus."
        "<br>3. <b>Insemination:</b> Donor bred 2 to 3 times at 12-hour intervals with elite pedigreed semen."
        "<br>4. <b>Non-Surgical Uterine Flushing (Day 7):</b> Seven days post-insemination (when embryos have entered the uterine horns as morulae or unhatched blastocysts), a three-way balloon Foley catheter is passed through the cervix. Uterus is flushed with Dulbecco's Phosphate-Buffered Saline (DPBS) &plus; 1% BSA."
        "<br>5. <b>Embryo Searching, Grading & Transfer:</b> Flushed fluid passes through an embryo filter (70 &mu;m). Embryos are graded under a stereomicroscope into Grade 1 (excellent), Grade 2 (good), Grade 3 (fair), and degenerate. "
        "Viable embryos are immediately transferred non-surgically into the <b>ipsilateral uterine horn</b> of synchronized recipient surrogate cows (at Day 7 of their cycle, adjacent to the ovary with active corpus luteum) or cryopreserved in liquid nitrogen using ethylene glycol (vitrification).</li>"
        "</ul><br>"
        "<b>III. IN-VITRO EMBRYO PRODUCTION (IVEP / IVF)</b><br>"
        "Encompasses <b>Transvaginal Ultrasound-Guided Ovum Pick-Up (OPU)</b> from living cows followed by in-vitro maturation (IVM), in-vitro fertilization (IVF), and in-vitro culture (IVC) to the blastocyst stage. Applicable to pregnant cows, infertile elite donors with blocked oviducts, and even prepubertal heifer calves.<br><br>"
        "<b>IV. GENOMIC SELECTION (MEUWISSEN, GODDARD, HAYES 2001)</b><br>"
        "The revolutionary apex of modern quantitative animal breeding:"
        "<ul>"
        "<li><b>Principle:</b> Instead of tracking a few candidate genes, dense panels of tens of thousands of Single Nucleotide Polymorphism (SNP) markers (50K to 777K High-Density chips) distributed evenly across the entire genome are utilized so that <i>every quantitative trait locus (QTL) is in close Linkage Disequilibrium (LD) with at least one neighboring SNP marker</i>.</li>"
        "<li><b>Methodology:</b>"
        "<br>1. <b>Reference Population:</b> Large group of animals (thousands of progeny-tested bulls) possessing both phenotypic records (y) and dense SNP genotypes. Statistical models estimate the precise additive effect (<code>\\hat{g}_i</code>) of every individual SNP marker across the genome."
        "<br>2. <b>Prediction in Candidates:</b> Newborn calves are genotyped at birth via DNA from a hair follicle or blood drop."
        "<br>3. <b>Genomic Estimated Breeding Value (GEBV):</b> Summation of all marker effects: <code>GEBV = &Sigma; X_i \\hat{g}_i</code>.</li>"
        "<li><b>Why Genomic Selection Doubled Annual Genetic Progress:</b>"
        "<br>&bull; In the classic breeder's equation <code>&Delta;G = (i &times; r_TI &times; &sigma;_A) / L</code>, traditional progeny testing took <b>6 to 7 years</b> to prove a bull. Genomic evaluation achieves <b>r_TI = 0.70 to 0.85 at birth</b>, slashing the generation interval (L) from 6 years to <b>1.5 to 2 years</b>!</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>The Mathematical Machinery of GBLUP & Single-Step BLUP (ssGBLUP):</b><br>"
        "To earn 10/10 in competitive exams, explain the transition from pedigree to genomic matrices:"
        "<ul>"
        "<li><b>VanRaden's Genomic Relationship Matrix (G Matrix):</b> "
        "Calculated directly from the SNP marker incidence matrix <code>M</code> (coded as -1, 0, 1 for genotypes aa, Aa, AA):<br>"
        "<code>G = (Z Z') / [ 2 &Sigma; p_i (1 - p_i) ]</code> (where <code>Z = M - P</code>, and <code>P = 2(p_i - 0.5)</code>)."
        "<br>&bull; Unlike the pedigree <b>A</b> matrix, which only gives the <i>expected</i> average relationship between full sibs (0.50), the <b>G</b> matrix captures the <i>realized Mendelian segregation</i> (exact genomic sharing between full sibs can range from 0.35 to 0.65!).</li>"
        "<li><b>Single-Step GBLUP (Legarra et al. 2009):</b> Replaces <code>A⁻¹</code> in Henderson's Mixed Model Equations with <code>H⁻¹</code>, blending the pedigree matrix <b>A</b> with genomic matrix <b>G</b>: "
        "<code>H⁻¹ = A⁻¹ + [ 0 &nbsp; 0 ; 0 &nbsp; (G⁻¹ - A₂₂⁻¹) ]</code>, allowing simultaneous genetic evaluation of genotyped and non-genotyped animals together.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "AI is the primary multiplier of male genetic merit, enabling a bull to sire > 30,000 calves annually.",
        "Bovine semen is extended with Tris-egg yolk dilutor and 6.4–7% glycerol cryoprotectant at -196°C.",
        "Bovine AI uses the rectovaginal technique, depositing semen into the body of the uterus during mid-to-late estrus.",
        "Sexed semen uses flow cytometry to separate X from Y sperm based on 3.8% more DNA in X-sperm.",
        "Sex-sorted semen delivers ≥ 90% female calves, transforming dairy commercial replacement economics.",
        "MOET superovulates elite donor cows using declining doses of FSH over 4 days around Day 9-11.",
        "Uterine flushing in MOET occurs non-surgically on Day 7 post-insemination using a three-way Foley catheter.",
        "Flushed embryos are transferred into the ipsilateral uterine horn of synchronized recipient surrogate dams.",
        "Genomic Selection (Meuwissen et al., 2001) estimates GEBV by summing whole-genome dense SNP marker effects.",
        "Genomic selection slashes generation interval in dairy cattle from 6 years to 1.5–2 years, doubling annual genetic gain.",
        "The Genomic Relationship Matrix (G) captures actual realized Mendelian chromosomal sharing between relatives."
    ],
    "tables": [
        {
            "title": "Comparison of Reproductive and Biotechnological Tools in Animal Breeding",
            "headers": ["Biotechnological Tool", "Primary Biological Target", "Multiplication Factor", "Key Reagent / Instrument", "Impact on Breeder's Equation (&Delta;G)"],
            "rows": [
                ["Artificial Insemination (AI)", "Elite male gamete (spermatozoa)", "30,000–50,000 doses / bull / year", "French straws, Liquid nitrogen (-196&deg;C)", "Massively elevates male selection intensity (i)"],
                ["Sex-Sorted Semen", "X-bearing spermatozoa separation", "> 90% female calves born", "Hoechst 33342, Laser Flow Cytometer", "Maximizes female selection intensity; eliminates unwanted males"],
                ["MOET (In-Vivo Embryos)", "Elite female gamete (oocytes/embryos)", "20–40 calves / elite cow / year", "Porcine FSH, PGF2&alpha;, Foley Catheter", "Elevates female selection intensity and dam-line accuracy"],
                ["OPU-IVF (In-Vitro)", "Oocytes from live / abattoir ovaries", "50–100 blastocysts / cow / year", "Transvaginal ultrasound probe, CO2 incubator", "Enables propagation from pregnant, infertile, or prepubertal females"],
                ["Genomic Selection (GS)", "Whole-genome SNP marker genotypes", "Population-wide early screening at birth", "Illumina / Affymetrix SNP chips (50K–777K)", "Halves generation interval (L) & elevates juvenile accuracy (r_TI)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In field AI practice, a common reason for conception failure when using expensive sexed semen straws is improper handling. "
        "Sex-sorted spermatozoa have reduced lifespan due to mechanical shearing stress during high-speed flow cytometric sorting. "
        "Field veterinarians must strictly follow the <b>Thawing Protocol: 37&deg;C water bath for exactly 30 seconds</b>, "
        "inseminate within 10 minutes of thawing, and ensure deep uterine horn deposition precisely at <b>16–20 hours after the onset of standing estrus</b> "
        "to maintain conception rates above 50–55%."
    ),
    "tags": ["Biotechnology", "Artificial Insemination", "Sexed Semen", "MOET", "IVF", "Genomic Selection", "SNP", "GBLUP", "French Straw"]
}

topics["u3-t23"] = {
    "summary": "Breeding for disease resistance exploits host genetic variation in immune loci—notably the Major Histocompatibility Complex (MHC/BoLA/B-complex)—to select animals that resist, tolerate, or control infectious pathogens.",
    "desc": (
        "<b>CONCEPTS: RESISTANCE, TOLERANCE, AND RESILIENCE</b><br>"
        "In veterinary genetics, host defense mechanisms against pathogens are categorized into three distinct biological phenomena:"
        "<ol>"
        "<li><b>Disease Resistance:</b> The inherited capacity of an animal to prevent pathogen establishment, restrict pathogen replication, or rapidly clear the infection (e.g., lower parasite burden, negative diagnostic titer).</li>"
        "<li><b>Disease Tolerance:</b> The host's capacity to limit the physiological and cellular damage caused by a pathogen load without necessarily reducing pathogen replication. The animal harbors pathogens but maintains normal production.</li>"
        "<li><b>Disease Resilience:</b> The ability of an animal to maintain its growth, milk yield, or reproductive performance unaffected in the presence of endemic field infection.</li>"
        "</ol><br>"
        "<b>THE MAJOR HISTOCOMPATIBILITY COMPLEX (MHC) IN LIVESTOCK</b><br>"
        "The MHC is the most polymorphic gene cluster in vertebrate genomes, encoding cell-surface glycoproteins that bind and present processed antigenic peptides to T-lymphocytes:"
        "<ul>"
        "<li><b>Cattle (Bovine Leukocyte Antigen - BoLA):</b>"
        "<br>&bull; Located on bovine <b>Chromosome 23</b>; partitioned into Class I, Class II (IIa and IIb), and Class III regions."
        "<br>&bull; The <b>BoLA-DRB3 locus</b> in Class II displays extreme polymorphism (> 100 alleles). Specific alleles (e.g., <code>BoLA-DRB3*16</code>) correlate with resistance to <b>Bovine Leukemia Virus (BLV)</b> and low proviral loads."
        "<br>&bull; Certain alleles correlate with lower Somatic Cell Count (SCC) and resistance to clinical mastitis.</li>"
        "<li><b>Poultry (Chicken B-Complex & Marek's Disease):</b>"
        "<br>&bull; Located on microchromosome 16. Encodes B-F (Class I), B-L (Class II), and B-G (erythrocyte antigens)."
        "<br>&bull; <b>The B21 Haplotype:</b> Discovered by Briles (1977), the <code>B^{21}</code> haplotype confers <b>extraordinary genetic resistance to Marek's Disease</b> (an oncogenic herpesvirus inducing T-cell lymphoma). Birds carrying <code>B^{21}</code> develop minimal tumors and maintain high livability."
        "<br>&bull; Conversely, the <code>B^{19}</code> haplotype confers extreme susceptibility, with over 80% mortality upon field exposure!</li>"
        "</ul><br>"
        "<b>GENETIC RESISTANCE TO SPECIFIC LIVESTOCK DISEASES</b><br>"
        "<ul>"
        "<li><b>1. Mastitis Resistance in Dairy Cattle:</b>"
        "<br>&bull; <i>Indicator Trait:</i> <b>Somatic Cell Count (SCC)</b> in milk (primarily neutrophils and macrophages migrating into the udder). "
        "<br>&bull; Standardized as <b>Somatic Cell Score (SCS):</b> <code>SCS = log_2(SCC / 100,000) + 3</code> (Heritability h&sup2; &approx; 0.12–0.15)."
        "<br>&bull; <i>The Genetic Dilemma:</i> The genetic correlation between milk yield and mastitis susceptibility is unfavorable (<code>r_g = +0.20 to +0.30</code>). Selecting purely for higher milk yield inadvertently increases mastitis incidence. Modern breeding indices counter this by assigning negative economic weights to SCS.</li>"
        "<li><b>2. Gastrointestinal Nematode Resistance in Sheep:</b>"
        "<br>&bull; <i>Haemonchus contortus</i> (barber's pole worm) causes devastating blood loss and anemia."
        "<br>&bull; <i>Selection Criteria:</i> <b>Fecal Egg Count (FEC)</b> via McMaster technique (h&sup2; = 0.25–0.35) and mucosal membrane pallor scoring via the <b>FAMACHA chart</b>. Resistant sheep breeds (e.g., Red Maasai, Barbados Blackbelly, Garole) mount intense Th2 eosinophilic mucosal responses.</li>"
        "<li><b>3. Tick Resistance in Cattle:</b>"
        "<br>&bull; <i>Rhipicephalus microplus</i> transmits <i>Theileria</i>, <i>Babesia</i>, and <i>Anaplasma</i>."
        "<br>&bull; Zebu cattle (<i>Bos indicus</i>) carry > 80% fewer ticks than European taurine cattle (<i>Bos taurus</i>) due to vigorous grooming, smooth coat hair, tight skin twitching (panniculus reflex), high arteriolar vasoconstriction, and local cutaneous histamine hypersensitivity.</li>"
        "<li><b>4. Scrapie Resistance in Sheep (PrP Genotypes):</b>"
        "<br>&bull; Scrapie is a fatal neurodegenerative transmissible spongiform encephalopathy (prion disease)."
        "<br>&bull; Governed by codons <b>136, 154, and 171</b> of the prion protein (<i>PrP</i>) gene."
        "<br>&bull; Allele <code>ARR</code> (Alanine-136, Arginine-154, Arginine-171) confers <b>complete genetic resistance</b>."
        "<br>&bull; Allele <code>VRQ</code> (Valine-136, Arginine-154, Glutamine-171) confers <b>extreme susceptibility</b>. National eradication programs genotype and eliminate <code>VRQ</code> carrier rams!</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Single-Gene Monogenic vs Polygenic Disease Inheritance:</b><br>"
        "In university exams, clearly categorize genetic resistance mechanisms:"
        "<ul>"
        "<li><b>Monogenic Resistance (Single Gene Mendelian):</b>"
        "<br>&bull; <i>E. coli F18 receptor gene (FUT1) in swine:</i> Mutation in alpha-(1,2)-fucosyltransferase gene renders pigs resistant to post-weaning diarrhea and edema disease."
        "<br>&bull; <i>PrP gene in sheep:</i> <code>ARR/ARR</code> homozygotes are immune to classical scrapie.</li>"
        "<li><b>Polygenic Resistance (Quantitative Inheritance):</b>"
        "<br>&bull; Mastitis, foot rot, gastrointestinal nematodes, and bovine respiratory disease are polygenic, controlled by hundreds of small-effect QTLs."
        "<br>&bull; Genomic selection utilizing single-step GBLUP incorporates health, immune, and longevity traits into national selection indexes (e.g., Net Merit $, Dairy Wellness Profit Index - DWP$).</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Disease resistance is the host's inherited ability to block, control, or clear pathogen infection.",
        "Disease tolerance allows normal production despite harboring pathogen burdens without clinical disease.",
        "Major Histocompatibility Complex (MHC) on cattle chromosome 23 is known as BoLA (Bovine Leukocyte Antigen).",
        "BoLA-DRB3 locus alleles correlate with resistance to Bovine Leukemia Virus and lower somatic cell count.",
        "In chickens, the B21 haplotype on microchromosome 16 confers genetic resistance to Marek's Disease lymphoma.",
        "Chicken B19 haplotype confers extreme susceptibility to Marek's Disease with > 80% flock mortality.",
        "Somatic Cell Score [SCS = log2(SCC/100,000) + 3] serves as the primary genetic indicator for mastitis resistance.",
        "Genetic correlation between milk yield and mastitis is unfavorably positive (rg = +0.25), requiring selection index balance.",
        "Sheep scrapie prion resistance is governed by PrP codons 136, 154, and 171; ARR confers resistance, VRQ susceptibility.",
        "Zebu cattle resist Rhipicephalus microplus ticks through dermal histology, grooming, and histamine hypersensitivity.",
        "Fecal Egg Count (FEC) and FAMACHA eye scores are the primary selection tools for barber's pole worm resistance in sheep."
    ],
    "tables": [
        {
            "title": "Genetic Basis of Disease Resistance in Major Livestock and Poultry Species",
            "headers": ["Pathogen / Disease", "Host Species", "Genetic Locus / Marker", "Resistant Genotype / Haplotype", "Susceptible Genotype"],
            "rows": [
                ["Marek's Disease (MDV)", "Poultry (Chicken)", "MHC Class I / IV (B-complex)", "B21 haplotype (low lymphoma)", "B19 haplotype (> 80% mortality)"],
                ["Classical Scrapie (Prion)", "Sheep (Ovine)", "Prion Protein (PrP) codons 136/154/171", "ARR / ARR (fully immune)", "VRQ / VRQ (extremely susceptible)"],
                ["Clinical Mastitis", "Dairy Cattle", "BoLA-DRB3 / SCS polygenic", "BoLA-DRB3*16 / Low SCS breeding value", "High SCS breeding values"],
                ["Cattle Tick (R. microplus)", "Bovine (Cattle)", "Taurine vs Indicine genome", "Bos indicus (Gir, Sahiwal, Brahman)", "Bos taurus (Holstein, Angus)"],
                ["Post-weaning Edema Disease", "Swine (Pig)", "FUT1 (F18 receptor locus)", "AA genotype (receptor negative)", "GG genotype (adherent receptor)"],
                ["Barber's Pole Worm (Haemonchus)", "Sheep & Goats", "Polygenic / Th2 cytokine cluster", "Garole, Red Maasai (Low FEC, FAMACHA 1)", "Commercial fine-wool breeds (High FEC)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In field sheep health management, veterinary practitioners encounter widespread anthelmintic resistance to benzimidazoles and ivermectin. "
        "Veterinarians implement <b>Targeted Selective Treatment (TST) using the FAMACHA system</b>: "
        "only sheep displaying clinical mucosal pallor (FAMACHA scores 4 and 5) are dosed with anthelmintics. "
        "Simultaneously, ewes with consistently high Fecal Egg Counts (FEC) are <b>systematically culled from the breeding flock</b>, "
        "while rams demonstrating natural resistance (low FEC, FAMACHA score 1–2) are retained as seedstock sires, progressively breeding natural nematode resistance into the flock."
    ),
    "tags": ["Disease Resistance", "MHC", "BoLA", "B-Complex", "Marek's Disease", "Scrapie", "PrP", "Mastitis", "SCS", "FAMACHA", "Ticks"]
}

topics["u3-t24"] = {
    "summary": "Canine and feline breeds are systematized by international kennel clubs into functional utility groups, anchored by rigorous breed standards, official pedigree sheets, and conservation of indigenous Indian hound and working breeds.",
    "desc": (
        "<b>KENNEL CLUB RECOGNITION AND BREED STANDARDS</b><br>"
        "A <b>Breed Standard</b> is the official written blueprint issued by recognized kennel governing bodies—such as the <b>F&eacute;d&eacute;ration Cynologique Internationale (FCI)</b> and the <b>Kennel Club of India (KCI)</b>—describing the ideal physical conformation, height at withers, weight, coat texture, colour, gait, and typical temperament of a specific pure breed.<br><br>"
        "<b>FCI / KCI CANINE BREED CLASSIFICATION (10 FUNCTIONAL GROUPS)</b><br>"
        "<ol>"
        "<li><b>Group 1: Sheepdogs and Cattledogs (Except Swiss Cattle Dogs):</b> German Shepherd Dog (GSD), Belgian Malinois, Border Collie, Rough Collie. Working herding instinct, high trainability.</li>"
        "<li><b>Group 2: Pinscher and Schnauzer - Molossoid and Swiss Mountain:</b> Doberman Pinscher, Rottweiler, Boxer, Great Dane, Mastiff, Saint Bernard. Guarding, protection, muscular power.</li>"
        "<li><b>Group 3: Terriers:</b> Bull Terrier, Fox Terrier, Scottish Terrier. High gameness, historically bred to dig out burrowing rodents and vermin.</li>"
        "<li><b>Group 4: Dachshunds:</b> Standard, Miniature, and Kaninchen (smooth, long-haired, and wire-haired). Specialized badger hunting with elongated spine and short limbs (chondrodysplasia).</li>"
        "<li><b>Group 5: Spitz and Primitive Types:</b> Siberian Husky, Alaskan Malamute, Pomeranian, Chow Chow, Samoyed, Basenji, <b>Indian Spitz</b>. Wedge-shaped head, erect prick ears, curled tail over back, thick double coat.</li>"
        "<li><b>Group 6: Scenthounds and Related Breeds:</b> Beagle, Bloodhound, Basset Hound, Dalmatian. Phenomenal olfactory tracking capacity, pendulous ears, deep melodious bark.</li>"
        "<li><b>Group 7: Pointing Dogs:</b> English Pointer, German Shorthaired Pointer, Irish Setter. Stands rigid and 'points' with muzzle and raised paw toward hidden game birds.</li>"
        "<li><b>Group 8: Retrievers - Flushing Dogs - Water Dogs:</b> Labrador Retriever, Golden Retriever, Cocker Spaniel, English Springer Spaniel. Gentle 'soft mouth' to retrieve shot waterfowl undamaged.</li>"
        "<li><b>Group 9: Companion and Toy Dogs:</b> Pug, Shih Tzu, Chihuahua, Cavalier King Charles Spaniel, Poodle. Selected strictly for companion behavior, lapdog docility, and miniature size.</li>"
        "<li><b>Group 10: Sighthounds:</b> Greyhound, Whippet, Afghan Hound, Saluki, and indigenous Indian hounds. Hunt by sight and blistering speed; deep chest, tucked abdomen, dolichocephalic skull.</li>"
        "</ol><br>"
        "<b>PREMIER INDIGENOUS CANINE BREEDS OF INDIA</b><br>"
        "India possesses magnificent, hardy indigenous dog breeds adapted to semi-arid tropical climates, recognized by KCI and ICAR-NBAGR:"
        "<ul>"
        "<li><b>Mudhol Hound (Caravan Hound):</b> Native to Bagalkot and Vijayapura (Karnataka) and Maharashtra. Feathered or smooth-coated sighthound; unmatched sprinting speed, stamina, and hunting vision. Inducted into Indian Army and paramilitary border patrol.</li>"
        "<li><b>Rajapalayam (Polgar Hound):</b> Native to Virudhunagar district (Tamil Nadu). Aristocratic boar-hound; pristine milky-white short coat, pink nose, golden eyes, and deep chest. Guarded royal Nayak palaces.</li>"
        "<li><b>Chippiparai & Kanni:</b> Native to southern Tamil Nadu (Madurai, Tirunelveli). Sleek, fawn or black-and-tan sighthounds bred for hare coursing; resilient against ticks and heat.</li>"
        "<li><b>Combai (Indian Bear Hound):</b> Heavy-jawed, red-brown or tan mastiff-type with black muzzle; fierce loyalty, boar hunting, and estate defense.</li>"
        "<li><b>Himalayan Sheepdog (Gaddi Kutta / Bakharwal Dog):</b> Massive mountain mastiff with dense double coat; guards migratory sheep flocks against leopards and snow wolves in Himachal and J&K.</li>"
        "<li><b>Jonangi:</b> Andhra Pradesh; celebrated for hunting crabs and fish in shallow waters and unique somersaulting gait.</li>"
        "</ul><br>"
        "<b>THE CANINE PEDIGREE SHEET</b><br>"
        "An official legal certificate issued by KCI containing: (a) Registered Name of Dog, (b) Microchip Number (15-digit ISO 11784/11785 transponder), (c) Date of Birth and Sex, (d) Color and Markings, (e) 3 to 5 generation ancestral lineage (Sire, Dam, Grandparents, Great-grandparents), (f) Championship Titles earned (e.g., Ch., Gr.Ch.), and (g) Health clearances (Hip Dysplasia OFA score, DNA PRA clearance)."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Canine Cephalic Index & Genetic Skeletal Conformations:</b><br>"
        "In university exams, classify dog skulls and associated pathologies using the <b>Cephalic Index (CI)</b>:"
        "<code>CI = (Skull Width / Skull Length) &times; 100</code>."
        "<ul>"
        "<li><b>Dolichocephalic (CI &lt; 75):</b> Long, narrow muzzle, elongated skull (e.g., Greyhound, Mudhol Hound, Afghan Hound, Whippet). Anatomically optimized for panoramic 270&deg; field of vision during high-speed sighthound chases.</li>"
        "<li><b>Mesocephalic (CI 75–80):</b> Balanced proportions (e.g., German Shepherd, Labrador Retriever, Golden Retriever).</li>"
        "<li><b>Brachycephalic (CI &gt; 80):</b> Severely compressed, shortened facial skeleton with retroflexed maxilla (e.g., Pug, Bulldog, Shih Tzu, Boxer). "
        "Driven by mutations in the <i>DVL2</i> and <i>BMP3</i> genes. Triggers <b>Brachycephalic Obstructive Airway Syndrome (BOAS)</b>: stenotic nares, elongated soft palate, everted laryngeal saccules, and hypoplastic trachea.</li>"
        "<li><b>Chondrodysplasia in Dachshunds / Bassets:</b> Caused by an expressed retrocopy of the <i>FGF4</i> gene on chromosome 18, leading to premature calcification of long bone growth plates and disproportionate dwarfism.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "A Breed Standard is an official blueprint describing ideal conformation, gait, and temperament.",
        "FCI and Kennel Club of India (KCI) classify dogs into 10 distinct functional utility groups.",
        "Group 1 contains Sheepdogs and Cattledogs (German Shepherd, Belgian Malinois, Border Collie).",
        "Group 9 contains Companion and Toy Dogs (Pug, Chihuahua, Shih Tzu, Toy Poodle).",
        "Group 10 contains Sighthounds hunting by sight and speed (Greyhound, Whippet, Mudhol Hound).",
        "Mudhol Hound (Karnataka) is an elite indigenous sighthound inducted into the Indian Army border patrol.",
        "Rajapalayam of Tamil Nadu is a majestic royal boar-hound with pure white coat and pink nose.",
        "Combai is an indigenous bear-hunting mastiff of Tamil Nadu with high jaw strength.",
        "Gaddi Kutta (Himalayan Sheepdog) is a massive livestock guardian protecting against leopards.",
        "An official KCI pedigree sheet traces 3–5 generations of lineage with 15-digit microchip identification.",
        "Brachycephalic breeds (Pug, Bulldog) carry DVL2 mutations predisposing them to BOAS respiratory distress."
    ],
    "tables": [
        {
            "title": "Characteristics of Premier Indigenous Canine Breeds of India",
            "headers": ["Indigenous Breed", "Native State / Region", "Functional Utility Type", "Distinguishing Physical Conformation", "Key Temperamental Traits"],
            "rows": [
                ["Mudhol Hound", "Karnataka (Mudhol / Bagalkot)", "Sighthound (Hunting / Guard)", "Aerodynamic tucked abdomen, long muzzle, whip tail", "High speed, keen sight, independent, aloof with strangers"],
                ["Rajapalayam", "Tamil Nadu (Virudhunagar)", "Boar Hound / Estate Guard", "Pristine white coat, flesh/pink nose, golden eyes, deep chest", "Fiercely loyal to single master, fearless, territorial"],
                ["Chippiparai", "Tamil Nadu (Madurai/Periyar)", "Sighthound (Hare coursing)", "Extremely lean, fawn/grey coat, arched loin, light build", "Tireless endurance, agile sprinter, docile household pet"],
                ["Combai", "Tamil Nadu (Theni/Madurai)", "Mastiff / Bear Hound", "Reddish-brown coat, black mask/muzzle, powerful jaws", "Extreme tenacity, pain tolerance, aggressive guard instinct"],
                ["Gaddi Kutta (Himalayan)", "Himachal Pradesh & J&K", "Livestock Guardian Dog", "Massive robust frame, heavy bones, dense insulating double coat", "Fearless against predators (snow leopard), vigilant at night"],
                ["Jonangi", "Andhra Pradesh (Kolleru lake)", "Primitive Working Dog", "Short smooth coat, forehead wrinkles, somersault hunting gait", "Expert fish/crab catcher, docile, unique yodel vocalization"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "Small animal practitioners routinely conduct <b>Pre-Breeding Health Screening</b> on registered purebred dogs. "
        "Veterinarians must never certify breeding fitness based purely on pedigree papers. "
        "They must enforce mandatory clinical screenings: (a) Radiographic evaluation for <b>Hip and Elbow Dysplasia</b> (OFA / BVA scoring) in German Shepherds and Labradors, "
        "(b) DNA testing for Progressive Retinal Atrophy (PRA) and Exercise Induced Collapse (EIC), and "
        "(c) Clinical grading for <b>Patellar Luxation</b> in toy breeds (Pugs, Pomeranians) to prevent propagating crippling hereditary orthopedic defects into future litters."
    ),
    "tags": ["Canine Breeds", "Kennel Club of India", "KCI", "Breed Standards", "Mudhol Hound", "Rajapalayam", "Pedigree Sheet", "Brachycephalic", "BOAS"]
}

topics["u3-t25"] = {
    "summary": "Breeding management in companion dogs and cats requires precise estrous staging via vaginal cytology and serial progesterone assays, alongside diligent care during pregnancy, whelping, and the neonatal phase.",
    "desc": (
        "<b>I. REPRODUCTIVE CYCLE AND ESTROUS PHASES IN THE BITCH (CANINE)</b><br>"
        "The domestic bitch is <b>non-seasonal, monoestrous</b>, exhibiting estrous cycles typically once every 6 to 8 months (average interval 7 months):"
        "<ol>"
        "<li><b>1. Proestrus (Average 9 days, range 3–17 days):</b>"
        "<br>&bull; <i>Clinical Signs:</i> Marked turgid vulvar swelling, serosanguinous (bloody) vaginal discharge resulting from diapedesis of erythrocytes across endometrial capillaries under rising estrogen."
        "<br>&bull; <i>Behavior:</i> Attracts male dogs but fiercely rejects mounting/copulation (tucks tail, growls, or sits down).</li>"
        "<li><b>2. Estrus (Average 9 days, range 3–21 days) — Period of Receptivity:</b>"
        "<br>&bull; <i>Clinical Signs:</i> Vulva becomes softer and flaccid; vaginal discharge turns from bloody to straw-colored or salmon-pink."
        "<br>&bull; <i>Behavior:</i> Receptive to mating; displays <b>'Flagging'</b> (deviates tail to one side and elevates perineum upon tactile stimulation of the rump).</li>"
        "<li><b>3. Diestrus / Metestrus (Average 60 days in non-pregnant, 63 days in pregnant bitch):</b>"
        "<br>&bull; Begins abruptly when the bitch refuses to mate. Progesterone is secreted by the corpora lutea whether pregnant or not. "
        "<br>&bull; If non-pregnant, this prolonged progesterone dominance can culminate in <b>Overt Pseudopregnancy (False Pregnancy / Pseudocyesis)</b> or predispose to <b>Pyometra</b> under cystic endometrial hyperplasia (CEH).</li>"
        "<li><b>4. Anestrus (Average 3 to 5 months):</b>"
        "<br>&bull; Phase of reproductive quiescence; baseline estrogen and progesterone.</li>"
        "</ol><br>"
        "<b>OVULATION TIMING: THE CORNIFICATION INDEX & PROGESTERONE ASSAY</b><br>"
        "Unlike other mammals, <b>the bitch ovulates immature primary oocytes</b> at LH peak + 2 days, which require an additional <b>48 to 72 hours in the oviduct to undergo meiosis II</b> to become fertilizable secondary oocytes. Fertilization window occurs 4 to 6 days after the LH surge!"
        "<ul>"
        "<li><b>Exfoliative Vaginal Cytology:</b>"
        "<br>&bull; <i>Proestrus:</i> Parabasal and intermediate cells, abundant red blood cells (RBCs), neutrophils, and background mucus."
        "<br>&bull; <i>Estrus:</i> Dominated by <b>> 80–90% cornified superficial cells</b> (large, flat, angular polygonal cells with pyknotic nuclei or anuclear squames). RBCs decline; neutrophils are completely absent!"
        "<br>&bull; <i>Diestrus:</i> Sudden reappearance of neutrophils and sudden drop in superficial cells (> 50% shift to parabasal and intermediate cells within 24 hours).</li>"
        "<li><b>Quantitative Serum Progesterone Assay (Gold Standard):</b>"
        "<br>&bull; Baseline / Proestrus: <code>&lt; 1.0 ng/ml</code>."
        "<br>&bull; LH Surge: <code>1.5 to 2.5 ng/ml</code>."
        "<br>&bull; Ovulation: <code>4.0 to 10.0 ng/ml</code> (typically ~5.0 ng/ml)."
        "<br>&bull; <b>Optimal Breeding / AI Window:</b> 2 to 3 days post-ovulation, when progesterone is <b>10 to 20 ng/ml</b>.</li>"
        "</ul><br>"
        "<b>GESTATION AND WHELPING CARE IN BITCHES</b><br>"
        "<ul>"
        "<li><b>Gestation Length:</b> <b>63 days</b> from ovulation (range 58 to 68 days from breeding).</li>"
        "<li><b>Pregnancy Diagnosis:</b> Abdominal palpation (Day 28–30, discrete spherical ampullae); B-mode Ultrasonography (Day 25+; visualizes heartbeat); Radiography (Day 45+; fetal skeletal calcification allows exact puppy count).</li>"
        "<li><b>Whelping Predictor:</b> A sharp <b>drop in rectal body temperature below 99&deg;F (37.2&deg;C)</b> occurs 12 to 24 hours prior to Stage II labor, caused by rapid luteolysis and progesterone collapse.</li>"
        "</ul><br>"
        "<b>II. FELINE REPRODUCTION (THE QUEEN)</b><br>"
        "The domestic cat is <b>seasonally polyestrous</b> and an <b>INDUCED (REFLEX) OVULATOR</b>:"
        "<ul>"
        "<li>Ovulation occurs only if coitus takes place. Penile spines of the tomcat induce neural stimulation of the queen's vagina, sending signals through the spinal cord to the hypothalamus, releasing a GnRH surge and subsequent LH peak.</li>"
        "<li>Estrus lasts 6 to 10 days, repeating every 2 to 3 weeks if not bred. Queen shows intense lordosis, rolling, rubbing, and vociferous 'calling'.</li>"
        "<li>Gestation in queen: <b>63 to 65 days</b>.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>The Copulatory Tie & Frozen Semen AI Nuances in Canines:</b><br>"
        "In university exams, detail the physiological mechanism of canine mating:"
        "<ul>"
        "<li><b>The Copulatory Tie (Coital Lock):</b> Mating encompasses two stages. In the second stage, the male's <b>bulbus glandis</b> engorges with venous blood, locking inside the bitch's constrictor vestibuli muscles. The male steps one hindleg over, turning to face opposite directions for <b>15 to 30 minutes</b>. "
        "Veterinarians must emphasize: <i>Never forcefully separate tied dogs</i>; doing so causes penile fracture or severe vaginal laceration!</li>"
        "<li><b>Frozen Semen AI:</b> Because frozen-thawed canine sperm survives only 12–24 hours (vs 4–5 days for fresh semen), vaginal AI results in poor conception. Sires evaluated with frozen semen require <b>Transcervical Insemination (TCI) using an endoscope</b> or surgical AI to deposit semen directly into the uterine horns at precisely 5 to 6 days after the LH surge.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "The bitch is non-seasonal and monoestrous, cycling on average every 6 to 8 months.",
        "Proestrus lasts ~9 days, characterized by vulvar swelling, bloody discharge, and refusal to mate.",
        "Estrus lasts ~9 days, marked by straw-colored discharge, vulvar softening, and tail flagging.",
        "Bitches ovulate immature primary oocytes requiring 48-72 hours in the oviduct to reach meiosis II.",
        "Vaginal cytology during estrus shows > 80-90% cornified superficial cells with pyknotic or absent nuclei.",
        "Ovulation occurs when serum progesterone reaches 4.0 to 10.0 ng/ml (average 5.0 ng/ml).",
        "Optimal breeding window is 2-3 days post-ovulation when serum progesterone reaches 10-20 ng/ml.",
        "Gestation in the bitch is 63 days; temperature drop below 99°F (37.2°C) predicts whelping within 24 hours.",
        "The queen (cat) is seasonally polyestrous and an induced (reflex) ovulator triggered by coitus.",
        "The copulatory tie in dogs lasts 15-30 minutes due to engorgement of the bulbus glandis.",
        "Prolonged diestrous progesterone in non-pregnant bitches predisposes to pseudopregnancy and pyometra."
    ],
    "tables": [
        {
            "title": "Phases of the Canine Estrous Cycle: Hormonal, Cytological, and Behavioral Markers",
            "headers": ["Estrous Phase", "Average Duration", "Predominant Hormone", "Vaginal Cytology Picture", "Bitch Behavioral Response"],
            "rows": [
                ["Proestrus", "9 days (3–17 d)", "Estrogen rising", "Parabasal, intermediate cells, abundant RBCs, mucus", "Attracts males; fiercely rejects mating"],
                ["Estrus", "9 days (3–21 d)", "Estrogen falling; Progesterone rising", "> 80–90% cornified superficial cells; zero neutrophils", "Receptive; flags tail; allows copulatory tie"],
                ["Diestrus (Metestrus)", "60 days", "Progesterone dominant (> 10 ng/ml)", "Abrupt shift (< 50% superficial, influx of neutrophils)", "Aggressively refuses male; settles into nesting"],
                ["Anestrus", "3–5 months", "Baseline basal levels", "Scanty parabasal and small intermediate cells only", "Sexually completely quiescent; indifferent to males"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "A common emergency presented to small animal clinics is <b>Canine Dystocia (Obstructed Labor)</b>. "
        "Veterinarians diagnose secondary uterine inertia or obstructive dystocia if: "
        "(a) Strong, active abdominal contractions continue for > 30 minutes without pup expulsion, "
        "(b) > 2 to 3 hours elapse between successive pups, or "
        "(c) Purulent or greenish-black (uteroverdin) lochia is discharged without a pup born within 2 hours. "
        "After checking calcium and glucose levels and verifying unobstructed birth canal on radiograph, "
        "the veterinarian administers 10% Calcium Gluconate followed by low-dose Oxytocin (1–5 IU IM); if medical management fails, an immediate <b>Emergency Cesarean Section (C-Section)</b> is performed."
    ),
    "tags": ["Canine Reproduction", "Vaginal Cytology", "Progesterone Assay", "Whelping", "Copulatory Tie", "Queen", "Induced Ovulation", "Dystocia"]
}

topics["u3-t26"] = {
    "summary": "Avian breeding management for companion birds in India covers cage/aviary design, sexual dimorphism, balanced seed-soft food nutrition, nest box management, and statutory adherence to the Wildlife Protection Amendment Act 2022.",
    "desc": (
        "<b>POPULAR PET BIRD SPECIES IN INDIA</b><br>"
        "Aviculture in India centers on four major domesticated companion species:"
        "<ol>"
        "<li><b>Budgerigar (Budgie - <i>Melopsittacus undulatus</i>):</b>"
        "<br>&bull; Small Australian parakeet; highly social, hardy, and prolific."
        "<br>&bull; <i>Sexual Dimorphism:</i> Differentiated by the color of the <b>cere</b> (fleshy area above the beak enclosing nostrils):"
        "<br>&nbsp;&nbsp;&bull; <b>Adult Male:</b> Smooth, bright royal blue or purplish cere."
        "<br>&nbsp;&nbsp;&bull; <b>Adult Female:</b> Crusty, hypertrophied, tan-to-dark brown cere (during breeding readiness) or pale chalky blue/white (non-breeding).</li>"
        "<li><b>Cockatiel (<i>Nymphicus hollandicus</i>):</b>"
        "<br>&bull; Medium-sized crested Australian cockatoo family member."
        "<br>&bull; <i>Sexual Dimorphism (Normal Grey):</i>"
        "<br>&nbsp;&nbsp;&bull; <b>Adult Male:</b> Brilliant bright yellow facial mask with vibrant, fiery orange circular cheek patches; solid dark grey tail feathers."
        "<br>&nbsp;&nbsp;&bull; <b>Adult Female:</b> Duller, greyish-yellow face with muted orange cheek patches; distinct horizontal yellow barring/stripes on the underside of tail feathers.</li>"
        "<li><b>Lovebirds (<i>Agapornis</i> species):</b>"
        "<br>&bull; Small, compact African parrots (Peach-faced, Fischer's, Masked lovebirds). Monomorphic; exact sexing requires <b>DNA feather sexing</b> or pelvic bone palpation (females have wider, flexible pubic distance > 1 cm).</li>"
        "<li><b>Finches:</b>"
        "<br>&bull; <b>Zebra Finch (<i>Taeniopygia guttata</i>):</b> Male possesses distinctive chestnut ear patches, zebra-like horizontal black/white throat barring, and white-spotted chestnut flank stripes. Females are uniformly grey without flank/cheek coloration."
        "<br>&bull; <b>Bengalese (Society) Finch & Gouldian Finch:</b> Peaceful colonial breeders; Bengalese finches are universally celebrated as exceptional foster parents for rearing delicate exotic chicks.</li>"
        "</ol><br>"
        "<b>HOUSING, AVIARY HYGIENE, AND NEST BOX DESIGN</b><br>"
        "<ul>"
        "<li><b>Caging Dimensions:</b> Must provide ample horizontal flight space (birds fly horizontally, not vertically). Minimum flight cage: 60 &times; 45 &times; 45 cm for a pair of budgies. Perches should be made of variable-diameter natural branches (guava, neem) to exercise foot tendons and prevent <b>Pododermatitis (Bumblefoot)</b>.</li>"
        "<li><b>Nest Boxes:</b>"
        "<br>&bull; Budgerigars: Wooden nest box (20 &times; 15 &times; 15 cm) with a circular entry hole (4 cm) and a <b>concave hollow bottom</b> (prevents eggs from rolling and prevents 'splayed legs' in growing chicks)."
        "<br>&bull; Cockatiels: Larger vertical wooden box (30 &times; 25 &times; 25 cm) with coarse pine wood shavings."
        "<br>&bull; Finches: Woven wicker baskets or wooden finch nest boxes with dry Bermuda grass and coconut coir.</li>"
        "</ul><br>"
        "<b>AVIAN NUTRITION AND BREEDING DIET</b><br>"
        "All-seed diets (millet-only) cause chronic malnutrition, hypovitaminosis A, and egg binding. A balanced breeding diet requires:"
        "<ul>"
        "<li><b>Seed Mixture:</b> French millet, foxtail millet (kangni), canary seed, sunflower seeds (sparingly for cockatiels due to high fat).</li>"
        "<li><b>Sprouted Seeds & Greens:</b> Soaked and sprouted green gram (moong), wheat, and fresh washed greens (coriander, spinach, fenugreek).</li>"
        "<li><b>Egg Food (Soft Food):</b> Hard-boiled grated egg mixed with breadcrumbs or commercial egg food to supply concentrated protein (18–20%) and essential amino acids (methionine, lysine) for chick growth.</li>"
        "<li><b>Mineral & Calcium Supplementation:</b> <b>Cuttlefish bone</b> and mineral grit blocks must be available perpetually. Critical for eggshell calcification and preventing hypocalcemic uterine inertia (egg binding).</li>"
        "</ul><br>"
        "<b>INCUBATION, HATCHING, AND REARING PARAMETERS</b><br>"
        "<ul>"
        "<li><b>Budgerigars:</b> Clutch size 4–6 eggs; incubation period <b>18 days</b>; altricial chicks; fledge at 4–5 weeks.</li>"
        "<li><b>Cockatiels:</b> Clutch size 4–5 eggs; incubation period <b>19–21 days</b>; both parents incubate; fledge at 5–6 weeks.</li>"
        "<li><b>Finches:</b> Clutch size 3–6 eggs; incubation period <b>14–16 days</b>; fledge at 3 weeks.</li>"
        "</ul><br>"
        "<b>INDIAN STATUTORY REGULATION: THE WILD LIFE (PROTECTION) ACT 1972 (AMENDMENT 2022)</b><br>"
        "Captive pet bird breeding in India is strictly regulated under the amended <b>Wild Life (Protection) Act, 1972 (enforced from April 2023)</b>:"
        "<ul>"
        "<li>All indigenous Indian wild bird species (e.g., Rose-ringed Parakeet / Alexandrine Parakeet / Munias) are protected under Schedule I & II; their trapping, trade, or domestic caging is a <b>non-bailable criminal offense</b>!</li>"
        "<li>Exotic companion birds listed under <b>CITES Appendices (Schedule IV of WPA 2022)</b>—including African Grey Parrots and certain exotic cockatoos—require <b>Mandatory Online Registration of possession and captive breeding stock on the Ministry's PARIVESH Portal</b>.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Pathophysiology and Management of Egg Binding (Dystocia) in Pet Birds:</b><br>"
        "In veterinary board examinations, detail this life-threatening emergency:"
        "<ul>"
        "<li><b>Etiology:</b> Hypocalcemia (dietary calcium deficiency depleting uterine smooth muscle reserves), oversized/misshapen eggs, obesity, breeding at too young an age, or cold room temperatures.</li>"
        "<li><b>Clinical Presentation:</b> Fluffed feathers, lethargy, wide-based stance on cage floor, continuous tail bobbing, tenesmus (straining), and dyspnea due to oviductal egg compressing the caudal air sacs.</li>"
        "<li><b>Emergency Treatment Protocol:</b>"
        "<br>1. Immediate warmth (humid incubator at <b>30–32&deg;C</b> with 60–70% humidity) to relax smooth muscles."
        "<br>2. <b>Calcium Sandoz (10% Calcium Borogluconate)</b> administered SC/IM (50–100 mg/kg) alongside Vitamin D3."
        "<br>3. Gentle cloacal application of warm sterile liquid paraffin or water-soluble lubricant."
        "<br>4. If oviposition does not occur, perform <b>Ovocentesis</b>: aspirate egg contents through a large-gauge needle via cloacal speculum, gently collapse the shell inward, and remove shell fragments with atraumatic forceps.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Common pet birds in India include Budgerigars, Cockatiels, Lovebirds, and Zebra Finches.",
        "Budgerigar males have bright blue/purple ceres; females have crusty tan/brown ceres during breeding.",
        "Normal grey cockatiel males display bright yellow faces and fiery orange cheek patches without tail barring.",
        "Budgerigar nest boxes require a concave bottom to prevent egg scattering and chick splayed legs.",
        "All-seed diets cause severe hypovitaminosis A and hypocalcemia, leading to fatal egg binding.",
        "Egg food (boiled egg + breadcrumbs) supplies 18–20% crude protein essential for rearing altricial chicks.",
        "Incubation periods: Finches (14–16 days), Budgerigars (18 days), Cockatiels (19–21 days).",
        "Indigenous Indian wild birds (Rose-ringed parakeets) cannot be caged; it is a crime under WPA 1972.",
        "Exotic pet bird breeders must register CITES-listed species on the Government of India's PARIVESH portal.",
        "Egg binding is treated with a humid incubator (30-32°C), injectable Calcium Borogluconate, and ovocentesis.",
        "Variable-diameter natural perches prevent avian pododermatitis (bumblefoot)."
    ],
    "tables": [
        {
            "title": "Breeding Biological Parameters of Common Pet Bird Species Kept in India",
            "headers": ["Avian Species", "Scientific Name", "Clutch Size", "Incubation Period", "Fledging Age", "Primary Sexual Dimorphism Marker"],
            "rows": [
                ["Budgerigar", "Melopsittacus undulatus", "4 to 6 eggs", "18 days", "28 to 35 days", "Cere color: Royal blue in adult males; crusty brown in females"],
                ["Cockatiel", "Nymphicus hollandicus", "4 to 5 eggs", "19 to 21 days", "35 to 42 days", "Bright yellow face & plain grey tail in males; barred tail in females"],
                ["Lovebird", "Agapornis roseicollis", "4 to 6 eggs", "21 to 23 days", "40 to 45 days", "Monomorphic; confirmed via DNA feather sexing / pelvic spacing"],
                ["Zebra Finch", "Taeniopygia guttata", "3 to 6 eggs", "14 to 16 days", "18 to 21 days", "Chestnut cheek patch & zebra throat stripes present exclusively in males"],
                ["Society (Bengalese) Finch", "Lonchura domestica", "4 to 7 eggs", "15 to 16 days", "20 to 24 days", "Monomorphic; singing & courtship display unique to males"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "A critical condition presented to avian veterinarians is <b>Splayed Legs in hand-reared or nestling budgies</b>. "
        "Occurs when smooth, slippery, flat nest box bottoms lack adequate concave indentation or nesting substrate, "
        "forcing the growing chick's femurs to luxate laterally under maternal brooding weight. "
        "Veterinarians correct this in chicks under 2 weeks of age by fashioning a <b>Figure-8 Hobble Splint</b> using soft adhesive porous tape or surgical foam, "
        "realigning legs to normal anatomical shoulder width for 7 to 10 days while long bones undergo rapid mineralization."
    ),
    "tags": ["Pet Birds", "Aviculture", "Budgerigar", "Cockatiel", "Finch", "Cere Color", "Egg Binding", "WPA 2022", "PARIVESH", "Splayed Legs"]
}

topics["u3-t27"] = {
    "summary": "Small wildlife populations in fragmented habitats are threatened by the extinction vortex; calculating Effective Population Size (Ne) through demographic formulas guides conservation genetics to prevent fatal loss of heterozygosity.",
    "desc": (
        "<b>POPULATION DYNAMICS IN WILD SPECIES</b><br>"
        "Wildlife population abundance is governed by four primary demographic parameters: <b>Births (B), Deaths (D), Immigrations (I), and Emigrations (E)</b>: "
        "<code>N_{t+1} = N_t + (B - D) + (I - E)</code>. "
        "When habitat destruction and poaching isolate populations into small fragments, populations lose demographic buffering and enter the <b>Small Population Paradigm</b>.<br><br>"
        "<b>THE EXTINCTION VORTEX</b><br>"
        "Small populations are sucked into a self-reinforcing downward spiral termed the <b>Extinction Vortex</b>:"
        "<ul>"
        "<li><b>Habitat Fragmentation & Poaching</b> &rarr; Population drops below critical threshold.</li>"
        "<li><b>Inbreeding Accumulates Rapidly & Genetic Drift Accelerates</b> &rarr; Loss of rare alleles and drastic decline in genome-wide heterozygosity.</li>"
        "<li><b>Inbreeding Depression Manifests</b> &rarr; Reduced sperm motility, deformed offspring, embryonic death, poor cub survival, and loss of disease immunity.</li>"
        "<li><b>Demographic & Environmental Stochasticity</b> &rarr; Skewed birth sex ratios, annual droughts, and localized epidemic outbreaks wipe out remaining individuals, driving the population to extinction!</li>"
        "</ul><br>"
        "<b>CONCEPT OF EFFECTIVE POPULATION SIZE (Ne)</b><br>"
        "Formulated by <b>Sewall Wright (1931)</b>, the <b>Effective Population Size (Ne)</b> is defined as the size of an idealized, randomly mating population (with equal numbers of males and females and Poisson distribution of family size) that would experience the same rate of inbreeding (<code>&Delta;F</code>) or the same rate of random genetic drift as the actual observed wild population.<br><br>"
        "<b>Crucial Insight:</b> In wild and captive populations, <b>Ne is almost always significantly smaller than the total census count (N)</b> (typically <code>Ne / N &approx; 0.10 to 0.30</code>).<br><br>"
        "<b>MATHEMATICAL FORMULAS GOVERNING Ne</b><br>"
        "<ol>"
        "<li><b>1. Skewed Breeding Sex Ratio (Unequal Numbers of Males and Females):</b><br>"
        "<code>N_e = (4 &times; N_m &times; N_f) / (N_m + N_f)</code><br>"
        "Where <code>N_m</code> is the number of breeding males, and <code>N_f</code> is the number of breeding females."
        "<br>&bull; <i>Exam Scoring Demonstration:</i> Consider a lion pride with 1 breeding dominant pride male and 99 females (Total Census <code>N = 100</code>):"
        "<br>&nbsp;&nbsp;<code>N_e = (4 &times; 1 &times; 99) / (1 + 99) = 396 / 100 = 3.96 &approx; 4 individuals!</code>"
        "<br>&bull; Even though 100 live lions exist, genetically the population behaves and accumulates inbreeding as if it contains only <b>4 animals</b>!</li>"
        "<li><b>2. Fluctuating Population Size Across Generations (Population Bottlenecks):</b><br>"
        "When population size fluctuates over <code>t</code> generations, <code>N_e</code> is governed by the <b>Harmonic Mean</b> (which is heavily skewed by the single lowest generation count!):<br>"
        "<code>1 / N_e = (1 / t) &times; [ (1 / N_1) + (1 / N_2) + ... + (1 / N_t) ]</code><br>"
        "A single generation of severe drought or poaching that shrinks a herd to 10 animals depresses the long-term <code>N_e</code> for decades, regardless of subsequent demographic recovery!</li>"
        "<li><b>3. Variance in Family Size (Unequal Reproductive Output):</b><br>"
        "<code>N_e = (4N - 2) / (V_k + 2)</code><br>"
        "Where <code>V_k</code> is the variance in the number of offspring left by parents."
        "<br>&bull; If every single pair of wild animals is managed to leave <b>exactly two breeding offspring</b> (<code>V_k = 0</code>), then <code>N_e &approx; 2N</code>! Equalizing family sizes doubles the effective population size.</li>"
        "</ol><br>"
        "<b>MINIMUM VIABLE POPULATION (MVP) AND FRANKLIN'S 50/500 RULE</b><br>"
        "<b>Minimum Viable Population (MVP)</b> is the smallest isolated population size having a 99% probability of persisting for 1,000 years despite stochastic shocks:"
        "<ul>"
        "<li><b>Ne = 50 (Short-Term Survival):</b> Limits inbreeding rate to <code>&Delta;F &le; 1%</code> per generation (<code>&Delta;F = 1 / [2 Ne] = 1/100 = 0.01</code>), avoiding catastrophic short-term inbreeding depression.</li>"
        "<li><b>Ne = 500 (Long-Term Evolutionary Potential):</b> Balances the loss of quantitative genetic variance due to drift against the creation of new genetic variance by mutation, preserving evolutionary adaptability.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Heterozygosity Loss & The Asirgarh Asiatic Lion Case Study:</b><br>"
        "In university exams, demonstrate mastery of conservation genetics through mathematical loss of heterozygosity:"
        "<ul>"
        "<li>Rate of decay of heterozygosity per generation: <code>H_t / H_0 = [ 1 - 1 / (2 N_e) ]^t &approx; e^{-(t / 2N_e)}</code>.</li>"
        "<li><b>Asiatic Lion (<i>Panthera leo persica</i>) of Gir National Park:</b>"
        "<br>&bull; By the early 20th century, excessive trophy hunting shrunk the global population to fewer than <b>20 surviving individuals</b> (a severe genetic bottleneck)."
        "<br>&bull; Today, although census numbers have recovered to > 670 lions through strict protection, whole-genome sequencing proves they exhibit <b>> 70% reduction in genetic diversity</b> compared to African lions."
        "<br>&bull; Clinical manifestations: High incidence of teratospermia (> 60% abnormal spermatozoa with folded tails and broken acrosomes), deformed cranial bifurcations, and extreme vulnerability to a single outbreak of <b>Canine Distemper Virus (CDV)</b>.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Small wildlife populations are threatened by the extinction vortex of inbreeding and genetic drift.",
        "Sewall Wright (1931) formulated Effective Population Size (Ne) as the genetic equivalent of an ideal population.",
        "In nature, Ne is almost always significantly smaller than census size N (typically Ne / N = 0.10 to 0.30).",
        "Unequal breeding sex ratios collapse Ne: Ne = (4 * Nm * Nf) / (Nm + Nf).",
        "A breeding ratio of 1 male to 99 females results in an Ne of only ~4 individuals.",
        "Fluctuating population size across generations makes Ne equal to the harmonic mean of generation sizes.",
        "A single generational bottleneck depresses long-term effective population size for generations.",
        "Equalizing family size (Vk = 0) maximizes effective population size, reaching Ne ≈ 2N.",
        "Franklin's 50/500 rule: Ne ≥ 50 prevents short-term inbreeding depression; Ne ≥ 500 maintains long-term evolution.",
        "Rate of heterozygosity loss per generation is ΔH = 1 / (2 Ne).",
        "Gir Asiatic lions suffered a severe genetic bottleneck (< 20 founders), resulting in high teratospermia."
    ],
    "tables": [
        {
            "title": "Impact of Skewed Breeding Sex Ratios on Effective Population Size (Ne) for Census Size N = 100",
            "headers": ["Breeding Males (N_m)", "Breeding Females (N_f)", "Total Census Count (N)", "Effective Population Size (N_e)", "Ratio N_e / N (%)", "Conservation Genetics Assessment"],
            "rows": [
                ["50", "50", "100", "100.0", "100.0%", "Ideal theoretical sex parity; zero drift inflation"],
                ["25", "75", "100", "75.0", "75.0%", "Mild skew; acceptable captive breeding structure"],
                ["10", "90", "100", "36.0", "36.0%", "Substantial loss of genetic variation (~64% loss)"],
                ["5", "95", "100", "19.0", "19.0%", "Dangerous bottleneck; rapid inbreeding accumulation"],
                ["2", "98", "100", "7.84", "7.84%", "Severe genetic crisis; behaves like ~8 animals"],
                ["1", "99", "100", "3.96", "3.96%", "Catastrophic collapse; immediate extinction vortex risk"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In wildlife safari parks and conservation reserves, wildlife veterinarians frequently observe <b>Cryptorchidism and High Cub Mortality</b> in inbred felids. "
        "Veterinarians manage genetic rescue through <b>Assisted Migration / Translocation</b>: "
        "introducing just <b>1 to 2 unrelated breeding individuals per generation</b> into an isolated, inbred wild reserve "
        "(the 'One-Migrant-per-Generation' rule) is sufficient to halt inbreeding depression (<code>m &times; N_e &ge; 1</code>) "
        "without disrupting local ecological adaptations."
    ),
    "tags": ["Wildlife Genetics", "Effective Population Size", "Ne", "Extinction Vortex", "50/500 Rule", "Asiatic Lion", "Bottleneck", "Harmonic Mean"]
}

topics["u3-t28"] = {
    "summary": "Wildlife conservation breeding combines studbook pedigree analysis, Mean Kinship pairing to minimize inbreeding, assisted reproductive technologies (semen cryopreservation, IVF, cloning), and structured reintroduction into natural habitats.",
    "desc": (
        "<b>ROLE OF CAPTIVE CONSERVATION BREEDING</b><br>"
        "When a wild species declines below its Minimum Viable Population in the wild, <b>Ex-situ Conservation Breeding</b> in accredited zoological parks becomes the final defense against extinction. "
        "Under the <b>Central Zoo Authority (CZA)</b> of India and the <b>IUCN Conservation Breeding Specialist Group (CBSG)</b>, zoos have evolved from public exhibitions into sophisticated scientific bio-repositories dedicated to producing genetically viable stock for eventual wild reintroduction.<br><br>"
        "<b>STUDBOOK MANAGEMENT AND THE MEAN KINSHIP CRITERION</b><br>"
        "To prevent inbreeding and preserve founder genetic diversity, captive breeding is regulated by <b>National and International Studbooks</b> using specialized biometrical software (<b>SPARKS, PopLink, PMx, and ZIMS</b>):"
        "<ul>"
        "<li><b>Mean Kinship (MK):</b>"
        "<br>&bull; The single most vital metric in captive breeding."
        "<br>&bull; Defined as the average coefficient of relationship between a specific captive individual and all other living individuals in the entire captive population (including itself)."
        "<br>&bull; <i>Breeding Rule:</i>"
        "<br>&nbsp;&nbsp;&bull; Animals with <b>LOW Mean Kinship</b> possess rare, under-represented founder alleles; they are given <b>highest breeding priority</b> to spread their rare genes."
        "<br>&nbsp;&nbsp;&bull; Animals with <b>HIGH Mean Kinship</b> have lineages over-represented in the studbook; their breeding is strictly restricted or contracepted!</li>"
        "<li><b>Pairing Strategy:</b> Mates are paired to: (a) Minimize the kinship between the pair (keeping progeny inbreeding <code>F &lt; 0.05</code>), and (b) Equalize founder representations across the population.</li>"
        "</ul><br>"
        "<b>ASSISTED REPRODUCTIVE TECHNOLOGIES (ART) IN WILDLIFE CONSERVATION</b><br>"
        "Where physical animal transport across international borders is dangerous, expensive, or blocked by quarantine, ART provides non-invasive genetic exchange:"
        "<ol>"
        "<li><b>Non-Invasive Endocrine Monitoring:</b>"
        "<br>&bull; Measuring fecal, urinary, or salivary hormone metabolites (estradiol-17&beta;, progesterone, testosterone, and cortisol) via Enzyme Immunoassays (EIA)."
        "<br>&bull; Allows stress-free tracking of estrous cycles, pregnancy diagnosis, and ovarian dormancy in wild tigers, rhinos, and elephants without chemical capture.</li>"
        "<li><b>Electroejaculation and Cryobanking:</b>"
        "<br>&bull; Transrectal electroejaculation under general anesthesia in wild carnivores, ungulates, and primates."
        "<br>&bull; <b>LaCONES (Laboratory for the Conservation of Endangered Species, CCMB Hyderabad):</b> India's premier wildlife biotechnology facility; houses a dedicated cryogenic gene bank of deep-frozen semen, embryos, and somatic cell lines from endangered Indian tigers, leopards, lions, blackbucks, and deer.</li>"
        "<li><b>Artificial Insemination (AI) in Wildlife:</b>"
        "<br>&bull; Successfully executed in Giant Pandas, Royal Bengal Tigers, Indian Leopards, and Cheetahs."
        "<br>&bull; Transcervical or laparoscopic intrauterine insemination using frozen-thawed semen.</li>"
        "<li><b>In-Vitro Fertilization & Interspecific Embryo Transfer (iET):</b>"
        "<br>&bull; Oocytes harvested post-mortem from accidentally killed endangered animals are matured, fertilized in vitro, and transferred into common domestic surrogate mothers (e.g., <b>Indian Gaur embryo transferred into a domestic Holstein cow</b>; Blackbuck embryo in a domestic goat).</li>"
        "<li><b>Somatic Cell Nuclear Transfer (SCNT / Cloning):</b>"
        "<br>&bull; Enucleating a domestic oocyte and fusing it with a cryopreserved somatic cell nucleus from an endangered or recently extinct individual (e.g., cloning of the endangered Banteng and Gaur).</li>"
        "</ol><br>"
        "<b>REINTRODUCTION AND POST-RELEASE PROTOCOLS</b><br>"
        "Captive-bred animals cannot simply be released into the jungle. Successful reintroduction mandates:"
        "<ul>"
        "<li><b>Soft Release via In-situ Acclimatization Bomas:</b> Enclosed predator-proof natural enclosures inside the release park where animals adjust to local climate and learn to forage for 6–12 months.</li>"
        "<li><b>Pre-Release Training:</b> Predator avoidance training, live prey capture capability, and human aversion conditioning.</li>"
        "<li><b>Post-Release Monitoring:</b> Satellite GPS radio-collaring, VHF telemetry, and camera trapping.</li>"
        "<li><b>Celebrated Indian Conservation Breeding & Reintroduction Successes:</b>"
        "<br>&bull; <b>Vulture Conservation Breeding Centres (VCBC - BNHS & MoEFCC):</b> Pinjore (Haryana), Rajabhatkhawa (WB), Rani (Assam). Captive breeding of White-rumped, Slender-billed, and Indian vultures wiped out by veterinary diclofenac, successfully soft-released back into the wild."
        "<br>&bull; <b>Project Cheetah (Kuno National Park, MP):</b> Re-establishing the extinct Asiatic Cheetah niche using translocated southern African cheetahs under scientific monitored breeding."
        "<br>&bull; <b>Gharial (<i>Gavialis gangeticus</i>) Rehabilitation:</b> Kukrail Reserve Forest (Lucknow) and Tikarpada (Odisha)."
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Genetic Adaptation to Captivity (Relaxation of Natural Selection):</b><br>"
        "In university exams, discuss the crucial biological pitfall of prolonged captive breeding:"
        "<ul>"
        "<li>In captivity, natural selection is relaxed: predators are absent, veterinary care is instant, and balanced food is delivered daily.</li>"
        "<li>Simultaneously, inadvertent <b>artificial selection favors docile, calm individuals</b> that tolerate concrete floors and human presence. Hyper-alert, aggressive wild survival behaviors are selected against!</li>"
        "<li>Mathematical risk: <code>R = h&sup2; &times; S</code>. For every generation spent in captivity, wild fitness alleles decay."
        "<br>&bull; <b>Management Solution:</b> Limit total generations in captivity to fewer than <b>3 to 5 generations</b> before reintroduction, maintain complex enriched enclosures, and continually infuse wild-rescued genomes.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Captive breeding under Central Zoo Authority (CZA) acts as an ex-situ insurance policy against extinction.",
        "Studbook databases (ZIMS, SPARKS) record pedigree, ancestral origins, and genetic relationships.",
        "Mean Kinship (MK) measures an individual's average relationship to the rest of the captive population.",
        "Individuals with low Mean Kinship possess rare alleles and are granted highest breeding priority.",
        "Individuals with high Mean Kinship are genetically over-represented and their mating is restricted.",
        "LaCONES (CCMB Hyderabad) is India's premier facility for wildlife reproductive biotechnology and cryobanking.",
        "Non-invasive endocrine monitoring analyzes fecal and urinary steroid metabolites without animal capture.",
        "Interspecific embryo transfer transfers wild embryos into common domestic surrogates (e.g., Gaur in cow).",
        "Soft release in habituation bomas allows captive-bred animals to acclimatize before full wild release.",
        "BNHS Vulture Conservation Breeding Centres successfully breed and release diclofenac-decimated vultures.",
        "Captive breeding must minimize generations in captivity to prevent loss of wild fitness and flight behaviors."
    ],
    "tables": [
        {
            "title": "Application of Reproductive Technologies in Endangered Wildlife Conservation",
            "headers": ["Reproductive Tool", "Target Wildlife Species", "Technical Approach / Surrogate", "Primary Conservation Breakthrough", "Key Institutional Center"],
            "rows": [
                ["Fecal Hormone Monitoring", "Royal Bengal Tiger, Asiatic Elephant", "Extraction of fecal corticosterone & progesterone", "Stress-free estrous cycle tracking & pregnancy diagnosis", "LaCONES-CCMB Hyderabad, WII Dehradun"],
                ["Electroejaculation & Semen Banking", "Asiatic Lion, Blackbuck, Spotted Deer", "Transrectal electrical stimulus under anesthesia", "Cryopreservation of gametes in liquid nitrogen gene bank", "LaCONES-CCMB Hyderabad"],
                ["Interspecific Embryo Transfer (iET)", "Indian Gaur (Bos gaurus)", "In-vitro embryo transferred into Holstein Friesian cow", "Common domestic cow gives birth to wild endangered Gaur", "San Diego Zoo / International Consortia"],
                ["Captive Colony Soft-Release", "Oriental White-backed Vulture", "Double-clutching manipulation in custom aviaries", "Breed & release vultures into diclofenac-free safe zones", "BNHS Vulture Breeding Centre, Pinjore (Haryana)"],
                ["Translocation & GPS Telemetry", "African / Asiatic Cheetah, One-horned Rhino", "Air-transport in bomas & satellite collar release", "Restoring apex carnivore / megaherbivore ecological niches", "Kuno National Park (MP), Kaziranga (Assam)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "When handling wild felids and ungulates for captive breeding or reproductive evaluation, "
        "zoo veterinarians must prevent <b>Capture Myopathy (Exertional Rhabdomyolysis)</b>, "
        "a fatal hyperthermic muscle necrosis and acute renal failure caused by severe metabolic acidosis and excessive catecholamine release during chemical immobilization. "
        "Veterinarians minimize chase time, use precise neuroleptic darting combinations (e.g., Medetomidine-Ketamine or Thiafentanil with immediate Atipamezole/Naltrexone reversal), "
        "administer prophylactic Sodium Bicarbonate, Vitamin E, Selenium, and chilled intravenous fluids, and maintain a quiet, dark environment."
    ),
    "tags": ["Wildlife Conservation", "Captive Breeding", "Mean Kinship", "LaCONES", "Studbooks", "ZIMS", "Vulture Conservation", "Capture Myopathy", "Cheetah"]
}
