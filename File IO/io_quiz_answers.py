# Comuter Programming 1
# File IO Quiz
#
# Names: Ethan McCauley

# Answers to 1 - 11
'''

1)D                 2)A                 3)B, C, D

4)A                 5)B                 6)B, C

7)B                 8)C                 9)B

10)C                11)A

'''


#12
file = open('scrabble_list.txt', 'r')
words = file.readlines()

#13
file2 = open('scrabble_list.txt', 'r')
scrabble = file2.readlines()
print(len(scrabble))
print()
file2.close()


#14
with open('scrabble_list.txt') as f:
    words = f.read().splitlines()
    
print(words[:10])


#15
count = 0
for w in words:
    if w[:-1] == 'e':
        count += 1
print(count)    

#16
with open("same_endings.txt", "w") as f:
    for wo in words:
        if wo[-1] == wo[0]:
            f.write(wo + '\n')
