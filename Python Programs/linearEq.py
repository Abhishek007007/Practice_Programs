import numpy as np

A = np.array([[2, 3, -1], [4, 1, -3], [1, -2, 1]])
b = np.array([9, -2, 3])

x = np.linalg.solve(A, b)

print("The solution of the system of linear equations is:")
for i in range(len(x)):
    print("x{} = {}".format(i+1, x[i]))
