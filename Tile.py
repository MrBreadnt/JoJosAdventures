import pygame

TILE_WIDTH = 40
TILE_IMAGES = {
    "bricks": pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load("res/test_bricks.jpg"), (TILE_WIDTH, TILE_WIDTH)), 90),
    "bricks2": pygame.transform.scale(pygame.image.load("res/test_bricks2.jpg"), (TILE_WIDTH, TILE_WIDTH)),
    "bricks3": pygame.transform.scale(pygame.image.load("res/test_bricks3.jpg"), (TILE_WIDTH, TILE_WIDTH))
}


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, tiles_group, pos_x, pos_y):
        super().__init__(tiles_group)
        self.image = TILE_IMAGES[tile_type]
        self.rect = pygame.Rect(pos_x, pos_y, TILE_WIDTH, TILE_WIDTH)
