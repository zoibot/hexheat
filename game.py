from random import randint

import pygame
from pygame.locals import *

from hexagon import *
from player import Player

initialize_graphics()

WAITING = 0
FLAG_SHOWN = 1
SINKING = 2
RISING = 3

state = WAITING
current_hex = -1
height = 0
frames = 0

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                if state == WAITING:
                    current_hex = randint(0, 6)
                    state = FLAG_SHOWN
                    frames = 200 # this is dumb
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.move(-0.01, 0)
    elif keys[K_RIGHT]:
        player.move(0.01, 0)
    if keys[K_UP]:
        player.move(0, -0.01)
    elif keys[K_DOWN]:
        player.move(0, 0.01)
 
    if state == FLAG_SHOWN:
        frames -= 1
        if not frames:
            state = SINKING

    if state == SINKING:
        height += 0.01
        if height >= 1:
            state = RISING
    if state == RISING:
        height -= 0.01
        if height <= 0:
            height = 0
            state = WAITING
            current_hex = -1
    draw_level(current_hex, height)
    draw_player(player.x, player.y, height)
    flip_graphics()

