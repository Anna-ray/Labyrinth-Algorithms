import pygame
import random
import time
from Spot import Spot
from Button import Button

#what did i understand from lambda function that  A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

current_milli_time = lambda: int(round(time.time()))
# "round": Round a number to only two decimals
# The time() function returns the number of seconds passed since epoch.
# time.time() * 1000 get the number of milliseconds sonce epoch
# pygame.init() : initialize all imported pygame modules
pygame.init()

width = height = 600
# window's total width
width_tot = width + 200

# Python gradient color
FFCBF = (255, 203, 242)
FLUFY = (255, 153, 153)
RED = (56, 56, 188)
PURPLE = (246, 52, 201)
BORDO = (159, 58, 62)

# my screen details   (size , display , name)
WINDOW_SIZE = [width_tot, height]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(" Welcome To My Labyrinth ")

# to trace time execution
done = False
clock = pygame.time.Clock()

# Setup  for square maze
user = str(input("Give me your name please ! "))
cols = rows = int(input("Dear " + user + " Enter Columns and Raws number: "))

allow_diagonals = True
show_visited = False

grid = []
# for all
openSet = []
closedSet = []
path = []
saved_path = []

w = width / cols
h = height / rows

for i in range(cols):
    grid.append([])

for i in range(cols):
    for j in range(rows):
        grid[i].append(Spot(i, j, w, h, rows, cols))

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid, allow_diagonals)

# the begin and the end cases
start = grid[0][0]
end = grid[cols - 1][rows - 1]
# you can build walls with this false
start.wall = False
end.wall = False

# Show buttons  with their colors
randomize = Button(width + 25, 30 + 0 * 55, 150, 50, 'Walls', (94, 96, 206))
clear = Button(width + 25, 30 + 1 * 55, 150, 50, 'Clear All', (78, 168, 222))
start = Button(width + 25, 30 + 2 * 55, 150, 50, 'A*', (72, 191, 227))
start_bfs = Button(width + 25, 30 + 3 * 55, 150, 50, 'BFS', (86, 207, 225))
start_dfs = Button(width + 25, 30 + 4 * 55, 150, 50, 'DFS', (100, 223, 223))
start_idfs = Button(width + 25, 30 + 5 * 55, 150, 50, 'IDFS', (114, 239, 221))
start_path = Button(width + 25, 30 + 6 * 55, 150, 50, 'A* + PATHS', (181, 131, 141))
start_bfs_path = Button(width + 25, 30 + 7 * 55, 150, 50, 'BFS + PATHS', (229, 152, 155))
start_dfs_path = Button(width + 25, 30 + 8 * 55, 150, 50, 'DFS + PATHS', (255, 180, 162))
start_idfs_path = Button(width + 25, 30 + 9 * 55, 150, 50, 'IDFS + PATHS', (255, 205, 178))


def clear_grid():
    global openSet
    global closedSet
    global saved_path
    saved_path = []
    for i in range(rows):
        for j in range(cols):
            grid[i][j].wall = False
    openSet = []
    closedSet = []


def randomize_grid():
    clear_grid()
    for i in range(rows):
        for j in range(cols):
            if random.random() < 0.3:
                grid[i][j].wall = True
    grid[0][0].wall = False
    grid[rows - 1][cols - 1].wall = False


# don't start until draw
start_enable = False  # for a star
start_enable_rec = False  # for bfs
start_enable_recd = False  # for dfs


# green start
def start_general():
    global openSet
    global closedSet
    global path
    openSet = []
    closedSet = []
    path = []
    start = grid[0][0]
    openSet.append(start)
    end = grid[cols - 1][rows - 1]
    start.wall = False
    end.wall = False


# drawing the way of algos " with path "
# A STAR ALGO
def start_grid():
    start_general()
    global start_enable
    start_enable = True


# class BFS :  Algo

def start_grid_bfs():
    start_general()
    global start_enable_rec
    start_enable_rec = True


# DFS Algo
def start_grid_dfs():
    start_general()
    global start_enable_recd
    start_enable_recd = True


# IDFS Algo
def start_grid_idfs():
    start_general()
    global start_enable_recd
    start_enable_recd = True


time_start = 0
# give break to function (to the buttons for example)
hold = False
# Game loop
while not done:
    # if the event is done show it (get events from the queue)
    # Pygame will register all events from the user into an event ...
    # queue which can be received with the code pygame.event.get()...
    for event in pygame.event.get():
        # type is an integer representing what kind of event it is.
        if event.type == pygame.QUIT:
            done = True
        # get the state button
        if pygame.mouse.get_pressed()[0]:
            # pygame.mouse.get_pos() : get the mouse cursor position(Returns the x and y position of the mouse cursor.)
            pos = pygame.mouse.get_pos()
            clicked_sprites = [sprite for r in grid for sprite in r if sprite.rect.collidepoint(pos)]
            # test if A.rect.midleft, A.rect.midright, A.rect.midtop, A.rect.midbottom, A.rect.topleft,
            # A.rect.bottomleft , A.rect.topright, A.rect.bottomright are inside B.rect
            if clear.rect.collidepoint(pos) > 0:
                hold = False
                clear_grid()

            if randomize.rect.collidepoint(pos) > 0:
                hold = False
                randomize_grid()

            if start.rect.collidepoint(pos) > 0:
                time_start = current_milli_time()
                hold = False
                show_visited = False
                start_grid()

            if start_path.rect.collidepoint(pos) > 0:
                time_start = current_milli_time()
                hold = False
                show_visited = True
                start_grid()


#here it's my BFS I didn't use a oriented object .... the oop in python we use

            if start_bfs.rect.collidepoint(pos) > 0:
                time_start = current_milli_time()
                hold = False
                show_visited = False
                start_grid_bfs()

            if start_bfs_path.rect.collidepoint(pos) > 0:
                time_start = current_milli_time()
                hold = False
                show_visited = True
                start_grid_bfs()

#here it's my DFS


            if start_dfs.rect.collidepoint(pos) > 0:
                time_start = current_milli_time()
                hold = False
                show_visited = False
                start_grid_dfs()

            if start_dfs_path.rect.collidepoint(pos) > 0:
                time_start = current_milli_time()
                hold = False
                show_visited = True
                start_grid_dfs()

#here it's my idfs
            if start_idfs.rect.collidepoint(pos) > 0:
                time_start = current_milli_time()
                hold = False
                show_visited = False
                start_grid_idfs()
                print(" " + user + "it's same with dfs just put the mous on the last pos that you want !")
            if start_idfs_path.rect.collidepoint(pos) > 0:
                time_start = current_milli_time()
                hold = False
                show_visited = True
                start_grid_idfs()
                print(" Sir please put the mouse on the cases and click to know your idfs positions ^^")

            if len(clicked_sprites) > 0:
                # create walls
                # ( to print the case coordinate for each case that we want to know
                print(pos)
                # false case the buttons clicked can't be a wall
                clicked_sprites[0].wall = True
        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [sprite for r in grid for sprite in r if sprite.rect.collidepoint(pos)]

            if len(clicked_sprites) > 0:
                clicked_sprites[0].wall = False

    if hold:
        continue

    # Class path bfs
    if start_enable_rec:
        if len(openSet) > 0:
            current = openSet[0]
            # case of bgin qual to end
            if current == end:
                print('Done in ', (current_milli_time() - time_start), ' milliseconds!')
                hold = True
                start_enable_rec = False
                saved_path = path
            # remove() method takes a single element as an argument and removes it from the list
            openSet.remove(current)

            neighbors = current.neighbors

            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                if neighbor not in closedSet and not neighbor.wall:
                    if neighbor not in openSet:
                        openSet.append(neighbor)
                        closedSet.append(neighbor)
                    neighbor.previous = current
            closedSet.append(current)
        else:
            print(" " + user + ' Try again ... we don''t have a BFS solution for you!')
            # wait for a single event from the queue
            pygame.event.wait()
            break

    # Class path Dfs
    if start_enable_recd:
        if len(openSet) > 0:
            current = openSet[0]
            # case of begin equal to end
            if current == end:
                print('Done in ', (current_milli_time() - time_start), ' milliseconds!')
                hold = True
                start_enable_rec = False
                saved_path = path
            # remove() method takes a single element as an argument and removes it from the list
            openSet.remove(current)

            neighbors = current.neighbors
            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                while current != end:
                    neighbors = current.neighbors
                    if len(neighbors) >= 1:
                        openSet.append(neighbor)
                        # push current cell to stack
                        saved_path.append(current)
                        # set current cell to new cell


        else:
            print(" " + user + ' Try again ... we don''t have a BFS solution for you!')
            # wait for a single event from the queue
            pygame.event.wait()
            break

    # Class path A_star
    if start_enable:
        if len(openSet) > 0:
            winner = 0
            for i in range(len(openSet)):
                if openSet[i].f < openSet[winner].f:
                    winner = i  # f(n) the litle "with heuristic"

            current = openSet[winner]

            if current == end:
                print('Done in ', (current_milli_time() + time_start), ' milliseconds!') #- time_start
                hold = True
                start_enable = False
                saved_path = path

            openSet.remove(current)
            closedSet.append(current)

            neighbors = current.neighbors
            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                if neighbor not in closedSet and not neighbor.wall:
                    tempG = current.g + 1  # take a move  of heuristic distance

                    newPath = False
                    if neighbor in openSet:
                        if tempG < neighbor.g:
                            neighbor.g = tempG
                            newPath = True
                    else:
                        neighbor.g = tempG
                        openSet.append(neighbor)
                        newPath = True
                    if newPath:
                        neighbor.h = Spot.heuristic(neighbor, end)
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.previous = current
        else:
            print(" " + user + ' Try again ... we don''t have a solution for you!')
            pygame.event.wait()
            break

    screen.fill(FFCBF)

    randomize.show(screen)
    clear.show(screen)
    start.show(screen)
    start_bfs.show(screen)
    start_path.show(screen)
    start_bfs_path.show(screen)
    start_dfs.show(screen)
    start_dfs_path.show(screen)
    start_idfs.show(screen)
    start_idfs_path.show(screen)

    for i in range(cols):
        for j in range(rows):
            grid[i][j].show(screen, FLUFY)
            # cleared screen

    if start_enable_rec or start_enable or start_enable_recd:
        # Find path to draw path bfs, dfs and a star
        path = []
        # temporar case
        temp = current
        path.append(temp)
        while temp.previous:
            path.append(temp.previous)
            temp = temp.previous
        path.append(temp)
        temp.show(screen, BORDO)
        for i in range(len(path)):
            path[i].show(screen, BORDO)
    else:  # drawing the paths at the end with color after finding
        for i in range(len(saved_path)):
            saved_path[i].show(screen, BORDO)

    if show_visited:  # Paths  around bfs and a star
        for i in range(len(closedSet)):
            closedSet[i].show(screen, RED)

        for i in range(len(openSet)):
            openSet[i].show(screen, PURPLE)
        for j in range(len(closedSet)):
            closedSet[j].show(screen, RED)
        for j in range(len(openSet)):
            openSet[j].show(screen, PURPLE)
    clock.tick(60)
    # will update the contents of the entire display
    pygame.display.flip()
pygame.quit()
