#!/usr/bin/env node

import { copyFile, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(scriptDir, '..');
const assets = [
  'new-building-asset-flow.drawio.png',
  'new-building-asset-flow.drawio.svg',
  'new-building-asset-flow.en.drawio.png',
  'new-building-asset-flow.en.drawio.svg',
];

const assetsDir = path.join(repoRoot, 'assets');
const docsPublicDir = path.join(repoRoot, 'docs', 'public');

await mkdir(docsPublicDir, { recursive: true });

for (const fileName of assets) {
  const source = path.join(assetsDir, fileName);
  const target = path.join(docsPublicDir, fileName);
  await copyFile(source, target);
  console.log(`[sync-docs-diagram-assets] ${path.relative(repoRoot, source)} -> ${path.relative(repoRoot, target)}`);
}
