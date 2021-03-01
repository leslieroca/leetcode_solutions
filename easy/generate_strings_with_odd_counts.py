https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts


class Solution:
    def generateTheString(self, n: int) -> str:
        result = "a"
        
        if n % 2 == 0:
            result += "b" * (n - 1)
        else:
            result *= n
            
        return result   
        
