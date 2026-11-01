import csv
import io
from collections import Counter

ENCODING = "cp1252"
SEPARATOR = ";"
NATURE_COLUMN = "Natureza"


def count_calls(content: bytes) -> tuple[int, dict[str, int]]:
    text = content.decode(ENCODING)
    reader = csv.DictReader(io.StringIO(text, newline=""), delimiter=SEPARATOR)
    categories = Counter(row[NATURE_COLUMN][0].upper() for row in reader)
    return categories.total(), dict(sorted(categories.items()))


def format_summary(total: int, categories: dict[str, int]) -> str:
    lines = [f"Total: {total}"]
    lines += [f"{letter} - {amount}" for letter, amount in categories.items()]
    return "\n".join(lines)
