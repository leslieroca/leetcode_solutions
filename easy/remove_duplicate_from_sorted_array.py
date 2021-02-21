https://leetcode.com/problems/remove-duplicates-from-sorted-array



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums <= 1:
            return len_nums
        
        p = 0 
        runner = 1
        while runner < len_nums:
            if nums[p] != nums[runner]:
                p += 1
                nums[p] = nums[runner]
            runner += 1
        
        return p + 1
