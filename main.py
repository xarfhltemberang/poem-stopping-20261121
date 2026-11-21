#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem about agency — the power to stop and to stay —
to /output/entry.txt. Deterministic, no network, no input.
"""

import os
import stat

POEM = """My thumb hovers over send \u2014
one sentence that would set
a whole day moving.

Beside me, the agent waits,
patient as a held breath,
its hands full of nothing yet.

I delete the words instead.
The quiet stays mine.
I did not freeze. I chose."""

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    text = POEM.strip() + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
