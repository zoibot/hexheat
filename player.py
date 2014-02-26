GROUNDED = 0
IN_AIR = 2
 
class Player(object):
    x = y = 0
    y_velocity = 0
    height = 0
    state = GROUNDED

    def update(self, floor_height):
        self.height -= self.y_velocity
        self.y_velocity -= 0.01
        if self.height + 0.02 >= floor_height:
            self.height = floor_height
            self.state = GROUNDED
            self.y_velocity = 0
        else:
            self.height += 0.02
            self.state = IN_AIR

    def move(self, x, y):
        self.x += x
        self.y += y

    def jump(self):
        if self.state == GROUNDED:
            self.y_velocity = 0.1

