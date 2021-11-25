import pygame, os
from pygame import Color, Rect, draw, Surface
from config import *

bricks = pygame.transform.scale(pygame.image.load("res/test_bricks.jpg"), (40, 40))
bricks2 = pygame.transform.scale(pygame.image.load("res/test_bricks2.jpg"), (40, 40))
bricks3 = pygame.transform.scale(pygame.image.load("res/test_bricks3.jpg"), (40, 40))
pers = pygame.transform.scale(pygame.image.load("res/pers.png"), (80, 80))


class Game:
    def __init__(self, screen, player, clock):
        self.screen = screen
        self.player = player
        self.clock = clock

    def start(self):
        map = [str('1' * 18) if 5 <= i <= 9 else str('0' * 18) if 10 <= i else str('0' * 18) for i in range(12)]
        map[3] = "0000200002000020000"

        up, down, left, right, flip = 0, 0, 0, 0, False
        is_going = True
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
                        self.player.jump(1000)

                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_d:
                        right = 0
                    if e.key == pygame.K_a:
                        left = 0
                    if e.key == pygame.K_w:
                        up = 0
                    if e.key == pygame.K_s:
                        down = 0

                elif e.type == pygame.QUIT:
                    is_going = False

            self.player.move(right, left, up, down, 1 / FPS)
            self.screen.fill(Color("#004400"))
            x = y = 0
            for i in map:
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
            t = Surface((self.player.width-15, self.player.width / 2), pygame.SRCALPHA)
            draw.ellipse(t, Color(0, 0, 0, 150),
                         Rect(0, 0, self.player.width-15,
                              self.player.width / 2))
            self.screen.blit(t, (self.player.x+(-5 if flip else 15), self.player.y + self.player.width - 20))
            self.screen.blit(pygame.transform.flip(pers, flip, False), (self.player.x, self.player.y + self.player.z))
            # draw.rect(self.screen, Color("white"),
            #         Rect(self.player.x, self.player.y + self.player.z, self.player.width, self.player.height))
            pygame.display.flip()
            self.clock.tick(FPS)

    pygame.quit()
