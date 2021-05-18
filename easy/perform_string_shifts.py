https://leetcode.com/problems/perform-string-shifts


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:      
        val = 0 
        length_s = len(s)
        
        for d, a in shift:
            if d == 0:
                val += a
            else:
                val -= a
        
        val %= length_s
        
        return s[val:] + s[:val]
