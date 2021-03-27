https://leetcode.com/problems/sort-array-by-parity

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0 
        j = len(A) - 1
        while i < j:
            if A[j] % 2 != 0:
                j -=1
            elif A[i] % 2 != 0:
                [A[i], A[j]] = [A[j], A[i]]
            else:
                i += 1
        
        return A
