def bintoOct(num):
    power = 1
    oct = 0
    for i in range(3):
        if(num[i]=='1'):
            oct += power
        power *=2
    return str(oct)
octstr=""
binstr = input()
revBinStr = binstr[::-1]

if len(revBinStr)%3 != 0:
    revBinStr+= "0"*(3-len(revBinStr)%3)

for i in range(0,len(revBinStr),3):
    octstr += bintoOct(revBinStr[i:i+3])
print(int(octstr[::-1]))