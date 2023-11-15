firString = input();
secString = input();
firString = firString.lower()
secString = secString.lower()
letCount = 0;
for i in range(len(firString)):
    if firString[i]>secString[i]:
        letCount +=1;
        break;
    if firString[i]<secString[i]:
        letCount -=1;
        break;
print(letCount);