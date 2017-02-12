from Environment import Mansion
import time
import os

mansion = Mansion(5, 5, True)
robot = mansion.insert_robot()
mansion.show()
print()


while True:
    mansion.update()
    robot.update()
    os.system('cls' if os.name == 'nt' else 'clear')
    mansion.show()
    time.sleep(1.00)
    print()
