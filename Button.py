import pygame

class Button(pygame.sprite.Sprite):
 #buttons
    def __init__(self, x, y, w, h, text, color):
        super(Button, self).__init__()
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont('𝒮𝓉𝓎𝓁𝑒', 25)
        #Park Avenue
    def show(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h])
        #buttons details description ("blit"give same detail of button for all buttons)
        #This function says take the background surface and draw it onto the screen and position it at (x,y)
        screen.blit(self.font.render(self.text, True, (222, 170, 255)), (self.x + 25, self.y + 10))

