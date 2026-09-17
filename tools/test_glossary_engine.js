// tools/test_glossary_engine.js
// Automated verification suite for the 540-term Animal Genetics & Breeding Glossary

const fs = require('fs');
const path = require('path');
const assert = require('assert');

console.log('🧪 Starting Glossary Engine Test Suite (540 Terms Target)...\n');

const filesToTest = [
    { name: 'js/glossary.js', path: path.join(__dirname, '../js/glossary.js') },
    { name: 'repo/js/glossary.js', path: path.join(__dirname, '../repo/js/glossary.js') }
];

const EXPECTED_COUNTS = {
    "Biostatistics & Experimental Design": 90,
    "Classical & Mendelian Genetics": 90,
    "Cytogenetics & Molecular Genetics": 95,
    "Population Genetics": 75,
    "Quantitative Genetics & Inheritance": 90,
    "Animal Breeding & Selection Systems": 100
};

filesToTest.forEach(({ name, path: filePath }) => {
    console.log(`[TEST] Testing ${name}...`);
    assert(fs.existsSync(filePath), `File does not exist: ${filePath}`);

    const code = fs.readFileSync(filePath, 'utf8');

    // Test syntax and evaluation
    const mockWindow = {};
    const mockApp = { esc: s => s, icon: s => s };
    let glossary;
    try {
        const fn = new Function('window', 'app', code + '; return glossary;');
        glossary = fn(mockWindow, mockApp);
    } catch (err) {
        console.error(`❌ Syntax/evaluation error in ${name}:`, err);
        process.exit(1);
    }

    assert(glossary, `${name}: glossary object not exported`);
    assert(glossary.categories, `${name}: categories missing`);
    assert(glossary.terms, `${name}: terms missing`);

    // 1. Total unique terms count
    const termKeys = Object.keys(glossary.terms);
    console.log(`  ✓ Total terms in glossary.terms: ${termKeys.length}`);
    assert.strictEqual(termKeys.length, 540, `Expected 540 terms, found ${termKeys.length}`);

    // 2. Categories count and mapping
    const categoryNames = Object.keys(glossary.categories);
    assert.strictEqual(categoryNames.length, 6, `Expected 6 categories, found ${categoryNames.length}`);

    let totalKeysInCategories = 0;
    const seenCategoryKeys = new Set();

    categoryNames.forEach(cat => {
        const keys = glossary.categories[cat];
        assert(Array.isArray(keys), `Category ${cat} is not an array`);
        const expectedCount = EXPECTED_COUNTS[cat];
        assert.strictEqual(keys.length, expectedCount, `Category "${cat}" expected ${expectedCount} terms, found ${keys.length}`);
        console.log(`  ✓ Category "${cat}": ${keys.length} terms (matches expected ${expectedCount})`);
        totalKeysInCategories += keys.length;

        keys.forEach(k => {
            assert(!seenCategoryKeys.has(k), `Duplicate key "${k}" across categories`);
            seenCategoryKeys.add(k);

            // Verify entry exists in terms
            assert(glossary.terms[k], `Category key "${k}" has no entry in glossary.terms`);
            assert.strictEqual(glossary.terms[k].category, cat, `Term "${k}" category mismatch: expected "${cat}", found "${glossary.terms[k].category}"`);
        });
    });

    assert.strictEqual(totalKeysInCategories, 540, `Expected 540 keys across categories, found ${totalKeysInCategories}`);

    // 3. Every term in terms has valid definition and term
    termKeys.forEach(k => {
        const entry = glossary.terms[k];
        assert(entry.term && entry.term.trim().length > 0, `Term "${k}" missing display term`);
        assert(entry.category && entry.category.trim().length > 0, `Term "${k}" missing category`);
        assert(entry.def && entry.def.trim().length > 10, `Term "${k}" definition is too short or missing`);
        assert(seenCategoryKeys.has(k), `Term "${k}" is in terms but not in any category list`);
    });

    // 4. Test getAll() method
    assert(typeof glossary.getAll === 'function', 'getAll method missing');
    const all = glossary.getAll();
    assert(Array.isArray(all), 'getAll() must return an array');
    assert.strictEqual(all.length, 540, `getAll() returned length ${all.length}, expected 540`);
    assert(all[0].key && all[0].term && all[0].category && all[0].def, 'getAll() items missing required fields');
    console.log(`  ✓ getAll() returns ${all.length} complete items`);

    // 5. Test getSortedTerms()
    assert(typeof glossary.getSortedTerms === 'function', 'getSortedTerms method missing');
    const sorted = glossary.getSortedTerms();
    assert.strictEqual(sorted.length, 540, `getSortedTerms() returned length ${sorted.length}, expected 540`);
    for (let i = 0; i < sorted.length - 1; i++) {
        assert(sorted[i].length >= sorted[i + 1].length, `getSortedTerms not sorted descending by length at index ${i}`);
    }
    console.log(`  ✓ getSortedTerms() returned 540 keys sorted longest-first (longest: "${sorted[0]}" [${sorted[0].length} chars])`);

    // 6. Test window.glossary assignment
    assert(mockWindow.glossary === glossary, 'window.glossary was not assigned');
    console.log(`  ✓ window.glossary properly exported\n`);
});

console.log('🎉 ALL 540 GLOSSARY TESTS PASSED PERFECTLY!\n');
