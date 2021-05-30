https://leetcode.com/problems/set-mismatch


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        b = sum(nums)
        c = sum(set(nums))
        a = (n * (n+1)) // 2
        missing = a - c
        duplicate = b - c
        return [duplicate, missing]
