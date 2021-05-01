https://leetcode.com/problems/decompress-run-length-encoded-list


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(0, len(nums), 2):
            freq = nums[i]
            while freq > 0:
                result.append(nums[i + 1]);
                freq -= 1
                
        return result

