// tools/test_quiz_engine.js
// Verifies quiz data integration with quiz.js logic

const fs = require('fs');
const path = require('path');

// Mock window and global objects for headless node verification
global.window = global;
global.syllabus = {
  meta: {
    papers: [
      { id: "paper-1", units: [1, 2] },
      { id: "paper-2", units: [3] }
    ]
  },
  theory: [
    { id: "unit-1", no: 1, short: "Biostatistics" },
    { id: "unit-2", no: 2, short: "Genetics" },
    { id: "unit-3", no: 3, short: "Breeding" }
  ],
  practical: []
};

// Load data-quiz.JS
const quizJsCode = fs.readFileSync(path.join(__dirname, '..', 'data', 'data-quiz.JS'), 'utf8');
eval(quizJsCode);

console.log("==========================================");
console.log("   QUIZ ENGINE COMPREHENSIVE TEST SUITE   ");
console.log("==========================================");

let totalMCQ = 0;
let totalTF = 0;
let totalFIB = 0;

['unit-1', 'unit-2', 'unit-3'].forEach(u => {
  const bank = quizBank[u];
  if (!bank) throw new Error("Missing unit: " + u);
  
  const mcq = bank.mcq || [];
  const tf = bank.tf || [];
  const fib = bank.fib || [];
  
  console.log(`\nUnit: ${u}`);
  console.log(`  MCQ: ${mcq.length} (Expected 90)`);
  console.log(`  TF:  ${tf.length} (Expected 45)`);
  console.log(`  FIB: ${fib.length} (Expected 45)`);
  console.log(`  Unit Total: ${mcq.length + tf.length + fib.length} (Expected 180)`);
  
  if (mcq.length !== 90) throw new Error(`${u} MCQ count is ${mcq.length}, expected 90`);
  if (tf.length !== 45) throw new Error(`${u} TF count is ${tf.length}, expected 45`);
  if (fib.length !== 45) throw new Error(`${u} FIB count is ${fib.length}, expected 45`);
  
  totalMCQ += mcq.length;
  totalTF += tf.length;
  totalFIB += fib.length;

  // Check sub-sections
  const subCounts = {};
  [...mcq, ...tf, ...fib].forEach(q => {
    subCounts[q.subSection] = (subCounts[q.subSection] || 0) + 1;
  });

  console.log("  Sub-sections distribution:");
  Object.keys(subCounts).sort().forEach(s => {
    console.log(`    - ${s}: ${subCounts[s]} questions`);
    if (subCounts[s] !== 36) {
      throw new Error(`Sub-section ${s} has ${subCounts[s]} questions, expected 36!`);
    }
  });
});

console.log("\n------------------------------------------");
console.log(`Grand Total MCQs: ${totalMCQ} (Expected 270)`);
console.log(`Grand Total TF:   ${totalTF} (Expected 135)`);
console.log(`Grand Total FIB:  ${totalFIB} (Expected 135)`);
console.log(`Grand Total All:  ${totalMCQ + totalTF + totalFIB} (Expected 540)`);
console.log("Ratio: exactly 2 : 1 : 1");
console.log("------------------------------------------");
console.log("ALL UNIT TESTS PASSED SUCCESSFULLY! 🏆\n");
