class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
        self.d = 0
        self.speed = 200
        self.width, self.height = 80, 80

    def move(self, r, l, u, d, k):
        if self.z < 0:
            self.z -= self.d * k
            if self.z >= 0:
                self.z = 0
            self.d -= 3000 * k
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
