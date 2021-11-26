from random import uniform, randint


class HamonEffect:
    def __init__(self, width, height, count, verts):
        self.width = width
        self.height = height
        self.count = count
        self.verts = verts
        self.color = "yellow"

    def get_effect(self):
        a = []
        for _ in range(self.count):
            light = []
            k = uniform(-5,5)
            verts = randint(self.verts//2, self.verts)
            for i in range(verts):
                light.append((i * self.width / self.verts, k))
                k += uniform(-3, 3)
            a.append(light)
        return a
