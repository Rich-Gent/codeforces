import math

#num of piles
piles = input()
#number of worms in each pile
numWorms = input()
numWorms = numWorms.split();
numWorms = list(map(int,numWorms));
newNumWorms = [0] * int(piles);
#num of juicy worms
juicyW = input();
#worm labels
labelW = input();
labelW = labelW.split();
labelW = list(map(int,labelW));
def binarySearch(label):
    left = 0;
    right = int(piles) - 1;
    while left <= right:
        middle = math.floor((left+right)/2);
        if newNumWorms[middle] < label:
            left = middle+1;
        elif newNumWorms[middle] > label:
            right = middle-1;
        else:
            return middle + 1;
    return left + 1;

for i in range(int(piles)):
    if(i==0):
        newNumWorms[i] = numWorms[i]
    else:
        newNumWorms[i] = numWorms[i]+newNumWorms[i-1];

for j in range(int(juicyW)):
    print(binarySearch(labelW[j]));



