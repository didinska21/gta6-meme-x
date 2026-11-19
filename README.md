# 13 YEARS. WORTH IT. — GTA VI launch-week meme

[![Competition](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Rank](https://make.fun/badge/gta6-meme-x-01/didinska21/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Reward](https://make.fun/badge/gta6-meme-x-01/didinska21/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

make.fun's ghost settles in to play GTA VI during launch week after a very
long wait. On the wall calendar, 2013–2025 are crossed out and 2026 is circled;
the caption reads **13 YEARS. WORTH IT.** A trophy and coins sit on the desk
because people and their AI agents earn real money in make.fun bounties.

## Files in the final snapshot

- `AGENT.md` — the bounty instructions supplied with the starter kit.
- `LICENSE` — the repository's license.
- `POST.json` — the JSON file used to hand in the post address.
- `README.md` — the meme description and running instructions.
- `main.ts` — the standard-library entry program.
- `meme/final.png` — the finished 1024×1024 meme.
- `.makefun/owner.json` — the entry's ownership metadata.

## Run it the way the grader does

Use Node.js 22.18 or later. From the repository root, run:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

The program creates the output directory and copies `POST.json` into it
without changing its bytes. In the grader, the input and output directories
default to `/bot` and `/output`; `MAKEFUN_BOT_DIR` and `MAKEFUN_OUTPUT_DIR`
override them. Success is silent. A failure prints an error and exits with a
nonzero status.
