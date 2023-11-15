import math
bSize = input() 
bSize = bSize.split()
bSize = int(bSize[0])*int(bSize[1])
totalDom = math.floor(bSize / 2)
print(totalDom)