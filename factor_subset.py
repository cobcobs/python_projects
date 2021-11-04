#number 1
number = int(input("Please input a number: "))
factor_list = []
subset_list = []
sum_list = []
is_perfect_square = False
output = []

#check if number is perfect square
for i in range(1, number + 1):
    if number % i == 0:
        factor_list.append(i) #adds the factor to a list

factor_list_length = len(factor_list)

# perfect squares have an ODD number of factors
if len(factor_list) % 2 != 0 and len(factor_list) > 1:
    is_perfect_square = True
    
# mathematically the number of subsets a set has is 2 ** n, where n is the number of elements
# & is a bitwise or binary operator that does some weird magic that I don't understand, but it works
# looks like it checks whether a number or 'bit' is in the set already
for j in range(2 ** factor_list_length):
    subset = [factor_list[k] for k in range(factor_list_length) if j & (2 ** k)]
    subset_list.append(subset)

# this avoids the '&' operator, but leaves out some sets
# for j in range(factor_list_length + 1):
#      for k in range(j + 1, factor_list_length + 1): 
#             subset = factor_list[j:k] 
#             subset_list.append(subset) 

# print("Subset List: " + str(subset_list))

for subset in subset_list:
    total = 0
    for element in subset:
        total += element
    sum_list.append(total)

# print("Sum List: " + str(sum_list))

# uses enumerate
for index, element_sum in enumerate(sum_list):
    if element_sum == number:
        if number not in subset_list[index]:
            output.append(subset_list[index])

print()
if is_perfect_square and output:
    print(is_perfect_square)
    for item in output:
        print(item)
else:
    print(False)

