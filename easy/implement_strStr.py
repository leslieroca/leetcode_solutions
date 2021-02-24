https://leetcode.com/problems/implement-strstr


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack)):
            if haystack[i:len(needle)+i] == needle:
                return i
        
        return -1
