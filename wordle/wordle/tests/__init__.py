from enum import Enum


class Letter(Enum):
    NOT_IN_WORD = "NOT_IN_WORD"
    NOT_IN_RIGHT_POSITION = "NOT_IN_RIGHT_POSITION"


def found_letters(attempt, word):
    result = []
    for attempt_letter in attempt:
        if attempt_letter not in word:
            result.append(Letter.NOT_IN_WORD)
        else:
            result.append(Letter.NOT_IN_RIGHT_POSITION)

    return tuple(result)
