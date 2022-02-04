from copy import deepcopy
from typing import List

Grid = List[List[str]]


def get_next_generation(grid: Grid) -> Grid:
    prev_len = len(grid[0])
    for row in grid:
        if len(row) != prev_len:
            raise ValueError("lines should have the same lenght")

    new_grid = deepcopy(grid)
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            living_neighbors = 0

            try:
                neighbor = grid[x - 1][y - 1]
                living_neighbors += 1 if neighbor == "L" else 0
            except:
                pass

            try:
                neighbor = grid[x - 1][y]
                living_neighbors += 1 if neighbor == "L" else 0
            except:
                pass

            try:
                neighbor = grid[x - 1][y + 1]
                living_neighbors += 1 if neighbor == "L" else 0
            except:
                pass

            try:
                neighbor = grid[x][y - 1]
                living_neighbors += 1 if neighbor == "L" else 0
            except:
                pass

            try:
                neighbor = grid[x][y + 1]
                living_neighbors += 1 if neighbor == "L" else 0
            except:
                pass

            try:
                neighbor = grid[x + 1][y - 1]
                living_neighbors += 1 if neighbor == "L" else 0
            except:
                pass

            try:
                neighbor = grid[x + 1][y]
                living_neighbors += 1 if neighbor == "L" else 0
            except:
                pass

            try:
                neighbor = grid[x + 1][y + 1]
                living_neighbors += 1 if neighbor == "L" else 0
            except:
                pass

            if living_neighbors < 2:
                new_grid[x][y] = "D"
    return new_grid
