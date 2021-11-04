x = int(input("x = "))

factor_list = []
factor_subset_list = []

for i in range(1, x + 1):
    if x % i == 0:
        factor_list.append(i)

factor_list.pop()

print(factor_list)

# factor_subset_list = [factor_list[i - 1][j] for [[j for j in range(1, x + 1)] for i in range(1, x + 1) if j < factor_list[i - 1]]]

for j in range(1, x + 1):
    for k in range(1, x + 1):
        if k >= factor_list[j - 1]:
            factor_subset_list[j][k] = factor_subset_list[j - 1][k]
        if k < factor_list[j - 1]:
            factor_subset_list[j][k] = (factor_subset_list[j - 1][k] or factor_subset_list[j - 1][k - factor_list[j - 1]])

print(factor_subset_list)
