from random import randint
from Agent import Robot
import os


class Mansion(object):
    def __init__(self, width, height, debug):
        self.av_action = None
        self.av_pickup = None
        self.av_suck = None
        self.nb_action = 0
        self.nb_pickup = 0
        self.nb_suck = 0
        self.debug = debug
        self.width = width
        self.height = height
        self.board = [[Room(x, y) for x in range(self.width)] for y in range(self.height)]
        self.x_robot = None
        self.y_robot = None

    def update(self):
        event_occurred = randint(0, 99)
        if event_occurred < 10:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            if self.debug:
                print('+dirt (', x, ',', y, ')')
            self.board[x][y].insert_dirt()
        event_occurred = randint(0, 99)
        if event_occurred < 10:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            if self.debug:
                print('+jewel (', x, ',', y, ')')
            self.board[x][y].insert_jewel()

    def insert_robot(self):
        robot = Robot(self)
        x = self.height // 2
        y = self.width // 2
        self.x_robot = x
        self.y_robot = y
        return robot

    def suck_room(self):
        if self.board[self.x_robot][self.y_robot].has_jewel():
            if self.debug:
                print("OUPS, jewel lost")
        self.board[self.x_robot][self.y_robot].state = 0
        self.nb_suck += 1
        self.nb_action += 1

    def pickup_room(self):
        if self.board[self.x_robot][self.y_robot].state == 2:
            self.board[self.x_robot][self.y_robot].state = 0
            self.nb_pickup += 1
            self.nb_action += 1
        if self.board[self.x_robot][self.y_robot].state == 3:
            self.board[self.x_robot][self.y_robot].state = 1
            self.nb_pickup += 1
            self.nb_action += 1
        if self.board[self.x_robot][self.y_robot].state == 1:
            if self.debug:
                print("Dirt not to pick up !!")

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if False:
            print("Number")
            print("  actions:  " + str(self.nb_action))
            print("  pickups:  " + str(self.nb_pickup))
            print("  sucks:    " + str(self.nb_suck))
            if self.nb_suck > 0:
                print("Ratio")
                print("  pickups/sucks:  " + str(self.nb_pickup / self.nb_suck))
            print("Average")
            print("  move before action:  " + str(self.av_action))
            print("  move before pickup:  " + str(self.av_suck))
            print("  move before suck:    " + str(self.av_pickup))
            print()
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
