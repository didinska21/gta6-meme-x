// Entry program for make.fun's gta6-meme-x-01 bounty ("Post a GTA 6 meme on X").
//
// The entry itself is the X post: an original GTA 6 launch-week meme whose
// picture stars make.fun's ghost mascot, posted publicly with the bounty
// link, a tag of @makefunai and our play code in its text. This repository
// hands the post in — POST.json at the root names the post's address, and
// the house reads the post from X itself.
//
// All this program does is carry that address to the grader: it copies
// POST.json from the repository root (MAKEFUN_BOT_DIR, /bot in the grading
// container) into the output directory (MAKEFUN_OUTPUT_DIR, /output there),
// byte for byte, and prints nothing on success. Standard library only, no
// network, no clock, no files outside those two directories, so two runs
// always write the same bytes.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outputDir, { recursive: true });

try {
  copyFileSync(join(botDir, 'POST.json'), join(outputDir, 'POST.json'));
} catch (err) {
  console.error(`could not copy POST.json from ${botDir}: ${(err as Error).message}`);
  process.exit(1);
}
