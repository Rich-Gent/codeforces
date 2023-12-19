word = input().lower()
sortWord=""
word = word.replace('a',"")
word = word.replace('i',"")
word = word.replace('e',"")
word = word.replace('o',"")
word = word.replace('u',"")
word = word.replace('y',"")
for i in range(0,len(word)):
    sortWord += "."+ word[i]
print(sortWord)
