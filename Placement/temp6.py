num = int(input())
count1=0
count2=0
for i in range(1,num+1):
    for j in range(1,num+1):
        if((i==1 or i == num) and (j == 1 or j==num)):
            print(end=" ")
        elif(i>1 and i<num and j>1 and j<num):
            print(end=" ")
        else:
            if(i%2==0):
                if count2 == 26:
                    count2 =0
                print(chr(97+count2),end="")
                count2 += 1
            else:
                if count1 == 26:
                    count1 =0
                print(chr(65+count1),end="")
                count1+= 1
    print()
