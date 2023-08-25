num = int(input("Enter the number of cubes you want to add to file :"))

f = open("output.txt","w")
for i in range(num):
    cube = int(input())
    f.write(str(cube)+"^3 = "+str(cube**3)+"\n")
f.close()