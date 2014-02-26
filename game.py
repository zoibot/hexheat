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

delay = 0
waiting_delay = 150 

player = Player()
previous_position = 0,0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
                
    # player movement
    previous_position = player.x, player.y
    keys = pygame.key.get_pressed()
    move_x = 0
    move_y = 0
    if keys[K_LEFT]:
        move_x -= 0.01
    elif keys[K_RIGHT]:
        move_x += 0.01
    if keys[K_UP]:
        move_y -= 0.01
    elif keys[K_DOWN]:
        move_y = 0.01
    new_hexagon = which_platform(player.x + move_x, player.y + move_y)
    player_hexagon = which_platform(player.x, player.y)
    moving_up = new_hexagon != player_hexagon and new_hexagon == current_hex and height > 0
    if not moving_up and new_hexagon != -1:
        player.move(move_x, move_y)
    floor_height = 0 if current_hex == player_hexagon else height
    player.update(floor_height)
 
    if state == WAITING:
        waiting_delay -= 1
        if not waiting_delay:
            current_hex = randint(0, 6)
            state = FLAG_SHOWN
            delay = 150 # this is dumb

    if state == FLAG_SHOWN:
        delay -= 1
        if not delay:
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
            delay = 150
            current_hex = -1

    draw_level(current_hex, player_hexagon, height)
    draw_player(player.x, player.y, player.height)
    flip_graphics()

