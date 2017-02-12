from Environment import Mansion
import time

mansion = Mansion(5, 5)
mansion.show()
print()


def cls():
    clear = '\n' * 100
    print(clear)

while True:
    mansion.update()
    mansion.show()
    time.sleep(1.00)
    print()
