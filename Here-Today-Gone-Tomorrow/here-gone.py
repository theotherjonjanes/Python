import random
import os

rand = random.randrange(101)

if (rand < 50):
    f = open('here.txt', 'w+')
    print("Here!")
    f.close()
else:
    f = open('here.txt', 'w+')
    os.rename('here.txt', 'gone.txt')
    print("Gone!")
    os.remove('gone.txt')
