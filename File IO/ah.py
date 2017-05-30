
with open('scrabble_list2.txt') as f:
    words = f.read().splitlines()
    if len(words[1:6]):
        print (len(words))
        
with open('scrabble_list2.txt') as f:
    words = f.read()
    count = 0
    for w in words:
        if w[:3] == 'r':
            count += 1
    print(count)         
file = open('scrabble_list2.txt', 'r')
contents = file.read()
print (len(contents))



