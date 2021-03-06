"""
|<-------------------------------------------------------------------------->|
|<------------------------------------------------------------------->|
Spaced Out: The Space Game
by Philip deZonia, started on 2017-02-05 on a rainy day in Verona.
This is the main function that calls all the functions and classes.
Will be used for testing classes in early stages of development.
This is the refactored version of space_game_main.py
"""

import os
import sys
from math import *
import pygame
import ship
import station

# initialize variables
is_done = False
screen_width = 1200
screen_height = 900

# i don't know what this does
pygame.init()

# create game objects
clock = pygame.time.Clock()
window = pygame.display.set_mode((screen_width, screen_height))
game_font = pygame.font.Font(None, 36)
player_pos = [600, 450]
player_ship = ship.Ship('Applecat', player_pos)
npc_ship = ship.Ship('Applecat', [1000, 600])
station1 = station.Station('Loanne', [600, 1000])


# game loop
while not is_done:
    # go through event queue
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN 
            and event.key == pygame.K_ESCAPE)):
            is_done = True
    # [w, s, d, a, shift, ctrl, space]
    inputs = [0, 0, 0, 0, 0, 0, 0]
    if pygame.key.get_pressed()[pygame.K_w]: inputs[0] = 1
    if pygame.key.get_pressed()[pygame.K_s]: inputs[1] = 1
    if pygame.key.get_pressed()[pygame.K_a]: inputs[3] = 1
    if pygame.key.get_pressed()[pygame.K_d]: inputs[2] = 1
    if pygame.key.get_pressed()[pygame.K_LSHIFT]: inputs[4] = 1
    if pygame.key.get_pressed()[pygame.K_LCTRL]: inputs[5] = 1
    if pygame.key.get_pressed()[pygame.K_SPACE]: inputs[6] = 1
    # calculate turret angle
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    turr_ang = degrees(atan2(-mouse_y + screen_height/2, 
                       mouse_x - screen_width/2))
    player_pos = player_ship.motion(
        inputs, turr_ang, [player_pos[0] - screen_width/2,
        player_pos[1] - screen_height/2])
    npc_ship.motion([0, 0, 0, 0, 0, 0, 0], 0, player_pos)
    station1.motion(player_pos)
    """ end of loop work """
    window.fill((50, 50, 50))
    player_ship.render(window)
    npc_ship.render(window)
    station1.render(window)
    pygame.display.flip()
    clock.tick(60)