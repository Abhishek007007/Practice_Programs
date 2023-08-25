def binToDec(n):
    exp = 1
    sum = 0
    for item in n:
        if(item == '1'):
            sum += exp
        exp *= 2
    return sum

num = input()
num = ('0'*(3 - len(num)%3)) + num
oct = ''
print(num)

for i in range(0,len(num),3):
    print(num[i+2:i])
    oct += str(binToDec(num[i+3:i+1:-1]))

print(int(oct))