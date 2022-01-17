import sys

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
health = pygame.transform.scale(pygame.image.load("res/health.png"), (
    0.25 * pygame.image.load("res/health.png").get_width(), 0.2 * pygame.image.load("res/health.png").get_height()))


class Game:
    def __init__(self, screen, clock):
        self.entity = EntityGroup()
        self.player = Player(50, 250, self.entity)
        self.screen = screen
        self.clock = clock

    def start(self):
        camera = Camera()
        enemy = [Enemy(490, 290, self.entity), Enemy(320, 200, self.entity), Enemy(230, 250, self.entity)]
        score = sum(map(lambda it: it.lives, self.entity.sprites()))
        map_sprite = pygame.sprite.Group()
        world_map = [str('1' * 36) if 5 <= i <= 9 else str('0' * 36) if 10 <= i else str('0' * 36) for i in range(12)]
        world_map[3] = str([("0" if i % 1 != 0 else "2") for i in range(36)])

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

        is_going = True
        light = HamonEffect(100, 50, 4, 42)
        while is_going:
            for e in pygame.event.get():

                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.player.attacking:
                self.player.breath -= 20 / FPS
                if self.player.breath <= 0:
                    self.player.breath = 0
                    self.player.attacking = False
                    light = HamonEffect(0, 0, 0, 0)
            else:
                self.player.breath += 10 / FPS
                if self.player.breath > 100:
                    self.player.breath = 100

            self.screen.fill(Color("#004400"))
            self.entity.update(self.clock.get_time(), self.player, enemy, score)
            map_sprite.draw(self.screen)
            self.entity.draw(self.screen)
            if self.player.attacking:
                for lm in light.get_effect():
                    draw.lines(self.screen, light.color, False,
                               list(map(lambda m: (
                                   self.player.x + m[0] * (-1 if self.player.flip else 1) + (
                                       40 if self.player.flip else 40),
                                   self.player.y + self.player.z + m[1] + 30), lm)),
                               width=1)
            self.screen.blit(bar_empty, (20, 20))
            t = Surface((self.player.breath, 40))
            t.blit(bar_full, (0, 0))
            self.screen.blit(t, (20, 20))
            draw.rect(self.screen, Color("red"),
                      Rect(WIN_WIDTH - health.get_width() + 5, 26, (health.get_width() - 27) / 100 * self.player.lives,
                           health.get_height() - 10))
            self.screen.blit(health, (WIN_WIDTH - health.get_width() - 20, 20))
            sc = pygame.transform.scale(self.screen, (604, 463))
            self.screen.fill(Color(0, 0, 0))
            self.screen.blit(sc, (WIN_WIDTH / 2 - sc.get_width() / 2, WIN_HEIGHT / 2 - sc.get_height() / 2))
            if self.player.lives <= 0:
                return score + self.player.lives - sum(
                    map(lambda it: it.lives, self.entity.sprites())) - 100 + self.player.lives
            if len(self.entity.sprites()) == 1:
                return score + self.player.lives - sum(
                    map(lambda it: it.lives, self.entity.sprites())) - 100 + self.player.lives
            pygame.display.flip()
            self.clock.tick(FPS)
