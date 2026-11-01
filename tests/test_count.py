from pathlib import Path

from summary.count import count_calls, format_summary

SAMPLE = Path(__file__).parent / "fixtures" / "sample.csv"


def test_total_counts_every_row():
    total, _ = count_calls(SAMPLE.read_bytes())
    assert total == 6


def test_category_is_first_letter_of_nature():
    _, categories = count_calls(SAMPLE.read_bytes())
    assert categories == {"A": 2, "P": 3, "R": 1}


def test_lowercase_letter_is_uppercased():
    content = "Natureza\r\np01 - teste\r\nP02 - teste\r\n".encode("cp1252")
    _, categories = count_calls(content)
    assert categories == {"P": 2}


def test_categories_are_in_alphabetical_order():
    _, categories = count_calls(SAMPLE.read_bytes())
    assert list(categories) == ["A", "P", "R"]


def test_reads_windows_1252_accents():
    content = "Natureza\r\nÁ01 - INCÊNDIO\r\n".encode("cp1252")
    _, categories = count_calls(content)
    assert categories == {"Á": 1}


def test_summary_format():
    total, categories = count_calls(SAMPLE.read_bytes())
    assert format_summary(total, categories) == "Total: 6\nA - 2\nP - 3\nR - 1"
