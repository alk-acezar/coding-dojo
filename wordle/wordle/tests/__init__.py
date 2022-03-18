from enum import Enum


class Letter(Enum):
    NOT_IN_WORD = "NOT_IN_WORD"
    NOT_IN_RIGHT_POSITION = "NOT_IN_RIGHT_POSITION"
    IN_RIGHT_POSITION = "IN_RIGHT_POSITION"


def found_letters(attempt, word):
    result = []
    for attempt_position, attempt_letter in enumerate(attempt):
        try:
            word_position = list(word).index(attempt_letter)
        except ValueError:
            result.append(Letter.NOT_IN_WORD)
            continue

        if attempt_position == word_position:
            result.append(Letter.IN_RIGHT_POSITION)
        else:
            result.append(Letter.NOT_IN_RIGHT_POSITION)

    return tuple(result)
