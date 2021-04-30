https://leetcode.com/problems/counting-elements


class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = 0
        dic = collections.Counter(arr)
        
        for e in arr:
            if (e + 1) in dic:
                counter += 1
                
        return counter
