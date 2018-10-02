fin = open('words.txt')
line = fin.readline()
word = line.strip()

def threeConsecutiveDoubleLetters():
    for line in fin:
        word = line.strip()
        for x in range(len(word)-5):
            if word[x] == word[x+1]:
                if word[x+2] == word[x+3]:
                    if word[x+4] == word[x+5]:
                        print(word)

threeConsecutiveDoubleLetters()
