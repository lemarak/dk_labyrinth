# -*- coding: utf-8 -*-

"""
CLasses for the DK Labyrinth game
"""

import pygame
import pygame.locals as py

import constantes as c


# Class LEVEL
class Level:

    def __init__(self, num_file):

        self.level_file = c.PATH_LEVELS + num_file + ".txt"
        self.struct_level = []

    # generate the sprites for a level
    def generate_level(self):

        with open(self.level_file, "r") as file:
            # generate 1 row
            for row in file:
                struct_row = []
                for sprite in row:
                    if sprite != "\n":
                        struct_row.append(sprite)
                self.struct_level.append(struct_row)

    # display the sprites of the level
    def display_level(self, window):

        # initialize pictures
        wall = pygame.image.load(c.IMG_WALL).convert()
        departure = pygame.image.load(c.IMG_DEPARTURE).convert()
        arrival = pygame.image.load(c.IMG_ARRIVAL).convert()

        # intialize positions
        pos_x, pos_y = 0, 0

        # loop on structure
        for row in self.struct_level:
            pos_x = 0
            for sprite in row:
                if sprite == 'm':
                    window.blit(wall, (pos_x, pos_y))
                elif sprite == 'd':
                    window.blit(departure, (pos_x, pos_y))
                elif sprite == 'a':
                    window.blit(arrival, (pos_x, pos_y))
                pos_x += c.SIZE_SPRITE

            pos_y += c.SIZE_SPRITE


# Class AVATAR
class Avatar:

    def __init__(self, level):
        self.right = pygame.image.load(c.IMG_RIGHT).convert_alpha()
        self.left = pygame.image.load(c.IMG_LEFT).convert_alpha()
        self.up = pygame.image.load(c.IMG_UP).convert_alpha()
        self.down = pygame.image.load(c.IMG_DOWN).convert_alpha()

        self.x = 0
        self.y = 0

        self.case_x = 0
        self.case_y = 0

        self.position_avatar = self.right
        self.level = level

    def move_avatar(self, direction):

        # move right
        if direction == py.K_RIGHT:
            if self.case_x < c.NB_SPRITES - 1:
                # if OK (no wall)
                if self.level.struct_level[self.case_y][self.case_x + 1] != 'm':
                    self.case_x += 1
                self.x = self.case_x * c.SIZE_SPRITE
            self.position_avatar = self.right

        # move left
        if direction == py.K_LEFT:
            if self.case_x > 0:
                # if OK (no wall)
                if self.level.struct_level[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                self.x = self.case_x * c.SIZE_SPRITE
            self.position_avatar = self.left

        # move up
        if direction == py.K_UP:
            if self.case_y > 0:
                # if OK (no wall)
                if self.level.struct_level[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                self.y = self.case_y * c.SIZE_SPRITE
            self.position_avatar = self.up

        # move down
        if direction == py.K_DOWN:
            if self.case_y < c.NB_SPRITES - 1:
                # if OK (no wall)
                if self.level.struct_level[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                self.y = self.case_y * c.SIZE_SPRITE
            self.position_avatar = self.down
