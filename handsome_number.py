# maximum handsome and prime number from 1 to n

# find prime numbers
num = input("Please input a number: ")
n = int(num)
prime_count = 0
prime_list = []

for i in range (1,n+1):
    divisor = 1
    factor_counter = 0
    for j in range(divisor, i+1):
        if i % j == 0:
            factor_counter += 1
    if factor_counter == 2:
        prime_list.append(i)
        prime_count += 1
        
# print("Prime count = {}".format(prime_count))
# print("Prime list = {}".format(prime_list))

# check if the prime is a handsome number
total = 0

prime_and_handsome_list = []

for number in prime_list:
    x = number
    # print("Number: {}".format(number))
    count = 0
    while int(x) != 1 and count < 6:
        for digit in str(x): # loop through
            total += int(digit) ** 2
        # print("Total: {}".format(total))
        x = total
        total = 0
        count += 1
    if int(x) == 1:
        prime_and_handsome_list.append(number)

# print("Prime and Handsome List = {}".format(prime_and_handsome_list))

# get product of numbers digits
product_list = []

for number in prime_and_handsome_list:
    # print("Number: {}".format(number))
    product = 1
    for digit in str(number):
        # print("Digit: {}".format(digit))
        product *= int(digit)
        # print("Product: {}".format(product))
    product_list.append(product)

# print("Product List: {}".format(product_list))

# get maximum
maximum = 0
for y in product_list:
    if int(y) > maximum:
        maximum = y
# print("Maximum: {}".format(maximum))

# pull its index from list
list_index = [] # just in case there are two or more maximums
for i in range(len(product_list)):
    # print("Index: {}".format(i))
    if product_list[i] == maximum:
        list_index.append(i)
# print("List Indices: {}".format(list_index))

# find the original numbers using it's index or indices
final_list = []
for i in list_index:
    final_list.append(prime_and_handsome_list[i])
# print("Final List: {}".format(final_list))

print(str(final_list)[1:-1])

