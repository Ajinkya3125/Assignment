##Given an m x n binary matrix mat, return the number of special positions in mat.
##A position (i, j) is called special if mat[i][j] == 1 and all other elements
##in row i and column j are 0 (rows and columns are 0-indexed).


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        row_count = [0] * rows
        for i in range(rows):
            row_count[i] = sum(mat[i])

        col_count = [0] * cols
        for j in range(cols):
            for i in range(rows):
                col_count[j] += mat[i][j]
            
        special = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special += 1
        
        return special