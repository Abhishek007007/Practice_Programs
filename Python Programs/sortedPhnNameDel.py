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

delName = input("enter the name customer that is to be deleted from the list :")
flag = 0
for key in sortedphnDict:
    if sortedphnDict[key] == delName:
        flag = 1
        sortedphnDict.pop(key)
        break
if flag == 1:
    print("Updated dictionary :")
    print(sortedphnDict)
else:
    print("No pair deleted")