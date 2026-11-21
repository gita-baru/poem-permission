"""Copy entry.txt (the poem) to the output directory.

Runs with no network. Deterministic: copies the exact bytes.
"""
import os, shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
dest = os.path.join(out, "entry.txt")
shutil.copyfile(src, dest)
# Sanity: the gate requires 1-280 UTF-8 chars, not only whitespace.
text = open(dest, encoding="utf-8").read()
assert 1 <= len(text) <= 280 and text.strip(), "entry.txt outside 1-280 chars"
