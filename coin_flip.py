import random


runs = 10000
flips_per_run = 100
streak_length = 6

total_streaks = 0
for i in range(runs):
    # generate sample of flips
    flips = []
    for _ in range(flips_per_run):
        if random.randint(0, 1) == 1:
            flips.append('H')
        else:
            flips.append('T')

    # check for streaks of consecutive flips
    current_streak = 1
    previous_flip = None
    for flip in flips:
        if flip == previous_flip:
            current_streak += 1
            if current_streak == streak_length:
                total_streaks += 1
                break
        else:
            current_streak = 1
        previous_flip = flip

percentage_with_streaks = total_streaks / runs
print(
    f'Percentage of runs with a streak of {streak_length}: '
    f'{percentage_with_streaks*100:.2f}%'
)
