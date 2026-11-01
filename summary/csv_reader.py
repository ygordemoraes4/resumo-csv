import csv
import io
from collections.abc import Iterator

ENCODING = "cp1252"
SEPARATOR = ";"
UNIT_COLUMN = "Unidade Responsável"
UNIT_MARKER = "(PASSOS)"


def read_all_rows(content: bytes) -> Iterator[dict[str, str]]:
    text = content.decode(ENCODING)
    yield from csv.DictReader(io.StringIO(text, newline=""), delimiter=SEPARATOR)


def is_own_unit(row: dict[str, str]) -> bool:
    return UNIT_MARKER in row[UNIT_COLUMN].upper()


def read_rows(content: bytes) -> Iterator[dict[str, str]]:
    yield from (row for row in read_all_rows(content) if is_own_unit(row))


def count_rows(content: bytes) -> tuple[int, int]:
    kept = ignored = 0
    for row in read_all_rows(content):
        if is_own_unit(row):
            kept += 1
        else:
            ignored += 1
    return kept, ignored
