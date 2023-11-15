tempList = input()
tempList = tempList.split()
topTempList = tempList[1]
finalScore = 0
tempScore = input()
tempScore = tempScore.split()
topScore = tempScore[int(topTempList)-1]
for x in range(int(tempList[0])):
    if int(tempScore[x]) <= 0:
        pass
    else:
        if int(tempScore[x]) >= int(topScore):
            finalScore+=1
print(finalScore)


   
        