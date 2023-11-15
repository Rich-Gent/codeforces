loopNum = input()
finalScore = 0
for x in range(int(loopNum)):
    currentScore = 0
    probInp = input()
    probList = probInp.split()
    for y in range(len(probList)):
        if probList[y]=="1":
            currentScore += 1
    if currentScore>1:
        finalScore+=1
print(finalScore)