stuDict = {}
for i in range(5):
    name = input("Enter name of"+str(i+1)+"the student :")
    roll = int(input("Enter the roll no :"))
    stuDict[roll] = name
sortedStuDict = {}

temp = list(stuDict.values())
temp.sort()
for value in temp:
    for key in stuDict:
        if stuDict[key] == value:
            sortedStuDict[key] = value
print("sorted dictionary")
print(sortedStuDict)
