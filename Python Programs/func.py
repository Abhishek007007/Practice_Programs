def fn1(n):
    ret = (22 * n) + n + 5
    return ret

n = int(input("Enter the number :"))
ret = fn1(n)

print("fn(",n,") = ",ret)