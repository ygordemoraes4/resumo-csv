from collections import Counter

from summary.csv_reader import read_rows

NATURE_COLUMN = "Natureza"


def count_calls(content: bytes) -> tuple[int, dict[str, int]]:
    categories = Counter(row[NATURE_COLUMN][0].upper() for row in read_rows(content))
    return categories.total(), dict(sorted(categories.items()))


def format_summary(total: int, categories: dict[str, int]) -> str:
    lines = [f"Total: {total}"]
    lines += [f"{letter} - {amount}" for letter, amount in categories.items()]
    return "\n".join(lines)
