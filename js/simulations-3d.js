/* ============================================================
   simulations-3d.js — True 3D Rotatable Cytogenetics & Molecular Engine
   Animal Genetics and Breeding Studio (100% Offline, Vanilla JS)
   ------------------------------------------------------------
   Registers 4 true 3D perspective-projected, depth-sorted,
   drag-to-rotate Canvas visualizers into window.simEngine:
     1. mitosis_meiosis_3d  — Mitosis vs Meiosis, Crossing-Over & Nondisjunction
     2. karyotype_3d        — Chromosome Morphology + Livestock/Poultry Karyotypes
     3. dna_molecular_3d    — 3D DNA Double Helix, Replication, Mutations & PCR/RFLP
     4. aberrations_3d      — Structural & Numerical Chromosomal Aberrations
   ============================================================ */

(function () {
  "use strict";
  if (!window.simEngine) return;

  /* ---- 3D Math & Perspective Projection Helpers ---- */
  function project3D(x, y, z, rotX, rotY, zoom, cx, cy) {
    var cosY = Math.cos(rotY), sinY = Math.sin(rotY);
    var x1 = x * cosY - z * sinY;
    var z1 = x * sinY + z * cosY;
    var cosX = Math.cos(rotX), sinX = Math.sin(rotX);
    var y2 = y * cosX - z1 * sinX;
    var z2 = y * sinX + z1 * cosX;
    var fov = 460 * (zoom || 1);
    var dist = 420;
    var scale = fov / Math.max(80, dist + z2);
    return { x: cx + x1 * scale, y: cy + y2 * scale, z: z2, s: scale };
  }

  function draw3DTube(ctx, p1, p2, radius, col, strokeCol) {
    var r = Math.max(2, radius * ((p1.s + p2.s) * 0.5));
    ctx.lineCap = "round";
    if (strokeCol) {
      ctx.strokeStyle = strokeCol;
      ctx.lineWidth = r * 2 + 2;
      ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
    }
    ctx.strokeStyle = col;
    ctx.lineWidth = r * 2;
    ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
  }

  function draw3DSphere(ctx, p, radius, col, borderCol) {
    var r = Math.max(2, radius * p.s);
    ctx.beginPath();
    ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
    ctx.fillStyle = col;
    ctx.fill();
    if (borderCol) {
      ctx.strokeStyle = borderCol;
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }
  }

  /* ============================================================
     1. 3D MITOSIS vs MEIOSIS, CROSSING-OVER & NONDISJUNCTION
     ============================================================ */
  window.simEngine.registerRenderer("mitosis_meiosis_3d", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var mode = st.params.division || "meiosis";
    var stage = Math.round(st.params.stage != null ? st.params.stage : st.step || 1);
    var nondisp = st.params.nondisj === "on";
    var cx = w * 0.5, cy = h * 0.52;

    // 3D Cell Membrane sphere wireframe
    ctx.save();
    ctx.strokeStyle = P.borderStrong;
    ctx.lineWidth = 1.5;
    for (var ring = 0; ring < 3; ring++) {
      ctx.beginPath();
      for (var a = 0; a <= 48; a++) {
        var ang = (a / 48) * Math.PI * 2;
        var rx = ring === 0 ? Math.cos(ang) * 145 : (ring === 1 ? Math.cos(ang) * 145 : 0);
        var ry = ring === 0 ? Math.sin(ang) * 115 : (ring === 1 ? 0 : Math.sin(ang) * 115);
        var rz = ring === 0 ? 0 : (ring === 1 ? Math.sin(ang) * 115 : Math.cos(ang) * 115);
        var pr = project3D(rx, ry, rz, st.rotX, st.rotY, st.zoom, cx, cy);
        if (a === 0) ctx.moveTo(pr.x, pr.y); else ctx.lineTo(pr.x, pr.y);
      }
      ctx.globalAlpha = 0.28;
      ctx.stroke();
    }
    ctx.restore();

    // Spindle poles
    var poleL = project3D(-135, 0, 0, st.rotX, st.rotY, st.zoom, cx, cy);
    var poleR = project3D(135, 0, 0, st.rotX, st.rotY, st.zoom, cx, cy);
    draw3DSphere(ctx, poleL, 7, P.amberFill, P.text);
    draw3DSphere(ctx, poleR, 7, P.amberFill, P.text);

    // Build 3D chromatid segments for 2 homologous pairs (Pair 1: Blue/Coral, Pair 2: Teal/Purple)
    var items = [];
    function addChromatid(x0, y0, z0, dx, dy, dz, col, colTip, crossed) {
      var pA = project3D(x0 - dx, y0 - dy, z0 - dz, st.rotX, st.rotY, st.zoom, cx, cy);
      var pC = project3D(x0, y0, z0, st.rotX, st.rotY, st.zoom, cx, cy);
      var pB = project3D(x0 + dx, y0 + dy, z0 + dz, st.rotX, st.rotY, st.zoom, cx, cy);
      items.push({ z: (pA.z + pC.z) / 2, draw: function () { draw3DTube(ctx, pA, pC, 5.5, col, P.surface); } });
      items.push({ z: (pB.z + pC.z) / 2, draw: function () { draw3DTube(ctx, pC, pB, 5.5, crossed ? colTip : col, P.surface); } });
      items.push({ z: pC.z - 2, draw: function () { draw3DSphere(ctx, pC, 5.5, P.amberFill, P.text); } });
    }

    var pulse = st.playing ? Math.sin(st.t * 2.2) * 6 : 0;

    if (mode === "meiosis") {
      if (stage === 0) {
        // Interphase / Replication
        addChromatid(-26, -34, 15, 0, 32, 0, P.blue, P.blue, false);
        addChromatid(-16, -34, 15, 0, 32, 0, P.blue, P.blue, false);
        addChromatid(26, -34, -15, 0, 32, 0, P.coral, P.coral, false);
        addChromatid(16, -34, -15, 0, 32, 0, P.coral, P.coral, false);
        addChromatid(-24, 38, -12, 0, 22, 0, P.teal, P.teal, false);
        addChromatid(24, 38, 12, 0, 22, 0, P.purple, P.purple, false);
      } else if (stage === 1) {
        // Prophase I: Synapsis & Chiasma Crossing-Over!
        addChromatid(-18, -32, 6, 0, 34, 0, P.blue, P.blue, false);
        addChromatid(-6, -32, 4, 8, 34, 0, P.blue, P.coral, true);
        addChromatid(6, -32, -4, -8, 34, 0, P.coral, P.blue, true);
        addChromatid(18, -32, -6, 0, 34, 0, P.coral, P.coral, false);
        // Second bivalent
        addChromatid(-10, 40, 8, 4, 24, 0, P.teal, P.purple, true);
        addChromatid(10, 40, -8, -4, 24, 0, P.purple, P.teal, true);
      } else if (stage === 2) {
        // Metaphase I: Bivalents at equator + spindle fibers
        var xOff = 18 + pulse * 0.4;
        addChromatid(-xOff, -34, 8, 0, 32, 0, P.blue, P.coral, true);
        addChromatid(xOff, -34, -8, 0, 32, 0, P.coral, P.blue, true);
        addChromatid(-xOff, 36, -8, 0, 24, 0, P.teal, P.purple, true);
        addChromatid(xOff, 36, 8, 0, 24, 0, P.purple, P.teal, true);
      } else if (stage === 3) {
        // Anaphase I: Homologs separate (or Nondisjunction!)
        var sep = 72 + pulse;
        var p1Right = nondisp ? sep : -sep;
        addChromatid(p1Right, -34, 10, 0, 30, 0, P.blue, P.coral, true);
        addChromatid(sep, -18, -10, 0, 30, 0, P.coral, P.blue, true);
        addChromatid(-sep, 36, -8, 0, 22, 0, P.teal, P.purple, true);
        addChromatid(sep, 36, 8, 0, 22, 0, P.purple, P.teal, true);
      } else {
        // Telophase II / 4 Haploid Gametes
        var gPos = [[-78, -48], [78, -48], [-78, 48], [78, 48]];
        var gCols = [[P.blue, P.teal], [P.blue, P.purple], [P.coral, P.teal], [P.coral, P.purple]];
        gPos.forEach(function (gp, idx) {
          var pG = project3D(gp[0], gp[1], 0, st.rotX, st.rotY, st.zoom, cx, cy);
          items.push({ z: pG.z + 20, draw: function () {
            ctx.beginPath(); ctx.arc(pG.x, pG.y, 38 * pG.s, 0, Math.PI * 2);
            ctx.strokeStyle = P.teal; ctx.lineWidth = 2; ctx.stroke();
          }});
          addChromatid(gp[0] - 8, gp[1], 0, 0, 18, 0, gCols[idx][0], gCols[idx][1], idx === 1 || idx === 2);
          if (!(nondisp && idx === 0)) {
            addChromatid(gp[0] + 8, gp[1], 0, 0, 14, 0, gCols[idx][1], gCols[idx][0], false);
          }
          if (nondisp && idx === 3) {
            addChromatid(gp[0] + 18, gp[1], 4, 0, 16, 0, P.blue, P.coral, true);
          }
        });
      }
    } else {
      // Mitosis: Sister chromatids align singly at equator and separate identically -> 2 diploid (2n) daughter cells
      var mSep = stage >= 3 ? 72 + pulse : (stage === 2 ? 4 : 18);
      addChromatid(-mSep, -42, 8, 0, 26, 0, P.blue, P.blue, false);
      addChromatid(mSep, -42, 8, 0, 26, 0, P.blue, P.blue, false);
      addChromatid(-mSep, -10, -8, 0, 26, 0, P.coral, P.coral, false);
      addChromatid(mSep, -10, -8, 0, 26, 0, P.coral, P.coral, false);
      addChromatid(-mSep, 26, 6, 0, 20, 0, P.teal, P.teal, false);
      addChromatid(mSep, 26, 6, 0, 20, 0, P.teal, P.teal, false);
      addChromatid(-mSep, 54, -6, 0, 20, 0, P.purple, P.purple, false);
      addChromatid(mSep, 54, -6, 0, 20, 0, P.purple, P.purple, false);
    }

    // Painter's algorithm Z-sort (back-to-front)
    items.sort(function (a, b) { return b.z - a.z; });
    items.forEach(function (it) { it.draw(); });

    var stageNames = mode === "meiosis"
      ? ["Interphase (S-Phase Replication)", "Prophase I (Synapsis & Chiasma Crossing-Over)", "Metaphase I (Bivalent Equator & Indep. Assortment)", "Anaphase I (Homolog Disjunction)", "Telophase II (4 Haploid Gametes)"]
      : ["Interphase (DNA Replication)", "Prophase (Condensation — No Synapsis)", "Metaphase (Single-File Equator)", "Anaphase (Sister Chromatid Separation)", "Telophase (2 Identical Diploid Cells)"];

    var insightText = mode === "meiosis"
      ? (nondisp
          ? "<b>NONDISJUNCTION ALERT!</b> Failure of homologous chromosomes to separate at Anaphase I produces aneuploid gametes: <b>n+1 (Trisomy upon fertilization, 2n+1)</b> and <b>n−1 (Monosomy, 2n−1)</b>!"
          : "<b>Meiosis (" + stageNames[stage] + "):</b> In Pachytene of Prophase I, non-sister chromatids form <b>Chiasmata</b> and exchange segments (Crossing-Over), generating genetic recombination. Reduction division (Meiosis I) halves chromosome number from <b>2n → n</b>.")
      : "<b>Mitosis (" + stageNames[stage] + "):</b> Equational division! Chromosomes line up singly at Metaphase (NO synapsis, NO crossing-over) and sister chromatids split to yield <b>2 genetically identical diploid (2n) daughter cells</b>.";

    return {
      readouts: [
        { label: "Division Type", value: mode === "meiosis" ? "Meiosis (Reductional)" : "Mitosis (Equational)", tone: "accent" },
        { label: "Current Stage", value: stageNames[stage].split(" ")[0], tone: "teal" },
        { label: "Daughter Cells", value: mode === "meiosis" ? (nondisp ? "4 Aneuploid (n±1)" : "4 Haploid (n)") : "2 Diploid (2n)", tone: nondisp ? "danger" : "ok" },
        { label: "Crossing-Over", value: mode === "meiosis" ? "Yes (Pachytene)" : "None", tone: "purple" }
      ],
      insight: insightText,
      formula: "Mitosis: 2n → 2 × (2n)   |   Meiosis: 2n → 4 × (n)   |   Crossing-Over = Pachytene (Prophase I)"
    };
  });

  /* ============================================================
     2. 3D CHROMOSOME MORPHOLOGY & LIVESTOCK KARYOTYPE EXPLORER
     ============================================================ */
  window.simEngine.registerRenderer("karyotype_3d", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var spKey = st.params.species || "cattle";
    var morph = st.params.morph || "metacentric";

    // 100% VCI-verified Livestock & Poultry Diploid Chromosome Numbers
    var speciesDB = {
      cattle:   { name: "Cattle (Bos taurus / B. indicus)", n2: 60, auto: "29 pairs (all acrocentric)", sex: "XX / XY (X submetacentric; Y submetacentric in B. taurus, acrocentric in B. indicus)" },
      rbuffalo: { name: "River Buffalo (Bubalus bubalis)", n2: 50, auto: "24 pairs (5 bi-armed + 19 acrocentric)", sex: "XX / XY (both acrocentric)" },
      sbuffalo: { name: "Swamp Buffalo", n2: 48, auto: "23 pairs (fusion of chr 4 & 9)", sex: "XX / XY" },
      sheep:    { name: "Sheep (Ovis aries)", n2: 54, auto: "26 pairs (3 large metacentric + 23 acrocentric)", sex: "XX / XY" },
      goat:     { name: "Goat (Capra hircus)", n2: 60, auto: "29 pairs (all acrocentric)", sex: "XX / XY (Y tiny metacentric)" },
      pig:      { name: "Pig (Sus scrofa)", n2: 38, auto: "18 pairs (12 bi-armed + 6 acrocentric)", sex: "XX / XY" },
      horse:    { name: "Horse (Equus caballus)", n2: 64, auto: "31 pairs (13 bi-armed + 18 acrocentric)", sex: "XX / XY (Donkey 2n=62, Mule 2n=63 sterile)" },
      dog:      { name: "Dog (Canis familiaris)", n2: 78, auto: "38 pairs (all acrocentric)", sex: "XX / XY (X large submetacentric)" },
      cat:      { name: "Cat (Felis catus)", n2: 38, auto: "18 pairs (mostly bi-armed)", sex: "XX / XY" },
      chicken:  { name: "Chicken (Gallus gallus)", n2: 78, auto: "38 pairs (macro + microchromosomes)", sex: "ZZ Male / ZW Female (Heterogametic Female!)" }
    };
    var sp = speciesDB[spKey] || speciesDB.cattle;

    // Centromere position ratio p/(p+q) for 3D chromosome
    var morphDB = {
      metacentric:    { p: 0.48, shape: "V-shaped at Anaphase", desc: "Centromere in middle (p ≈ q, arm ratio 1.0–1.7)" },
      submetacentric: { p: 0.30, shape: "L-shaped at Anaphase", desc: "Centromere sub-median (p < q, arm ratio 1.7–3.0)" },
      acrocentric:    { p: 0.14, shape: "J-shaped at Anaphase", desc: "Centromere near one end (all cattle & goat autosomes!)" },
      telocentric:    { p: 0.03, shape: "I-shaped (Rod)", desc: "Centromere at terminal tip (p-arm absent)" }
    };
    var mf = morphDB[morph] || morphDB.metacentric;

    // Left side: 3D Rotatable Sister-Chromatid Chromosome with G-Bands!
    var cx = w * 0.30, cy = h * 0.52;
    var totalLen = 190;
    var centY = -totalLen / 2 + totalLen * mf.p;
    var segs = [];

    [-14, 14].forEach(function (xOff) {
      for (var i = 0; i < 16; i++) {
        var y1 = -totalLen / 2 + (totalLen * i) / 16;
        var y2 = -totalLen / 2 + (totalLen * (i + 1)) / 16;
        // Pinch inward near centromere
        var d1 = Math.abs(y1 - centY), d2 = Math.abs(y2 - centY);
        var x1 = xOff * Math.min(1, 0.25 + d1 / 28);
        var x2 = xOff * Math.min(1, 0.25 + d2 / 28);
        var p1 = project3D(x1, y1, 0, st.rotX, st.rotY, st.zoom, cx, cy);
        var p2 = project3D(x2, y2, 0, st.rotX, st.rotY, st.zoom, cx, cy);
        var isDarkBand = (i % 3 === 1);
        var col = isDarkBand ? P.blueDark : P.blue;
        segs.push({ z: (p1.z + p2.z) / 2, draw: function () { draw3DTube(ctx, p1, p2, 8, col, null); } });
      }
    });
    var pCent = project3D(0, centY, 0, st.rotX, st.rotY, st.zoom, cx, cy);
    segs.push({ z: pCent.z - 5, draw: function () { draw3DSphere(ctx, pCent, 10, P.coral, P.surface); } });
    segs.sort(function (a, b) { return b.z - a.z; });
    segs.forEach(function (s) { s.draw(); });

    // Labels for p-arm, Centromere, q-arm
    ctx.fillStyle = P.text; ctx.font = "700 12px " + P.fontSans; ctx.textAlign = "left";
    ctx.fillText("p-arm (short)", cx + 44, Math.max(28, cy - totalLen * 0.35));
    ctx.fillStyle = P.coral;
    ctx.fillText("Centromere", cx + 44, pCent.y + 4);
    ctx.fillStyle = P.text;
    ctx.fillText("q-arm (long) + G-bands", cx + 44, Math.min(h - 24, cy + totalLen * 0.35));

    // Right side: Species Karyotype Comparison Bar Chart
    var rx0 = w * 0.54, rw = w * 0.42;
    ctx.fillStyle = P.text; ctx.font = "700 13px " + P.fontSans; ctx.textAlign = "left";
    ctx.fillText("Livestock & Poultry Diploid Numbers (2n)", rx0, 32);
    var keys = Object.keys(speciesDB);
    var rowH = (h - 56) / keys.length;
    keys.forEach(function (k, idx) {
      var item = speciesDB[k];
      var y = 44 + idx * rowH;
      var isSel = k === spKey;
      var barW = (item.n2 / 84) * (rw - 115);
      ctx.fillStyle = isSel ? P.coral : P.blueLight;
      env.roundRect(ctx, rx0 + 88, y + 3, barW, rowH - 8, 4); ctx.fill();
      ctx.fillStyle = isSel ? P.coral : P.textMuted;
      ctx.font = (isSel ? "700" : "600") + " 12px " + P.fontSans; ctx.textAlign = "right";
      ctx.fillText(item.name.split(" (")[0], rx0 + 82, y + rowH * 0.65);
      ctx.fillStyle = isSel ? P.coral : P.text;
      ctx.font = "700 12px " + P.fontMono; ctx.textAlign = "left";
      ctx.fillText("2n=" + item.n2, rx0 + 94 + barW, y + rowH * 0.65);
    });

    return {
      readouts: [
        { label: "Species Diploid (2n)", value: "2n = " + sp.n2, tone: "accent" },
        { label: "Haploid Gamete (n)", value: "n = " + (sp.n2 / 2), tone: "teal" },
        { label: "Morphology Shape", value: mf.shape, tone: "purple" },
        { label: "Sex Chromosomes", value: spKey === "chicken" ? "ZZ / ZW" : "XX / XY", tone: spKey === "chicken" ? "warn" : "ok" }
      ],
      insight: "<b>" + sp.name + " (2n = " + sp.n2 + "):</b> Autosomes: " + sp.auto + ". Sex chromosomes: <b>" + sp.sex + "</b>. Active 3D Morphology: <b>" + morph.toUpperCase() + "</b> — " + mf.desc + ".",
      formula: "Cattle & Goat: 2n=60 | River Buff: 2n=50 | Swamp Buff: 2n=48 | Sheep: 2n=54 | Horse: 2n=64 | Pig & Cat: 2n=38 | Dog & Chicken: 2n=78"
    };
  });

  /* ============================================================
     3. 3D DNA DOUBLE HELIX, REPLICATION, MUTATIONS & PCR/RFLP
     ============================================================ */
  window.simEngine.registerRenderer("dna_molecular_3d", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var mode = st.params.mode || env.cfg.defaultMode || "helix";

    if (mode === "pcr") {
      var cycles = Math.round(st.params.cycles != null ? st.params.cycles : 20);
      var copies = Math.pow(2, cycles);
      var pad = { l: 56, r: 28, t: 44, b: 54 };
      // Draw PCR Exponential Curve (left) + RFLP Agarose Gel Electrophoresis (right)
      var splitX = w * 0.56;
      ctx.fillStyle = P.text; ctx.font = "700 13px " + P.fontSans; ctx.textAlign = "left";
      ctx.fillText("PCR Amplification: 2ⁿ = 2^" + cycles + " Copies", 28, 28);
      ctx.fillText("RFLP Agarose Gel (Genotyping)", splitX + 18, 28);

      // Exponential bar chart
      var maxC = Math.min(30, Math.max(10, cycles));
      for (var c = 1; c <= maxC; c++) {
        var frac = Math.pow(2, c) / Math.pow(2, maxC);
        var bx = 28 + ((c - 1) / maxC) * (splitX - 54);
        var bw = Math.max(4, ((splitX - 54) / maxC) - 3);
        var bh = Math.max(4, frac * (h - 104));
        ctx.fillStyle = c === cycles ? P.coral : P.blue;
        ctx.fillRect(bx, h - 54 - bh, bw, bh);
      }
      ctx.fillStyle = P.textMuted; ctx.font = "600 12px " + P.fontMono; ctx.textAlign = "center";
      ctx.fillText("Denaturation 94°C → Annealing 55–65°C → Extension 72°C (Taq Pol)", splitX / 2, h - 22);

      // RFLP Gel Box (AA = 1 uncut band, AB = 3 bands, BB = 2 cut bands)
      var gx = splitX + 18, gy = 44, gw = w - splitX - 42, gh = h - 98;
      ctx.fillStyle = P.surface2;
      env.roundRect(ctx, gx, gy, gw, gh, 8); ctx.fill();
      ctx.strokeStyle = P.borderStrong; ctx.lineWidth = 1.5; ctx.stroke();

      var lanes = [
        { lbl: "Ladder", bands: [0.18, 0.35, 0.52, 0.72, 0.88], col: P.textMuted },
        { lbl: "AA", bands: [0.24], col: P.blue },
        { lbl: "AB", bands: [0.24, 0.56, 0.76], col: P.purple },
        { lbl: "BB", bands: [0.56, 0.76], col: P.teal }
      ];
      lanes.forEach(function (ln, idx) {
        var lx = gx + ((idx + 0.5) / lanes.length) * gw;
        ctx.fillStyle = P.textMuted; ctx.font = "700 12px " + P.fontMono; ctx.textAlign = "center";
        ctx.fillText(ln.lbl, lx, gy + gh + 18);
        ln.bands.forEach(function (pos) {
          ctx.fillStyle = ln.col;
          env.roundRect(ctx, lx - 18, gy + pos * gh, 36, 7, 3); ctx.fill();
        });
      });

      return {
        readouts: [
          { label: "PCR Cycles (n)", value: String(cycles), tone: "accent" },
          { label: "DNA Copies (2ⁿ)", value: copies >= 1e6 ? (copies / 1e6).toFixed(1) + "M" : copies.toLocaleString(), tone: "ok" },
          { label: "RFLP Heterozygote", value: "3 Bands (Codominant)", tone: "purple" }
        ],
        insight: "<b>PCR (Kary Mullis):</b> Amplifies a target gene exponentially (<b>2ⁿ</b> copies) using heat-stable <b>Taq DNA Polymerase</b>. <b>RFLP</b> is a <b>codominant</b> molecular marker: heterozygote <b>AB</b> shows all 3 bands (1 uncut + 2 cut fragments) on agarose gel!",
        formula: "PCR Yield = N₀ × 2ⁿ   |   Steps: Denaturation (94°C) → Annealing (55–65°C) → Extension (72°C)"
      };
    }

    // True 3D Rotatable DNA Double Helix (also animates Replication fork or Point Mutation!)
    var cx = w * 0.5, cy = h * 0.5;
    var mutType = st.params.mutation || "none";
    var pairs = [
      ["A", "T", 2], ["G", "C", 3], ["T", "A", 2], ["C", "G", 3],
      ["A", "T", 2], ["G", "C", 3], ["G", "C", 3], ["T", "A", 2],
      ["C", "G", 3], ["A", "T", 2], ["T", "A", 2], ["G", "C", 3]
    ];
    var drawList = [];
    var prevL = null, prevR = null;
    for (var i = 0; i < pairs.length; i++) {
      var y = -126 + i * 23;
      var ang = i * 0.56 + (st.playing ? st.t * 0.6 : 0);
      var rad = (mode === "replication" && i > 6) ? 62 + (i - 6) * 14 : 62;
      var xL = Math.cos(ang) * rad, zL = Math.sin(ang) * rad;
      var xR = -Math.cos(ang) * rad, zR = -Math.sin(ang) * rad;
      var pL = project3D(xL, y, zL, st.rotX, st.rotY, st.zoom, cx, cy);
      var pR = project3D(xR, y, zR, st.rotX, st.rotY, st.zoom, cx, cy);
      var isMut = (mode === "mutation" && mutType !== "none" && i === 5);

      (function (pA, pB, pLA, pRA, pair, mutFlag) {
        if (pLA) drawList.push({ z: (pA.z + pLA.z) / 2, draw: function () { draw3DTube(ctx, pLA, pA, 4.5, P.blue, null); } });
        if (pRA) drawList.push({ z: (pB.z + pRA.z) / 2, draw: function () { draw3DTube(ctx, pRA, pB, 4.5, P.teal, null); } });
        if (!(mode === "replication" && pair === null)) {
          drawList.push({ z: (pA.z + pB.z) / 2, draw: function () {
            ctx.strokeStyle = mutFlag ? P.danger : (pair[2] === 3 ? P.purple : P.amberFill);
            ctx.lineWidth = mutFlag ? 4 : 2.5;
            ctx.beginPath(); ctx.moveTo(pA.x, pA.y); ctx.lineTo(pB.x, pB.y); ctx.stroke();
            draw3DSphere(ctx, pA, mutFlag ? 8 : 6, mutFlag ? P.danger : P.blue, P.surface);
            draw3DSphere(ctx, pB, mutFlag ? 8 : 6, mutFlag ? P.danger : P.teal, P.surface);
          }});
        }
      })(pL, pR, prevL, prevR, (mode === "replication" && i > 6) ? null : pairs[i], isMut);
      prevL = pL; prevR = pR;
    }
    drawList.sort(function (a, b) { return b.z - a.z; });
    drawList.forEach(function (d) { d.draw(); });

    // Codon readout overlay
    var mutDesc = {
      none: "Normal B-DNA Double Helix (Watson-Crick): Antiparallel 5'→3' & 3'→5' strands, 10 bp/turn, 3.4 nm pitch, A=T (2 H-bonds), G≡C (3 H-bonds).",
      silent: "<b>Silent Mutation (GAA → GAG):</b> Base substitution produces the SAME amino acid (Glutamic acid) due to genetic code degeneracy.",
      missense: "<b>Missense Mutation (GAG → GUG):</b> Single base change alters the amino acid (Glu → Val), altering protein structure/function.",
      nonsense: "<b>Nonsense Mutation (CAG → UAG):</b> Converts an amino acid codon into a premature STOP codon (UAA, UAG, UGA), truncating the protein!",
      frameshift: "<b>Frameshift Mutation (+1/−1 bp indel):</b> Insertion or deletion not in multiples of 3 shifts the entire downstream reading frame!"
    };

    return {
      readouts: [
        { label: "Helix Geometry", value: "10 bp / turn (3.4 nm)", tone: "accent" },
        { label: "Base Pairing", value: "A=T (2H) · G≡C (3H)", tone: "purple" },
        { label: "Chargaff's Rule", value: "A=T, G=C (Pur=Pyr)", tone: "teal" },
        { label: "Active Mode", value: mode === "mutation" ? mutType.toUpperCase() : mode.toUpperCase(), tone: mode === "mutation" && mutType !== "none" ? "danger" : "ok" }
      ],
      insight: mode === "replication"
        ? "<b>Semi-Conservative Replication (Meselson & Stahl):</b> Helicase unwinds the fork; DNA Polymerase III synthesizes continuously on the <b>Leading Strand (5'→3')</b> and discontinuously as <b>Okazaki Fragments</b> on the Lagging Strand (joined by DNA Ligase)."
        : (mutDesc[mutType] || mutDesc.none),
      formula: "DNA →(Transcription)→ mRNA →(Translation)→ Protein   |   A + G = T + C"
    };
  });

  /* ============================================================
     4. 3D CHROMOSOMAL ABERRATIONS (Structural & Numerical)
     ============================================================ */
  window.simEngine.registerRenderer("aberrations_3d", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var ab = st.params.aberration || "robertsonian";
    var cx = w * 0.5, cy = h * 0.52;

    var info = {
      deletion:      { segs: ["A", "B", "D", "E"], cols: [P.blue, P.teal, P.amberFill, P.coral], desc: "<b>Deletion (Deficiency):</b> Loss of chromosomal segment <b>C</b>. Causes pseudodominance and severe developmental defects." },
      duplication:   { segs: ["A", "B", "C", "C", "D", "E"], cols: [P.blue, P.teal, P.purple, P.purple, P.amberFill, P.coral], desc: "<b>Duplication:</b> Repetition of segment <b>C</b> (e.g., unequal crossing-over). Important source of gene dosage increase." },
      inversion:     { segs: ["A", "D", "C", "B", "E"], cols: [P.blue, P.amberFill, P.purple, P.teal, P.coral], desc: "<b>Inversion (B-C-D flipped to D-C-B):</b> Paracentric (excludes centromere) vs Pericentric (includes centromere). Suppresses recovered recombinants." },
      translocation: { segs: ["A", "B", "C", "X", "Y"], cols: [P.blue, P.teal, P.purple, P.coral, P.coral], desc: "<b>Reciprocal Translocation:</b> Exchange of segments between non-homologous chromosomes; heterozygotes form a cross-shaped quadrivalent at pachytene." },
      robertsonian:  { segs: ["Chr 1", "CENT", "Chr 29"], cols: [P.blue, P.coral, P.teal], desc: "<b>Robertsonian Translocation 1/29 in Cattle (Centric Fusion):</b> Fusion of two acrocentric chromosomes (1 & 29) into one large submetacentric chromosome (2n drops 60 → 59), reducing fertility by ~5–10% due to unbalanced gametes!" },
      trisomy:       { segs: ["Copy 1", "Copy 2", "Extra +1"], cols: [P.blue, P.blue, P.danger], desc: "<b>Numerical Aberration — Trisomy (2n + 1):</b> One extra chromosome due to meiotic nondisjunction (e.g., XXY Klinefelter syndrome in bulls/rams/calico tomcats)." }
    };
    var cur = info[ab] || info.robertsonian;

    // Draw Normal Reference (left) and Aberrant 3D Chromosome (right)
    function drawSegmented3D(xBase, labels, cols, title) {
      var n = labels.length;
      var step = 170 / Math.max(3, n);
      var drawables = [];
      for (var i = 0; i < n; i++) {
        var y1 = -85 + i * step, y2 = y1 + step - 4;
        var p1 = project3D(xBase, y1, 0, st.rotX, st.rotY, st.zoom, cx, cy);
        var p2 = project3D(xBase, y2, 0, st.rotX, st.rotY, st.zoom, cx, cy);
        (function (pa, pb, col, lbl) {
          drawables.push({ z: (pa.z + pb.z) / 2, draw: function () {
            draw3DTube(ctx, pa, pb, 12, col, P.surface);
            ctx.fillStyle = P.textInvert; ctx.font = "700 12px " + P.fontMono;
            ctx.textAlign = "center"; ctx.textBaseline = "middle";
            ctx.fillText(lbl, (pa.x + pb.x) / 2, (pa.y + pb.y) / 2);
          }});
        })(p1, p2, cols[i], labels[i]);
      }
      drawables.sort(function (a, b) { return b.z - a.z; });
      drawables.forEach(function (d) { d.draw(); });
      var pTitle = project3D(xBase, -112, 0, st.rotX, st.rotY, st.zoom, cx, cy);
      ctx.fillStyle = P.text; ctx.font = "700 13px " + P.fontSans; ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
      ctx.fillText(title, pTitle.x, Math.max(24, pTitle.y));
    }

    drawSegmented3D(-95, ["A", "B", "C", "D", "E"], [P.blue, P.teal, P.purple, P.amberFill, P.coral], "Normal Reference");
    drawSegmented3D(95, cur.segs, cur.cols, "Aberration: " + ab.toUpperCase());

    return {
      readouts: [
        { label: "Aberration Class", value: ab === "trisomy" ? "Numerical (Aneuploidy)" : "Structural", tone: "danger" },
        { label: "Selected Type", value: ab.toUpperCase(), tone: "accent" },
        { label: "Veterinary Impact", value: ab === "robertsonian" ? "2n=59 Subfertility" : "Altered Dosage / Linkage", tone: "warn" }
      ],
      insight: cur.desc,
      formula: "Euploidy: 2n, 3n, 4n   |   Aneuploidy: 2n−1 (Monosomy), 2n+1 (Trisomy)   |   Rob(1;29) in Cattle: 2n = 59"
    };
  });
})();
