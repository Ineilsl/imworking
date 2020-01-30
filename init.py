import random
import time
lastValue = ""
cnt = 0

f = open("log.db", "r")
lines = f.readlines()

nLines = sum(1 for line in open('log.db'))

while True:
    rand = random.randrange(nLines)
    value = lines[rand][:-1]
    if value != lastValue:
        if rand%2 == 0:
            print(value[:-1])
            time.sleep(0.2)
    lastValue = value
