https://leetcode.com/problems/climbing-stairs


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 or n == 3:
            return n
        else:
            dic = {3: 3, 4: 5}
            for i in range(5, n+1):
                dic[i] = dic.get(i-1) + dic.get(i-2)
                
        return dic.get(n)
        
