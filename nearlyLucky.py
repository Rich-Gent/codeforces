num = [int(x) for x in input()]
count = 0
count += num.count(4)
count += num.count(7)

if(count == 4 or count==7):
    print("YES")
else:
    print("NO")