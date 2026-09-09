# -*- coding: utf-8 -*-
"""
Unit 2: 5 Twelve-Mark Long Essay Questions (u2-q21 to u2-q25)
Principles of Animal Genetics & Population Genetics (VCI MSVE 2016 Standard)
"""

questions = [
    {
        "id": "u2-q21",
        "type": "long",
        "marks": 12,
        "question": (
            "Define Epistasis. Describe the various types of non-allelic gene interactions that modify the classical "
            "Mendelian dihybrid ratio (9:3:3:1) into modified ratios (9:3:4, 12:3:1, 13:3, 9:7, 15:1, 9:6:1). "
            "Illustrate each with its underlying biochemical or genetic mechanism and animal examples."
        ),
        "topicId": "u2-t03",
        "answer": (
            "<b>1. Introduction and Definition of Epistasis:</b><br>"
            "<b>Epistasis</b> (William Bateson, 1909) is a form of non-allelic gene interaction wherein an allele at one gene locus "
            "masks, alters, or suppresses the phenotypic expression of alleles at another, distinct gene locus. The gene that exerts "
            "the masking effect is termed <b>epistatic</b>, while the gene whose phenotypic expression is concealed is termed <b>hypostatic</b>.<br>"
            "In classical Mendelian dihybrid inheritance, independent assortment of two heterozygous loci (<code>AaBb &times; AaBb</code>) "
            "produces four distinct phenotypic classes in a <b>9:3:3:1</b> ratio [<code>9 A_B_ : 3 A_bb : 3 aaB_ : 1 aabb</code>]. "
            "Epistatic interactions modify this ratio into various combinations depending on the biochemical pathway involved.<br><br>"
            "<b>2. Detailed Classification of Epistatic Interactions:</b><br><br>"
            "<b>A. Supplementary Epistasis / Recessive Epistasis (9 : 3 : 4):</b><br>"
            "<ul>"
            "<li><b>Mechanism:</b> The homozygous recessive genotype at the epistatic locus (<code>aa</code>) completely suppresses the expression of the second locus (<code>B_</code> or <code>bb</code>). When dominant allele <code>A</code> is present, <code>B</code> supplements it to produce a third phenotype.</li>"
            "<li><b>Biochemical Model:</b> Precursor (Colorless) &mdash;[Enzyme A]&rarr; Intermediate Pigment &mdash;[Enzyme B]&rarr; Final Pigment.</li>"
            "<li><b>Animal Example:</b> Coat color in Labrador Retrievers. Locus <i>B</i> determines pigment color (<code>B_</code> black, <code>bb</code> chocolate brown). Locus <i>E</i> controls pigment deposition in hair shafts. Homozygous recessive <code>ee</code> prevents any eumelanin deposition regardless of B locus, producing <b>Yellow Labrador</b>. Cross of dihybrid blacks (<code>BbEe &times; BbEe</code>) yields: <b>9 Black (B_E_) : 3 Chocolate (bbE_) : 4 Yellow (_ _ee)</b>.</li>"
            "</ul><br>"
            "<b>B. Dominant Epistasis / Masking Epistasis (12 : 3 : 1):</b><br>"
            "<ul>"
            "<li><b>Mechanism:</b> A single dominant allele at the epistatic locus (<code>A_</code>) completely masks the phenotypic expression of the hypostatic locus (<code>B_</code> or <code>bb</code>). The hypostatic alleles are expressed only when the epistatic locus is homozygous recessive (<code>aa</code>).</li>"
            "<li><b>Animal Example:</b> Dominant White plumage in White Leghorn poultry. Locus <i>C</i> produces colored plumage (<code>C_</code> pigmented, <code>cc</code> white). Locus <i>I</i> is a dominant inhibitor of melanin synthesis. Whenever dominant <code>I_</code> is present, plumage is pure white regardless of C genotype. Only <code>iiC_</code> chickens develop colored plumage, while <code>iicc</code> is white. Cross <code>IiCc &times; IiCc</code> yields: <b>12 White (9 I_C_ + 3 I_cc) : 3 Colored (iiC_) : 1 White (iicc)</b> = <b>12 White : 3 Colored : 1 White</b> (net 12 White : 3 Colored : 1 White).</li>"
            "</ul><br>"
            "<b>C. Inhibitory Gene Interaction / Dominant & Recessive Epistasis (13 : 3):</b><br>"
            "<ul>"
            "<li><b>Mechanism:</b> A dominant allele at one locus (<code>A_</code>) inhibits the expression of a dominant allele at another locus (<code>B_</code>), while the homozygous recessive of the second locus (<code>bb</code>) independently produces the same blank phenotype.</li>"
            "<li><b>Outcome:</b> Classes <code>9 A_B_ + 3 A_bb + 1 aabb = 13</code> show the inhibitory/white phenotype, while only <code>3 aaB_</code> show the colored phenotype, generating a <b>13 : 3</b> ratio.</li>"
            "</ul><br>"
            "<b>D. Complementary Epistasis / Duplicate Recessive Epistasis (9 : 7):</b><br>"
            "<ul>"
            "<li><b>Mechanism:</b> Dominant alleles at both loci (<code>A_B_</code>) are mutually required to complete a multi-step biochemical pathway and produce the functional phenotype. Homozygosity for recessive alleles at either locus (<code>A_bb</code>, <code>aaB_</code>, or <code>aabb</code>) halts the pathway, giving identical null phenotypes.</li>"
            "<li><b>Biochemical Basis:</b> Substrate &mdash;[Enzyme A]&rarr; Intermediate &mdash;[Enzyme B]&rarr; Chromophore.</li>"
            "<li><b>Outcome:</b> <b>9 Expressed (A_B_) : 7 Unexpressed (3 A_bb + 3 aaB_ + 1 aabb)</b>. Example: Deaf-mutism in animals/humans; anthocyanin synthesis.</li>"
            "</ul><br>"
            "<b>E. Duplicate Dominant Epistasis / Duplicate Genes (15 : 1):</b><br>"
            "<ul>"
            "<li><b>Mechanism:</b> Either dominant allele (<code>A_</code> or <code>B_</code>) is fully sufficient on its own to produce the complete trait phenotype. Only the double homozygous recessive (<code>aabb</code>) exhibits the mutant/alternative phenotype.</li>"
            "<li><b>Animal Example:</b> Feathered shanks in chickens. Presence of either dominant allele <code>F1</code> or <code>F2</code> produces feathered legs. Shank feathers absent only in double recessive <code>f1f1 f2f2</code>. F2 cross yields <b>15 Feathered : 1 Clean shank</b>.</li>"
            "</ul><br>"
            "<b>F. Duplicate Genes with Cumulative Effect (9 : 6 : 1):</b><br>"
            "<ul>"
            "<li><b>Mechanism:</b> Dominant alleles at both loci individually produce identical intermediate phenotypes, but when present together (<code>A_B_</code>), they act cumulatively to produce an enhanced phenotype. The double recessive (<code>aabb</code>) produces a third distinct phenotype.</li>"
            "<li><b>Outcome:</b> <b>9 Enhanced (A_B_) : 6 Intermediate (3 A_bb + 3 aaB_) : 1 Null (aabb)</b>.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Clear definition of epistasis (epistatic vs hypostatic gene loci).",
            "Biochemical pathway foundation for departure from 9:3:3:1.",
            "Recessive Epistasis (9:3:4) with Labrador retriever coat color (B and E loci).",
            "Dominant Epistasis (12:3:1) with White Leghorn poultry plumage (I and C loci).",
            "Inhibitory Epistasis (13:3) and Complementary Epistasis (9:7).",
            "Duplicate Dominant Epistasis (15:1) with feathered shanks in fowl.",
            "Comprehensive comparative summary table of all epistatic ratios."
        ],
        "diagram": "",
        "table": {
            "title": "Master Summary of Modified Mendelian Dihybrid Epistatic Ratios",
            "headers": ["Type of Interaction", "Modified F2 Ratio", "A_B_ (9)", "A_bb (3)", "aaB_ (3)", "aabb (1)", "Classic Animal Example"],
            "rows": [
                ["Classical Dihybrid Cross", "9 : 3 : 3 : 1", "Phenotype 1", "Phenotype 2", "Phenotype 3", "Phenotype 4", "Mendelian independent assortment"],
                ["Recessive Epistasis", "9 : 3 : 4", "Black (9)", "Chocolate (3)", "Yellow (3)", "Yellow (1)", "Coat color in Labrador Retrievers (B/E loci)"],
                ["Dominant Epistasis", "12 : 3 : 1", "White (9)", "White (3)", "Colored (3)", "White (1)", "Plumage color in White Leghorn fowl (I/C loci)"],
                ["Inhibitory Epistasis", "13 : 3", "Inhibited (9)", "Inhibited (3)", "Expressed (3)", "Inhibited (1)", "Feather color inhibition in poultry"],
                ["Complementary Epistasis", "9 : 7", "Colored (9)", "White (3)", "White (3)", "White (1)", "Purple/White flower color; congenital deafness"],
                ["Duplicate Dominant Epistasis", "15 : 1", "Feathered (9)", "Feathered (3)", "Feathered (3)", "Clean (1)", "Feathered vs Clean shanks in domestic fowl"],
                ["Cumulative Duplicate Genes", "9 : 6 : 1", "Disc/Deep (9)", "Spherical (3)", "Spherical (3)", "Long/Elongate (1)", "Fruit shape in summer squash / metric traits"]
            ]
        },
        "pyq": ["VCI Annual 2018", "TANUVAS 2020", "IVRI 2021", "KVASU 2023"]
    },
    {
        "id": "u2-q22",
        "type": "long",
        "marks": 12,
        "question": (
            "Define Cytogenetics and Karyotyping. Describe in detail the standard protocol for peripheral blood lymphocyte "
            "karyotyping in cattle. Provide a comprehensive comparative table of diploid chromosome numbers, morphological types, "
            "and sex chromosomes in domestic animals. Discuss the economic significance of chromosomal abnormalities in livestock breeding."
        ),
        "topicId": "u2-t07",
        "answer": (
            "<b>1. Definitions:</b><br>"
            "<ul>"
            "<li><b>Cytogenetics:</b> The branch of genetics that correlates cellular structure and behavior, particularly the morphology, structural organization, number, and meiotic/mitotic dynamics of <b>chromosomes</b>, with the principles of heredity and phenotypic expression.</li>"
            "<li><b>Karyotype & Idiogram:</b> A <i>karyotype</i> is the systematic photographic or diagrammatic representation of the complete chromosomal complement of an individual somatic cell, arranged in descending order of size and grouped by centromeric position. An <i>idiogram</i> is a formalized, standardized diagrammatic mapping of the karyotype showing diagnostic G-banding patterns.</li>"
            "</ul><br>"
            "<b>2. Standard Protocol for Peripheral Blood Lymphocyte Culture (Moorhead et al., modified):</b>"
            "<ol>"
            "<li><b>Aseptic Blood Collection:</b> Collect 5&ndash;10 mL of venous blood from the jugular vein into a sterile vacutainer containing preservative-free sodium heparin (20 IU/mL). Invert gently to prevent clotting.</li>"
            "<li><b>Culture Inoculation:</b> In a laminar airflow cabinet, add 0.5&ndash;1.0 mL of whole heparinized blood to a sterile culture vessel containing 8&ndash;10 mL of RPMI-1640 or Ham's F-10 medium supplemented with 15&ndash;20% fetal bovine serum (FBS), antibiotics (penicillin 100 IU/mL, streptomycin 100 &mu;g/mL), and <b>Phytohaemagglutinin (PHA-M / PHA-P, 5&ndash;10 &mu;g/mL)</b>. PHA acts as a potent mitogen that stimulates resting non-dividing T-lymphocytes to dedifferentiate, enter blastogenesis, and begin mitotic division.</li>"
            "<li><b>Incubation:</b> Incubate at 37.5&deg;C in a 5% CO<sub>2</sub> humidified incubator for <b>70 to 72 hours</b>.</li>"
            "<li><b>Mitotic Arrest (Colchicine / Colcemid):</b> At 70 hours (2 hours prior to harvest), add <b>Colcemid (0.05&ndash;0.1 &mu;g/mL final concentration)</b>. Colcemid binds tubulin dimers, disrupting spindle microtubule assembly, thereby arresting dividing lymphocytes at <b>metaphase</b> where chromosomes are maximally condensed.</li>"
            "<li><b>Hypotonic Swelling:</b> Centrifuge at 1200 rpm for 10 min. Discard supernatant. Resuspend pellet in pre-warmed (37&deg;C) <b>hypotonic solution (0.075 M KCl or 0.8% sodium citrate)</b> for 15&ndash;20 minutes. The hypotonic osmotic influx swells the cytoplasm, dispersing metaphase chromosomes widely to eliminate overlapping.</li>"
            "<li><b>Fixation:</b> Add 2 mL of freshly prepared, ice-cold <b>Carnoy's fixative (3 parts absolute methanol : 1 part glacial acetic acid)</b>. Mix gently, centrifuge, discard supernatant, and repeat washing 3&ndash;4 times until the cell pellet becomes crisp, clean, and chalky white.</li>"
            "<li><b>Slide Preparation & Ageing:</b> Drop the concentrated cell suspension from a height of 1&ndash;2 feet onto clean, chilled, wet glass slides. Flame-dry gently or air-dry to spread chromosomes. Bake slides at 60&deg;C for 24 hours.</li>"
            "<li><b>Staining & Banding:</b> Stain with 4% Giemsa (for conventional solid karyotyping) or treat with 0.025% Trypsin followed by Giemsa for <b>GTG-banding (G-bands by Trypsin using Giemsa)</b> to produce diagnostic alternating light and dark transverse bands.</li>"
            "</ol><br>"
            "<b>3. Economic Significance of Chromosomal Abnormalities in Livestock Breeding:</b>"
            "<ul>"
            "<li><b>1/29 Robertsonian Translocation in Cattle [rob(1;29)]:</b> Centric fusion of autosomes 1 and 29. Heterozygous carrier bulls are phenotypically normal and produce normal semen volume and motility, but produce unbalanced secondary spermatocytes (nullisomic and disomic gametes). Causes <b>5&ndash;10% reduction in conception rates</b>, repeat breeding, and early embryonic death in mated cows. Mandatory karyotypic screening eliminates carriers from AI bull stations.</li>"
            "<li><b>Bovine Freemartinism:</b> Vascular anastomoses between heterosexual twin bovine fetuses (male-female twins) allow exchange of anti-Müllerian hormone (AMH) and testosterone, along with fetal hematopoetic stem cells. The female co-twin becomes an infertile <b>freemartin</b> with masculinized non-functional ovaries, hypoplastic uterus, and blind vagina. Cytogenetically diagnosed via <b>XX/XY leukocyte chimerism</b> (leukocyte karyotyping shows both 60,XX and 60,XY metaphases). Early karyotypic culling saves calf rearing costs.</li>"
            "<li><b>Reciprocal Translocations in Pigs:</b> Reduces litter size by 30&ndash;50% due to high peri-implantation embryonic mortality caused by unbalanced gametes.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Definitions of Cytogenetics, Karyotype, and Idiogram.",
            "Complete 8-step lymphocyte culture protocol (Heparin, PHA-M mitogen, 72h incubation, Colcemid metaphase arrest, 0.075M KCl hypotonic swelling, Carnoy fixative, GTG-banding).",
            "Comprehensive table of 2n numbers, autosome morphology, and sex chromosomes across cattle, buffalo, sheep, goat, pig, horse, and chicken.",
            "Economic impacts: rob(1;29) fertility reduction in cattle, Freemartinism (XX/XY chimerism), swine translocations."
        ],
        "diagram": "",
        "table": {
            "title": "Comprehensive Chromosomal Profiles of Farm Animals and Poultry",
            "headers": ["Species", "2n", "Autosome Morphology", "X Chromosome", "Y Chromosome", "Fundamental Arm Number (NF)"],
            "rows": [
                ["Cattle (Bos taurus / Bos indicus)", "60", "All 58 autosomes are Acrocentric", "Large Sub-metacentric", "Small Metacentric (B. taurus) / Acrocentric (B. indicus)", "60 (excluding sex chromosomes)"],
                ["River Buffalo (Bubalus bubalis)", "50", "5 pairs Sub-metacentric / Metacentric, 19 pairs Acrocentric", "Largest Acrocentric", "Small Acrocentric", "60"],
                ["Swamp Buffalo (Bubalus carabanensis)", "48", "6 pairs Bi-armed, 17 pairs Acrocentric", "Largest Acrocentric", "Small Acrocentric", "60"],
                ["Goat (Capra hircus)", "60", "All 58 autosomes are Acrocentric", "Large Acrocentric", "Minute Acrocentric / Dot-like", "60"],
                ["Sheep (Ovis aries)", "54", "3 pairs large Metacentric, 23 pairs Acrocentric", "Largest Acrocentric", "Small Metacentric", "60"],
                ["Pig (Sus scrofa domesticus)", "38", "12 pairs Bi-armed (Meta/Submeta), 6 pairs Acrocentric", "Medium Metacentric", "Small Metacentric", "64"],
                ["Horse (Equus caballus)", "64", "13 pairs Bi-armed, 18 pairs Acrocentric", "Large Sub-metacentric", "Small Acrocentric", "94"],
                ["Domestic Fowl (Gallus domesticus)", "78", "10 pairs Macrochromosomes, 28 pairs Microchromosomes", "Z: 4th largest Metacentric", "W: Small Sub-metacentric (Female heterogametic ZW)", "~108"]
            ]
        },
        "pyq": ["VCI Annual 2017", "IVRI 2020", "TANUVAS 2021", "GADVASU 2022", "LUVAS 2023"]
    },
    {
        "id": "u2-q23",
        "type": "long",
        "marks": 12,
        "question": (
            "Describe the molecular architecture of the DNA Double Helix according to the Watson-Crick model. "
            "Explain the Central Dogma of Molecular Genetics, detailing the stages of Transcription and Translation. "
            "Discuss the practical applications of recombinant DNA technology and Marker-Assisted Selection (MAS) in livestock improvement."
        ),
        "topicId": "u2-t12",
        "answer": (
            "<b>1. Molecular Architecture of DNA (Watson and Crick Model, 1953):</b>"
            "<ul>"
            "<li><b>Double-Helical Structure:</b> DNA consists of two right-handed antiparallel polynucleotide chains wound around a central axis (one running 5'&rarr;3', the other 3'&rarr;5').</li>"
            "<li><b>Sugar-Phosphate Backbone:</b> Hydrophilic deoxyribose sugars linked by 3'&ndash;5' phosphodiester bonds form the external structural backbone, while hydrophobic purine and pyrimidine bases project perpendicularly inward into the core.</li>"
            "<li><b>Complementary Base Pairing (Chargaff's Rules):</b> Adenine pairs specifically with Thymine via <b>two hydrogen bonds</b> (<code>A = T</code>), and Guanine pairs with Cytosine via <b>three hydrogen bonds</b> (<code>G &equiv; C</code>). Consequently, Purines = Pyrimidines (<code>A + G = T + C</code>), though <code>(A+T)/(G+C)</code> ratio varies across species.</li>"
            "<li><b>Helical Dimensions:</b> Diameter = <b>2.0 nm (20 &Aring;)</b>; complete helical turn = <b>3.4 nm (34 &Aring;)</b> containing exactly <b>10.4 to 10.5 base pairs</b> (pitch); distance between adjacent base pairs = <b>0.34 nm (3.4 &Aring;)</b>. Forms alternating Major (2.2 nm) and Minor (1.2 nm) grooves for regulatory protein interaction.</li>"
            "</ul><br>"
            "<b>2. The Central Dogma of Molecular Biology (Francis Crick, 1958):</b><br>"
            "The unidirectional flow of genetic information: <b>DNA &mdash;[Replication]&rarr; DNA &mdash;[Transcription]&rarr; mRNA &mdash;[Translation]&rarr; Functional Polypeptide/Protein</b>.<br><br>"
            "<b>A. Transcription (DNA to mRNA):</b>"
            "<ul>"
            "<li><b>Initiation:</b> RNA Polymerase II holoenzyme binds to the gene promoter region (TATA box at -25 bp, CAAT box at -75 bp) assisted by general transcription factors (TFIID, TFIIB). DNA unzips to form an open transcription bubble.</li>"
            "<li><b>Elongation:</b> RNA polymerase synthesizes single-stranded mRNA in the 5'&rarr;3' direction by reading the antisense (template) DNA strand 3'&rarr;5', incorporating ribonucleotides (ATP, UTP, GTP, CTP).</li>"
            "<li><b>Termination:</b> Reaches a polyadenylation signal sequence (<code>AAUAAA</code>), cleaved 10&ndash;30 nucleotides downstream.</li>"
            "<li><b>Post-Transcriptional Processing in Eukaryotes:</b> (i) 5'-capping with 7-methylguanosine; (ii) 3'-polyadenylation (150&ndash;250 A-residues); (iii) Splicing by spliceosomes (removal of non-coding introns and ligation of coding exons).</li>"
            "</ul><br>"
            "<b>B. Translation (mRNA to Functional Protein):</b>"
            "<ul>"
            "<li><b>Genetic Code:</b> Triplet codons, non-overlapping, commaless, degenerate (64 codons: 61 sense codons coding 20 amino acids, 3 nonsense stop codons: <code>UAA, UAG, UGA</code>; universal start codon: <code>AUG</code> coding for Methionine).</li>"
            "<li><b>Activation & Charging:</b> Amino acid is activated by aminoacyl-tRNA synthetase via ATP to form aminoacyl-AMP, then transferred to the 3'-CCA end of cognate tRNA.</li>"
            "<li><b>Ribosomal Assembly:</b> Small 40S subunit binds mRNA at 5' cap and scans for AUG; initiator Met-tRNA binds at the P-site; large 60S subunit joins to form active 80S ribosome.</li>"
            "<li><b>Elongation & Peptide Bond Formation:</b> Incoming aminoacyl-tRNA enters A-site (assisted by EF-1&alpha;); peptidyl transferase (28S rRNA ribozyme) catalyzes peptide bond between P-site amino acid and A-site amino acid; ribosome translocates 3 nucleotides along mRNA via EF-2.</li>"
            "<li><b>Termination:</b> Stop codon enters A-site; release factors (eRF1, eRF3) trigger hydrolysis and release of the nascent polypeptide chain.</li>"
            "</ul><br>"
            "<b>3. Livestock Applications: Marker-Assisted Selection (MAS) & Gene Diagnostics:</b>"
            "<ul>"
            "<li><b>Screening for Genetic Diseases:</b> Routine diagnostic PCR-RFLP screens out fatal alleles such as BLAD, CVM, Citrullinaemia, and DUMPS in dairy sires.</li>"
            "<li><b>Marker-Assisted Selection for Quantitative Traits:</b> Direct selection for desirable allelic variants: (i) <b>Kappa-casein (CSN3) B allele</b> in dairy cattle associated with superior cheese yield, firmer curd, and higher milk protein content; (ii) <b>DGAT1 K232A polymorphism</b> for elevated milk fat percentage; (iii) <b>Booroola fecundity gene (FecB)</b> in sheep, which increases ovulation rate and litter size by 1.0&ndash;1.5 lambs per ewe.</li>"
            "<li><b>Genomic Selection:</b> High-density SNP genotyping arrays (e.g., Bovine 50K and 777K HD BeadChips) predict Genomic Estimated Breeding Values (GEBVs) at calfhood, shortening the generation interval from 5 years to 1.5 years.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Watson-Crick DNA structure: Double helix, antiparallel, 2.0 nm diameter, 3.4 nm pitch (10.5 bp/turn), complementary hydrogen bonding (A=T 2 bonds, G≡C 3 bonds).",
            "Central Dogma flow: DNA -> RNA -> Protein.",
            "Transcription stages (Initiation, Elongation, Termination, 5' cap, poly-A tail, splicing).",
            "Translation mechanism (Genetic code properties, 80S ribosome, P and A sites, peptidyl transferase, peptide bond).",
            "Livestock applications: BLAD/CVM screening, CSN3 B allele for cheese yield, DGAT1, FecB gene in sheep, and high-density SNP genomic selection."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["IVRI 2018", "TANUVAS 2020", "GADVASU 2021", "KVASU 2022", "MAFSU 2023"]
    },
    {
        "id": "u2-q24",
        "type": "long",
        "marks": 12,
        "question": (
            "State the Hardy-Weinberg Law of Population Genetics. Derive the mathematical formulation of genotype frequencies "
            "for a two-allele locus. Detail the five fundamental assumptions required for the law to hold true. Explain how a "
            "population is tested for Hardy-Weinberg Equilibrium using Chi-square test (df = 1). Discuss the four evolutionary "
            "forces that disturb genetic equilibrium in domestic livestock populations."
        ),
        "topicId": "u2-t19",
        "answer": (
            "<b>1. Statement of the Hardy-Weinberg Law (G.H. Hardy & Wilhelm Weinberg, 1908):</b><br>"
            "In a large, randomly mating diploid population, both gene (allele) frequencies and genotypic frequencies "
            "remain constant and in stable equilibrium from generation to generation, provided there are no disturbing "
            "influences of mutation, migration, selection, and random genetic drift.<br><br>"
            "<b>2. Mathematical Derivation for a Two-Allele Locus:</b><br>"
            "Consider an autosomal locus with two alleles, <i>A</i> and <i>a</i>.<br>"
            "Let frequency of allele <i>A</i> = <code>p</code>, and frequency of allele <i>a</i> = <code>q</code>, such that <code>p + q = 1.0</code>.<br>"
            "In random mating (panmixia), the probability of union between male and female gametes is the mathematical product of their independent allele frequencies:<br>"
            "<ul>"
            "<li>Union of sperm <i>A</i> (prob <code>p</code>) and ovum <i>A</i> (prob <code>p</code>) &rarr; Genotype <code>AA</code> = <code>p &times; p = p&sup2;</code></li>"
            "<li>Union of sperm <i>A</i> (prob <code>p</code>) and ovum <i>a</i> (prob <code>q</code>) &rarr; Genotype <code>Aa</code> = <code>p &times; q = pq</code></li>"
            "<li>Union of sperm <i>a</i> (prob <code>q</code>) and ovum <i>A</i> (prob <code>p</code>) &rarr; Genotype <code>aA</code> = <code>q &times; p = pq</code></li>"
            "<li>Union of sperm <i>a</i> (prob <code>q</code>) and ovum <i>a</i> (prob <code>q</code>) &rarr; Genotype <code>aa</code> = <code>q &times; q = q&sup2;</code></li>"
            "</ul>"
            "Combining heterozygous classes (<code>pq + pq = 2pq</code>), the expected zygotic genotypic distribution is the binomial expansion:<br>"
            "<code>(p + q)&sup2; = p&sup2; (AA) + 2pq (Aa) + q&sup2; (aa) = 1.0</code><br><br>"
            "<b>Proof of Stability Across Generations:</b><br>"
            "Allele frequency of <i>A</i> in the next generation:<br>"
            "<code>p' = Freq(AA) + &frac12; Freq(Aa) = p&sup2; + &frac12;(2pq) = p&sup2; + pq = p(p + q) = p(1) = p</code>.<br>"
            "Thus, gene frequencies and genotypic frequencies reach permanent equilibrium after a single generation of random mating.<br><br>"
            "<b>3. Fundamental Assumptions of Hardy-Weinberg Law:</b>"
            "<ol>"
            "<li><b>Infinitely Large Population Size:</b> Eliminates random gamete sampling errors (no genetic drift).</li>"
            "<li><b>Random Mating (Panmixia):</b> Every individual has an equal probability of mating with any individual of opposite sex; no assortative mating or inbreeding.</li>"
            "<li><b>No Mutation:</b> Forward and reverse mutation rates must be zero or in exact dynamic balance.</li>"
            "<li><b>No Migration (Gene Flow):</b> Population is strictly closed to introduction of genes from outside or selective emigration.</li>"
            "<li><b>No Selection:</b> All genotypes (AA, Aa, aa) have equal reproductive viability and fertility (fitness coefficient <code>w = 1.0</code>, selection coefficient <code>s = 0</code>).</li>"
            "</ol><br>"
            "<b>4. Testing for Hardy-Weinberg Equilibrium using Chi-Square (&chi;&sup2;) Test:</b>"
            "<ol>"
            "<li>Step 1: Calculate observed allele frequencies (<code>p</code> and <code>q</code>) from sample genotype counts (<code>N</code>) using gene counting.</li>"
            "<li>Step 2: Calculate expected numbers for each genotype:<br>"
            "<code>E(AA) = p&sup2; &times; N</code>, <code>E(Aa) = 2pq &times; N</code>, <code>E(aa) = q&sup2; &times; N</code>.</li>"
            "<li>Step 3: Compute Chi-square statistic: <code>&chi;&sup2; = &sum; [(O - E)&sup2; / E]</code>.</li>"
            "<li>Step 4: Degrees of Freedom: <code>df = k - 1 - m</code>, where <code>k</code> = number of phenotypic classes (3), and <code>m</code> = number of independent parameters estimated from data (1, since p was estimated and q=1-p).<br>"
            "Therefore, <b><code>df = 3 - 1 - 1 = 1</code></b> (Always 1 degree of freedom for a 2-allele locus!).</li>"
            "<li>Step 5: Compare calculated &chi;&sup2; with table value at 5% level of significance (&chi;&sup2;<sub>crit</sub> = 3.841). If &chi;&sup2;<sub>calc</sub> &le; 3.841, null hypothesis is accepted: population is in HWE.</li>"
            "</ol><br>"
            "<b>5. Evolutionary Forces Altering Gene Frequencies in Livestock:</b>"
            "<ul>"
            "<li><b>A. Selection (Artificial and Natural):</b> The primary tool of the animal breeder. Selection acts by differential reproductive success. Directional selection against recessive homozygotes (<code>aa</code> with selection coefficient <code>s</code>) reduces <code>q</code> over generations:<br>"
            "<code>&Delta;q = -sq&sup2;(1 - q) / (1 - sq&sup2;)</code>. Complete culling (<code>s = 1.0</code>) changes <code>q<sub>1</sub> = q<sub>0</sub> / (1 + q<sub>0</sub>)</code>.</li>"
            "<li><b>B. Migration (Gene Flow):</b> Introduction of breeding animals from an outside donor population. If migrant proportion is <code>m</code> with allele frequency <code>q<sub>m</sub></code>, and native frequency is <code>q<sub>0</sub></code>:<br>"
            "<code>q<sub>1</sub> = m &times; q<sub>m</sub> + (1 - m) &times; q<sub>0</sub> &rArr; &Delta;q = m(q<sub>m</sub> - q<sub>0</sub>)</code>. (e.g., crossbreeding local cattle with exotic HF bulls).</li>"
            "<li><b>C. Mutation:</b> Spontaneous chemical alteration of nucleotide sequence. If forward mutation <i>A &rarr; a</i> occurs at rate <code>u</code>, and reverse <i>a &rarr; A</i> at rate <code>v</code>, equilibrium frequency is reached at: <code>q_hat = u / (u + v)</code>. Because mutation rates are very low (<code>10<sup>-5</sup> to 10<sup>-6</sup></code>), mutation alone causes negligible change per generation.</li>"
            "<li><b>D. Genetic Drift:</b> Random sampling fluctuations in finite populations (effective population size <code>N<sub>e</sub></code>). Variance of change in allele frequency per generation is: <code>&sigma;<sub>&Delta;q</sub>&sup2; = pq / (2N<sub>e</sub>)</code>. Causes random loss or fixation of alleles in small closed herds.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Complete statement and historical attribution (Hardy and Weinberg, 1908).",
            "Mathematical derivation of p² + 2pq + q² = 1 with gametic union probabilities and proof of generational stability.",
            "5 explicit assumptions (infinite size, panmixia, no mutation, no migration, no selection).",
            "Goodness of fit testing with Chi-square, explicitly deriving df = 1 (k - 1 - m = 3 - 1 - 1 = 1) and critical value 3.841.",
            "Detailed quantitative analysis of 4 disturbing forces: Selection (formula for Δq), Migration (formula for Δq), Mutation (u, v balance), and Genetic Drift (sampling variance pq/2Ne)."
        ],
        "diagram": "",
        "table": None,
        "pyq": ["VCI Annual 2017", "IVRI 2019", "TANUVAS 2020", "RAJUVAS 2021", "GADVASU 2022", "KVASU 2023"]
    },
    {
        "id": "u2-q25",
        "type": "long",
        "marks": 12,
        "question": (
            "Define Heritability (h²) and Repeatability (r). Describe the Paternal Half-Sib Analysis of Variance (ANOVA) method "
            "for estimating heritability, including the statistical model, ANOVA table layout, variance components, heritability formula, "
            "and standard error. Explain how repeatability is estimated and how it is used to calculate the Most Probable Producing "
            "Ability (MPPA) of a dairy cow. Discuss the practical breeding applications of heritability and repeatability in livestock improvement."
        ),
        "topicId": "u2-t25",
        "answer": (
            "<b>1. Fundamental Concepts & Definitions:</b>"
            "<ul>"
            "<li><b>Heritability in Narrow Sense (<code>h&sup2;</code>):</b> The proportion of total phenotypic variance (<code>V<sub>P</sub></code>) that is attributable to <i>additive genetic variance</i> (<code>V<sub>A</sub></code>):<br>"
            "<code>h&sup2; = V<sub>A</sub> / V<sub>P</sub></code> (Ranges from <code>0.0 to 1.0</code>).<br>"
            "It measures the extent to which offspring resemble their parents and dictates the efficiency of mass selection.</li>"
            "<li><b>Repeatability (<code>r</code>):</b> The intraclass correlation coefficient between repeated measurements of the same trait expressed multiple times in the lifetime of an individual (e.g., successive 305-day lactation yields, egg weight, fleece yield):<br>"
            "<code>r = (V<sub>A</sub> + V<sub>D</sub> + V<sub>I</sub> + V<sub>Eg</sub>) / V<sub>P</sub> = (V<sub>G</sub> + V<sub>Eg</sub>) / V<sub>P</sub></code>.<br>"
            "Because it includes both permanent environmental variance (<code>V<sub>Eg</sub></code>) and non-additive genetic variance, <b>repeatability sets the upper biological limit for heritability (<code>r &ge; h&sup2;</code>)</b>.</li>"
            "</ul><br>"
            "<b>2. Estimation of Heritability by Paternal Half-Sib Correlation (One-Way Nested ANOVA):</b><br>"
            "This is the most standard biometrical method in dairy cattle and poultry where multiple sires are mated to random, distinct groups of dams, each dam producing one recorded daughter.<br><br>"
            "<b>Statistical Model:</b><br>"
            "<code>Y<sub>ij</sub> = &mu; + s<sub>i</sub> + e<sub>ij</sub></code><br>"
            "where: <code>Y<sub>ij</sub></code> = phenotypic observation on the <i>j</i>-th progeny of the <i>i</i>-th sire;<br>"
            "<code>&mu;</code> = general population mean;<br>"
            "<code>s<sub>i</sub></code> = random effect of <i>i</i>-th sire ~ <code>NID(0, &sigma;<sub>s</sub>&sup2;)</code>;<br>"
            "<code>e<sub>ij</sub></code> = random residual error associated with <i>j</i>-th progeny within <i>i</i>-th sire ~ <code>NID(0, &sigma;<sub>e</sub>&sup2;)</code>.<br><br>"
            "<b>ANOVA Table Layout (for <code>S</code> sires, each having <code>k</code> progeny, total <code>N = S &times; k</code>):</b>"
            "<ul>"
            "<li><b>Between Sires:</b> Degrees of Freedom = <code>S - 1</code>; Mean Square = <code>MS<sub>S</sub></code>; Expected Mean Square = <code>E(MS<sub>S</sub>) = &sigma;<sub>e</sub>&sup2; + k &times; &sigma;<sub>s</sub>&sup2;</code></li>"
            "<li><b>Within Sires (Between Progeny):</b> Degrees of Freedom = <code>N - S</code>; Mean Square = <code>MS<sub>W</sub></code>; Expected Mean Square = <code>E(MS<sub>W</sub>) = &sigma;<sub>e</sub>&sup2;</code></li>"
            "</ul>"
            "<i>Note:</i> For unequal family sizes, the coefficient <code>k</code> is replaced by:<br>"
            "<code>k* = [1 / (S - 1)] &times; [N - (&sum; n<sub>i</sub>&sup2; / N)]</code>.<br><br>"
            "<b>Computation of Variance Components:</b><br>"
            "<code>&sigma;<sub>e</sub>&sup2; = MS<sub>W</sub></code><br>"
            "<code>&sigma;<sub>s</sub>&sup2; = (MS<sub>S</sub> - MS<sub>W</sub>) / k*</code><br>"
            "Total Phenotypic Variance = <code>&sigma;<sub>P</sub>&sup2; = &sigma;<sub>s</sub>&sup2; + &sigma;<sub>e</sub>&sup2;</code>.<br><br>"
            "<b>Intraclass Correlation (<code>t</code>) & Heritability Formulation:</b><br>"
            "The intraclass correlation among paternal half-sibs is: <code>t = &sigma;<sub>s</sub>&sup2; / (&sigma;<sub>s</sub>&sup2; + &sigma;<sub>e</sub>&sup2;)</code>.<br>"
            "Genetically, covariance among paternal half-sibs equals <code>&frac14; V<sub>A</sub></code>. Thus, the sire component <code>&sigma;<sub>s</sub>&sup2; = &frac14; V<sub>A</sub></code>.<br>"
            "Therefore:<br>"
            "<b><code>h&sup2; = 4 &times; t = 4 &times; &sigma;<sub>s</sub>&sup2; / (&sigma;<sub>s</sub>&sup2; + &sigma;<sub>e</sub>&sup2;)</code></b>.<br><br>"
            "<b>Standard Error of Heritability:</b><br>"
            "<code>SE(h&sup2;) &approx; 4 &times; &radic;[ {2(1 - t)&sup2; &times; [1 + (k* - 1)t]&sup2;} / {k*(k* - 1)(S - 1)} ]</code>.<br><br>"
            "<b>3. Estimation of Repeatability and Most Probable Producing Ability (MPPA):</b><br>"
            "Repeatability is estimated via one-way ANOVA across repeated lactation records of <code>N</code> cows (Between Cows and Within Cows across lactations):<br>"
            "<code>r = &sigma;<sub>c</sub>&sup2; / (&sigma;<sub>c</sub>&sup2; + &sigma;<sub>w</sub>&sup2;)</code>.<br><br>"
            "<b>Most Probable Producing Ability (MPPA):</b><br>"
            "MPPA predicts an animal's future production based on <code>n</code> past records, taking into account herd average (<code>&mu;</code>):<br>"
            "<b><code>MPPA = &mu; + [ (n &times; r) / (1 + (n - 1)r) ] &times; (X_bar - &mu;)</code></b><br>"
            "where: <code>n</code> = number of completed lactations, <code>r</code> = repeatability of lactation yield (~0.40), <code>X_bar</code> = cow's average milk yield, <code>&mu;</code> = herd average.<br>"
            "<i>Application:</i> Enables accurate culling of cows with poor future milk yield after 1 or 2 lactations.<br><br>"
            "<b>4. Practical Applications in Livestock Breeding:</b>"
            "<ul>"
            "<li><b>Predicting Selection Response:</b> Genetic gain per generation is directly proportional to heritability: <code>R = h&sup2; &times; S = i &times; h &times; &sigma;<sub>A</sub></code>.</li>"
            "<li><b>Choice of Selection Method:</b>"
            "<ul>"
            "<li><i>High h² (>0.40, e.g., Body weight at yearling, fat percentage):</i> Individual (mass) selection is highly effective.</li>"
            "<li><i>Moderate h² (0.20–0.40, e.g., 305-day milk yield):</i> Pedigree and progeny testing combined with individual selection.</li>"
            "<li><i>Low h² (<0.10, e.g., Calving interval, service period, fertility traits):</i> Individual selection is ineffective; family selection, progeny testing, and management/environmental interventions are required.</li>"
            "</ul></li>"
            "<li><b>Culling Decisions:</b> High repeatability (>0.50) justifies culling low-producing females based on their very first lactation record, because future performance will closely mirror past records.</li>"
            "<li><b>Multiple Records Efficiency:</b> The gain in accuracy of estimating breeding value from <code>n</code> records is: <code>&radic;[n / {1 + (n - 1)r}]</code>. Diminishing returns occur beyond 3 lactations when <code>r &approx; 0.40</code>.</li>"
            "</ul>"
        ),
        "keyPoints": [
            "Definitions and biological limits of h² and r (r >= h²).",
            "Paternal half-sib model: Y_ij = μ + s_i + e_ij.",
            "Complete ANOVA table with df, MS, EMS (σ_e² + k*σ_s²), and derivation of h² = 4t.",
            "Standard error of heritability formula.",
            "Repeatability formula and MPPA derivation: MPPA = μ + [nr / (1 + (n-1)r)] * (X̄ - μ).",
            "Livestock breeding applications: Selection method choice based on h² magnitude, culling based on r, predicting genetic response R = h²S."
        ],
        "diagram": "",
        "table": {
            "title": "One-Way Nested ANOVA Table for Paternal Half-Sib Heritability Estimation",
            "headers": ["Source of Variation", "Degrees of Freedom (df)", "Sum of Squares (SS)", "Mean Square (MS)", "Expected Mean Square [E(MS)]"],
            "rows": [
                ["Between Sires", "S - 1", "SS_S = Σ (Y_i.² / n_i) - (Y_..² / N)", "MS_S = SS_S / (S - 1)", "σ_e² + k* σ_s²"],
                ["Within Sires (Residual Progeny)", "N - S", "SS_W = SS_Total - SS_S", "MS_W = SS_W / (N - S)", "σ_e²"],
                ["Total", "N - 1", "SS_Total = ΣΣ Y_ij² - (Y_..² / N)", "-", "-"]
            ]
        },
        "pyq": ["VCI Annual 2018", "TANUVAS 2019", "IVRI 2020", "GADVASU 2021", "KVASU 2022", "LUVAS 2023"]
    }
]
