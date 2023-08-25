import string
f = open("k.txt","r")
content  = f.readlines()
f.close()

f1 = open("output1.txt","w")
f2 = open("output2.txt","w")
f1.write("Positive\n")
f2.write("Negative\n")
for line in content:
    if int(line) < 0:
        f2.write(line)
    else:
        f1.write(line)
f1.close()
f2.close()