loops = int(input())
for z in range(loops):
    tps = 0
    y=0
    rPoint = 0
    smallList = []
    smallNum = 0
    ribLen = int(input())
    numList = [int(x) for x in input().split()]
    while(y<ribLen):
        if(y==ribLen-1):
            tps+=numList[y]
            break
        if(numList[y]>0):
            for x in range(ribLen):
                if(numList[x]>0 and x==ribLen-1):
                    rPoint=x+1
                    break
                if(numList[y+x]<= 0):
                    rPoint = x+1
                    break
            for i in range(rPoint):
                if(numList[y+i]>0):
                    smallList.append(numList[y+i])
                else:
                    break
            smallNum = min(smallList)
            tps+=smallNum
            smallList.clear()
            for i in range(rPoint):
                if(numList[y+i]>0):
                    numList[y+i]-=smallNum
                else:
                    break
        else:
            y+=1
    print(tps-1)

        