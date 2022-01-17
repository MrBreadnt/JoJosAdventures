from AnimationManager import Animation
import pygame
from config import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, anim, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.z = 0
        self.lives = 100
        self.attack = 0.1
        self.d = 0
        self.speed = 200
        self.rect = pygame.Rect(x, y, 80, 80)
        self.width, self.height = 80, 80
        self.data_anim = anim
        self.anim = self.data_anim[0]
        self.image = self.anim.get_current_frame(0)
        self.flip = False

    def move(self, r, l, u, d, rect):
        if not rect[1] or rect[1][0] < self.y + u * self.speed * 1 / FPS + self.height < rect[1][1]:
            if u != 0:
                self.y += u * self.speed * 1 / FPS
            else:
                self.y += d * self.speed * 1 / FPS
            if 1 in self.data_anim.keys():
                self.anim = self.data_anim[1]
        if r != 0:
            self.x += r * self.speed * 1 / FPS
            if 1 in self.data_anim.keys():
                self.anim = self.data_anim[1]
        else:
            self.x += l * self.speed * 1 / FPS
        if r == l == u == d:
            self.anim = self.data_anim[0]
        if self.z < 0:
            self.z -= self.d * 1 / FPS
            if self.z >= 0:
                self.z = 0
            self.d -= 3000 * 1 / FPS
            if 2 in self.data_anim.keys():
                self.anim = self.data_anim[2]
        else:
            self.z = 0

    def jump(self, d):
        if self.z == 0:
            self.d = d
            self.z -= 0.00001

    def update(self, *args, **kwargs):
        self.rect = pygame.Rect(self.x, self.y + self.z, self.width, self.height)
        if self.flip:
            self.image = pygame.transform.flip(self.anim.get_current_frame(args[0]), self.flip, False)
        else:
            self.image = self.anim.get_current_frame(args[0])
