phnDict = {}
numC = int(input(("Enter the number of customers :")))
for i in range(numC):
    name = input("Enter name of "+str(i+1)+"th customer :")
    phn = int(input("Enter the phone no :"))
    phnDict[phn] = name
sortedphnDict = {}

temp = list(phnDict.values())
temp.sort()
for value in temp:
    for key in phnDict:
        if phnDict[key] == value:
            sortedphnDict[key] = value
print("sorted dictionary")
print(sortedphnDict)