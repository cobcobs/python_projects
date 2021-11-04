report = ""

def comma_and(list_arg):
    for i in range(len(list_arg)):
        if i != len(list_arg) - 1:
            report += list_arg[i] + ", "
        else:
            report += list_arg.prepend('and ')

test_1 = ['dog', 'cat', 'bird']
test_2 = []
test_3 = ['dog', 'cat']
comma_and(test_1)
print()
comma_and(test_2)
print()
comma_and(test_3)
