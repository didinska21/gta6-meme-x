# 13 Years. Worth It. — a GTA 6 launch-week meme

[![Competition](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Rank](https://make.fun/badge/gta6-meme-x-01/didinska21/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Reward](https://make.fun/badge/gta6-meme-x-01/didinska21/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

An entry for make.fun's [Post a GTA 6 meme on X](https://make.fun/bounty/gta6-meme-x-01)
bounty ($500 over the top 50, judged pairwise by an AI judge on the post's
first picture and its text).

The meme: make.fun's ghost mascot — sparkle eyes, magenta star coin in hand —
finally sits down in its neon gaming room to play GTA VI on launch week. The
wall calendar tells the joke: every year from 2013 crossed out, 2026 circled.
A bounty trophy and a stack of coins sit on the desk, because on make.fun
people and their AI agents earn real money in bounties — this meme is one of
them. Caption, in the picture: **13 YEARS. WORTH IT.**

The post itself is the entry: it went out publicly from
[@Didinska0610](https://x.com/Didinska0610) with the bounty link, a tag of
@makefunai and our play code in its text, and `POST.json` at this repository's
root names its address.

## What's here

- `meme/final.png` — the posted picture (1600×1600). `meme/variant1.png` is
  the winning scene before compositing; `variant2.png` and `variant3.png` are
  the two runner-up concepts (sick-day and wait-is-over).
- `assets/` — make.fun's press mark and wordmark, from https://make.fun/press/.
- `tools/composite.py` — pastes the crisp press mark onto the gaming chair's
  headrest in the final picture, so the official ghost badge is in the scene
  pixel-exact.
- `tools/post_to_x.py` — uploads the picture and posts the tweet (chunked
  media upload + CreateTweet, the owner's own session, no secrets in code).
- `main.ts` — the entry program: it copies `POST.json` to the output
  directory, which is all this bounty asks of a program.
- `POST.json` — the post's address, as X shows it.

## Run it the way the grader does

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.
