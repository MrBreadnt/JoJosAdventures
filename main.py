import pygame
from Player import Player
from Game import Game
from config import *

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("JoJo's bizarre adventures")
    game = Game(screen, clock)
    game.start()
