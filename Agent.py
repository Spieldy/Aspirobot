from random import randint


class Robot(object):
    def __init__(self, mansion):
        self.mansion = mansion
        self.actuator = Actuator(mansion)
        self.sensor = Sensor(mansion)
        self.belief = None
        self.intentions = ''

    def update(self):
        print(self.intentions)
        if self.intentions.__len__() > 0:
            self.act()
        else:
            self.think()

    def act(self):
        action = self.intentions[0]
        if action == 'u':
            self.actuator.up()
        if action == 'r':
            self.actuator.right()
        if action == 'd':
            self.actuator.down()
        if action == 'l':
            self.actuator.left()
        if action == 'p':
            self.actuator.pickup()
        if action == 's':
            self.actuator.suck()
        self.intentions = self.intentions[1:]

    def think(self):
        self.belief = self.sensor.get_mansion_state()
        rx = self.mansion.x_robot
        ry = self.mansion.y_robot
        dst_x, dst_y = self.find_closest(rx, ry)
        print('closest:', dst_x, '', dst_y)
        if dst_x < 0:
            return
        self.update_intentions(rx, ry, dst_x, dst_y)

    def find_closest(self, rx, ry):
        closest_dist = self.mansion.width * 4
        closest_x = -1
        closest_y = -1
        for x in range(self.mansion.width):
            for y in range(self.mansion.height):
                if self.belief[x][y].state > 0:
                    dist = abs(rx - x) + abs(ry - y)
                    if dist < closest_dist:
                        closest_x = x
                        closest_y = y
                        closest_dist = dist
        return closest_x, closest_y

    def update_intentions(self, src_x, src_y, dst_x, dst_y):
        while src_x != dst_x:
            if src_x < dst_x:
                src_x += 1
                self.intentions += 'r'
            if src_x > dst_x:
                src_x -= 1
                self.intentions += 'l'
        while src_y != dst_y:
            if src_y < dst_y:
                src_y += 1
                self.intentions += 'd'
            if src_y > dst_y:
                src_y -= 1
                self.intentions += 'u'
        if self.belief[dst_x][dst_y].has_jewel():
            self.intentions += 'p'
        if self.belief[dst_x][dst_y].has_dirt():
            self.intentions += 's'


class Actuator(object):
    def __init__(self, mansion):
        self.mansion = mansion

    def up(self):
        if self.mansion.y_robot > 0:
            self.mansion.y_robot -= 1

    def down(self):
        if self.mansion.y_robot < (self.mansion.width - 1):
            self.mansion.y_robot += 1

    def left(self):
        if self.mansion.x_robot > 0:
            self.mansion.x_robot -= 1

    def right(self):
        if self.mansion.x_robot < (self.mansion.height - 1):
            self.mansion.x_robot += 1

    def suck(self):
        self.mansion.suck_room()

    def pickup(self):
        self.mansion.pickup_room()


class Sensor(object):
    def __init__(self, mansion):
        self.mansion = mansion

    def get_mansion_state(self):
        return self.mansion.board
