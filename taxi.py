import math
numGroup = input()
gList = [int(x) for x in input().split()]
ones = 0
twos = 0
threes = 0
fours = 0

ones = gList.count(1)
twos = gList.count(2)
threes = gList.count(3)
fours = gList.count(4)
total = 0


total += fours

if (ones-threes) <= 0:
    ones = 0
else:
    ones -= threes
total += threes

total +=   twos // 2
twos = twos%2

total += (ones//4)
ones = ones%4
if ones>2 and twos>0:
    total += 2
elif twos>0 or ones>0:
    total+=1

print(total)







