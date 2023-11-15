#num of piles
piles = input()
#number of worms in each pile
numWorms = input()
numWorms = numWorms.split();
numWorms = list(map(int,numWorms));
#num of juicy worms
juicyW = input();
#worm labels
labelW = input();
labelW = labelW.split();
labelW = list(map(int,labelW));
#loop for number of juicy worms
for i in range(int(juicyW)):
    for j in range(int(piles)):
        labelW[i] = labelW[i]-numWorms[j];
        if(labelW[i]<1):
            print(j+1);
            break;