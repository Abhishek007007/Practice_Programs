import string
f = open("k.txt","r")
content  = f.readlines()
f.close()

f = open("output.txt","w")
for line in content:
    line = line.translate(str.maketrans('', '',string.punctuation))
    f.write(line)
f.close()