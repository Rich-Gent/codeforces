x = 0
numLoops = input()
for y in range(int(numLoops)):
    ops = input()
    if(ops[1] == "+"):
        x +=1;
    else:
        x -=1;
print(x)