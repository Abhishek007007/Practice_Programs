d1 = {'a':10, 'b': 20, 'c':30}
d2 = {'a': 30, 'b': 20, 'd':40}

d3 = d1
for key in d2:
    if key in d3:
        d3[key] += d2[key]
    else:
        d3[key] = d2[key]

print(d3)