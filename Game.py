import pygame

from Camera import Camera
from EntityGroup import EntityGroup
from HamonEffect import HamonEffect
from pygame import Color, Rect, draw, Surface

from Tile import Tile
from config import *
from AnimationManager import Animation
from Entity import Entity
from Enemy import Enemy
from Player import Player

pers = pygame.transform.scale(pygame.image.load("res/pers.png"), (80, 80))
bar_empty = pygame.image.load("res/bar_0.png")
bar_full = pygame.image.load("res/bar_1.png")


class Game:
    def __init__(self, screen, clock):
        self.entity = EntityGroup()
        self.player = Player(50, 250, self.entity)
        self.screen = screen
        self.clock = clock

    def start(self):
        camera = Camera()
        breath = 100
        _ = [Enemy(490, 290, self.entity), Enemy(320, 200, self.entity), Enemy(230, 250, self.entity)]
        map_sprite = pygame.sprite.Group()
        world_map = [str('1' * 36) if 5 <= i <= 9 else str('0' * 36) if 10 <= i else str('0' * 36) for i in range(12)]
        world_map[3] = str(["0" if i % 1 != 0 else "2" for i in range(36)])

        x = y = 0
        for i in world_map:
            for j in i:
                if j == '1':
                    Tile('bricks', map_sprite, x, y)
                elif j == '2':
                    Tile('bricks3', map_sprite, x, y)
                else:
                    Tile('bricks2', map_sprite, x, y)
                x += 40
            y += 40
            x = 0

        attacking = False
        is_going = True
        light = HamonEffect(0, 0, 0, 0)
        while is_going:
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if breath >= 30:
                        light = HamonEffect(100, 50, 4, 42)
                        attacking = True

                elif e.type == pygame.MOUSEBUTTONUP:
                    light = HamonEffect(0, 0, 0, 0)
                    attacking = False

                if e.type == pygame.QUIT:
                    is_going = False

            if attacking:
                breath -= 20 / FPS
                if breath <= 0:
                    breath = 0
                    attacking = False
                    light = HamonEffect(0, 0, 0, 0)
            else:
                breath += 10 / FPS
                if breath > 100:
                    breath = 100

            self.screen.fill(Color("#004400"))
            # x = y = 0
            # for i in world_map:
            #     for j in i:
            #         pf = Surface((40, 40))
            #         if j == '1':
            #             pf.blit(bricks, (0, 0))
            #         elif j == '2':
            #             pf.blit(bricks3, (0, 0))
            #         else:
            #             pf.blit(bricks2, (0, 0))
            #         self.screen.blit(pf, (x, y))
            #         x += 40
            #     y += 40
            #     x = 0
            self.entity.update(self.clock.get_time(), self.player)
            camera.update(self.player)
            for i in self.entity:
                camera.apply(i)
            for i in map_sprite:
                camera.apply(i)
            map_sprite.draw(self.screen)
            self.entity.draw(self.screen)
            for lm in light.get_effect():
                draw.lines(self.screen, light.color, False,
                           list(map(lambda m: (
                               self.player.x + m[0] * (-1 if self.player.flip else 1) + (
                                   40 if self.player.flip else 40),
                               self.player.y + self.player.z + m[1] + 30), lm)),
                           width=1)
            self.screen.blit(bar_empty, (20, 20))
            t = Surface((breath, 40))
            t.blit(bar_full, (0, 0))
            self.screen.blit(t, (20, 20))
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
