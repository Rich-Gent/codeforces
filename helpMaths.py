mathStr = input();
mathStr = mathStr.split("+");
mathStr.sort();
sortStr = "";
sortStr = "+".join(mathStr);
print(sortStr);