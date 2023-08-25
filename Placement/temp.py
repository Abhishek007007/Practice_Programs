n = int(input())

for i in range(1,n+1):
    count=0
    for j in range(1,n+i):
        if(j < n-i+1):
            print(end=" ")
        else:
            if n%2 == 0:
                if i%2 == 0:
                    if (j%2 == 0):
                        print(end=" ")
                    else:
                        print(chr(65+count),end="")
                        count +=1
                else:
                    if (j%2 != 0):
                        print(end=" ")
                    else:
                        print(chr(65+count),end="")
                        count +=1
            elif n%2 != 0:
                if i%2 != 0:
                    if (j%2 == 0):
                        print(end=" ")
                    else:
                        print(chr(65+count),end="")
                        count +=1
                else:
                    if (j%2 != 0):
                        print(end=" ")
                    else:
                        print(chr(65+count),end="")
                        count +=1
    print()
      