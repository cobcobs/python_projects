group = "ABCDEFGHIJ"

while True:
    infected = input("Input Infected: ").upper()
    if infected in group:
        break
    else:
        print("Invalid input, please try again")
        continue

infected_individuals = []

for index, individuals in enumerate(group):
    adjacent_individuals = group[index - 1: index + 2]
    if individuals == infected:
        for individual in adjacent_individuals:
            # print("Individual: " + individual)
            infected_individuals.append(individual)
            # print(infected_individuals)

print("People Infected After First Round: " + "".join(sorted(infected_individuals)))


while True:
    group_2 = input("Input Positions of Each Individual in Second Round: ").upper()
    if len(group_2) > len(group):
        print("Invalid input, please try again")
        continue
    sorted_group_2 = "".join(sorted(group_2))
    if sorted_group_2 != group:
        print("Invalid input, please try again")
        continue
    else:
        break

infected_individuals_2 = []

for index, individual in enumerate(group_2):
    adjacent_individuals = group_2[index - 1: index + 2]
    if individual in str(infected_individuals):
        # print("Adjacent Individuals: " + str(adjacent_individuals))
        for individual in adjacent_individuals:
            if individual not in infected_individuals:
                infected_individuals_2.append(individual)

infected_individuals += infected_individuals_2

print("People Infected After Second Round: " + "".join(sorted(infected_individuals)))


while True:
    group_3 = input("Input Positions of Each Individual in Third Round: ").upper()
    if len(group_3) > len(group):
        print("Invalid input, please try again")
        continue
    sorted_group_3 = "".join(sorted(group_3))
    if sorted_group_3 != group:
        print("Invalid input, please try again")
        continue
    else:
        break

infected_individuals_3 = []

for index, individual in enumerate(group_3):
    adjacent_individuals = group_3[index - 1: index + 2]
    if individual in str(infected_individuals):
        # print("Adjacent Individuals: " + str(adjacent_individuals))
        for individual in adjacent_individuals:
            if individual not in infected_individuals:
                infected_individuals_3.append(individual)

for individual in infected_individuals_3:
    if individual not in infected_individuals and individual not in infected_individuals_2:
        infected_individuals.append(individual)

print("People Infected After Third Round: " + "".join(sorted(infected_individuals)))
