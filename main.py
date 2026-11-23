#!/usr/bin/env python3
"""news-image-20261123 entry: copy entry.png to /output/entry.png.

Standard library only. Deterministic: the same input bytes always produce
the same output bytes.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, out_path)
    src_size = os.path.getsize(SRC)
    out_size = os.path.getsize(out_path)
    if src_size != out_size:
        raise SystemExit("copy verification failed: size mismatch")
    if _sha256(SRC) != _sha256(out_path):
        raise SystemExit("copy verification failed: sha256 mismatch")
    print(f"copied entry.png ({out_size} bytes, sha256 {_sha256(out_path)[:16]})")


if __name__ == "__main__":
    main()
