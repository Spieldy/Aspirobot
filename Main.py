from Environment import Mansion
from random import randint
import time


mansion = Mansion(5, 5)
mansion.show()
print()

def should_dirt():
    random = randint(0, 99)
    if (random < 29):
        mansion.insert_dirt()

def should_jewel():
    random = randint(0, 99)
    if (random < 29):
        mansion.insert_jewel()



while True:
    should_dirt()
    should_jewel()
    mansion.show()
    time.sleep(1.25)
    print()


