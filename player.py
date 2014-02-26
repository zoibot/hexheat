class Player(object):
    x = y = 0
    height = 0

    def update(self, floor_height):
        height = floor_height

    def move(self, x, y):
        self.x += x
        self.y += y


