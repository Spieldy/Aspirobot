from random import randint
import os

# Global variables defining performance increase or decrease
GOOD_SUCK = 8
GOOD_PICKUP = 8
BAD_SUCK = 100
# Global variables defining generation probabilities
DIRT_PROBABILITY = 50
JEWEL_PROBABILITY = 10


class Mansion(object):

    def __init__(self, dim):
        self.status_message = ''  # Used to display information
        self.width = dim  # Mansion dimensions
        self.height = dim
        self.board = [[Room(x, y) for x in range(self.width)] for y in range(self.height)]  # The 2D array of rooms
        self.x_robot = self.width // 2  # Robot position
        self.y_robot = self.height // 2
        self.score = 50  # Performance score

    # Called once per frame, decides whether dust or jewels should appear
    def update(self):
        self.status_message += 'Performance score: %i\n' % self.score
        # Generate dust
        event_occurred = randint(0, 99)
        if event_occurred < DIRT_PROBABILITY:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            self.board[x][y].insert_dirt()
        # Generate jewel
        event_occurred = randint(0, 99)
        if event_occurred < JEWEL_PROBABILITY:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            self.board[x][y].insert_jewel()

    # Suck the content of the room where the robot is
    def suck_room(self):
        room = self.board[self.x_robot][self.y_robot]
        if room.has_jewel() and room.has_dirt():
            self.status_message += "Oops, jewel sucked!\n"
            self.score -= BAD_SUCK
        if room.has_dirt() and not room.has_jewel():
            self.status_message += "Dust sucked.\n"
            self.score += GOOD_SUCK
        else:
            if not room.has_jewel() and not room.has_dirt():
                self.status_message += "Nothing to suck!\n"
        self.board[self.x_robot][self.y_robot].state = 0

    # Pick up the content of the room where the robot is
    def pickup_room(self):
        room = self.board[self.x_robot][self.y_robot]
        if (room.state == 1) or (room.state == 0):
            self.status_message += "Nothing to pick up!.\n"
        if room.state == 2:
            room.state = 0
            self.status_message += "Jewel picked up.\n"
            self.score += GOOD_PICKUP
        if room.state == 3:
            room.state = 1
            self.status_message += "Jewel picked up.\n"
            self.score += GOOD_PICKUP

    # Display the mansion state
    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('+', end='')
        for i in range(self.width):
            print(' -', end='')
        print(' +')
        for y in range(self.height):
            print('|', end=' ')
            for x in range(self.width):
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
