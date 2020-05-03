
messages=[]
f = open('beemoviescript.txt', 'r')
for x in f:
    word = x.split()
    for msg in word:
        messages.append(msg)
