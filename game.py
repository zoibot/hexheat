from hexagon import *

import pygame
from pygame.locals import *

pygame.init()
#init pygame display
screen = pygame.display.set_mode((640,480), pygame.OPENGL | pygame.DOUBLEBUF)

initialize_graphics()

angle = 120
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    draw_scene(-1, 0)
    angle += 1
    pygame.display.flip()
    flip_graphics()

