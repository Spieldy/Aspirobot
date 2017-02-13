from Environment import Mansion
from Agent import Robot
import time

# Initialize
mansion = Mansion(5)
robot = Robot(mansion)
mansion.show()
print()

# Basic game loop
while True:
    mansion.update()
    robot.update()
    mansion.show()
    time.sleep(0.5)
    print()
