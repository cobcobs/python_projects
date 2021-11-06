def next_smaller(n):
    array = list(str(n))
    if len(array) == 1:
        return -1
    i = max((i for i in range(1, len(array)) if array[i - 1] > array[i]), default=-1)
    j = max((j for j in range(i, len(array)) if array[j] < array[i - 1]), default=-1)
    if i == -1 or j == -1:
        return -1
    array[j], array[i - 1] = array[i - 1], array[j]
    array[i:] = reversed(array[i:])
    output = int(''.join(array))
    return output if len(str(n)) == len(str(output)) else -1


print(next_smaller(10))
