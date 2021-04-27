https://leetcode.com/problems/subarray-sum-equals-k/submissions


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_sub = 0
        sums = 0 
        dic = {0:1}
        
        for num in nums:
            sums += num
            if sums - k in dic:
                total_sub += dic[sums - k]
            if sums in dic:
                dic[sums] += 1
            else:
                dic[sums] = 1
        
        return total_sub
