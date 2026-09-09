# -*- coding: utf-8 -*-
"""
Unit 2 - Part 2: Topics u2-t08 to u2-t14
Principles of Animal and Population Genetics (IVRI Undergrad 10 CGPA Standard)
"""

topics = {}

topics["u2-t08"] = {
    "summary": "Multiple alleles represent three or more alternative forms of a gene occupying the same locus across a population, governing diverse livestock blood group systems used in parentage verification and forensic testing.",
    "desc": (
        "<b>CONCEPT AND CHARACTERISTICS OF MULTIPLE ALLELES</b><br>"
        "Classical Mendelian genetics describes genes with two alternative alleles (e.g., A and a). "
        "However, because a gene is a linear sequence of hundreds or thousands of nucleotide base pairs, spontaneous mutations can occur at different points within the gene, generating multiple alternative states. "
        "When <b>three or more alternative alleles</b> occupy the exact same homologous chromosomal locus in a population, they constitute a <b>Multiple Allelic Series</b>.<br><br>"
        "<b>Essential Characteristics of Multiple Alleles:</b>"
        "<ul>"
        "<li>All alleles of the series occupy the <b>exact same chromosomal locus</b> on homologous chromosomes.</li>"
        "<li>An individual diploid organism can possess <b>at most two alleles</b> of the series at any one time; a haploid gamete carries only one allele.</li>"
        "<li><b>No Crossing Over:</b> Recombination cannot occur between alleles of a multiple allelic series because they occupy the identical chromosomal position.</li>"
        "<li>They always control different manifestations of the <b>same physiological or biochemical trait</b> (e.g., coat pigment, blood group glycoprotein antigen).</li>"
        "<li>They frequently exhibit a hierarchy of dominance (e.g., <code>A₁ &gt; A₂ &gt; A₃ &gt; a</code>) or codominance.</li>"
        "<li><b>Number of Possible Genotypes:</b> For a series with 'n' multiple alleles, the total number of possible diploid genotypes is: "
        "<br><code>Total Genotypes = n(n + 1) / 2</code>"
        "<br>where 'n' are homozygous genotypes and <code>n(n - 1) / 2</code> are heterozygous genotypes.</li>"
        "</ul><br>"
        "<b>BLOOD GROUP SYSTEMS IN DOMESTIC ANIMALS</b><br>"
        "Blood groups are determined by polymorphic glycoprotein and glycolipid surface antigens on erythrocyte membranes, inherited as multiple allelic systems:"
        "<ul>"
        "<li><b>Cattle Blood Groups:</b>"
        "<br>Cattle possess <b>11 major recognized blood group systems</b>: <b>A, B, C, F-V, J, L, M, S, Z, R'-S', and T'</b>."
        "<br>&bull; <i>The Bovine B Blood Group System:</i> The most complex multiple allelic system known in animal genetics! Possesses over <b>1,000 distinct phenogroups (alleles)</b> at a single locus, encoding combinations of more than 40 antigenic factors (B, G, K, I, O, P, Q, T, Y, etc.). Provides extraordinary individual specificity for parentage identification."
        "<br>&bull; <i>The J System:</i> A soluble, humoral lipid antigen synthesized in tissues, secreted into blood plasma, and secondarily absorbed onto the erythrocyte surface (not synthesized within the RBC membrane!).</li>"
        "<li><b>Sheep Blood Groups:</b> 7 systems recognized: <b>A, B, C, D, M, R-O, and X</b>. The ovine B system is homologous to the bovine B system, highly polymorphic. The M system controls active potassium transport across erythrocyte membranes (high potassium HK vs low potassium LK phenotypes).</li>"
        "<li><b>Horse Blood Groups:</b> 8 major systems: <b>A, C, D, K, P, Q, U, and T</b>. Alleles <code>A^a</code> and <code>Q^a</code> are clinically significant as the primary causal triggers of fatal <b>Neonatal Isoerythrolysis (NI)</b> in newborn foals.</li>"
        "<li><b>Swine Blood Groups:</b> 16 systems recognized: <b>A to P</b>. The porcine <b>H blood group system</b> is genetically linked to the <i>Halothane (HAL / RYR1)</i> gene governing Porcine Stress Syndrome (PSS) and Pale Soft Exudative (PSE) pork.</li>"
        "<li><b>Dog Blood Groups (DEA System):</b> Dog Erythrocyte Antigen (DEA) system comprising DEA 1.1, DEA 1.2, DEA 3, 4, 5, 7. DEA 1.1 is the most potent antigen; DEA 1.1 negative dogs serve as universal canine blood donors.</li>"
        "</ul><br>"
        "<b>PRACTICAL APPLICATIONS IN VETERINARY SCIENCE</b>"
        "<ol>"
        "<li><b>Parentage Verification and Pedigree Certification:</b> In artificial insemination (AI) studs, multiple allelic blood typing and microsatellites/SNPs exclude falsely registered sires with &gt; 99% statistical accuracy.</li>"
        "<li><b>Diagnosis of Freemartinism:</b> In heterosexual twin calves (bull and heifer), vascular placental anastomoses allow mutual blood chimerism. If the heifer shares two distinct populations of blood types (erythrocyte chimerism), she is definitively diagnosed as a sterile freemartin.</li>"
        "<li><b>Forensic Medicine:</b> Matching animal bloodstains in cases of cattle rustling, poaching, and animal cruelty.</li>"
        "<li><b>Blood Transfusion Compatibility:</b> Preventing fatal hemolytic transfusion reactions in companion animals and neonatal isoerythrolysis in equines.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Mathematical Combinatorics of Multiple Alleles:</b><br>"
        "For 'n' multiple alleles, calculating genotypic diversity is an essential exam numerical: "
        "<br>&bull; If a gene has <code>n = 4</code> alleles (e.g., rabbit coat color: C, c^ch, c^h, c): "
        "<br>Total genotypes = <code>4(4 + 1) / 2 = 10 genotypes</code> (4 homozygous + 6 heterozygous). "
        "<br>&bull; In the Bovine B blood group with approximately 1,000 distinct alleles: "
        "<br>Total possible genotypes = <code>1000 &times; 1001 / 2 = 500,500 distinct genotypes</code>! "
        "This colossal combinatorial diversity makes it nearly impossible for two unrelated bulls to share the identical B-system genotype, providing near-absolute forensic certainty in bull registration."
    ),
    "keyPoints": [
        "Multiple alleles are 3 or more alternative alleles of a gene occupying the same locus on homologous chromosomes.",
        "An individual diploid animal carries at most two alleles of a multiple allelic series; a gamete carries one.",
        "No crossing over can occur between alleles of a multiple allelic series.",
        "Total number of genotypes possible for n alleles: Total = n(n + 1) / 2.",
        "Cattle possess 11 major blood group systems: A, B, C, F-V, J, L, M, S, Z, R'-S', T'.",
        "The Bovine B blood group system is the most polymorphic system known, with over 1,000 alleles.",
        "The Bovine J blood group antigen is unique: soluble in plasma and secondarily adsorbed onto RBC membranes.",
        "Equine blood group antigens Aᵃ and Qᵃ are the primary causes of fatal Neonatal Isoerythrolysis (NI) in foals.",
        "The Swine H blood group system is genetically linked to the Halothane gene (PSS / PSE pork defect).",
        "Canine blood groups use the DEA (Dog Erythrocyte Antigen) system; DEA 1.1 negative is the universal donor.",
        "Blood typing and DNA profiling provide >99% exclusion power for livestock parentage verification.",
        "Erythrocyte chimerism (mixed blood types) definitively confirms freemartinism in bovine twin heifers."
    ],
    "clinical": (
        "In Thoroughbred equine breeding, Neonatal Isoerythrolysis occurs when an <code>A^a</code> negative mare is bred to an <code>A^a</code> positive stallion. The mare becomes sensitized to fetal RBCs during gestation. Upon foaling, the foal ingests high-titer anti-Aᵃ antibodies in maternal colostrum, triggering massive intravascular hemolysis, severe icterus, hemoglobinuria, and fatal anemia within 48 hours unless colostrum is immediately withheld."
    ),
    "tables": [
        {
            "title": "Major Blood Group Systems Across Domestic Animals and Their Veterinary Significance",
            "headers": ["Livestock Species", "Number of Systems", "Major Blood Group Systems", "Clinical / Applied Genetic Significance"],
            "rows": [
                ["Cattle (Bos taurus / indicus)", "11 Systems", "A, B, C, F-V, J, L, M, S, Z, R'-S', T'", "B system >1000 alleles; parentage testing; freemartin chimerism"],
                ["Horse (Equus caballus)", "8 Systems", "A, C, D, K, P, Q, U, T", "Aᵃ and Qᵃ antigens cause fatal Neonatal Isoerythrolysis (NI) in foals"],
                ["Sheep (Ovis aries)", "7 Systems", "A, B, C, D, M, R-O, X", "M system controls active red cell potassium levels (HK vs LK)"],
                ["Pig (Sus scrofa)", "16 Systems", "A through P (notably A, E, H)", "H system linked to malignant hyperthermia and Halothane gene"],
                ["Dog (Canis familiaris)", "8 Systems", "DEA 1.1, 1.2, 3, 4, 5, 7", "DEA 1.1 is highly antigenic; DEA 1.1 negative is universal donor dog"]
            ]
        }
    ],
    "img": "",
    "tags": ["multiple-alleles", "blood-groups", "bovine-b-system", "neonatal-isoerythrolysis", "parentage-testing", "dea-system"]
}

topics["u2-t09"] = {
    "summary": "Sex determination mechanisms define the genetic and chromosomal triggers directing gonadogenesis, balanced by dosage compensation mechanisms like X-inactivation in mammals to equalize X-linked gene expression between sexes.",
    "desc": (
        "<b>CHROMOSOMAL MECHANISMS OF SEX DETERMINATION</b><br>"
        "In bisexual organisms, sex determination is the biological process that directs an undifferentiated bipotential embryonic gonad to develop into either a testis or an ovary:"
        "<ul>"
        "<li><b>1. XX-XY Mechanism (Male Heterogametic):</b>"
        "<br>Occurs in all placental mammals (cattle, buffalo, sheep, goat, horse, pig, dog, cat) and <i>Drosophila</i>. "
        "<br>&bull; Females possess two morphologically homomorphic sex chromosomes (<code>XX</code>) and produce only one type of gamete: all ova contain one X chromosome (<b>Homogametic Sex</b>). "
        "<br>&bull; Males possess two heteromorphic sex chromosomes (<code>XY</code>) and produce two distinct types of spermatozoa in equal 50:50 proportions: 50% carry an X chromosome (gynosperm), and 50% carry a Y chromosome (androsperm) (<b>Heterogametic Sex</b>). "
        "<br>&bull; The male gamete determines the sex of the zygote at the instant of fertilization!</li>"
        "<li><b>2. ZZ-ZW Mechanism (Female Heterogametic):</b>"
        "<br>Occurs in domestic birds (chicken, turkey, duck, quail) and reptiles. "
        "<br>&bull; Males possess two homomorphic Z chromosomes (<code>ZZ</code>) and are <b>Homogametic</b>. "
        "<br>&bull; Females possess one Z and one smaller W chromosome (<code>ZW</code>) and are <b>Heterogametic</b>, producing two types of ova (50% Z-bearing and 50% W-bearing). "
        "<br>&bull; In birds, the <b>female determines the sex of the offspring</b>!</li>"
        "<li><b>3. XX-XO Mechanism:</b> Male possesses only a single X chromosome (XO) and produces two types of sperm (X and no sex chromosome); females are XX (e.g., grasshoppers, bugs).</li>"
        "<li><b>4. Genic Balance Theory (Calvin Bridges, 1921):</b>"
        "<br>Demonstrated in <i>Drosophila</i> that sex is determined not by the mere presence of Y, but by the ratio of X chromosomes to Autosome sets: <code>Sex Index = X / A</code>. "
        "<br>&bull; X/A = 1.0 &rarr; Female; X/A = 0.5 &rarr; Male; X/A &gt; 1.0 &rarr; Metafemale; X/A &lt; 0.5 &rarr; Metamale. (Note: in mammals, Y is dominant and the X/A ratio does not govern sex).</li>"
        "</ul><br>"
        "<b>MOLECULAR BASIS OF MAMMALIAN SEX DETERMINATION: THE SRY GENE</b><br>"
        "In mammals, male sex determination is actively directed by the dominant action of the Y chromosome. "
        "The critical master switch is the <b>SRY Gene (Sex-determining Region Y)</b> located on the short arm (p) of the Y chromosome, encoding a 204-amino acid transcription factor known as <b>Testis-Determining Factor (TDF)</b>:"
        "<ul>"
        "<li><b>If SRY is Present:</b> TDF activates downstream transcription factor <i>SOX9</i> &rarr; differentiates bipotential genital ridge into <b>Sertoli cells</b> and <b>Leydig cells</b>. "
        "<br>&bull; Sertoli cells secrete <b>Anti-M&uuml;llerian Hormone (AMH)</b>, causing regression of female M&uuml;llerian ducts. "
        "<br>&bull; Leydig cells secrete <b>Testosterone</b> (stabilizes male Wolffian ducts into epididymis, vas deferens) and <b>Dihydrotestosterone (DHT)</b> (directs development of penis, scrotum, and prostate).</li>"
        "<li><b>If SRY is Absent (XX):</b> In the absence of SRY, ovarian genes (<i>WNT4, RSPO1, FOXL2</i>) are expressed &rarr; cortex develops into <b>Ovary</b> &rarr; M&uuml;llerian ducts develop into oviducts, uterus, and cranial vagina; Wolffian ducts regress.</li>"
        "</ul><br>"
        "<b>DOSAGE COMPENSATION AND THE LYON HYPOTHESIS</b><br>"
        "Because female mammals possess two X chromosomes (XX) while males possess only one (XY), females potentially have double the dosage of X-linked gene products. "
        "To equalize gene expression between sexes, nature employs <b>Dosage Compensation</b> through <b>Random X-Chromosome Inactivation</b>, formulated by British geneticist <b>Mary F. Lyon (1961)</b> (The <b>Lyon Hypothesis</b>):<br>"
        "<b>Principles of the Lyon Hypothesis:</b>"
        "<ol>"
        "<li>In female mammalian somatic cells, one of the two X chromosomes is randomly and permanently inactivated during early embryonic blastocyst development (approx. 16-cell to blastocyst stage).</li>"
        "<li>The inactivation is <b>random</b>: in some cells, the maternal X (X_m) is inactivated; in other cells, the paternal X (X_p) is inactivated.</li>"
        "<li>The inactivation is <b>clonal and irreversible</b>: once an X chromosome is inactivated in an embryonic cell, all mitotic daughter cells descendents maintain the exact same X inactivated.</li>"
        "<li>The inactivated, heterochromatinized X chromosome condenses against the inner nuclear membrane during interphase, visible under light microscopy as a dark, dense chromatic mass termed the <b>Barr Body (Sex Chromatin)</b>. "
        "<br>Formula: <code>Number of Barr Bodies = Total X Chromosomes - 1</code>. "
        "<br>(Normal female XX = 1 Barr body; Normal male XY = 0 Barr bodies).</li>"
        "<li><i>Molecular Engine:</i> Regulated by the <b>X-inactivation center (XIC)</b>, which transcribes a 17-kb non-coding RNA called <b>XIST (X-inactive specific transcript)</b> that coats the inactive X chromosome in cis, recruiting histone methyltransferases to permanently condense it into heterochromatin.</li>"
        "</ol><br>"
        "<b>Cellular Mosaicism in Females: Calico and Tortoiseshell Cats:</b>"
        "<br>Female mammals are genetic <b>mosaics</b>. In domestic cats, the coat color gene for Orange (<code>O</code>) vs Black (<code>o</code>) is X-linked. "
        "Heterozygous females (<code>X^O X^o</code>) exhibit patches of orange fur (where paternal X^o was inactivated) and patches of black fur (where maternal X^O was inactivated). "
        "Combined with autosomal piebald white spotting (S gene), this produces the classic tri-color <b>Calico cat</b>. "
        "<i>Topper Rule:</i> <b>Calico and tortoiseshell cats are almost exclusively FEMALE!</b> A male calico cat is an extreme cytogenetic anomaly possessing Klinefelter syndrome (<code>XXY</code> with 39 chromosomes, sterile)."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Avian Dosage Compensation vs Mammalian Lyonization:</b><br>"
        "A major theoretical contrast tested in competitive examinations: "
        "Birds (ZZ male / ZW female) <b>DO NOT undergo global chromosome inactivation</b>! "
        "There is no W-inactivation or Z-inactivation in male birds; male birds do not form Barr bodies. "
        "Instead, avian dosage compensation is gene-specific and incomplete: the dosage-sensitive gene <b>DMRT1 (Doublesex and MAB-3 Related Transcription Factor 1)</b> located on the Z chromosome determines sex through a direct quantitative dosage effect. "
        "Two doses of DMRT1 (<code>ZZ</code>) trigger male testicular differentiation, whereas a single dose (<code>ZW</code>) is insufficient, allowing female ovarian development."
    ),
    "keyPoints": [
        "In mammals, males are heterogametic (XY) and females are homogametic (XX); the male determines offspring sex.",
        "In birds (poultry), females are heterogametic (ZW) and males are homogametic (ZZ); the female determines offspring sex.",
        "Genic Balance Theory in Drosophila (Bridges) determines sex by the ratio of X chromosomes to Autosome sets (X/A).",
        "The SRY gene on the mammalian Y chromosome encodes Testis-Determining Factor (TDF), triggering male gonadogenesis.",
        "Sertoli cells secrete Anti-Müllerian Hormone (AMH); Leydig cells secrete Testosterone.",
        "The Lyon Hypothesis (Mary Lyon, 1961) explains dosage compensation through random X-inactivation in female mammals.",
        "X-inactivation occurs during early blastocyst development, is random, clonal, and irreversible.",
        "The condensed, inactivated X chromosome forms the Barr body (Sex Chromatin) against the nuclear membrane.",
        "Number of Barr bodies = Total X Chromosomes - 1 (Normal XX female has 1 Barr body; XY male has 0).",
        "X-inactivation is mediated by the non-coding RNA XIST transcribed from the X-inactivation center (XIC).",
        "Calico and tortoiseshell cats are genetic mosaics resulting from random X-inactivation in XᴼXᵒ heterozygous females.",
        "Birds do not undergo global chromosome inactivation; avian sex determination is mediated by Z-linked DMRT1 dosage."
    ],
    "clinical": (
        "In clinical cytogenetics of dairy calves born with ambiguous external genitalia, gonadal dysgenesis, or male pseudo-hermaphroditism, peripheral blood smear cytology is used to screen for Barr bodies in polymorphonuclear neutrophils (where they appear as distinctive 'drumstick' nuclear appendages). Absence of drumsticks in a phenotypic female confirms Turner syndrome (XO) or XY sex-reversal."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Sex Determination Systems Across Animal Phyla",
            "headers": ["Parameter", "Mammalian System (Placental Livestock)", "Avian System (Domestic Poultry / Birds)"],
            "rows": [
                ["Chromosomal Mechanism", "XX - XY System", "ZZ - ZW System"],
                ["Heterogametic Sex", "Male (XY) produces two types of sperm (50% X, 50% Y)", "Female (ZW) produces two types of ova (50% Z, 50% W)"],
                ["Sex-Determining Parent", "The Male (Sire) determines the sex of the offspring", "The Female (Dam) determines the sex of the offspring"],
                ["Master Genetic Switch", "SRY gene on Y chromosome producing TDF protein", "DMRT1 gene dosage on Z chromosome (ZZ = male, ZW = female)"],
                ["Dosage Compensation", "Global X-inactivation (Lyonization forming Barr bodies)", "No chromosome inactivation; incomplete gene-by-gene compensation"],
                ["Sex-Linked Gene Transmission", "Sire transmits X-linked genes strictly to daughters", "Dam transmits Z-linked genes strictly to sons (Criss-cross)"]
            ]
        }
    ],
    "img": "",
    "tags": ["sex-determination", "sry-gene", "dosage-compensation", "lyon-hypothesis", "barr-body", "calico-cat", "dmrt1"]
}

topics["u2-t10"] = {
    "summary": "Sex-related inheritance includes Sex-Linked traits (governed by genes on sex chromosomes showing criss-cross transmission), Sex-Limited traits (expressed exclusively in one sex), and Sex-Influenced traits (where dominance shifts with sex).",
    "desc": (
        "<b>CLASSIFICATION OF SEX-RELATED INHERITANCE</b><br>"
        "Not all traits associated with sex follow the same genetic mechanisms. "
        "Veterinary genetics strictly classifies sex-related inheritance into three fundamentally distinct categories: <b>Sex-Linked</b>, <b>Sex-Limited</b>, and <b>Sex-Influenced</b> traits.<br><br>"
        "<b>1. SEX-LINKED INHERITANCE (X-LINKED OR Z-LINKED)</b><br>"
        "Governed by genes physically located on the non-homologous differential segment of the sex chromosomes (X in mammals, Z in birds) that have no homologous counter-alleles on the Y or W chromosome:"
        "<ul>"
        "<li><b>Hallmark Feature — Criss-Cross Inheritance:</b>"
        "<br>An X-linked recessive trait is transmitted from an affected <b>father &rarr; carrier daughter &rarr; grandson</b>, skipping the intermediate female generation phenotypically. A father can <i>never</i> transmit an X-linked gene to his son because he contributes only his Y chromosome to male progeny.</li>"
        "<li><b>Hemizygous State in Males:</b>"
        "<br>Mammalian males possess only one X chromosome (<code>X^a Y</code>). Therefore, a single recessive mutant allele on the X chromosome is <b>always expressed phenotypically</b> in males! Recessive X-linked conditions are vastly more frequent in males than females.</li>"
        "<li><b>Veterinary Livestock Examples:</b>"
        "<br>&bull; <i>Hemophilia A (Factor VIII Deficiency) in Dogs:</i> Severe X-linked bleeding disorder; affected males (<code>X^h Y</code>) bleed profusely; carrier females (<code>X^H X^h</code>) are clinically normal."
        "<br>&bull; <i>Anhidrotic Ectodermal Dysplasia in Cattle:</i> X-linked absence of sweat glands and teeth."
        "<br>&bull; <i>Feather Sexing in Day-Old Commercial Chicks (Avian Z-Linkage):</i> "
        "Rapid feathering (<code>k</code>, recessive) vs Slow feathering (<code>K</code>, dominant) is Z-linked. Crossing slow-feathering females (<code>Z^K W</code>) with rapid-feathering males (<code>Z^k Z^k</code>) produces: "
        "<b>All male chicks slow feathering (<code>Z^K Z^k</code>)</b> and <b>all female chicks rapid feathering (<code>Z^k W</code>)</b>! "
        "Hatchery technicians visually sex day-old chicks at 100% accuracy within seconds by inspecting primary wing feather length, eliminating vent sexing costs. "
        "<br>&bull; <i>Barred Plumage in Chickens (Barred Plymouth Rock):</i> Dominant Z-linked gene <code>B</code> produces white bars on black feathers. Barred females (<code>Z^B W</code>) mated to non-barred black males (<code>Z^b Z^b</code>) produce barred sons (<code>Z^B Z^b</code>) and non-barred black daughters (<code>Z^b W</code>).</li>"
        "</ul><br>"
        "<b>2. SEX-LIMITED TRAITS</b><br>"
        "Governed by <b>autosomal genes</b> present in both sexes, but their phenotypic expression is <b>strictly confined to only one sex</b> due to anatomical differences or the presence/absence of sex steroid hormones:"
        "<ul>"
        "<li><b>Biological Characteristics:</b> Expressed in 0% of one sex, regardless of genotype; transmitted equally through both sires and dams.</li>"
        "<li><b>Livestock Examples:</b>"
        "<br>&bull; <b>Lactation Milk Yield and Fat Percentage in Dairy Cattle:</b> Autosomal genes for 305-day milk production are present in both bulls and cows. A sire cannot produce milk, yet his genetic merit (Breeding Value) for milk yield is transmitted to his daughters! (Evaluated through Progeny Testing). "
        "<br>&bull; <b>Egg Production and Shell Quality in Poultry:</b> Expressed only in female layers; transmitted through roosters."
        "<br>&bull; <b>Cryptorchidism in Bulls, Rams, and Stallions:</b> Failure of one or both testes to descend into scrotum; autosomal recessive, expressed only in males."
        "<br>&bull; <b>Cock-Feathering in Domestic Fowl:</b> Hen-feathering (H) is dominant to cock-feathering (h). The homozygous recessive genotype <code>hh</code> produces long, pointed, curving sickle feathers <i>only in roosters</i>; females with <code>hh</code> maintain normal rounded hen plumage.</li>"
        "</ul><br>"
        "<b>3. SEX-INFLUENCED (SEX-CONDITIONED) TRAITS</b><br>"
        "Governed by <b>autosomal genes</b> present in both sexes, but the <b>dominance relationship of the alleles shifts or reverses</b> depending on the hormonal sex environment of the individual:"
        "<ul>"
        "<li>An allele acts as <b>dominant in one sex</b>, but acts as <b>recessive in the opposite sex</b>, typically modulated by testosterone vs estrogen.</li>"
        "<li><b>Classic Livestock Example — Horns in Sheep:</b>"
        "<br>In crosses between horned Dorset and hornless (polled) Suffolk sheep, the horned allele (<code>h^+</code>) and polled allele (<code>h</code>) interact with sex:"
        "<br>&bull; Genotype <code>h^+ h^+</code> &rarr; Horned in BOTH rams and ewes."
        "<br>&bull; Genotype <code>h h</code> &rarr; Hornless (polled) in BOTH rams and ewes."
        "<br>&bull; Heterozygote <code>h^+ h</code> &rarr; <b>HORNED in Rams</b> (testosterone renders <code>h^+</code> dominant), but <b>HORNLESS in Ewes</b> (estrogen renders <code>h^+</code> recessive)!"
        "<br>Mating two heterozygous sheep (<code>h^+ h &times; h^+ h</code>) yields an F₂ phenotypic ratio of <b>3 Horned : 1 Polled in Rams</b>, but <b>1 Horned : 3 Polled in Ewes</b>!</li>"
        "<li><b>Other Examples:</b> Scurs in polled cattle; Pattern Baldness in humans.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Summary Diagnostic Matrix for Written Board Examinations:</b><br>"
        "Examiners frequently present unknown pedigree scenarios and demand exact classification. Master this decision algorithm: "
        "<ol>"
        "<li><i>Is the gene on the X (or Z) chromosome?</i> &rarr; <b>Sex-Linked</b>. Look for criss-cross transmission (father never passes to son; male chicks inherit dam's Z).</li>"
        "<li><i>Is the gene on an autosome, but expressed in ONLY ONE sex?</i> &rarr; <b>Sex-Limited</b>. Expression is 0% in one sex (e.g., milk yield, cryptorchidism). Phenotypic variance in the unexpressed sex is zero.</li>"
        "<li><i>Is the gene on an autosome, expressed in BOTH sexes, but heterozygous Aa has OPPOSITE phenotypes in males vs females?</i> &rarr; <b>Sex-Influenced</b>. Heterozygote Aa is dominant in males, recessive in females (e.g., sheep horns).</li>"
        "</ol>"
    ),
    "keyPoints": [
        "Sex-linked genes are located on sex chromosomes (X or Z) and exhibit criss-cross inheritance.",
        "In mammals, males are hemizygous for X-linked genes; recessive X-linked alleles are always expressed in males.",
        "A mammalian sire never transmits an X-linked gene to his son (transmits Y to sons, X to daughters).",
        "Hemophilia A in dogs is an X-linked recessive disorder causing severe coagulopathy.",
        "Commercial poultry utilizes Z-linked feather sexing (slow K vs rapid k) to visually sex day-old chicks.",
        "Sex-limited traits are autosomal genes expressed exclusively in one sex (milk yield, egg production, cryptorchidism).",
        "A bull transmits autosomal genes for milk production to his daughters even though he never lactates.",
        "Cock-feathering in poultry is an autosomal sex-limited trait expressed only in roosters with genotype hh.",
        "Sex-influenced traits are autosomal genes whose dominance reverses between sexes depending on hormones.",
        "Horns in sheep (h⁺ vs h) is sex-influenced: the heterozygote h⁺h is horned in rams, but hornless in ewes.",
        "In sex-influenced traits, F₂ phenotypic ratios are inverted between sexes (3:1 in males vs 1:3 in females)."
    ],
    "clinical": (
        "In commercial poultry hatcheries producing millions of layer pullets, using Z-linked slow-feathering dams (ZᴷW) crossed with rapid-feathering sires (ZᵏZᵏ) produces 100% rapid-feathering female chicks (ZᵏW) identifiable at day-old by primary wing pinfeathers extending beyond covert feathers. This genetic tool completely eliminates skilled manual cloacal vent sexing, saving commercial poultry operations millions in labor costs."
    ),
    "tables": [
        {
            "title": "Comprehensive Diagnostic Comparison: Sex-Linked versus Sex-Limited versus Sex-Influenced Traits",
            "headers": ["Diagnostic Criterion", "Sex-Linked Traits", "Sex-Limited Traits", "Sex-Influenced Traits"],
            "rows": [
                ["Chromosomal Location", "Located on Sex Chromosomes (X in mammals, Z in birds)", "Located on Autosomes (present equally in both sexes)", "Located on Autosomes (present equally in both sexes)"],
                ["Expression in Both Sexes", "Expressed in both sexes (vastly higher in hemizygous sex)", "Expressed in ONLY ONE sex (0% expression in other sex)", "Expressed in BOTH sexes, but with differing dominance"],
                ["Phenotype of Heterozygote (Aa)", "Normal in females; males cannot be heterozygous", "Expressed only if individual is of the permissive sex", "Dominant phenotype in one sex; Recessive in opposite sex"],
                ["Inheritance Pattern", "Criss-cross inheritance (Father &rarr; Daughter &rarr; Grandson)", "Standard autosomal transmission (inherited via both sexes)", "Autosomal transmission with sex-dependent phenotypic ratio"],
                ["Classic Livestock Example", "Barred plumage & feather sexing in fowl; Hemophilia A", "305-day milk yield in cows; cryptorchidism in rams", "Horns in Dorset &times; Suffolk sheep; scurs in cattle"]
            ]
        }
    ],
    "img": "",
    "tags": ["sex-linked", "sex-limited", "sex-influenced", "criss-cross-inheritance", "feather-sexing", "sheep-horns", "cryptorchidism"]
}

topics["u2-t11"] = {
    "summary": "Linkage describes syntenic genes on the same chromosome inherited together, broken by crossing over during meiotic pachytene, with recombination frequencies used to construct linear genetic linkage maps.",
    "desc": (
        "<b>THE DISCOVERY AND CONCEPT OF GENETIC LINKAGE</b><br>"
        "Discovered by William Bateson and Reginald Punnett (1905) in sweet peas, who termed the non-random association <i>Coupling and Repulsion</i>. "
        "The physical mechanism was conclusively established by Thomas Hunt Morgan (1910) using <i>Drosophila melanogaster</i>. "
        "<b>Linkage</b> is the tendency of two or more genes situated on the same chromosome to remain together during meiotic gamete formation and be transmitted together into the progeny as an unbroken unit.<br><br>"
        "<b>CHROMOSOME THEORY OF LINKAGE (MORGAN'S POSTULATES)</b><br>"
        "<ol>"
        "<li>Genes are arranged in a continuous linear order along the length of the chromosome, like beads on a string.</li>"
        "<li>Genes residing on the same chromosome are termed <b>Syntenic</b> and tend to remain linked together.</li>"
        "<li>The strength of linkage is <b>inversely proportional to the physical distance</b> separating the two genes: genes close together exhibit tight linkage; genes far apart exhibit weak linkage.</li>"
        "<li>Linkage is broken by <b>Crossing Over</b> during meiotic prophase I.</li>"
        "</ol><br>"
        "<b>TYPES OF LINKAGE</b><br>"
        "<ul>"
        "<li><b>Complete Linkage:</b> Linked genes are located so close together that no crossing over occurs between them; parental combinations are transmitted 100% intact (0% recombinants). "
        "<br><i>Example:</i> Heterozygous male <i>Drosophila</i> and female silkworms (<i>Bombyx mori</i>) exhibit complete linkage (crossing over is entirely absent in these sexes!).</li>"
        "<li><b>Incomplete Linkage:</b> Linked genes are separated by sufficient distance that crossing over occasionally breaks the linkage, producing both parental and recombinant gametes (recombinant frequency &gt; 0% but &lt; 50%). Standard in farm livestock.</li>"
        "<li><b>Coupling versus Repulsion Phase:</b>"
        "<br>&bull; <i>Coupling Phase (Cis-arrangement):</i> Both dominant alleles are on one homolog and both recessive alleles on the other (<code>AB / ab</code>). Produces high frequency of <code>AB</code> and <code>ab</code> gametes."
        "<br>&bull; <i>Repulsion Phase (Trans-arrangement):</i> Each homolog carries one dominant and one recessive allele (<code>Ab / aB</code>). Produces high frequency of <code>Ab</code> and <code>aB</code> gametes.</li>"
        "</ul><br>"
        "<b>CROSSING OVER AND RECOMBINATION FREQUENCY</b><br>"
        "Crossing over is the physical breakage and reciprocal exchange of chromosomal segments between <b>non-sister chromatids of homologous chromosomes</b> during the Pachytene stage of Meiosis I. "
        "The degree of crossing over is quantified by the <b>Recombination Frequency (RF)</b>:"
        "<br><br>"
        "<code>Recombination Frequency (RF %) = [ (Total Number of Recombinant Progeny) / (Total Number of Progeny) ] &times; 100</code>"
        "<br><br>"
        "<b>Upper Limit of Recombination:</b> The maximum possible recombination frequency between any two linked genes is <b>50%</b> (0.50). Even if crossing over occurs in 100% of tetrads, only 2 of the 4 chromatids participate in a single crossover, yielding a maximum 50% recombinant gametes, mimicking independent assortment.<br><br>"
        "<b>CONSTRUCTION OF GENETIC LINKAGE MAPS (GENE MAPPING)</b><br>"
        "First formulated by Morgan's undergraduate student, <b>Alfred H. Sturtevant (1913)</b>. "
        "Sturtevant realized that recombination frequency is a direct mathematical function of the physical distance separating two genes along the chromosome: "
        "<br>&bull; <b>1% Recombination Frequency = 1 Map Unit (mu) = 1 centiMorgan (cM)</b> (named in honor of T. H. Morgan). "
        "<br>&bull; 1 Morgan = 100 cM.<br><br>"
        "<b>The Three-Point Test Cross:</b>"
        "<br>The gold standard for determining: (1) the relative linear order of three linked genes (e.g., A, B, C); (2) the exact map distances between them; and (3) chromosome interference. "
        "In a three-point test cross (<code>AaBbCc &times; aabbcc</code>):"
        "<ul>"
        "<li>The two most frequent phenotypic classes are always the <b>Parental (Non-crossover) Types</b>.</li>"
        "<li>The two least frequent phenotypic classes are always the <b>Double Crossover (DCO) Types</b>.</li>"
        "<li><b>Gene Order Determination:</b> Comparing the parental types with the double crossover types reveals which single gene has switched position: the gene that is switched in the DCO classes is the <b>MIDDLE GENE</b>!</li>"
        "<li><b>Interference (I) and Coefficient of Coincidence (CC):</b>"
        "<br>The occurrence of one crossover in a chromosomal region frequently physically inhibits the formation of a second crossover in adjacent regions: "
        "<br><code>Coefficient of Coincidence (CC) = (Observed DCO Frequency) / (Expected DCO Frequency)</code>"
        "<br>where <code>Expected DCO = RF₁ &times; RF₂</code>."
        "<br><code>Interference (I) = 1 - CC</code>. (If CC = 0.6, Interference I = 0.40 or 40%, meaning 40% of expected double crossovers were physically blocked).</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Haldane's Mapping Function (Correcting for Double Crossovers):</b><br>"
        "For small genetic distances (&lt; 10 cM), observed recombination frequency (RF) is linearly proportional to true map distance (d). "
        "However, as physical distance increases beyond 10 cM, multiple undetected double crossovers (which restore parental allele combinations) go uncounted, causing raw RF to underestimate true physical distance. "
        "J. B. S. Haldane (1919) formulated the mapping function assuming crossovers follow a Poisson distribution: "
        "<br><code>d = - 0.5 &times; ln(1 - 2 &times; RF)</code>, or <code>RF = 0.5 &times; (1 - e^(-2d))</code>. "
        "This mathematical function corrects for multiple crossovers, asymptotically approaching 50% as map distance 'd' extends to infinity."
    ),
    "keyPoints": [
        "Linkage is the tendency of syntenic genes on the same chromosome to be inherited together as a unit.",
        "T. H. Morgan formulated the Chromosome Theory of Linkage using Drosophila melanogaster.",
        "Linkage breaks Mendel's Law of Independent Assortment, producing parental types in excess of 50%.",
        "Complete linkage yields 100% parental combinations (e.g., male Drosophila, female silkworms).",
        "Cis-arrangement (Coupling) has AB/ab; Trans-arrangement (Repulsion) has Ab/aB.",
        "Crossing over occurs between non-sister chromatids of homologous chromosomes during meiotic Pachytene.",
        "Recombination Frequency: RF % = (Recombinant Progeny / Total Progeny) × 100.",
        "The maximum theoretical recombination frequency between linked genes is 50%.",
        "1% Recombination Frequency = 1 centiMorgan (cM) = 1 Map Unit (mu), formulated by Alfred Sturtevant (1913).",
        "In a three-point test cross, the middle gene is identified by comparing parental and double crossover classes.",
        "Coefficient of Coincidence: CC = Observed DCO / Expected DCO; Interference: I = 1 - CC.",
        "Haldane's mapping function corrects for undetected multiple double crossovers over large map distances."
    ],
    "clinical": (
        "In commercial swine breeding, genetic linkage between the Halothane gene (RYR1, causing Porcine Stress Syndrome) and the blood group H/PHI locus allowed early animal breeders to eradicate malignant hyperthermia susceptibility from Landrace and Pietrain seedstock before direct DNA sequencing was invented, using serological blood typing as a linked diagnostic marker."
    ),
    "tables": [
        {
            "title": "Comprehensive Comparison of Independent Assortment versus Genetic Linkage",
            "headers": ["Genetic Criterion", "Independent Assortment (Mendelian)", "Genetic Linkage (Morgan)"],
            "rows": [
                ["Chromosomal Relationship", "Genes located on separate non-homologous chromosomes", "Genes located syntenically on the same chromosome"],
                ["Dihybrid Test Cross Ratio", "Exact 1 : 1 : 1 : 1 ratio (50% parental, 50% recombinant)", "Distorted ratio: Parental types &gt; 50%; Recombinant types &lt; 50%"],
                ["Dihybrid F₂ Phenotypic Ratio", "Classic 9 : 3 : 3 : 1 ratio", "Severe deviation from 9:3:3:1 (excess of parental phenotypes)"],
                ["Physical Basis", "Random centromeric orientation at Metaphase I", "Physical proximity along a single DNA chromatin fiber"],
                ["Influence of Distance", "Distance is irrelevant (on different chromosomes)", "Recombination frequency is directly proportional to map distance"]
            ]
        }
    ],
    "img": "",
    "tags": ["linkage", "crossing-over", "recombination-frequency", "centimorgan", "sturtevant", "three-point-testcross", "interference"]
}

topics["u2-t12"] = {
    "summary": "Gene mutations are sudden, heritable changes in the nucleotide sequence of DNA, classified into point mutations (transitions, transversions, frameshifts) and induced by physical, chemical, or biological mutagens.",
    "desc": (
        "<b>DEFINITION AND HISTORICAL FOUNDATION</b><br>"
        "The term <b>Mutation</b> (Latin: <i>mutare</i> = to change) was introduced by Dutch botanist <b>Hugo de Vries (1901)</b> based on his observations in the evening primrose (<i>Oenothera lamarckiana</i>). "
        "In modern molecular genetics, a mutation is defined as any sudden, permanent, heritable change in the primary nucleotide sequence of an organism's genomic DNA, serving as the ultimate raw source of all novel genetic variation in animal breeding.<br><br>"
        "<b>CLASSIFICATION OF GENE MUTATIONS</b><br>"
        "<b>1. Based on Cell Type:</b>"
        "<ul>"
        "<li><b>Germline Mutations:</b> Occur in reproductive gametic cells (spermatogonia, oogonia). Transmitted to offspring; present in every cell of the progeny's body. Essential for evolution and selective breeding.</li>"
        "<li><b>Somatic Mutations:</b> Occur in non-reproductive body cells (e.g., skin, mammary gland, liver). Not inherited by sexual offspring; manifest as mosaic tissue patches or neoplastic malignancies (cancer).</li>"
        "</ul>"
        "<b>2. Based on Cause / Origin:</b>"
        "<ul>"
        "<li><b>Spontaneous Mutations:</b> Occur naturally in the absence of external mutagens, arising from DNA replication errors (tautomeric shifts), spontaneous base deamination, or oxidative radical damage. Baseline rate is low (approx. 1 in 10⁵ to 10⁶ per locus per generation).</li>"
        "<li><b>Induced Mutations:</b> Produced artificially by exposing animals or cells to environmental physical or chemical agents (mutagens) that drastically increase the baseline mutation rate.</li>"
        "</ul>"
        "<b>3. Based on Direction:</b> Forward mutation (Wild-type &rarr; Mutant) vs Reverse / Back mutation (Mutant &rarr; Wild-type).<br><br>"
        "<b>MOLECULAR MECHANISMS OF POINT (GENE) MUTATIONS</b><br>"
        "Point mutations involve changes within a single nucleotide base pair or a few adjacent base pairs:"
        "<ul>"
        "<li><b>1. Base-Pair Substitutions:</b> One nucleotide base is replaced by another: "
        "<br>&bull; <b>Transition:</b> Replacement of a purine by another purine (<code>A &harr; G</code>), or a pyrimidine by another pyrimidine (<code>C &harr; T</code>). There are 4 possible transitions. "
        "<br>&bull; <b>Transversion:</b> Replacement of a purine by a pyrimidine, or a pyrimidine by a purine (<code>A &harr; C, A &harr; T, G &harr; C, G &harr; T</code>). There are 8 possible transversions.</li>"
        "<li><b>Functional Consequences of Base Substitutions:</b>"
        "<br>&bull; <i>Silent (Synonymous) Mutation:</i> Base change alters codon, but due to genetic code degeneracy, encodes the <b>exact same amino acid</b> (e.g., <code>GAA &rarr; GAG</code> both encode Glutamate). No phenotypic change."
        "<br>&bull; <i>Missense Mutation:</i> Base change alters codon to encode a <b>different amino acid</b> (e.g., Sickle cell anemia: <code>GAG &rarr; GTG</code> changes Glutamate to Valine in beta-globin; BLAD in cattle: adenine to guanine transition changing Aspartate to Glycine at codon 128 of CD18 gene). Causes altered protein function or disease."
        "<br>&bull; <i>Nonsense Mutation:</i> Base change transforms an amino acid codon into a premature <b>stop/termination codon</b> (<code>UAA, UAG, or UGA</code>). Causes premature translation termination, yielding a truncated, non-functional protein."
        "<li><b>2. Frameshift Mutations:</b>"
        "<br>Arise from the <b>Insertion or Deletion (Indel)</b> of a number of nucleotides that is <b>NOT a multiple of 3</b>. "
        "Because the genetic code is non-overlapping and read in strict triplets from a fixed reading frame, an insertion or deletion of 1 or 2 bases shifts the entire downstream reading frame, radically altering every subsequent amino acid and usually introducing a premature nonsense stop codon! (Devastating functional impact).</li>"
        "</ul><br>"
        "<b>MUTAGENIC AGENTS (MUTAGENS)</b><br>"
        "<ol>"
        "<li><b>Physical Mutagens:</b>"
        "<br>&bull; <i>Ionizing Radiation:</i> X-rays (H. J. Muller, 1927, who first demonstrated artificial mutagenesis in <i>Drosophila</i>, Nobel Prize 1946), gamma rays, cosmic rays. Cause deep tissue penetration, water radiolysis producing reactive hydroxyl free radicals (OH&bull;), and double-stranded DNA backbone breaks. "
        "<br>&bull; <i>Non-Ionizing Radiation:</i> Ultraviolet (UV) light (peak absorption at 260 nm). Does not penetrate deep tissues; absorbed by DNA pyrimidines, creating <b>Thymine-Thymine (Pyrimidine) Dimers</b> that distort the double helix and stall replication forks (causes cutaneous squamous cell carcinoma / 'Cancer Eye' in Hereford cattle).</li>"
        "<li><b>Chemical Mutagens:</b>"
        "<br>&bull; <i>Base Analogues:</i> Chemically resemble natural bases and incorporate into replicating DNA. (e.g., <b>5-Bromouracil (5-BU)</b> resembles Thymine but frequently undergoes tautomeric shift to pair with Guanine, inducing <code>A:T &harr; G:C</code> transitions; <b>2-Aminopurine (2-AP)</b> resembles Adenine). "
        "<br>&bull; <i>Alkylating Agents:</i> Add alkyl (methyl/ethyl) groups to bases, altering base pairing. (e.g., <b>Ethyl Methane Sulfonate - EMS</b>, Methyl Methane Sulfonate - MMS, Mustard Gas). EMS causes <code>G:C &rarr; A:T</code> transitions. "
        "<br>&bull; <i>Deaminating Agents:</i> Remove amino groups (-NH₂). (e.g., <b>Nitrous Acid - HNO₂</b> deaminates Adenine to Hypoxanthine [pairs with C] and Cytosine to Uracil [pairs with A]). "
        "<br>&bull; <i>Intercalating Acridine Dyes:</i> Planar aromatic molecules (<b>Acridine orange, Proflavine, Ethidium bromide</b>) that wedge between adjacent base pairs, stretching the helix and causing <b>Frameshift insertions/deletions</b> during replication.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>DNA Repair Pathways in Livestock:</b><br>"
        "Veterinary organisms maintain genome integrity via four primary enzymatic repair pathways: "
        "<ol>"
        "<li><b>Photoreactivation (Direct Reversal):</b> The enzyme <i>photolyase</i> absorbs visible blue light (300–500 nm) and directly cleaves UV-induced cyclobutane pyrimidine dimers (present in birds/reptiles; absent in placental mammals).</li>"
        "<li><b>Base Excision Repair (BER):</b> DNA glycosylases recognize and cleave damaged deaminated bases (e.g., Uracil DNA glycosylase), followed by AP-endonuclease, DNA polymerase, and ligase repair.</li>"
        "<li><b>Nucleotide Excision Repair (NER):</b> Excises bulky helix-distorting DNA adducts and pyrimidine dimers as a multi-nucleotide oligonucleotide patch (defective in Xeroderma Pigmentosum).</li>"
        "<li><b>Mismatch Repair (MMR):</b> Corrects post-replication proofreading errors (MutS/MutL machinery).</li>"
        "</ol>"
    ),
    "keyPoints": [
        "Mutation is a sudden, permanent, heritable change in the genomic DNA sequence, coined by Hugo de Vries (1901).",
        "Germline mutations occur in gametes and are transmitted to offspring; somatic mutations are non-heritable.",
        "H. J. Muller (1927) first demonstrated artificial induced mutagenesis using X-rays in Drosophila (Nobel Prize 1946).",
        "Point mutations involve changes in a single nucleotide base pair.",
        "Transition is purine to purine (A ↔ G) or pyrimidine to pyrimidine (C ↔ T); Transversion is purine to pyrimidine.",
        "Silent mutations alter codons without changing amino acids; Missense mutations alter single amino acids.",
        "Nonsense mutations convert an amino acid codon into a premature stop codon (UAA, UAG, UGA).",
        "Frameshift mutations result from insertions/deletions not divisible by 3, altering the entire downstream reading frame.",
        "UV radiation causes Thymine (pyrimidine) dimers, triggering 'Cancer Eye' in Hereford cattle.",
        "Base analogue 5-Bromouracil (5-BU) mimics thymine, inducing transition mutations.",
        "Alkylating agents like EMS add alkyl groups; Intercalating acridine dyes cause frameshift mutations.",
        "DNA repair pathways (BER, NER, MMR) actively maintain livestock genome integrity against mutagenic insults."
    ],
    "clinical": (
        "In bovine genetics, Bovine Leukocyte Adhesion Deficiency (BLAD) in Holstein calves is caused by a single missense point mutation: an adenine to guanine (A &rarr; G) transition at nucleotide position 383 of the CD18 gene. This single nucleotide swap converts an aspartic acid to glycine at amino acid 128, destroying the adhesion protein required for neutrophils to migrate into infected tissues, leading to fatal recurrent pneumonia and calf mortality."
    ),
    "tables": [
        {
            "title": "Comprehensive Classification of Molecular Point Mutations and Their Functional Impacts",
            "headers": ["Mutation Category", "Molecular DNA Alteration", "Effect on Polypeptide Amino Acid Sequence", "Clinical / Livestock Consequence"],
            "rows": [
                ["Transition", "Purine &harr; Purine (A&harr;G) or Pyrimidine &harr; Pyrimidine (C&harr;T)", "Variable depending on codon position (often silent or missense)", "BLAD missense mutation in Holsteins (A &rarr; G transition)"],
                ["Transversion", "Purine &harr; Pyrimidine (A&harr;C, A&harr;T, G&harr;C, G&harr;T)", "Variable (missense or nonsense)", "Double-muscling in Belgian Blue cattle (myostatin mutation)"],
                ["Silent (Synonymous)", "Codon altered, but encodes same amino acid (degenerate code)", "Zero change; identical wild-type amino acid sequence", "Neutral polymorphism; no phenotypic or clinical effect"],
                ["Missense", "Codon altered to encode a different amino acid", "Single amino acid substitution in synthesized protein", "Sickle cell; CD18 dysfunction in bovine BLAD"],
                ["Nonsense", "Codon altered to premature stop codon (UAA, UAG, UGA)", "Premature truncation of polypeptide chain", "Complete loss-of-function; often recessive lethal"],
                ["Frameshift", "Insertion or deletion of 1 or 2 base pairs (not multiple of 3)", "Complete alteration of all downstream amino acids", "Severe functional disruption; non-functional protein synthesized"]
            ]
        }
    ],
    "img": "",
    "tags": ["mutations", "point-mutation", "transition", "transversion", "frameshift", "mutagens", "thymine-dimers", "blad"]
}

topics["u2-t13"] = {
    "summary": "Chromosomal aberrations are large-scale alterations in chromosome structure (deletions, duplications, inversions, translocations) or number (aneuploidy, polyploidy) causing severe congenital malformations and livestock subfertility.",
    "desc": (
        "<b>CLASSIFICATION OF CHROMOSOMAL ABERRATIONS</b><br>"
        "Unlike microscopic point mutations that involve individual DNA base pairs, <b>Chromosomal Aberrations</b> represent large-scale cytogenetic modifications visible under a light microscope, categorized into <b>Numerical Aberrations</b> and <b>Structural Aberrations</b>.<br><br>"
        "<b>1. NUMERICAL CHROMOSOMAL ABERRATIONS (HETEROPLOIDY)</b><br>"
        "Alterations in the total number of chromosomes relative to the normal diploid species complement (2n):"
        "<ul>"
        "<li><b>A. Aneuploidy (Changes in Individual Chromosomes):</b>"
        "<br>Arises primarily from <b>meiotic non-disjunction</b> (failure of homologous chromosomes or sister chromatids to separate properly during anaphase):"
        "<br>&bull; <i>Nullisomy (2n - 2):</i> Loss of an entire homologous chromosome pair. Almost universally lethal in animals."
        "<br>&bull; <i>Monosomy (2n - 1):</i> Loss of a single chromosome. Autosomal monosomies are lethal in utero in livestock. "
        "<i>Sex-chromosome Monosomy (XO):</i> <b>Turner Syndrome</b> (e.g., 63,XO in mares; 59,XO in heifers), characterized by gonadal dysgenesis, infantile reproductive tract, and permanent sterility."
        "<br>&bull; <i>Trisomy (2n + 1):</i> Presence of an extra chromosome. Trisomies of large autosomes cause embryonic mortality. Trisomy of small autosomes (e.g., Trisomy 28 in cattle) causes brachygnathia and developmental arrest. "
        "<i>Sex-chromosome Trisomy (XXY):</i> <b>Klinefelter Syndrome</b> (e.g., 61,XXY in bulls; 39,XXY in male calico cats), characterized by hypoplastic testes, azoospermia, and absolute sterility."
        "<br>&bull; <i>Tetrasomy (2n + 2):</i> Presence of an extra pair of homologous chromosomes.</li>"
        "<li><b>B. Euploidy / Polyploidy (Changes in Entire Genome Sets):</b>"
        "<br>Presence of exact multiples of the haploid chromosome complement (n):"
        "<br>&bull; <i>Monoploidy / Haploidy (n):</i> Single set of chromosomes. Normal in male honeybees (drones; arrhenotoky); lethal in farm animals."
        "<br>&bull; <i>Polyploidy (3n, 4n, 5n...):</i> Triploidy (3n) and Tetraploidy (4n) arise from polyspermy (fertilization of an ovum by two sperm) or retention of a polar body. In mammals and birds, polyploidy causes 100% embryonic mortality before or shortly after implantation.</li>"
        "</ul><br>"
        "<b>2. STRUCTURAL CHROMOSOMAL ABERRATIONS</b><br>"
        "Arise from chromosome breakage followed by abnormal, illegitimate re-joining of broken ends:"
        "<ol>"
        "<li><b>Deletion (Deficiency):</b> Loss of a chromosomal segment. "
        "<br>&bull; <i>Terminal Deletion:</i> Single break at the end of a chromosome arm. "
        "<br>&bull; <i>Interstitial Deletion:</i> Two internal breaks with loss of the intervening segment. Severe gene dosage loss; causes Cri-du-chat syndrome (human 5p-) and congenital skeletal anomalies in calves.</li>"
        "<li><b>Duplication:</b> Presence of an extra chromosomal segment (tandem, reverse, or displaced). Can cause gene dosage imbalances, though generally less lethal than deletions.</li>"
        "<li><b>Inversion:</b> A chromosomal segment breaks in two places, rotates 180&deg;, and re-inserts in reverse linear order: "
        "<br>&bull; <i>Paracentric Inversion:</i> Does NOT include the centromere (both breaks are within the same chromosome arm). "
        "<br>&bull; <i>Pericentric Inversion:</i> INCLUDES the centromere (breaks are on opposite arms; can change chromosome morphology, e.g., acrocentric to metacentric). "
        "<br><i>Cytogenetic Feature:</i> Inversion heterozygotes form characteristic <b>Inversion Loops</b> during meiotic pachytene. Crossing over within the loop generates acentric fragments and dicentric bridges, causing gametic lethality.</li>"
        "<li><b>Translocation:</b> Transfer of a chromosomal segment to a non-homologous chromosome: "
        "<br>&bull; <i>Reciprocal Translocation:</i> Mutual, two-way exchange of broken segments between two non-homologous chromosomes. During meiosis, forms a cross-shaped <b>Quadrivalent</b> figure. "
        "<br>&bull; <b>Robertsonian Translocation (Centric Fusion):</b> The most important structural aberration in veterinary medicine! Two acrocentric chromosomes undergo breaks at or near their centromeres and fuse to form a <b>single large metacentric or submetacentric chromosome</b>, with the loss of minute heterochromatic fragments. "
        "The diploid number decreases (2n = 59 instead of 60 in cattle), but the animal remains phenotypically normal because virtually all euchromatic genetic arm material is preserved.</li>"
        "</ol><br>"
        "<b>THE ROBERTSONIAN 1/29 TRANSLOCATION (rob 1;29) IN CATTLE</b><br>"
        "First discovered by Ingemar Gustavsson (1964) in Swedish Red and White cattle. "
        "Consists of the centric fusion of <b>Autosome 1 and Autosome 29</b> (karyotype: <code>59,XX,rob(1;29)</code> or <code>59,XY,rob(1;29)</code>):"
        "<ul>"
        "<li>Carrier bulls and cows appear completely normal in growth, conformation, and general health.</li>"
        "<li><b>The Veterinary Pathology:</b> During meiosis in carrier animals, a trivalent forms, resulting in unbalanced gametes (nullisomic or disomic for chromosomes 1 or 29). "
        "Fertilization of these unbalanced gametes causes <b>monosomic and trisomic zygotes that die during early embryonic cleavage</b> (days 8–16 post-conception).</li>"
        "<li><b>Clinical Impact:</b> Causes a <b>5% to 10% reduction in herd fertility</b> and repeat breeding syndrome. Mandatory cytogenetic karyotyping of all AI breeding bulls is enforced worldwide to eradicate the 1/29 translocation.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Segregation Modes of Reciprocal Translocation Quadrivalents:</b><br>"
        "At Metaphase I, the cross-shaped quadrivalent formed by reciprocal translocation heterozygotes disjoins in three distinct modes: "
        "<ol>"
        "<li><b>Alternate Segregation:</b> Diagonal chromosomes move to the same pole (T₁ + T₂ to one pole; N₁ + N₂ to other pole). Produces 100% genetically balanced gametes (50% normal, 50% balanced translocation carriers). All offspring survive!</li>"
        "<li><b>Adjacent-1 Segregation:</b> Non-homologous adjacent chromosomes with different centromeres move to the same pole (T₁ + N₂ and T₂ + N₁). Produces 100% unbalanced gametes carrying segmental duplications and deficiencies. Offspring die in utero.</li>"
        "<li><b>Adjacent-2 Segregation:</b> Homologous adjacent centromeres move to the same pole (rare). 100% lethal unbalanced gametes.</li>"
        "</ol>"
        "Because alternate and adjacent-1 segregations occur in roughly equal frequencies, translocation carriers suffer <b>Semi-Sterility (approx. 50% embryonic mortality)</b>."
    ),
    "keyPoints": [
        "Chromosomal aberrations are large-scale visible alterations in chromosome structure or number.",
        "Aneuploidy involves changes in individual chromosomes (2n ± 1), caused by meiotic non-disjunction.",
        "Turner Syndrome in mares and heifers is sex chromosome monosomy (XO), causing gonadal dysgenesis and sterility.",
        "Klinefelter Syndrome in bulls is XXY trisomy (61,XXY), characterized by testicular hypoplasia and azoospermia.",
        "Polyploidy (3n, 4n) represents whole-genome multiplications; causes 100% embryonic lethality in livestock.",
        "Structural aberrations include: Deletions, Duplications, Inversions, and Translocations.",
        "Paracentric inversions do not include the centromere; Pericentric inversions include the centromere.",
        "Inversion heterozygotes form characteristic Inversion Loops during meiotic Pachytene.",
        "Reciprocal translocations form cross-shaped Quadrivalent figures at Meiosis I, causing 50% semi-sterility.",
        "Robertsonian Translocation (Centric Fusion) fuses two acrocentric chromosomes into one large metacentric.",
        "The 1/29 Robertsonian Translocation (rob 1;29) in cattle fuses chromosomes 1 and 29, reducing 2n to 59.",
        "rob(1;29) causes 5–10% embryonic mortality and repeat breeding; AI studs mandate karyotypic screening."
    ],
    "clinical": (
        "In dairy herd reproductive health management, repeat breeding cows that fail to conceive after 4 consecutive artificial inseminations without clinical uterine infections are subjected to cytogenetic screening. In many indigenous and crossbred herds, identification of subclinical Robertsonian translocation carriers [rob(1;29)] or reciprocal translocations identifies the genetic cause of early embryonic death, justifying selective culling."
    ),
    "tables": [
        {
            "title": "Comprehensive Classification of Numerical Chromosomal Aberrations (Heteroploidy)",
            "headers": ["Classification Category", "Symbolic Formula", "Chromosome Count in Cattle (2n = 60)", "Livestock Pathology / Clinical Manifestation"],
            "rows": [
                ["Disomy (Normal Diploid)", "2n", "60 chromosomes", "Normal healthy bovine karyotype"],
                ["Monosomy (Sex Chromosome)", "2n - 1", "59 chromosomes (59,XO)", "Turner syndrome; gonadal hypoplasia, aplasia of uterus, permanent sterility"],
                ["Trisomy (Sex Chromosome)", "2n + 1", "61 chromosomes (61,XXY)", "Klinefelter syndrome; testicular hypoplasia, small scrotum, azoospermia"],
                ["Trisomy (Autosomal)", "2n + 1", "61 chromosomes (e.g., Trisomy 28)", "Brachygnathia, congenital cardiac anomalies, early perinatal calf death"],
                ["Nullisomy", "2n - 2", "58 chromosomes", "Pre-implantation embryonic lethal; complete developmental arrest"],
                ["Triploidy", "3n", "90 chromosomes", "Polyspermy origin; 100% embryonic mortality within first trimester"],
                ["Tetraploidy", "4n", "120 chromosomes", "Cleavage failure; early blastocyst death before day 14"]
            ]
        }
    ],
    "img": "",
    "tags": ["chromosomal-aberrations", "aneuploidy", "robertsonian-translocation", "rob-1-29", "klinefelter", "turner-syndrome", "inversion"]
}

topics["u2-t14"] = {
    "summary": "Cytogenetics investigates the structure, function, and abnormalities of chromosomes using peripheral blood lymphocyte cultures, karyotype construction, and advanced banding techniques (G, Q, C, R, and NOR banding).",
    "desc": (
        "<b>DEFINITION AND VETERINARY IMPORTANCE OF CYTOGENETICS</b><br>"
        "Cytogenetics is the hybrid branch of genetics and cell biology that investigates the morphology, structure, number, function, and pathological aberrations of chromosomes. "
        "In livestock production, clinical cytogenetics serves as an indispensable diagnostic tool for certifying breeding sires, diagnosing congenital freemartinism, screening for embryonic lethal translocations, and cataloging breed-specific chromosomal standards.<br><br>"
        "<b>PERIPHERAL BLOOD LYMPHOCYTE CULTURE TECHNIQUE</b><br>"
        "First standardized by Moorhead et al. (1960). Peripheral blood lymphocytes are naturally arrested in the quiescent G₀ phase of the cell cycle. To obtain metaphase chromosomes, they must be stimulated to divide in vitro:<br>"
        "<ol>"
        "<li><b>Aseptic Venipuncture:</b> Collect 5–10 mL of blood from the jugular vein into a sterile vacutainer containing preservative-free <b>Sodium Heparin</b> (EDTA must be strictly avoided as it chelates divalent cations and kills lymphocytes!).</li>"
        "<li><b>Inoculation & Culture:</b> Add 0.5–1.0 mL of whole blood or buffy coat to culture medium (<b>RPMI-1640</b> or TC-199) supplemented with 15–20% fetal bovine serum (FBS), antibiotics (penicillin, streptomycin), and L-glutamine.</li>"
        "<li><b>Mitogenic Stimulation:</b> Add <b>Phytohaemagglutinin (PHA-M)</b>, a plant lectin extracted from the red kidney bean (<i>Phaseolus vulgaris</i>) that specifically stimulates T-lymphocytes to transform into actively dividing blast cells. "
        "Incubate in an incubator at <b>37.5&deg;C with 5% CO₂ for 72 hours</b>.</li>"
        "<li><b>Mitotic Arrest:</b> At the 70th to 71st hour of incubation, add <b>Colchicine or Colcemid</b> (0.05–0.1 &mu;g/mL). "
        "Colcemid binds to tubulin dimers, preventing spindle microtubule polymerisation and arresting dividing lymphocytes precisely at <b>Metaphase</b> where chromosomes reach maximal condensation.</li>"
        "<li><b>Hypotonic Swelling:</b> Centrifuge culture and treat cell pellet with warm (37&deg;C) hypotonic solution (<b>0.075 M KCl</b> or 0.8% sodium citrate) for 15–20 minutes. "
        "Water rushes into the cells by osmosis, causing lymphocytes to swell and dispersing metaphase chromosomes to prevent overlapping on the slide.</li>"
        "<li><b>Fixation:</b> Add ice-cold <b>Carnoy's Fixative</b> (Fresh mixture of <b>3 parts absolute Methanol : 1 part Glacial Acetic Acid</b>). "
        "Methanol fixes proteins; acetic acid lyses fragile erythrocytes and preserves chromatin. Centrifuge and wash pellet 3–4 times until clean.</li>"
        "<li><b>Slide Preparation:</b> Drop cell suspension onto clean, chilled, wet glass slides from a height of 1–2 feet to rupture the swollen cell membrane and spread chromosomes. Air dry or flame dry.</li>"
        "</ol><br>"
        "<b>KARYOTYPING AND IDIOGRAMS</b><br>"
        "<ul>"
        "<li><b>Karyotype:</b> The standardized photographic or digital arrangement of the complete diploid metaphase chromosome complement of a single cell, paired into homologous pairs and ordered systematically by decreasing physical length and centromere location.</li>"
        "<li><b>Idiogram:</b> The standardized diagrammatic schematic representation of the karyotype, depicting chromosome lengths, arm ratios, and official band patterns.</li>"
        "</ul><br>"
        "<b>CHROMOSOME BANDING TECHNIQUES</b><br>"
        "Conventional Giemsa staining colors chromosomes uniformly solid dark, making it impossible to distinguish between the 29 pairs of acrocentric autosomes in cattle. Specialized banding techniques produce characteristic alternating dark and light longitudinal transverse bands unique to each chromosome pair:<br>"
        "<ol>"
        "<li><b>G-Banding (Giemsa Banding - GTG):</b>"
        "<br>The gold standard in livestock cytogenetics. Slides are treated briefly with the proteolytic enzyme <b>Trypsin</b> to partially digest chromosomal proteins, then stained with <b>Giemsa</b>. "
        "<br>&bull; <i>Dark G-bands:</i> Represent <b>heterochromatic regions rich in Adenine-Thymine (A-T) base pairs</b>; late-replicating, gene-poor. "
        "<br>&bull; <i>Light G-bands:</i> Represent <b>euchromatic regions rich in Guanine-Cytosine (G-C) base pairs</b>; early-replicating, gene-dense.</li>"
        "<li><b>Q-Banding (Quinacrine Fluorescent Banding - QFQ):</b>"
        "<br>Stained with fluorescent dyes (<b>Quinacrine mustard</b> or Quinacrine dihydrochloride) and viewed under an Epifluorescence UV microscope. "
        "Bright fluorescent bands correspond exactly to dark G-bands (A-T rich). Useful for visualizing the human Y chromosome and heterochromatic polymorphisms.</li>"
        "<li><b>C-Banding (Constitutive Heterochromatin Banding - CBG):</b>"
        "<br>Sequential treatment with <b>0.2 N HCl &rarr; saturated Barium Hydroxide [Ba(OH)₂] at 50&deg;C &rarr; warm 2&times;SSC buffer &rarr; Giemsa</b>. "
        "Selectively stains <b>Constitutive Centromeric Heterochromatin</b> dark. "
        "<br><i>Veterinary Utility:</i> In cattle, all 58 acrocentric autosomes exhibit dense dark C-bands at their centromeres, whereas the submetacentric X chromosome has a minimal C-band, and the Y chromosome is almost entirely heterochromatic.</li>"
        "<li><b>R-Banding (Reverse Banding - RHG):</b>"
        "<br>Heat denaturation in hot phosphate buffer at 85&deg;C followed by Giemsa staining. "
        "Produces a pattern that is the <b>exact inverse (reverse) of G-banding</b>: G-C rich euchromatic regions stain dark; A-T rich regions stain light. Ideal for analyzing terminal chromosome ends and telomeric deletions.</li>"
        "<li><b>NOR-Banding (Nucleolar Organizer Region - Ag-NOR):</b>"
        "<br>Staining with <b>Silver Nitrate (AgNO₃)</b> under controlled temperature. "
        "Selectively stains the active ribosomal RNA gene clusters (18S and 28S rRNA) at secondary constrictions that were transcriptionally active in the preceding interphase.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Fluorescence In Situ Hybridization (FISH) and Chromosome Painting:</b><br>"
        "Modern molecular cytogenetics integrates recombinant DNA probes with classical metaphase spreads. "
        "In <b>FISH</b>, DNA probes specific to individual genes (e.g., SRY gene, BLAD locus) or whole-chromosome painting libraries are fluorescently labeled (rhodamine, FITC) and hybridized to denatured metaphase chromosomes. "
        "FISH achieves physical gene mapping resolution down to 1–2 megabases (Mb), allowing immediate visual localization of cryptic microdeletions and submicroscopic translocations undetectable by conventional G-banding."
    ),
    "keyPoints": [
        "Cytogenetics investigates chromosome morphology, number, function, and pathological aberrations.",
        "Moorhead et al. (1960) developed the peripheral blood lymphocyte culture method using Sodium Heparin.",
        "Phytohaemagglutinin (PHA) is a plant mitogen that selectively stimulates T-lymphocytes into mitotic blast cells.",
        "Colchicine/Colcemid arrests dividing lymphocytes in Metaphase by inhibiting mitotic spindle formation.",
        "Hypotonic KCl (0.075 M) treatment swells cells by osmosis, dispersing metaphase chromosomes.",
        "Carnoy's fixative is a fresh 3:1 mixture of absolute Methanol and Glacial Acetic Acid.",
        "A Karyotype is the ordered photographic arrangement of homologous chromosome pairs by size and centromere location.",
        "G-banding uses Trypsin digestion followed by Giemsa; Dark G-bands are A-T rich and gene-poor.",
        "Q-banding uses fluorescent Quinacrine dye under UV microscopy, matching G-banding patterns.",
        "C-banding utilizes Barium Hydroxide to selectively stain constitutive centromeric heterochromatin.",
        "R-banding (Reverse Banding) is the exact reverse of G-banding, darkly staining G-C rich active regions.",
        "Ag-NOR silver staining selectively highlights active Nucleolar Organizer Regions synthesizing rRNA."
    ],
    "clinical": (
        "In artificial breeding centers, compulsory cytogenetic screening of all AI breeding bulls using GTG-banding and CBG-banding is legally mandated by the Department of Animal Husbandry and Dairying (DAHD). Any bull exhibiting the 1/29 Robertsonian translocation, reciprocal translocations, or mosaicism (e.g., 60,XY / 60,XX freemartin chimerism) is strictly disqualified from semen collection and rejected from entry into national AI programs."
    ),
    "tables": [
        {
            "title": "Comprehensive Summary of Chromosome Banding Techniques in Livestock Cytogenetics",
            "headers": ["Banding Method", "Pre-treatment Agent / Chemical", "Dye / Stain Used", "Staining Specificity & Visual Appearance"],
            "rows": [
                ["G-Banding (GTG)", "Mild proteolytic Trypsin digestion", "Giemsa stain", "Alternating dark/light bands; Dark bands = A-T rich, late-replicating, gene-poor"],
                ["Q-Banding (QFQ)", "None (direct fluorochrome staining)", "Quinacrine mustard / dihydrochloride", "Fluorescent bright bands under UV light; identical pattern to dark G-bands"],
                ["C-Banding (CBG)", "HCl &rarr; Barium Hydroxide Ba(OH)₂ &rarr; warm 2&times;SSC", "Giemsa stain", "Selectively stains Constitutive Centromeric Heterochromatin dark"],
                ["R-Banding (RHG)", "Thermal denaturation in hot buffer (85&deg;C)", "Giemsa / Acridine orange", "Exact reverse of G-banding; Dark bands = G-C rich, gene-dense euchromatin"],
                ["NOR-Banding (Ag-NOR)", "Formic acid / Gelatin developer", "Silver Nitrate (AgNO₃)", "Black silver precipitate deposits on active Nucleolar Organizer Regions (rRNA)"]
            ]
        }
    ],
    "img": "",
    "tags": ["cytogenetics", "lymphocyte-culture", "phytohaemagglutinin", "colcemid", "karyotyping", "g-banding", "c-banding", "nor-banding"]
}
