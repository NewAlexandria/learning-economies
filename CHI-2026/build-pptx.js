#!/usr/bin/env node
/**
 * Build CHI 2026 slides as .pptx using the Anthropic pptx skill (html2pptx).
 * Requires: npm install pptxgenjs playwright sharp
 * Run from repo root: node CHI-2026/build-pptx.js
 * Or from CHI-2026: node build-pptx.js
 */

const path = require('path');
const pptxgen = require('pptxgenjs');

const CHI_DIR = path.resolve(__dirname);
const SKILL_HTML2PPTX = path.join(CHI_DIR, '..', 'skills', 'pptx', 'scripts', 'html2pptx.js');
const SLIDES_DIR = path.join(CHI_DIR, 'pptx-slides');
const BUILD_DIR = path.join(CHI_DIR, 'build');
const OUTPUT_FILE = path.join(BUILD_DIR, 'chi-2026-slides-skill.pptx');

const SLIDE_FILES = [
  '01-title.html',
  '02-problem.html',
  '03-contribution.html',
  '04-five-economies.html',
  '05-resonance.html',
  '06-llm-architecture.html',
  '07-reflective-loop.html',
  '08-metrics.html',
  '09-design.html',
  '10-scope.html',
  '11-limitations.html',
  '12-takeaway.html',
  '13-thankyou.html'
];

const fs = require('fs');

async function main() {
  if (!fs.existsSync(BUILD_DIR)) fs.mkdirSync(BUILD_DIR, { recursive: true });
  const html2pptx = require(SKILL_HTML2PPTX);
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'CHI 2026 Tools for Thought Workshop';
  pptx.title = 'Learning Economies: A Framework for Measuring Cognitive Outcomes in AI-Augmented Learning';

  for (const file of SLIDE_FILES) {
    const htmlPath = path.join(SLIDES_DIR, file);
    await html2pptx(htmlPath, pptx);
  }

  await pptx.writeFile({ fileName: OUTPUT_FILE });
  console.log('Written:', OUTPUT_FILE);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
