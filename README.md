# TinyChess CRC32 Book + PVS Depth-4

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/KembangPasir-dot/tiny-chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/KembangPasir-dot/tiny-chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4KB Python chess engine for the [tiny-chess-01 bounty on make.fun](https://make.fun/bounty/tiny-chess-01): a 180-entry CRC32 opening book (1,800 B) + tapered PeSTO evaluation + PVS search to depth 4 with a 100,000-node cap. Practice trials on the submitted bytes: 1,099 / 1,099 / 1,279 Elo, mean 1,159.

`main.py` is the whole engine (3,205 B, Python 3.13 stdlib only, fixed depth and node count, never a clock). `source.py` is its readable source, packed by the official `makefun compress`.
