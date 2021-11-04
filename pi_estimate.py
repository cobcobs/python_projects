import random


def estimate_pi(n):
    circle = 0
    square = 0
    for _ in range(n):
        x = random.randint(0, 1)
        y = random.randint(0, 1)
        distance = (x ** 2 + y ** 2) ** 0.5
        if distance <= 1:
            circle += 1
        square += 1
    result = 4 * circle / square
    return result
    print(result)

estimate_pi(100)
estimate_pi(1000)
estimate_pi(10000)
estimate_pi(100000)
