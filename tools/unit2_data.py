# tools/unit2_data.py
# Unit 2: Principles of Animal and Population Genetics
# 180 questions: 90 MCQs, 45 True/False, 45 Fill in the Blanks
# Exactly 18 MCQs, 9 T/F, 9 FIB per sub-section across u2-s1 to u2-s5

unit2_mcq = [
    # ============================================================
    # u2-s1: Mendelian Genetics & Gene Interactions (18 MCQs)
    # ============================================================
    {
        "q": "Who is universally recognized as the 'Father of Genetics' for discovering the fundamental laws of inheritance in Pisum sativum?",
        "o": ["Gregor Johann Mendel", "William Bateson", "Thomas Hunt Morgan", "Wilhelm Johannsen"],
        "a": 0,
        "e": "Gregor Johann Mendel conducted his famous hybridization experiments on the garden pea from 1856 to 1863, establishing particulate inheritance.",
        "topicId": "u2-t01",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "The term 'Genetics' was coined in the year 1905 by which pioneer scientist?",
        "o": ["Gregor Mendel", "William Bateson", "Carl Correns", "Hugo de Vries"],
        "a": 1,
        "e": "William Bateson coined the term 'Genetics' in 1905, along with terms like 'allele', 'homozygote', 'heterozygote', and 'F1 generation'.",
        "topicId": "u2-t01",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "Which scientist formulated the Germplasm Theory, disproving the inheritance of acquired characters by cutting mice tails for 22 generations?",
        "o": ["Jean-Baptiste Lamarck", "Charles Darwin", "August Weismann", "Theodor Boveri"],
        "a": 2,
        "e": "August Weismann (1892) proposed the Germplasm Theory, showing a strict physical distinction between somatoplasm and immortal germplasm.",
        "topicId": "u2-t01",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "Mendel's First Law (Law of Segregation) is also known as the Law of:",
        "o": ["Independent Assortment", "Purity of Gametes", "Dominance", "Linkage"],
        "a": 1,
        "e": "The Law of Segregation states that paired alleles separate cleanly during meiosis so that each gamete carries only one allele, hence 'Purity of Gametes'.",
        "topicId": "u2-t04",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "What is the expected phenotypic ratio in the F₂ generation of a typical Mendelian monohybrid cross with complete dominance?",
        "o": ["1:2:1", "3:1", "9:3:3:1", "1:1"],
        "a": 1,
        "e": "A monohybrid cross (e.g. Tt x Tt) yields a 3:1 phenotypic ratio (3 dominant : 1 recessive) and a 1:2:1 genotypic ratio.",
        "topicId": "u2-t04",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "A genetic cross between an unknown dominant phenotype individual and a homozygous recessive individual is called a:",
        "o": ["Backcross", "Testcross", "Reciprocal cross", "Dihybrid cross"],
        "a": 1,
        "e": "A testcross is specifically performed with a homozygous recessive tester to determine whether the dominant parent is homozygous or heterozygous.",
        "topicId": "u2-t04",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "What phenotypic ratio is obtained from a testcross of a heterozygous dihybrid individual (AaBb × aabb)?",
        "o": ["9:3:3:1", "1:1:1:1", "3:1", "1:2:1"],
        "a": 1,
        "e": "A dihybrid testcross produces equal proportions of four recombinant and parental phenotypes in a 1:1:1:1 ratio.",
        "topicId": "u2-t04",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "In Andalusian fowl, crossing a true-breeding black fowl with a splashed white fowl produces 100% blue offspring. This is a classic example of:",
        "o": ["Complete dominance", "Incomplete dominance", "Codominance", "Recessive epistasis"],
        "a": 1,
        "e": "Incomplete dominance results in an intermediate heterozygous phenotype (blue plumage in Andalusian fowl, pink in Mirabilis jalapa) with a 1:2:1 F2 ratio.",
        "topicId": "u2-t05",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "The roan coat color in Shorthorn cattle (intermingled red and white hairs) is an example of:",
        "o": ["Incomplete dominance", "Codominance", "Dominant epistasis", "Overdominance"],
        "a": 1,
        "e": "Codominance occurs when both alleles (red hair and white hair) are fully and simultaneously expressed in the heterozygote without blending.",
        "topicId": "u2-t05",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "In yellow mice (Lucien Cuénot, 1905), crossing two yellow mice always produces yellow and agouti offspring in which modified ratio?",
        "o": ["3:1", "2:1", "1:2:1", "9:3:4"],
        "a": 1,
        "e": "The yellow allele (A^Y) is a recessive lethal in homozygous state (A^Y A^Y dies in utero), producing a modified surviving ratio of 2 yellow : 1 agouti.",
        "topicId": "u2-t05",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "The lethal condition known as 'Bulldog Calf' (severe chondrodysplasia and abortion) in Dexter cattle is caused by:",
        "o": ["A homozygous recessive lethal gene", "A homozygous dominant lethal gene", "A sex-linked recessive gene", "Mitochondrial mutation"],
        "a": 0,
        "e": "In Dexter cattle, heterozygous calves are short-legged (Dexter type), but homozygous lethal calves exhibit severe achondroplasia ('Bulldog calf') and are aborted.",
        "topicId": "u2-t05",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "What modified dihybrid F₂ phenotypic ratio represents Complementary Gene Action (e.g. Bateson and Punnett's sweet pea flower color)?",
        "o": ["9:7", "12:3:1", "9:3:4", "15:1"],
        "a": 0,
        "e": "Complementary gene interaction requires the presence of at least one dominant allele at both loci (A-B-) to produce the trait, yielding a 9:7 ratio.",
        "topicId": "u2-t06",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "A modified dihybrid F₂ phenotypic ratio of 12:3:1 is characteristic of:",
        "o": ["Dominant epistasis", "Recessive epistasis", "Duplicate dominant genes", "Inhibitory gene interaction"],
        "a": 0,
        "e": "In dominant epistasis (e.g. fruit color in summer squash, feather color in Leghorn fowl), a single dominant allele at one locus masks both alleles at the other locus, yielding 12:3:1.",
        "topicId": "u2-t06",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "Coat color inheritance in Labrador retrievers (black, brown/chocolate, and yellow) is governed by:",
        "o": ["Dominant epistasis (12:3:1)", "Recessive epistasis (9:3:4)", "Complementary genes (9:7)", "Duplicate genes (15:1)"],
        "a": 1,
        "e": "Recessive epistasis (9:3:4) operates in Labrador coat color: homozygous recessive ee at the extension locus masks the black/brown B locus, resulting in yellow coat.",
        "topicId": "u2-t06",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "The phenomenon where a single gene influences multiple distinct and apparently unrelated phenotypic traits is called:",
        "o": ["Polygeny", "Pleiotropy", "Epistasis", "Penetrance"],
        "a": 1,
        "e": "Pleiotropy occurs when one gene affects multiple organ systems or traits (e.g. frizzle gene in chickens causing curled feathers, high metabolic rate, and enlarged heart).",
        "topicId": "u2-t07",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "The percentage of individuals carrying a specific genotype who actually express the corresponding phenotype is termed:",
        "o": ["Expressivity", "Penetrance", "Heritability", "Repeatability"],
        "a": 1,
        "e": "Penetrance is the statistical proportion of genotypes that express the expected phenotype. Expressivity refers to the degree or severity of expression.",
        "topicId": "u2-t07",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "An environmentally induced non-hereditary phenotypic modification that closely mimics a known genetic mutant is called a:",
        "o": ["Phenocopy", "Genocopy", "Pleiotrope", "Atavism"],
        "a": 0,
        "e": "A phenocopy is an environmentally produced condition (e.g. nutritional or drug-induced deformity) resembling a genetic defect but lacking any altered genotype.",
        "topicId": "u2-t07",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "Which blood group system in cattle is the most complex and polymorphic, possessing over 600 recognized phenogroups/alleles?",
        "o": ["A system", "B system", "J system", "C system"],
        "a": 1,
        "e": "The B blood group system in cattle is extremely complex and polymorphic with hundreds of antigenic combinations (phenogroups), highly useful in parentage verification.",
        "topicId": "u2-t08",
        "subSection": "u2-s1",
        "diff": 2
    },

    # ============================================================
    # u2-s2: Cytogenetics, Linkage & Sex Linkage (18 MCQs)
    # ============================================================
    {
        "q": "During which sub-stage of Prophase I of Meiosis does crossing over and genetic recombination physically occur?",
        "o": ["Leptotene", "Zygotene", "Pachytene", "Diplotene"],
        "a": 2,
        "e": "Crossing over occurs during the Pachytene stage through the formation of recombination nodules between non-sister chromatids.",
        "topicId": "u2-t02",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "What is the diploid chromosome number (2n) in domestic cattle (Bos taurus and Bos indicus)?",
        "o": ["50", "54", "60", "64"],
        "a": 2,
        "e": "Cattle have 2n = 60 chromosomes: 58 acrocentric autosomes, a submetacentric X chromosome, and a small submetacentric (Bos taurus) or acrocentric (Bos indicus) Y chromosome.",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "What is the diploid chromosome number (2n) of the River Buffalo (Bubalus bubalis)?",
        "o": ["48", "50", "54", "60"],
        "a": 1,
        "e": "River buffalo (Murrah, Nili-Ravi) has 2n = 50 chromosomes (5 pairs of submetacentric/metacentric autosomes and 20 pairs of acrocentric autosomes). Swamp buffalo has 2n = 48.",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "What is the diploid chromosome number (2n) in domestic sheep (Ovis aries)?",
        "o": ["60", "54", "50", "38"],
        "a": 1,
        "e": "Domestic sheep have 2n = 54 chromosomes (3 pairs of large metacentric autosomes and 23 pairs of acrocentric autosomes plus sex chromosomes).",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "What is the diploid chromosome number (2n) of domestic goat (Capra hircus)?",
        "o": ["54", "60", "64", "78"],
        "a": 1,
        "e": "Goat has 2n = 60 chromosomes, where all 58 autosomes are acrocentric, similar to cattle.",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "What is the diploid chromosome number (2n) of the domestic chicken (Gallus gallus domesticus)?",
        "o": ["60", "78", "64", "54"],
        "a": 1,
        "e": "Chicken has 2n = 78 chromosomes, divided into 10 pairs of macrochromosomes and 29 pairs of distinct microchromosomes.",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "In avian species (poultry), what is the chromosomal mechanism of sex determination?",
        "o": ["XX female, XY male", "ZZ male, ZW female", "XX female, XO male", "Haplodiploidy"],
        "a": 1,
        "e": "In birds, the female is the heterogametic sex (ZW), while the male is the homogametic sex (ZZ).",
        "topicId": "u2-t09",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "The Lyon hypothesis explains dosage compensation in female mammalian somatic cells by:",
        "o": ["Doubling transcription of the single male X", "Random inactivation of one X chromosome", "Inactivating both parental X chromosomes", "Eliminating Y chromosomes"],
        "a": 1,
        "e": "Mary Lyon (1961) showed that one of the two X chromosomes in female somatic cells is randomly condensed into an inactive heterochromatic Barr body.",
        "topicId": "u2-t09",
        "subSection": "u2-s2",
        "diff": 2
    },
    {
        "q": "Tortoiseshell or calico coat coloration (orange and black patches) in domestic cats is almost exclusively observed in females because:",
        "o": ["The orange gene is Y-linked", "The orange gene is X-linked and undergoes random X-inactivation", "Male embryos carrying black pigment die in utero", "It is an autosomal sex-limited trait"],
        "a": 1,
        "e": "The O (orange) locus is on the X chromosome. Heterozygous females (X^O X^B) form a mosaic of orange and black patches due to random lyonization.",
        "topicId": "u2-t09",
        "subSection": "u2-s2",
        "diff": 2
    },
    {
        "q": "Which type of genetic trait is expressed in only one biological sex due to anatomical or physiological factors (e.g. milk yield in cows, cryptorchidism in bulls)?",
        "o": ["Sex-linked trait", "Sex-influenced trait", "Sex-limited trait", "Holandric trait"],
        "a": 2,
        "e": "Sex-limited traits are governed by autosomal genes that are expressed exclusively in one sex due to anatomical limitations (e.g. egg laying, lactation).",
        "topicId": "u2-t10",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "Horn development in Dorset/Merino sheep (dominant in males, recessive in females) is a classic example of:",
        "o": ["Sex-linked inheritance", "Sex-influenced inheritance", "Sex-limited inheritance", "Cytoplasmic inheritance"],
        "a": 1,
        "e": "Sex-influenced traits are autosomal traits whose phenotypic expression and dominance relationship are altered by male or female sex hormones.",
        "topicId": "u2-t10",
        "subSection": "u2-s2",
        "diff": 2
    },
    {
        "q": "One map unit (centiMorgan, cM) on a genetic linkage map corresponds to what percentage of recombination?",
        "o": ["0.1%", "1%", "10%", "50%"],
        "a": 1,
        "e": "By definition, 1 centiMorgan (cM) equals 1% recombination frequency between two linked gene loci.",
        "topicId": "u2-t11",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "What is the theoretical maximum recombination frequency between two widely separated linked genes on the same chromosome?",
        "o": ["25%", "50%", "75%", "100%"],
        "a": 1,
        "e": "Crossing over involves non-sister chromatids; even with multiple crossovers, the maximum recombination frequency cannot exceed 50% (independent assortment).",
        "topicId": "u2-t11",
        "subSection": "u2-s2",
        "diff": 2
    },
    {
        "q": "A sterile heifer calf born co-twin to a bull calf with fused placental circulation exhibiting intersex gonads is called a:",
        "o": ["Hermaphrodite", "Freemartin", "Gynandromorph", "Klinefelter heifer"],
        "a": 1,
        "e": "Freemartinism occurs in over 90% of heterosexual twin cattle pregnancies due to chorionic vascular anastomosis and anti-Müllerian hormone transfer from the male fetus.",
        "topicId": "u2-t13",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "Which structural chromosomal aberration involves the fusion of two acrocentric chromosomes at their centromeres to form a single large metacentric chromosome?",
        "o": ["Reciprocal translocation", "Robertsonian translocation (Centric fusion)", "Paracentric inversion", "Pericentric inversion"],
        "a": 1,
        "e": "Robertsonian translocation (centric fusion) unites two acrocentric chromosomes, such as the famous 1/29 translocation in cattle which reduces bull fertility.",
        "topicId": "u2-t13",
        "subSection": "u2-s2",
        "diff": 2
    },
    {
        "q": "In livestock cytogenetics, G-banding of metaphase chromosomes is achieved by treating chromosomes with which enzyme followed by Giemsa staining?",
        "o": ["Pepsin", "Trypsin", "Amylase", "Lysozyme"],
        "a": 1,
        "e": "G-banding standardly uses controlled mild trypsin digestion followed by Giemsa staining to produce alternating AT-rich dark bands and GC-rich light bands.",
        "topicId": "u2-t14",
        "subSection": "u2-s2",
        "diff": 2
    },
    {
        "q": "Extra-chromosomal or maternal inheritance in animals is primarily mediated by genes located in:",
        "o": ["Centrosomes", "Ribosomes", "Mitochondrial DNA (mtDNA)", "Endoplasmic reticulum"],
        "a": 2,
        "e": "Mitochondria possess their own circular double-stranded DNA (mtDNA) transmitted exclusively through the ovum cytoplasm, demonstrating non-Mendelian maternal inheritance.",
        "topicId": "u2-t15",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "An inversion that does NOT include the centromere within the inverted chromosome segment is termed a:",
        "o": ["Pericentric inversion", "Paracentric inversion", "Reciprocal translocation", "Isochromosome"],
        "a": 1,
        "e": "A paracentric inversion occurs entirely within one chromosome arm without involving the centromere. A pericentric inversion spans the centromere.",
        "topicId": "u2-t13",
        "subSection": "u2-s2",
        "diff": 2
    },

    # ============================================================
    # u2-s3: Molecular Genetics & Techniques (18 MCQs)
    # ============================================================
    {
        "q": "According to the Watson-Crick double helix model of B-DNA, the distance between two adjacent nucleotide base pairs is:",
        "o": ["3.4 nm", "0.34 nm (3.4 Å)", "2.0 nm", "34 nm"],
        "a": 1,
        "e": "In B-DNA, each helical turn comprises 10 base pairs with a pitch of 3.4 nm, giving a distance between adjacent base pairs of 0.34 nm (3.4 Å).",
        "topicId": "u2-t16",
        "subSection": "u2-s3",
        "diff": 2
    },
    {
        "q": "According to Chargaff's rules for double-stranded DNA:",
        "o": ["A = C and G = T", "A = T and G = C", "A + T = G + C", "Purines < Pyrimidines"],
        "a": 1,
        "e": "Chargaff established that Adenine equals Thymine (A = T) and Guanine equals Cytosine (G = C), so Total Purines (A+G) = Total Pyrimidines (C+T).",
        "topicId": "u2-t16",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "How many hydrogen bonds are formed between Guanine and Cytosine in a DNA double helix?",
        "o": ["1", "2", "3", "4"],
        "a": 2,
        "e": "Guanine and Cytosine pair via three hydrogen bonds (G ≡ C), whereas Adenine and Thymine pair via two hydrogen bonds (A = T).",
        "topicId": "u2-t16",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Meselson and Stahl (1958) experimentally proved that DNA replication is:",
        "o": ["Conservative", "Semiconservative", "Dispersive", "Non-directional"],
        "a": 1,
        "e": "Using heavy nitrogen (¹⁵N) density-gradient centrifugation in E. coli, Meselson and Stahl proved that each daughter DNA molecule contains one conserved parental strand and one newly synthesized strand.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 2
    },
    {
        "q": "During DNA replication, the short discontinuous fragments synthesized on the lagging strand are known as:",
        "o": ["Khorana fragments", "Okazaki fragments", "Watson fragments", "Sanger fragments"],
        "a": 1,
        "e": "Okazaki fragments are short stretches of DNA (100–200 nt in eukaryotes) synthesized discontinuously on the lagging strand in the 5' to 3' direction.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Which enzyme is responsible for sealing nicks in the phosphodiester backbone by joining Okazaki fragments during DNA replication?",
        "o": ["DNA Helicase", "DNA Polymerase I", "DNA Ligase", "Topoisomerase"],
        "a": 2,
        "e": "DNA ligase forms a covalent phosphodiester bond between the 3'-OH and 5'-phosphate ends of adjacent Okazaki fragments.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The synthesis of an RNA molecule from a DNA template strand is formally known as:",
        "o": ["Replication", "Transcription", "Translation", "Reverse transcription"],
        "a": 1,
        "e": "Transcription is the enzymatic synthesis of RNA (mRNA, tRNA, rRNA) from a complementary antisense DNA template by RNA polymerase.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Which of the following codons functions as the universal initiation (start) codon for protein synthesis?",
        "o": ["UAA", "UAG", "AUG", "UGA"],
        "a": 2,
        "e": "AUG is the universal start codon coding for Methionine in eukaryotes and Formyl-methionine in prokaryotes.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Which triplet codons are the three termination (nonsense / stop) codons in the standard genetic code?",
        "o": ["AUG, GUG, UUG", "UAA, UAG, UGA", "AAA, UUU, CCC", "CGA, CGU, CGC"],
        "a": 1,
        "e": "The three stop codons are UAA (Ochre), UAG (Amber), and UGA (Opal). They do not code for any amino acid.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The fact that more than one codon can specify the same amino acid demonstrates that the genetic code is:",
        "o": ["Ambiguous", "Degenerate", "Overlapping", "Universal"],
        "a": 1,
        "e": "Degeneracy (or redundancy) of the genetic code means that 18 of the 20 standard amino acids are coded by multiple synonymous codons.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 2
    },
    {
        "q": "Who invented the Polymerase Chain Reaction (PCR) technique in 1983, receiving the Nobel Prize in 1993?",
        "o": ["Frederick Sanger", "Kary Mullis", "Edwin Southern", "James Watson"],
        "a": 1,
        "e": "Kary Mullis conceived and developed the Polymerase Chain Reaction (PCR) to amplify specific DNA fragments exponentially.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "What is the correct temperature sequence for the three steps of a standard PCR cycle?",
        "o": ["Denaturation (94°C) → Annealing (55°C) → Extension (72°C)", "Annealing (55°C) → Denaturation (94°C) → Extension (72°C)", "Denaturation (72°C) → Annealing (94°C) → Extension (55°C)", "Extension (72°C) → Denaturation (55°C) → Annealing (94°C)"],
        "a": 0,
        "e": "A PCR cycle operates at: 1. Denaturation (94–95°C), 2. Primer Annealing (50–60°C), and 3. Taq Extension (72°C).",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The heat-stable DNA polymerase enzyme used in standard PCR is isolated from which thermophilic bacterium?",
        "o": ["Escherichia coli", "Bacillus subtilis", "Thermus aquaticus", "Pseudomonas aeruginosa"],
        "a": 2,
        "e": "Taq polymerase is extracted from Thermus aquaticus, a hot-spring bacterium, allowing it to withstand 95°C denaturation temperatures.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Restriction endonucleases (molecular scissors) cleave DNA molecules specifically at:",
        "o": ["Random poly-A sequences", "Palindromic recognition sequences", "Promoter regions only", "Telomeric repeats"],
        "a": 1,
        "e": "Restriction enzymes (e.g. EcoRI: 5'-GAATTC-3') cleave double-stranded DNA at specific symmetrical palindromic recognition sites.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 2
    },
    {
        "q": "During agarose gel electrophoresis, DNA fragments migrate towards which electrode and why?",
        "o": ["Negative cathode; DNA is positively charged", "Positive anode; DNA has a negative phosphate backbone", "Positive anode; DNA is neutral", "Negative cathode; histones are negatively charged"],
        "a": 1,
        "e": "Because of its repeating phosphate group backbone, DNA carries a net negative charge and migrates towards the positive anode (+).",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 2
    },
    {
        "q": "The Sanger DNA sequencing method relies on which modified nucleotides to cause chain termination?",
        "o": ["dNTPs (deoxynucleotide triphosphates)", "ddNTPs (dideoxynucleotide triphosphates)", "Ribonucleotides", "cAMP"],
        "a": 1,
        "e": "Dideoxynucleotides (ddNTPs) lack the 3'-OH group needed for phosphodiester bond formation, halting elongation upon incorporation.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 2
    },
    {
        "q": "The molecular hybridization technique used to detect specific target DNA fragments immobilized on a membrane is called:",
        "o": ["Southern Blotting", "Northern Blotting", "Western Blotting", "Eastern Blotting"],
        "a": 0,
        "e": "Southern blotting (developed by Edwin Southern) detects specific DNA sequences using labeled complementary probes. Northern blotting detects RNA, Western detects proteins.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Reverse transcriptase is an enzyme that synthesizes:",
        "o": ["RNA from RNA template", "DNA from RNA template", "Protein from DNA template", "DNA from DNA template"],
        "a": 1,
        "e": "Reverse transcriptase (found in retroviruses like bovine leukemia virus) carries out reverse transcription: synthesizing cDNA from an RNA template.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },

    # ============================================================
    # u2-s4: Population Genetics & Hardy-Weinberg Law (18 MCQs)
    # ============================================================
    {
        "q": "A group of interbreeding individuals of the same species existing concurrently in a geographic area and sharing a common gene pool is a:",
        "o": ["Clone", "Mendelian population", "Phenocopy", "Lineage"],
        "a": 1,
        "e": "A Mendelian population is a community of sexually interbreeding individuals sharing a common gene pool across generations.",
        "topicId": "u2-t19",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "In a herd of 100 cattle, the genotypes are 40 AA, 40 Aa, and 20 aa. What is the gene frequency of allele A (p)?",
        "o": ["0.40", "0.50", "0.60", "0.80"],
        "a": 2,
        "e": "Total alleles = 200. Frequency p = (2 * 40 + 40) / 200 = (80 + 40) / 200 = 120 / 200 = 0.60.",
        "topicId": "u2-t20",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "If the frequencies of alleles A and a are p and q respectively, what is the sum of (p + q)?",
        "o": ["0.5", "1.0", "2.0", "100"],
        "a": 1,
        "e": "By biological definition, the sum of all allelic frequencies at a given genetic locus in a population must equal 1.0 (p + q = 1).",
        "topicId": "u2-t20",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "The Hardy-Weinberg Law was independently formulated in 1908 by G.H. Hardy and:",
        "o": ["Wilhelm Weinberg", "Sewall Wright", "J. B. S. Haldane", "R. A. Fisher"],
        "a": 0,
        "e": "British mathematician G. H. Hardy and German physician Wilhelm Weinberg independently discovered the equilibrium law in 1908.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "According to the Hardy-Weinberg Law, what is the expected frequency of heterozygous carriers (Aa) in an equilibrium population?",
        "o": ["p²", "q²", "2pq", "p + q"],
        "a": 2,
        "e": "Under HW equilibrium, genotypic frequencies expand as (p + q)² = p²(AA) + 2pq(Aa) + q²(aa) = 1. The heterozygote frequency is 2pq.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "In a dairy herd at Hardy-Weinberg equilibrium, 16% of calves are born with a recessive black coat (aa). What is the frequency of the recessive allele a (q)?",
        "o": ["0.16", "0.40", "0.84", "0.04"],
        "a": 1,
        "e": "q² = 0.16; therefore q = sqrt(0.16) = 0.40. Allele A frequency p = 1 - 0.40 = 0.60.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "Using the herd data above where q = 0.40 and p = 0.60, what percentage of the herd consists of heterozygous carriers (2pq)?",
        "o": ["24%", "36%", "48%", "60%"],
        "a": 2,
        "e": "2pq = 2 * 0.60 * 0.40 = 0.48, which corresponds to 48% heterozygous carriers.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "Which of the following conditions is REQUIRED for a population to maintain Hardy-Weinberg equilibrium?",
        "o": ["Small population size", "Non-random assortative mating", "Random mating (panmixia) and large population size", "Continuous high mutation rate"],
        "a": 2,
        "e": "Hardy-Weinberg equilibrium requires: 1. Infinitely large population, 2. Panmixia (random mating), 3. No selection, 4. No mutation, 5. No migration, 6. No genetic drift.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "When testing Hardy-Weinberg equilibrium for a two-allele locus using the Chi-Square goodness-of-fit test, the degrees of freedom is:",
        "o": ["1", "2", "3", "0"],
        "a": 0,
        "e": "df = Number of genotypes (3) - Number of independent alleles estimated (2) = 3 - 2 = 1.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "Which evolutionary force is the ultimate original source of all new genetic variation in farm animals?",
        "o": ["Genetic drift", "Migration", "Mutation", "Selection"],
        "a": 2,
        "e": "Mutation is the only fundamental biological mechanism that generates entirely novel alleles; other forces merely alter the frequencies of existing alleles.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "Random fluctuations in allele frequencies from generation to generation purely due to sampling error in small populations is known as:",
        "o": ["Hardy-Weinberg equilibrium", "Gene flow", "Genetic drift (Sewall Wright effect)", "Selection pressure"],
        "a": 2,
        "e": "Genetic drift refers to random sampling variation in gametes leading to erratic shifts in allele frequencies, loss of heterozygosity, or allele fixation in small herds.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "The establishment of a new herd by a very small number of founder individuals carrying an unrepresentative sample of alleles is called the:",
        "o": ["Bottleneck effect", "Founder effect", "Sewall Wright plateau", "Inbreeding depression"],
        "a": 1,
        "e": "The founder effect is a special case of genetic drift occurring when a new colony is initiated by a handful of breeding animals.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "If 20% of a native herd is replaced each generation by immigrant sires from another breed (migration rate m = 0.20), the process altering gene frequencies is:",
        "o": ["Genetic drift", "Gene flow (Migration)", "Meiotic drive", "Balanced polymorphism"],
        "a": 1,
        "e": "Migration (gene flow) introduces foreign alleles into a recipient population at rate m, systematically changing allele frequencies.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "The reproductive efficiency or relative survival of a genotype compared to the most favored genotype is called its:",
        "o": ["Selection coefficient (s)", "Fitness / Adaptive value (W)", "Heritability", "Breeding value"],
        "a": 1,
        "e": "Biological fitness (W) is the relative reproductive success of a genotype, scaled from 0.0 to 1.0 (where s = 1 - W).",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "If a recessive lethal mutation is completely selected against (s = 1.0) in homozygous state (aa), can selection completely eliminate the recessive allele from the population?",
        "o": ["Yes, in 1 generation", "Yes, in 10 generations", "No, because the recessive allele hides in heterozygous carriers (Aa)", "Yes, within 5 generations"],
        "a": 2,
        "e": "As allele frequency q becomes small, almost all recessive alleles reside in healthy heterozygous carriers (Aa), making complete eradication by phenotypic selection impossible.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "A sudden drastic reduction in population size due to an epidemic disease or famine, causing loss of genetic diversity, is called a:",
        "o": ["Genetic bottleneck", "Founder effect", "Assortative mating", "Genetic assimilation"],
        "a": 0,
        "e": "A population bottleneck occurs when an event severely decimates herd numbers, drastically reducing the gene pool of surviving generations.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "In the formula for change in allele frequency due to migration, Δq = m(q_m - q₀), if immigrant frequency q_m equals native frequency q₀, then Δq is:",
        "o": ["1.0", "0", "0.5", "Negative"],
        "a": 1,
        "e": "If immigrant allele frequency matches native frequency (q_m = q₀), migration produces zero change in allele frequency (Δq = 0).",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "Sewall Wright is best known in population genetics for his mathematical description of:",
        "o": ["Genetic drift and inbreeding coefficient", "Polymerase Chain Reaction", "Chromosome karyotyping", "DNA structure"],
        "a": 0,
        "e": "Sewall Wright formulated the inbreeding coefficient (F), the shifting balance theory, and the mathematics of random genetic drift.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },

    # ============================================================
    # u2-s5: Quantitative Genetics & Parameters (18 MCQs)
    # ============================================================
    {
        "q": "Which of the following is a classic continuous quantitative trait in dairy cattle?",
        "o": ["Coat color (Black vs Red)", "Horned vs Polled condition", "305-day Lactation Milk Yield", "Blood group B phenogroup"],
        "a": 2,
        "e": "305-day lactation milk yield is a polygenic quantitative trait showing continuous phenotypic distribution influenced heavily by nutrition and environment.",
        "topicId": "u2-t23",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "In quantitative genetics, the phenotypic value P of an individual is partitioned as:",
        "o": ["P = G + E", "P = G * E", "P = G / E", "P = G - E"],
        "a": 0,
        "e": "Under the standard linear model: Phenotypic Value (P) = Genotypic Value (G) + Environmental Deviation (E).",
        "topicId": "u2-t24",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "The genotypic value G is further partitioned into:",
        "o": ["G = A + D + I", "G = A * D", "G = V_P + V_E", "G = h² + r"],
        "a": 0,
        "e": "G = Additive genetic value (A) + Dominance deviation (D) + Epistatic / Interaction deviation (I).",
        "topicId": "u2-t25",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "The breeding value (BV) of an individual animal is judged strictly by the mean performance of its:",
        "o": ["Ancestors", "Collateral relatives", "Progeny (Offspring)", "Full-sibs"],
        "a": 2,
        "e": "Breeding value is defined as the genetic merit an individual transmits to its progeny, equal to twice the deviation of its progeny mean from the population mean.",
        "topicId": "u2-t24",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Which component of genetic variance is directly transmissible from parents to offspring and responds to mass selection?",
        "o": ["Dominance variance (V_D)", "Additive genetic variance (V_A)", "Epistatic variance (V_I)", "Permanent environmental variance"],
        "a": 1,
        "e": "Only individual genes (not intact diploid genotypes) are passed through gametes; thus Additive genetic variance (V_A) is the sole transmissible genetic component.",
        "topicId": "u2-t25",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Narrow-sense heritability (h²) is mathematically defined as the ratio of:",
        "o": ["V_G / V_P", "V_A / V_P", "V_D / V_A", "V_E / V_P"],
        "a": 1,
        "e": "Narrow-sense heritability is h² = V_A / V_P (Additive genetic variance divided by Total phenotypic variance). Broad-sense is H² = V_G / V_P.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Which of the following classes of livestock traits characteristically exhibits low heritability (h² < 0.15)?",
        "o": ["Carcass traits", "Reproductive and fertility traits (e.g. calving interval, service period)", "Mature body weight", "Milk butterfat percentage"],
        "a": 1,
        "e": "Fertility and fitness traits (calving interval, service period, hatchability) have low heritability (<0.15) and respond poorly to mass selection.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Which method of estimating heritability is most widely used in farm animal breeding using sire component of variance?",
        "o": ["Paternal Half-Sib Correlation", "Twin study method", "Selection experiment", "Offspring-parent covariance"],
        "a": 0,
        "e": "Paternal half-sib correlation (PHS) is the standard method in animal breeding because one bull mates with many dams, yielding large half-sib families: h² = 4 * t.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "In paternal half-sib analysis, the intraclass correlation t is multiplied by which factor to estimate heritability h²?",
        "o": ["2", "3", "4", "0.5"],
        "a": 2,
        "e": "Because paternal half-sibs share 1/4th of their additive genes, the sire component σ²_s = 0.25 * V_A. Therefore, h² = 4 * t.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "In offspring-parent regression where daughter records are regressed on dam records (b_OP), heritability is estimated as:",
        "o": ["h² = b_OP", "h² = 2 * b_OP", "h² = 4 * b_OP", "h² = 0.5 * b_OP"],
        "a": 1,
        "e": "The covariance between one parent and offspring equals 0.5 * V_A. Thus regression coefficient b_OP = 0.5 * h², so h² = 2 * b_OP.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "If daughter on dam regression for 305-day milk yield is b_OP = 0.15, what is the estimated heritability h²?",
        "o": ["0.15", "0.30", "0.60", "0.075"],
        "a": 1,
        "e": "h² = 2 * b_OP = 2 * 0.15 = 0.30.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "Repeatability (r) measures the correlation between repeated records of the same animal and sets the theoretical upper limit to:",
        "o": ["Dominance variance", "Narrow-sense heritability (h²)", "Selection intensity", "Environmental variance"],
        "a": 1,
        "e": "Because repeatability includes permanent environmental variance (r = (V_G + V_Ep) / V_P), it always sets the upper boundary: h² ≤ r.",
        "topicId": "u2-t28",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "Which parameter is computed using repeatability to predict an animal's future productivity for culling decisions?",
        "o": ["Genomic Index", "Most Probable Producing Ability (MPPA)", "Inbreeding Coefficient", "Selection Differential"],
        "a": 1,
        "e": "MPPA combines the herd average with the animal's past records weighted by repeatability: MPPA = Herd_Mean + [n*r / (1 + (n-1)r)] * (Cow_Mean - Herd_Mean).",
        "topicId": "u2-t28",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "What are the two primary biological causes of genetic correlation (r_G) between two traits in farm animals?",
        "o": ["Pleiotropy and Linkage", "Mutation and Inbreeding", "Epistasis and Selection", "Drift and Migration"],
        "a": 0,
        "e": "Pleiotropy (one gene affecting both traits) and chromosomal linkage (genes situated close together on the same chromosome) are the dual causes of genetic correlation.",
        "topicId": "u2-t29",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "In dairy cattle breeding, the genetic correlation between milk yield and milk fat percentage is characteristically:",
        "o": ["Strongly positive (+0.80)", "Negative (-0.25 to -0.40)", "Zero (0.00)", "Perfect positive (+1.00)"],
        "a": 1,
        "e": "Milk yield and fat percentage have an unfavorable negative genetic correlation (-0.25 to -0.40): selecting solely for higher milk volume tends to dilute fat percentage.",
        "topicId": "u2-t29",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "When different genotypes perform differently in different environments (e.g. temperate vs tropical climates), this is called:",
        "o": ["Genotype × Environment (G × E) Interaction", "Epistatic deviation", "Pleiotropic effect", "Inbreeding depression"],
        "a": 0,
        "e": "Genotype-Environment (GxE) interaction occurs when the relative ranking or phenotypic superiority of genotypes changes across contrasting nutritional or climatic environments.",
        "topicId": "u2-t26",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "What is the heritability of a trait if total phenotypic variance V_P = 100 and additive genetic variance V_A = 25?",
        "o": ["0.25", "0.50", "2.5", "4.0"],
        "a": 0,
        "e": "h² = V_A / V_P = 25 / 100 = 0.25 (or 25%).",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Permanent environmental effects (V_Ep) in dairy cattle include permanent damage caused by:",
        "o": ["Annual feed fluctuation", "Severe clinical mastitis leading to loss of an udder quarter", "Ambient temperature change", "Daily milking routine"],
        "a": 1,
        "e": "Permanent environmental effects affect all future lactations of an animal (e.g. loss of a quarter to mastitis, calfhood lung damage), unlike temporary seasonal fluctuations.",
        "topicId": "u2-t25",
        "subSection": "u2-s5",
        "diff": 2
    }
]

unit2_tf = [
    # ============================================================
    # u2-s1: Mendelian Genetics & Gene Interactions (9 T/F)
    # ============================================================
    {
        "q": "Mendel's experiments were conducted on the garden pea (Pisum sativum) and published in 1866.",
        "a": True,
        "e": "Gregor Mendel published 'Versuche über Pflanzen-Hybriden' in 1866 in the Proceedings of the Natural History Society of Brünn.",
        "topicId": "u2-t01",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "Mendel's laws were independently rediscovered in 1900 by Hugo de Vries, Carl Correns, and Erich von Tschermak.",
        "a": True,
        "e": "Three botanists working in three different European countries independently verified Mendel's principles in the year 1900.",
        "topicId": "u2-t01",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "A testcross ratio for a monohybrid cross with complete dominance is 3:1.",
        "a": False,
        "e": "A monohybrid F2 phenotypic ratio is 3:1, but a monohybrid testcross (Tt x tt) yields a 1:1 ratio.",
        "topicId": "u2-t04",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "In incomplete dominance, the phenotypic and genotypic ratios in the F₂ generation are both 1:2:1.",
        "a": True,
        "e": "Because the heterozygote displays an intermediate phenotype (e.g. pink flower), the phenotypic ratio directly reflects the 1:2:1 genotypic ratio.",
        "topicId": "u2-t05",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "The yellow coat color gene in mice (A^Y) is a dominant lethal in homozygous condition.",
        "a": False,
        "e": "The yellow allele is dominant for coat color (heterozygotes are yellow), but is a RECESSIVE lethal (only homozygous A^Y A^Y die in utero).",
        "topicId": "u2-t05",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "A modified dihybrid ratio of 9:7 is indicative of complementary gene interaction.",
        "a": True,
        "e": "Complementary gene interaction yields 9 colored : 7 white, requiring both dominant genes (A-B-) to produce the trait.",
        "topicId": "u2-t06",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "In epistasis, one gene masks or suppresses the phenotypic expression of another non-allelic gene.",
        "a": True,
        "e": "Epistasis is non-allelic interaction where an epistatic gene overrides the phenotypic expression of a hypostatic gene.",
        "topicId": "u2-t06",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "Multiple alleles of a gene occupy different chromosomes in the cell.",
        "a": False,
        "e": "Multiple alleles are alternative forms of the same gene and must occupy the exact same homologous locus on the chromosome.",
        "topicId": "u2-t08",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "The B blood group system in cattle is considered the most polymorphic blood group system in domestic livestock.",
        "a": True,
        "e": "The bovine B system features more than 600 complex phenogroups, making it highly valuable for animal identification and pedigree verification.",
        "topicId": "u2-t08",
        "subSection": "u2-s1",
        "diff": 1
    },

    # ============================================================
    # u2-s2: Cytogenetics, Linkage & Sex Linkage (9 T/F)
    # ============================================================
    {
        "q": "Synapsis and formation of the synaptonemal complex between homologous chromosomes occur in the Zygotene stage of Meiosis I.",
        "a": True,
        "e": "Zygotene is characterized by the precise pairing (synapsis) of homologous chromosomes mediated by the synaptonemal complex.",
        "topicId": "u2-t02",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "Domestic cattle (Bos taurus) have 2n = 60 chromosomes, with all 58 autosomes being acrocentric.",
        "a": True,
        "e": "In cattle, all 58 autosomes are strictly acrocentric, while the X and Y sex chromosomes are submetacentric.",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "Domestic sheep and domestic goats have identical diploid chromosome numbers of 2n = 60.",
        "a": False,
        "e": "Goats have 2n = 60, whereas sheep have 2n = 54 (due to ancestral centric fusions creating 3 metacentric chromosome pairs).",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "In poultry (birds), the male is the heterogametic sex possessing XY chromosomes.",
        "a": False,
        "e": "In birds, males are homogametic (ZZ) and females are heterogametic (ZW).",
        "topicId": "u2-t09",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "Milk production in dairy cows is an example of a sex-limited trait.",
        "a": True,
        "e": "Milk production is governed by autosomal genes present in both sexes but expressed exclusively in females due to physiological and anatomical limitations.",
        "topicId": "u2-t10",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "The maximum possible recombination frequency between two linked genes on a chromosome is 50%.",
        "a": True,
        "e": "Even when crossing over occurs in 100% of tetrads, only non-sister chromatids exchange segments, yielding a maximum of 50% recombinant gametes.",
        "topicId": "u2-t11",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "A freemartin heifer is fertile and capable of normal reproductive cycling.",
        "a": False,
        "e": "Freemartin heifers are completely sterile intersexes with blind-ended vaginas and hypoplastic ovaries due to fetal anastomosis with a male twin.",
        "topicId": "u2-t13",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "The 1/29 Robertsonian translocation in cattle involves the centric fusion of chromosomes 1 and 29, reducing fertility.",
        "a": True,
        "e": "The 1/29 Robertsonian translocation is the most common chromosomal defect in cattle, causing embryonic mortality and reduced conception rates.",
        "topicId": "u2-t13",
        "subSection": "u2-s2",
        "diff": 2
    },
    {
        "q": "Mitochondrial DNA (mtDNA) is inherited biparentally from both the sire and the dam.",
        "a": False,
        "e": "Mitochondrial DNA is inherited strictly maternally via the ovum cytoplasm; sperm mitochondria are degraded upon fertilization.",
        "topicId": "u2-t15",
        "subSection": "u2-s2",
        "diff": 1
    },

    # ============================================================
    # u2-s3: Molecular Genetics & Techniques (9 T/F)
    # ============================================================
    {
        "q": "In double-stranded DNA, Adenine pairs with Thymine via three hydrogen bonds.",
        "a": False,
        "e": "Adenine and Thymine form two hydrogen bonds (A = T). Guanine and Cytosine form three hydrogen bonds (G ≡ C).",
        "topicId": "u2-t16",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "DNA replication proceeds in the 5' to 3' direction on both leading and lagging strands.",
        "a": True,
        "e": "DNA polymerase can add incoming nucleotides only to the free 3'-OH group; hence synthesis on both strands proceeds strictly 5' → 3'.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 2
    },
    {
        "q": "The genetic code is overlapping, meaning adjacent codons share nucleotide bases.",
        "a": False,
        "e": "The genetic code is non-overlapping and commaless; each triplet is read consecutively without sharing bases with neighboring codons.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Taq DNA polymerase used in PCR is isolated from the thermophilic bacterium Thermus aquaticus.",
        "a": True,
        "e": "Taq polymerase is derived from Thermus aquaticus, remaining enzymatic active after repeated cycles at 95°C.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Northern blotting is the laboratory technique used for detecting specific proteins.",
        "a": False,
        "e": "Northern blotting detects RNA. Western blotting is used to detect proteins, while Southern blotting detects DNA.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "During PCR, primer annealing typically occurs at a temperature range of 50°C to 60°C.",
        "a": True,
        "e": "Annealing allows forward and reverse oligonucleotide primers to bind specifically to complementary single-stranded DNA at 50–60°C.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Okazaki fragments are formed on the leading strand during continuous DNA synthesis.",
        "a": False,
        "e": "Okazaki fragments are synthesized discontinuously on the LAGGING strand.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "AUG serves as the universal initiation codon coding for methionine.",
        "a": True,
        "e": "AUG signals the start of translation and incorporates methionine in all eukaryotic organisms.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "Restriction endonucleases recognize specific palindromic nucleotide sequences in DNA.",
        "a": True,
        "e": "Type II restriction enzymes cut DNA at inverted symmetrical palindromic sequences (e.g., GAATTC).",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },

    # ============================================================
    # u2-s4: Population Genetics & Hardy-Weinberg Law (9 T/F)
    # ============================================================
    {
        "q": "In a population at Hardy-Weinberg equilibrium, gene and genotypic frequencies remain constant across generations.",
        "a": True,
        "e": "The Hardy-Weinberg theorem establishes that allelic and genotypic frequencies remain in equilibrium indefinitely in the absence of evolutionary forces.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "If allele frequencies are p = 0.7 and q = 0.3, the expected frequency of heterozygotes in equilibrium is 0.42.",
        "a": True,
        "e": "Heterozygote frequency = 2pq = 2 * 0.7 * 0.3 = 0.42 (or 42%).",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "Genetic drift has a much more pronounced effect in large livestock populations than in small herds.",
        "a": False,
        "e": "Genetic drift is inversely proportional to population size (1 / (2*Ne)); its effects are strongest in very small populations.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "Mutation is the ultimate source of all novel genetic variation in biological populations.",
        "a": True,
        "e": "Mutations generate entirely new alleles, providing raw material for selection and evolution.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "Artificial selection against a lethal recessive allele can completely eliminate the allele from a herd in a single generation.",
        "a": False,
        "e": "Even with 100% culling of affected homozygotes, the recessive allele persists hidden in heterozygous carriers (Aa).",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "The sum of all allelic frequencies at a single locus in a population is always equal to 1.",
        "a": True,
        "e": "By definition, p + q = 1 (or Σ p_i = 1 for multiple alleles).",
        "topicId": "u2-t20",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "Non-random mating changes gene frequencies in a single generation.",
        "a": False,
        "e": "Non-random mating (such as inbreeding) alters genotypic frequencies (increasing homozygotes), but does NOT by itself alter gene (allelic) frequencies.",
        "topicId": "u2-t20",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "The Sewall Wright effect is another name for random genetic drift.",
        "a": True,
        "e": "Sewall Wright developed the mathematical theory of random genetic drift, hence the term Sewall Wright effect.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "A population bottleneck causes an increase in genetic variation in the surviving herd.",
        "a": False,
        "e": "A bottleneck drastically reduces the population size and results in severe loss of genetic diversity and increased inbreeding.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },

    # ============================================================
    # u2-s5: Quantitative Genetics & Parameters (9 T/F)
    # ============================================================
    {
        "q": "Narrow-sense heritability (h²) is defined as the ratio of additive genetic variance (V_A) to total phenotypic variance (V_P).",
        "a": True,
        "e": "Narrow-sense heritability is h² = V_A / V_P, representing the portion of variance responsive to artificial mass selection.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Heritability of a biological trait is a fixed biological constant that never changes across different herds or environments.",
        "a": False,
        "e": "Heritability is a population-specific parameter; it varies depending on allele frequencies, environmental variance, and management in that specific herd.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "Reproductive traits like calving interval and service period generally have high heritability (>0.50).",
        "a": False,
        "e": "Reproductive traits have low heritability (<0.15) and are heavily influenced by feeding, management, and environment.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Repeatability sets the theoretical upper limit for narrow-sense heritability (h² ≤ r).",
        "a": True,
        "e": "Because repeatability includes permanent environmental variance and total genotypic variance, h² can never exceed repeatability r.",
        "topicId": "u2-t28",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "The breeding value of a sire is defined as twice the average deviation of his progeny from the population mean.",
        "a": True,
        "e": "Because a sire contributes half of his genes to each offspring, BV = 2 * (P_progeny - P_pop).",
        "topicId": "u2-t24",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "In paternal half-sib correlation, heritability is estimated as 4 times the intraclass correlation (h² = 4*t).",
        "a": True,
        "e": "Paternal half-sibs share 1/4 of their additive genetic variance; thus h² = 4 * t.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "Genetic correlation between two traits is caused solely by environmental fluctuations.",
        "a": False,
        "e": "Genetic correlation is caused by pleiotropy and linkage. Environmental correlation is caused by shared environmental factors.",
        "topicId": "u2-t29",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Genotype by Environment (G × E) interaction can cause a reranking of sires when daughters are evaluated in contrasting climates.",
        "a": True,
        "e": "GxE interaction occurs when the top-performing sire in a temperate environment is not the best in a tropical heat-stress environment.",
        "topicId": "u2-t26",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Broad-sense heritability (H²) includes both additive and non-additive (dominance and epistatic) genetic variances.",
        "a": True,
        "e": "Broad-sense heritability H² = V_G / V_P = (V_A + V_D + V_I) / V_P.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 1
    }
]

unit2_fib = [
    # ============================================================
    # u2-s1: Mendelian Genetics & Gene Interactions (9 FIB)
    # ============================================================
    {
        "q": "Gregor Johann Mendel conducted his genetic hybridization experiments on the garden pea, scientifically named ______ sativum.",
        "a": ["Pisum", "pisum"],
        "a_display": "Pisum",
        "e": "Mendel worked on the garden pea, Pisum sativum.",
        "topicId": "u2-t01",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "The fundamental terms 'Gene', 'Genotype', and 'Phenotype' were coined in 1909 by Wilhelm ______.",
        "a": ["Johannsen", "Wilhelm Johannsen"],
        "a_display": "Johannsen",
        "e": "Danish botanist Wilhelm Johannsen coined the terms Gene, Genotype, and Phenotype in 1909.",
        "topicId": "u2-t01",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "Mendel's First Law is known as the Law of ______.",
        "a": ["Segregation", "purity of gametes"],
        "a_display": "Segregation",
        "e": "The Law of Segregation states that allele pairs separate during gamete formation.",
        "topicId": "u2-t04",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "A testcross of a heterozygous monohybrid individual (Tt × tt) produces a phenotypic ratio of ______.",
        "a": ["1:1", "1 to 1"],
        "a_display": "1:1",
        "e": "A monohybrid testcross yields 50% dominant and 50% recessive offspring (1:1).",
        "topicId": "u2-t04",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "Roan coat color in Shorthorn cattle is a classic example of ______ where both red and white hairs are expressed.",
        "a": ["codominance"],
        "a_display": "Codominance",
        "e": "Codominance allows both alleles to be fully and simultaneously expressed in heterozygotes.",
        "topicId": "u2-t05",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "In poultry, complementary gene interaction for walnut comb produces an F₂ ratio of 9 to ______.",
        "a": ["7", "seven"],
        "a_display": "7",
        "e": "Complementary gene interaction gives a 9:7 phenotypic ratio.",
        "topicId": "u2-t06",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "The phenomenon where a single gene affects multiple unrelated phenotypic traits is called ______.",
        "a": ["pleiotropy", "pleiotropism"],
        "a_display": "Pleiotropy",
        "e": "Pleiotropy refers to a single locus having phenotypic consequences across multiple systems.",
        "topicId": "u2-t07",
        "subSection": "u2-s1",
        "diff": 1
    },
    {
        "q": "An environmentally produced phenotype that simulates a genetic mutation is called a ______.",
        "a": ["phenocopy"],
        "a_display": "Phenocopy",
        "e": "A phenocopy mimics a mutant phenotype but has an unaltered wild-type genotype.",
        "topicId": "u2-t07",
        "subSection": "u2-s1",
        "diff": 2
    },
    {
        "q": "The most polymorphic and complex blood group system in cattle is the ______ system.",
        "a": ["B", "B system"],
        "a_display": "B",
        "e": "The bovine B blood group system contains over 600 phenogroups.",
        "topicId": "u2-t08",
        "subSection": "u2-s1",
        "diff": 1
    },

    # ============================================================
    # u2-s2: Cytogenetics, Linkage & Sex Linkage (9 FIB)
    # ============================================================
    {
        "q": "Crossing over occurs during the ______ sub-stage of Prophase I of meiosis.",
        "a": ["pachytene"],
        "a_display": "Pachytene",
        "e": "Genetic crossing over and chiasma formation occur during pachytene.",
        "topicId": "u2-t02",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "The diploid chromosome number (2n) of domestic cattle is ______.",
        "a": ["60", "sixty"],
        "a_display": "60",
        "e": "Cattle (Bos taurus and Bos indicus) possess 2n = 60 chromosomes.",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "The diploid chromosome number (2n) of the river buffalo is ______.",
        "a": ["50", "fifty"],
        "a_display": "50",
        "e": "River buffalo (Bubalus bubalis) has 2n = 50 chromosomes.",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "The diploid chromosome number (2n) of domestic sheep is ______.",
        "a": ["54", "fifty-four", "fifty four"],
        "a_display": "54",
        "e": "Domestic sheep (Ovis aries) have 2n = 54 chromosomes.",
        "topicId": "u2-t03",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "In birds and poultry, the heterogametic sex is the female, possessing ______ sex chromosomes.",
        "a": ["ZW", "zw"],
        "a_display": "ZW",
        "e": "Avian females are ZW heterogametic, while males are ZZ homogametic.",
        "topicId": "u2-t09",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "The dark heterochromatic inactive X chromosome visible in female somatic cells is called a ______ body.",
        "a": ["Barr", "Barr body"],
        "a_display": "Barr",
        "e": "Murray Barr discovered the Barr body (sex chromatin) representing the lyonized inactive X chromosome.",
        "topicId": "u2-t09",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "One map unit on a genetic chromosome linkage map is called a ______.",
        "a": ["centiMorgan", "cM", "centimorgan"],
        "a_display": "centiMorgan (cM)",
        "e": "1 centiMorgan (cM) represents 1% recombination frequency between two linked loci.",
        "topicId": "u2-t11",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "A sterile heifer born co-twin with a bull calf in cattle is called a ______.",
        "a": ["freemartin"],
        "a_display": "Freemartin",
        "e": "A freemartin is an infertile female twin modified by male fetal hormones via placental vascular fusion.",
        "topicId": "u2-t13",
        "subSection": "u2-s2",
        "diff": 1
    },
    {
        "q": "The centric fusion of two acrocentric chromosomes is called a ______ translocation.",
        "a": ["Robertsonian", "robertsonian translocation"],
        "a_display": "Robertsonian",
        "e": "Robertsonian translocations involve fusion at the centromere (e.g. 1/29 translocation in cattle).",
        "topicId": "u2-t13",
        "subSection": "u2-s2",
        "diff": 2
    },

    # ============================================================
    # u2-s3: Molecular Genetics & Techniques (9 FIB)
    # ============================================================
    {
        "q": "In DNA base pairing, Guanine pairs with Cytosine via ______ hydrogen bonds.",
        "a": ["3", "three"],
        "a_display": "3 (three)",
        "e": "G and C pair via three hydrogen bonds (G ≡ C).",
        "topicId": "u2-t16",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The short DNA fragments synthesized discontinuously on the lagging strand are ______ fragments.",
        "a": ["Okazaki", "okazaki fragments"],
        "a_display": "Okazaki",
        "e": "Okazaki fragments are formed on the lagging strand during DNA replication.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The enzyme that seals nicks by creating phosphodiester bonds during DNA replication is DNA ______.",
        "a": ["ligase"],
        "a_display": "Ligase",
        "e": "DNA ligase joins Okazaki fragments by catalyzing phosphodiester bond formation.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The universal start codon that initiates protein translation is ______.",
        "a": ["AUG"],
        "a_display": "AUG",
        "e": "AUG is the universal start codon coding for methionine.",
        "topicId": "u2-t17",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The Polymerase Chain Reaction (PCR) was invented by Kary ______ in 1983.",
        "a": ["Mullis", "Kary Mullis"],
        "a_display": "Mullis",
        "e": "Kary Mullis conceived and developed PCR, earning the 1993 Nobel Prize in Chemistry.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The thermostable DNA polymerase used in PCR is isolated from Thermus ______.",
        "a": ["aquaticus"],
        "a_display": "aquaticus",
        "e": "Taq polymerase is purified from the thermophilic bacterium Thermus aquaticus.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The three steps in a PCR cycle are Denaturation, Annealing, and ______.",
        "a": ["Extension", "elongation", "extension/elongation"],
        "a_display": "Extension",
        "e": "A PCR thermal cycle consists of Denaturation (94°C), Annealing (55°C), and Extension (72°C).",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "During agarose gel electrophoresis, negatively charged DNA fragments migrate toward the positive ______.",
        "a": ["anode"],
        "a_display": "Anode",
        "e": "DNA carries a negative charge from its phosphate backbone and migrates toward the positive anode.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },
    {
        "q": "The molecular blotting technique used specifically to detect RNA molecules is ______ blotting.",
        "a": ["Northern", "northern blotting"],
        "a_display": "Northern",
        "e": "Northern blotting detects RNA, Southern detects DNA, and Western detects proteins.",
        "topicId": "u2-t18",
        "subSection": "u2-s3",
        "diff": 1
    },

    # ============================================================
    # u2-s4: Population Genetics & Hardy-Weinberg Law (9 FIB)
    # ============================================================
    {
        "q": "The sum of all allelic frequencies at a single genetic locus (p + q) is equal to ______.",
        "a": ["1", "1.0", "one"],
        "a_display": "1.0",
        "e": "In population genetics, the total frequency of all alleles at a locus equals 1 (p + q = 1).",
        "topicId": "u2-t20",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "The Hardy-Weinberg law was formulated in the year ______.",
        "a": ["1908"],
        "a_display": "1908",
        "e": "G. H. Hardy and Wilhelm Weinberg formulated the equilibrium principle in 1908.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "Under Hardy-Weinberg equilibrium, the expected frequency of heterozygous individuals is 2______.",
        "a": ["pq"],
        "a_display": "pq",
        "e": "The genotypic expansion is p² + 2pq + q² = 1; heterozygotes are represented by 2pq.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "When testing Hardy-Weinberg equilibrium for two alleles using Chi-Square, the degrees of freedom is ______.",
        "a": ["1", "one"],
        "a_display": "1",
        "e": "Degrees of freedom = 3 genotypes - 2 alleles = 1 df.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "Random fluctuations in allele frequency in small populations due to gametic sampling is called genetic ______.",
        "a": ["drift"],
        "a_display": "Drift",
        "e": "Genetic drift (Sewall Wright effect) alters allele frequencies by chance in small populations.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "The establishment of a new population by a small group with unrepresentative allele frequencies is the ______ effect.",
        "a": ["founder", "founder effect"],
        "a_display": "Founder",
        "e": "The founder effect is a form of genetic drift seen when a small group establishes a new herd.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },
    {
        "q": "The relationship between relative fitness W and the selection coefficient s is s = 1 - ______.",
        "a": ["W", "w"],
        "a_display": "W",
        "e": "The selection coefficient measures the proportional disadvantage: s = 1 - W.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "Random mating in a population is also referred to as ______.",
        "a": ["panmixia"],
        "a_display": "Panmixia",
        "e": "Panmixia is the biological term for completely random mating where every individual has an equal chance of mating.",
        "topicId": "u2-t21",
        "subSection": "u2-s4",
        "diff": 2
    },
    {
        "q": "The ultimate biological source of all brand new genetic alleles is ______.",
        "a": ["mutation"],
        "a_display": "Mutation",
        "e": "Mutation generates new genetic alleles upon which other evolutionary forces act.",
        "topicId": "u2-t22",
        "subSection": "u2-s4",
        "diff": 1
    },

    # ============================================================
    # u2-s5: Quantitative Genetics & Parameters (9 FIB)
    # ============================================================
    {
        "q": "In the standard quantitative model, Phenotype = Genotype + ______.",
        "a": ["Environment", "E"],
        "a_display": "Environment",
        "e": "Phenotypic performance is partitioned into genetic and environmental components: P = G + E.",
        "topicId": "u2-t24",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "The genetic variance component that is directly transmissible to offspring is ______ genetic variance (V_A).",
        "a": ["additive", "additive genetic"],
        "a_display": "Additive",
        "e": "Additive genetic variance V_A is the only transmissible component that responds to selection.",
        "topicId": "u2-t25",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "Narrow-sense heritability (h²) is the ratio of additive genetic variance to total ______ variance.",
        "a": ["phenotypic", "phenotypic variance"],
        "a_display": "Phenotypic",
        "e": "Narrow-sense heritability is h² = V_A / V_P.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "In paternal half-sib analysis, heritability is estimated as ______ times the intraclass correlation (t).",
        "a": ["4", "four"],
        "a_display": "4",
        "e": "Since half-sibs share 1/4th of additive genes, h² = 4 * t.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "In offspring on single-parent regression (b_OP), heritability is estimated as ______ times b_OP.",
        "a": ["2", "two"],
        "a_display": "2",
        "e": "Because one parent passes half its genes to its offspring, h² = 2 * b_OP.",
        "topicId": "u2-t27",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "Repeatability sets the theoretical upper limit to narrow-sense ______.",
        "a": ["heritability", "h2", "h²"],
        "a_display": "Heritability",
        "e": "Heritability cannot exceed repeatability: h² ≤ r.",
        "topicId": "u2-t28",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "The formula used to predict an animal's future producing performance for culling is Most Probable Producing ______ (MPPA).",
        "a": ["Ability"],
        "a_display": "Ability",
        "e": "MPPA (Most Probable Producing Ability) estimates future lactation yield using repeatability.",
        "topicId": "u2-t28",
        "subSection": "u2-s5",
        "diff": 2
    },
    {
        "q": "The primary genetic causes of genetic correlation are pleiotropy and chromosomal ______.",
        "a": ["linkage"],
        "a_display": "Linkage",
        "e": "Pleiotropy and genetic linkage are the two causes of genetic correlation between traits.",
        "topicId": "u2-t29",
        "subSection": "u2-s5",
        "diff": 1
    },
    {
        "q": "When genotypes perform differently across different management conditions, this is called Genotype by Environment ______.",
        "a": ["interaction", "GxE interaction"],
        "a_display": "Interaction",
        "e": "G × E interaction occurs when the relative ranking of genotypes alters across environments.",
        "topicId": "u2-t26",
        "subSection": "u2-s5",
        "diff": 1
    }
]
