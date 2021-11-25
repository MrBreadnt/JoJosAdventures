class Animation:
    def __init__(self, sprites, speed):
        self.sprites = sprites
        self.speed = speed
        self.time = 0
        self.current_frame = 0

    def get_current_frame(self, time):
        self.time += time
        if self.time > self.speed:
            self.current_frame += 1
            self.time = 0
        if self.current_frame >= len(self.sprites):
            self.current_frame = 0
        return self.sprites[self.current_frame]
