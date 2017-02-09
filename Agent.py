class Robot(object):
    def __init__(self, wide, height):
        self.w = wide
        self.h = height
        self.x = self.w / 2
        self.y = self.h / 2

    def up(self):
        if self.x > 0:
            self.x -= 1
            return True
        else:
            return False

    def down(self):
        if self.x < self.w - 1:
            self.x += 1
            return True
        else:
            return False

    def left(self):
        if self.y > 0:
            self.y -= 1
            return True
        else:
            return False

    def right(self):
        if self.y < self.h - 1:
            self.y += 1
            return True
        else:
            return False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
