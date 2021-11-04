table_arrangement_binary = input("Table Arrangement: ")
# k = int(input("Social Distancing Policy: "))
binary_list = [int(i) for i in table_arrangement_binary]
occupied_table_indeces = []
distance_list = []

# print(binary_list)

while True:
    k = int(input("Social Distancing Policy: "))
    if k < 0:
        continue
    elif len(str(table_arrangement_binary)) <= k:
        continue
    else:
        break

index = -1
for digit in binary_list:
    index += 1
    if digit == 1:
        occupied_table_indeces.append(index)

index = -1
for i in occupied_table_indeces:
    if index < len(occupied_table_indeces) - 2:
        index += 1
        distance = abs(occupied_table_indeces[index] - occupied_table_indeces[index + 1])
        print(distance)
        distance_list.append(distance)
    # else:
    #     index += 1
    #     distance = abs(occupied_table_indeces[index] - occupied_table_indeces[0])
    #     print(distance)
    #     distance_list.append(distance)

for distance in distance_list:
    if distance >= k:
        output = True
    else:
        output = False

print(output)
