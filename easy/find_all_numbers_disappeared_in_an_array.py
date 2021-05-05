https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        set_nums = set(nums)
        
        i = 1
        while i <= len(nums):
            if i not in set_nums:
                result.append(i)
            i += 1
            
        return result
