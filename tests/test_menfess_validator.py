
from src.menfess_validator import validate_menfess


def test_valid_message():
    assert validate_menfess("Semangat kuliah!") is True


def test_valid_anonymous_message():
    assert validate_menfess("Pesan rahasia") is True


def test_message_with_outer_spaces():
    assert validate_menfess("  Halo teman!  ") is True


def test_message_with_200_characters():
    assert validate_menfess("A" * 200) is True


def test_empty_message():
    assert validate_menfess("") is False


def test_spaces_only():
    assert validate_menfess("     ") is False


def test_message_with_one_character():
    assert validate_menfess("A") is True


def test_message_with_500_characters():
    assert validate_menfess("A" * 500) is True


def test_message_with_501_characters():
    assert validate_menfess("A" * 501) is False


def test_non_string_input():
    assert validate_menfess(123) is False
