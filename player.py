GROUNDED = 0
JUMPING = 1
FALLING = 2
 
class Player(object):
    x = y = 0
    height = 0
    jump_duration = 0
    state = GROUNDED

    def update(self, floor_height):
        if self.state == JUMPING:
            self.height -= 0.05
            self.jump_duration -= 1
            if not self.jump_duration:
                self.state = FALLING
        else:
            if self.height + 0.03 >= floor_height:
                self.height = floor_height
                self.state = GROUNDED
            else:
                self.height += 0.03
                self.state = FALLING

    def move(self, x, y):
        self.x += x
        self.y += y

    def jump(self):
        if self.state == GROUNDED:
            self.state = JUMPING
            self.jump_duration = 10

