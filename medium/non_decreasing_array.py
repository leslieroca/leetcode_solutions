https://leetcode.com/problems/non-decreasing-array


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = 0;
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if i + 2 == len(nums):
                    nums[i + 1] = nums[i]   
                elif nums[i] <= nums[i + 2]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
                    
                if i > 0 and nums[ i - 1] > nums[i]:
                    return False
      
                modified += 1
    
        return modified <= 1
    
