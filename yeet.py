def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    i = abs(int(input("Please input a positive integer:\n")))
    while i != 1:
        i = collatz(i)
        print(i)
except ValueError:
    print("Please input a valid number")
    i = abs(int(input("Please input a positive integer:\n")))
    while i != 1:
        i = collatz(i)
        print(i)
