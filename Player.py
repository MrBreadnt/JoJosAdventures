from AnimationManager import Animation
from Entity import Entity
import pygame

ANIM = {0: Animation([pygame.transform.scale(pygame.image.load("res/pers.png"), (80, 80))], 0),
        1: Animation([pygame.transform.scale(pygame.image.load("res/pers_walk_1.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("res/pers_walk_2.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("res/pers_walk_3.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("res/pers_walk_2.png"), (80, 80))], 200),
        2: Animation([pygame.transform.scale(pygame.image.load("res/pers_jump.png"), (80, 80))], 0)}


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, ANIM)
