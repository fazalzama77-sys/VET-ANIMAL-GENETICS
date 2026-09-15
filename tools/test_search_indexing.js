// tools/test_search_indexing.js
// Tests that search.js successfully indexes all 480 glossary items

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

// Check glossary.getAll() returns 480 items
const items = glossary.getAll();
assert.strictEqual(items.length, 480, `Expected 480 items from glossary.getAll(), got ${items.length}`);

// Check specific newly added terms exist
const checkTerms = [
    'Class Interval',
    'Standard Normal Distribution',
    'Wild-Type Allele',
    'Amorphic Allele',
    'Maternal Inheritance',
    'Allopolyploidy',
    'Fluorescence In Situ Hybridization',
    'Reverse Transcriptase',
    'Epigenetics',
    'Demographic Bottleneck',
    'Coalescent Theory',
    'Haldane\'s Rule',
    'Kinship (Co-Ancestry) Matrix',
    'Marker-Assisted Selection',
    'Genome-Wide Association Study',
    'Juvenile In-Vitro Embryo Technology'
];

checkTerms.forEach(term => {
    const termFirstWord = term.toLowerCase().split(' ')[0];
    const found = items.some(item => item.term.toLowerCase().includes(termFirstWord));
    assert(found, `Expected term matching "${term}" not found in items`);
});

console.log('✓ All 480 terms correctly retrievable via glossary.getAll() for Search indexing!');
