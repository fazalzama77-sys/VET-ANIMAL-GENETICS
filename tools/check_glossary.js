const fs = require('fs');
const path = require('path');

const glossaryContent = fs.readFileSync(path.join(__dirname, '../js/glossary.js'), 'utf8');

const mockWindow = {};
const mockApp = { esc: s => s, icon: s => s };
const fn = new Function('window', 'app', glossaryContent + '; return glossary;');
const glossary = fn(mockWindow, mockApp);

const existingKeys = Object.keys(glossary.terms);
console.log('Existing terms in js/glossary.js:', existingKeys.length);

console.log('Category breakdown:');
for (const [cat, keys] of Object.entries(glossary.categories)) {
    console.log(`  ${cat}: ${keys.length} items`);
}

const { execSync } = require('child_process');
const pyScript = `
import sys, os, json
sys.path.insert(0, r"${path.join(__dirname).replace(/\\/g, '\\\\')}")
from expand_glossary import NEW_TERMS
print(json.dumps(list(NEW_TERMS.keys())))
`;
fs.writeFileSync(path.join(__dirname, 'dump_keys.py'), pyScript, 'utf8');
const newKeys = JSON.parse(execSync('python tools/dump_keys.py', { cwd: path.join(__dirname, '..') }).toString());
fs.unlinkSync(path.join(__dirname, 'dump_keys.py'));

console.log('New terms in expand_glossary.py:', newKeys.length);

const existingSet = new Set(existingKeys.map(k => k.toLowerCase()));
const overlap = newKeys.filter(k => existingSet.has(k.toLowerCase()));
console.log('Overlapping keys count:', overlap.length);
console.log('Overlapping keys:', overlap);
