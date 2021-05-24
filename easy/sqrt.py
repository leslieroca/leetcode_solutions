https://leetcode.com/problems/sqrtx


class Solution:
    def mySqrt(self, x: int) -> int:
        min_ = 1;
        max_ = x;
        
        while min_ <= max_:
            mid = (max_ + min_) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                max_ = mid - 1
            else:
                min_ = mid + 1
        return max_
