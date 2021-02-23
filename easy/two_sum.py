https://leetcode.com/problems/two-sum



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            if target - num in d:
                return [i, d[target-num]]
            
            d[num] = i
            
        
