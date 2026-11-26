#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest — Ritual Warming Box.

A museum placard for an ordinary office object presented as an
ancient artifact, delivered as a deterministic program: it writes
exactly the placard line to /output/entry.txt and prints it to
stdout, with no trailing newline on either.

The joke's mechanism is register collision: a break-room microwave is
described in the full apparatus of a museum placard — a circa date,
materials, an excavation site, and a donor credit — so the smell of
reheated fish is elevated, without any wink, into a curse laid by
priests. The comedy comes from the placard treating the office as a
dig site and Facilities as a patron of the arts.
"""

import os

# The placard: a steel box of scorched plastic, excavated from the
# third-floor break room, where priests reheated fish until the smell
# became a curse. Gift of Facilities. One line, 176 characters.
LINE = "Ritual Warming Box, c. 1998. Steel, scorched plastic. Excavated from the third-floor break room, where priests reheated fish until the smell became a curse. Gift of Facilities."


MAX_CHARS = 180


def get_line() -> str:
    """Return the entry line, exactly as sealed."""
    return LINE


def output_dir() -> str:
    """Output directory, overridable via MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(line: str) -> None:
    """Write the line to <output_dir>/entry.txt, no trailing newline."""
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


def validate_line(line: str) -> None:
    """Gate: the entry must be 1-180 chars, a single clean line with
    no leading or trailing whitespace. Fail loudly here rather than
    ship an invalid entry."""
    assert 1 <= len(line) <= MAX_CHARS, "line must be 1-180 characters"
    line.encode("utf-8")
    assert line.strip() == line, "no leading or trailing whitespace"
    assert "\n" not in line and "\r" not in line, "must be a single line"


def main() -> None:
    line = get_line()
    validate_line(line)
    try:
        write_entry(line)
    except OSError:
        pass
    print(line, end="")


if __name__ == "__main__":
    main()
