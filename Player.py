from AnimationManager import Animation
from Entity import Entity
import pygame

from config import *

ANIM = {0: Animation([pygame.transform.scale(pygame.image.load("res/pers.png"), (80, 80))], 0),
        1: Animation([pygame.transform.scale(pygame.image.load("res/pers_walk_1.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("res/pers_walk_2.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("res/pers_walk_3.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("res/pers_walk_2.png"), (80, 80))], 200),
        2: Animation([pygame.transform.scale(pygame.image.load("res/pers_jump.png"), (80, 80))], 0)}


class Player(Entity):
    def __init__(self, x, y, *group):
        super().__init__(x, y, ANIM, *group)
        self.attack = 1
        self.breath = 100
        self.attacking = False

    def update(self, *args, **kwargs):
        up, down, left, right = 0, 0, 0, 0
        e = pygame.key.get_pressed()
        # self.lives -= 0.1
        if e[pygame.K_d]:
            right = 1
            self.flip = False
        elif e[pygame.K_a]:
            left = -1
            self.flip = True
        if e[pygame.K_RETURN] and self.breath >= 30:
            self.attacking = True
        else:
            self.attacking = False
        if e[pygame.K_w]:
            up = -1
        elif e[pygame.K_s]:
            down = 1
        if e[pygame.K_SPACE]:
            self.jump(700)
        self.move(right, left, up, down, (None, (225, 375)))
        super().update(*args, **kwargs)
