from math import sqrt
from random import random, randint

from AnimationManager import Animation
from Entity import Entity
import pygame
from config import *

ANIM = {0: Animation([pygame.transform.scale(pygame.image.load("res/dio_0.png"), (80, 80))], 0)}


class Enemy(Entity):
    def __init__(self, x, y, *group):
        super().__init__(x, y, ANIM, *group)
        self.speed = self.speed - randint(10, 30)

    def update(self, *args, **kwargs):
        if len(args) > 1:
            length = sqrt((args[1].x - self.x) ** 2 + (args[1].y - self.y) ** 2)
            if length >= 80:
                self.move(0, -(self.x - args[1].x) / length, 0, -(self.y - args[1].y) / length, (None, (225, 375)))
            # self.x -= (self.x - args[1].x) / length * self.speed * 1/FPS
            # self.y -= (self.y - args[1].y) / length * self.speed * 1/FPS
            elif 0 < length <= 65:
                self.move((self.x - args[1].x) / length, 0, 0, 0, (None, (225, 375)))
            self.flip = args[1].rect[0] < self.rect[0]
            super().update(*args, **kwargs)
