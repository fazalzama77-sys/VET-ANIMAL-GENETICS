// tools/check_sync.js
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const rootDir = path.join(__dirname, '..');
const repoDir = path.join(rootDir, 'repo');

function hashFile(p) {
    const buf = fs.readFileSync(p);
    return crypto.createHash('sha256').update(buf).digest('hex');
}

const keyFiles = [
    'js/glossary.js',
    'js/app.js',
    'js/search.js',
    'service-worker.js',
    'data/data-quiz.JS'
];

keyFiles.forEach(rel => {
    const p1 = path.join(rootDir, rel);
    const p2 = path.join(repoDir, rel);
    if (!fs.existsSync(p2)) {
        console.log(`[MISSING IN REPO] ${rel}`);
    } else {
        const h1 = hashFile(p1);
        const h2 = hashFile(p2);
        if (h1 === h2) {
            console.log(`[IN SYNC] ${rel}`);
        } else {
            console.log(`[DIFF] ${rel}`);
        }
    }
});
