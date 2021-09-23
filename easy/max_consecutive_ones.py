https://leetcode.com/problems/max-consecutive-ones


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        
        for num in nums:
            if num != 1:
                max_count = max(max_count, count)
                count = 0
            else:  # num == 1
                count += 1
        
        return max(max_count, count)
        
