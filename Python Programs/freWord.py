def list_of_frequency(str1):
    freqDict = {}
    for c in str1:
        if c.isalpha():
            if c.lower() in freqDict:
                freqDict[c.lower()] += 1
            else : 
                freqDict[c.lower()] = 1
    freqList = list(freqDict.values())
    freqList.sort(reverse=True)
    sortedFreqDict = {}
    for value in freqList:
        for key in freqDict:
            if freqDict[key] == value:
                sortedFreqDict[key] = value
    for key in sortedFreqDict:
        print(key," : ",sortedFreqDict[key] )

str1 = input("Enter the string :")
list_of_frequency(str1)