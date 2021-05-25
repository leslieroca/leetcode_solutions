https://leetcode.com/problems/to-lower-case


class Solution:
    def toLowerCase(self, s: str) -> str: 
        return "".join(chr(ord(i) + 32) if "A" <= i <= "Z" else i for i in s)    
        

