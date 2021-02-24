https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # [9,9,9,9] => [1,0,0,0,0]
        
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            if digits[i] == 9:
                digits[i] = 0
        
        digits.insert(0, 1)
            
        return digits
