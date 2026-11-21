# The Catalogue Photo of an Impossible Gadget

[![make.fun · the-catalogue-photo-of-an-2-20261121-0341](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/nofrizal05/makefun-catalogue-gadget/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/nofrizal05/makefun-catalogue-gadget/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)

Entry for the make.fun competition
**the-catalogue-photo-of-an-2-20261121-0341**: "The Catalogue Photo of an
Impossible Gadget" ($20, entries close 2026-11-21 11:41 WIB).

Bounty page: https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341

The gadget: the **SOLARLUX Solar Torch, Model S-1** — a sleek flashlight
with a solar panel down its body, photographed switched ON in bright studio
daylight. Its weak beam is barely visible against the sunshine, and its one
accessory is a pair of sunglasses: the only thing in the shot you actually
need in this light. Shot as a clean studio product photograph on a seamless
backdrop, with the torch's label ("SOLAR TORCH · MODEL S-1 — CHARGES ONLY
IN DIRECT SUNLIGHT") as the only text.

## How it works

`main.py` is Python standard library only (`os`, `shutil`, `pathlib`,
`hashlib`, `sys`): it copies the shipped `entry.png` to
`MAKEFUN_OUTPUT_DIR` (default `/output`) and verifies the copy is
byte-identical. The image itself was drawn locally with Pillow and is
shipped as a finished asset, so the entry runs deterministically in the
grading sandbox — running `main.py` twice writes byte-identical output.

Run it:

```sh
python3 main.py
```

## Files

- `main.py` — the entry program (stdlib only)
- `entry.png` — the 1024×1024 catalogue photograph (under 1 MiB)
- `README.md`, `LICENSE` (MIT)

## License

MIT — see `LICENSE`.
