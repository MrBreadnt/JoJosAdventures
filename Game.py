import pygame
from pygame import Color, Rect, draw, Surface
from config import *


class Game:
    def __init__(self, screen, player, clock):
        self.screen = screen
        self.player = player
        self.clock = clock

    def start(self):
        map = [str('1' * 36) if 10 < i < 20 else str('0' * 36) for i in range(24)]

        up, down, left, right = 0, 0, 0, 0
        is_going = True
        while is_going:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_d:
                        right = 1
                    elif e.key == pygame.K_a:
                        left = -1
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
            draw.rect(self.screen, Color("gray"), Rect(0, 200, WIN_WIDTH, 200))
            # x = y = 0
            # for i in map:
            #     for j in i:
            #         if j == '1':
            #             pf = Surface((20, 20))
            #             pf.fill(Color(Color("red")))
            #             self.screen.blit(pf, (y, x))
            #     x += 20
            # y += 20
            # x = 0
            draw.rect(self.screen, Color("black"),
                      Rect(self.player.x, self.player.y + self.player.width + 20, self.player.width,
                           self.player.width / 2))
            draw.rect(self.screen, Color("white"),
                      Rect(self.player.x, self.player.y + self.player.z, self.player.width, self.player.height))
            pygame.display.flip()
            self.clock.tick(FPS)

    pygame.quit()
