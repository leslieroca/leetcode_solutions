https://leetcode.com/problems/paint-fence


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        
        if k == 1 and n > 2:
            return 0
        
        def total(n):
            return same(n) + diff(n)
        
        def same(n):
            if n == 2:
                return k
            return diff(n - 1)
        
        mem = {}
        def diff(n):
            if n == 2:
                return k * (k-1)
            if n in mem:
                return mem[n]
            result =  total(n-1) * (k-1)
            mem[n] = result
            return result
            
                                
        return total(n) 
