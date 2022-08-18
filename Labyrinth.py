import random
import time
from math import sqrt
import pygame
from VARIABLES import *
from Button import Button

class labyrinth:
    def __init__(self, x_case, y_case, x, y, width_case):
        self.x_case =x_case
        self.y_case = y_case
        self.x = x
        self.y = y
        self.width_case = width_case
        #self.walls = walls

# Drawing cases
def cases_with_coordinates(coordinates, cases):
    for case in cases:
        if ((case.x_case, case.y_case) == coordinates):
            return case



# Functions To Generate Walls
def bas(x_case, y_case):
    pygame.draw.rect(window, WHITE, (x_case + 1, y_case - width_case + 1, 29, 49), 0)
    pygame.display.update()


def haut(x_case, y_case):
    pygame.draw.rect(window, WHITE, (x_case + 1, y_case + 1, 29, 49), 0)
    pygame.display.update()


def gauche(x_case, y_case):
    pygame.draw.rect(window, WHITE, (x_case - width_case + 1, y_case + 1, 49, 29), 0)
    pygame.display.update()


def droite(x_case, y_case):
    pygame.draw.rect(window, WHITE, (x_case + 1, y_case + 1, 49, 29), 0)
    pygame.display.update()


class Case:
    # Case Constructor With Moves
    def __init__(self, up, down, right, left, x_case, y_case, width_case):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.x_case = x_case
        self.y_case = y_case
        self.width_case = width_case

    # Case Constructor
    def __init__(self, x_case, y_case, width_case):
        self.x_case = x_case
        self.y_case = y_case
        self.width_case = width_case
        self.up = (0, 0)
        self.down = (0, 0)
        self.left = (0, 0)
        self.right = (0, 0)

    def draw_case(self, window, color):
        # small rectangles in closed walls (if no ways are available)
        pygame.draw.rect(window, WHITE_ESPAGNE, (self.x_case, self.y_case, self.width_case, self.width_case))
        # making general maze walls
        pygame.draw.line(window, CITROUILLE, [self.x_case, self.y_case], [self.x_case + self.width_case, self.y_case])  # up
        pygame.draw.line(window, CITROUILLE, [self.x_case, self.y_case + self.width_case],
                         [self.x_case + self.width_case, self.y_case + self.width_case])  # down
        pygame.draw.line(window, FALUN_RED, [self.x_case + self.width_case, self.y_case],
                        [self.x_case + self.width_case, self.y_case + self.width_case]) # right
        pygame.draw.line(window, FALUN_RED, [self.x_case, self.y_case], [self.x_case, self.y_case + self.width_case])  # left
        pygame.display.update()


    def draw_chemin(self, window, color):
        pygame.draw.rect(window, blue, (self.x_case, self.y_case, 50, 50))


class GRID_2D:
    def __init__(self, cases):
        self.cases = cases

    def display_maze_cases(self):
        for case in cases:
            case.draw_case(window, BLACK)

    def generate_maze(self):
        visited_nodes = []  # no visited nodes yet
        queue = []   # empty queue
        x = cases[0].x_case
        y = cases[0].y_case
        w = cases[0].width_case
        # append() : add an element at the end of the list
        queue.append((x, y))
        visited_nodes.append((x, y))
        while len(queue) > 0:

            cell = []
        # Drawing Matrix Cells (Columns & Rows)
            if (x + w, y) not in visited_nodes and (x + w, y) in grid:
               cell.append("droite")

            if (x - w, y) not in visited_nodes and (x - w, y) in grid:
                cell.append("gauche")

            if (x, y + w) not in visited_nodes and (x, y + w) in grid:
                cell.append("bas")

            if (x, y - w) not in visited_nodes and (x, y - w) in grid:
                cell.append("haut")
            if len(cell) > 0:
                # random.choice : Return a random element from a list.
                cell_chosen = (random.choice(cell))

                # Generate right walls
                if cell_chosen == "droite":
                    droite(x, y)
                    cases_with_coordinates((x, y), cases).right = (x + w, y)
                    x = x + w
                    cases_with_coordinates((x, y), cases).left = (x - w, y)
                    visited_nodes.append((x, y))
                    queue.append((x, y))


                # Generate left walls
                elif cell_chosen == "gauche":
                    gauche(x, y)
                    cases_with_coordinates((x, y), cases).left = (x - w, y)
                    x = x - w
                    visited_nodes.append((x, y))
                    cases_with_coordinates((x, y), cases).right = (x + w, y)
                    queue.append((x, y))


                elif cell_chosen == "haut":
                    bas(x, y)
                    cases_with_coordinates((x, y), cases).up = (x, y - w)
                    y = y - w
                    cases_with_coordinates((x, y), cases).down = (x, y + w)
                    visited_nodes.append((x, y))
                    queue.append((x, y))


                elif cell_chosen == "bas":
                    haut(x, y)
                    cases_with_coordinates((x, y), cases).down = (x, y + w)
                    y = y + w
                    cases_with_coordinates((x, y), cases).up = (x, y - w)
                    visited_nodes.append((x, y))
                    queue.append((x, y))


            else:
                # The pop() method returns the item present at the given index. This item is also removed from the list.
                # If no position is specified, a.pop () removes and returns the last item in the list
                x, y = queue.pop()
                # time.sleep(.05)


cases = []

for nbr in range(0, T):

  fois += 1
  if fois == sqrt(T):
   grid.append((x_case, y_case))
   if y_case == y:
    case = Case(x_case, y_case, width_case)
    cases.append(case)
   elif y_case == y * fois:
      case = Case(x_case, y_case, width_case)
      cases.append(case)
   else:
      case = Case(x_case, y_case, width_case)
      cases.append(case)
   fois = 0
   x_case = 25
   y_case += width_case
  else:
    case = Case(x_case, y_case, width_case)

    # drawing the first maze case
    if x_case == x and y_case == y:
        grid.append((x_case, y_case))
        cases.append(case)

    # drawing the first column maze except the the first case
    elif x_case == x and y_case != y and y_case != y_case * sqrt(16):
        grid.append((x_case, y_case))
        cases.append(case)

    elif x_case == x and y_case == y_case * sqrt(16):
        # case.right = (x_pos + width, y_pos)
        # case.up = (x_pos, y_pos - width)
        grid.append((x_case, y_case))
        cases.append(case)
    # Drawing the first line maze except the first and end case of the first line
    elif x_case != x and y_case == y:
        grid.append((x_case, y_case))
        cases.append(case)

    # Drawing maze content
    elif x_case != x and y_case != y:
        grid.append((x_case, y_case))
        cases.append(case)

    elif x_case != x and y_case == y_case * sqrt(16):
        grid.append((x_case, y_case))
        cases.append(case)

    x_case += width_case

i = 0

run = True
grid_2d = GRID_2D(cases)
grid_2d.display_maze_cases()
grid_2d.generate_maze()


# button but - end button(goal node)-
pygame.draw.rect(window, BLACK, (30 + (30 * (t - 1)) + 2, 30 + (30 * (t - 1)) + 2, width_case - 10, width_case - 10))
pygame.display.update()
yes = False

# NOTE:
# If you want to display only the labyrinth, run the comment below
# If tou want to display BFS, DFS or IDFS path, let the comment below as it is
# and execute each algorithm in its file

"""while run:
    pass"""


