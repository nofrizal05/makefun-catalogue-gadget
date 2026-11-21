"""The Catalogue Photo of an Impossible Gadget.

make.fun competition the-catalogue-photo-of-an-2-20261121-0341: a catalogue
photograph of an impossible gadget — here, the SOLARLUX solar torch, a
flashlight that only works in daylight, photographed switched on in bright
sunshine with a pair of sunglasses as its one accessory.

The finished image is shipped in this repository as entry.png. This program
copies it to the output directory and verifies the copy byte for byte, so
the graded artifact is exactly the image that was made and checked locally.

Python standard library only — os, shutil, pathlib, hashlib, sys — because
the grading sandbox runs Python 3.13 with nothing installed.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHIPPED = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def sha256_of(path):
    """SHA-256 hex digest of a file, streamed in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not SHIPPED.is_file():
        print("error: shipped entry.png is missing from the repository",
              file=sys.stderr)
        return 1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SHIPPED, destination)
    if sha256_of(SHIPPED) != sha256_of(destination):
        print("error: copied entry.png differs from the shipped entry.png",
              file=sys.stderr)
        return 1
    print("wrote", destination, "sha256:", sha256_of(destination))
    return 0


if __name__ == "__main__":
    sys.exit(main())
