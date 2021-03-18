https://leetcode.com/problems/maximal-square/


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
    
        row, column = len(matrix), len(matrix[0])
        
        dp = [[0 for i in range(column+1)] for j in range(row+1)]
        
        max_square = 0
        
        for i in range(1, row + 1):
            
            for j in range(1, column+1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_square = max(max_square, dp[i][j])    
                    
        return max_square ** 2
