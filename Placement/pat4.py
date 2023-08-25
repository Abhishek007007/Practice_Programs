row = int(input())
count1 = 0
count2 = 0

for i in range(1,row+1):
    checker = 0
    for j in range(1,row-abs(((row//2)+1)- i)+1):
        if(j < abs(((row//2)+1)- i)+1):
            print(end=" ")
        else:
           if ((row//2)%2 != 0):
                if i%2 == 0 :
                    if j % 2 ==0:
                         print(end=" ")
                    else:
                        if checker == 0:
                            if(count1 == 10):
                                count1 = 0
                            print(count1,end="")
                            count1 +=1
                            checker = 1
                        else:
                            if count2 == 26:
                                count2 = 0
                            print(chr(97+count2),end="")
                            count2 +=1
                            checker = 0
                else:
                      if j % 2 == 0:
                            if checker == 0:
                                if(count1 == 10):
                                    count1 = 0
                                print(count1,end="")
                                count1 +=1
                                checker = 1
                            else:
                                if count2 == 26:
                                    count2 =0
                                print(chr(97+count2),end="")
                                count2 +=1
                                checker = 0
                      else:
                            print(end=" ")
           else:
                if i%2 != 0 :
                    if j % 2 ==0:
                         print(end=" ")
                    else:
                        if checker == 0:
                            if(count1 == 10):
                                count1 = 0
                            print(count1,end="")
                            count1 +=1
                            checker = 1
                        else:
                            if count2 == 26:
                                count2 =0
                            print(chr(97+count2),end="")
                            count2 +=1
                            checker = 0
                else:
                      if j % 2 == 0:
                            if checker == 0:
                                if(count1 == 10):
                                    count1 =0
                            
                                print(count1,end="")
                                count1 +=1
                                checker = 1
                            else:
                                if count2 == 26:
                                    count2 =0
                                print(chr(97+count2),end="")
                                count2 +=1
                                checker = 0
                      else:
                            print(end=" ")
    print()
                
                     
                         
                       
