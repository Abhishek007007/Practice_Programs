num = int(input())
if(num%2 == 0):
    print("Even")
else:
    print("Odd")


num = int(input())
i =0
while(2**i <= num):
    print(2**i,end=" ")
    i+=1


num = int(input())
for i in range(1,num+1):
    for j in range(i):
        print("*",end="")
    print()