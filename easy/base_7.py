https://leetcode.com/problems/base-7


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return "-" + self.toStr(abs(num), 7)
        else:
            return self.toStr(num, 7)
        
        
    
    def toStr(self, n, base):
        convertString = "0123456789ABCDEF"
        if n < base:
            return convertString[n]
        else:
            return self.toStr(n // base, base) + convertString[n % base]
