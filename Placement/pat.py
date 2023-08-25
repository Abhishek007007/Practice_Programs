num1 = int(input())
num2 = num1 + 1

for i in range(1,num1+1):
    for j in range(1,num1-i+1):
        print(end=" ")
    while(i>0):
        print("*",end = "")
        i-=1
    print()