https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                sqr = nums[right]
                right -= 1
            else:
                sqr = nums[left]
                left += 1
            
            result[i] = sqr * sqr
        
        return result


