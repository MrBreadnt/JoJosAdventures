from AnimationManager import Animation
import pygame

ANIM = {0: Animation([pygame.transform.scale(pygame.image.load("res/pers.png"), (80, 80))], 0),
        1: Animation([pygame.transform.scale(pygame.image.load("res/pers_walk_1.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("res/pers_walk_2.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("res/pers_walk_3.png"), (80, 80)),
                      pygame.transform.scale(pygame.image.load("res/pers_walk_2.png"), (80, 80))], 200),
        2: Animation([pygame.transform.scale(pygame.image.load("res/pers_jump.png"), (80, 80))], 0)}


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
        self.d = 0
        self.speed = 200
        self.width, self.height = 80, 80
        self.anim = ANIM[0]

    def move(self, r, l, u, d, k):
        if 225 < self.y + u * self.speed * k + self.height < 375:
            if u != 0:
                self.y += u * self.speed * k
            else:
                self.y += d * self.speed * k
                self.anim = ANIM[1]
        if r != 0:
            self.x += r * self.speed * k
        else:
            self.x += l * self.speed * k
            self.anim = ANIM[1]
        if r == l == u == d:
            self.anim = ANIM[0]
        if self.z < 0:
            self.z -= self.d * k
            if self.z >= 0:
                self.z = 0
            self.d -= 3000 * k
            self.anim = ANIM[2]
        else:
            self.z = 0

    def jump(self, d):
        if self.z == 0:
            self.d = d
            self.z -= 0.00001
