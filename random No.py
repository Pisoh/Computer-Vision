#This programme generates 4 random numbers between 0 and 54 when called.

import random
import math

def generate():
    givenNumbers = {}
    index = 0

    for index in range(5):
        givenNumbers = random.randrange(0,55)
        index += 1
        if index > 4:
            pass
        else:
            return givenNumbers

def factorial(n):
    x = n * (n - 1)


def combination():
    return math.factorial(54) / (math.factorial(4) * (math.factorial(50)))


print(generate(), generate(), generate(), generate())
print(generate(), generate(), generate(), generate())
print(generate(), generate(), generate(), generate())
print(generate(), generate(), generate(), generate())

#print(combination())
