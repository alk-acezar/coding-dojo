from enum import Enum


class Letter(Enum):
    NOT_IN_WORD = "NOT_IN_WORD"


def found_letters(attempt, word):
    return (
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
        Letter.NOT_IN_WORD,
    )
