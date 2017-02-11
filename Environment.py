from random import randint


class Mansion(object):
    def __init__(self, wide, height):
        self.w = wide
        self.h = height
        self.board = [[Room() for x in range(self.w)] for y in range(self.h)]

    def insert_dirt(self):
        random = randint(0, self.w * self.h)
        i = 0
        for x in range(self.w):
            for y in range(self.h):
                if i == random:
                    self.board[x][y].insert_dirt()
                i += 1
        print("Wild DIRT appeared!")

    def insert_jewel(self):
        random = randint(0, self.w * self.h)
        i = 0
        for x in range(self.w):
            for y in range(self.h):
                if i == random:
                    self.board[x][y].insert_jewel()
                i += 1
        print("JEWEL drop on the floor")

    def should_dirt(self):
        random = randint(0, 99)
        if random < 29:
            self.insert_dirt()

    def should_jewel(self):
        random = randint(0, 99)
        if random < 29:
            self.insert_jewel()

    def update(self):
        self.should_dirt()
        self.should_jewel()

    def show(self):
        for x in range(self.w):
            for y in range(self.h):
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
