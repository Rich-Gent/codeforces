numLines = input();
numLines = int(numLines);
binaryLine = input();
binaryLine = binaryLine.split();
#find lower limit
def stripLower():
    for i in range(len(binaryLine)):
        if binaryLine[0] == "0":
            return i;
        else:
            binaryLine.pop(0);

#find upper limit
def stripHigher():
    for i in range((len(binaryLine)-1), 0, -1):
        if binaryLine[i] == "0":
            break;
        else:
            binaryLine.pop(i);

#remove upper and lower 1s
numLines -= stripLower()
numLines -= stripHigher()



print(binaryLine);

