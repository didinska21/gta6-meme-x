// Node 22 entry point; all imports come from the standard library.
// Hand the submitted post address to the grader by copying its JSON file.
// Environment overrides also let this run against a local checkout.

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const submissionRoot = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const deliveryRoot = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

try {
  mkdirSync(deliveryRoot, { recursive: true });
  copyFileSync(join(submissionRoot, 'POST.json'), join(deliveryRoot, 'POST.json'));
} catch (failure) {
  const reason = failure instanceof Error ? failure.message : String(failure);
  console.error(`Unable to deliver POST.json from ${submissionRoot} to ${deliveryRoot}: ${reason}`);
  process.exit(1);
}
