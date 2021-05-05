https://leetcode.com/problems/find-numbers-with-even-number-of-digits


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        
        for n in nums:
            if len(str(n)) % 2 == 0:
                even_count += 1
                
        return even_count
