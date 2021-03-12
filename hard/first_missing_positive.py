https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        while smallest in nums:
            smallest += 1
        return smallest        
