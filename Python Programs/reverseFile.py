f = open("k.txt","r")
content  = f.readlines()
f.close()
f = open("output.txt","w")
for line in reversed(content):
    f.writelines(line)
f.close