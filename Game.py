import pygame
from HamonEffect import HamonEffect
from pygame import Color, Rect, draw, Surface
from config import *
from AnimationManager import Animation

bricks = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("res/test_bricks.jpg"), (40, 40)), 90)
bricks2 = pygame.transform.scale(pygame.image.load("res/test_bricks2.jpg"), (40, 40))
bricks3 = pygame.transform.scale(pygame.image.load("res/test_bricks3.jpg"), (40, 40))
pers = pygame.transform.scale(pygame.image.load("res/pers.png"), (80, 80))
bar_empty = pygame.image.load("res/bar_0.png")
bar_full = pygame.image.load("res/bar_1.png")


class Game:
    def __init__(self, screen, player, clock):
        self.screen = screen
        self.player = player
        self.clock = clock

    def start(self):
        breath = 100

        world_map = [str('1' * 18) if 5 <= i <= 9 else str('0' * 18) if 10 <= i else str('0' * 18) for i in range(12)]
        world_map[3] = "0000200002000020000"

        attacking = False
        up, down, left, right, flip = 0, 0, 0, 0, False
        is_going = True
        light = HamonEffect(0, 0, 0, 0)
        light2 = HamonEffect(0,0,0,0)#300, 50, 1, 70)
        while is_going:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_d:
                        right = 1
                        flip = False
                    elif e.key == pygame.K_a:
                        left = -1
                        flip = True
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

            self.player.move(right, left, up, down, 1 / FPS)
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
            t = Surface((self.player.width - 15, self.player.width / 2), pygame.SRCALPHA)
            draw.ellipse(t, Color(0, 0, 0, 150),
                         Rect(0, 0, self.player.width - 15,
                              self.player.width / 2))
            self.screen.blit(t, (self.player.x + (-5 if flip else 15), self.player.y + self.player.width - 20))
            self.screen.blit(
                pygame.transform.flip(self.player.anim.get_current_frame(self.clock.get_time()), flip, False),
                (self.player.x, self.player.y + self.player.z))
            # draw.rect(self.screen, Color("white"),
            #         Rect(self.player.x, self.player.y + self.player.z, self.player.width, self.player.height))
            for lm in light.get_effect():
                draw.lines(self.screen, light.color, False,
                           list(map(lambda m: (
                               self.player.x + m[0] * (-1 if flip else 1) + (40 if flip else 40),
                               self.player.y + self.player.z + m[1] + 30), lm)),
                           width=1)
            for lm in light2.get_effect():
                draw.lines(self.screen, light.color, False, list(map(lambda x: (x[1]+ 250, x[0]), lm)), width=1)
            self.screen.blit(bar_empty, (20, 20))
            t = Surface((breath, 40))
            t.blit(bar_full, (0, 0))
            self.screen.blit(t, (20, 20))
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
