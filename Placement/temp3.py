n = int(input())
for i in range(1,n+1):
    count = i
    for j in range(1,n+i):
        if j < n-i+1:
            print(end=" ")
        else:
            if j<n:
                print(count,end="")
                count+=1
            else:
                print(count,end="")
                count-=1
    print()