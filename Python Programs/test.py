import string
temp = ":dsjbf'snd="

print(string.punctuation)

for c in temp:
    if c in string.punctuation:
        temp = temp.replace(c,"")
print(temp)
