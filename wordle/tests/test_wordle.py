from wordle import LetterPosition, __version__, validate_letter, validate_word


def test_version():
    assert __version__ == "0.1.0"


def test_if_letter_not_exist_in_word_return_not_in_word():
    result = validate_letter("z", 0, "crate")

    assert result == LetterPosition.NOT_IN_WORD


def test_if_letter_not_in_right_position_return_not_in_right_position():
    result = validate_letter("a", 0, "crate")

    assert result == LetterPosition.NOT_IN_RIGHT_POSITION


def test_if_letter_in_right_position_return_ok():

    result = validate_letter("c", 0, "crate")

    assert result == LetterPosition.OK


def test_word_is_correct():
    result = validate_word("crate", "crate")

    assert result == [
        ("c", LetterPosition.OK),
        ("r", LetterPosition.OK),
        ("a", LetterPosition.OK),
        ("t", LetterPosition.OK),
        ("e", LetterPosition.OK),
    ]


def test_occurence_of_letter_is_correct():
    result = validate_word("armas", "crate")

    assert result == [
        ("a", LetterPosition.NOT_IN_RIGHT_POSITION),
        ("r", LetterPosition.OK),
        ("m", LetterPosition.NOT_IN_WORD),
        ("a", LetterPosition.NOT_IN_WORD),
        ("s", LetterPosition.NOT_IN_WORD),
    ]
