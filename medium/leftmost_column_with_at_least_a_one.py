https://leetcode.com/problems/leftmost-column-with-at-least-a-one


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMa# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m,n = binaryMatrix.dimensions()
        
        def find_first_one(row, binaryMatrix):
            _ , n = binaryMatrix.dimensions()
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                # print("GET",  row, mid)
                if binaryMatrix.get(row, mid) == 1:
                    r = mid - 1
                else:
                    l = mid + 1
            return l if l < n else -1
        
        result = float('inf')
        for i in range(m):
            first_one_index = find_first_one(i, binaryMatrix) 
            if first_one_index != -1:
                result = min(result, first_one_index)
        
        return result if result != float('inf') else -1
