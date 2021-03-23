https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        self.grid = grid
        counter = 0
        
        for e in grid:
            for val in e:
                if val < 0:
                    counter += 1
        
        return counter     
