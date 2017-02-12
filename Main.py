from Environment import Mansion
import time

mansion = Mansion(5, 5, True)
robot = mansion.insert_robot()
mansion.show()
print()


def cls():
    clear = '\n' * 100
    print(clear)

while True:
    mansion.update()
    robot.update()
    mansion.show()
    time.sleep(1.00)
    print()
