import os

css_path = os.path.join(os.path.dirname(__file__), "..", "assets", "css", "sections.css")
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

target = ".lesson__fig { margin-top: var(--s8); }\r\n.lesson__fig img { border-radius: var(--r-md); border: 1px solid var(--border); }"
if target not in content:
    target = ".lesson__fig { margin-top: var(--s8); }\n.lesson__fig img { border-radius: var(--r-md); border: 1px solid var(--border); }"

replacement = """/* ---------- lesson figure & scientific visual plate ---------- */
.lesson__fig {
  margin: var(--s8) 0 var(--s6);
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: var(--r-lg);
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.lesson__fig-media {
  position: relative;
  cursor: pointer;
  background: #020617;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.lesson__fig-media img {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.25s ease;
  border-radius: 0;
  border: none;
}

.lesson__fig-media:hover img {
  transform: scale(1.015);
}

.lesson__fig-zoom-hint {
  position: absolute;
  bottom: 12px;
  right: 12px;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  color: #38bdf8;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 20px;
  border: 1px solid rgba(56, 189, 248, 0.35);
  display: flex;
  align-items: center;
  gap: 6px;
  pointer-events: none;
  opacity: 0.9;
  transition: opacity 0.2s ease, transform 0.2s ease, background 0.2s ease;
}

.lesson__fig-media:hover .lesson__fig-zoom-hint {
  opacity: 1;
  transform: translateY(-2px);
  background: rgba(2, 132, 199, 0.95);
  color: #ffffff;
}

.lesson__figcaption {
  padding: var(--s4) var(--s5);
  background: var(--surface);
  border-top: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  gap: var(--s2);
}

.lesson__fig-caption-header {
  display: flex;
  align-items: center;
  gap: var(--s2);
}

.lesson__fig-caption-text {
  margin: 0;
  font-size: 0.92rem;
  color: var(--text);
  line-height: 1.5;
  font-weight: 500;
}

.lesson__fig-actions {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--s2);
  margin-top: 4px;
}

/* ---------- Image Lightbox Modal ---------- */
.img-modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 100000;
  background: rgba(15, 23, 42, 0.82);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 16px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.22s ease, visibility 0.22s ease;
}

.img-modal-overlay.open {
  display: flex !important;
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
}

.img-modal-dialog {
  background: var(--surface, #ffffff);
  color: var(--text, #0f172a);
  border: 1px solid var(--border-strong, #cbd5e1);
  border-radius: var(--r-xl, 16px);
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.55), 0 0 1px rgba(0, 0, 0, 0.2);
  width: min(960px, calc(100vw - 32px));
  max-height: 92vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
  z-index: 100001;
  margin: auto;
  transform: scale(0.95) translateY(12px);
  transition: transform 0.25s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.img-modal-overlay.open .img-modal-dialog {
  transform: scale(1) translateY(0);
}

.img-modal-head {
  padding: 14px 20px;
  border-bottom: 1px solid var(--border);
  background: var(--surface-2);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;
  position: relative;
}

.img-modal-title-wrap {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  padding-right: 40px;
}

.img-modal-title {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
}

.img-modal-close {
  position: absolute;
  top: 12px;
  right: 16px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1px solid var(--border);
  background: var(--surface);
  color: var(--text-muted);
  font-size: 1.25rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  transition: all 0.15s ease;
  line-height: 1;
}

.img-modal-close:hover {
  background: var(--surface-3, var(--border));
  color: var(--text);
  transform: scale(1.08);
}

.img-modal-body {
  padding: 16px 20px;
  overflow-y: auto;
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #020617;
}

.img-modal-media-wrap {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #020617;
  border-radius: var(--r-md);
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  min-height: 240px;
}

.img-modal-img {
  max-width: 100%;
  max-height: 60vh;
  object-fit: contain;
  display: block;
}

.img-modal-caption {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
  color: #cbd5e1;
  background: rgba(15, 23, 42, 0.85);
  padding: 10px 14px;
  border-radius: var(--r-md);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.img-modal-foot {
  padding: 12px 20px;
  border-top: 1px solid var(--border);
  background: var(--surface-2);
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  flex-shrink: 0;
}"""

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully replaced lesson figure styles in sections.css")
else:
    print("Target not found in sections.css")
