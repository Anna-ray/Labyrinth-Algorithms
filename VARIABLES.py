import pygame

#Set colors.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TAUPE = (70, 63, 50)
FALUN_RED = (128, 24, 24)
CITROUILLE = (223, 109, 20)
WHITE_ESPAGNE = (254, 253, 245)


# set the height/width of each location on the grid

# case width
width_case = 30

# coordinates of matrix cases
x_case = 25
y_case = 25
# coordinates of the whole matrix
x = 25
y = 25

# fois: building square matrix
fois = 0
grid = []
t = 20
T = t * t

size = [650, 650]

pygame.init()
window = pygame.display.set_mode(size)
window.fill(WHITE_ESPAGNE)
pygame.WINDOWSHOWN
