import random


number_of_flips = 100
runs = 10000
streak = 1
total_streaks = 0

for run in range(runs):
    flips = []
    for i in range(number_of_flips):
        if random.randint(0,1) == 1:
            flips.append('H')
        else:
            flips.append('T')

    # check for streaks
    streak = 1
    previous_flip = None

    for flip in flips:
        if flip == previous_flip:
            streak += 1
            if streak == 6:
                total_streaks += 1
                break
        else:
            streak = 1
        previous_flip = flip

print(f'Chance of streak: {total_streaks / 100}%')
