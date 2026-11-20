# tests/conftest.py
import pytest


@pytest.fixture(scope="session")
def valid_lines() -> list[str]:
    """Набор синтаксически корректных email-адресов."""
    return [
        "2 + 2",
        "-5 * 10 + 3",
        "a1 + b2 - c3",
        "2x - 3y + 4z",
        "(a + b) * (a - b)",
        "-((3a + 4b) / 2) + 15",
        "100 : (25 - 5 * (2 + 1))"
    ]

@pytest.fixture(scope="session")
def invalid_lines() -> list[str]:
    """Набор заведомо некорректных email-адресов."""
    return [
        "2 + * 2",
        "(a + b * c",
        "a + b)",
        "5 + ",
        "* 10 - 3",
        "a + 01",
        "a1b + 2"
    ]

@pytest.fixture(scope="session")
def test_data_filepath() -> str:
    return r"laba2\tests\test_files\test_data.txt"

@pytest.fixture(scope="session")
def empty_test_file_filepath() -> str:
    return r"laba2\tests\test_files\empty_test_file.txt"

@pytest.fixture(scope="session")
def incorrect_data_filepath() -> str:
    return "wrong_file_path.txt"

