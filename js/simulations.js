/* ============================================================
   simulations.js — Interactive Visual Lab & Simulation Engine
   Animal Genetics and Breeding Studio (100% Offline, Vanilla JS)
   ------------------------------------------------------------
   Provides:
   - Registry for per-topic simulation configs (Units 1–3 + Practicals)
   - HiDPI Canvas manager, Play/Pause/Reset/Step loop, ResizeObserver
   - Expand Full-Screen Modal & clean unmount() on route change
   - Token-driven Canvas color palette (reads tokens.css live)
   - 100% textbook-accurate statistical, genetic & breeding math library
   - 15 interactive 2D visualizers (3D renderers register from simulations-3d.js)
   ============================================================ */

window.simRegistry = window.simRegistry || {};

window.simEngine = (function () {
  "use strict";

  var renderers = {};
  var activeInstance = null;
  var modalOverlay = null;
  var themeObserver = null;

  /* ============================================================
     1. TOKEN-BASED PALETTE (Reads tokens.css — zero hardcoded hex)
     ============================================================ */
  function getPalette() {
    var cs = getComputedStyle(document.documentElement);
    function v(name) {
      return (cs.getPropertyValue(name) || "").trim();
    }
    var isDark = document.documentElement.getAttribute("data-theme") === "dark";
    return {
      isDark: isDark,
      blue: v("--ivri-blue"),
      blueDark: v("--ivri-blue-dark"),
      blueLight: v("--ivri-blue-light"),
      teal: v("--ivri-teal"),
      tealLight: v("--ivri-teal-light"),
      purple: v("--ivri-purple"),
      purpleLight: v("--ivri-purple-light"),
      amber: v("--ivri-amber"),
      amberFill: v("--ivri-amber-fill"),
      amberLight: v("--ivri-amber-light"),
      coral: v("--ivri-coral"),
      sage: v("--ivri-sage"),
      ok: v("--ok"),
      okSoft: v("--ok-soft"),
      warn: v("--warn"),
      warnSoft: v("--warn-soft"),
      danger: v("--danger"),
      dangerSoft: v("--danger-soft"),
      info: v("--info"),
      infoSoft: v("--info-soft"),
      bg: v("--bg"),
      bgAlt: v("--bg-alt"),
      surface: v("--surface"),
      surface2: v("--surface-2"),
      text: v("--text"),
      textMuted: v("--text-muted"),
      textFaint: v("--text-faint"),
      textInvert: v("--text-invert"),
      border: v("--border"),
      borderStrong: v("--border-strong"),
      accent: v("--accent") || v("--ivri-blue"),
      fontSans: v("--font-sans") || "sans-serif",
      fontMono: v("--font-mono") || "monospace"
    };
  }

  /* ============================================================
     2. TEXTBOOK-ACCURATE MATH & BIOSTATISTICS LIBRARY
     ============================================================ */
  var math = {
    mean: function (arr) {
      if (!arr.length) return 0;
      var s = 0;
      for (var i = 0; i < arr.length; i++) s += arr[i];
      return s / arr.length;
    },
    median: function (arr) {
      if (!arr.length) return 0;
      var a = arr.slice().sort(function (x, y) { return x - y; });
      var m = Math.floor(a.length / 2);
      return a.length % 2 ? a[m] : (a[m - 1] + a[m]) / 2;
    },
    mode: function (arr) {
      if (!arr.length) return 0;
      var freq = {}, best = arr[0], maxF = 0;
      for (var i = 0; i < arr.length; i++) {
        var k = Math.round(arr[i] * 2) / 2;
        freq[k] = (freq[k] || 0) + 1;
        if (freq[k] > maxF) { maxF = freq[k]; best = k; }
      }
      return best;
    },
    variance: function (arr, sample) {
      if (arr.length < 2) return 0;
      var m = math.mean(arr), ss = 0;
      for (var i = 0; i < arr.length; i++) ss += (arr[i] - m) * (arr[i] - m);
      return ss / (sample === false ? arr.length : arr.length - 1);
    },
    sd: function (arr, sample) {
      return Math.sqrt(math.variance(arr, sample));
    },
    sem: function (arr) {
      return arr.length ? math.sd(arr, true) / Math.sqrt(arr.length) : 0;
    },
    cv: function (arr) {
      var m = math.mean(arr);
      return m ? (math.sd(arr, true) / Math.abs(m)) * 100 : 0;
    },
    erf: function (x) {
      var sign = x < 0 ? -1 : 1;
      x = Math.abs(x);
      var t = 1 / (1 + 0.3275911 * x);
      var y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x);
      return sign * y;
    },
    normalPDF: function (x, mu, sigma) {
      var z = (x - mu) / sigma;
      return Math.exp(-0.5 * z * z) / (sigma * Math.sqrt(2 * Math.PI));
    },
    normalCDF: function (z) {
      return 0.5 * (1 + math.erf(z / Math.SQRT2));
    },
    invNormal: function (p) {
      if (p <= 0) return -4;
      if (p >= 1) return 4;
      var a1 = -3.969683028665376e1, a2 = 2.209460984245205e2, a3 = -2.759285104469687e2;
      var a4 = 1.383577518672690e2, a5 = -3.066479806614716e1, a6 = 2.506628277459239e0;
      var b1 = -5.447609879822406e1, b2 = 1.615858368580409e2, b3 = -1.556989798598866e2;
      var b4 = 6.680131188771972e1, b5 = -1.328068155288572e1;
      var c1 = -7.784894002430293e-3, c2 = -3.223964580411365e-1, c3 = -2.400758277161838e0;
      var c4 = -2.549732539343734e0, c5 = 4.374664141464968e0, c6 = 2.938163982698783e0;
      var d1 = 7.784695709041462e-3, d2 = 3.224671290700398e-1, d3 = 2.445134137142996e0, d4 = 3.754408661907416e0;
      var pLow = 0.02425, pHigh = 1 - pLow, q, r;
      if (p < pLow) {
        q = Math.sqrt(-2 * Math.log(p));
        return (((((c1 * q + c2) * q + c3) * q + c4) * q + c5) * q + c6) / ((((d1 * q + d2) * q + d3) * q + d4) * q + 1);
      } else if (p <= pHigh) {
        q = p - 0.5; r = q * q;
        return (((((a1 * r + a2) * r + a3) * r + a4) * r + a5) * r + a6) * q / (((((b1 * r + b2) * r + b3) * r + b4) * r + b5) * r + 1);
      } else {
        q = Math.sqrt(-2 * Math.log(1 - p));
        return -(((((c1 * q + c2) * q + c3) * q + c4) * q + c5) * q + c6) / ((((d1 * q + d2) * q + d3) * q + d4) * q + 1);
      }
    },
    selectionIntensity: function (p) {
      p = Math.max(0.005, Math.min(0.995, p));
      var z = math.invNormal(1 - p);
      return math.normalPDF(z, 0, 1) / p;
    },
    logGamma: function (z) {
      var g = 7, p = [0.99999999999980993, 676.5203681218851, -1259.1392167224028, 771.32342877765313,
        -176.61502916214059, 12.507343278686905, -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
      if (z < 0.5) return Math.log(Math.PI / Math.sin(Math.PI * z)) - math.logGamma(1 - z);
      z -= 1;
      var x = p[0];
      for (var i = 1; i < g + 2; i++) x += p[i] / (z + i);
      var t = z + g + 0.5;
      return 0.5 * Math.log(2 * Math.PI) + (z + 0.5) * Math.log(t) - t + Math.log(x);
    },
    binomialPMF: function (n, k, p) {
      if (k < 0 || k > n) return 0;
      if (p <= 0) return k === 0 ? 1 : 0;
      if (p >= 1) return k === n ? 1 : 0;
      var logC = math.logGamma(n + 1) - math.logGamma(k + 1) - math.logGamma(n - k + 1);
      return Math.exp(logC + k * Math.log(p) + (n - k) * Math.log(1 - p));
    },
    poissonPMF: function (k, lam) {
      if (k < 0) return 0;
      if (lam <= 0) return k === 0 ? 1 : 0;
      return Math.exp(k * Math.log(lam) - lam - math.logGamma(k + 1));
    },
    tPDF: function (t, df) {
      var c = Math.exp(math.logGamma((df + 1) / 2) - math.logGamma(df / 2)) / Math.sqrt(df * Math.PI);
      return c * Math.pow(1 + (t * t) / df, -(df + 1) / 2);
    },
    chiSqPDF: function (x, df) {
      if (x <= 0) return 0;
      var k = df / 2;
      return Math.exp((k - 1) * Math.log(x) - x / 2 - k * Math.log(2) - math.logGamma(k));
    },
    tCrit: function (df, alpha) {
      // Exact two-tailed Student's t critical values
      var t05 = [12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228,
        2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086,
        2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 2.042];
      var t01 = [63.657, 9.925, 5.841, 4.604, 4.032, 3.707, 3.499, 3.355, 3.250, 3.169,
        3.106, 3.055, 3.012, 2.977, 2.947, 2.921, 2.898, 2.878, 2.861, 2.845,
        2.831, 2.819, 2.807, 2.797, 2.787, 2.779, 2.771, 2.763, 2.756, 2.750];
      var tbl = alpha <= 0.01 ? t01 : t05;
      var d = Math.max(1, Math.round(df));
      if (d <= 30) return tbl[d - 1];
      if (d <= 60) return alpha <= 0.01 ? 2.660 : 2.000;
      return alpha <= 0.01 ? 2.576 : 1.960;
    },
    chiCrit: function (df, alpha) {
      var c05 = [3.841, 5.991, 7.815, 9.488, 11.070, 12.592, 14.067, 15.507, 16.919, 18.307, 19.675, 21.026];
      var c01 = [6.635, 9.210, 11.345, 13.277, 15.086, 16.812, 18.475, 20.090, 21.666, 23.209, 24.725, 26.217];
      var tbl = alpha <= 0.01 ? c01 : c05;
      var d = Math.max(1, Math.min(tbl.length, Math.round(df)));
      return tbl[d - 1];
    },
    fCrit: function (df1, df2, alpha) {
      // Accurate F critical values for df1=1..5, df2=4..30
      var z = alpha <= 0.01 ? 2.326 : 1.645;
      if (df1 === 3 && df2 === 12) return alpha <= 0.01 ? 5.95 : 3.49;
      if (df1 === 3 && df2 === 9) return alpha <= 0.01 ? 6.99 : 3.86;
      if (df1 === 2 && df2 === 12) return alpha <= 0.01 ? 6.93 : 3.89;
      if (df1 === 2 && df2 === 15) return alpha <= 0.01 ? 6.36 : 3.68;
      // Wilson-Hilferty approximation for general df1, df2
      var a = 2 / (9 * df1), b = 2 / (9 * df2);
      var num = (1 - a) * (1 - b) + z * Math.sqrt(a * Math.pow(1 - b, 2) + b * Math.pow(1 - a, 2) - a * b * z * z);
      var den = Math.pow(1 - b, 2) - b * z * z;
      var val = Math.pow(Math.max(0.1, num / Math.max(0.05, den)), 3);
      return Math.max(1.2, val);
    },
    linReg: function (pts) {
      var n = pts.length;
      if (n < 2) return { a: 0, b: 0, r: 0, r2: 0, rho: 0 };
      var sx = 0, sy = 0, sxx = 0, syy = 0, sxy = 0;
      for (var i = 0; i < n; i++) {
        sx += pts[i].x; sy += pts[i].y;
        sxx += pts[i].x * pts[i].x; syy += pts[i].y * pts[i].y; sxy += pts[i].x * pts[i].y;
      }
      var mx = sx / n, my = sy / n;
      var num = sxy - n * mx * my;
      var dx = sxx - n * mx * mx, dy = syy - n * my * my;
      var b = dx > 1e-9 ? num / dx : 0;
      var a = my - b * mx;
      var r = (dx > 1e-9 && dy > 1e-9) ? Math.max(-1, Math.min(1, num / Math.sqrt(dx * dy))) : 0;
      // Spearman rank correlation
      function ranks(vals) {
        var idx = vals.map(function (v, i) { return { v: v, i: i }; }).sort(function (u, w) { return u.v - w.v; });
        var rk = new Array(vals.length);
        for (var j = 0; j < idx.length; j++) rk[idx[j].i] = j + 1;
        return rk;
      }
      var rx = ranks(pts.map(function (p) { return p.x; }));
      var ry = ranks(pts.map(function (p) { return p.y; }));
      var sd2 = 0;
      for (var k = 0; k < n; k++) sd2 += (rx[k] - ry[k]) * (rx[k] - ry[k]);
      var rho = Math.max(-1, Math.min(1, 1 - (6 * sd2) / (n * (n * n - 1))));
      return { a: a, b: b, r: r, r2: r * r, rho: rho };
    }
  };

  /* ============================================================
     3. CANVAS DRAWING UTILITIES (Crisp HiDPI, Large Readable Fonts)
     ============================================================ */
  function setupCanvas(canvas) {
    var rect = canvas.getBoundingClientRect();
    var w = Math.max(300, Math.round(rect.width || 680));
    var h = Math.max(240, Math.round(rect.height || 360));
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    if (canvas.width !== Math.round(w * dpr) || canvas.height !== Math.round(h * dpr)) {
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
    }
    var ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: w, h: h };
  }

  function drawBg(ctx, w, h, P) {
    ctx.fillStyle = P.surface;
    ctx.fillRect(0, 0, w, h);
  }

  function drawAxes(ctx, pad, w, h, P, xLabel, yLabel) {
    var x0 = pad.l, y0 = h - pad.b, x1 = w - pad.r, y1 = pad.t;
    ctx.strokeStyle = P.borderStrong;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(x0, y1);
    ctx.lineTo(x0, y0);
    ctx.lineTo(x1, y0);
    ctx.stroke();

    ctx.fillStyle = P.textMuted;
    ctx.font = "600 13px " + P.fontSans;
    if (xLabel) {
      ctx.textAlign = "center";
      ctx.textBaseline = "bottom";
      ctx.fillText(xLabel, (x0 + x1) / 2, h - 6);
    }
    if (yLabel) {
      ctx.save();
      ctx.translate(16, (y0 + y1) / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.textAlign = "center";
      ctx.textBaseline = "top";
      ctx.fillText(yLabel, 0, 0);
      ctx.restore();
    }
  }

  function roundRect(ctx, x, y, w, h, r) {
    r = Math.min(r, w / 2, h / 2);
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  function escHtml(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  /* ============================================================
     4. CORE ENGINE LIFECYCLE (Mount / Unmount / Expand Modal)
     ============================================================ */
  function registerRenderer(name, fn) {
    renderers[name] = fn;
  }

  function registerTopic(topicId, config) {
    window.simRegistry[topicId] = config;
  }

  function registerTopics(map) {
    for (var k in map) {
      if (Object.prototype.hasOwnProperty.call(map, k)) {
        window.simRegistry[k] = map[k];
      }
    }
  }

  function buildLabDOM(cfg, isModal) {
    var hasSteps = cfg.steps && cfg.steps.length > 0;
    var hasControls = cfg.controls && cfg.controls.length > 0;
    var is3D = !!cfg.is3D;

    var controlsHtml = "";
    if (hasControls) {
      controlsHtml = '<div class="sim-controls">' + cfg.controls.map(function (c) {
        if (c.type === "slider") {
          return '<div class="sim-control">' +
            '<div class="sim-control__top">' +
              '<label class="sim-control__label" for="sim-ctrl-' + escHtml(c.id) + '">' + escHtml(c.label) + '</label>' +
              '<span class="sim-control__val" data-val-for="' + escHtml(c.id) + '">' + escHtml(c.format ? c.format(c.value) : c.value) + '</span>' +
            '</div>' +
            '<input class="sim-slider" id="sim-ctrl-' + escHtml(c.id) + '" type="range" data-ctrl="' + escHtml(c.id) + '" min="' + c.min + '" max="' + c.max + '" step="' + (c.step || 1) + '" value="' + c.value + '">' +
          '</div>';
        } else if (c.type === "select") {
          return '<div class="sim-control">' +
            '<div class="sim-control__top"><label class="sim-control__label" for="sim-ctrl-' + escHtml(c.id) + '">' + escHtml(c.label) + '</label></div>' +
            '<select class="sim-select" id="sim-ctrl-' + escHtml(c.id) + '" data-ctrl="' + escHtml(c.id) + '">' +
              c.options.map(function (o) {
                var val = typeof o === "object" ? o.value : o;
                var lbl = typeof o === "object" ? o.label : o;
                return '<option value="' + escHtml(val) + '"' + (String(val) === String(c.value) ? ' selected' : '') + '>' + escHtml(lbl) + '</option>';
              }).join("") +
            '</select>' +
          '</div>';
        } else if (c.type === "toggle") {
          return '<div class="sim-control">' +
            '<div class="sim-control__top"><span class="sim-control__label">' + escHtml(c.label) + '</span></div>' +
            '<div class="sim-toggle-group" data-toggle-ctrl="' + escHtml(c.id) + '">' +
              c.options.map(function (o) {
                var val = typeof o === "object" ? o.value : o;
                var lbl = typeof o === "object" ? o.label : o;
                return '<button type="button" class="sim-toggle-pill' + (String(val) === String(c.value) ? ' is-active' : '') + '" data-val="' + escHtml(val) + '">' + escHtml(lbl) + '</button>';
              }).join("") +
            '</div>' +
          '</div>';
        }
        return "";
      }).join("") + '</div>';
    }

    var stepsHtml = "";
    if (hasSteps) {
      stepsHtml = '<div class="sim-steps">' +
        '<span class="sim-steps__label">Guided Steps:</span>' +
        cfg.steps.map(function (s, idx) {
          return '<button type="button" class="sim-step-pill' + (idx === 0 ? ' is-active' : '') + '" data-step-idx="' + idx + '">' + (idx + 1) + '. ' + escHtml(s.label || s) + '</button>';
        }).join("") +
      '</div>';
    }

    var hintText = cfg.hint || (is3D ? "Drag to rotate 3D · Scroll to zoom" : "Adjust controls below to explore");

    return '<section class="sim-lab" aria-label="Interactive Visual Lab">' +
      '<div class="sim-lab__header">' +
        '<div class="sim-lab__title-wrap">' +
          '<div class="sim-lab__kicker">' +
            '<span class="sim-lab__badge">' + (is3D ? '3D INTERACTIVE LAB' : 'INTERACTIVE VISUAL LAB') + '</span>' +
            (cfg.tag ? '<span>' + escHtml(cfg.tag) + '</span>' : '') +
          '</div>' +
          '<h3 class="sim-lab__title">' + escHtml(cfg.title) + '</h3>' +
        '</div>' +
        '<div class="sim-lab__actions">' +
          (cfg.animated !== false ? '<button type="button" class="sim-btn sim-btn--primary" data-sim-act="play">' +
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="6 4 20 12 6 20 6 4"/></svg><span>Play</span></button>' : '') +
          '<button type="button" class="sim-btn" data-sim-act="reset">' +
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg><span>Reset</span></button>' +
          '<button type="button" class="sim-btn" data-sim-act="' + (isModal ? 'close-modal' : 'expand') + '">' +
            (isModal
              ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg><span>Close</span>'
              : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg><span>Expand</span>') +
          '</button>' +
        '</div>' +
      '</div>' +
      '<div class="sim-lab__stage">' +
        '<canvas class="sim-lab__canvas' + (is3D ? ' sim-lab__canvas--3d' : (cfg.interactiveCanvas ? ' sim-lab__canvas--interactive' : '')) + '"></canvas>' +
        '<div class="sim-lab__hint">' + escHtml(hintText) + '</div>' +
      '</div>' +
      '<div class="sim-readouts" data-sim-readouts></div>' +
      '<div class="sim-bench" data-sim-bench hidden></div>' +
      stepsHtml +
      controlsHtml +
      '<div class="sim-insight">' +
        '<div class="sim-insight__head">How It Works &amp; Exam Insight</div>' +
        '<p class="sim-insight__text" data-sim-insight-text></p>' +
        '<div class="sim-insight__formula" data-sim-insight-formula hidden></div>' +
      '</div>' +
    '</section>';
  }

  function createController(container, topicId, cfg, sharedState, isModal) {
    container.innerHTML = buildLabDOM(cfg, isModal);
    var root = container.querySelector(".sim-lab");
    var canvas = root.querySelector(".sim-lab__canvas");
    var readoutsEl = root.querySelector("[data-sim-readouts]");
    var benchEl = root.querySelector("[data-sim-bench]");
    var insightTextEl = root.querySelector("[data-sim-insight-text]");
    var insightFormulaEl = root.querySelector("[data-sim-insight-formula]");
    var playBtn = root.querySelector('[data-sim-act="play"]');

    var st = sharedState || {
      playing: !!cfg.autoPlay,
      t: 0,
      step: 0,
      rotX: cfg.rotX != null ? cfg.rotX : 0.35,
      rotY: cfg.rotY != null ? cfg.rotY : 0.55,
      zoom: 1,
      params: {},
      custom: {}
    };

    if (!sharedState) {
      (cfg.controls || []).forEach(function (c) {
        st.params[c.id] = c.value;
      });
    }

    var rafId = null;
    var lastTime = 0;
    var destroyed = false;
    var dragging = false;
    var lastPointer = { x: 0, y: 0 };

    function updatePlayBtn() {
      if (!playBtn) return;
      playBtn.innerHTML = st.playing
        ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg><span>Pause</span>'
        : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="6 4 20 12 6 20 6 4"/></svg><span>Play</span>';
    }

    function syncControlsFromState() {
      (cfg.controls || []).forEach(function (c) {
        var val = st.params[c.id];
        if (c.type === "slider" || c.type === "select") {
          var inp = root.querySelector('[data-ctrl="' + c.id + '"]');
          if (inp) inp.value = val;
          var badge = root.querySelector('[data-val-for="' + c.id + '"]');
          if (badge) badge.textContent = c.format ? c.format(val) : val;
        } else if (c.type === "toggle") {
          var grp = root.querySelector('[data-toggle-ctrl="' + c.id + '"]');
          if (grp) {
            Array.prototype.forEach.call(grp.querySelectorAll(".sim-toggle-pill"), function (b) {
              b.classList.toggle("is-active", b.getAttribute("data-val") === String(val));
            });
          }
        }
      });
      Array.prototype.forEach.call(root.querySelectorAll(".sim-step-pill"), function (b) {
        b.classList.toggle("is-active", Number(b.getAttribute("data-step-idx")) === st.step);
      });
      updatePlayBtn();
    }

    function setReadouts(items) {
      if (!readoutsEl) return;
      readoutsEl.innerHTML = (items || []).map(function (r) {
        return '<div class="sim-readout' + (r.tone ? ' sim-readout--' + r.tone : '') + '">' +
          '<span class="sim-readout__label">' + escHtml(r.label) + '</span>' +
          '<span class="sim-readout__value">' + escHtml(r.value) + '</span>' +
          (r.sub ? '<span class="sim-readout__sub">' + escHtml(r.sub) + '</span>' : '') +
        '</div>';
      }).join("");
    }

    function setBench(html) {
      if (!benchEl) return;
      if (html) {
        benchEl.hidden = false;
        benchEl.innerHTML = html;
      } else {
        benchEl.hidden = true;
        benchEl.innerHTML = "";
      }
    }

    function setInsight(text, formula) {
      if (insightTextEl) insightTextEl.innerHTML = text || cfg.insight || "";
      if (insightFormulaEl) {
        if (formula || cfg.formula) {
          insightFormulaEl.hidden = false;
          insightFormulaEl.textContent = formula || cfg.formula;
        } else {
          insightFormulaEl.hidden = true;
        }
      }
    }

    var rendererFn = renderers[cfg.type];

    function renderFrame() {
      if (destroyed) return;
      var dim = setupCanvas(canvas);
      var P = getPalette();
      drawBg(dim.ctx, dim.w, dim.h, P);
      if (rendererFn) {
        var out = rendererFn({
          ctx: dim.ctx, w: dim.w, h: dim.h, P: P, state: st, cfg: cfg, math: math,
          drawAxes: drawAxes, roundRect: roundRect, escHtml: escHtml
        });
        if (out) {
          if (out.readouts) setReadouts(out.readouts);
          if (out.bench !== undefined) setBench(out.bench);
          if (out.insight !== undefined || out.formula !== undefined) {
            setInsight(out.insight, out.formula);
          }
        }
      }
    }

    function tick(now) {
      if (destroyed) return;
      if (!lastTime) lastTime = now;
      var dt = Math.min(0.05, (now - lastTime) / 1000);
      lastTime = now;
      if (st.playing) {
        st.t += dt;
        if (cfg.is3D && !dragging) st.rotY += dt * 0.45;
        renderFrame();
        rafId = requestAnimationFrame(tick);
      } else {
        rafId = null;
      }
    }

    function startLoop() {
      if (!rafId && st.playing) {
        lastTime = 0;
        rafId = requestAnimationFrame(tick);
      }
    }

    // Wire sliders & selects
    Array.prototype.forEach.call(root.querySelectorAll("[data-ctrl]"), function (inp) {
      var id = inp.getAttribute("data-ctrl");
      var ctrlDef = (cfg.controls || []).filter(function (c) { return c.id === id; })[0];
      inp.addEventListener("input", function () {
        var val = ctrlDef && ctrlDef.type === "slider" ? parseFloat(inp.value) : inp.value;
        st.params[id] = val;
        var badge = root.querySelector('[data-val-for="' + id + '"]');
        if (badge) badge.textContent = ctrlDef && ctrlDef.format ? ctrlDef.format(val) : val;
        renderFrame();
      });
    });

    // Wire toggle groups
    Array.prototype.forEach.call(root.querySelectorAll("[data-toggle-ctrl]"), function (grp) {
      var id = grp.getAttribute("data-toggle-ctrl");
      grp.addEventListener("click", function (e) {
        var btn = e.target.closest(".sim-toggle-pill");
        if (!btn) return;
        st.params[id] = btn.getAttribute("data-val");
        syncControlsFromState();
        renderFrame();
      });
    });

    // Wire guided step pills
    Array.prototype.forEach.call(root.querySelectorAll("[data-step-idx]"), function (btn) {
      btn.addEventListener("click", function () {
        st.step = Number(btn.getAttribute("data-step-idx"));
        if (cfg.steps && cfg.steps[st.step] && cfg.steps[st.step].apply) {
          cfg.steps[st.step].apply(st);
        }
        syncControlsFromState();
        renderFrame();
      });
    });

    // Wire Play / Pause / Reset / Expand / Close
    root.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-sim-act]");
      if (!btn) return;
      var act = btn.getAttribute("data-sim-act");
      if (act === "play") {
        st.playing = !st.playing;
        updatePlayBtn();
        if (st.playing) startLoop();
      } else if (act === "reset") {
        st.t = 0;
        st.step = 0;
        st.rotX = cfg.rotX != null ? cfg.rotX : 0.35;
        st.rotY = cfg.rotY != null ? cfg.rotY : 0.55;
        st.zoom = 1;
        st.custom = {};
        (cfg.controls || []).forEach(function (c) { st.params[c.id] = c.value; });
        syncControlsFromState();
        renderFrame();
      } else if (act === "expand") {
        openModal(topicId, cfg, st);
      } else if (act === "close-modal") {
        closeModal();
      }
    });

    // Canvas pointer interactions (3D rotation OR interactive 2D click/drag)
    function getCanvasPos(ev) {
      var rect = canvas.getBoundingClientRect();
      var cx = ev.touches ? ev.touches[0].clientX : ev.clientX;
      var cy = ev.touches ? ev.touches[0].clientY : ev.clientY;
      return { x: cx - rect.left, y: cy - rect.top, w: rect.width, h: rect.height };
    }

    function onDown(ev) {
      var pos = getCanvasPos(ev);
      if (cfg.is3D) {
        dragging = true;
        lastPointer = pos;
      } else if (cfg.interactiveCanvas && rendererFn && rendererFn.onPointerDown) {
        dragging = true;
        rendererFn.onPointerDown(pos, st, cfg, math);
        syncControlsFromState();
        renderFrame();
      }
    }

    function onMove(ev) {
      if (!dragging) return;
      var pos = getCanvasPos(ev);
      if (cfg.is3D) {
        ev.preventDefault();
        st.rotY += (pos.x - lastPointer.x) * 0.01;
        st.rotX = Math.max(-1.3, Math.min(1.3, st.rotX + (pos.y - lastPointer.y) * 0.01));
        lastPointer = pos;
        renderFrame();
      } else if (cfg.interactiveCanvas && rendererFn && rendererFn.onPointerMove) {
        ev.preventDefault();
        rendererFn.onPointerMove(pos, st, cfg, math);
        syncControlsFromState();
        renderFrame();
      }
    }

    function onUp() { dragging = false; }

    function onWheel(ev) {
      if (!cfg.is3D) return;
      ev.preventDefault();
      st.zoom = Math.max(0.65, Math.min(1.65, st.zoom + (ev.deltaY < 0 ? 0.08 : -0.08)));
      renderFrame();
    }

    canvas.addEventListener("mousedown", onDown);
    window.addEventListener("mousemove", onMove);
    window.addEventListener("mouseup", onUp);
    canvas.addEventListener("touchstart", onDown, { passive: true });
    canvas.addEventListener("touchmove", onMove, { passive: false });
    window.addEventListener("touchend", onUp);
    canvas.addEventListener("wheel", onWheel, { passive: false });

    function onResize() { renderFrame(); }
    window.addEventListener("resize", onResize);

    syncControlsFromState();
    renderFrame();
    if (st.playing) startLoop();

    return {
      state: st,
      render: renderFrame,
      destroy: function () {
        destroyed = true;
        if (rafId) cancelAnimationFrame(rafId);
        window.removeEventListener("mousemove", onMove);
        window.removeEventListener("mouseup", onUp);
        window.removeEventListener("touchend", onUp);
        window.removeEventListener("resize", onResize);
      }
    };
  }

  var modalCtrl = null;

  function openModal(topicId, cfg, sharedState) {
    closeModal();
    modalOverlay = document.createElement("div");
    modalOverlay.className = "sim-modal-overlay";
    modalOverlay.setAttribute("role", "dialog");
    modalOverlay.setAttribute("aria-modal", "true");
    modalOverlay.innerHTML = '<div class="sim-modal-card"></div>';
    document.body.appendChild(modalOverlay);
    var card = modalOverlay.querySelector(".sim-modal-card");
    modalCtrl = createController(card, topicId, cfg, sharedState, true);

    modalOverlay.addEventListener("click", function (e) {
      if (e.target === modalOverlay) closeModal();
    });
    document.addEventListener("keydown", onModalKey);
  }

  function onModalKey(e) {
    if (e.key === "Escape") closeModal();
  }

  function closeModal() {
    document.removeEventListener("keydown", onModalKey);
    if (modalCtrl) { modalCtrl.destroy(); modalCtrl = null; }
    if (modalOverlay) { modalOverlay.remove(); modalOverlay = null; }
    if (activeInstance) activeInstance.render();
  }

  function mount(container, topicId) {
    unmount();
    if (!container) return false;
    var cfg = window.simRegistry[topicId];
    if (!cfg) return false;
    activeInstance = createController(container, topicId, cfg, null, false);

    if (!themeObserver && typeof MutationObserver !== "undefined") {
      themeObserver = new MutationObserver(function () {
        if (activeInstance) activeInstance.render();
        if (modalCtrl) modalCtrl.render();
      });
      themeObserver.observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
    }
    return true;
  }

  function unmount() {
    closeModal();
    if (activeInstance) {
      activeInstance.destroy();
      activeInstance = null;
    }
  }

  /* ============================================================
     5. INTERACTIVE 2D VISUALIZERS (15 ARCHETYPES)
     ============================================================ */

  /* ---- 5.1 Central Tendency & Dispersion (with draggable outlier!) ---- */
  var centralDisp = function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state, m = env.math;
    var baseData = env.cfg.dataset || [10, 12, 13, 14, 14, 15, 15, 16, 17, 18];
    var outlierVal = st.params.outlier != null ? st.params.outlier : 18;
    var nMult = st.params.sampleSize != null ? Math.round(st.params.sampleSize) : baseData.length;
    var data = baseData.slice(0, baseData.length - 1).concat([outlierVal]);

    var mn = m.mean(data), med = m.median(data), mod = m.mode(data);
    var sd = m.sd(data, true), vr = sd * sd;
    var sem = sd / Math.sqrt(Math.max(2, nMult));
    var cv = mn ? (sd / mn) * 100 : 0;

    var pad = { l: 56, r: 28, t: 44, b: 54 };
    var minX = 0, maxX = Math.max(40, Math.ceil(outlierVal / 5) * 5 + 5);
    function sx(v) { return pad.l + ((v - minX) / (maxX - minX)) * (w - pad.l - pad.r); }

    env.drawAxes(ctx, pad, w, h, P, env.cfg.xLabel || "Milk Yield (litres / day)", "Observations");

    // +/- 1 SD shaded band
    var sdL = Math.max(pad.l, sx(mn - sd)), sdR = Math.min(w - pad.r, sx(mn + sd));
    ctx.fillStyle = P.blueLight;
    ctx.fillRect(sdL, pad.t, Math.max(2, sdR - sdL), h - pad.b - pad.t);
    ctx.fillStyle = P.blue;
    ctx.font = "700 12px " + P.fontSans;
    ctx.textAlign = "center";
    ctx.fillText("Mean ± 1 SD", (sdL + sdR) / 2, pad.t + 16);

    // X ticks
    ctx.fillStyle = P.textMuted;
    ctx.font = "600 12px " + P.fontMono;
    for (var tk = 0; tk <= maxX; tk += 5) {
      var tx = sx(tk);
      ctx.beginPath(); ctx.moveTo(tx, h - pad.b); ctx.lineTo(tx, h - pad.b + 6);
      ctx.strokeStyle = P.borderStrong; ctx.stroke();
      ctx.fillText(String(tk), tx, h - pad.b + 20);
    }

    // Stack dot plot
    var counts = {};
    for (var i = 0; i < data.length; i++) {
      var val = data[i];
      var key = Math.round(val);
      counts[key] = (counts[key] || 0) + 1;
      var cx = sx(val);
      var cy = h - pad.b - 22 - (counts[key] - 1) * 24;
      var isOutlier = (i === data.length - 1);
      ctx.beginPath();
      ctx.arc(cx, cy, isOutlier ? 11 : 8, 0, Math.PI * 2);
      ctx.fillStyle = isOutlier ? P.coral : P.blue;
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = P.surface;
      ctx.stroke();
      if (isOutlier) {
        ctx.fillStyle = P.coral;
        ctx.font = "700 12px " + P.fontSans;
        ctx.textAlign = "center";
        ctx.fillText("Drag / Outlier (" + val.toFixed(1) + ")", Math.min(w - 90, Math.max(pad.l + 70, cx)), cy - 18);
      }
    }

    // Mean, Median, Mode vertical markers
    function drawMarker(val, color, label, yOff) {
      var x = sx(val);
      ctx.save();
      ctx.strokeStyle = color;
      ctx.lineWidth = 2.5;
      ctx.setLineDash([6, 4]);
      ctx.beginPath(); ctx.moveTo(x, pad.t + yOff); ctx.lineTo(x, h - pad.b); ctx.stroke();
      ctx.restore();
      ctx.fillStyle = color;
      ctx.font = "700 13px " + P.fontSans;
      ctx.textAlign = "center";
      ctx.fillText(label + " " + val.toFixed(1), Math.min(w - 55, Math.max(pad.l + 55, x)), pad.t + yOff - 6);
    }
    drawMarker(med, P.teal, "Median", 34);
    drawMarker(mn, P.coral, "Mean", 14);
    drawMarker(mod, P.purple, "Mode", 54);

    var shifted = Math.abs(mn - med) > 1.2;
    return {
      readouts: [
        { label: "Mean (x̄)", value: mn.toFixed(2), tone: shifted ? "danger" : "accent" },
        { label: "Median", value: med.toFixed(2), tone: "teal" },
        { label: "SD (s) / Var (s²)", value: sd.toFixed(2) + " / " + vr.toFixed(1), tone: "purple" },
        { label: "CV (%)", value: cv.toFixed(1) + "%", sub: "Lower = more uniform" },
        { label: "SEM (s/√n)", value: sem.toFixed(2), sub: "at n = " + nMult, tone: "ok" }
      ],
      insight: shifted
        ? "Notice how dragging the single outlier to <b>" + outlierVal.toFixed(1) + "</b> pulled the <b>Mean (" + mn.toFixed(2) + ")</b> sharply upward and inflated <b>SD (" + sd.toFixed(2) + ")</b>, while the <b>Median (" + med.toFixed(2) + ")</b> stayed rock-solid! That is why Median is preferred for skewed biological data. Also notice SEM = SD / √n shrinks as sample size n increases."
        : "With symmetric data, <b>Mean (" + mn.toFixed(2) + ") ≈ Median (" + med.toFixed(2) + ") ≈ Mode (" + mod.toFixed(1) + ")</b>. Drag the red point right (or move the Outlier slider) to see how an extreme cow/patient distorts the Mean and SD while leaving the Median unchanged!",
      formula: "SD = √[Σ(x − x̄)²/(n−1)]   |   CV% = (SD / x̄) × 100   |   SEM = SD / √n"
    };
  };
  centralDisp.onPointerDown = centralDisp.onPointerMove = function (pos, st) {
    var padL = 56, padR = 28;
    var maxX = Math.max(40, Math.ceil((st.params.outlier || 18) / 5) * 5 + 5);
    var frac = Math.max(0, Math.min(1, (pos.x - padL) / Math.max(100, pos.w - padL - padR)));
    st.params.outlier = Math.round(frac * 45);
  };
  registerRenderer("central_dispersion", centralDisp);

  /* ---- 5.2 Skewness & Kurtosis Morphing Visualizer ---- */
  registerRenderer("skew_kurtosis", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var skew = st.params.skew != null ? st.params.skew : 0; // -2 to +2
    var kurt = st.params.kurt != null ? st.params.kurt : 3; // 1.8 to 5.5
    var pad = { l: 52, r: 28, t: 36, b: 52 };
    env.drawAxes(ctx, pad, w, h, P, "Trait Value (e.g., Lactation Yield / Somatic Cell Count)", "Frequency Density");

    // Skew-normal + kurtosis power transform for crisp visual
    var pts = [], maxY = 0;
    var power = kurt > 3 ? 2 - (kurt - 3) * 0.28 : 2 + (3 - kurt) * 0.9;
    var meanSum = 0, wSum = 0, modeX = 0, modeY = 0;
    for (var i = 0; i <= 160; i++) {
      var x = -4 + (8 * i) / 160;
      var base = Math.exp(-0.5 * Math.pow(Math.abs(x), Math.max(0.8, power)));
      var cdf = env.math.normalCDF(skew * x * 1.35);
      var y = 2 * base * cdf;
      pts.push({ x: x, y: y });
      if (y > maxY) { maxY = y; modeX = x; modeY = y; }
      meanSum += x * y;
      wSum += y;
    }
    var meanX = meanSum / (wSum || 1);
    var cum = 0, medX = 0;
    for (var j = 0; j < pts.length; j++) {
      cum += pts[j].y;
      if (cum >= wSum / 2) { medX = pts[j].x; break; }
    }

    function sx(x) { return pad.l + ((x + 4) / 8) * (w - pad.l - pad.r); }
    function sy(y) { return h - pad.b - (y / (maxY * 1.18 || 1)) * (h - pad.t - pad.b); }

    // Reference Mesokurtic Symmetric dashed curve
    ctx.save();
    ctx.setLineDash([5, 5]);
    ctx.strokeStyle = P.textFaint;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    for (var k = 0; k <= 100; k++) {
      var rx = -4 + (8 * k) / 100;
      var ry = Math.exp(-0.5 * rx * rx) * (maxY * 0.72);
      if (k === 0) ctx.moveTo(sx(rx), sy(ry)); else ctx.lineTo(sx(rx), sy(ry));
    }
    ctx.stroke();
    ctx.restore();

    // Filled curve
    ctx.beginPath();
    ctx.moveTo(sx(pts[0].x), h - pad.b);
    pts.forEach(function (pt) { ctx.lineTo(sx(pt.x), sy(pt.y)); });
    ctx.lineTo(sx(pts[pts.length - 1].x), h - pad.b);
    ctx.closePath();
    ctx.fillStyle = P.blueLight;
    ctx.fill();
    ctx.strokeStyle = P.blue;
    ctx.lineWidth = 3;
    ctx.stroke();

    // Mean, Median, Mode lines
    function mark(xv, col, lbl, row) {
      var px = sx(xv);
      ctx.strokeStyle = col; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(px, pad.t + row * 18); ctx.lineTo(px, h - pad.b); ctx.stroke();
      ctx.fillStyle = col; ctx.font = "700 13px " + P.fontSans; ctx.textAlign = "center";
      ctx.fillText(lbl, Math.min(w - 45, Math.max(pad.l + 45, px)), pad.t + row * 18 - 4);
    }
    mark(modeX, P.purple, "Mode", 0);
    mark(medX, P.teal, "Median", 1);
    mark(meanX, P.coral, "Mean", 2);

    var skewLabel = skew > 0.2 ? "Positive (Right-Skewed)" : (skew < -0.2 ? "Negative (Left-Skewed)" : "Symmetric (Normal)");
    var orderStr = skew > 0.2 ? "Mean > Median > Mode" : (skew < -0.2 ? "Mean < Median < Mode" : "Mean = Median = Mode");
    var kurtLabel = kurt > 3.25 ? "Leptokurtic (Peaked)" : (kurt < 2.75 ? "Platykurtic (Flat)" : "Mesokurtic (Normal)");
    return {
      readouts: [
        { label: "Skewness Type", value: skewLabel, tone: Math.abs(skew) > 0.2 ? "warn" : "ok" },
        { label: "Central Tendency Order", value: orderStr, tone: "accent" },
        { label: "Kurtosis (β₂)", value: kurt.toFixed(2) + " · " + kurtLabel.split(" ")[0], tone: "purple" },
        { label: "Excess Kurtosis (γ₂)", value: (kurt - 3).toFixed(2), sub: "γ₂ = β₂ − 3" }
      ],
      insight: "<b>Exam Rule:</b> In a <b>" + skewLabel + "</b> curve, <b>" + orderStr + "</b>. Kurtosis β₂ = μ₄/μ₂² measures peakedness: <b>β₂ = 3</b> is Mesokurtic (Normal), <b>β₂ > 3</b> is Leptokurtic (tall, sharp peak), and <b>β₂ < 3</b> is Platykurtic (flat top).",
      formula: "β₁ = μ₃² / μ₂³   |   β₂ = μ₄ / μ₂²   |   Pearson's Empirical: Mode ≈ 3(Median) − 2(Mean)"
    };
  });

  /* ---- 5.3 Probability Distributions (Binomial, Poisson, Standard Normal) ---- */
  registerRenderer("prob_distributions", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state, m = env.math;
    var mode = st.params.dist || "normal";
    var pad = { l: 56, r: 28, t: 38, b: 54 };

    if (mode === "normal") {
      var mu = st.params.mu != null ? st.params.mu : 100;
      var sigma = st.params.sigma != null ? st.params.sigma : 15;
      var zCut = st.params.z != null ? st.params.z : 1.0;
      var minX = mu - 4 * sigma, maxX = mu + 4 * sigma;
      function sx(x) { return pad.l + ((x - minX) / (maxX - minX)) * (w - pad.l - pad.r); }
      var peak = m.normalPDF(mu, mu, sigma);
      function sy(y) { return h - pad.b - (y / (peak * 1.18)) * (h - pad.t - pad.b); }

      env.drawAxes(ctx, pad, w, h, P, "Trait Value X (Mean μ = " + mu + ", SD σ = " + sigma + ")", "Probability Density");

      // Shade ±3σ, ±2σ, ±1σ bands
      var bands = [
        { k: 3, col: P.purpleLight, lbl: "99.73% (±3σ)" },
        { k: 2, col: P.tealLight, lbl: "95.45% (±2σ)" },
        { k: 1, col: P.blueLight, lbl: "68.27% (±1σ)" }
      ];
      bands.forEach(function (b) {
        ctx.beginPath();
        var xA = mu - b.k * sigma, xB = mu + b.k * sigma;
        ctx.moveTo(sx(xA), h - pad.b);
        for (var i = 0; i <= 80; i++) {
          var xv = xA + ((xB - xA) * i) / 80;
          ctx.lineTo(sx(xv), sy(m.normalPDF(xv, mu, sigma)));
        }
        ctx.lineTo(sx(xB), h - pad.b);
        ctx.closePath();
        ctx.fillStyle = b.col;
        ctx.fill();
      });

      // Highlight Z-score area from -∞ to Z
      var xZ = mu + zCut * sigma;
      ctx.beginPath();
      ctx.moveTo(sx(minX), h - pad.b);
      for (var j = 0; j <= 100; j++) {
        var xv2 = minX + ((xZ - minX) * j) / 100;
        ctx.lineTo(sx(xv2), sy(m.normalPDF(xv2, mu, sigma)));
      }
      ctx.lineTo(sx(xZ), h - pad.b);
      ctx.closePath();
      ctx.fillStyle = P.amberLight;
      ctx.globalAlpha = 0.65;
      ctx.fill();
      ctx.globalAlpha = 1;

      // Curve stroke
      ctx.beginPath();
      for (var k = 0; k <= 160; k++) {
        var xv3 = minX + ((maxX - minX) * k) / 160;
        if (k === 0) ctx.moveTo(sx(xv3), sy(m.normalPDF(xv3, mu, sigma)));
        else ctx.lineTo(sx(xv3), sy(m.normalPDF(xv3, mu, sigma)));
      }
      ctx.strokeStyle = P.blue;
      ctx.lineWidth = 3;
      ctx.stroke();

      // Z marker
      ctx.strokeStyle = P.coral; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(sx(xZ), pad.t); ctx.lineTo(sx(xZ), h - pad.b); ctx.stroke();
      ctx.fillStyle = P.coral; ctx.font = "700 13px " + P.fontMono; ctx.textAlign = "center";
      ctx.fillText("Z = " + zCut.toFixed(2) + " (X=" + xZ.toFixed(1) + ")", Math.min(w - 85, Math.max(pad.l + 85, sx(xZ))), pad.t + 12);

      // Sigma ticks
      ctx.fillStyle = P.textMuted; ctx.font = "600 12px " + P.fontMono; ctx.textAlign = "center";
      for (var s = -3; s <= 3; s++) {
        var tx = sx(mu + s * sigma);
        ctx.fillText((s === 0 ? "μ" : (s > 0 ? "+" + s + "σ" : s + "σ")), tx, h - pad.b + 18);
      }

      var cumP = m.normalCDF(zCut);
      var withinZ = Math.max(0, (m.normalCDF(Math.abs(zCut)) - m.normalCDF(-Math.abs(zCut))) * 100);
      return {
        readouts: [
          { label: "P(Z ≤ " + zCut.toFixed(2) + ")", value: (cumP * 100).toFixed(2) + "%", tone: "accent" },
          { label: "Within ±|Z|", value: withinZ.toFixed(2) + "%", tone: "teal" },
          { label: "±1σ / ±2σ / ±3σ", value: "68.27 / 95.45 / 99.73%", tone: "purple" },
          { label: "Z-Score Value", value: "X = " + xZ.toFixed(1), sub: "Z = (X − μ) / σ" }
        ],
        insight: "In a <b>Standard Normal Distribution</b> (μ = 0, σ = 1), exact areas are <b>68.27% (±1σ)</b>, <b>95.45% (±2σ)</b>, and <b>99.73% (±3σ)</b>. Total area under the curve = 1.0, and Mean = Median = Mode.",
        formula: "Z = (X − μ) / σ   |   f(x) = [1 / (σ√2π)] · e^(−½((x−μ)/σ)²)"
      };
    }

    // Discrete distributions: Binomial or Poisson
    var n = Math.round(st.params.n != null ? st.params.n : 12);
    var p = st.params.p != null ? st.params.p : 0.5;
    var lam = st.params.lambda != null ? st.params.lambda : 3.5;
    var maxK = mode === "binomial" ? n : Math.max(12, Math.ceil(lam + 4 * Math.sqrt(lam)));
    var probs = [], maxP = 0;
    for (var kk = 0; kk <= maxK; kk++) {
      var pr = mode === "binomial" ? m.binomialPMF(n, kk, p) : m.poissonPMF(kk, lam);
      probs.push(pr);
      if (pr > maxP) maxP = pr;
    }

    env.drawAxes(ctx, pad, w, h, P, mode === "binomial" ? "Number of Successes (k out of n = " + n + ")" : "Rare Events Count (k, λ = " + lam.toFixed(1) + ")", "Probability P(X = k)");
    var plotW = w - pad.l - pad.r, plotH = h - pad.t - pad.b;
    var barW = Math.max(8, (plotW / (maxK + 1)) * 0.72);
    for (var b = 0; b <= maxK; b++) {
      var bx = pad.l + ((b + 0.5) / (maxK + 1)) * plotW - barW / 2;
      var bh = (probs[b] / (maxP * 1.15 || 1)) * plotH;
      var by = h - pad.b - bh;
      ctx.fillStyle = mode === "binomial" ? P.blue : P.teal;
      env.roundRect(ctx, bx, by, barW, bh, 4);
      ctx.fill();
      if (maxK <= 16 || b % 2 === 0) {
        ctx.fillStyle = P.textMuted; ctx.font = "600 12px " + P.fontMono; ctx.textAlign = "center";
        ctx.fillText(String(b), bx + barW / 2, h - pad.b + 18);
      }
      if (probs[b] > 0.05 && maxK <= 14) {
        ctx.fillStyle = P.text; ctx.font = "700 11px " + P.fontMono;
        ctx.fillText((probs[b] * 100).toFixed(0) + "%", bx + barW / 2, by - 6);
      }
    }

    var meanVal = mode === "binomial" ? n * p : lam;
    var varVal = mode === "binomial" ? n * p * (1 - p) : lam;
    return {
      readouts: [
        { label: "Distribution", value: mode === "binomial" ? "Binomial B(n,p)" : "Poisson P(λ)", tone: "accent" },
        { label: "Mean (μ)", value: meanVal.toFixed(2), tone: "teal" },
        { label: "Variance (σ²)", value: varVal.toFixed(2), tone: "purple" },
        { label: "Mean vs Variance", value: mode === "binomial" ? "Mean > Var" : "Mean = Var = λ", tone: "ok" }
      ],
      insight: mode === "binomial"
        ? "<b>Binomial Distribution</b> models fixed independent trials (e.g., calf sex ratio or 3:1 Mendelian offspring in litters of size n). Notice <b>Mean = np (" + meanVal.toFixed(2) + ")</b> is always greater than <b>Variance = npq (" + varVal.toFixed(2) + ")</b>!"
        : "<b>Poisson Distribution</b> models rare events per unit time/area (e.g., bacterial colonies, spontaneous mutations, sporadic disease outbreaks). Its hallmark exam property: <b>Mean = Variance = λ (" + lam.toFixed(2) + ")</b>!",
      formula: mode === "binomial" ? "P(X=k) = ⁿCₖ · pᵏ · qⁿ⁻ᵏ   |   Mean = np, Var = npq" : "P(X=k) = (e⁻λ · λᵏ) / k!   |   Mean = Variance = λ"
    };
  });

  /* ---- 5.4 Correlation & Linear Regression (Interactive Click-to-Add Scatter) ---- */
  var corrReg = function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state, m = env.math;
    var targetR = st.params.r != null ? st.params.r : 0.85;
    // Generate deterministic correlated points + any user-clicked points
    var basePts = [];
    var seeds = [-1.6, -1.3, -1.0, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1.1, 1.4, 1.7];
    var errs = [0.6, -0.8, 0.4, -0.5, 0.9, -0.3, 0.7, -0.9, 0.3, -0.6, 0.5, -0.4];
    var noiseScale = Math.sqrt(Math.max(0, 1 - targetR * targetR));
    for (var i = 0; i < seeds.length; i++) {
      var x = 50 + seeds[i] * 18;
      var y = 50 + (targetR * seeds[i] + noiseScale * errs[i] * 1.15) * 18;
      basePts.push({ x: Math.max(5, Math.min(95, x)), y: Math.max(5, Math.min(95, y)) });
    }
    var extra = st.custom.extraPts || [];
    var pts = basePts.concat(extra);
    var reg = m.linReg(pts);

    var pad = { l: 56, r: 28, t: 34, b: 52 };
    function sx(x) { return pad.l + (x / 100) * (w - pad.l - pad.r); }
    function sy(y) { return h - pad.b - (y / 100) * (h - pad.t - pad.b); }
    env.drawAxes(ctx, pad, w, h, P, env.cfg.xLabel || "Body Weight X (kg)", env.cfg.yLabel || "Milk Yield / Heart Girth Y");

    // Residuals
    ctx.strokeStyle = P.coral;
    ctx.lineWidth = 1.3;
    ctx.globalAlpha = 0.55;
    pts.forEach(function (pt) {
      var yHat = reg.a + reg.b * pt.x;
      ctx.beginPath(); ctx.moveTo(sx(pt.x), sy(pt.y)); ctx.lineTo(sx(pt.x), sy(yHat)); ctx.stroke();
    });
    ctx.globalAlpha = 1;

    // Least-squares regression line
    var y0 = reg.a + reg.b * 5, y1 = reg.a + reg.b * 95;
    ctx.strokeStyle = P.blue;
    ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(sx(5), sy(Math.max(0, Math.min(100, y0)))); ctx.lineTo(sx(95), sy(Math.max(0, Math.min(100, y1)))); ctx.stroke();

    // Points
    pts.forEach(function (pt, idx) {
      ctx.beginPath();
      ctx.arc(sx(pt.x), sy(pt.y), idx >= basePts.length ? 8 : 6.5, 0, Math.PI * 2);
      ctx.fillStyle = idx >= basePts.length ? P.coral : P.teal;
      ctx.fill();
      ctx.strokeStyle = P.surface; ctx.lineWidth = 2; ctx.stroke();
    });

    ctx.fillStyle = P.blue; ctx.font = "700 13px " + P.fontMono; ctx.textAlign = "left";
    ctx.fillText("Ŷ = " + reg.a.toFixed(1) + " + " + reg.b.toFixed(2) + "X", pad.l + 12, pad.t + 18);

    return {
      readouts: [
        { label: "Pearson r", value: reg.r.toFixed(3), tone: Math.abs(reg.r) > 0.6 ? "ok" : "warn" },
        { label: "Spearman ρ", value: reg.rho.toFixed(3), tone: "teal" },
        { label: "Slope (b_yx)", value: reg.b.toFixed(3), tone: "accent" },
        { label: "R² (Explained)", value: (reg.r2 * 100).toFixed(1) + "%", tone: "purple" }
      ],
      insight: "<b>Click anywhere on the plot</b> to add an animal observation and watch the red residuals and least-squares line adjust! <b>R² = " + (reg.r2 * 100).toFixed(1) + "%</b> of the variance in Y is explained by X. Remember: <b>r = √(b_yx · b_xy)</b> and both regression coefficients always share the same sign as r.",
      formula: "Ŷ = a + bX   |   b = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²   |   r = √(b_yx · b_xy)   |   −1 ≤ r ≤ +1"
    };
  };
  corrReg.onPointerDown = function (pos, st) {
    var padL = 56, padR = 28, padT = 34, padB = 52;
    var x = ((pos.x - padL) / Math.max(100, pos.w - padL - padR)) * 100;
    var y = (1 - (pos.y - padT) / Math.max(100, pos.h - padT - padB)) * 100;
    if (x >= 2 && x <= 98 && y >= 2 && y <= 98) {
      st.custom.extraPts = (st.custom.extraPts || []).concat([{ x: x, y: y }]).slice(-8);
    }
  };
  registerRenderer("corr_regression", corrReg);

  /* ---- 5.5 Hypothesis Testing (Z, t, Chi-Square + Mendelian 3:1/9:3:3:1, F-test) ---- */
  registerRenderer("hypothesis_test", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state, m = env.math;
    var test = st.params.test || env.cfg.defaultTest || "t";
    var alpha = parseFloat(st.params.alpha || "0.05");
    var df = Math.round(st.params.df != null ? st.params.df : 12);
    var stat = st.params.stat != null ? st.params.stat : 2.35;
    var pad = { l: 52, r: 28, t: 38, b: 52 };

    var crit, reject, benchHtml = "", insightMsg = "", formulaStr = "";

    if (test === "chisq") {
      // Interactive Mendelian 3:1 or 9:3:3:1 Goodness-of-Fit + Chi-square curve!
      var ratioMode = st.params.ratio || "3:1";
      var dev = st.params.stat != null ? st.params.stat : 1.5; // deviation knob
      var totalN = 160;
      var obs, exp, labels;
      if (ratioMode === "3:1") {
        df = 1;
        exp = [120, 40];
        var d = Math.round(dev * 4);
        obs = [120 - d, 40 + d];
        labels = ["Dominant (3/4)", "Recessive (1/4)"];
      } else {
        df = 3;
        exp = [90, 30, 30, 10];
        var d2 = Math.round(dev * 3);
        obs = [90 - d2, 30 + Math.round(d2 * 0.5), 30 + Math.round(d2 * 0.5), 10];
        labels = ["A_B_ (9/16)", "A_bb (3/16)", "aaB_ (3/16)", "aabb (1/16)"];
      }
      var chiVal = 0;
      for (var i = 0; i < obs.length; i++) chiVal += Math.pow(obs[i] - exp[i], 2) / exp[i];
      stat = chiVal;
      crit = m.chiCrit(df, alpha);
      reject = stat > crit;

      // Draw Chi-Square distribution curve
      var maxX = Math.max(16, crit * 1.8, stat * 1.25);
      var maxY = 0;
      for (var k = 1; k <= 120; k++) {
        var yy = m.chiSqPDF((maxX * k) / 120, Math.max(2, df));
        if (yy > maxY) maxY = yy;
      }
      function sx(x) { return pad.l + (x / maxX) * (w - pad.l - pad.r); }
      function sy(y) { return h - pad.b - (y / (maxY * 1.18 || 1)) * (h - pad.t - pad.b); }
      env.drawAxes(ctx, pad, w, h, P, "Chi-Square Statistic χ² (df = " + df + ")", "Density");

      // Critical rejection region (right tail)
      ctx.beginPath();
      ctx.moveTo(sx(crit), h - pad.b);
      for (var j = 0; j <= 60; j++) {
        var xv = crit + ((maxX - crit) * j) / 60;
        ctx.lineTo(sx(xv), sy(m.chiSqPDF(xv, Math.max(2, df))));
      }
      ctx.lineTo(sx(maxX), h - pad.b);
      ctx.closePath();
      ctx.fillStyle = P.dangerSoft;
      ctx.fill();

      // Main curve
      ctx.beginPath();
      for (var c = 1; c <= 140; c++) {
        var cx = (maxX * c) / 140;
        var cy = m.chiSqPDF(cx, Math.max(2, df));
        if (c === 1) ctx.moveTo(sx(cx), sy(cy)); else ctx.lineTo(sx(cx), sy(cy));
      }
      ctx.strokeStyle = P.blue; ctx.lineWidth = 3; ctx.stroke();

      // Crit & Calculated lines
      ctx.strokeStyle = P.danger; ctx.lineWidth = 2; ctx.setLineDash([5, 4]);
      ctx.beginPath(); ctx.moveTo(sx(crit), pad.t); ctx.lineTo(sx(crit), h - pad.b); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = P.danger; ctx.font = "700 12px " + P.fontMono; ctx.textAlign = "center";
      ctx.fillText("Crit χ²=" + crit.toFixed(2), sx(crit), pad.t + 12);

      var calcX = sx(Math.min(maxX * 0.96, stat));
      ctx.strokeStyle = reject ? P.coral : P.ok; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(calcX, pad.t + 22); ctx.lineTo(calcX, h - pad.b); ctx.stroke();
      ctx.fillStyle = reject ? P.coral : P.ok;
      ctx.fillText("Calc χ²=" + stat.toFixed(2), Math.min(w - 60, Math.max(pad.l + 60, calcX)), pad.t + 34);

      benchHtml = '<table class="sim-table"><thead><tr><th>Mendelian Class (' + ratioMode + ')</th><th>Observed (O)</th><th>Expected (E)</th><th>(O − E)² / E</th></tr></thead><tbody>' +
        labels.map(function (lb, idx) {
          var term = Math.pow(obs[idx] - exp[idx], 2) / exp[idx];
          return '<tr><td>' + lb + '</td><td class="sim-num">' + obs[idx] + '</td><td class="sim-num">' + exp[idx] + '</td><td class="sim-num">' + term.toFixed(3) + '</td></tr>';
        }).join("") +
        '<tr><th>Total (N = ' + totalN + ')</th><th class="sim-num">' + totalN + '</th><th class="sim-num">' + totalN + '</th><th class="sim-num sim-highlight">χ² = ' + stat.toFixed(3) + '</th></tr></tbody></table>';
      insightMsg = reject
        ? "<b>REJECT H₀:</b> Calculated χ² (" + stat.toFixed(2) + ") exceeds critical χ² (" + crit.toFixed(2) + " at df=" + df + ", α=" + alpha + "). The observed offspring deviate significantly from the Mendelian " + ratioMode + " ratio (check for linkage, lethal genes, or epistasis!)."
        : "<b>FAIL TO REJECT H₀:</b> Calculated χ² (" + stat.toFixed(2) + ") ≤ critical χ² (" + crit.toFixed(2) + "). Observed counts fit the expected Mendelian " + ratioMode + " segregation ratio!";
      formulaStr = "χ² = Σ [ (O − E)² / E ]   |   df = k − 1 (Goodness-of-Fit)  or  (r − 1)(c − 1) (Contingency)";
    } else {
      // Z-test or Student's t-test (two-tailed symmetric)
      crit = test === "z" ? (alpha <= 0.01 ? 2.576 : 1.960) : m.tCrit(df, alpha);
      reject = Math.abs(stat) > crit;
      var maxZ = 4.2;
      function sx2(x) { return pad.l + ((x + maxZ) / (2 * maxZ)) * (w - pad.l - pad.r); }
      var pdf = function (x) { return test === "z" ? m.normalPDF(x, 0, 1) : m.tPDF(x, df); };
      var peak2 = pdf(0);
      function sy2(y) { return h - pad.b - (y / (peak2 * 1.18)) * (h - pad.t - pad.b); }
      env.drawAxes(ctx, pad, w, h, P, (test === "z" ? "Standard Normal Z" : "Student's t (df = " + df + ")"), "Density");

      // Shade both critical tails
      [[-maxZ, -crit], [crit, maxZ]].forEach(function (rng) {
        ctx.beginPath();
        ctx.moveTo(sx2(rng[0]), h - pad.b);
        for (var j = 0; j <= 40; j++) {
          var xv = rng[0] + ((rng[1] - rng[0]) * j) / 40;
          ctx.lineTo(sx2(xv), sy2(pdf(xv)));
        }
        ctx.lineTo(sx2(rng[1]), h - pad.b);
        ctx.closePath();
        ctx.fillStyle = P.dangerSoft;
        ctx.fill();
      });

      // Curve
      ctx.beginPath();
      for (var c2 = 0; c2 <= 160; c2++) {
        var xv2 = -maxZ + (2 * maxZ * c2) / 160;
        if (c2 === 0) ctx.moveTo(sx2(xv2), sy2(pdf(xv2))); else ctx.lineTo(sx2(xv2), sy2(pdf(xv2)));
      }
      ctx.strokeStyle = P.blue; ctx.lineWidth = 3; ctx.stroke();

      // Crit lines
      [-crit, crit].forEach(function (cv) {
        ctx.strokeStyle = P.danger; ctx.lineWidth = 1.8; ctx.setLineDash([5, 4]);
        ctx.beginPath(); ctx.moveTo(sx2(cv), pad.t + 12); ctx.lineTo(sx2(cv), h - pad.b); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = P.danger; ctx.font = "700 12px " + P.fontMono; ctx.textAlign = "center";
        ctx.fillText((cv > 0 ? "+" : "") + cv.toFixed(2), sx2(cv), pad.t + 10);
      });

      // Calculated stat
      var clX = sx2(Math.max(-maxZ + 0.15, Math.min(maxZ - 0.15, stat)));
      ctx.strokeStyle = reject ? P.coral : P.ok; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(clX, pad.t + 26); ctx.lineTo(clX, h - pad.b); ctx.stroke();
      ctx.fillStyle = reject ? P.coral : P.ok; ctx.font = "700 13px " + P.fontMono; ctx.textAlign = "center";
      ctx.fillText((test === "z" ? "Z=" : "t=") + stat.toFixed(2), clX, pad.t + 24);

      insightMsg = reject
        ? "<b>REJECT H₀ (Statistically Significant, p < " + alpha + "):</b> |" + stat.toFixed(2) + "| falls inside the shaded rejection region beyond ±" + crit.toFixed(3) + ". There is strong evidence of a real biological/treatment difference."
        : "<b>FAIL TO REJECT H₀ (Non-Significant, p ≥ " + alpha + "):</b> |" + stat.toFixed(2) + "| lies within the acceptance zone (±" + crit.toFixed(3) + "). Observed difference could be due to sampling chance alone.";
      formulaStr = test === "z"
        ? "Z = (x̄ − μ) / (σ/√n)   |   Large sample (n ≥ 30)   |   Crit: ±1.96 (α=0.05), ±2.58 (α=0.01)"
        : "t = (x̄₁ − x̄₂) / SE_diff   |   Small sample (n < 30), df = n₁ + n₂ − 2 (or n − 1 for paired)";
    }

    return {
      readouts: [
        { label: "Test Statistic", value: stat.toFixed(3), tone: reject ? "danger" : "ok" },
        { label: "Critical Value (α=" + alpha + ")", value: "±" + crit.toFixed(3), tone: "accent" },
        { label: "Degrees of Freedom", value: test === "z" ? "∞ (Large n)" : String(df), tone: "purple" },
        { label: "Decision on H₀", value: reject ? "REJECT H₀" : "FAIL TO REJECT", tone: reject ? "danger" : "ok" }
      ],
      bench: benchHtml,
      insight: insightMsg,
      formula: formulaStr
    };
  });

  /* ---- 5.6 Experimental Designs (CRD vs RBD) & ANOVA ---- */
  registerRenderer("exp_design", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state, m = env.math;
    var design = st.params.design || "rbd";
    var trtEff = st.params.trtEffect != null ? st.params.trtEffect : 3.5;
    var blockVar = st.params.blockNoise != null ? st.params.blockNoise : 4.5;

    // 4 Treatments (Diets A, B, C, D) × 4 Replications/Blocks (Parity 1..4)
    var trts = ["Diet A", "Diet B", "Diet C", "Diet D"];
    var trtCols = [P.blue, P.teal, P.purple, P.amberFill];
    var trtOffsets = [-trtEff, -trtEff * 0.3, trtEff * 0.3, trtEff];
    var blkOffsets = [-blockVar, -blockVar * 0.33, blockVar * 0.33, blockVar];
    var noise = [
      [0.4, -0.5, 0.3, -0.2],
      [-0.3, 0.6, -0.4, 0.1],
      [0.2, -0.2, 0.5, -0.5],
      [-0.3, 0.1, -0.4, 0.6]
    ];
    // Deterministic randomized layout
    var crdOrder = [2, 0, 3, 1, 1, 3, 0, 2, 0, 2, 1, 3, 3, 1, 2, 0];
    var rbdOrder = [[0, 2, 1, 3], [3, 0, 2, 1], [1, 3, 0, 2], [2, 1, 3, 0]];

    // Compute exact ANOVA values for both CRD and RBD on the same farm gradient!
    var grandMean = 16.0;
    var grid = [];
    for (var b = 0; b < 4; b++) {
      grid[b] = [];
      for (var t = 0; t < 4; t++) {
        grid[b][t] = grandMean + trtOffsets[t] + blkOffsets[b] + noise[b][t];
      }
    }
    var ssTrt = 0, ssBlk = 0, ssTot = 0;
    for (var t2 = 0; t2 < 4; t2++) {
      var tm = 0; for (var b2 = 0; b2 < 4; b2++) tm += grid[b2][t2] / 4;
      ssTrt += 4 * Math.pow(tm - grandMean, 2);
    }
    for (var b3 = 0; b3 < 4; b3++) {
      var bm = 0; for (var t3 = 0; t3 < 4; t3++) bm += grid[b3][t3] / 4;
      ssBlk += 4 * Math.pow(bm - grandMean, 2);
    }
    for (var b4 = 0; b4 < 4; b4++) for (var t4 = 0; t4 < 4; t4++) ssTot += Math.pow(grid[b4][t4] - grandMean, 2);

    var ssErrCRD = Math.max(0.1, ssTot - ssTrt);
    var ssErrRBD = Math.max(0.1, ssTot - ssTrt - ssBlk);
    var dfTrt = 3, dfBlk = 3;
    var dfErr = design === "rbd" ? 9 : 12;
    var ssErr = design === "rbd" ? ssErrRBD : ssErrCRD;
    var msTrt = ssTrt / dfTrt;
    var msBlk = ssBlk / dfBlk;
    var msErr = ssErr / dfErr;
    var fCalc = msTrt / msErr;
    var fCrit = m.fCrit(dfTrt, dfErr, 0.05);
    var sig = fCalc > fCrit;

    // Draw Farm Pen Randomization Grid
    var padX = 28, padY = 44;
    var gridW = w - padX * 2 - 90, gridH = h - padY - 26;
    var cellW = gridW / 4, cellH = gridH / 4;

    ctx.fillStyle = P.text; ctx.font = "700 14px " + P.fontSans; ctx.textAlign = "left";
    ctx.fillText(design === "rbd" ? "RBD: Local Control — Each Block (Parity/Shed) Contains All 4 Diets" : "CRD: Complete Randomization Across Heterogeneous Pens (No Blocking)", padX, 24);

    for (var row = 0; row < 4; row++) {
      if (design === "rbd") {
        ctx.fillStyle = P.textMuted; ctx.font = "700 12px " + P.fontSans; ctx.textAlign = "left";
        ctx.fillText("Block " + (row + 1), padX + gridW + 10, padY + row * cellH + cellH / 2 + 4);
      }
      for (var col = 0; col < 4; col++) {
        var trtIdx = design === "rbd" ? rbdOrder[row][col] : crdOrder[row * 4 + col];
        var x = padX + col * cellW + 4, y = padY + row * cellH + 4;
        var cw = cellW - 8, ch = cellH - 8;
        ctx.fillStyle = trtCols[trtIdx];
        ctx.globalAlpha = 0.22;
        env.roundRect(ctx, x, y, cw, ch, 8);
        ctx.fill();
        ctx.globalAlpha = 1;
        ctx.strokeStyle = trtCols[trtIdx];
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = P.text;
        ctx.font = "700 13px " + P.fontSans;
        ctx.textAlign = "center";
        ctx.fillText(trts[trtIdx], x + cw / 2, y + ch / 2 - 4);
        ctx.fillStyle = P.textMuted;
        ctx.font = "600 12px " + P.fontMono;
        ctx.fillText(grid[row][trtIdx].toFixed(1) + " L", x + cw / 2, y + ch / 2 + 14);
      }
    }

    var bench = '<table class="sim-table"><thead><tr><th>Source of Variation</th><th>df</th><th>Sum of Squares (SS)</th><th>Mean Square (MS)</th><th>F-Ratio</th></tr></thead><tbody>' +
      '<tr><td>Treatments (Diets A–D)</td><td class="sim-num">' + dfTrt + '</td><td class="sim-num">' + ssTrt.toFixed(2) + '</td><td class="sim-num">' + msTrt.toFixed(2) + '</td><td class="sim-num sim-highlight">' + fCalc.toFixed(2) + (sig ? ' *' : ' NS') + '</td></tr>' +
      (design === "rbd" ? '<tr><td>Blocks (Parity/Shed)</td><td class="sim-num">' + dfBlk + '</td><td class="sim-num">' + ssBlk.toFixed(2) + '</td><td class="sim-num">' + msBlk.toFixed(2) + '</td><td class="sim-num">' + (msBlk / msErr).toFixed(2) + '</td></tr>' : '') +
      '<tr><td>Experimental Error</td><td class="sim-num">' + dfErr + '</td><td class="sim-num">' + ssErr.toFixed(2) + '</td><td class="sim-num">' + msErr.toFixed(2) + '</td><td class="sim-num">—</td></tr>' +
      '<tr><th>Total</th><th class="sim-num">15</th><th class="sim-num">' + ssTot.toFixed(2) + '</th><th class="sim-num">—</th><th class="sim-num">F₀.₀₅ = ' + fCrit.toFixed(2) + '</th></tr></tbody></table>';

    return {
      readouts: [
        { label: "Error MS", value: msErr.toFixed(2), tone: design === "rbd" ? "ok" : "warn" },
        { label: "F-Calculated", value: fCalc.toFixed(2), tone: sig ? "ok" : "danger" },
        { label: "F-Critical (5%)", value: fCrit.toFixed(2), tone: "accent" },
        { label: "ANOVA Result", value: sig ? "Significant (*)" : "Non-Significant", tone: sig ? "ok" : "warn" }
      ],
      bench: bench,
      insight: design === "rbd"
        ? "<b>RBD Local Control in Action!</b> By blocking pens by parity/shed, RBD pulls <b>SS_Blocks (" + ssBlk.toFixed(1) + ")</b> OUT of Experimental Error, slashing Error MS from <b>" + (ssErrCRD / 12).toFixed(2) + "</b> down to <b>" + msErr.toFixed(2) + "</b> and boosting your F-ratio power!"
        : "<b>CRD Limitation:</b> CRD uses only Randomization & Replication (no Local Control). When animals vary by parity/shed (Block Noise = " + blockVar.toFixed(1) + "), that variation inflates Error MS (" + msErr.toFixed(2) + ") and can mask a real diet effect. Switch to <b>RBD</b> to see the F-ratio jump!",
      formula: "F = MS_Treatment / MS_Error   |   CRD Error df = N − t   |   RBD Error df = (t − 1)(r − 1)"
    };
  });

  /* ---- 5.7 Herd Sampling Simulator & Veterinary DBMS/Excel Lab ---- */
  registerRenderer("sampling_excel", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var mode = env.cfg.submode || st.params.mode || "sampling";

    if (mode === "excel") {
      var fnName = st.params.formula || "AVERAGE";
      var vals = [14.2, 16.8, 15.5, 18.1, 13.9, 17.4];
      var mn = env.math.mean(vals), sd = env.math.sd(vals, true);
      var outVal = fnName === "AVERAGE" ? mn.toFixed(2) + " L" :
        (fnName === "STDEV.S" ? sd.toFixed(2) + " L" :
        (fnName === "TTEST" ? "p = 0.032 (*)" : "p = 0.418 (NS)"));
      var syntax = fnName === "AVERAGE" ? "=AVERAGE(B2:B7)" :
        (fnName === "STDEV.S" ? "=STDEV.S(B2:B7)" :
        (fnName === "TTEST" ? "=T.TEST(B2:B7, C2:C7, 2, 2)" : "=CHISQ.TEST(B2:B3, C2:C3)"));

      // Draw Excel-like spreadsheet grid on canvas
      var padX = 24, padY = 38;
      var cols = ["Cow ID (A)", "Yield L (B)", "Control L (C)", "Breed (D)"];
      var rows = [
        ["IVRI-101", "14.2", "12.5", "Sahiwal"],
        ["IVRI-102", "16.8", "13.1", "Sahiwal"],
        ["IVRI-103", "15.5", "14.0", "Vrindavani"],
        ["IVRI-104", "18.1", "13.8", "Vrindavani"],
        ["IVRI-105", "13.9", "12.9", "Tharparkar"],
        ["IVRI-106", "17.4", "14.2", "Vrindavani"]
      ];
      var cw = (w - padX * 2) / 4, rh = 34;

      // Formula bar
      ctx.fillStyle = P.surface2;
      env.roundRect(ctx, padX, 12, w - padX * 2, 32, 6); ctx.fill();
      ctx.strokeStyle = P.borderStrong; ctx.lineWidth = 1.2; ctx.stroke();
      ctx.fillStyle = P.blue; ctx.font = "700 13px " + P.fontMono; ctx.textAlign = "left";
      ctx.fillText("fx   " + syntax + "   →   " + outVal, padX + 12, 33);

      // Header row
      var y0 = padY + 18;
      for (var c = 0; c < 4; c++) {
        ctx.fillStyle = P.blueLight;
        ctx.fillRect(padX + c * cw, y0, cw, rh);
        ctx.strokeStyle = P.borderStrong; ctx.strokeRect(padX + c * cw, y0, cw, rh);
        ctx.fillStyle = P.text; ctx.font = "700 13px " + P.fontSans; ctx.textAlign = "center";
        ctx.fillText(cols[c], padX + c * cw + cw / 2, y0 + 22);
      }
      // Data rows
      for (var r = 0; r < rows.length; r++) {
        for (var c2 = 0; c2 < 4; c2++) {
          var isSel = c2 === 1 || (c2 === 2 && (fnName === "TTEST" || fnName === "CHISQ.TEST"));
          ctx.fillStyle = isSel ? P.tealLight : P.surface;
          ctx.fillRect(padX + c2 * cw, y0 + (r + 1) * rh, cw, rh);
          ctx.strokeStyle = P.border; ctx.strokeRect(padX + c2 * cw, y0 + (r + 1) * rh, cw, rh);
          ctx.fillStyle = P.text; ctx.font = (c2 === 1 || c2 === 2 ? "600 13px " + P.fontMono : "500 13px " + P.fontSans);
          ctx.fillText(rows[r][c2], padX + c2 * cw + cw / 2, y0 + (r + 1) * rh + 22);
        }
      }

      return {
        readouts: [
          { label: "Active Formula", value: syntax, tone: "accent" },
          { label: "Computed Result", value: outVal, tone: "ok" },
          { label: "Primary Key (DBMS)", value: "Cow_ID", tone: "purple" },
          { label: "Sample Size (n)", value: "6 cows", tone: "teal" }
        ],
        insight: "In veterinary herd management, <b>DBMS tables</b> store each animal with a unique <b>Primary Key (Cow_ID)</b> to avoid duplicate records. In <b>MS-Excel</b>, <code>" + syntax + "</code> computes live statistics without manual rounding errors.",
        formula: "SQL: SELECT Breed, AVG(Yield) FROM Herd GROUP BY Breed;   |   Excel: " + syntax
      };
    }

    // Herd Sampling Simulator (40 animals in 4 breed strata / sheds)
    var method = st.params.method || "srs";
    var colsN = 8, rowsN = 5;
    var selected = {};
    if (method === "srs") {
      [2, 7, 11, 16, 21, 27, 33, 38].forEach(function (i) { selected[i] = true; });
    } else if (method === "stratified") {
      // 2 from each of 4 breed strata (columns 0-1, 2-3, 4-5, 6-7)
      [1, 17, 10, 26, 4, 29, 14, 39].forEach(function (i) { selected[i] = true; });
    } else if (method === "systematic") {
      // Every k = 5th animal starting from random start r = 2
      for (var s = 2; s < 40; s += 5) selected[s] = true;
    } else {
      // Cluster: entire Shed 2 (columns 2-3, all 10 animals)
      for (var r2 = 0; r2 < rowsN; r2++) { selected[r2 * colsN + 2] = true; selected[r2 * colsN + 3] = true; }
    }

    var pad = { l: 28, r: 28, t: 48, b: 36 };
    var cw2 = (w - pad.l - pad.r) / colsN;
    var ch2 = (h - pad.t - pad.b) / rowsN;
    var strataCols = [P.blue, P.teal, P.purple, P.amberFill];
    var strataNames = ["Shed 1 (Sahiwal)", "Shed 2 (Gir)", "Shed 3 (Murrah)", "Shed 4 (Crossbred)"];

    for (var stIdx = 0; stIdx < 4; stIdx++) {
      var sx0 = pad.l + stIdx * 2 * cw2;
      ctx.fillStyle = strataCols[stIdx];
      ctx.globalAlpha = 0.1;
      env.roundRect(ctx, sx0 + 2, pad.t - 26, cw2 * 2 - 4, h - pad.t - pad.b + 30, 8);
      ctx.fill();
      ctx.globalAlpha = 1;
      ctx.fillStyle = strataCols[stIdx];
      ctx.font = "700 12px " + P.fontSans;
      ctx.textAlign = "center";
      ctx.fillText(strataNames[stIdx], sx0 + cw2, pad.t - 10);
    }

    var selCount = 0;
    for (var idx = 0; idx < 40; idx++) {
      var rr = Math.floor(idx / colsN), cc = idx % colsN;
      var cx = pad.l + cc * cw2 + cw2 / 2;
      var cy = pad.t + rr * ch2 + ch2 / 2;
      var isSel2 = !!selected[idx];
      if (isSel2) selCount++;
      ctx.beginPath();
      ctx.arc(cx, cy, isSel2 ? 14 : 10, 0, Math.PI * 2);
      ctx.fillStyle = isSel2 ? P.coral : P.surface2;
      ctx.fill();
      ctx.strokeStyle = isSel2 ? P.coral : P.borderStrong;
      ctx.lineWidth = isSel2 ? 2.5 : 1.5;
      ctx.stroke();
      ctx.fillStyle = isSel2 ? P.textInvert : P.textMuted;
      ctx.font = "700 11px " + P.fontMono;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(String(idx + 1), cx, cy);
    }
    ctx.textBaseline = "alphabetic";

    var descMap = {
      srs: "<b>Simple Random Sampling (SRS):</b> Every animal in the N = 40 herd has an equal chance (1/N) of selection. Best for homogeneous herds.",
      stratified: "<b>Stratified Random Sampling:</b> Herd is divided into homogeneous breed strata (Sahiwal, Gir, Murrah, Crossbred) and sampled proportionally — guarantees representation of every breed and minimizes sampling error!",
      systematic: "<b>Systematic Sampling:</b> Pick a random start (Animal #3) and select every k-th animal (k = N/n = 5: #3, #8, #13, #18…). Fast in field vaccination/serosurveys.",
      cluster: "<b>Cluster Sampling:</b> Randomly select an entire shed/village (Shed 2) and test all animals inside it. Cuts field travel cost in large veterinary surveys."
    };

    return {
      readouts: [
        { label: "Sampling Method", value: method.toUpperCase(), tone: "accent" },
        { label: "Population (N)", value: "40 animals", tone: "teal" },
        { label: "Sample Size (n)", value: selCount + " sampled", tone: "purple" },
        { label: "Sampling Interval (k)", value: method === "systematic" ? "k = N/n = 5" : "N/A" }
      ],
      insight: descMap[method],
      formula: "SRS: P = n/N   |   Systematic: k = N / n   |   Stratified: nᵢ = n · (Nᵢ / N)"
    };
  });

  /* ---- 5.8 Mendelian, Modified Mendelian & Epistasis Cross Simulator ---- */
  registerRenderer("mendelian_epistasis", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var cross = st.params.cross || env.cfg.defaultCross || "mono";

    var presets = {
      mono: {
        name: "Monohybrid Cross (Aa × Aa — Polled vs Horned Cattle)",
        ratio: "3 : 1",
        bars: [{ lbl: "Polled (P_)", n: 3, col: P.blue }, { lbl: "Horned (pp)", n: 1, col: P.coral }],
        grid: [["", "P", "p"], ["P", "PP (Polled)", "Pp (Polled)"], ["p", "Pp (Polled)", "pp (Horned)"]],
        insight: "<b>Mendel's Law of Segregation:</b> Heterozygote × Heterozygote (Pp × Pp) gives phenotypic ratio <b>3 Polled : 1 Horned</b> and genotypic ratio <b>1 PP : 2 Pp : 1 pp</b>."
      },
      test: {
        name: "Monohybrid Test Cross (Pp × pp)",
        ratio: "1 : 1",
        bars: [{ lbl: "Polled (Pp)", n: 1, col: P.blue }, { lbl: "Horned (pp)", n: 1, col: P.coral }],
        grid: [["", "p", "p"], ["P", "Pp (Polled)", "Pp (Polled)"], ["p", "pp (Horned)", "pp (Horned)"]],
        insight: "<b>Test Cross:</b> Crossing a phenotypically dominant animal with a homozygous recessive (pp) reveals whether it is homozygous (100% dominant) or heterozygous (<b>1:1 ratio</b>)."
      },
      incomplete: {
        name: "Incomplete Dominance — Andalusian Fowl (Bb × Bb)",
        ratio: "1 : 2 : 1",
        bars: [{ lbl: "Black (BB)", n: 1, col: P.text }, { lbl: "Blue (Bb)", n: 2, col: P.blue }, { lbl: "White (bb)", n: 1, col: P.textFaint }],
        grid: [["", "B", "b"], ["B", "BB (Black)", "Bb (Andalusian Blue)"], ["b", "Bb (Andalusian Blue)", "bb (Splash White)"]],
        insight: "<b>Incomplete Dominance:</b> Heterozygote (Bb) shows an intermediate phenotype (Andalusian Blue). Phenotypic and genotypic ratios are identical: <b>1 : 2 : 1</b>."
      },
      codom: {
        name: "Codominance — Shorthorn Cattle Coat (RR × WW → F2)",
        ratio: "1 : 2 : 1",
        bars: [{ lbl: "Red (RR)", n: 1, col: P.coral }, { lbl: "Roan (RW)", n: 2, col: P.purple }, { lbl: "White (WW)", n: 1, col: P.textFaint }],
        grid: [["", "R", "W"], ["R", "RR (Red)", "RW (Roan — Both expressed)"], ["W", "RW (Roan — Both expressed)", "WW (White)"]],
        insight: "<b>Codominance:</b> Both alleles express equally and independently in heterozygotes (Roan Shorthorn cattle have distinct red AND white hairs; also seen in ABO/cattle blood groups). Ratio = <b>1 : 2 : 1</b>."
      },
      lethal: {
        name: "Recessive Lethal — Dexter Bulldog Calf / Creeper Fowl (Dd × Dd)",
        ratio: "2 : 1 (Living)",
        bars: [{ lbl: "Bulldog (DD — Lethal)", n: 1, col: P.danger }, { lbl: "Dexter (Dd — Short-leg)", n: 2, col: P.amberFill }, { lbl: "Kerry (dd — Normal)", n: 1, col: P.sage }],
        grid: [["", "D", "d"], ["D", "DD (Bulldog — LETHAL)", "Dd (Dexter)"], ["d", "Dd (Dexter)", "dd (Normal Kerry)"]],
        insight: "<b>Lethal Gene Modification:</b> Homozygous DD calves die in utero (achondroplastic Bulldog calf). Among living progeny, the classic 1:2:1 ratio collapses to <b>2 Dexter : 1 Normal</b>!"
      },
      dihybrid: {
        name: "Dihybrid Independent Assortment (PpBb × PpBb)",
        ratio: "9 : 3 : 3 : 1",
        bars: [{ lbl: "Polled Black (9)", n: 9, col: P.blue }, { lbl: "Polled Red (3)", n: 3, col: P.coral }, { lbl: "Horned Black (3)", n: 3, col: P.teal }, { lbl: "Horned Red (1)", n: 1, col: P.amberFill }],
        grid: [["", "PB", "Pb", "pB", "pb"], ["PB", "PPBB", "PPBb", "PpBB", "PpBb"], ["Pb", "PPBb", "PPbb", "PpBb", "Ppbb"], ["pB", "PpBB", "PpBb", "ppBB", "ppBb"], ["pb", "PpBb", "Ppbb", "ppBb", "ppbb"]],
        insight: "<b>Law of Independent Assortment:</b> Two unlinked genes assort independently to yield the canonical <b>9 : 3 : 3 : 1</b> phenotypic ratio (4 phenotypes, 9 genotypes)."
      },
      epi_rec: {
        name: "Recessive Epistasis — Labrador Coat Color (BbEe × BbEe)",
        ratio: "9 : 3 : 4",
        bars: [{ lbl: "Black (B_E_)", n: 9, col: P.text }, { lbl: "Chocolate (bbE_)", n: 3, col: P.amber }, { lbl: "Yellow (B_ee + bbee)", n: 4, col: P.amberFill }],
        grid: [["Genotype", "Count / 16", "Coat Phenotype", "Mechanism"], ["B_E_", "9", "Black", "E allows eumelanin; B = black"], ["bbE_", "3", "Chocolate", "E allows eumelanin; bb = brown"], ["B_ee / bbee", "3 + 1 = 4", "Yellow", "ee masks B/b locus (epistatic)!"]],
        insight: "<b>Recessive Epistasis (9:3:4):</b> Homozygous recessive <b>ee</b> prevents eumelanin deposition in hair regardless of B/b, merging the 3 B_ee and 1 bbee classes into <b>4 Yellow</b> Labradors!"
      },
      epi_dom: {
        name: "Dominant Epistasis (12 : 3 : 1 — Coat/Plumage Inhibitor)",
        ratio: "12 : 3 : 1",
        bars: [{ lbl: "White (I_C_ + I_cc)", n: 12, col: P.textFaint }, { lbl: "Colored Dom (iiC_)", n: 3, col: P.blue }, { lbl: "Colored Rec (iicc)", n: 1, col: P.coral }],
        grid: [["Genotype", "Count / 16", "Phenotype"], ["I_C_ & I_cc", "9 + 3 = 12", "White (Dominant I masks C/c)"], ["iiC_", "3", "Pigmented Type 1"], ["iicc", "1", "Pigmented Type 2"]],
        insight: "<b>Dominant Epistasis (12:3:1):</b> A single dominant allele (<b>I_</b>) masks expression of the second gene, collapsing 9 + 3 into <b>12</b>."
      },
      epi_comp: {
        name: "Complementary Gene Action (9 : 7 — White Leghorn × Silkie)",
        ratio: "9 : 7",
        bars: [{ lbl: "Colored (C_P_)", n: 9, col: P.purple }, { lbl: "White (C_pp + ccP_ + ccpp)", n: 7, col: P.textFaint }],
        grid: [["Genotype", "Count / 16", "Phenotype"], ["C_P_", "9", "Colored (Both dominant enzymes present)"], ["C_pp / ccP_ / ccpp", "3 + 3 + 1 = 7", "White (Pathway blocked)"]],
        insight: "<b>Complementary Genes (9:7):</b> Both dominant genes (C_ AND P_) are required in a biochemical pathway to produce pigment. Missing either gives white (3+3+1 = <b>7</b>)."
      },
      epi_dup: {
        name: "Duplicate Dominant Epistasis (15 : 1 — Feathered Shanks)",
        ratio: "15 : 1",
        bars: [{ lbl: "Feathered (F1_ or F2_)", n: 15, col: P.teal }, { lbl: "Unfeathered (f1f1 f2f2)", n: 1, col: P.coral }],
        grid: [["Genotype", "Count / 16", "Phenotype"], ["F1_F2_, F1_f2f2, f1f1F2_", "9 + 3 + 3 = 15", "Feathered shanks (Either dominant suffices)"], ["f1f1 f2f2", "1", "Clean / Unfeathered shanks"]],
        insight: "<b>Duplicate Genes (15:1):</b> Either dominant gene alone produces the dominant trait; only the double recessive (1/16) shows the alternative phenotype."
      },
      comb: {
        name: "Comb Shape in Poultry (RrPp × RrPp — Bateson & Punnett)",
        ratio: "9 : 3 : 3 : 1",
        bars: [{ lbl: "Walnut (R_P_)", n: 9, col: P.coral }, { lbl: "Rose (R_pp)", n: 3, col: P.blue }, { lbl: "Pea (rrP_)", n: 3, col: P.teal }, { lbl: "Single (rrpp)", n: 1, col: P.purple }],
        grid: [["Genotype", "Count / 16", "Comb Phenotype", "Breed Example"], ["R_P_", "9", "Walnut", "Malay"], ["R_pp", "3", "Rose", "Wyandotte"], ["rrP_", "3", "Pea", "Brahma"], ["rrpp", "1", "Single", "White Leghorn"]],
        insight: "<b>Novel Phenotype Interaction (9:3:3:1):</b> Rose (R_pp) × Pea (rrP_) produces 100% <b>Walnut (RrPp)</b> in F1, and <b>9 Walnut : 3 Rose : 3 Pea : 1 Single</b> in F2!"
      }
    };

    var pr = presets[cross] || presets.mono;
    var total = pr.bars.reduce(function (s, b) { return s + b.n; }, 0);
    var pad = { l: 52, r: 28, t: 44, b: 64 };
    env.drawAxes(ctx, pad, w, h, P, pr.name, "Proportion (%)");

    var plotW = w - pad.l - pad.r, plotH = h - pad.t - pad.b;
    var bw = Math.min(110, (plotW / pr.bars.length) * 0.62);
    pr.bars.forEach(function (b, i) {
      var frac = b.n / total;
      var cx = pad.l + ((i + 0.5) / pr.bars.length) * plotW;
      var bh = frac * plotH * 0.92;
      ctx.fillStyle = b.col;
      env.roundRect(ctx, cx - bw / 2, h - pad.b - bh, bw, bh, 8);
      ctx.fill();
      ctx.fillStyle = P.text; ctx.font = "700 14px " + P.fontMono; ctx.textAlign = "center";
      ctx.fillText(b.n + "/" + total + " (" + (frac * 100).toFixed(1) + "%)", cx, h - pad.b - bh - 10);
      ctx.fillStyle = P.textMuted; ctx.font = "600 12px " + P.fontSans;
      ctx.fillText(b.lbl, cx, h - pad.b + 20);
    });

    var bench = '<table class="sim-table"><thead><tr>' + pr.grid[0].map(function (hd) { return '<th>' + hd + '</th>'; }).join("") + '</tr></thead><tbody>' +
      pr.grid.slice(1).map(function (row) {
        return '<tr>' + row.map(function (cell, ci) { return '<td' + (ci === 0 ? ' style="font-weight:700;"' : '') + '>' + cell + '</td>'; }).join("") + '</tr>';
      }).join("") + '</tbody></table>';

    return {
      readouts: [
        { label: "Phenotypic Ratio", value: pr.ratio, tone: "accent" },
        { label: "Phenotype Classes", value: String(pr.bars.length), tone: "teal" },
        { label: "Total Parts", value: String(total), tone: "purple" }
      ],
      bench: bench,
      insight: pr.insight,
      formula: "F2 Phenotypic Ratio = " + pr.ratio + "   |   Verify deviation with Chi-Square χ² = Σ(O−E)²/E"
    };
  });

  /* ---- 5.9 Hardy-Weinberg Equilibrium & Forces Changing Gene Frequency ---- */
  registerRenderer("hardy_weinberg", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var p0 = st.params.p0 != null ? st.params.p0 : 0.6;
    var sel = st.params.s != null ? st.params.s : 0.0;       // selection against aa
    var mig = st.params.m != null ? st.params.m : 0.0;       // migration rate from p_m = 0.1
    var mut = st.params.mu != null ? st.params.mu : 0.0;     // forward mutation A->a
    var ne = Math.round(st.params.ne != null ? st.params.ne : 500);
    var gens = 40;

    // Deterministic trajectory
    var pHist = [p0], p = p0;
    for (var g = 1; g <= gens; g++) {
      // 1. Mutation A->a
      p = p * (1 - mut);
      // 2. Migration from donor herd with p_m = 0.15
      p = p * (1 - mig) + mig * 0.15;
      // 3. Selection against recessive aa (fitness: AA=1, Aa=1, aa=1-s)
      var q = 1 - p;
      var wBar = 1 - sel * q * q;
      if (wBar > 0.001) p = (p * p + p * q) / wBar;
      p = Math.max(0, Math.min(1, p));
      pHist.push(p);
    }

    // Drift trajectories when Ne < 200 (seeded deterministic pseudo-random for crisp visual)
    var driftLines = [];
    if (ne < 250) {
      for (var rep = 0; rep < 3; rep++) {
        var dp = p0, arr = [dp], seed = 137 * (rep + 1) + ne;
        for (var g2 = 1; g2 <= gens; g2++) {
          seed = (seed * 16807) % 2147483647;
          var u = (seed / 2147483647) - 0.5;
          var sdDrift = Math.sqrt((dp * (1 - dp)) / (2 * ne));
          dp = Math.max(0, Math.min(1, dp + u * sdDrift * 3.1));
          arr.push(dp);
        }
        driftLines.push(arr);
      }
    }

    var pad = { l: 56, r: 28, t: 36, b: 52 };
    env.drawAxes(ctx, pad, w, h, P, "Generations (0 to " + gens + ")", "Frequency (0.0 to 1.0)");
    function sx(g) { return pad.l + (g / gens) * (w - pad.l - pad.r); }
    function sy(v) { return h - pad.b - v * (h - pad.t - pad.b); }

    // Grid lines at 0.25, 0.5, 0.75, 1.0
    ctx.strokeStyle = P.border; ctx.lineWidth = 1;
    [0.25, 0.5, 0.75, 1.0].forEach(function (lv) {
      ctx.beginPath(); ctx.moveTo(pad.l, sy(lv)); ctx.lineTo(w - pad.r, sy(lv)); ctx.stroke();
      ctx.fillStyle = P.textMuted; ctx.font = "600 12px " + P.fontMono; ctx.textAlign = "right";
      ctx.fillText(lv.toFixed(2), pad.l - 8, sy(lv) + 4);
    });

    // Plot drift replicate lines if small Ne
    driftLines.forEach(function (dl) {
      ctx.beginPath();
      dl.forEach(function (v, idx) { if (idx === 0) ctx.moveTo(sx(idx), sy(v)); else ctx.lineTo(sx(idx), sy(v)); });
      ctx.strokeStyle = P.amberFill; ctx.lineWidth = 1.6; ctx.globalAlpha = 0.7; ctx.stroke();
      ctx.globalAlpha = 1;
    });

    // Plot p, p^2, 2pq, q^2
    function plotSeries(fn, col, dash) {
      ctx.save();
      if (dash) ctx.setLineDash(dash);
      ctx.beginPath();
      pHist.forEach(function (pv, idx) {
        var yv = fn(pv);
        if (idx === 0) ctx.moveTo(sx(idx), sy(yv)); else ctx.lineTo(sx(idx), sy(yv));
      });
      ctx.strokeStyle = col; ctx.lineWidth = dash ? 2 : 3; ctx.stroke();
      ctx.restore();
    }
    plotSeries(function (pv) { return pv; }, P.blue);
    plotSeries(function (pv) { return pv * pv; }, P.teal, [6, 4]);
    plotSeries(function (pv) { return 2 * pv * (1 - pv); }, P.purple, [4, 4]);
    plotSeries(function (pv) { return (1 - pv) * (1 - pv); }, P.coral, [2, 3]);

    // Legend
    var leg = [["p (Allele A)", P.blue], ["p² (AA)", P.teal], ["2pq (Aa)", P.purple], ["q² (aa)", P.coral]];
    leg.forEach(function (item, idx) {
      var lx = pad.l + 14 + idx * 125;
      ctx.fillStyle = item[1]; ctx.fillRect(lx, 12, 12, 12);
      ctx.fillStyle = P.text; ctx.font = "700 12px " + P.fontSans; ctx.textAlign = "left";
      ctx.fillText(item[0], lx + 16, 22);
    });

    var pEnd = pHist[gens], qEnd = 1 - pEnd;
    var inEq = sel === 0 && mig === 0 && mut === 0 && ne >= 250;
    return {
      readouts: [
        { label: "Final p / q (Gen 40)", value: pEnd.toFixed(3) + " / " + qEnd.toFixed(3), tone: "accent" },
        { label: "AA (p²)", value: (pEnd * pEnd * 100).toFixed(1) + "%", tone: "teal" },
        { label: "Aa (2pq)", value: (2 * pEnd * qEnd * 100).toFixed(1) + "%", tone: "purple" },
        { label: "aa (q²)", value: (qEnd * qEnd * 100).toFixed(1) + "%", tone: "danger" }
      ],
      insight: inEq
        ? "<b>Hardy-Weinberg Equilibrium Held!</b> With zero selection, migration, or mutation in a large random-mating population (Nₑ = " + ne + "), allele frequencies (p = " + p0.toFixed(2) + ", q = " + (1 - p0).toFixed(2) + ") and genotype frequencies (p², 2pq, q²) remain strictly constant across all generations. Note: Heterozygotes (2pq) peak at <b>50% when p = q = 0.5</b>!"
        : "<b>Equilibrium Disrupted!</b> " + (sel > 0 ? "Selection (s=" + sel.toFixed(2) + ") against recessive aa increases p, but elimination slows dramatically when q becomes small because most 'a' alleles hide in Aa carriers! " : "") + (ne < 250 ? "Small Nₑ (" + ne + ") triggers <b>Random Genetic Drift</b> (amber trajectories), causing unpredictable fixation or loss of alleles!" : ""),
      formula: "p + q = 1   |   p² + 2pq + q² = 1   |   Δq_sel = −s·p·q² / (1 − s·q²)   |   σ²_drift = pq / (2Nₑ)"
    };
  });

  /* ---- 5.10 Quantitative Genetics, Variance Partitioning & G×E ---- */
  registerRenderer("quant_variance", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var mode = st.params.mode || env.cfg.defaultMode || "variance";
    var pad = { l: 56, r: 28, t: 38, b: 54 };

    if (mode === "polygenic") {
      var loci = Math.round(st.params.loci != null ? st.params.loci : 3);
      var envBlur = st.params.envBlur != null ? st.params.envBlur : 0.35;
      var alleles = 2 * loci;
      var probs = [], maxP = 0;
      for (var k = 0; k <= alleles; k++) {
        var pr = env.math.binomialPMF(alleles, k, 0.5);
        probs.push(pr);
        if (pr > maxP) maxP = pr;
      }
      env.drawAxes(ctx, pad, w, h, P, "Additive Allele Dose (" + loci + " Polygenic Loci → " + (alleles + 1) + " Genotypic Classes)", "Frequency");
      var plotW = w - pad.l - pad.r, plotH = h - pad.t - pad.b;
      var bw = Math.max(10, (plotW / (alleles + 1)) * 0.72);
      for (var i = 0; i <= alleles; i++) {
        var bx = pad.l + ((i + 0.5) / (alleles + 1)) * plotW - bw / 2;
        var bh = (probs[i] / (maxP * 1.18)) * plotH;
        ctx.fillStyle = P.blueLight; ctx.strokeStyle = P.blue; ctx.lineWidth = 2;
        env.roundRect(ctx, bx, h - pad.b - bh, bw, bh, 4); ctx.fill(); ctx.stroke();
      }
      // Continuous phenotypic curve when environment blurs discrete classes
      if (envBlur > 0.05) {
        var mu = alleles / 2, sig = Math.sqrt(alleles * 0.25 + envBlur * envBlur * 2.5);
        var peak = env.math.normalPDF(mu, mu, sig);
        ctx.beginPath();
        for (var j = 0; j <= 140; j++) {
          var xv = (alleles * j) / 140;
          var px = pad.l + ((xv + 0.5) / (alleles + 1)) * plotW;
          var py = h - pad.b - (env.math.normalPDF(xv, mu, sig) / (peak * 1.12)) * plotH;
          if (j === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.strokeStyle = P.coral; ctx.lineWidth = 3; ctx.stroke();
      }
      return {
        readouts: [
          { label: "Polygenic Loci (n)", value: String(loci), tone: "accent" },
          { label: "Phenotype Classes (2n+1)", value: String(alleles + 1), tone: "teal" },
          { label: "Extreme Ratio (1/4ⁿ)", value: "1 / " + Math.pow(4, loci), tone: "purple" }
        ],
        insight: "As the number of additive genes increases from <b>1 locus (3 classes)</b> to <b>5 loci (11 classes)</b> and environmental variation blurs boundaries, discrete Mendelian bars merge into a smooth <b>continuous bell curve</b> (milk yield, body weight, fleece weight)!",
        formula: "Classes = 2n + 1   |   P = G + E   |   Quantitative traits follow continuous Normal distribution"
      };
    }

    if (mode === "gxe") {
      var gxe = st.params.gxe != null ? st.params.gxe : 1.0; // 0 = parallel, 1 = rank crossing
      env.drawAxes(ctx, pad, w, h, P, "Production Environment (Temperate Intensive  →  Tropical Field)", "Lactation Milk Yield (kg)");
      var x1 = pad.l + (w - pad.l - pad.r) * 0.22;
      var x2 = pad.l + (w - pad.l - pad.r) * 0.78;
      var hfTemp = 6800, hfTrop = Math.round(6200 - gxe * 4000);
      var sahTemp = 2600, sahTrop = Math.round(2100 + gxe * 900);
      function sy(v) { return h - pad.b - ((v - 1000) / 6500) * (h - pad.t - pad.b); }

      // Holstein line
      ctx.strokeStyle = P.blue; ctx.lineWidth = 3.5;
      ctx.beginPath(); ctx.moveTo(x1, sy(hfTemp)); ctx.lineTo(x2, sy(hfTrop)); ctx.stroke();
      // Sahiwal line
      ctx.strokeStyle = P.coral; ctx.lineWidth = 3.5;
      ctx.beginPath(); ctx.moveTo(x1, sy(sahTemp)); ctx.lineTo(x2, sy(sahTrop)); ctx.stroke();

      [[x1, hfTemp, P.blue, "Holstein: " + hfTemp + " kg"], [x2, hfTrop, P.blue, "Holstein: " + hfTrop + " kg"],
       [x1, sahTemp, P.coral, "Sahiwal: " + sahTemp + " kg"], [x2, sahTrop, P.coral, "Sahiwal: " + sahTrop + " kg"]].forEach(function (pt) {
        ctx.beginPath(); ctx.arc(pt[0], sy(pt[1]), 7, 0, Math.PI * 2);
        ctx.fillStyle = pt[2]; ctx.fill();
        ctx.fillStyle = pt[2]; ctx.font = "700 13px " + P.fontSans; ctx.textAlign = "center";
        ctx.fillText(pt[3], pt[0], sy(pt[1]) - 12);
      });

      var rankFlip = hfTrop < sahTrop;
      return {
        readouts: [
          { label: "Temperate Winner", value: "Holstein Friesian", tone: "accent" },
          { label: "Tropical Winner", value: rankFlip ? "Sahiwal (Rank Flip!)" : "Holstein (No Flip)", tone: rankFlip ? "danger" : "ok" },
          { label: "G × E Type", value: rankFlip ? "Re-ranking (Crossover)" : (gxe > 0.25 ? "Scale Interaction" : "No G × E (Parallel)"), tone: "purple" }
        ],
        insight: rankFlip
          ? "<b>Crossover G × E Interaction!</b> The lines cross: Holstein dominates in temperate farms (6800 kg), but heat stress and tropical diseases crash its yield below heat-tolerant <b>Sahiwal</b> in tropical India — proving why sires must be tested in the target environment!"
          : "<b>Parallel Lines = Zero G × E:</b> Both breeds shift by the same amount across environments, so ranking stays identical. Slide G × E Strength right to see rank reversal!",
        formula: "P = μ + G + E + (G × E)   |   V_P = V_G + V_E + V_GE + 2·Cov(G, E)"
      };
    }

    // Variance Partitioning (V_A, V_D, V_I, V_Ep, V_Et)
    var va = st.params.va != null ? st.params.va : 30;
    var vd = st.params.vd != null ? st.params.vd : 12;
    var vi = st.params.vi != null ? st.params.vi : 6;
    var vep = st.params.vep != null ? st.params.vep : 14;
    var vet = st.params.vet != null ? st.params.vet : 38;
    var vp = va + vd + vi + vep + vet || 1;
    var vg = va + vd + vi;
    var h2 = va / vp, H2 = vg / vp, rep = (vg + vep) / vp;

    // Stacked horizontal variance bar + 3 comparison bars (h², H², r)
    var barX = 48, barW = w - 96, barY = 58, barH = 54;
    ctx.fillStyle = P.text; ctx.font = "700 14px " + P.fontSans; ctx.textAlign = "left";
    ctx.fillText("Total Phenotypic Variance (V_P = " + vp.toFixed(0) + ") Partitioned into Genetic & Environmental Components", barX, 34);

    var segs = [
      { lbl: "V_A", val: va, col: P.blue },
      { lbl: "V_D", val: vd, col: P.purple },
      { lbl: "V_I", val: vi, col: P.teal },
      { lbl: "V_Ep", val: vep, col: P.amberFill },
      { lbl: "V_Et", val: vet, col: P.textFaint }
    ];
    var curX = barX;
    segs.forEach(function (s) {
      var sw = (s.val / vp) * barW;
      if (sw > 1) {
        ctx.fillStyle = s.col;
        ctx.fillRect(curX, barY, sw, barH);
        if (sw > 38) {
          ctx.fillStyle = P.textInvert; ctx.font = "700 12px " + P.fontMono; ctx.textAlign = "center";
          ctx.fillText(s.lbl + " " + Math.round((s.val / vp) * 100) + "%", curX + sw / 2, barY + 32);
        }
        curX += sw;
      }
    });

    // Draw h², H², and Repeatability r bars below to prove h² <= H² <= r visually!
    var metrics = [
      { name: "Narrow-Sense Heritability  h² = V_A / V_P", val: h2, col: P.blue },
      { name: "Broad-Sense Heritability   H² = (V_A + V_D + V_I) / V_P", val: H2, col: P.purple },
      { name: "Repeatability              r  = (V_G + V_Ep) / V_P  (Upper Limit of h²)", val: rep, col: P.teal }
    ];
    metrics.forEach(function (mt, idx) {
      var my = 152 + idx * 58;
      ctx.fillStyle = P.text; ctx.font = "700 13px " + P.fontSans; ctx.textAlign = "left";
      ctx.fillText(mt.name, barX, my);
      ctx.fillStyle = P.bgAlt;
      env.roundRect(ctx, barX, my + 8, barW, 24, 6); ctx.fill();
      ctx.fillStyle = mt.col;
      env.roundRect(ctx, barX, my + 8, Math.max(8, mt.val * barW), 24, 6); ctx.fill();
      ctx.fillStyle = P.text; ctx.font = "700 13px " + P.fontMono; ctx.textAlign = "right";
      ctx.fillText(mt.val.toFixed(3) + " (" + (mt.val * 100).toFixed(1) + "%)", barX + barW, my);
    });

    return {
      readouts: [
        { label: "Narrow h² (V_A/V_P)", value: h2.toFixed(2), tone: "accent" },
        { label: "Broad H² (V_G/V_P)", value: H2.toFixed(2), tone: "purple" },
        { label: "Repeatability (r)", value: rep.toFixed(2), tone: "teal" },
        { label: "Rule Verified", value: "h² ≤ H² ≤ r", tone: "ok" }
      ],
      insight: "<b>VCI Board Favourite:</b> Because <b>V_G = V_A + V_D + V_I</b> and Repeatability includes permanent environment (<b>V_Ep</b>), Repeatability <b>r (" + rep.toFixed(2) + ")</b> is ALWAYS the upper limit of Heritability <b>h² (" + h2.toFixed(2) + ")</b>! Only <b>V_A (Additive variance)</b> is transmitted reliably from parent to offspring.",
      formula: "V_P = V_A + V_D + V_I + V_Ep + V_Et   |   h² = V_A / V_P   |   r = (V_G + V_Ep) / V_P"
    };
  });

  /* ---- 5.11 Selection Response (ΔG = h²·S = i·r_IA·σ_A / L) ---- */
  registerRenderer("selection_response", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state, m = env.math;
    var pSel = (st.params.pSel != null ? st.params.pSel : 20) / 100;
    var h2 = st.params.h2 != null ? st.params.h2 : 0.25;
    var sigmaP = st.params.sigmaP != null ? st.params.sigmaP : 500;
    var genL = st.params.L != null ? st.params.L : 5.0;

    var mu = 3000;
    var zCut = m.invNormal(1 - pSel);
    var xCut = mu + zCut * sigmaP;
    var iVal = m.selectionIntensity(pSel);
    var S = iVal * sigmaP;
    var dG = h2 * S;
    var dGyr = dG / Math.max(0.5, genL);

    var pad = { l: 56, r: 28, t: 38, b: 54 };
    var minX = mu - 3.5 * sigmaP, maxX = mu + 3.5 * sigmaP;
    function sx(x) { return pad.l + ((x - minX) / (maxX - minX)) * (w - pad.l - pad.r); }
    var peak = m.normalPDF(mu, mu, sigmaP);
    function sy(y) { return h - pad.b - (y / (peak * 1.18)) * (h - pad.t - pad.b); }

    env.drawAxes(ctx, pad, w, h, P, "Trait Performance (Mean μ = " + mu + " kg, Selected Top " + Math.round(pSel * 100) + "%)", "Density");

    // Shade selected parents tail
    ctx.beginPath();
    ctx.moveTo(sx(xCut), h - pad.b);
    for (var j = 0; j <= 80; j++) {
      var xv = xCut + ((maxX - xCut) * j) / 80;
      ctx.lineTo(sx(xv), sy(m.normalPDF(xv, mu, sigmaP)));
    }
    ctx.lineTo(sx(maxX), h - pad.b);
    ctx.closePath();
    ctx.fillStyle = P.okSoft;
    ctx.fill();

    // Base population curve
    ctx.beginPath();
    for (var k = 0; k <= 150; k++) {
      var xv2 = minX + ((maxX - minX) * k) / 150;
      if (k === 0) ctx.moveTo(sx(xv2), sy(m.normalPDF(xv2, mu, sigmaP)));
      else ctx.lineTo(sx(xv2), sy(m.normalPDF(xv2, mu, sigmaP)));
    }
    ctx.strokeStyle = P.blue; ctx.lineWidth = 3; ctx.stroke();

    // Next-generation shifted offspring curve (dashed teal)
    ctx.save();
    ctx.setLineDash([6, 4]);
    ctx.beginPath();
    for (var k2 = 0; k2 <= 150; k2++) {
      var xv3 = minX + ((maxX - minX) * k2) / 150;
      if (k2 === 0) ctx.moveTo(sx(xv3), sy(m.normalPDF(xv3, mu + dG, sigmaP)));
      else ctx.lineTo(sx(xv3), sy(m.normalPDF(xv3, mu + dG, sigmaP)));
    }
    ctx.strokeStyle = P.teal; ctx.lineWidth = 2.5; ctx.stroke();
    ctx.restore();

    // Truncation line & Mean markers
    ctx.strokeStyle = P.ok; ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(sx(xCut), pad.t + 16); ctx.lineTo(sx(xCut), h - pad.b); ctx.stroke();
    ctx.fillStyle = P.ok; ctx.font = "700 12px " + P.fontSans; ctx.textAlign = "center";
    ctx.fillText("Cutoff (" + Math.round(pSel * 100) + "%)", sx(xCut), pad.t + 12);

    // S arrow
    var xMeanSel = mu + S;
    ctx.strokeStyle = P.coral; ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(sx(mu), pad.t + 36); ctx.lineTo(sx(xMeanSel), pad.t + 36); ctx.stroke();
    ctx.fillStyle = P.coral; ctx.font = "700 12px " + P.fontMono;
    ctx.fillText("S = +" + S.toFixed(0), (sx(mu) + sx(xMeanSel)) / 2, pad.t + 30);

    var traitHint = h2 < 0.15 ? "Low h² (Fertility/Fitness): Individual selection is weak — use Family/Progeny testing!"
      : (h2 < 0.35 ? "Medium h² (Milk Yield ~0.25): Combine Individual + Progeny/BLUP evaluation."
      : "High h² (Fat% / Carcass / Growth ~0.50): Mass/Individual selection gives rapid genetic gain!");

    return {
      readouts: [
        { label: "Intensity (i)", value: iVal.toFixed(3), tone: "accent", sub: "Top " + Math.round(pSel * 100) + "% selected" },
        { label: "Diff. (S = i·σ_P)", value: "+" + S.toFixed(1) + " kg", tone: "purple" },
        { label: "ΔG / Generation", value: "+" + dG.toFixed(1) + " kg", tone: "teal" },
        { label: "ΔG / Year (ΔG/L)", value: "+" + dGyr.toFixed(1) + " kg/yr", tone: "ok", sub: "at L = " + genL.toFixed(1) + " yrs" }
      ],
      insight: "<b>" + traitHint + "</b> Selecting a smaller top % raises intensity <b>i (" + iVal.toFixed(2) + ")</b>, while cutting generation interval <b>L (" + genL.toFixed(1) + " yr)</b> via Genomic Selection/MOET multiplies annual gain <b>ΔG/year</b>!",
      formula: "ΔG = h² · S = i · h² · σ_P   |   ΔG/year = (i · r_IA · σ_A) / L"
    };
  });

  /* ---- 5.12 Multi-Trait Selection Comparator (Tandem vs ICL vs Selection Index) ---- */
  registerRenderer("multi_trait_selection", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var method = st.params.method || "index";
    var pad = { l: 58, r: 28, t: 38, b: 54 };
    env.drawAxes(ctx, pad, w, h, P, "Trait 1: Milk Yield (Std. Units)", "Trait 2: Fat % / Fertility (Std. Units)");

    // Deterministic 80-animal herd
    var herd = [];
    for (var i = 0; i < 80; i++) {
      var a1 = Math.sin(i * 12.9898) * 43758.5453; var u1 = a1 - Math.floor(a1);
      var a2 = Math.sin(i * 78.233 + 1.5) * 43758.5453; var u2 = a2 - Math.floor(a2);
      var x = 10 + u1 * 80, y = 10 + u2 * 80;
      var score = 0.6 * x + 0.4 * y; // True aggregate merit H
      herd.push({ x: x, y: y, score: score });
    }

    function sx(v) { return pad.l + (v / 100) * (w - pad.l - pad.r); }
    function sy(v) { return h - pad.b - (v / 100) * (h - pad.t - pad.b); }

    // Select top 25% (20 animals) under chosen method
    var selSet = [];
    if (method === "tandem") {
      var sortedT = herd.slice().sort(function (a, b) { return b.x - a.x; });
      var cutX = sortedT[19].x;
      ctx.fillStyle = P.okSoft;
      ctx.fillRect(sx(cutX), pad.t, w - pad.r - sx(cutX), h - pad.b - pad.t);
      ctx.strokeStyle = P.ok; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(sx(cutX), pad.t); ctx.lineTo(sx(cutX), h - pad.b); ctx.stroke();
      herd.forEach(function (a) { a.sel = a.x >= cutX; if (a.sel) selSet.push(a); });
    } else if (method === "icl") {
      var cxCut = 52, cyCut = 52;
      ctx.fillStyle = P.okSoft;
      ctx.fillRect(sx(cxCut), pad.t, w - pad.r - sx(cxCut), sy(cyCut) - pad.t);
      ctx.strokeStyle = P.ok; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(sx(cxCut), pad.t); ctx.lineTo(sx(cxCut), sy(cyCut)); ctx.lineTo(w - pad.r, sy(cyCut)); ctx.stroke();
      herd.forEach(function (a) { a.sel = (a.x >= cxCut && a.y >= cyCut); if (a.sel) selSet.push(a); });
    } else {
      // Selection Index: I = 0.6*X1 + 0.4*X2
      var sortedI = herd.slice().sort(function (a, b) { return b.score - a.score; });
      var cutI = sortedI[19].score;
      // Diagonal line 0.6x + 0.4y = cutI => y = (cutI - 0.6x) / 0.4
      var yAt0 = (cutI) / 0.4, yAt100 = (cutI - 60) / 0.4;
      ctx.beginPath();
      ctx.moveTo(sx(0), sy(Math.min(100, yAt0)));
      ctx.lineTo(sx(100), sy(Math.max(0, yAt100)));
      ctx.lineTo(sx(100), pad.t);
      ctx.lineTo(sx(0), pad.t);
      ctx.closePath();
      ctx.fillStyle = P.okSoft; ctx.fill();
      ctx.strokeStyle = P.ok; ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(sx(Math.max(0, (cutI - 40) / 0.6)), sy(100));
      ctx.lineTo(sx(100), sy(Math.max(0, yAt100)));
      ctx.stroke();
      herd.forEach(function (a) { a.sel = a.score >= cutI; if (a.sel) selSet.push(a); });
    }

    // Draw herd points
    herd.forEach(function (a) {
      ctx.beginPath();
      ctx.arc(sx(a.x), sy(a.y), a.sel ? 7 : 5, 0, Math.PI * 2);
      ctx.fillStyle = a.sel ? P.blue : P.textFaint;
      ctx.fill();
      if (a.sel) { ctx.strokeStyle = P.surface; ctx.lineWidth = 1.5; ctx.stroke(); }
    });

    var popH = env.math.mean(herd.map(function (a) { return a.score; }));
    var selH = selSet.length ? env.math.mean(selSet.map(function (a) { return a.score; })) : popH;
    var gainH = selH - popH;

    return {
      readouts: [
        { label: "Method", value: method === "index" ? "Selection Index" : (method === "icl" ? "Indep. Culling" : "Tandem"), tone: "accent" },
        { label: "Animals Selected", value: selSet.length + " / 80", tone: "teal" },
        { label: "Net Merit Gain (ΔH)", value: "+" + gainH.toFixed(1) + " pts", tone: method === "index" ? "ok" : "warn" },
        { label: "Efficiency Rank", value: method === "index" ? "#1 Most Efficient" : (method === "icl" ? "#2 Intermediate" : "#3 Least Efficient"), tone: method === "index" ? "ok" : "purple" }
      ],
      insight: method === "index"
        ? "<b>Selection Index (Hazel & Lush) is ALWAYS Most Efficient!</b> The diagonal index line allows an elite cow in Milk Yield to compensate for slightly average Fat %, capturing the highest aggregate economic gain (<b>ΔH = +" + gainH.toFixed(1) + "</b>)!"
        : (method === "icl"
          ? "<b>Independent Culling Levels (L-shaped cutoff):</b> Any animal failing EITHER cutoff is culled immediately — even a champion milk producer with 0.1% lower fat! Useful when traits are expressed at different ages, but less efficient than Selection Index."
          : "<b>Tandem Selection (Vertical cutoff):</b> Selects for only ONE trait at a time, ignoring Trait 2 completely. Least efficient method — especially if traits are negatively correlated!"),
      formula: "I = b₁X₁ + b₂X₂ + … + bₙXₙ   |   Efficiency: Selection Index > Independent Culling > Tandem"
    };
  });

  /* ---- 5.13 Wright's Inbreeding Coefficient (F_X) & Relationship (R_XY) ---- */
  registerRenderer("pedigree_inbreeding", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var mating = st.params.mating || "fullsib";
    var fAnc = st.params.fA != null ? st.params.fA : 0; // Common ancestor inbreeding F_A

    var presets = {
      selfing: { name: "Self-Fertilization", fBase: 0.5, rBase: 1.0, paths: "1 path (n₁=0, n₂=0)", n1: 0, n2: 0, nPaths: 1,
        nodes: [{ id: "A", x: 0.5, y: 0.22, ca: true }, { id: "X", x: 0.5, y: 0.78, target: true }],
        edges: [["A", "X", -28], ["A", "X", 28]] },
      parent_off: { name: "Parent × Offspring (Sire × Daughter)", fBase: 0.25, rBase: 0.50, paths: "1 path (n₁=0, n₂=1)", n1: 0, n2: 1, nPaths: 1,
        nodes: [{ id: "Sire (A)", x: 0.35, y: 0.22, ca: true }, { id: "Dam", x: 0.72, y: 0.22 }, { id: "Daughter", x: 0.62, y: 0.52 }, { id: "X", x: 0.48, y: 0.82, target: true }],
        edges: [["Sire (A)", "Daughter", 0], ["Dam", "Daughter", 0], ["Sire (A)", "X", 0], ["Daughter", "X", 0]] },
      fullsib: { name: "Full-Sib Mating (Brother × Sister)", fBase: 0.25, rBase: 0.50, paths: "2 paths via Sire A & Dam B (each n₁=1, n₂=1)", n1: 1, n2: 1, nPaths: 2,
        nodes: [{ id: "Sire (A)", x: 0.34, y: 0.18, ca: true }, { id: "Dam (B)", x: 0.66, y: 0.18, ca: true }, { id: "Bro (S)", x: 0.34, y: 0.52 }, { id: "Sis (D)", x: 0.66, y: 0.52 }, { id: "X", x: 0.5, y: 0.84, target: true }],
        edges: [["Sire (A)", "Bro (S)", 0], ["Sire (A)", "Sis (D)", 0], ["Dam (B)", "Bro (S)", 0], ["Dam (B)", "Sis (D)", 0], ["Bro (S)", "X", 0], ["Sis (D)", "X", 0]] },
      halfsib: { name: "Half-Sib Mating (Common Sire A)", fBase: 0.125, rBase: 0.25, paths: "1 path via Common Sire A (n₁=1, n₂=1)", n1: 1, n2: 1, nPaths: 1,
        nodes: [{ id: "Common Sire (A)", x: 0.5, y: 0.18, ca: true }, { id: "Dam 1", x: 0.18, y: 0.18 }, { id: "Dam 2", x: 0.82, y: 0.18 }, { id: "Half-Bro", x: 0.34, y: 0.52 }, { id: "Half-Sis", x: 0.66, y: 0.52 }, { id: "X", x: 0.5, y: 0.84, target: true }],
        edges: [["Common Sire (A)", "Half-Bro", 0], ["Common Sire (A)", "Half-Sis", 0], ["Dam 1", "Half-Bro", 0], ["Dam 2", "Half-Sis", 0], ["Half-Bro", "X", 0], ["Half-Sis", "X", 0]] },
      cousin: { name: "First-Cousin Mating", fBase: 0.0625, rBase: 0.125, paths: "2 paths (each n₁=2, n₂=2)", n1: 2, n2: 2, nPaths: 2,
        nodes: [{ id: "GP1 (A)", x: 0.36, y: 0.14, ca: true }, { id: "GP2 (B)", x: 0.64, y: 0.14, ca: true }, { id: "P1", x: 0.32, y: 0.40 }, { id: "P2", x: 0.68, y: 0.40 }, { id: "Cousin 1", x: 0.32, y: 0.64 }, { id: "Cousin 2", x: 0.68, y: 0.64 }, { id: "X", x: 0.5, y: 0.88, target: true }],
        edges: [["GP1 (A)", "P1", 0], ["GP1 (A)", "P2", 0], ["GP2 (B)", "P1", 0], ["GP2 (B)", "P2", 0], ["P1", "Cousin 1", 0], ["P2", "Cousin 2", 0], ["Cousin 1", "X", 0], ["Cousin 2", "X", 0]] }
    };

    var pr = presets[mating] || presets.fullsib;
    var fX = pr.nPaths * Math.pow(0.5, pr.n1 + pr.n2 + 1) * (1 + fAnc);
    var rSD = pr.rBase * (1 + fAnc);
    var nodeMap = {};
    pr.nodes.forEach(function (nd) { nodeMap[nd.id] = { x: nd.x * w, y: nd.y * h, ca: nd.ca, target: nd.target, id: nd.id }; });

    // Draw edges
    pr.edges.forEach(function (ed) {
      var a = nodeMap[ed[0]], b = nodeMap[ed[1]];
      var isPath = a.ca || b.target || (!a.ca && !b.target);
      ctx.strokeStyle = (a.ca || b.target) ? P.blue : P.borderStrong;
      ctx.lineWidth = (a.ca || b.target) ? 3 : 2;
      ctx.beginPath();
      if (ed[2]) {
        ctx.moveTo(a.x, a.y);
        ctx.quadraticCurveTo((a.x + b.x) / 2 + ed[2] * 2, (a.y + b.y) / 2, b.x, b.y);
      } else {
        ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y);
      }
      ctx.stroke();
    });

    // Draw nodes
    pr.nodes.forEach(function (nd) {
      var p = nodeMap[nd.id];
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.target ? 24 : (p.ca ? 22 : 19), 0, Math.PI * 2);
      ctx.fillStyle = p.target ? P.coral : (p.ca ? P.blue : P.surface2);
      ctx.fill();
      ctx.strokeStyle = p.target ? P.coral : (p.ca ? P.blueDark : P.borderStrong);
      ctx.lineWidth = 2.5; ctx.stroke();
      ctx.fillStyle = (p.target || p.ca) ? P.textInvert : P.text;
      ctx.font = "700 12px " + P.fontSans; ctx.textAlign = "center"; ctx.textBaseline = "middle";
      ctx.fillText(nd.id, p.x, p.y);
    });
    ctx.textBaseline = "alphabetic";

    return {
      readouts: [
        { label: "Inbreeding (F_X)", value: (fX * 100).toFixed(2) + "% (" + fX.toFixed(4) + ")", tone: fX >= 0.25 ? "danger" : "warn" },
        { label: "Relationship (R_SD)", value: (rSD * 100).toFixed(1) + "%", tone: "accent" },
        { label: "Wright's Path Count", value: pr.paths, tone: "purple" },
        { label: "Heterozygosity Loss", value: "−" + (fX * 100).toFixed(1) + "%", tone: "danger" }
      ],
      insight: "<b>" + pr.name + ":</b> " + pr.paths + ". Using Wright's formula, <b>F_X = " + (fX * 100).toFixed(2) + "%</b>. Inbreeding increases homozygosity and exposes lethal/deleterious recessives, causing <b>Inbreeding Depression</b> — most severe in <b>low-h² fitness &amp; fertility traits</b> (conception rate, calf survival, litter size)!",
      formula: "F_X = Σ [ (½)^(n₁ + n₂ + 1) · (1 + F_A) ]   |   F_X = ½ · R_SD (for non-inbred parents)"
    };
  });

  /* ---- 5.14 Outbreeding, Grading-Up & Heterosis (H%) Lab ---- */
  registerRenderer("crossbreeding_heterosis", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var mode = st.params.mode || env.cfg.defaultMode || "grading";
    var pad = { l: 56, r: 28, t: 40, b: 54 };

    if (mode === "grading") {
      var gens = Math.round(st.params.gens != null ? st.params.gens : 7);
      env.drawAxes(ctx, pad, w, h, P, "Backcross Generation (Non-descript × Purebred Murrah/Sahiwal Sire)", "Exotic / Purebred Inheritance (%)");
      var plotW = w - pad.l - pad.r, plotH = h - pad.t - pad.b;
      var bw = Math.min(64, (plotW / gens) * 0.65);

      for (var g = 1; g <= gens; g++) {
        var exotic = (1 - Math.pow(0.5, g)) * 100;
        var cx = pad.l + ((g - 0.5) / gens) * plotW;
        var bh = (exotic / 100) * plotH;
        // Nondescript portion on top
        ctx.fillStyle = P.bgAlt;
        ctx.fillRect(cx - bw / 2, pad.t, bw, plotH - bh);
        // Purebred portion
        ctx.fillStyle = P.blue;
        env.roundRect(ctx, cx - bw / 2, h - pad.b - bh, bw, bh, 4);
        ctx.fill();
        ctx.fillStyle = P.text; ctx.font = "700 12px " + P.fontMono; ctx.textAlign = "center";
        ctx.fillText(exotic.toFixed(1) + "%", cx, h - pad.b - bh - 8);
        ctx.fillStyle = P.textMuted; ctx.font = "700 12px " + P.fontSans;
        ctx.fillText("G" + g, cx, h - pad.b + 20);
      }

      var curExotic = (1 - Math.pow(0.5, gens)) * 100;
      return {
        readouts: [
          { label: "Generation", value: "G" + gens, tone: "accent" },
          { label: "Purebred Inheritance", value: curExotic.toFixed(2) + "%", tone: "ok" },
          { label: "Nondescript Remaining", value: (100 - curExotic).toFixed(2) + "%", tone: "warn" },
          { label: "Purebred Status", value: gens >= 7 ? "Achieved (≥99.2%)" : "In Progress", tone: gens >= 7 ? "ok" : "purple" }
        ],
        insight: "<b>Grading-Up Progression:</b> Continuous backcrossing of non-descript females to purebred sires (e.g., Murrah buffalo or Sahiwal bulls) replaces half the remaining non-descript genes every generation: <b>50% → 75% → 87.5% → 93.75% → 96.88% → 98.44% → 99.22%</b>. After <b>7–8 generations</b>, animals are phenotypically purebred!",
        formula: "Purebred % in Gen n = [ 1 − (½)ⁿ ] × 100"
      };
    }

    // Crossbreeding & Heterosis Comparator
    var pA = st.params.pA != null ? st.params.pA : 2200;
    var pB = st.params.pB != null ? st.params.pB : 4200;
    var f1 = st.params.f1 != null ? st.params.f1 : 3680;
    var pMid = (pA + pB) / 2;
    var hPct = ((f1 - pMid) / pMid) * 100;

    var systems = [
      { lbl: "2-Breed F1", ret: 100, col: P.blue },
      { lbl: "3-Breed Terminal", ret: 100, col: P.teal },
      { lbl: "Crisscross (2-Br)", ret: 66.7, col: P.purple },
      { lbl: "3-Breed Rotation", ret: 85.7, col: P.sage },
      { lbl: "Synthetic (2-Br)", ret: 50.0, col: P.amberFill }
    ];
    env.drawAxes(ctx, pad, w, h, P, "Crossbreeding System", "Retained Individual Heterosis (%)");
    var pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
    var sw = Math.min(82, (pw / systems.length) * 0.62);
    systems.forEach(function (sys, i) {
      var cx = pad.l + ((i + 0.5) / systems.length) * pw;
      var bh = (sys.ret / 110) * ph;
      ctx.fillStyle = sys.col;
      env.roundRect(ctx, cx - sw / 2, h - pad.b - bh, sw, bh, 6); ctx.fill();
      ctx.fillStyle = P.text; ctx.font = "700 13px " + P.fontMono; ctx.textAlign = "center";
      ctx.fillText(sys.ret.toFixed(1) + "%", cx, h - pad.b - bh - 8);
      ctx.fillStyle = P.textMuted; ctx.font = "600 11px " + P.fontSans;
      ctx.fillText(sys.lbl, cx, h - pad.b + 20);
    });

    return {
      readouts: [
        { label: "Mid-Parent (P̄)", value: pMid.toFixed(0) + " kg", tone: "accent" },
        { label: "F1 Mean (F̄₁)", value: f1.toFixed(0) + " kg", tone: "teal" },
        { label: "Heterosis (H%)", value: (hPct >= 0 ? "+" : "") + hPct.toFixed(2) + "%", tone: hPct > 0 ? "ok" : "danger" },
        { label: "Crisscross / 3-Rot", value: "66.7% / 85.7%", tone: "purple" }
      ],
      insight: "<b>Heterosis (Hybrid Vigour):</b> F1 (" + f1 + " kg) exceeds mid-parent mean (" + pMid + " kg) by <b>+" + hPct.toFixed(1) + "%</b> due to dominance &amp; overdominance masking deleterious recessives. Retained heterosis at equilibrium: <b>2-breed Crisscrossing = 66.7%</b>, <b>3-breed Rotational = 85.7%</b>, and <b>n-breed Synthetic = (n−1)/n</b>!",
      formula: "H% = [ (F̄₁ − P̄) / P̄ ] × 100   |   Rotational Retained H = (2ⁿ − 2) / (2ⁿ − 1)"
    };
  });

  /* ---- 5.15 Sire Evaluation (Contemporary Comparison & BLUP) & Genomic Selection ---- */
  registerRenderer("sire_blup_onbs", function (env) {
    var ctx = env.ctx, w = env.w, h = env.h, P = env.P, st = env.state;
    var method = st.params.method || "blup";
    var nDau = Math.round(st.params.nDau != null ? st.params.nDau : 40);
    var h2 = 0.25;
    var k = (4 - h2) / h2; // k = 15 for h2 = 0.25
    var wFactor = nDau / (nDau + k);

    // 3 Sires: Sire A in elite herd (4200 kg), Sire B in average herd (3000 kg), Sire C in poor herd (2200 kg)
    var sires = [
      { name: "Bull A (Elite Herd)", dauAvg: 4350, herdAvg: 4200, col: P.amberFill },
      { name: "Bull B (Avg Herd)", dauAvg: 3450, herdAvg: 3000, col: P.blue },
      { name: "Bull C (Poor Herd)", dauAvg: 2900, herdAvg: 2200, col: P.teal }
    ];
    var breedAvg = 3133;
    sires.forEach(function (s) {
      s.dev = s.dauAvg - s.herdAvg;
      s.cc = breedAvg + 2 * wFactor * s.dev; // Sire Breeding Value via CC / BLUP adjustment
      s.score = method === "raw" ? s.dauAvg : s.cc;
    });
    var ranked = sires.slice().sort(function (a, b) { return b.score - a.score; });

    var pad = { l: 58, r: 28, t: 44, b: 56 };
    env.drawAxes(ctx, pad, w, h, P, method === "raw" ? "Raw Daughter Average (Biased by Herd Environment!)" : "BLUP / Contemporary Comparison Breeding Value (Adjusted for Herd)", "Estimated Merit (kg)");
    var pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
    var bw = Math.min(96, (pw / 3) * 0.56);

    sires.forEach(function (s, idx) {
      var cx = pad.l + ((idx + 0.5) / 3) * pw;
      var bh = ((s.score - 1500) / 3500) * ph;
      ctx.fillStyle = s.col;
      env.roundRect(ctx, cx - bw / 2, h - pad.b - Math.max(20, bh), bw, Math.max(20, bh), 8);
      ctx.fill();
      ctx.fillStyle = P.text; ctx.font = "700 13px " + P.fontMono; ctx.textAlign = "center";
      ctx.fillText(Math.round(s.score) + " kg", cx, h - pad.b - Math.max(20, bh) - 10);
      ctx.fillStyle = P.textMuted; ctx.font = "600 12px " + P.fontSans;
      ctx.fillText(s.name, cx, h - pad.b + 20);
    });

    var acc = Math.sqrt((nDau * h2) / (4 + (nDau - 1) * h2));
    var bench = '<table class="sim-table"><thead><tr><th>Sire</th><th>Daughter Avg</th><th>Herd-Year-Season Avg</th><th>Deviation (D − H)</th><th>BLUP / CC BV</th></tr></thead><tbody>' +
      sires.map(function (s) {
        return '<tr><td><b>' + s.name + '</b></td><td class="sim-num">' + s.dauAvg + '</td><td class="sim-num">' + s.herdAvg + '</td><td class="sim-num">+' + s.dev + '</td><td class="sim-num sim-highlight">' + Math.round(s.cc) + ' kg</td></tr>';
      }).join("") + '</tbody></table>';

    return {
      readouts: [
        { label: "#1 Ranked Sire", value: ranked[0].name.split(" ")[0] + " " + ranked[0].name.split(" ")[1], tone: "ok" },
        { label: "Reg. Weight (n/(n+k))", value: wFactor.toFixed(2), tone: "accent", sub: "k = (4−h²)/h² = 15" },
        { label: "Progeny Accuracy (r_IA)", value: (acc * 100).toFixed(1) + "%", tone: "purple", sub: "n = " + nDau + " daughters" }
      ],
      bench: bench,
      insight: method === "raw"
        ? "<b>Trap of Raw Daughter Average!</b> Bull A looks #1 (4350 kg) ONLY because his daughters live in an elite herd (4200 kg, +150 kg above contemporaries), while <b>Bull C (+700 kg above herd!)</b> looks worst! Switch to <b>BLUP / Contemporary Comparison</b> to remove herd bias."
        : "<b>BLUP / Contemporary Comparison Reveals the True Champion!</b> After adjusting for Herd-Year-Season fixed effects, <b>Bull C (+700 kg superiority)</b> jumps from #3 to <b>#1</b>! With Genomic Selection (SNP chips), bulls are evaluated at birth, slashing generation interval L from 6+ years to ~2 years!",
      formula: "EBV = μ + [ 2n / (n + k) ] · (D̄ − H̄)   |   k = (4 − h²) / h²   |   BLUP: y = Xb + Zu + e"
    };
  });

  return {
    registerRenderer: registerRenderer,
    registerTopic: registerTopic,
    registerTopics: registerTopics,
    mount: mount,
    unmount: unmount,
    math: math,
    getPalette: getPalette
  };
})();
