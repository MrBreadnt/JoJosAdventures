import pygame

from EntityGroup import EntityGroup
from HamonEffect import HamonEffect
from pygame import Color, Rect, draw, Surface
from config import *
from AnimationManager import Animation
from Entity import Entity
from Player import ANIM, Player

ANIM_D = {0: Animation([pygame.transform.scale(pygame.image.load("res/dio_0.png"), (80, 80))], 0)}

bricks = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("res/test_bricks.jpg"), (40, 40)), 90)
bricks2 = pygame.transform.scale(pygame.image.load("res/test_bricks2.jpg"), (40, 40))
bricks3 = pygame.transform.scale(pygame.image.load("res/test_bricks3.jpg"), (40, 40))
pers = pygame.transform.scale(pygame.image.load("res/pers.png"), (80, 80))
bar_empty = pygame.image.load("res/bar_0.png")
bar_full = pygame.image.load("res/bar_1.png")


class Game:
    def __init__(self, screen, clock):
        self.entity = EntityGroup()
        self.enemy = EntityGroup()
        self.player = Player(50, 250, self.entity)
        self.screen = screen
        self.clock = clock

    def start(self):

        breath = 100
        entity = Entity(490, 290, ANIM_D, self.entity)
        entity2 = Entity(320, 200, ANIM_D, self.entity)
        entity3 = Entity(230, 250, ANIM_D, self.entity)

        world_map = [str('1' * 18) if 5 <= i <= 9 else str('0' * 18) if 10 <= i else str('0' * 18) for i in range(12)]
        world_map[3] = "0000200002000020000"

        attacking = False
        up, down, left, right = 0, 0, 0, 0
        is_going = True
        light = HamonEffect(0, 0, 0, 0)
        while is_going:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_d:
                        right = 1
                        self.player.flip = False
                    elif e.key == pygame.K_a:
                        left = -1
                        self.player.flip = True
                    if e.key == pygame.K_w:
                        up = -1
                    elif e.key == pygame.K_s:
                        down = 1
                    if e.key == pygame.K_SPACE:
                        self.player.jump(700)

                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_d:
                        right = 0
                    if e.key == pygame.K_a:
                        left = 0
                    if e.key == pygame.K_w:
                        up = 0
                    if e.key == pygame.K_s:
                        down = 0

                if e.type == pygame.MOUSEBUTTONDOWN:
                    if breath >= 30:
                        light = HamonEffect(100, 50, 4, 42)
                        attacking = True

                elif e.type == pygame.MOUSEBUTTONUP:
                    light = HamonEffect(0, 0, 0, 0)
                    attacking = False

                elif e.type == pygame.QUIT:
                    is_going = False

            if attacking:
                breath -= 20 / FPS
                if breath <= 0:
                    breath = 0
                    attacking = False
                    light = HamonEffect(0, 0, 0, 0)
            else:
                breath += 10 / FPS
                if breath > 100: breath = 100

            self.player.move(right, left, up, down, 1 / FPS, (None, (225, 375)))
            self.screen.fill(Color("#004400"))
            x = y = 0
            for i in world_map:
                for j in i:
                    pf = Surface((40, 40))
                    if j == '1':
                        pf.blit(bricks, (0, 0))
                    elif j == '2':
                        pf.blit(bricks3, (0, 0))
                    else:
                        pf.blit(bricks2, (0, 0))
                    self.screen.blit(pf, (x, y))
                    x += 40
                y += 40
                x = 0
            self.entity.update(self.clock.get_time())
            self.entity.draw(self.screen)
            # for entity in sorted((entity + [self.player]), key=lambda x: x.y):
            #     if entity == self.player:
            #         self.screen.blit(
            #             pygame.transform.flip(self.player.image, self.player.flip, False),
            #             (self.player.x, self.player.y + self.player.z))
            #     else:
            #         self.screen.blit(entity.anim.get_current_frame(self.clock.get_time()),
            #                          (entity.x, entity.y + entity.z))
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
