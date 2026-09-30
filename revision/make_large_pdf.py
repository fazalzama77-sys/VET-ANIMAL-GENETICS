"""Build LARGE-PRINT PDFs of the rapid-revision sheets.

The original sheets squeeze each unit onto 6 fixed A4 pages, which forces
the type down to ~7pt. This script instead lets the content flow naturally
across as many A4 pages as it needs, at comfortable reading size
(body ~12pt, tables ~11pt), and prints each unit to PDF with headless Chrome.

    python make_large_pdf.py
"""
import io, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "pdf")
SCALE = 1.0  # every font size is multiplied by this (8.75pt body -> ~12.2pt)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
UNITS = [
    ("unit1-rapid-revision.html", "AGB-Unit1-Biostatistics-LARGE.pdf"),
    ("unit2-rapid-revision.html", "AGB-Unit2-Genetics-LARGE.pdf"),
    ("unit3-rapid-revision.html", "AGB-Unit3-Breeding-LARGE.pdf"),
]


def scale_pt(text):
    return re.sub(r"font-size:\s*([\d.]+)pt",
                  lambda m: "font-size:%.1fpt" % (float(m.group(1)) * SCALE), text)


FLOW_CSS = """
/* ===== LARGE PRINT: free-flowing pages ===== */
@page{size:A4 portrait;margin:12mm 11mm 13mm;}
html,body{background:#fff !important;}
body{line-height:1.42 !important;}
.toolbar,.page-no,.page-foot{display:none !important;}
.page{width:auto !important;height:auto !important;min-height:0 !important;
  margin:0 0 5mm !important;padding:0 !important;box-shadow:none !important;
  overflow:visible !important;display:block !important;
  page-break-after:auto !important;break-after:auto !important;}
.pg{width:auto !important;transform:none !important;}
/* every unit block starts cleanly; keep small items whole */
.blk{margin-bottom:5mm;}
.g2,.g3,.row{margin-bottom:0 !important;margin-top:0 !important;}
.bh{break-after:avoid;page-break-after:avoid;}
tr,.fx,.call,.node,.map .m,.box,.skel .s,.rf p,.rf3 p,li{break-inside:avoid;page-break-inside:avoid;}
.map{grid-template-columns:repeat(3,1fr) !important;}
/* single full-width column: nothing gets squeezed or clipped */
.g2,.g3,.row{display:block !important;}
.g2>*,.g3>*,.row>*,.col{margin-bottom:5mm !important;width:auto !important;}
.row .col>.blk,.row>.col{margin-bottom:4mm;}
/* uniform comfortable sizes */
.pg,.pg *{font-size:11pt !important;line-height:1.45 !important;}
.pg sub,.pg sup{font-size:.7em !important;line-height:0 !important;}
.mh-t{font-size:18pt !important;line-height:1.2 !important;}
.mh-s,.mh-right{font-size:9.5pt !important;}
.runner .rn{font-size:15pt !important;}
.runner .rs{font-size:9pt !important;}
.bh,.bh *{font-size:12pt !important;}
table.t th{font-size:10.5pt !important;}
.fx,.fx *{font-size:11pt !important;}
.fx .lbl,.call .ct{font-size:10pt !important;}
.chip,.node small,.map .m span{font-size:9.5pt !important;}
.mark{font-size:14pt !important;width:36px !important;height:36px !important;}
.rf3{column-count:2 !important;}
.flow{flex-wrap:wrap;row-gap:4px;}
.masthead,.runner{break-after:avoid;}
.runner{margin-top:3mm;}
table.t td,table.t th{padding:3px 5px !important;}
.bb{padding:6px 8px !important;}
.fx{padding:3px 7px !important;margin:3px 0 !important;}
.call{padding:5px 8px !important;margin:4px 0 !important;}
.dash li,ul.t li,ol.t li{margin-bottom:3px !important;}
"""

os.makedirs(OUT, exist_ok=True)
css = scale_pt(io.open(os.path.join(HERE, "_revision.css"), encoding="utf-8").read())

for src, pdf in UNITS:
    html = io.open(os.path.join(HERE, src), encoding="utf-8").read()
    html = re.sub(r"<style>.*?</style>",
                  lambda m: "<style>\n" + css + FLOW_CSS + "\n</style>", html, count=1, flags=re.S)
    html = scale_pt(html)  # inline style="font-size:..pt" too
    html = html.replace("<title>", "<title>LARGE PRINT — ", 1)
    tmp = os.path.join(OUT, src.replace(".html", "-LARGE.html"))
    io.open(tmp, "w", encoding="utf-8").write(html)
    out = os.path.join(OUT, pdf)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + out, "file:///" + tmp.replace("\\", "/")],
                   check=True, capture_output=True)
    print("built", out)
