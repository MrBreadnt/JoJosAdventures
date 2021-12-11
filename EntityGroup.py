import pygame


class EntityGroup(pygame.sprite.AbstractGroup):
    def __init__(self):
        super().__init__()

    def draw(self, surface):
        sprites = sorted(self.sprites(), key=lambda x: x.y)
        for spr in sprites:
            t = pygame.Surface((spr.rect[2] - 15, spr.rect[3] / 2), pygame.SRCALPHA)
            pygame.draw.ellipse(t, pygame.Color(0, 0, 0, 120),
                         pygame.Rect(0, 0, spr.rect[2] - 15,
                              spr.rect[2] / 2))
            surface.blit(t, (spr.rect[0] + (-5 if spr.flip else 15), spr.y + spr.rect[2] - 20))
        if hasattr(surface, "blits"):
            self.spritedict.update(
                zip(
                    sprites,
                    surface.blits((spr.image, spr.rect) for spr in sprites)
                )
            )
        else:
            for spr in sprites:
                self.spritedict[spr] = surface.blit(spr.image, spr.rect)
        self.lostsprites = []
