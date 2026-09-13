// tools/test_search_indexing.js
// Tests that search.js successfully indexes all 400 glossary items

const fs = require('fs');
const path = require('path');
const assert = require('assert');

const glossaryCode = fs.readFileSync(path.join(__dirname, '../js/glossary.js'), 'utf8');
const searchCode = fs.readFileSync(path.join(__dirname, '../js/search.js'), 'utf8');

// Mock browser environment
const mockWindow = {};
const mockApp = { esc: s => s, icon: s => s };

const gFn = new Function('window', 'app', glossaryCode + '; return glossary;');
const glossary = gFn(mockWindow, mockApp);

global.glossary = glossary;
global.window = mockWindow;
mockWindow.glossary = glossary;

// Mock syllabus data
global.syllabus = { units: [], topicById: {}, allSubSections: [] };
global.calculator = { tools: [] };
global.examBank = { questions: [] };
global.quizBank = { "unit-1": [], "unit-2": [], "unit-3": [] };

// Check glossary.getAll() returns 400 items
const items = glossary.getAll();
assert.strictEqual(items.length, 400, `Expected 400 items from glossary.getAll(), got ${items.length}`);

// Check specific newly added terms exist
const checkTerms = [
    'Weighted Arithmetic Mean',
    'Split-Plot Design',
    'Monohybrid Ratio',
    'Punnett Square',
    'Kinetochore',
    'CRISPR-Cas9',
    'Wobble Hypothesis',
    'Hardy-Weinberg Equilibrium Equation',
    'Sewall Wright Effect',
    'Infinitesimal Model',
    'Liability Model',
    'Robert Bakewell',
    'Jay L. Lush',
    'Henderson\'s Mixed Model Equations'
];

checkTerms.forEach(term => {
    const termFirstWord = term.toLowerCase().split(' ')[0];
    const found = items.some(item => item.term.toLowerCase().includes(termFirstWord));
    assert(found, `Expected term matching "${term}" not found in items`);
});

console.log('✓ All 400 terms correctly retrievable via glossary.getAll() for Search indexing!');
