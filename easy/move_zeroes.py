https://leetcode.com/problems/move-zeroes


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, p = 0, 0
        
        while i < len(nums):
            if nums[i] != 0:
                nums[p] = nums[i]
                i += 1
                p += 1
            else:
                i += 1
                
        for i in range(p, len(nums)):
            nums[i] = 0
