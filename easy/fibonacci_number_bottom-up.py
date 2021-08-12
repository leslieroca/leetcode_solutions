https://leetcode.com/problems/fibonacci-number



# Bottom-Up Solution
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        n_1 = 1
        n_2 = 1
        for num in range(3, n + 1):
            fib_num = n_1 + n_2
            n_1 = n_2
            n_2 = fib_num     
        return n_2


