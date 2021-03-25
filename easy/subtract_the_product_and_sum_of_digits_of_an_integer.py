https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer


import numpy

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        self.digits = []
        
        i = len(str(n))
        while i > 0:
            self.digits.append(n % 10)
            n = n // 10
            i -= 1
       
        product = numpy.prod(self.digits)
        suma = sum(self.digits)
        
        return product - suma
