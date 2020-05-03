import math
from urllib.request import urlopen

x = 10.7
print(math.ceil(x))

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