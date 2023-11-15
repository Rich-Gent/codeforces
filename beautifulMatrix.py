moveCount = 0
line1 = input()
line2 = input()
line3 = input()
line4 = input()
line5 = input()
line1 = line1.split()
line2 = line2.split()
line3 = line3.split()
line4 = line4.split()
line5 = line5.split()
if "1" in line1:
    moveCount += 2;
    index = line1.index("1");
if "1" in line2:
    moveCount += 1;
    index = line2.index("1");
if "1" in line3:
    index = line3.index("1");
if "1" in line4:
    moveCount += 1;
    index = line4.index("1");
if "1" in line5:
    moveCount += 2;
    index = line5.index("1");
moveCount += abs(index - 2);
print(moveCount);