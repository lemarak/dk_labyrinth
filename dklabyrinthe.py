# -*- coding: utf-8 -*-

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
import pygame.locals as py

import classes as cl
import constantes as c

def main():
    pygame.init()
    
    # initialisation window
    window = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
    
    # icon
    icon = pygame.image.load(c.IMG_ICON)
    pygame.display.set_icon(icon)
    
    # title
    pygame.display.set_caption(c.TXT_TITLE)
    
    # main loop
    progress = 1
    
    while progress:
        # load and refresh window
        home = pygame.image.load(c.IMG_HOME).convert()
        window.blit(home, (0, 0))
        pygame.display.flip()
    
        progress_menu = 1
        progress_game = 1
    
        # menu loop
        while progress_menu:
    
            # limit speed
            pygame.time.Clock().tick(30)
            level_file = ""
            for event in pygame.event.get():
                # level choice
                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        progress, progress_menu, progress_game = 0, 0, 0
                    if event.key == py.K_F1:
                        progress_menu, progress_game = 0, 1
                        level_file = "n1"
                    elif event.key == py.K_F2:
                        progress_menu, progress_game = 0, 1
                        level_file = "n2"
                    else:
                        level_file = ""
    
            if level_file != "":
                # load background
                background = pygame.image.load(c.IMG_BACKGROUND).convert()
                window.blit(background, (0, 0))
    
                # load level
                level_structure = cl.Level(level_file)
                level_structure.generate_level()
    
                # display level
                level_structure.display_level(window)
    
                # create avatar
                avatar = cl.Avatar(level_structure)
                pygame.display.flip()
    
        # game loop
        while progress_game:
    
            # limit speed
            pygame.time.Clock().tick(30)
    
            # loop for KEYDOWN
            for event in pygame.event.get():

                if event.type == py.KEYDOWN:
                    # escape for quit the game
                    if event.key == py.K_ESCAPE:
                        progress_menu, progress_game = 1, 0
                    # all directions
                    key_press = [py.K_RIGHT, py.K_LEFT, 
                                 py.K_UP, py.K_DOWN]
                    if event.key in key_press:
                        avatar.move_avatar(event.key)
            print(avatar.case_x, avatar.case_y)
            if (avatar.case_x, avatar.case_y) == (c.NB_SPRITES - 1, c.NB_SPRITES - 1):
                you_win = pygame.image.load(c.IMG_YOU_WIN).convert()
                window.blit(you_win, (0, 0))
            else:
                window.blit(background, (0, 0))
                level_structure.display_level(window)
                window.blit(avatar.position_avatar, (avatar.x, avatar.y))
            pygame.display.flip()

if __name__ == "__main__":
    main()