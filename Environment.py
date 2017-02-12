from random import randint
from Agent import Robot


class Mansion(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[Room(x, y) for x in range(self.width)] for y in range(self.height)]
        self.x_robot = None
        self.y_robot = None

    def update(self):
        event_occurred = randint(0, 99)
        if event_occurred < 29:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            print('+dirt (', x, ',', y, ')')
            self.board[x][y].insert_dirt()
        event_occurred = randint(0, 99)
        if event_occurred < 29:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            print('+jewel (', x, ',', y, ')')
            self.board[x][y].insert_jewel()

    def insert_robot(self):
        robot = Robot(self)
        x = self.height // 2
        y = self.width // 2
        self.x_robot = x
        self.y_robot = y
        self.board[x][y].set_robot_on()
        return robot

    def suck_room(self, x, y):
        self.board[x][y] = 0

    def pickup_room(self, x, y):
        self.board[x][y] = 0

    def show(self):
        print('+', end='')
        for i in range(self.width):
            print(' -', end='')
        print(' +')
        for x in range(self.width):
            print('|', end=' ')
            for y in range(self.height):
                if (y == self.y_robot) & (x == self.x_robot):
                    print("@", end=' ')
                else:
                    print('~' if self.board[x][y].state == 1
                          else 'o' if self.board[x][y].state == 2
                          else 'õ' if self.board[x][y].state == 3
                          else ' ', end=' ')
            print('|')
        print('+', end='')
        for i in range(self.width):
            print(' -', end='')
        print(' +')


class Room(object):
    def __init__(self, x, y):
        self.state = 0
        self.robot = False
        self.x = x
        self.y = y

    def insert_dirt(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 2:
            self.state = 3
        else:
            pass

    def insert_jewel(self):
        if self.state == 0:
            self.state = 2
        elif self.state == 1:
            self.state = 3
        else:
            pass

    def has_dirt(self):
        if self.state == 1 or self.state == 3:
            return True
        else:
            return False

    def has_jewel(self):
        if self.state == 2 or self.state == 3:
            return True
        else:
            return False

    def set_robot_on(self):  # TODO Et si le robot etait juste modélisé par un x et un y dans le mansion, et pas stocké en boolean dans chaque room ?
        self.robot = True

    def set_robot_off(self):
        self.robot = False

    def is_robot_on(self):
        return self.robot
