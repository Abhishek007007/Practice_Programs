try:
    n1 = int(input())
except ValueError:
    print("Wrong Input")
try:
    n2 = int(input())
except ValueError:
    print("Wrong Input")

if(n1>=1 and n1<=10000 and n2 >=1 and n2<=10000 and n1<n2):
    for i in range(n1,n2+1):
        check = i
        s = 0
        n = 0
        while(check>0):
            n = n + 1
            check = check//10
        check = i
        while(check>0):
            s = s + (check%10)**n
            check = check//10
        if(i == s):
            print(i,end = " ")
else:
    print("Wrong Input")