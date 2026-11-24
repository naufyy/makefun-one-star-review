"""Gravity: a one-star review of something essential.

The entry is a deadpan complaint about gravity. The joke lands on the last
line: the whole floor was available, and gravity still picked the corner of
the screen as the place to land.
"""

import os

ENTRY = "One star. Dropped my phone from waist height. Gravity had the entire floor to work with and chose the corner of the screen."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
