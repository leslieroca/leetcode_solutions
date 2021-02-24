https://leetcode.com/problems/set-matrix-zeroes


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        
        row_has_zero = [False] * n
        col_has_zero = [False] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_has_zero[i] = True 
                    col_has_zero[j] = True
        
        for i in range(n):
            for j in range(m):
                if row_has_zero[i] or col_has_zero[j]:
                    matrix[i][j] = 0
                    
            
