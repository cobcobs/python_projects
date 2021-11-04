import random
import test


def pi_estimate(n):
    circle_point = 0
    square_point = 0
    for _ in range(n):
        x = random.randint(0, 1)
        y = random.randint(0, 1)
        distance = x ** 2 + y ** 2
        if distance ** 0.5 <= 1:
            circle_point += 1
        square_point += 1

    return 4 * circle_point / square_point

