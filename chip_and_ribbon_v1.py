loops = int(input())
for z in range(loops):
    tps = 0
    y=0
    ribLen = int(input())
    numList = [int(x) for x in input().split()]
    numList[0] -= 1
    while(y<ribLen):
        try:
            if(numList[y+1]>0):
                numList[y+1] -=1
                y+=1
                continue
            else:
                for x in range(ribLen):
                    if(numList[x]>0):
                        tps+=1
                        numList[x] -=1
                        y=x
                        break
                    if(x == (ribLen-1)):
                        y=ribLen
        except:
            for i in range(ribLen):
                if(numList[i]>0):
                    y=i-1
                    tps+=1
                    break
                if(i == (ribLen-1)):
                    y = ribLen


    print(tps)

        