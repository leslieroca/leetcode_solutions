https://leetcode.com/problems/product-of-array-except-self


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        right = [0]*l
        left = [0]*l
        result = [0]*l
      
        left[0] = 1
        for i in range(1, l):
            left[i] = nums[i - 1] * left[i - 1]
            right[l - 1] = 1
            
        for i in reversed(range(l - 1)):
            right[i] = nums[i + 1] * right[i + 1]
        
      
        for i in range(l):
             result[i] = left[i] * right[i]
        
        return result
