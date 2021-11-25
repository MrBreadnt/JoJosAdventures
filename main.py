import pygame
from pygame import Color, Rect, draw, Surface
from time import sleep

WIN_WIDTH = 720
WIN_HEIGHT = 480
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"
FPS = 60


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
        self.d = 0
        self.speed = 0.2
        self.width, self.height = 50, 80

    def move(self, r, l, u, d, k):
        if self.z < 0:
            self.z -= self.d * k
            if self.z >= 0:
                self.z = 0
            self.d -= 0.003 * k
        else:
            self.z = 0
        if 225 < self.y + u * self.speed * k + self.height < 375:
            if u != 0:
                self.y += u * self.speed * k
            else:
                self.y += d * self.speed * k
        if r != 0:
            self.x += r * self.speed * k
        else:
            self.x += l * self.speed * k

    def jump(self, d):
        if self.z == 0:
            self.d = d
            self.z -= 0.00001


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("JoJo's bizarre adventures")

    map = [str('1' * 36) if 10 < i < 20 else str('0' * 36) for i in range(24)]

    up, down, left, right = 0, 0, 0, 0
    player = Player(50, 250)
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
                    player.jump(1)

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

        player.move(right, left, up, down, FPS * 0.5)
        screen.fill(Color(BACKGROUND_COLOR))
        draw.rect(screen, Color("gray"), Rect(0, 200, WIN_WIDTH, 200))
        # x = y = 0
        # for i in map:
        #     for j in i:
        #         if j == '1':
        #             pf = Surface((20, 20))
        #             pf.fill(Color(Color("red")))
        #             screen.blit(pf, (y, x))
        #     x += 20
        # y += 20
        # x = 0
        draw.rect(screen, Color("black"), Rect(player.x, player.y + player.width + 20, player.width, player.width / 2))
        draw.rect(screen, Color("white"), Rect(player.x, player.y + player.z, player.width, player.height))
        pygame.display.flip()
        clock.tick(FPS)
