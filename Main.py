from Environment import Mansion
import time

mansion = Mansion(5, 5)
mansion.show()
print()


def cls():
    clear = '\n' * 100
    print(clear)

while True:
    cls()
    mansion.update()
    mansion.show()
    time.sleep(1.25)
    print()


