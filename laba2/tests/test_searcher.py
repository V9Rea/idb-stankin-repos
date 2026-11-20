# tests/test_searcher.py
import pytest

from laba2.main import check_string, search_math_line_in_file



# ---------- Тесты через фикстуры из conftest.py ----------
def test_all_valid_fixture_lines(valid_lines):
    for line in valid_lines:
        assert check_string(line) is True, f"должен быть валидным: r{line!r}"


def test_all_invalid_fixture_lines(invalid_lines):
    for line in invalid_lines:
        assert check_string(line) is False, f"должен быть невалидным: {line!r}"


def test_search_in_file(test_data_filepath):
    output_lines = [
        "2 + 2",
        "-5 * 10 + 3",
        "a1 + b2 - c3",
        "2x - 3y + 4z",
        "(a + b) * (a - b)",
        "-((3a + 4b) / 2) + 15",
        "100 : (25 - 5 * (2 + 1))",
        "10 - 3"
    ]

    result = search_math_line_in_file(test_data_filepath)

    assert result == output_lines, f"Не соответствует эталону: {result!r}"

def test_empty_file(empty_test_file_filepath):
    result = search_math_line_in_file(empty_test_file_filepath)
    assert result == [], f"должен быть пустым: {result!r}"

def test_wrong_file_path(incorrect_data_filepath):
    result = search_math_line_in_file(incorrect_data_filepath)
    assert result is None, f"должен быть None: {incorrect_data_filepath!r}"
