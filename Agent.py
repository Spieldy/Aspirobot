from random import randint


class Robot(object):
    def __init__(self, mansion):
        self.mansion = mansion
        self.actuator = Actuator(mansion)
        self.sensor = Sensor(mansion)
        self.belief = None
        self.intentions = ''

    def turn_on(self):
        self.mansion.insert_robot()
        print("Domo Arigato Mr Roboto")
        while True:
            self.move()
            self.do()

    def update(self):
        self.move()
        self.do()

    def move(self):  # TODO up() right() etc does not work because it now needs to call Room.set_robot()
        r = randint(0, 3)  # TODO maybe add move commands to Mansion
        if r == 0:
            self.up()
        if r == 1:
            self.right()
        if r == 2:
            self.down()
        if r == 3:
            self.left()

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
