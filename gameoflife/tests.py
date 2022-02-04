import pytest

from game import get_next_generation


def test_grid_is_invalid_when_lines_does_not_have_same_number_of_columns():
    grid = [["L", "L"], ["L"]]

    with pytest.raises(ValueError):
        get_next_generation(grid)


def test_any_live_cell_with_fewer_than_two_live_neighbours_dies():
    grid = [
        ["D", "D"],
        ["L", "D"],
    ]

    result = get_next_generation(grid)

    assert result == [
        ["D", "D"],
        ["D", "D"],
    ]
