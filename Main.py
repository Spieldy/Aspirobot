from Environment import Mansion
import time

mansion = Mansion(5, 5, True)
robot = mansion.insert_robot()
mansion.show()
print()

while True:
    mansion.update()
    robot.update()
    mansion.show()
    time.sleep(0.5)
    print()
