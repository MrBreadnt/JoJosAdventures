from math import sqrt
from random import random, randint

from AnimationManager import Animation
from Entity import Entity
import pygame
from pygame.sprite import Sprite
from config import *

ANIM = {0: Animation([pygame.transform.scale(pygame.image.load("res/dio_0.png"), (80, 80))], 0),
        3: Animation([pygame.transform.scale(pygame.image.load("res/dio_1.png"), (80, 80))], 0)}


class Enemy(Entity):
    def __init__(self, x, y, *group):
        super().__init__(x, y, ANIM, *group)
        self.speed = self.speed - randint(10, 30)

    def update(self, *args, **kwargs):
        if len(args) > 1:
            length = sqrt((args[1].x - self.x) ** 2 + (args[1].y - self.y) ** 2)
            a = args[2].copy()
            a.remove(self)
            if length >= 80:
                self.move(0, -(self.x - args[1].x) / length, 0, -(self.y - args[1].y) / length, (None, (225, 375)))
            elif 0 < length <= 65:
                self.move((self.x - args[1].x) / length, 0, 0, 0, (None, (225, 375)))
            else:
                self.anim = self.data_anim[3]
                args[1].lives -= self.attack
                if args[1].attacking and self.flip != args[1].flip:
                    self.lives -= args[1].attack
            self.flip = args[1].rect[0] < self.rect[0]
            super().update(*args, **kwargs)
            if self.lives <= 0:
                self.kill()
