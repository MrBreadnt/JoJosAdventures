import pygame
from Player import Player
from Game import Game
from config import *
import os, csv
from Intro import *

if __name__ == "__main__":
    pygame.init()
    if not os.access("res/records.csv", os.F_OK):
        with open('res/records.csv', 'w', newline='') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(5):
                writer.writerow([0])
    pygame.mixer.music.load('res/music_op.mp3')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("JoJo's bizarre adventures")
    #intro(screen, clock)
    is_running = True
    while is_running:
        pygame.mixer.music.play()
        menu(screen, clock)
        game = Game(screen, clock)
        outro(screen, clock, game.start(0, 0))
    pygame.quit()
