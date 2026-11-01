from pathlib import Path

import pytest

from summary.csv_reader import count_rows, is_own_unit, read_rows

SAMPLE = Path(__file__).parent / "fixtures" / "sample.csv"


@pytest.mark.parametrize(
    ("unit", "expected"),
    [
        ("1CIA IND/2CIA/1PEL(PASSOS)", True),
        ("1CIA IND/2CIA/PEL PREV E VIST(PASSOS)", True),
        ("1cia ind/2cia/1pel(passos)", True),
        ("1CIA IND/1CIA/1PEL", False),
        ("1CIA IND/2CIA/1PEL(OUTRACIDADE)", False),
        ("UNIDADE PASSOS", False),
        ("", False),
    ],
)
def test_is_own_unit(unit, expected):
    assert is_own_unit({"Unidade Responsável": unit}) is expected


def test_read_rows_keeps_only_rows_of_the_unit():
    rows = list(read_rows(SAMPLE.read_bytes()))
    assert [row["Numero"] for row in rows] == ["1", "2", "3", "4", "5", "6"]


def test_count_rows_reports_kept_and_ignored():
    assert count_rows(SAMPLE.read_bytes()) == (6, 2)


def test_count_rows_requires_the_unit_column():
    with pytest.raises(KeyError):
        count_rows("Natureza\r\nP01 - teste\r\n".encode("cp1252"))
