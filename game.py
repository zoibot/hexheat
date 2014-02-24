from random import randint

import pygame
from pygame.locals import *

from hexagon import *

pygame.init()
#init pygame display
screen = pygame.display.set_mode((640,480), pygame.OPENGL | pygame.DOUBLEBUF)

initialize_graphics()

rising = False
sinking = False
current_hex = -1
height = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if not (rising or sinking):
                current_hex = randint(0, 6)
                rising = True
    if rising:
        height += 0.01
        if height >= 1:
            rising = False
            sinking = True
    if sinking:
        height -= 0.01
        if height <= 0:
            height = 0
            sinking = False
            current_hex = -1
    draw_level(current_hex, height)
    draw_player(0, 0, height)
    pygame.display.flip()
    flip_graphics()

