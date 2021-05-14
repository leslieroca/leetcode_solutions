https://leetcode.com/problems/n-repeated-element-in-size-2n-array


from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)//2
        map_A = Counter(A)
        for key, value in map_A.items():
            if value == N:
                return key
