__version__ = "0.1.0"


from enum import Enum


class LetterPosition(Enum):
    NOT_IN_WORD = "NOT_IN_WORD"
    OK = "OK"
    NOT_IN_RIGHT_POSITION = "NOT_IN_RIGHT_POSITION"


def validate_letter(letter, position, word):
    try:
        found_position = list(word).index(letter)
    except ValueError:
        return LetterPosition.NOT_IN_WORD
    return (
        LetterPosition.OK
        if position == found_position
        else LetterPosition.NOT_IN_RIGHT_POSITION
    )


def validate_word(input, word):
    result = []
    for position, letter in enumerate(input):
        letter_result = validate_letter(letter, position, word)
        occurences = list(word).count(letter)
        counter = 0
        for letter2, letter_result2 in result:
            if letter2 == letter and letter_result2 in (
                LetterPosition.OK,
                LetterPosition.NOT_IN_RIGHT_POSITION,
            ):
                counter += 1
        if occurences != counter:
            result.append((letter, letter_result))
        else:
            result.append((letter, LetterPosition.NOT_IN_WORD))
    return result
