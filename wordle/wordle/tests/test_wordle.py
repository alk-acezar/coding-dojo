from wordle import __version__

from tests import Letter, found_letters


def test_version():
    assert __version__ == "0.1.0"


def test_a_letter_not_in_word_returns_not_in_word():
    result = found_letters("abcde", "uvxyz")

    assert result == (
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
    )


def test_a_letter_not_in_right_position_returns_not_in_right_position():
    result = found_letters("zbcde", "uvxyz")

    assert result == (
        Letter.NOT_IN_RIGHT_POSITION,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
    )


def test_a_letter_in_right_position_returns_in_right_position():
    result = found_letters("abcdz", "uvxyz")

    assert result == (
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.IN_RIGHT_POSITION,
    )


def test_a_letter_not_in_right_position_returns_not_in_right_position_only_once():
    result = found_letters("zzcde", "uvxyz")

    assert result == (
        Letter.NOT_IN_RIGHT_POSITION,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
    )
