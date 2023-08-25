rows = int(input())
count = rows -1
for i in range(1,rows+1):
    for j in range(1,2*rows-i+1):
        if(j<i-1):
            print(end=" ")
        else:
            if j == i or j == (2*rows - i):
                print(chr(65+count),end=" ")
                
            else:
                print(end=" ")
    count -=1
    print()
5