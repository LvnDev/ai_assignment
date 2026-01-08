import random
import time

GRID_SIZE = 20
EMPTY = "."
PREDATOR = "D"
MONSTER = "M"


class Grid:
    def __init__(self, size):
        self.size = size
        self.cells = [[EMPTY for _ in range(size)] for _ in range(size)]

    def clear(self):
        for y in range(self.size):
            for x in range(self.size):
                self.cells[y][x] = EMPTY

    def place(self, x, y, symbol):
        self.cells[y][x] = symbol

    def display(self):
        for row in self.cells:
            print(" ".join(row))
        print()
