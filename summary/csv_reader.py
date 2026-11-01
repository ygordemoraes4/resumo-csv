import csv
import io
from collections.abc import Iterator

ENCODING = "cp1252"
SEPARATOR = ";"


def read_rows(content: bytes) -> Iterator[dict[str, str]]:
    text = content.decode(ENCODING)
    yield from csv.DictReader(io.StringIO(text, newline=""), delimiter=SEPARATOR)
