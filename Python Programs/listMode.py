num = int(input("Enter the number of elements in the list:"))
ilist = []
for i in range(num):
    ilist.append(int(input("Enter the "+str(i+1)+"th element :")))
freq = {}

for value in ilist:
    if value in freq:
        freq[value] += 1
    else:
        freq[value] = 1
modeList = [key for key in freq.keys() if freq[key] == max(freq.values())]
print("Mode of the list :",modeList)