"""Append the Zillow cover letter and resume into one PDF."""

from pathlib import Path
import sys

from pypdf import PdfWriter

COVER_LETTER = Path("zillow 2026-10-01/Cover Letter Zillow.pdf")
RESUME = Path("resume zillow.pdf")
OUTPUT = Path("combined.pdf")


def main() -> None:
    inputs = (COVER_LETTER, RESUME)
    missing = [path for path in inputs if not path.is_file()]
    if missing:
        names = ", ".join(str(path) for path in missing)
        print(f"Missing input file(s): {names}", file=sys.stderr)
        sys.exit(1)

    writer = PdfWriter()
    for path in inputs:
        writer.append(path)
    writer.write(OUTPUT)
    writer.close()
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
