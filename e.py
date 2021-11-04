def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def estimate_e(n):
    e = (1 + 1/n) ** n
    return e
