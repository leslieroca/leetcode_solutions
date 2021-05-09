https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        reversed_nums = sorted(nums)
        
        for e in nums:
            result.append(reversed_nums.index(e))
            
        return result     
