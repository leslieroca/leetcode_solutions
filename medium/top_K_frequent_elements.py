https://leetcode.com/problems/top-k-frequent-elements



from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = [0]*k
        
        dic = collections.Counter(nums)
        i = 0
        while k > 0:
            max_val = max(dic.keys(), key=lambda key: dic[key])
            result[i] = max_val
            del dic[max_val]
            i -= 1
            k -= 1
        return result  
