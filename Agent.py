class Robot(object):
    def __init__(self, mansion):
        self.mansion = mansion
        # The max amount of action before exploring again. Directly correlates to performance score.
        self.max_steps = 10
        # Actuator and Sensor
        self.actuator = Actuator(mansion)
        self.sensor = Sensor(mansion)
        # BDI model
        self.belief = None  # 2D Room array
        self.desire = None  # 2D boolean array. True means the room needs to be reached and interacted with.
        self.intentions = ''  # Each letter corresponds to an action, essentially an action queue

    # Called once per frame. The robot either moves, sucks, picks up, or explores.
    def update(self):
        if self.intentions.__len__() > 0:  # If the robot has things to do
            self.mansion.status_message += "Executing path of length %i: " % self.max_steps \
                                           + self.intentions[0].capitalize() + self.intentions[1:]\
                                           + " (%i left)\n" % self.intentions.__len__()
            self.act()
        else:
            self.mansion.status_message += "Planning path...\n"
            self.think()

    # Reads the intentions string and act accordingly
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

    # Exploration function
    def think(self):
        # Initialize
        self.belief = self.sensor.get_mansion_state()
        self.max_steps = self.sensor.get_performance_score() // 10
        self.desire = [[False for x in range(self.mansion.width)] for y in range(self.mansion.height)]
        if self.max_steps < 1:
            self.max_steps = 1
        src_x = self.mansion.x_robot
        src_y = self.mansion.y_robot

        # Keep exploring until action queue is full, or nothing is worth exploring anymore.
        while self.intentions.__len__() < self.max_steps:
            dst_x, dst_y = self.find_closest(src_x, src_y)  # Find closest element of interest
            if dst_x < 0:  # No element found
                break
            self.desire[dst_x][dst_y] = True  # Marks the element as a goal
            self.update_intentions(src_x, src_y, dst_x, dst_y)  # Update action queue
            src_x = dst_x
            src_y = dst_y

    # Find the closest element of interest from specified position. Returns -1, -1 if none was found
    def find_closest(self, rx, ry):
        closest_dist = self.mansion.width * 4
        closest_x = -1
        closest_y = -1
        for x in range(self.mansion.width):
            for y in range(self.mansion.height):
                # If the room has something in it and it is not already a goal
                if (self.belief[x][y].state > 0) & (not self.desire[x][y]):
                    dist = abs(rx - x) + abs(ry - y)
                    if dist < closest_dist: # If it's closer than the previous one
                        closest_x = x
                        closest_y = y
                        closest_dist = dist
        return closest_x, closest_y

    # Simple pathfinding algorithm between two positions
    def update_intentions(self, src_x, src_y, dst_x, dst_y):
        while (src_x != dst_x) & (self.intentions.__len__() < self.max_steps):
            if src_x < dst_x:
                src_x += 1
                self.intentions += 'r'
            if src_x > dst_x:
                src_x -= 1
                self.intentions += 'l'
        while (src_y != dst_y) & (self.intentions.__len__() < self.max_steps):
            if src_y < dst_y:
                src_y += 1
                self.intentions += 'd'
            if src_y > dst_y:
                src_y -= 1
                self.intentions += 'u'
        if (self.belief[dst_x][dst_y].has_jewel()) & (self.intentions.__len__() < self.max_steps):
            self.intentions += 'p'
        if (self.belief[dst_x][dst_y].has_dirt()) & (self.intentions.__len__() < self.max_steps):
            self.intentions += 's'


class Actuator(object):
    def __init__(self, mansion):
        self.mansion = mansion
        self.energy_cost = 2

    def up(self):
        if self.mansion.y_robot > 0:
            self.mansion.y_robot -= 1
            self.mansion.score -= self.energy_cost

    def down(self):
        if self.mansion.y_robot < (self.mansion.width - 1):
            self.mansion.y_robot += 1
            self.mansion.score -= self.energy_cost

    def left(self):
        if self.mansion.x_robot > 0:
            self.mansion.x_robot -= 1
            self.mansion.score -= self.energy_cost

    def right(self):
        if self.mansion.x_robot < (self.mansion.height - 1):
            self.mansion.x_robot += 1
            self.mansion.score -= self.energy_cost

    def suck(self):
        self.mansion.suck_room()
        self.mansion.score -= self.energy_cost

    def pickup(self):
        self.mansion.pickup_room()
        self.mansion.score -= self.energy_cost


class Sensor(object):
    def __init__(self, mansion):
        self.mansion = mansion

    def get_mansion_state(self):
        return self.mansion.board

    def get_performance_score(self):
        return self.mansion.score
