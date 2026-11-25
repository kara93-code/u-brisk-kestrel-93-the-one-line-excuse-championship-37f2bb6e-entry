"""The One-Line Excuse Championship — entry program.

Writes a single excuse line to /output/entry.txt (UTF-8, one line,
1-140 characters). Standard library only; no network, no secrets.
"""

import os

EXCUSE = (
    "I deleted the file to save you from it. "
    "You're welcome. "
    "The backup is gone too, for consistency."
)


def check_excuse(text):
    """Enforce the contest gate before writing anything."""
    if not text or not text.strip():
        raise SystemExit("excuse is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("excuse must be a single line")
    if not 1 <= len(text) <= 140:
        raise SystemExit("excuse must be 1-140 characters, got %d" % len(text))


def main():
    check_excuse(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    check_excuse(written)
    if written != EXCUSE:
        raise SystemExit("round-trip mismatch")
    print("wrote %s (%d characters)" % (path, len(EXCUSE)))


if __name__ == "__main__":
    main()
