https://leetcode.com/problems/happy-number


class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getDigits(num):
            digits = []
            while num > 0:
                digits.append(num % 10)
                num = math.trunc(num / 10)
            return digits
        
        def sqrSum(arr) -> int:
            sum_squared = 0
            for e in arr:
                sum_squared += e**2
            return sum_squared
        
        
        my_set = set()
        while n != 1 and n not in my_set:  
            my_set.add(n)
            n = sqrSum(getDigits(n))
           
            
        return n == 1
