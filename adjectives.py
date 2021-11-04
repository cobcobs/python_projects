paragraph = input().lower()
paragraph_list = paragraph.split()
punctuation_marks = ['!', '.', ',', ';', ':']
output = dict()

for word in paragraph_list:
    if word[-1:] in punctuation_marks:
        word = word[0:-1]
    if word[-2:] == 'er':
        root_word = word[0: -2]
        output[root_word] = output.get(root_word, 0) + 1
    elif word[-3:] == 'est':
        root_word = word[0: -3]
        output[root_word] = output.get(root_word, 0) + 1

print(output)
