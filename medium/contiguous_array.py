https://leetcode.com/problems/contiguous-array


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        counter = 0
        
        dic = {0: -1}
        
        for i, val in enumerate(nums):
            if val == 1:
                counter += 1
            else:
                counter -= 1
                
            if counter in dic:
                max_length = max(i - dic[counter], max_length)
            else:
                dic[counter] = i
                        
        return max_length
