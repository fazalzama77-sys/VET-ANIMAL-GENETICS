const fs = require('fs');
const path = require('path');
const glossaryContent = fs.readFileSync(path.join(__dirname, '../js/glossary.js'), 'utf8');
const fn = new Function('window', 'app', glossaryContent + '; return glossary;');
const glossary = fn({}, { esc: s => s, icon: s => s });

const existingKeys = new Set(Object.keys(glossary.terms).map(k => k.toLowerCase()));

const { execSync } = require('child_process');
const pyScript = `import sys, os, json
sys.path.insert(0, r"${__dirname.replace(/\\/g, '\\\\')}")
from expand_glossary import NEW_TERMS
print(json.dumps(list(NEW_TERMS.keys())))
`;
fs.writeFileSync(path.join(__dirname, 'dump_keys.py'), pyScript, 'utf8');
const newKeys = JSON.parse(execSync('python tools/dump_keys.py', { cwd: path.join(__dirname, '..') }).toString());
fs.unlinkSync(path.join(__dirname, 'dump_keys.py'));

const newSet = new Set(newKeys.map(k => k.toLowerCase()));

const candidates = [
  'threshold trait',
  'individual selection',
  'pedigree index',
  'animal model',
  'sire model',
  'heterobeltiosis',
  'standard heterosis',
  'synthetic breed',
  'grading up ratio',
  'diallel cross',
  'introgression',
  'rotational crossbreeding',
  'terminal crossbreeding',
  'recurrent selection'
];

candidates.forEach(c => {
  console.log(c.padEnd(25), 'in existing:', existingKeys.has(c), '| in NEW_TERMS:', newSet.has(c));
});
