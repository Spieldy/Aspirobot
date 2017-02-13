from random import randint
from Agent import Robot
import os


class Mansion(object):

    def __init__(self, width, height, debug):
        self.debug = debug
        self.status_message = ''
        self.width = width
        self.height = height
        self.board = [[Room(x, y) for x in range(self.width)] for y in range(self.height)]
        self.x_robot = None
        self.y_robot = None
        self.score = None
        self.G_SUCK = 10
        self.G_PICKUP = 10
        self.B_SUCK = 30

    def update(self):
        self.status_message += 'Performance score: %i\n' %self.score
        event_occurred = randint(0, 99)
        if event_occurred < 10:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            self.board[x][y].insert_dirt()
        event_occurred = randint(0, 99)
        if event_occurred < 10:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            self.board[x][y].insert_jewel()

    def insert_robot(self):
        robot = Robot(self)
        x = self.height // 2
        y = self.width // 2
        self.x_robot = x
        self.y_robot = y
        self.score = 100
        return robot

    def suck_room(self):
        room = self.board[self.x_robot][self.y_robot]
        if room.has_jewel() and room.has_dirt():
            self.status_message += "Oops, jewel sucked!\n"
            self.score -= self.B_SUCK
        if room.has_dirt() and not room.has_jewel():
            self.status_message += "Dust removed.\n"
            self.score += self.G_SUCK
        else:
            if not room.has_jewel() and not room.has_dirt():
                self.status_message += "Nothing to suck!\n"

        self.board[self.x_robot][self.y_robot].state = 0

    def pickup_room(self):
        room = self.board[self.x_robot][self.y_robot]
        if (room.state == 1) or (room.state == 0):
            self.status_message += "Nothing to pick up!.\n"
        if room.state == 2:
            room.state = 0
            self.status_message += "Jewel picked up.\n"
            self.score += self.G_PICKUP
        if room.state == 3:
            room.state = 1
            self.status_message += "Jewel picked up.\n"
            self.score += self.G_PICKUP

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
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
        print(self.status_message)
        self.status_message = ''


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
