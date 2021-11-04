def collatz(number):
    # recursive form
    print(number)
    if number == 1:
        return
    elif number % 2 == 0:
        number //= 2
        collatz(number)
    else:
        number = 3 * number + 1
        collatz(number)

    # loop form
    # while number != 1:
    #     print(number)
    #     if number % 2 == 0:
    #         number //= 2
    #     elif number % 2 != 0:
    #         number = 3 * number + 1
    # if number == 1:
    #     print(number)


i = int(input("Please input a positive integer:\n"))
print()
collatz(i)
