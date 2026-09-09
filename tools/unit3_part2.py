# -*- coding: utf-8 -*-
"""
Unit 3 - Part 2: Topics u3-t08 to u3-t14
Principles of Animal Breeding (IVRI Undergrad 10 CGPA Standard)
"""

topics = {}

topics["u3-t08"] = {
    "summary": "Mating systems in animal breeding direct the union of gametes through random mating (panmixia) or non-random mating based on phenotypic resemblance (assortative/disassortative) or ancestral genetic relationship (inbreeding/outbreeding).",
    "desc": (
        "<b>DEFINITION AND PURPOSE OF MATING SYSTEMS</b><br>"
        "A <b>Mating System</b> is the planned arrangement and regulation of mates chosen from selected parents to produce the next generation. "
        "While <i>selection</i> decides <b>which</b> animals become parents and how many offspring they leave, <i>mating systems</i> determine <b>how</b> the chosen parents are paired together. "
        "Mating systems do not change gene frequencies by themselves; instead, they reorganize genes into specific genotypic combinations (changing genotypic frequencies and heterozygosity/homozygosity).<br><br>"
        "<b>BROAD CLASSIFICATION OF MATING SYSTEMS</b><br>"
        "Mating systems are broadly divided into two major categories:"
        "<ol>"
        "<li><b>Random Mating (Panmixia):</b>"
        "<br>&bull; Every selected male has an equal probability of mating with any selected female in the population, irrespective of phenotypic appearance or pedigree relationship."
        "<br>&bull; Governed by Hardy-Weinberg equilibrium; maintains constant gene and genotypic frequencies across generations in the absence of evolutionary forces."
        "<br>&bull; Serves as the fundamental biometrical baseline or control population in breeding experiments.</li>"
        "<li><b>Non-Random Mating:</b>"
        "<br>&bull; Individuals are paired systematically according to specific criteria rather than chance."
        "<br>&bull; Divided into two distinct categories:"
        "<br>&nbsp;&nbsp;a) <b>Based on Phenotypic Resemblance (Assortative Mating)</b>"
        "<br>&nbsp;&nbsp;b) <b>Based on Ancestral / Genetic Relationship</b></li>"
        "</ol><br>"
        "<b>I. MATING BASED ON PHENOTYPIC RESEMBLANCE</b><br>"
        "<ul>"
        "<li><b>Positive Assortative Mating ('Like to Like'):</b>"
        "<br>&bull; Mating of animals possessing similar phenotypic characteristics (e.g., best milk yielders to sons of highest yielders; tall to tall; fastest racehorse to fastest racehorse)."
        "<br>&bull; <i>Genetic Consequence:</i> Increases population phenotypic variance; fractures population into extreme phenotypic tails; increases homozygosity for the specific genes controlling the trait (without increasing genome-wide inbreeding)."
        "<br>&bull; <i>Utility:</i> Rapidly produces exceptional, extreme individuals for specialized seedstock or commercial sales.</li>"
        "<li><b>Negative Assortative Mating / Disassortative Mating ('Unlike to Unlike'):</b>"
        "<br>&bull; Mating of animals exhibiting dissimilar phenotypic characters (e.g., high body weight sire mated to low body weight dams; correcting a conformational defect like weak pasterns or sickle hocks by mating to animals with exceptionally strong pasterns)."
        "<br>&bull; Known as <b>Corrective Mating</b> or <b>Compensatory Mating</b>."
        "<br>&bull; <i>Genetic Consequence:</i> Decreases population variance; pulls population toward the intermediate optimum; preserves phenotypic uniformity and increases heterozygosity.</li>"
        "</ul><br>"
        "<b>II. MATING BASED ON GENETIC / PEDIGREE RELATIONSHIP</b><br>"
        "<ul>"
        "<li><b>Inbreeding:</b> Mating of individuals that are more closely related to each other than the average relationship of the population from which they originate (e.g., parent-offspring, full-sibs, half-sibs). Increases genome-wide homozygosity.</li>"
        "<li><b>Outbreeding:</b> Mating of individuals that are less closely related than the average relationship of the population. Includes outcrossing, topcrossing, grading up, linecrossing, and species hybridization. Increases genome-wide heterozygosity and generates heterosis.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Biometrical Contrast: Phenotypic vs Genetic Assortment:</b><br>"
        "In university examinations, clearly distinguish between assortative mating and inbreeding:"
        "<ul>"
        "<li><b>Positive Assortative Mating</b> changes genotypic frequencies <i>only at the loci governing the chosen trait</i> and any closely linked flanking loci. Unlinked, neutral loci remain completely unaffected in Hardy-Weinberg frequencies. Correlation between uniting gametes is <code>m</code>.</li>"
        "<li><b>Inbreeding</b> affects the <i>entire genome uniformly</i> across all homologous chromosome pairs regardless of phenotype. It increases homozygosity at every locus by a factor equal to Wright's inbreeding coefficient <code>F</code>: <code>P(AA) = p&sup2; + Fpq</code>, <code>P(Aa) = 2pq(1 - F)</code>, <code>P(aa) = q&sup2; + Fpq</code>.</li>"
        "<li><b>Selection vs Mating System Synergy:</b> Selection determines the allele frequencies (<code>p</code> and <code>q</code>), while the mating system dictates the distribution of those alleles into homozygotes and heterozygotes. Maximum genetic progress occurs when directional selection is coupled with positive assortative mating in nucleus breeding herds.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "A mating system determines how selected parents are paired to produce the next generation.",
        "Selection changes gene frequency; mating systems reorganize genes into genotypes.",
        "Random mating (panmixia) gives every individual an equal chance of mating with any opposite sex partner.",
        "Positive assortative mating pairs 'like with like' and increases population phenotypic variance.",
        "Negative assortative (disassortative) mating pairs 'unlike with unlike' and serves as corrective mating.",
        "Corrective mating reduces population variance and creates uniformity around an intermediate optimum.",
        "Mating based on pedigree relationship is divided into Inbreeding (related) and Outbreeding (unrelated).",
        "Assortative mating alters genotypic frequencies only at trait-specific loci.",
        "Inbreeding increases homozygosity across the entire genome uniformly.",
        "Hardy-Weinberg equilibrium is maintained under panmixia but disrupted under non-random mating systems.",
        "In dairy cattle herds, compensatory mating is routinely practiced to rectify udder depth, teat placement, and rump angle."
    ],
    "tables": [
        {
            "title": "Comprehensive Comparison of Primary Mating Systems in Livestock",
            "headers": ["Parameter / Feature", "Random Mating (Panmixia)", "Positive Assortative Mating", "Disassortative (Corrective)", "Inbreeding", "Outbreeding"],
            "rows": [
                ["Basis of Pairing", "Chance / Equal probability", "Phenotypic similarity (high x high)", "Phenotypic divergence (high x low)", "Close genetic relationship", "Unrelated individuals"],
                ["Gene Frequencies", "No change", "No change (unless selected)", "No change (unless selected)", "No change", "No change"],
                ["Homozygosity", "Constant (2pq)", "Increased at trait loci only", "Decreased at trait loci", "Increased genome-wide (F)", "Decreased genome-wide"],
                ["Population Variance", "Constant", "Increased (extreme types)", "Decreased (uniformity)", "Increased between lines", "Decreased in F1"],
                ["Primary Breeding Goal", "Control baseline / Neutral maintenance", "Produce superior seedstock / extreme performers", "Correct conformational and functional faults", "Fix prepotency and eliminate bad recessives", "Exploit hybrid vigour (heterosis)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In dairy cattle artificial insemination and herd mating plans, <b>Corrective Mating Programs (CMP)</b> use computerized linear classification scores. "
        "For example, a high-producing Holstein cow with excessively low rear udder attachment or sickle hocks is deliberately mated (disassortatively) to an AI sire with high proof (+2.5 SD) for rear udder height and straight rear leg conformation. "
        "This corrects conformational flaws in the daughter without sacrificing genetic gains for lactation milk yield."
    ),
    "tags": ["Mating Systems", "Panmixia", "Random Mating", "Assortative Mating", "Disassortative Mating", "Corrective Mating", "Pedigree Relationship"]
}

topics["u3-t09"] = {
    "summary": "Inbreeding is the mating of individuals more closely related than the population average, quantified by Wright's Inbreeding Coefficient (Fx) and Coefficient of Relationship (Rxy) calculated through pedigree arrow paths.",
    "desc": (
        "<b>DEFINITION AND CLASSIFICATION OF INBREEDING</b><br>"
        "<b>Inbreeding</b> is defined as the mating of individuals that are more closely related to each other than the average relationship among animals within the general population. "
        "Two individuals are related if they share one or more common ancestors within their recent ancestral pedigree (typically traced back 4 to 6 generations).<br><br>"
        "<b>Classification Based on Degree of Relationship:</b>"
        "<ul>"
        "<li><b>Close Breeding:</b> Mating of very close relatives (Relationship &ge; 50%)."
        "<br>&bull; Sire &times; Daughter (F = 25%)"
        "<br>&bull; Dam &times; Son (F = 25%)"
        "<br>&bull; Full Brother &times; Full Sister (Full-sib mating: F = 25%)"
        "<br>&bull; Used experimentally to develop inbred lines in laboratory animals and poultry.</li>"
        "<li><b>Linebreeding:</b> A milder, conservative form of inbreeding designed to maintain a high genetic relationship to a single admired or outstanding ancestor without causing excessive general inbreeding."
        "<br>&bull; Half-sib matings (Half brother &times; Half sister: F = 12.5%)"
        "<br>&bull; Cousin matings (First cousins: F = 6.25%)"
        "<br>&bull; Grandparent &times; Grandchild (F = 12.5%)"
        "<br>&bull; Relationship to the chosen ancestor remains high (&ge; 25–50%) while inbreeding coefficient F is kept below 6–12.5%.</li>"
        "</ul><br>"
        "<b>WRIGHT'S INBREEDING COEFFICIENT (Fx)</b><br>"
        "Formulated by <b>Sewall Wright (1921)</b>, the inbreeding coefficient <code>F_X</code> is defined as the probability that two homologous alleles at any randomly chosen gene locus in individual X are <b>Identical by Descent (IBD)</b> — meaning they are physical replication copies derived from a single common ancestor.<br><br>"
        "<b>General Formula for Fx (Pedigree Arrow Path Method):</b><br>"
        "<code>F_X = &Sigma; [ (1/2)^(n1 + n2 + 1) &times; (1 + F_A) ]</code><br>"
        "Where:"
        "<ul>"
        "<li><b>&Sigma;:</b> Summation across all independent connecting paths through all common ancestors.</li>"
        "<li><b>A:</b> Common ancestor shared by the sire (S) and dam (D) of individual X.</li>"
        "<li><b>n1:</b> Number of generations (arrows/steps) from the sire (S) back to the common ancestor (A).</li>"
        "<li><b>n2:</b> Number of generations (arrows/steps) from the dam (D) back to the common ancestor (A).</li>"
        "<li><b>F_A:</b> Inbreeding coefficient of the common ancestor A itself (if A is not inbred, <code>F_A = 0</code>).</li>"
        "</ul><br>"
        "<b>COEFFICIENT OF RELATIONSHIP (Rxy)</b><br>"
        "The Coefficient of Relationship <code>R_XY</code> measures the degree of pedigree kinship between two individuals X and Y. "
        "It represents the expected proportion of genes shared identical by descent between X and Y:<br><br>"
        "<code>R_XY = &Sigma; [ (1/2)^(n1 + n2) &times; (1 + F_A) ] / &radic;[ (1 + F_X) &times; (1 + F_Y) ]</code><br>"
        "Where <code>n1</code> is generations from X to common ancestor A, and <code>n2</code> is generations from Y to A. If neither X nor Y is inbred (<code>F_X = 0, F_Y = 0</code>), the denominator equals 1.<br><br>"
        "<b>STEP-BY-STEP PROCEDURE TO SOLVE INBREEDING VIA ARROW DIAGRAM</b><br>"
        "<ol>"
        "<li>Convert the tabular pedigree into a directed arrow diagram running strictly forward from ancestors to descendants.</li>"
        "<li>Identify the parents (Sire S and Dam D) of the target inbred individual X.</li>"
        "<li>Identify all <b>Common Ancestors (A)</b> that appear in both the sire's and dam's ancestral lines.</li>"
        "<li>Trace all independent, mutually exclusive paths from S up to A and down to D. (A path cannot pass through any individual more than once, nor reverse direction).</li>"
        "<li>Count the connecting arrows (steps) <code>n1</code> and <code>n2</code> for each path.</li>"
        "<li>Calculate <code>(1/2)^(n1 + n2 + 1) &times; (1 + F_A)</code> for each path and sum them up to obtain <code>F_X</code>.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Mal&eacute;cot's Kinship Coefficient & Pedigree Matrix Algebra:</b><br>"
        "In advanced animal breeding evaluations (Mixed Model BLUP):"
        "<ul>"
        "<li><b>Gustave Mal&eacute;cot (1948)</b> formulated the <b>Coefficient of Kinship / Parentage (&Phi;_SD):</b> The probability that two randomly drawn homologous alleles, one from sire S and one from dam D, are identical by descent.</li>"
        "<li>Fundamental Identity: The inbreeding coefficient of an individual is exactly equal to the kinship coefficient between its parents: <code>F_X = &Phi;_SD = (1/2) &times; A_SD</code>, where <code>A_SD</code> is the numerator relationship between sire S and dam D from Henderson's Numerator Relationship Matrix (<b>A</b> matrix).</li>"
        "<li><b>Selfing:</b> Maximum inbreeding rate occurs in self-fertilizing plants and hermaphrodites: <code>F_t = 1 - (1/2)^t</code>. Under continuous full-sib mating in livestock: <code>F_t = 0.5 F_{t-1} + 0.25 F_{t-2} + 0.25</code> (asymptotic approach to 100% homozygosity).</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Inbreeding is mating of individuals more closely related than the average of the population.",
        "Close breeding involves mating first-degree relatives (sire x daughter, full-sibs; F = 25%).",
        "Linebreeding maintains high relationship to an admired ancestor while keeping F low (< 12.5%).",
        "Sewall Wright (1921) defined F as the probability that two alleles at a locus are Identical by Descent (IBD).",
        "Wright's formula: Fx = Σ [ (1/2)^(n1 + n2 + 1) * (1 + FA) ].",
        "Coefficient of relationship Rxy measures the proportion of shared genes between two individuals.",
        "Relationship between full sibs is 0.50 (50%); between half sibs is 0.25 (25%); between parent-offspring is 0.50 (50%).",
        "Fx of an individual equals the coefficient of kinship (parentage) between its parents: Fx = Φ_SD.",
        "An arrow diagram traces directed paths from sire through common ancestor down to dam without reversing.",
        "If the common ancestor is itself inbred, the term (1 + FA) increases the inbreeding coefficient of the progeny.",
        "In closed breeding herds, inbreeding accumulates inevitably at the rate: ΔF = 1 / (2 Ne)."
    ],
    "tables": [
        {
            "title": "Coefficients of Relationship (R) and Inbreeding (F) in Standard Livestock Matings",
            "headers": ["Parameter / Mating Type", "Relationship of Mates (R_SD)", "Inbreeding of Offspring (F_X)", "Generations to Common Ancestor", "Primary Purpose"],
            "rows": [
                ["Self-fertilization (Selfing)", "1.00 (100%)", "0.500 (50.0%)", "n1=0, n2=0", "Theoretical ceiling / Plant genetics"],
                ["Parent x Offspring (Sire x Daughter)", "0.50 (50%)", "0.250 (25.0%)", "n1=0, n2=1", "Proving carrier status for lethal recessives"],
                ["Full Brother x Full Sister (Full-sibs)", "0.50 (50%)", "0.250 (25.0%)", "n1=1, n2=1 (2 parents)", "Experimental inbred line generation"],
                ["Half Brother x Half Sister (Half-sibs)", "0.25 (25%)", "0.125 (12.5%)", "n1=1, n2=1 (1 parent)", "Linebreeding in registered seedstock"],
                ["Grandparent x Grandchild", "0.25 (25%)", "0.125 (12.5%)", "n1=0, n2=2", "Linebreeding to a legendary ancestor"],
                ["First Cousins", "0.125 (12.5%)", "0.0625 (6.25%)", "n1=2, n2=2", "Incidental inbreeding in closed farm herds"],
                ["Second Cousins", "0.0312 (3.12%)", "0.0156 (1.56%)", "n1=3, n2=3", "Negligible risk / Near outbreeding threshold"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In small, closed gaushalas and isolated nucleus herds of indigenous breeds (e.g., Ongole, Tharparkar, Sahiwal), "
        "retaining a single bull for more than 3–4 years leads to involuntary <b>sire-daughter matings (F = 25%)</b> when his female calves reach breeding age. "
        "Veterinarians must routinely audit breeding pedigrees and enforce a strict <b>Bull Exchange / Sire Rotation Protocol</b> every 2.5 to 3 years to ensure herd inbreeding coefficient <code>F</code> remains strictly below 6.25%, preventing inbreeding depression and congenital malformations."
    ),
    "tags": ["Inbreeding", "Wright's Inbreeding Coefficient", "Coefficient of Relationship", "Arrow Diagram", "Close Breeding", "Linebreeding", "Kinship"]
}

topics["u3-t10"] = {
    "summary": "Inbreeding uniformly increases genome-wide homozygosity and exposes deleterious recessives, leading to inbreeding depression that severely impairs fitness, reproductive fertility, and early postnatal survival.",
    "desc": (
        "<b>PRIMARY GENETIC CONSEQUENCES OF INBREEDING</b><br>"
        "Inbreeding exerts profound genetic modifications across the entire genome:"
        "<ol>"
        "<li><b>Increase in Homozygosity and Decrease in Heterozygosity:</b>"
        "<br>&bull; With each generation of inbreeding, heterozygous gene pairs (Aa) are progressively halved and converted into homozygous pairs (AA and aa)."
        "<br>&bull; The proportion of homozygous loci increases directly by Wright's coefficient <code>F</code>:"
        "<br>&nbsp;&nbsp;<code>P(AA) = p&sup2; + Fpq</code>"
        "<br>&nbsp;&nbsp;<code>P(Aa) = 2pq(1 - F)</code>"
        "<br>&nbsp;&nbsp;<code>P(aa) = q&sup2; + Fpq</code>"
        "<br>&bull; When <code>F = 1.0</code>, heterozygosity becomes zero; the population is completely homozygous and fixed.</li>"
        "<li><b>Fixation of Alleles:</b>"
        "<br>&bull; Alleles become permanently fixed (frequency = 1.0) or lost (frequency = 0) in different inbred sub-lines by random genetic drift and lineage divergence.</li>"
        "<li><b>Phenotypic Differentiation into Distinct Inbred Lines:</b>"
        "<br>&bull; A single heterogeneous population splits into numerous uniform, distinct sub-lines that differ dramatically from one another in phenotype and genotype.</li>"
        "<li><b>Increase in Prepotency:</b>"
        "<br>&bull; <b>Prepotency</b> is the ability of an animal to stamp its own characteristics onto its offspring so that the offspring uniformly resemble the parent and one another."
        "<br>&bull; Directly caused by increased homozygosity: a homozygous dominant sire (AA) can only transmit the 'A' allele to gametes, guaranteeing that every progeny receives 'A' regardless of the dam's genotype.</li>"
        "<li><b>Exposure of Deleterious Recessive Alleles:</b>"
        "<br>&bull; Harmful recessives normally masked in heterozygous condition (Aa) are forced into homozygous expression (aa), unmasking lethal, semi-lethal, and sub-vital genetic defects.</li>"
        "</ol><br>"
        "<b>INBREEDING DEPRESSION (ID)</b><br>"
        "<b>Definition:</b> Inbreeding depression is the reduction in phenotypic mean performance of fitness, reproductive, and physiological traits observed when an animal population is subjected to inbreeding.<br><br>"
        "<b>Characteristics of Traits Affected:</b>"
        "<ul>"
        "<li><b>Highest Depression:</b> Traits associated with Darwinian fitness, reproduction, and early survival (conception rate, litter size, calf viability, neonatal mortality, libido). These traits are governed by genes exhibiting directional dominance and overdominance.</li>"
        "<li><b>Moderate Depression:</b> Growth rate, weaning weight, daily weight gain, and milk yield.</li>"
        "<li><b>Lowest / Negligible Depression:</b> Conformation, skeletal body measurements (height at withers), carcass dressing percentage, and fleece quality (governed primarily by additive genes).</li>"
        "</ul><br>"
        "<b>Rule of Thumb in Dairy Cattle:</b> For every <b>1% increase in inbreeding coefficient (F)</b>, there is an approximate loss of <b>20 to 25 kg of 305-day lactation milk yield</b>, an increase of <b>0.5 to 1 day in calving interval</b>, and a significant rise in calf mortality.<br><br>"
        "<b>PURGING THE GENETIC LOAD</b><br>"
        "While inbreeding exposes lethal recessives, if accompanied by <b>rigorous, merciless culling</b> of affected individuals (aa), the deleterious recessive alleles ('a') are progressively eliminated from the population. This deliberate cleansing is called <b>Purging the Genetic Load</b>."
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Biometrical Derivation of Inbreeding Depression:</b><br>"
        "Let the genotypic values of <code>AA</code>, <code>Aa</code>, and <code>aa</code> be <code>+a</code>, <code>d</code>, and <code>-a</code> respectively (Falconer's metric model):"
        "<ul>"
        "<li>Population mean under random mating: <code>M_0 = a(p - q) + 2dpq</code></li>"
        "<li>Population mean after inbreeding with coefficient <code>F</code>: <code>M_F = a(p - q) + 2dpq(1 - F) = M_0 - 2dpqF</code></li>"
        "<li>The change in phenotypic mean (Depression): <code>&Delta;M = -2dpqF</code>.</li>"
        "<li><b>Key Inferences for 10/10 Score:</b>"
        "<br>&bull; Inbreeding depression is <i>strictly directional</i> and occurs <b>only if dominance (d &ne; 0) exists</b>. If all genes act additively (<code>d = 0</code>), inbreeding causes zero phenotypic depression!"
        "<br>&bull; The magnitude of depression is directly proportional to the degree of inbreeding (<code>F</code>), the dominance deviation (<code>d</code>), and gene frequencies (<code>2pq</code>).</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Inbreeding increases homozygosity and decreases heterozygosity across the genome.",
        "Genotypic frequencies under inbreeding: P(AA) = p² + Fpq, P(Aa) = 2pq(1-F), P(aa) = q² + Fpq.",
        "Inbreeding unmasks hidden deleterious recessive alleles, causing congenital defects.",
        "Prepotency is the ability of an animal to stamp its characteristics onto offspring due to homozygous dominance.",
        "Inbreeding depression is the reduction in phenotypic mean of fitness and reproductive traits.",
        "Fitness traits (fertility, embryo survival, neonate viability) suffer the highest inbreeding depression.",
        "Skeletal and conformation traits governed by additive genes show minimal inbreeding depression.",
        "In dairy cattle, each 1% rise in F causes ~20-25 kg reduction in 305-day milk yield.",
        "Inbreeding depression occurs only when dominance deviation is present (ΔM = -2dpqF).",
        "Purging is the deliberate culling of defective homozygotes exposed by inbreeding to cleanse genetic load.",
        "Acceptable safe threshold for cumulative inbreeding in commercial livestock herds is F < 6.25%."
    ],
    "tables": [
        {
            "title": "Severity of Inbreeding Depression Across Different Livestock Traits",
            "headers": ["Criterion / Trait Class", "Degree of Depression", "Gene Action Involved", "Typical Livestock Traits", "Management Remedy"],
            "rows": [
                ["Fitness & Reproduction", "Severe / Very High (5–15% decline per 10% F)", "Dominance and Overdominance (d > 0)", "Calving rate, litter size in swine, embryo survival, libido, calf vigor", "Crossbreeding or immediate outcrossing"],
                ["Physiological & Production", "Moderate (2–5% decline per 10% F)", "Partial dominance with additive effects", "305-day milk yield, weaning weight, daily body gain, egg production", "Sire rotation, linebreeding with strict culling"],
                ["Morphological & Skeletal", "Low to Negligible (< 1% change)", "Additive gene action (d = 0)", "Height at withers, chest depth, bone circumference, fleece fiber diameter", "Mass selection without inbreeding concern"],
                ["Lethal & Semi-lethal Defects", "Disastrous when exposed", "Single homozygous recessives (aa)", "Bovine Leukocyte Adhesion Deficiency (BLAD), Citrullinemia, Syndactyly", "DNA testing of sires & complete culling of carriers"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In Indian veterinary practice, artificial insemination using carrier semen historically spread lethal recessives such as "
        "<b>BLAD (Bovine Leukocyte Adhesion Deficiency)</b>, <b>DUMPs (Deficiency of Uridine Monophosphate Synthase)</b>, and <b>Citrullinemia</b> in crossbred Holstein-Friesian and Murrah herds. "
        "Under intensive inbreeding, these calves die of recurrent intractable diarrhea, pneumonia, or neurological seizures within weeks of birth. "
        "Strict national standards now mandate PCR-RFLP / capillary sequencing screening of all breeding bulls at semen stations to guarantee carrier-free status (free of lethal recessives) before semen release."
    ),
    "tags": ["Inbreeding Depression", "Homozygosity", "Prepotency", "Purging", "Genetic Load", "BLAD", "Fitness Traits"]
}

topics["u3-t11"] = {
    "summary": "Outbreeding systems mate individuals less closely related than the population average, encompassing outcrossing, topcrossing, grading up, and crossbreeding systems to elevate heterozygosity and maximize hybrid vigour.",
    "desc": (
        "<b>DEFINITION AND GENETIC BASIS OF OUTBREEDING</b><br>"
        "<b>Outbreeding</b> is the mating of animals that are less closely related to each other than the average relationship among individuals in the population. "
        "Genetically, outbreeding is the exact antithesis of inbreeding: it <b>increases heterozygosity</b>, masks deleterious recessive alleles behind dominant wild-type alleles, and generates <b>Heterosis (Hybrid Vigour)</b>.<br><br>"
        "<b>SYSTEMS OF OUTBREEDING WITHIN THE SAME BREED</b><br>"
        "<ul>"
        "<li><b>1. Outcrossing:</b>"
        "<br>&bull; Mating of completely unrelated individuals of the <b>same pure breed</b> having no common ancestors in their pedigree for at least 4 to 6 generations."
        "<br>&bull; <i>Purpose:</i> The most common mating system in purebred herds. It prevents inbreeding accumulation while introducing fresh genetic variation, revitalizing vigor without diluting breed purity.</li>"
        "<li><b>2. Topcrossing:</b>"
        "<br>&bull; Mating of an inbred or highly superior linebred sire (usually from a prestigious nucleus herd or inbred line) to ordinary, non-inbred purebred females of the same breed."
        "<br>&bull; <i>Purpose:</i> Injects the prepotency and genetic excellence of an inbred line into commercial registered herds.</li>"
        "</ul><br>"
        "<b>OUTBREEDING SYSTEMS BETWEEN DIFFERENT BREEDS</b><br>"
        "<ul>"
        "<li><b>3. Grading Up:</b>"
        "<br>&bull; A continuous, systematic breeding practice where ordinary, unimproved, non-descript (indigenous scrub) females are mated generation after generation to purebred sires of a distinct, superior breed."
        "<br>&bull; <i>Fraction of Superior Breed Inheritance:</i>"
        "<br>&nbsp;&nbsp;Generation 1 (F1): <code>1/2 (50.0%)</code>"
        "<br>&nbsp;&nbsp;Generation 2 (Backcross 1): <code>3/4 (75.0%)</code>"
        "<br>&nbsp;&nbsp;Generation 3 (Backcross 2): <code>7/8 (87.5%)</code>"
        "<br>&nbsp;&nbsp;Generation 4 (Backcross 3): <code>15/16 (93.75%)</code>"
        "<br>&nbsp;&nbsp;Generation 5 (Backcross 4): <code>31/32 (96.875%)</code>"
        "<br>&nbsp;&nbsp;Generation 6 (Backcross 5): <code>63/64 (98.44%)</code>"
        "<br>&bull; By the <b>5th or 6th generation</b> (over 96.88% purity), the graded-up animals are phenotypically and genetically indistinguishable from purebreds and can be registered in breed herdbooks."
        "<br>&bull; <i>Greatest Utility:</i> Upgrading massive populations of non-descript Indian cattle with Sahiwal/Gir, or local non-descript buffaloes with pure Murrah sires.</li>"
        "<li><b>4. Crossbreeding:</b>"
        "<br>&bull; Mating of individuals belonging to two or more distinctly different established breeds."
        "<br>&bull; <i>Purposes:</i> (a) Exploit heterosis (hybrid vigor), (b) Combine complementary traits from different breeds (<b>Breed Complementarity</b>), and (c) Form the genetic foundation for synthesizing new synthetic breeds.</li>"
        "</ul><br>"
        "<b>SYSTEMATIC COMMERCIAL CROSSBREEDING DESIGNS</b><br>"
        "<ol>"
        "<li><b>Two-Breed Cross (Single Cross / Terminal Cross):</b>"
        "<br>&bull; Breed A sire &times; Breed B dam &rarr; F1 progeny (AB)."
        "<br>&bull; All F1 males and females are marketed for meat or commercial production; none are retained for breeding."
        "<br>&bull; Yields 100% individual heterosis; zero maternal heterosis.</li>"
        "<li><b>Crisscrossing (Two-Breed Rotational Cross):</b>"
        "<br>&bull; Two breeds (A and B) are used alternately across generations."
        "<br>&bull; F1 females (AB) are mated back to Breed A sires &rarr; progeny (3/4 A, 1/4 B). These females are then mated to Breed B sires &rarr; progeny (5/8 B, 3/8 A)."
        "<br>&bull; At equilibrium, maintains <b>66.7% (2/3)</b> of maximum possible individual and maternal heterosis while producing replacement females on-farm.</li>"
        "<li><b>Three-Breed Rotational Cross:</b>"
        "<br>&bull; Three breeds (A, B, C) rotated in succession: A &times; B &rarr; AB &times; C &rarr; ABC &times; A..."
        "<br>&bull; At equilibrium, retains <b>85.7% (6/7)</b> of maximum individual and maternal heterosis.</li>"
        "<li><b>Three-Breed Terminal Cross:</b>"
        "<br>&bull; Crossbred F1 dams (AB, exploiting 100% maternal heterosis for milk, litter size, and mothering ability) are mated to an unrelated terminal meat-sire Breed C (selected strictly for growth rate and muscularity)."
        "<br>&bull; All three-breed terminal progeny (ABC) are slaughtered for market. Standard in commercial swine and sheep industries.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>General Mathematical Formula for Retained Heterosis in Rotational Crosses:</b><br>"
        "In competitive entrance and board examinations, calculate equilibrium retained heterosis (<code>RH</code>) using the formula:"
        "<code>RH = [ (2^n - 2) / (2^n - 1) ] &times; 100</code> (where <code>n</code> = number of breeds in rotation)."
        "<ul>"
        "<li>For a <b>2-breed rotation (crisscrossing):</b> <code>RH = (4 - 2)/(4 - 1) = 2/3 = 66.67%</code></li>"
        "<li>For a <b>3-breed rotation:</b> <code>RH = (8 - 2)/(8 - 1) = 6/7 = 85.71%</code></li>"
        "<li>For a <b>4-breed rotation:</b> <code>RH = (16 - 2)/(16 - 1) = 14/15 = 93.33%</code></li>"
        "<li><b>Breed Complementarity:</b> The distinct economic advantage where the strengths of one breed compensate for the weaknesses of another (e.g., crossing a high-yielding, heat-sensitive Holstein Friesian with a hardy, tick-resistant, heat-tolerant Gir or Tharparkar cow).</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Outbreeding mates individuals less related than the average of the population.",
        "Outbreeding increases heterozygosity and produces heterosis (hybrid vigor).",
        "Outcrossing mates unrelated animals within the same pure breed (no common ancestor for 4-6 generations).",
        "Topcrossing mates an inbred or superior linebred sire to non-inbred purebred females of the same breed.",
        "Grading up is the continuous backcrossing of non-descript scrub females to purebred sires of a superior breed.",
        "In grading up, purebred inheritance reaches 50%, 75%, 87.5%, 93.75%, and 96.88% from 1st to 5th generation.",
        "By the 5th generation (31/32 or 96.88%), graded animals become practically indistinguishable from purebreds.",
        "Crossbreeding mates animals of two or more distinct breeds to capture heterosis and breed complementarity.",
        "Two-breed rotational crossing (crisscrossing) retains 66.7% (2/3) of maximum heterosis at equilibrium.",
        "Three-breed rotational crossing retains 85.7% (6/7) of maximum individual and maternal heterosis.",
        "Three-breed terminal crossing mates crossbred F1 dams (AB) to a terminal sire (C) for meat marketing."
    ],
    "tables": [
        {
            "title": "Comprehensive Classification and Comparison of Outbreeding Systems",
            "headers": ["Parameter / System", "Parental Genetic Relationship", "Generations Required", "Retained Heterosis", "Primary Field Livestock Utility"],
            "rows": [
                ["Outcrossing", "Unrelated, same pure breed", "1 generation (per mating)", "Minimal (within-breed vigor)", "Standard practice in purebred dairy and beef cattle herds"],
                ["Topcrossing", "Inbred sire x non-inbred females", "1 generation", "Low to moderate", "Disseminate elite inbred seedstock genetics into commercial herds"],
                ["Grading Up", "Non-descript scrub dam x pure sire", "5 to 6 generations (96.88% purity)", "Transitory in early crosses; converts to purebred", "Upgrading indigenous non-descript cattle/buffaloes in rural India"],
                ["Two-Breed Terminal Cross", "Two distinct pure breeds (A x B)", "1 generation (all progeny marketed)", "100% individual heterosis (0% maternal)", "Commercial broiler and beef production"],
                ["Crisscrossing (2-Breed)", "Two breeds rotated alternately", "Continuous alternating cycles", "66.7% (2/3) at equilibrium", "Commercial swine and dual-purpose sheep systems"],
                ["Three-Breed Terminal Cross", "F1 crossbred dam (AB) x Terminal sire (C)", "2 stages (continuous F1 + terminal)", "100% individual + 100% maternal heterosis", "Commercial pork and prime lamb meat production"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In India, the <b>Grading Up of non-descript buffaloes with pure Murrah sires</b> has been the single most transformative livestock development success story. "
        "Over 65% of India's indigenous buffaloes were unimproved scrub animals producing under 600 kg milk per lactation. "
        "Through massive state AI networks utilizing frozen Murrah semen across Punjab, Haryana, UP, and Andhra Pradesh, successive generations reached 3rd (87.5%) and 4th (93.75%) graded-up status, boosting lactation yields to 1,800–2,500 kg with 7% fat."
    ),
    "tags": ["Outbreeding", "Outcrossing", "Topcrossing", "Grading Up", "Crossbreeding", "Crisscrossing", "Terminal Cross"]
}

topics["u3-t12"] = {
    "summary": "Heterosis (hybrid vigour) is the phenotypic superiority of crossbred progeny over the average of their purebred parental breeds, explained genetically by the dominance, overdominance, and epistasis hypotheses.",
    "desc": (
        "<b>DEFINITION OF HETEROSIS (HYBRID VIGOUR)</b><br>"
        "<b>Heterosis</b>, coined by <b>George Harrison Shull (1914)</b>, is the phenomenon wherein crossbred offspring (F1 generation) exhibit phenotypic superiority in growth, fertility, survival, or production over the mean of their purebred parental lines or breeds. "
        "The biological reverse of inbreeding depression, heterosis is directly driven by increased genome-wide heterozygosity.<br><br>"
        "<b>MATHEMATICAL ESTIMATION OF HETEROSIS</b><br>"
        "Heterosis is expressed in absolute units or as a percentage over the parental average:"
        "<ol>"
        "<li><b>Mid-Parent Heterosis (Standard Heterosis):</b>"
        "<br><code>Heterosis (H) = F1 - [ (P1 + P2) / 2 ]</code>"
        "<br><code>Heterosis % (H%) = [ (F1 - MidParent) / MidParent ] &times; 100</code>"
        "<br>Where <code>F1</code> is the mean of crossbred progeny, and <code>P1, P2</code> are the purebred parental means.</li>"
        "<li><b>High-Parent Heterosis (Better-Parent Heterosis / Heterobeltiosis):</b>"
        "<br><code>Heterobeltiosis = [ (F1 - BetterParent) / BetterParent ] &times; 100</code>"
        "<br>Proves true economic superiority: F1 outperforms even the best individual parental breed.</li>"
        "</ol><br>"
        "<b>TYPES OF HETEROSIS</b><br>"
        "<ul>"
        "<li><b>Individual (Direct) Heterosis:</b> The advantage of the crossbred individual itself due to its own crossbred genome (e.g., faster growth rate, higher vitality).</li>"
        "<li><b>Maternal Heterosis:</b> The advantage of using a crossbred female as a mother, providing superior uterine environment, higher milk yield, and excellent mothering ability to her progeny.</li>"
        "<li><b>Paternal Heterosis:</b> The advantage of using a crossbred male as a sire, reflected in higher libido, superior semen volume/viability, and improved conception rates.</li>"
        "</ul><br>"
        "<b>GENETIC THEORIES OF HETEROSIS</b><br>"
        "<ol>"
        "<li><b>Dominance Hypothesis (Davenport 1908, Bruce 1910, Keeble and Pellew 1910):</b>"
        "<br>&bull; Heterosis is caused by the masking of undesirable recessive alleles contributed by one parent with favorable dominant alleles contributed by the other parent at multiple loci."
        "<br>&bull; <i>Example:</i> Parent 1 has genotype <code>AAbbCCdd</code>; Parent 2 has genotype <code>aaBBccDD</code>. Both parents express inferior phenotypes due to homozygous recessives. The F1 crossbred is <code>AaBbCcDd</code>, possessing favorable dominant alleles at all four loci!"
        "<br>&bull; <i>Criticism:</i> If pure dominance were the only cause, it should theoretically be possible to isolate a homozygous true-breeding pure line (<code>AABBCCDD</code>) that equals the F1. In practice, this is rarely achieved due to tight linkage between favorable and unfavorable genes (repulsion phase linkage).</li>"
        "<li><b>Overdominance Hypothesis (East 1908, Shull 1908, Hull 1945):</b>"
        "<br>&bull; Heterozygotes (<code>Aa</code>) at a locus possess superior physiological fitness and metabolic versatility compared to either homozygote (<code>AA</code> or <code>aa</code>)."
        "<br>&bull; <i>Single Gene Superiority:</i> Heterozygote produces two distinct allelic protein variants (e.g., two enzyme isoforms with different temperature optima), providing broader biochemical adaptability."
        "<br>&bull; Under overdominance, the F1 cannot be fixed into a pure-breeding homozygous line because selfing or inter-se mating inevitably segregates out inferior homozygotes (1/4 AA, 1/2 Aa, 1/4 aa).</li>"
        "<li><b>Epistasis Hypothesis (Inter-allelic Interaction):</b>"
        "<br>&bull; Favorable non-allelic interactions between genes at different loci (additive &times; dominance, dominance &times; dominance epistasis) created in the F1 cross.</li>"
        "</ol>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Recombination Loss in F2 and Inter-Se Generations:</b><br>"
        "In university exams, explain why heterosis declines from F1 to F2:"
        "<ul>"
        "<li><b>F2 Breakdown (Recombination Loss):</b> When F1 crossbreds are mated among themselves (inter-se: F1 &times; F1), 50% of individual heterosis is lost due to segregation: <code>H_{F2} = (1/2) H_{F1}</code>.</li>"
        "<li>Additionally, crossing over shatters favorable epistatic gene complexes built up by selection in the parental breeds, causing high phenotypic variability and reduced performance in the F2 generation.</li>"
        "<li><b>Cockerham's Variance Model:</b> Heterosis expression is mathematically equal to: <code>&Sigma; d_i (p_1i - p_2i)&sup2;</code> where <code>d_i</code> is dominance deviation at locus <i>i</i> and <code>(p_1i - p_2i)</code> is the difference in gene frequency between the two crossing breeds.</li>"
        "<li><b>Crucial Deductions:</b>"
        "<br>&bull; Heterosis requires <b>directional dominance (d &gt; 0)</b>."
        "<br>&bull; Heterosis is maximized when crossing breeds that have <b>widely divergent gene frequencies</b> (maximum genetic distance). Crossing closely related breeds yields little heterosis!</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Heterosis (hybrid vigour), coined by G.H. Shull (1914), is the phenotypic superiority of F1 crossbreds over parents.",
        "Mid-parent heterosis % = [ (F1 - MidParent) / MidParent ] * 100.",
        "Heterobeltiosis is the superiority of F1 crossbred over the better purebred parent.",
        "Individual heterosis is the direct phenotypic advantage of the crossbred individual.",
        "Maternal heterosis is the advantage offered by a crossbred dam (superior uterus, lactation, mothering).",
        "Paternal heterosis is the advantage of a crossbred sire (higher libido, superior semen quality).",
        "Dominance hypothesis states that heterosis results from favorable dominant alleles masking harmful recessives.",
        "Overdominance hypothesis states that the heterozygote (Aa) is physiologically superior to both homozygotes (AA, aa).",
        "Epistasis hypothesis attributes heterosis to favorable non-allelic gene interactions.",
        "Heterosis is highest for low-heritability fitness and fertility traits (conception rate, survival, litter size).",
        "Heterosis is directly proportional to genetic distance (divergence in gene frequency) between parental breeds."
    ],
    "tables": [
        {
            "title": "Comparison of Classical Hypotheses Explaining Heterosis",
            "headers": ["Parameter / Feature", "Dominance Hypothesis", "Overdominance Hypothesis", "Epistasis Hypothesis"],
            "rows": [
                ["Pioneering Proponents", "Davenport (1908), Bruce (1910)", "East (1908), Shull (1908), Hull (1945)", "Wright (1935), Cockerham (1954)"],
                ["Locus Level Action", "Intra-allelic (Dominant vs Recessive)", "Intra-allelic (Single gene overdominance)", "Inter-allelic (Non-allelic interactions)"],
                ["Genotypic Advantage", "AA = Aa > aa (Dominant masks recessive)", "Aa > AA and Aa > aa (Heterozygote superior)", "A_B_ combinations superior to others"],
                ["Can True-breeding Pureline Equal F1?", "Theoretically YES (AABBCCDD), but blocked by linkage", "Theoretically IMPOSSIBLE (inevitable segregation in F2)", "Theoretically possible only if complete linkage blocks recombination"],
                ["F2 Segregation Effect", "Minor loss due to linkage repulsion", "50% loss of heterosis due to Mendelian segregation", "Recombination loss due to crossing over"],
                ["Breeding Selection Strategy", "Standard recurrent selection for general combining ability", "Reciprocal recurrent selection (RRS) for specific combining ability", "Selection for stable co-adapted gene complexes"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In commercial poultry, white-egg commercial layers (e.g., BV-300, Babcock-300) and commercial broilers (Cobb-500, Ross-308) "
        "exploit over <b>25–35% heterosis</b> for juvenile growth rate, feed conversion ratio (FCR), and annual egg production. "
        "Commercial poultry breeding companies never sell pure parental lines to farmers; they sell only <b>four-way cross chicks</b>. "
        "Farmers who attempt to mate commercial broiler or layer birds together suffer catastrophic <b>F2 breakdown</b>: growth drops by 30%, egg production plunges by 40%, and flock uniformity is completely lost."
    ),
    "tags": ["Heterosis", "Hybrid Vigour", "Dominance Hypothesis", "Overdominance Hypothesis", "Epistasis", "Heterobeltiosis", "F2 Breakdown"]
}

topics["u3-t13"] = {
    "summary": "Selection for combining ability evaluates parental lines using General Combining Ability (GCA - additive gene action) via Recurrent Selection and Specific Combining Ability (SCA - non-additive gene action) via Reciprocal Recurrent Selection.",
    "desc": (
        "<b>COMBINING ABILITY: CONCEPTS AND DEFINITIONS</b><br>"
        "<b>Sprague and Tatum (1942)</b> defined combining ability to measure the performance of inbred lines or parental breeds in cross combinations:"
        "<ol>"
        "<li><b>General Combining Ability (GCA):</b>"
        "<br>&bull; The average performance of an inbred line or breed across a series of crosses with several other lines."
        "<br>&bull; <i>Genetic Basis:</i> Controlled primarily by <b>additive gene action</b> and additive &times; additive epistasis."
        "<br>&bull; <i>Breeding Implication:</i> Highly responsive to traditional progeny testing and phenotypic selection; results are predictable and transmissible.</li>"
        "<li><b>Specific Combining Ability (SCA):</b>"
        "<br>&bull; Cases where certain specific cross combinations perform significantly better or worse than what would be predicted based on the average GCA of the two parental lines."
        "<br>&bull; <i>Genetic Basis:</i> Controlled by <b>non-additive gene action</b> (dominance, overdominance, and dominance &times; dominance epistasis)."
        "<br>&bull; <i>Breeding Implication:</i> Generates heterosis; cannot be captured by standard mass selection; requires specialized cross-testing designs.</li>"
        "</ol><br>"
        "<b>RECURRENT SELECTION (RS)</b><br>"
        "Proposed by <b>Fred Hull (1945)</b> to systematically improve combining ability for a quantitative trait:"
        "<ul>"
        "<li><b>Procedure:</b>"
        "<br>1. Several individual plants or animals from a broad-based foundation population are crossed to a <b>constant tester line</b>."
        "<br>&bull; If the tester is a <i>broad-based genetically diverse tester</i> &rarr; Selects primarily for <b>General Combining Ability (GCA)</b>."
        "<br>&bull; If the tester is a <i>homozygous, narrow-based inbred line</i> &rarr; Selects for <b>Specific Combining Ability (SCA)</b> and overdominance."
        "<br>2. Evaluate the crossbred progeny for target production traits."
        "<br>3. Select the best parental lines whose crossbred progeny were top performers."
        "<br>4. Inter-mate the selected parental lines (inter-se) to reconstitute an improved population for the next cycle of selection.</li>"
        "</ul><br>"
        "<b>RECIPROCAL RECURRENT SELECTION (RRS)</b><br>"
        "Formulated by <b>Comstock, Robinson, and Harvey (1949)</b>, RRS is the gold-standard breeding design to <b>simultaneously select for both GCA and SCA</b> across two genetically distinct populations (Population A and Population B):"
        "<ul>"
        "<li><b>Biological Principle:</b> Neither population needs an inbred tester. Population A serves as the tester for Population B, and simultaneously Population B serves as the tester for Population A!</li>"
        "<li><b>Step-by-Step Selection Cycle (3-Year / 3-Generation Cycle in Poultry/Swine):</b>"
        "<br><b>Year 1 (Testcross Matings):</b>"
        "<br>&bull; Males from Population A are mated to females from Population B &rarr; produce Crossbred Progeny (AB)."
        "<br>&bull; Simultaneously, males from Population B are mated to females from Population A &rarr; produce Reciprocal Crossbred Progeny (BA)."
        "<br>&bull; Parental males and females are maintained safely in reserve (or pedigree-tracked)."
        "<br><b>Year 2 (Performance Testing):</b>"
        "<br>&bull; Crossbred progenies (AB and BA) are tested under commercial field conditions for egg production, feed conversion, growth rate, and livability."
        "<br>&bull; The testcross performance identifies which purebred sires and dams possessed superior combining ability."
        "<br><b>Year 3 (Intra-Population Pureline Propagation):</b>"
        "<br>&bull; The top-ranking males and females within Population A (judged strictly by their crossbred progeny's performance) are mated <i>inter-se</i> to reconstitute and multiply an improved Pureline A."
        "<br>&bull; Similarly, the top-ranking males and females within Population B are mated <i>inter-se</i> to reconstitute Pureline B."
        "<br>&bull; Cycle repeats: Cycle 2, Cycle 3, etc.</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>Why RRS Outperforms All Other Systems for Heterosis Exploitation:</b><br>"
        "In university exams, explain the genetic allele-frequency dynamics under RRS:"
        "<ul>"
        "<li>Consider a locus with two alleles (<code>A1</code> and <code>A2</code>) exhibiting <b>overdominance</b> (<code>A1A2</code> superior to both <code>A1A1</code> and <code>A2A2</code>):"
        "<br>&bull; If Population A happens to have a higher frequency of <code>A1</code>, testcross performance with B will be maximized whenever Population B provides <code>A2</code>."
        "<br>&bull; Over successive cycles of RRS, selection systematically forces <b>fixation of A1 in Population A (p &rarr; 1.0)</b> and <b>fixation of A2 in Population B (q &rarr; 1.0)</b>!"
        "<br>&bull; Result: Pureline A becomes completely <code>A1A1</code> and Pureline B becomes completely <code>A2A2</code>. When crossed, they yield <b>100% heterozygous A1A2 crossbreds</b>, permanently capturing maximal overdominance heterosis!</li>"
        "<li>Simultaneously, for loci exhibiting additive gene action, RRS fixes the favorable additive alleles in both populations, improving baseline GCA. Thus, RRS captures additive variance, dominance variance, and overdominance simultaneously.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "Combining ability evaluates the capacity of inbred lines or breeds to produce superior crossbred progeny.",
        "General Combining Ability (GCA) is the average performance of a line across crosses, governed by additive gene action.",
        "Specific Combining Ability (SCA) is the deviation of a specific cross from expectation, governed by non-additive gene action.",
        "Recurrent Selection (RS), proposed by Fred Hull (1945), evaluates parents using a single tester line.",
        "Reciprocal Recurrent Selection (RRS) was developed by Comstock, Robinson, and Harvey (1949).",
        "In RRS, Population A serves as the tester for Population B, and Population B serves as the tester for Population A.",
        "RRS simultaneously exploits both additive gene effects (GCA) and non-additive/overdominance effects (SCA).",
        "In RRS, purebred parents are selected solely on the basis of their crossbred progeny's commercial performance.",
        "Selected parents are propagated pure within their own line (A x A and B x B) to reconstitute the next cycle.",
        "RRS drives mutually divergent allele fixation at overdominant loci (A1 fixed in Line A, A2 fixed in Line B).",
        "RRS is the fundamental breeding design utilized by global commercial poultry layer and broiler breeding companies."
    ],
    "tables": [
        {
            "title": "Comparison Between General Combining Ability (GCA) and Specific Combining Ability (SCA)",
            "headers": ["Parameter / Feature", "General Combining Ability (GCA)", "Specific Combining Ability (SCA)"],
            "rows": [
                ["Definition", "Average performance of a line across many diverse tester crosses", "Performance of a specific cross combination compared to expectation"],
                ["Primary Gene Action", "Additive gene action and Additive x Additive epistasis", "Non-additive: Dominance, Overdominance, Dominance x Dominance"],
                ["Heritability of Trait", "Usually moderate to high (h² > 0.30)", "Usually low (h² < 0.15, high environmental influence)"],
                ["Predictability", "Highly predictable; transmissible across generations", "Unpredictable; unique to the specific parental pair"],
                ["Breeding Selection Method", "Mass selection, family selection, progeny testing", "Reciprocal Recurrent Selection (RRS), diallel cross evaluation"],
                ["Commercial Application", "Developing superior pure breeds and synthetic breeds", "Commercial hybrid seed, commercial broilers and layer lines"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In commercial poultry genetics, RRS is applied between <b>White Leghorn strains (Strain A and Strain B)</b> to produce commercial egg layers. "
        "Neither Strain A nor Strain B is sold to commercial egg farmers. "
        "Instead, private hatcheries run 3-year RRS cycles in closed nucleus pedigree farms. "
        "The crossbred female chicks (A &times; B) possess phenomenal SCA, producing <b>320–335 eggs per hen housed</b> with exceptionally low feed consumption (1.35 kg feed per dozen eggs) and negligible mortality."
    ),
    "tags": ["Combining Ability", "GCA", "SCA", "Recurrent Selection", "Reciprocal Recurrent Selection", "RRS", "Overdominance", "Poultry Breeding"]
}

topics["u3-t14"] = {
    "summary": "Genetic improvement of dairy cattle and buffaloes in India couples selective breeding in superior indigenous breeds with structured crossbreeding using exotic dairy sires in non-descript cattle, supported by progeny testing and AI.",
    "desc": (
        "<b>LIVESTOCK SCENARIO AND PRODUCTION CHALLENGES IN INDIA</b><br>"
        "India possesses the world's largest bovine population (~303 million cattle and buffaloes) and is the global leader in milk production. "
        "However, average animal productivity remains constrained by late age at first calving (36–48 months), long calving intervals (15–20 months), short lactations, poor feed resources, and tropical heat/disease stress.<br><br>"
        "<b>BREEDING STRATEGY FOR INDIGENOUS CATTLE BREEDS</b><br>"
        "India possesses world-renowned indigenous (Zebu / <i>Bos indicus</i>) dairy and dual-purpose cattle breeds (Sahiwal, Gir, Red Sindhi, Tharparkar, Rathi, Kankrej, Ongole):"
        "<ul>"
        "<li><b>Breeding Policy:</b> <b>Selective Breeding within Purebred Populations</b>."
        "<br>&bull; No crossbreeding with exotic breeds is permitted in native breeding tracts to preserve genetic identity, heat tolerance, tick resistance, and adaptation to low-input systems."
        "<br>&bull; <i>Methods:</i> Pedigree selection of dams &plus; Progeny Testing / Genomic Evaluation of young bulls &plus; Open Nucleus Breeding Systems (ONBS)."
        "<br>&bull; Bull selection focuses on maternal 305-day milk yield (> 3,500 kg in Sahiwal/Gir) and sire conception rates.</li>"
        "</ul><br>"
        "<b>BREEDING STRATEGY FOR NON-DESCRIPT CATTLE (CROSSBREEDING)</b><br>"
        "Non-descript (scrub) cattle constitute over 60% of indigenous cattle, yielding under 400–600 kg milk per lactation:"
        "<ul>"
        "<li><b>Breeding Policy:</b> <b>Crossbreeding with Exotic Dairy Breeds</b> (Holstein-Friesian and Jersey)."
        "<br>&bull; <b>Jersey</b> is preferred in hilly, humid, and rainfed rural areas due to medium body size, lower maintenance feed requirements, heat tolerance, and higher milk fat percentage (4.5–5.0%)."
        "<br>&bull; <b>Holstein-Friesian (HF)</b> is preferred in irrigated, intensive dairy belts with abundant green fodder and stall-feeding management due to unmatched volumetric milk yields.</li>"
        "<li><b>Optimal Level of Exotic Inheritance:</b>"
        "<br>&bull; The National Dairy Development Board (NDDB) and Department of Animal Husbandry & Dairying (DAHD) mandate maintaining <b>50% to 62.5% (maximum 75%)</b> exotic inheritance."
        "<br>&bull; Above 75% exotic inheritance: extreme susceptibility to heat stroke, tropical theileriosis, babesiosis, mastitis, and severe reproductive failure."
        "<br>&bull; Below 50%: milk production gains are insufficient to justify commercial stall-feeding costs.</li>"
        "<li><b>Inter-Se Mating in Crossbreds:</b>"
        "<br>&bull; Once the 50% or 62.5% crossbred level is achieved (e.g., F1 HF &times; Indigenous), crossbred bulls are mated to crossbred cows (<b>Inter-se mating</b>) accompanied by intense progeny testing to stabilize a synthetic breed (e.g., Frieswal).</li>"
        "</ul><br>"
        "<b>BREEDING STRATEGY FOR BUFFALOES (THE BLACK GOLD OF INDIA)</b><br>"
        "Buffaloes (<i>Bubalus bubalis</i>) contribute over 45% of India's total milk production, yielding richer milk (6.5–8.5% fat) with superior conversion of coarse crop residues:"
        "<ul>"
        "<li><b>Breeding Policy:</b>"
        "<br>1. <b>Grading Up of Non-descript Buffaloes:</b> Use purebred <b>Murrah</b> (in northern/central India) or <b>Surti/Jaffarabadi/Nili-Ravi/Mehsana</b> in regional tracts."
        "<br>2. <b>Selective Breeding in Defined Purebreds:</b> Intensive field progeny testing programs (Network Project on Buffalo Improvement - CIRB Hisar) to identify elite Murrah and Mehsana sires whose daughters yield > 3,000 kg milk per lactation."
        "<br>3. <b>Zero Crossbreeding:</b> Buffaloes are never crossbred with foreign species (no exotic river buffalo exists that outperforms Murrah/Nili-Ravi).</li>"
        "</ul>"
    ),
    "eliteDesc": (
        "<b>TOPPER ADVANCED MECHANISM & THEORETICAL NUANCES</b><br>"
        "<b>The Genetic Dilemma of Crossbred Inter-se Mating (F2 Breakdown):</b><br>"
        "In university exams, explain the biological hurdles in stabilizing tropical dairy crossbreds:"
        "<ul>"
        "<li>In F1 crossbreds (Exotic &times; Zebu), individual heterosis is 100%, masking recessive defects. Milk yield rises by 200–300% and age at first calving drops from 45 to 28 months.</li>"
        "<li>However, when F1 &times; F1 are mated inter-se, the <b>F2 generation suffers a 15–30% drop in milk yield</b>, wider phenotypic variance, and prolonged calving intervals due to: (a) 50% loss of individual heterosis, and (b) Recombination loss (shattering of favorable co-adapted gene complexes).</li>"
        "<li><b>The Solution:</b> Massive progeny testing of F1/inter-se crossbred bulls across thousands of field cows to identify sires with superior <b>Additive Genetic Breeding Values</b>, effectively replacing lost heterosis with permanent additive genetic gain.</li>"
        "</ul>"
    ),
    "keyPoints": [
        "India possesses the world's largest bovine population and leads global milk production.",
        "Indigenous cattle breeding policy mandates selective breeding within pure breeds (Gir, Sahiwal, Kankrej).",
        "Exotic crossbreeding is strictly restricted to non-descript, low-yielding scrub cows.",
        "Holstein-Friesian is used for crossbreeding in intensive plains; Jersey in hills and low-input areas.",
        "Optimal exotic inheritance level recommended for Indian conditions is 50% to 62.5% (never exceeding 75%).",
        "Exotic inheritance > 75% results in heat intolerance, tick susceptibility (theileriosis), and poor reproduction.",
        "Inter-se mating mates crossbreds to crossbreds (50% x 50%) to stabilize new synthetic strains.",
        "F2 crossbred generation suffers a 15–30% decline due to 50% loss of heterosis and recombination breakdown.",
        "Buffalo breeding policy relies 100% on selective breeding in pure breeds and grading up in non-descript scrub.",
        "Murrah is the premier dairy buffalo breed used nationwide for grading up non-descript buffaloes.",
        "Network Project on Buffalo Improvement (NPBI) and NDDB implement large-scale field progeny testing."
    ],
    "tables": [
        {
            "title": "National Breeding Policy Guidelines for Dairy Cattle and Buffaloes in India",
            "headers": ["Livestock Category", "Genetic Makeup", "Breeding Policy Mandate", "Target Sires / Germplasm", "Primary Performance Goal"],
            "rows": [
                ["Defined Indigenous Dairy Cattle", "Sahiwal, Gir, Red Sindhi, Rathi", "Selective Breeding (Purebreeding)", "Progeny tested / Pedigreed indigenous bulls", "305-day milk yield > 3,500 kg; preserve heat/tick tolerance"],
                ["Defined Dual-Purpose Cattle", "Hariana, Ongole, Kankrej, Tharparkar", "Selective Breeding for Milk + Draft", "Superior proven indigenous bulls", "Lactation yield 2,000–2,500 kg + strong draft bullocks"],
                ["Non-Descript Scrub Cattle", "Heterogeneous low-yielding indigenous", "Crossbreeding (up to 50–62.5% exotic)", "Jersey (hilly/rainfed) or HF (intensive irrigated)", "Lactation yield > 3,000 kg, age at first calving < 30 months"],
                ["Defined Dairy Buffaloes", "Murrah, Nili-Ravi, Mehsana, Jaffarabadi", "Selective Breeding in native tracts", "Progeny tested Murrah / Mehsana bulls", "Lactation yield > 2,800 kg with 7.0–8.0% fat"],
                ["Non-Descript Scrub Buffaloes", "Heterogeneous low-yielding buffaloes", "Grading Up across generations", "Pure Murrah semen / sires", "Convert to high-yielding Murrah-type (> 2,000 kg milk)"]
            ]
        }
    ],
    "clinical": (
        "<b>VETERINARY & FIELD BREEDING APPLICATION</b><br>"
        "In field artificial insemination camps, veterinarians frequently encounter crossbred cows with > 75% or 87.5% HF inheritance "
        "brought by farmers complaining of chronic panting (open-mouth breathing, salivation), heat stress anoestrus, recurrent mastitis, and fatal <i>Theileria annulata</i> attacks. "
        "The veterinarian must educate dairy farmers to practice <b>Rotational Backcrossing with Indigenous Sahiwal/Gir semen</b> or use <b>50% stabilized crossbred bulls</b> to pull exotic inheritance back to the physiologically resilient 50–62.5% zone."
    ),
    "tags": ["Dairy Cattle Breeding", "Buffalo Breeding", "Crossbreeding", "Murrah", "Sahiwal", "Gir", "Exotic Inheritance", "Frieswal", "Theileriosis"]
}
