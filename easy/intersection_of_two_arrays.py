https://leetcode.com/problems/intersection-of-two-arrays


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        set_nums1 = set(nums1)
        for n in nums2:
            if n in set_nums1:
                result.append(n)
                set_nums1.remove(n)
        return result
