import csv
import sys
import pygame
import copy
from config import *


def intro(screen, clock):
    brgames_logo = pygame.image.load("res/br.png")
    brgames_logo = pygame.transform.scale(brgames_logo,
                                          (0.1 * brgames_logo.get_width(), 0.1 * brgames_logo.get_height()))
    yl_logo = pygame.image.load("res/yl.png")
    yl_logo = pygame.transform.scale(yl_logo,
                                     (0.5 * yl_logo.get_width(), 0.5 * yl_logo.get_height()))
    fase = 0
    logo = brgames_logo
    a = 0
    speed = 100
    is_going = True
    while is_going:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if a > 300:
            speed = -200
        if a < 0:
            a = 0
            fase += 1
            if fase >= 2:
                return
            speed = 100
        if fase == 0:
            logo = yl_logo
        elif fase == 1:
            logo = brgames_logo
        screen.fill(pygame.Color(0, 0, 0))
        logo.set_alpha(a)
        screen.blit(logo, (WIN_WIDTH / 2 - logo.get_width() / 2, WIN_HEIGHT / 2 - logo.get_height() / 2))
        a += speed / FPS
        pygame.display.flip()
        clock.tick(FPS)


def settings(screen, clock):
    logo = pygame.image.load("res/jojo_logo.png")
    logo = pygame.transform.scale(logo,
                                  (0.3 * logo.get_width(), 0.3 * logo.get_height()))
    bg = pygame.image.load("res/menu_bg.png")
    a = 0
    choose = 0
    speed = 100
    is_going = True
    font = pygame.font.Font("res/font.ttf", 36)
    font1 = pygame.font.Font("res/font.ttf", 40)
    font1.set_bold(True)
    texts = ['MUSIC', 'BACK']

    while is_going:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_s:
                    choose += 1
                    choose %= len(texts)
                elif e.key == pygame.K_w:
                    choose -= 1
                    choose %= len(texts)
                elif e.key == pygame.K_RETURN:
                    if choose == 0:
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    elif choose == 1:
                        return
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(pygame.Color(0, 0, 0))
        screen.blit(bg, (WIN_WIDTH / 2 - bg.get_width() / 2 + a, WIN_HEIGHT / 2 - bg.get_height() / 2))
        screen.blit(bg, (WIN_WIDTH / 2 + bg.get_width() / 2 + a, WIN_HEIGHT / 2 - bg.get_height() / 2))
        k = pygame.Surface((58, WIN_HEIGHT))
        k.fill(pygame.Color(0, 0, 0))
        screen.blit(k, (0, 0))
        screen.blit(k, (662, 0))
        y = 300
        for i in texts:
            f = font1 if (y - 300) // 40 == choose else font
            i = f.render(i, True, (255, 255, 255))
            screen.blit(i, (WIN_WIDTH / 2 - i.get_width() / 2, y))
            y += 40
        a -= 5
        if a <= -604:
            a = 0
        screen.blit(logo, (WIN_WIDTH / 2 - logo.get_width() / 2, logo.get_height() / 3))
        pygame.display.flip()
        clock.tick(FPS)


def top(screen, clock):
    logo = pygame.image.load("res/jojo_logo.png")
    logo = pygame.transform.scale(logo,
                                  (0.3 * logo.get_width(), 0.3 * logo.get_height()))
    bg = pygame.image.load("res/menu_bg.png")
    a = 0
    choose = 5
    speed = 100
    is_going = True
    font = pygame.font.Font("res/font.ttf", 36)
    font1 = pygame.font.Font("res/font.ttf", 40)
    font1.set_bold(True)
    scores = []
    with open('res/records.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            scores.append(row[0])
    texts = ['-' if i == '0' else i for i in sorted(scores, reverse=True)] + ['BACK']

    while is_going:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(pygame.Color(0, 0, 0))
        screen.blit(bg, (WIN_WIDTH / 2 - bg.get_width() / 2 + a, WIN_HEIGHT / 2 - bg.get_height() / 2))
        screen.blit(bg, (WIN_WIDTH / 2 + bg.get_width() / 2 + a, WIN_HEIGHT / 2 - bg.get_height() / 2))
        k = pygame.Surface((58, WIN_HEIGHT))
        k.fill(pygame.Color(0, 0, 0))
        screen.blit(k, (0, 0))
        screen.blit(k, (662, 0))
        y = 200
        for i in texts:
            f = font1 if (y - 200) // 40 == choose else font
            i = f.render(i, True, (255, 255, 255))
            screen.blit(i, (WIN_WIDTH / 2 - i.get_width() / 2, y))
            y += 40
        a -= 5
        if a <= -604:
            a = 0
        screen.blit(logo, (WIN_WIDTH / 2 - logo.get_width() / 2, logo.get_height() / 3))
        pygame.display.flip()
        clock.tick(FPS)


def menu(screen, clock):
    logo = pygame.image.load("res/jojo_logo.png")
    logo = pygame.transform.scale(logo,
                                  (0.3 * logo.get_width(), 0.3 * logo.get_height()))
    bg = pygame.image.load("res/menu_bg.png")
    a = 0
    choose = 0
    speed = 100
    is_going = True
    font = pygame.font.Font("res/font.ttf", 36)
    font1 = pygame.font.Font("res/font.ttf", 40)
    font1.set_bold(True)
    texts = ['PLAY', 'RECORDS', 'SETTINGS', 'EXIT']

    while is_going:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_s:
                    choose += 1
                    choose %= len(texts)
                elif e.key == pygame.K_w:
                    choose -= 1
                    choose %= len(texts)
                elif e.key == pygame.K_RETURN:
                    if choose == 0:
                        return
                    elif choose == 1:
                        top(screen, clock)
                    elif choose == 2:
                        settings(screen, clock)
                    elif choose == 3:
                        pygame.quit()
                        sys.exit()
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(pygame.Color(0, 0, 0))
        screen.blit(bg, (WIN_WIDTH / 2 - bg.get_width() / 2 + a, WIN_HEIGHT / 2 - bg.get_height() / 2))
        screen.blit(bg, (WIN_WIDTH / 2 + bg.get_width() / 2 + a, WIN_HEIGHT / 2 - bg.get_height() / 2))
        k = pygame.Surface((58, WIN_HEIGHT))
        k.fill(pygame.Color(0, 0, 0))
        screen.blit(k, (0, 0))
        screen.blit(k, (662, 0))
        y = 250
        for i in texts:
            f = font1 if (y - 250) // 40 == choose else font
            i = f.render(i, True, (255, 255, 255))
            screen.blit(i, (WIN_WIDTH / 2 - i.get_width() / 2, y))
            y += 40
        a -= 5
        if a <= -604:
            a = 0
        screen.blit(logo, (WIN_WIDTH / 2 - logo.get_width() / 2, logo.get_height() / 3))
        pygame.display.flip()
        clock.tick(FPS)


def outro(screen, clock, score):
    sc = pygame.transform.scale(screen, (WIN_WIDTH, WIN_HEIGHT))
    bg = pygame.image.load("res/menu_bg.png")
    a = 0
    o = 662
    choose = 3
    speed = 100
    is_going = True
    font = pygame.font.Font("res/font.ttf", 36)
    font1 = pygame.font.Font("res/font.ttf", 40)
    font1.set_bold(True)

    scores = []
    with open('res/records.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            scores.append(int(row[0]))
    scores.sort()
    if score > scores[0]:
        scores[0] = score
        with open('res/records.csv', 'w', newline='') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(5):
                writer.writerow([int(scores[i])])
    texts = ['SCORE', str(int(score)), '', 'BACK']

    while is_going:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(pygame.Color(0, 0, 0))
        screen.blit(bg, (WIN_WIDTH / 2 - bg.get_width() / 2, WIN_HEIGHT / 2 - bg.get_height() / 2 + a))
        screen.blit(bg, (WIN_WIDTH / 2 - bg.get_width() / 2, WIN_HEIGHT / 2 + bg.get_height() / 2 + a))
        k = pygame.Surface((58, WIN_HEIGHT))
        k.fill(pygame.Color(0, 0, 0))
        screen.blit(k, (0, 0))
        screen.blit(k, (662, 0))
        y = 200
        for i in texts:
            f = font1 if (y - 200) // 40 == choose else font
            i = f.render(i, True, (255, 255, 255))
            screen.blit(i, (WIN_WIDTH / 2 - i.get_width() / 2, y))
            y += 40
        a -= 5
        if a <= -463:
            a = 0
        font3 = pygame.font.Font("res/font.ttf", 90)
        font3.set_bold(True)
        t = font3.render('GAME OVER', True, (255, 255, 255))
        screen.blit(t, (WIN_WIDTH / 2 - t.get_width() / 2, t.get_height() / 3))
        sc2 = pygame.transform.scale(screen, (WIN_WIDTH, WIN_HEIGHT))
        screen.fill(pygame.Color(0, 0, 0))
        if o >= 58:
            o -= 5
        screen.blit(sc, (WIN_WIDTH / 2 + bg.get_width() / 2 - o, WIN_HEIGHT / 2 - sc.get_height() / 2))
        screen.blit(sc2, (WIN_WIDTH / 2 - bg.get_width() / 2 - o, WIN_HEIGHT / 2 - sc2.get_height() / 2))
        k = pygame.Surface((58, WIN_HEIGHT))
        k.fill(pygame.Color(0, 0, 0))
        screen.blit(k, (0, 0))
        screen.blit(k, (662, 0))
        pygame.display.flip()
        clock.tick(FPS)
