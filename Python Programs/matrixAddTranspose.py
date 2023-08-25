r1 = int(input("Enter the number of rows of the first matrix: "))
c1 = int(input("Enter the number of columns of the first matrix: "))
a1 = []
a2 = []
a3 = []
print("Enter the elements of the first matrix:")
for i in range(r1):
    temp = []
    for j in range(c1):
        temp.append(int(input("A[" + str(i+1) + "][" + str(j+1) + "]: ")))
    a1.append(temp)

r2 = int(input("Enter the number of rows of the second matrix: "))
c2 = int(input("Enter the number of columns of the second matrix: "))

print("Enter the elements of the second matrix:")
for i in range(r2):
    temp = []
    for j in range(c2):
        temp.append(int(input("A[" + str(i+1) + "][" + str(j+1) + "]: ")))
    a2.append(temp)

if r1 == r2 and c1 == c2:
    for i in range(r1):
        temp = []
        for j in range(c1):
            temp.append(a1[i][j] + a2[i][j])
        a3.append(temp)
else:
    print("Can't add the given matrices")

if a3:
    print("The sum of the matrices is:")
    for row in a3:
        for element in row:
            print(element, end=" ")
        print()

    transpose = [[a3[j][i] for j in range(len(a3))] for i in range(len(a3[0]))]
    print("The transpose of the sum matrix is:")
    for row in transpose:
        for element in row:
            print(element, end=" ")
        print()
