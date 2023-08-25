str1 = input("enter the string :")
str2 = str1.split()
strDict = {}

for word in str2:
    if word in strDict:
        strDict[word] += 1
    else:
        strDict[word] = 1
print("Count of words :")
print(strDict)