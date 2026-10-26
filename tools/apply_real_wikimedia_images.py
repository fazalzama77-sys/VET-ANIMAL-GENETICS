# -*- coding: utf-8 -*-
"""
Downloads all 79 verified Wikimedia Commons diagrams, graphs, and livestock photographs
locally into images/theory/, removes old placeholder SVGs, and updates both Theory (79 topics)
and Practical (25 topics) data files.
"""
import os
import re
import json
import time
import shutil
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, "images", "theory")
os.makedirs(IMAGES_DIR, exist_ok=True)

USER_AGENT = "VetGeneticsStudyApp/1.0 (https://github.com/fazalzama77-sys/VET-ANIMAL-GENETICS; personal educational use)"

PRACTICAL_TO_THEORY_MAP = {
    # Practical Unit 1
    "p1-t01": ("u1-t02", "Frequency Distribution & Histogram: Organizing raw livestock production records into class intervals."),
    "p1-t02": ("u1-t04", "Diagrammatic & Graphical Presentation: Histogram and frequency curve of continuous biological data."),
    "p1-t03": ("u1-t05", "Measures of Central Tendency: Geometric comparison of Mean, Median, and Mode."),
    "p1-t04": ("u1-t06", "Measures of Dispersion: Standard Deviation (σ) bands around the sample mean."),
    "p1-t05": ("u1-t11", "Standard Normal Distribution: Area under the normal curve within ±1σ, ±2σ, and ±3σ."),
    "p1-t06": ("u1-t13", "Correlation & Linear Regression: Least-squares regression line (Y = a + bX) fitted to experimental data."),
    "p1-t07": ("u1-t15", "Large Sample Z-Test: Critical rejection region and null hypothesis acceptance zone."),
    "p1-t08": ("u1-t16", "Student's t-Test: Probability density curves across degrees of freedom (ν) for small samples."),
    "p1-t09": ("u1-t17", "Chi-Square (χ²) Test: Distribution curves for Goodness of Fit and Contingency Table Independence."),
    "p1-t10": ("u1-t19", "Analysis of Variance (ANOVA): Snedecor's F-distribution for CRD and RBD experimental designs."),
    "p1-t11": ("u1-t22", "Spreadsheet Statistical Analysis: Tabular data entry, formula bar, and chart plotting."),
    # Practical Unit 2
    "p2-t01": ("u2-t04", "Monohybrid & Dihybrid Crosses: Mendelian segregation and independent assortment Punnett square."),
    "p2-t02": ("u2-t06", "Modified Mendelian Ratios & Epistasis: Non-allelic gene interaction modifying classical dihybrid ratios."),
    "p2-t03": ("u2-t11", "Linkage & Recombination Frequency: Homologous chiasma formation and crossing over."),
    "p2-t04": ("u2-t14", "Lymphocyte Culture & Karyotyping: G-banded metaphase chromosome idiogram."),
    "p2-t05": ("u2-t20", "Gene & Genotypic Frequencies: Allelic and genotypic distribution across a diploid locus."),
    "p2-t06": ("u2-t21", "Testing Hardy-Weinberg Equilibrium: Parabolic relationship of p², 2pq, and q² genotype frequencies."),
    "p2-t07": ("u2-t22", "Forces Changing Gene Frequency: Allele frequency trajectories under genetic drift and selection."),
    "p2-t08": ("u2-t27", "Heritability, Repeatability & Breeding Value: Parent-offspring regression and response to selection."),
    # Practical Unit 3
    "p3-t01": ("u3-t07", "Selection Differential (S) & Intensity (i): Truncation selection threshold in a normal population."),
    "p3-t02": ("u3-t04", "Expected Genetic Gain (ΔG): Directional shift of population mean under artificial selection."),
    "p3-t03": ("u2-t28", "EPA & MPPA Estimation: Repeatability and intraclass correlation across repeated lactation records."),
    "p3-t04": ("u3-t09", "Inbreeding Coefficient (F) & Relationship (R): Pedigree path analysis tracing common ancestors."),
    "p3-t05": ("u3-t12", "Heterosis (Hybrid Vigour) Percentage: F1 hybrid performance exceeding mid-parent average."),
    "p3-t06": ("u3-t17", "Sire Indices & Selection Index: Dairy sire progeny evaluation across contemporary groups.")
}

def get_ext(url):
    clean = url.split("?")[0].lower()
    if clean.endswith(".png"):
        return ".png"
    if clean.endswith(".jpg") or clean.endswith(".jpeg"):
        return ".jpg"
    if clean.endswith(".gif"):
        return ".gif"
    if clean.endswith(".svg"):
        return ".svg"
    return ".png"

def download_one(primary_tid, url):
    ext = get_ext(url)
    fname = f"{primary_tid}{ext}"
    fpath = os.path.join(IMAGES_DIR, fname)

    old_svg = os.path.join(IMAGES_DIR, f"{primary_tid}.svg")
    if ext != ".svg" and os.path.exists(old_svg):
        try:
            os.remove(old_svg)
        except OSError:
            pass

    if os.path.exists(fpath) and os.path.getsize(fpath) > 1500:
        return primary_tid, url, f"images/theory/{fname}", True

    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
            if len(data) > 500:
                with open(fpath, "wb") as f:
                    f.write(data)
                time.sleep(0.15)
                return primary_tid, url, f"images/theory/{fname}", True
        except Exception:
            time.sleep(0.8 * (attempt + 1))

    return primary_tid, url, url.split("?")[0], False

def main():
    verified_path = os.path.join(os.path.dirname(__file__), "verified_urls.json")
    with open(verified_path, "r", encoding="utf-8") as f:
        verified = json.load(f)

    url_to_tids = {}
    for tid, info in verified.items():
        url_to_tids.setdefault(info["url"], []).append(tid)

    print(f"Downloading {len(url_to_tids)} unique Wikimedia images for 79 topics...", flush=True)

    tid_to_local = {}
    with ThreadPoolExecutor(max_workers=3) as ex:
        futures = [ex.submit(download_one, tids[0], url) for url, tids in url_to_tids.items()]
        done_count = 0
        for fut in as_completed(futures):
            primary_tid, url, img_path, is_local = fut.result()
            done_count += 1
            if done_count % 15 == 0 or done_count == len(futures):
                print(f"Progress: {done_count}/{len(futures)} downloaded...", flush=True)
            tids = url_to_tids[url]
            tid_to_local[primary_tid] = (img_path, is_local)
            for other_tid in tids[1:]:
                ext = get_ext(url)
                old_svg = os.path.join(IMAGES_DIR, f"{other_tid}.svg")
                if ext != ".svg" and os.path.exists(old_svg):
                    try:
                        os.remove(old_svg)
                    except OSError:
                        pass
                if is_local:
                    src_file = os.path.join(BASE_DIR, img_path.replace("/", os.sep))
                    dst_fname = f"{other_tid}{ext}"
                    dst_file = os.path.join(IMAGES_DIR, dst_fname)
                    if src_file != dst_file:
                        shutil.copy2(src_file, dst_file)
                    tid_to_local[other_tid] = (f"images/theory/{dst_fname}", True)
                else:
                    tid_to_local[other_tid] = (img_path, False)

    local_count = sum(1 for _, (_, loc) in tid_to_local.items() if loc)
    print(f"Downloaded locally: {local_count} / {len(tid_to_local)}", flush=True)

    # Save mapping so Node script can update JS files cleanly
    all_updates = {
        "theory": {
            tid: {"img": tid_to_local[tid][0], "caption": info["caption"]}
            for tid, info in verified.items()
        },
        "practical": {
            ptid: {"img": tid_to_local[ref_tid][0], "caption": p_cap}
            for ptid, (ref_tid, p_cap) in PRACTICAL_TO_THEORY_MAP.items()
        }
    }
    map_out = os.path.join(os.path.dirname(__file__), "image_updates_map.json")
    with open(map_out, "w", encoding="utf-8") as f:
        json.dump(all_updates, f, indent=2, ensure_ascii=False)
    print("Saved image_updates_map.json!", flush=True)

if __name__ == "__main__":
    main()
