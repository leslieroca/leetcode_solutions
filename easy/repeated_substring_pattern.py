https://leetcode.com/problems/repeated-substring-pattern


Solution 1:

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1: -1]


Solution 2:

# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         for i in range(len(s) - 1):
#             sub_s = s[0:i+1]
#             if not self.can_construct(s, sub_s):
#                 continue
#             return True
        
#         return False
    
        
#     def can_construct(self, s, sub_s):
        
#         for i in range(0, len(s), len(sub_s)):
#             if s[i:len(sub_s)+i] != sub_s:
#                 return False
#         return True       
        
