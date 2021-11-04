N = int(input("Number of Dimensions: "))
print()
remove_list = [',', '']
columns = []
rows = []
diagonal_row_1 = []
diagonal_row_2 = []
sequences = []
output_list = []

# rows
for n in range(1, N + 1):
    # check if the row is valid
    # if it is, then parse it and remove commas or spaces
    # finally, append the items into a new 'clear_row' list
    while True:
        row = input("Input row " + str(n) + " containing " + str(N) + " numbers separated by commas: ")
        clear_row = []
        for digit in row:
            if digit not in remove_list:
                clear_row.append(digit)
        if len(clear_row) < N or len(clear_row) > N:
            print("Invalid row. Please try again.")
            continue
        else:
            break
    rows.append(clear_row)

# columns
for y in range(0, N):
    column_list = []
    for x in range(0, N):
        column_list.append(rows[x][y])

    columns.append(column_list)


count_1 = 0
count_2 = 0

# diagonals
for row in rows:
    diagonal_row_1.append(row[count_1])
    diagonal_row_2.append(row[count_2 - 1])
    count_1 += 1
    count_2 -= 1

# combine the diagonals with the rows
rows.append(diagonal_row_1)
rows.append(diagonal_row_2)

# combine rows and columns into one list
sequences.extend(columns)
sequences.extend(rows)

# check if each list within this list is a palindrome
# then create a list of outputs
# in order to avoid a situation where the output becomes True even if it was alreaddy False
for sequence in sequences:
    reversed_sequence = list(reversed(sequence))
    if sequence == reversed_sequence:
        output_list.append(True)
    else:
        output_list.append(False)

# check for at least one False in the outputs
if False in output_list:
    output = False
else:
    output = True

print("\n" + str(output))
