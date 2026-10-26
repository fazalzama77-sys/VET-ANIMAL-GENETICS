/**
 * tools/update_data_js_with_images.js
 * Cleanly updates data-theory-unit1.JS, data-theory-unit2.JS, data-theory-unit3.JS,
 * and data-practical.JS with the real Wikimedia Commons images and captions.
 */
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const BASE_DIR = path.resolve(__dirname, "..");
const mapPath = path.join(__dirname, "image_updates_map.json");
const updates = JSON.parse(fs.readFileSync(mapPath, "utf8"));

// 1. Update Theory Units 1, 2, 3
[1, 2, 3].forEach((unitNo) => {
  const filePath = path.join(BASE_DIR, "data", `data-theory-unit${unitNo}.JS`);
  const code = fs.readFileSync(filePath, "utf8");
  const ctx = { window: {} };
  vm.createContext(ctx);
  vm.runInContext(code, ctx);

  const unitKey = `unit-${unitNo}`;
  const unitData = ctx.theoryData[unitKey];
  let count = 0;

  Object.keys(unitData).forEach((tid) => {
    if (updates.theory[tid]) {
      unitData[tid].img = updates.theory[tid].img;
      unitData[tid].imgCaption = updates.theory[tid].caption;
      count++;
    }
  });

  const outJs =
    `var theoryData = (typeof theoryData !== 'undefined') ? theoryData : ((typeof window !== 'undefined' && window.theoryData) ? window.theoryData : {});\n` +
    `if (typeof window !== 'undefined') window.theoryData = theoryData;\n\n` +
    `theoryData["${unitKey}"] = ` +
    JSON.stringify(unitData, null, 2) +
    `;\n`;

  fs.writeFileSync(filePath, outJs, "utf8");
  console.log(`Updated ${filePath} (${count} topics)`);
});

// 2. Update Practical Units 1, 2, 3 in data-practical.JS
const pracPath = path.join(BASE_DIR, "data", "data-practical.JS");
const pracCode = fs.readFileSync(pracPath, "utf8");
const pCtx = { window: {} };
vm.createContext(pCtx);
vm.runInContext(pracCode, pCtx);

let pracCount = 0;
["prac-unit-1", "prac-unit-2", "prac-unit-3"].forEach((pKey) => {
  const pData = pCtx.practicalData[pKey];
  if (!pData) return;
  Object.keys(pData).forEach((ptid) => {
    if (updates.practical[ptid]) {
      pData[ptid].img = updates.practical[ptid].img;
      pData[ptid].imgCaption = updates.practical[ptid].caption;
      pracCount++;
    }
  });
});

const outPracJs =
  `var practicalData = (typeof practicalData !== 'undefined') ? practicalData : ((typeof window !== 'undefined' && window.practicalData) ? window.practicalData : {});\n` +
  `if (typeof window !== 'undefined') window.practicalData = practicalData;\n\n` +
  `practicalData["prac-unit-1"] = ` +
  JSON.stringify(pCtx.practicalData["prac-unit-1"], null, 2) +
  `;\n\n` +
  `practicalData["prac-unit-2"] = ` +
  JSON.stringify(pCtx.practicalData["prac-unit-2"], null, 2) +
  `;\n\n` +
  `practicalData["prac-unit-3"] = ` +
  JSON.stringify(pCtx.practicalData["prac-unit-3"], null, 2) +
  `;\n`;

fs.writeFileSync(pracPath, outPracJs, "utf8");
console.log(`Updated ${pracPath} (${pracCount} practical topics)`);
