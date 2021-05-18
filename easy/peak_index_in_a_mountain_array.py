https://leetcode.com/problems/peak-index-in-a-mountain-array


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i+1] < arr[i]:
                return i
