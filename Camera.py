from config import *


class Camera:
    def __init__(self):
        self.dx = 0

    def apply(self, obj):
        obj.rect.x += self.dx

    def update(self, target):
        if target.rect.x > WIN_WIDTH - 200:
            self.dx = -1
        elif target.rect.x < 200:
            if target.x > 200:
                self.dx = 1
        else:
            self.dx = 0
