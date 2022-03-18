from enum import Enum


class Letter(Enum):
    NOT_IN_WORD = "NOT_IN_WORD"
    NOT_IN_RIGHT_POSITION = "NOT_IN_RIGHT_POSITION"
    IN_RIGHT_POSITION = "IN_RIGHT_POSITION"


def found_letters(attempt, word):
    result = []
    seen_letters = []
    for attempt_position, attempt_letter in enumerate(attempt):
        if attempt_letter in seen_letters:
            result.append(Letter.NOT_IN_WORD)
            continue

        try:
            word_position = list(word).index(attempt_letter)
        except ValueError:
            result.append(Letter.NOT_IN_WORD)
            seen_letters.append(attempt_letter)
            continue

        if attempt_position == word_position:
            result.append(Letter.IN_RIGHT_POSITION)
        else:
            result.append(Letter.NOT_IN_RIGHT_POSITION)
        seen_letters.append(attempt_letter)

    return tuple(result)
