https://leetcode.com/problems/longest-palindrome


from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        for v in counter.values():
            if v % 2 == 1:
                ans += 1
        return len(s) - ans + 1 if ans > 0 else len(s)


