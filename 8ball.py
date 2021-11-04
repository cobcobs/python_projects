import random


def Outlook():
    input('What is your question?\n')
    randomNumber = random.randint(1, 4)
    if randomNumber == 1:
        return 'Most likely.'
    elif randomNumber == 2:
        return 'Outlook not so good.'
    elif randomNumber == 3:
        return 'Reply hazy. Try again.'
    elif randomNumber == 4:
        return 'ur gey'


print(Outlook())
