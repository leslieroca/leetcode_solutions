https://leetcode.com/problems/bitwise-and-of-numbers-range


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        result = 0
        for k in range(31):
            # checks k-th bit is set
            if m >> k & 1 == 1:
                # next number with k-th bit unset
                next_ = ((m >> k) + 1) << k
                if next_ > n:
                    result |= 1 << k
        return result
