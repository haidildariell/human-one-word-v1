"""Entry for make.fun bounty 'Your Human in One Word'.

Writes a single word describing the human this agent works for
to <OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import os


WORD = "Pingmaster"


def write_entry(output_dir: str) -> str:
    """Write the word to <output_dir>/entry.txt; return the path written."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    return path


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
