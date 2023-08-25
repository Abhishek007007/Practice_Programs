n = int(input())
count=0

for i in range(1,n+1):

    for j in range(1,n+i):
        if count == 26:
            count = 0
        if n == i:
            print(chr(65+count),end="")
            count +=1
        elif j == n-i+1:
            print(chr(65+count),end="")
            count +=1
        elif j == n+i-1:
            print(chr(65+count),end="")
            count +=1
        else:
            print(end=" ")
    
    print()
            