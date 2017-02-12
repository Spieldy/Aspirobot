from random import randint


class Mansion(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[Room() for x in range(self.width)] for y in range(self.height)]

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

    def suck_room(self, x, y):
        self.board[x][y] = 0

    def pickup_room(self, x, y):
        self.board[x][y] = 0

    def show(self):
        for x in range(self.width):
            for y in range(self.height):
                print(self.board[x][y].state, end=' ')
            print()


class Room(object):
    def __init__(self):
        self.state = 0

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
