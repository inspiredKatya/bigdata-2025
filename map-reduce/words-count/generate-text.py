import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

fileLength = 50000
i=0
stringForFile = ""
while i<fileLength:
    wordLen = 5
    stringForFile += (randomword(wordLen) +" ")
    i+= wordLen
    if i % 100 < 5:
        stringForFile += "\n"

with open("input-random.txt", "w") as f:
    f.write(stringForFile)