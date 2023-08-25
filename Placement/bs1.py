
bintr = f"{int(input()):b}"
s = [1-int(x) for x in bintr]
newbin = "".join(map(str,s))
print(int(newbin,2))