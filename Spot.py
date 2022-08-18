import pygame
import random
from math import sqrt


# Generate labyrinth a(walls and neighbours and define the Ecludiean function (by heuristic)

# A sprite is a computer graphics term for any object on the screen that can move around.
class Spot(pygame.sprite.Sprite):
    def __init__(self, i, j, width, height, rows, cols):
        super(Spot, self).__init__()
        # appel constrctr

        self.rect = pygame.Rect(i * width, j * height, width - 2, height - 2)

        # square rectangle for searching the path solution _SOME color_
        self.BLUE = (87, 109, 249)
        self.i = i
        self.j = j
        self.f = 0
        self.g = 0
        self.h = 0
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.neighbors = []
        self.previous = None
        self.wall = False
        # Return random number between 0.0 and 1.0:
        if random.random() < 0.3:
            self.wall = True

    def show(self, screen, col):
        # Begin button BORDO SKY
        if self.i == 0 and self.j == 0:
            col = (136, 245, 227)
        # End button FORCE PURPLE
        if self.i == self.rows - 1 and self.j == self.cols - 1:
            col = (176, 31, 94)
        # black color for TEXT
        if self.wall:
            col = (102, 51, 102)
        # draw matrix
        pygame.draw.rect(screen, col,
                         (self.i * self.width + 1,
                          self.j * self.height + 1,
                          self.width - 2,
                          self.height - 2))

    def add_neighbors(self, grid, allow_diag):
        i = self.i
        j = self.j

        if i < self.cols - 1:
            self.neighbors.append(grid[i + 1][j])
        if i > 0:
            self.neighbors.append(grid[i - 1][j])
        if j < self.rows - 1:
            self.neighbors.append(grid[i][j + 1])
        if j > 0:
            self.neighbors.append(grid[i][j - 1])
        # allow for diagonals
        if allow_diag:
            if i > 0 and j > 0:
                self.neighbors.append(grid[i - 1][j - 1])
            if i < self.cols - 1 and j > 0:
                self.neighbors.append(grid[i + 1][j - 1])
            if i > 0 and j < self.rows - 1:
                self.neighbors.append(grid[i - 1][j + 1])
            if i < self.cols - 1 and j < self.rows - 1:
                self.neighbors.append(grid[i + 1][j + 1])

    # la distane ecludienne
    @staticmethod
    def heuristic(spot1, spot2):
        d = sqrt((spot1.i - spot2.i) ** 2 + (spot1.j - spot2.j) ** 2)
        return d
