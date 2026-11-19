# tests/test_validator.py
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
        "100 : (25 - 5 * (2 + 1))]"
    ]

    print(search_math_line_in_file(test_data_filepath))

    assert search_math_line_in_file(test_data_filepath), output_lines

def test_wrong_file_path(incorrect_data_filepath):
    assert search_math_line_in_file(incorrect_data_filepath) is None, f"должен быть невалидным: {incorrect_data_filepath!r}"
