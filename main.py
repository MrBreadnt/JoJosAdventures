import pygame
from Player import Player
from Game import Game
from config import *

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("JoJo's bizarre adventures")
    player = Player(50, 250)
    game = Game(screen, player, clock)
    game.start()
