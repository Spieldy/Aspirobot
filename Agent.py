class Robot(object):
    def __init__(self, mansion):
        self.mansion = mansion
        self.x = self.mansion.width / 2
        self.y = self.mansion.height / 2
        self.actuator = Actuator(mansion)
        self.sensor = Sensor(mansion)

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


class Actuator(object):
    def __init__(self, mansion):
        self.mansion = mansion

    def suck(self, x, y):
        self.mansion.suck_room(x, y)

    def pickup(self, x, y):
        self.mansion.pickup_room(x, y)


class Sensor(object):
    def __init__(self, mansion):
        self.mansion = mansion

    def get_mansion_state(self):
        return self.mansion.board
