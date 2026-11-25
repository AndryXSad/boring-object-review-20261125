"""The Most Boring Object, Reviewed in One Line.

A deterministic one-line review of the dullest everyday object we could
name: the doormat. Its printed WELCOME wears away letter by letter under
every footstep, so the greeting it gives you slowly stops being a greeting
at all -- and the worn-down version is somehow the truest thing the house
says. The program writes exactly that one line to the entry file.

The output is fully deterministic: no randomness, no clock, no network,
no input is read, so every run writes the same bytes.

Run:  python3 main.py
Writes: <output dir>/entry.txt  (MAKEFUN_OUTPUT_DIR, or /output by default)
"""

import os

# The winning line from the local head-to-head tournament (19 candidates):
# object = doormat (genuinely boring, in every home), observation = the
# printed WELCOME really does wear down to WELCOM underfoot, joke = the
# half-erased greeting is the most honest one the house ever gives.
# 112 characters, one line, no trailing newline in the entry file.
REVIEW = (
    "My doormat's WELCOME has worn down to WELCOM, "
    "which is still the most honest greeting this house has ever given."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
