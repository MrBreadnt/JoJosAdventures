from AnimationManager import Animation
import pygame


class Entity:
    def __init__(self, x, y, anim):
        self.x = x
        self.y = y
        self.z = 0
        self.d = 0
        self.speed = 200
        self.width, self.height = 80, 80
        self.data_anim = anim
        self.anim = self.data_anim[0]

    def move(self, r, l, u, d, k, rect):
        if not rect[1] or rect[1][0] < self.y + u * self.speed * k + self.height < rect[1][1]:
            if u != 0:
                self.y += u * self.speed * k
            else:
                self.y += d * self.speed * k
                self.anim = self.data_anim[1]
        if r != 0:
            self.x += r * self.speed * k
        else:
            self.x += l * self.speed * k
            self.anim = self.data_anim[1]
        if r == l == u == d:
            self.anim = self.data_anim[0]
        if self.z < 0:
            self.z -= self.d * k
            if self.z >= 0:
                self.z = 0
            self.d -= 3000 * k
            self.anim = self.data_anim[2]
        else:
            self.z = 0

    def jump(self, d):
        if self.z == 0:
            self.d = d
            self.z -= 0.00001
