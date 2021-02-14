https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        many_sub = 0
        
        s = sum(arr[0:k - 1])
                
        for i in range(len(arr) - (k - 1)):
            s = s + arr[i + (k - 1)] - (arr[i - 1] if i > 0 else 0)
            average = s / k

            if average >= threshold:
                many_sub += 1
            
        return many_sub


