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
        if self.mansion.x_robot > 0:
            self.mansion.x_robot -= 1

    def down(self):
        if self.mansion.x_robot < (self.mansion.width - 1):
            self.mansion.x_robot += 1

    def left(self):
        if self.mansion.y_robot > 0:
            self.mansion.y_robot -= 1

    def right(self):
        if self.mansion.y_robot < (self.mansion.height - 1):
            self.mansion.y_robot += 1


class Actuator(object):
    def __init__(self, mansion):
        self.mansion = mansion

    def suck(self):
        self.mansion.suck_room()

    def pickup(self):
        self.mansion.pickup_room()


class Sensor(object):
    def __init__(self, mansion):
        self.mansion = mansion

    def get_mansion_state(self):
        return self.mansion.board
