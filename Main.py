from Environment import Mansion
import time

mansion = Mansion(10, 10, True)
robot = mansion.insert_robot()
mansion.show()
print()

while True:
    mansion.update()
    robot.update()
    mansion.show()
    time.sleep(0.2)
    print()
