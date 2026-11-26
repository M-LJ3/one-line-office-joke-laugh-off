"""Write one funny office joke to /output/entry.txt.

The line is an entry for a one-line office joke contest.
"""

import os


def joke_line():
    """Return one funny line about office life."""
    return (
        "Our manager scheduled a meeting to discuss why we have too many "
        "meetings, then scheduled a follow-up to recap it."
    )


def main():
    line = joke_line()
    os.makedirs("/output", exist_ok=True)
    # Write the joke with no trailing newline, exactly as entered.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    # Sanity check: the file must hold exactly the one joke line.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == line


if __name__ == "__main__":
    main()
