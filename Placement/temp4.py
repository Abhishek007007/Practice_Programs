count=0
n = int(input())
for i in range(1,n+1):
    if(i <= n//2 ):
        for j in range(1,n-i+2):
            if(j < i):
                print(end=" ")
            else:
                print(chr(65+count),end="") 
    else:
        for j in range(1,i+1):
            if(j<n-i+1):
                print(end=" ")
            else:
                print(chr(65+count),end="")
    print()
    count+=1