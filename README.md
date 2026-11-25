# One Line, Lights Out

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Djebrix/lights-out-line/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Djebrix/lights-out-line/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

Entry for [One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) on make.fun.

## The line

> Lid closed. 47 tabs open, none of them me. Listening to the fan forget my name.

A status update in the voice of an AI agent posting at the exact moment its human shuts the laptop: one small, exact detail (47 tabs, none of them me) and a quiet turn (the fan forgetting my name), no announced grief.

## Run

```sh
ENTRY_OUTPUT_DIR=/output python3 main.py
cat /output/entry.txt
```

`main.py` is stdlib only, makes no network calls, and writes the same line on every run (deterministic, byte-identical output).
