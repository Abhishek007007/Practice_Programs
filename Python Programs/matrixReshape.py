class Solution:
    def matrixReshape(mat, r: int, c: int):
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
            sol = []
            temp = []
            c1 = 0

            for row in mat:
                for col in row:
                    temp.append(col)
                    c1 +=1
                    if c1 == c:
                        c1 = 0
                        sol.append(temp)
                        temp = []
            return sol
        
print(Solution.matrixReshape([[1,2],[3,4]],4,1))