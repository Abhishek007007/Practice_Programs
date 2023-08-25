num1 = int(input())

for i in range(1,num1+1):
    for j in range(1,num1+2-i):
        print("*",end = "")
    print()
for i in range(1,num1):
    for j in range(1,i+2):
        print("*",end = "")
    print()
