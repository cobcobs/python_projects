from itertools import permutations


def get_pins(observed):
    expectations = []
    input_digits = [i for i in str(observed)]
    digits = [str(abs(int(observed) - 3)), str(abs(int(observed) - 1)), observed, str(int(observed) + 1), str(int(observed) + 3)]
    digits = list(dict.fromkeys(digits))
    print("Digits: {}".format(digits))
    for index, i in enumerate(digits):
        print(index)
        print(i)
        if int(i) < 1 or int(i) > 10:
            digits.pop(index)
        if int(i) == 10:
            digits[index] = '0'
    # expectations += "".join(permutations(digits, len(observed)))

get_pins('1')
