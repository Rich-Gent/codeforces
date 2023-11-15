loopNum = input()
for x in range(int(loopNum)):
    word = input()
    if len(word) >10 :
        wordLen = len(word) - 2
        newWord = word[0] + str(wordLen) + word[len(word)-1]
        print(newWord)
    else:
        print(str(word))