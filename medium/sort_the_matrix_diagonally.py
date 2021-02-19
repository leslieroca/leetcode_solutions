https://leetcode.com/problems/sort-the-matrix-diagonally


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonal_starts = []
        rows = len(mat)
        cols = len(mat[0])
        
        for i in range(rows):
            diagonal_starts.append((i, 0))
        for j in range(1, cols):
            diagonal_starts.append((0, j))
            
        for start in diagonal_starts:
            diagonal_values = []
            i, j = start[0], start[1]
            while i < rows and j < cols:
                diagonal_values.append(mat[i][j])
                i, j = i + 1, j + 1
            
            diagonal_values.sort()
            i, j = start[0], start[1]
            index = 0
            while i < rows and j < cols:
                mat[i][j] = diagonal_values[index]
                i, j, index = i + 1, j + 1, index + 1
             
        return mat
