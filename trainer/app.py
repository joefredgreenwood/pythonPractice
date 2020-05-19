import math
import random
from urllib.request import urlopen

x = 10.7
print(math.ceil(x))

y = math.ceil(9.8)
print(y)

print(random.randint(0,100))

g = [1,2,3,4,3,4]
h=sum(g, 0)
print(h)
print(g.count(0))

def findwords():
    story= urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
#         story_words.append(line_words)
        for word in line_words:
            story_words.append(word)

    story.close()
    print(story_words)
    


findwords()