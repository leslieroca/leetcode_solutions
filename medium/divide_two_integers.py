https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        if abs(dividend) < abs(divisor):
            return 0
        
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        
        get_sum = self.get_sum(dividend_abs, divisor_abs)
        quotient, current_sum = get_sum[0], get_sum[1]
        difference = dividend_abs - current_sum
        
        while difference >= divisor_abs:
            get_sum = self.get_sum(difference, divisor_abs)
            quotient += get_sum[0]
            current_sum = get_sum[1]
            difference -= current_sum
        
        if dividend < 0:
            if divisor < 0:
                return quotient 
            if divisor > 0:
                return -quotient
        if dividend > 0:
            if divisor < 0:
                return -quotient
            if divisor > 0:
                return quotient
        
        
    def get_sum(self, total, to_sum):
        count = 1
        while to_sum + to_sum < total:
            to_sum += to_sum
            count += count
            
        return (count, to_sum)
            
            
