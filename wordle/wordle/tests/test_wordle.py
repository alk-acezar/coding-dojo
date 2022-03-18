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
