rows = int(input("Enter the number of rows in the matrix :"))
col = int(input("Enter the number of columns in the matrix :"))

sparse = {}
sparse[('rows','column')] = (rows,col)

matrix = []
print("Enter the matrix : ")
for i in range(rows):
    temp = []
    for j in range(col):
        temp.append(int(input("Enter the "+str((i,j))+"th element :")))
    matrix.append(temp)
print("Given Matrix")
for i,r in enumerate(matrix):
    for j,c in enumerate(r):
        print(c,"\t",end="")
        if(c != 0):
            sparse[(i,j)] = c
    print()
print(sparse)