// Checks that every math span in the solution Markdown renders with KaTeX in strict mode.
// Usage: npm ci, then: node render_check.js [FILE]   (FILE defaults to ../problem-set-01-solution.md)
const fs = require('fs');
const path = require('path');
const katex = require('katex');

const file = process.argv[2] || path.join(__dirname, '..', 'problem-set-01-solution.md');
const src = fs.readFileSync(file, 'utf8');

// Display math: $$ ... $$ (may span lines)
const displays = [...src.matchAll(/\$\$([\s\S]*?)\$\$/g)].map(m => m[1].trim());
// Inline math: $...$ on a single line, excluding the display blocks
const noDisplay = src.replace(/\$\$[\s\S]*?\$\$/g, '');
const inlines = [...noDisplay.matchAll(/\$([^$\n]+?)\$/g)].map(m => m[1]);

let ok = true, count = 0;
const tryRender = (tex, displayMode) => {
  count++;
  try {
    katex.renderToString(tex, { displayMode, throwOnError: true, strict: 'error' });
  } catch (e) {
    ok = false;
    console.log(`FAIL (${displayMode ? 'display' : 'inline'}): ${tex}\n  -> ${e.message}`);
  }
};
displays.forEach(t => tryRender(t, true));
inlines.forEach(t => tryRender(t, false));
console.log(`rendered ${displays.length} display + ${inlines.length} inline math spans; ${ok ? 'ALL OK' : 'ERRORS FOUND'}`);
process.exit(ok ? 0 : 1);
