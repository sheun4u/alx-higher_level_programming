#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, "is Positive")
elif number < 0:
    print(number , "is Negative")
else:
    print(number, "is Zero", end="")
