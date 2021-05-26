https://leetcode.com/problems/two-sum-ii-input-array-is-sorted



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            suma = numbers[left] + numbers[right]  
            if suma == target:
                return [left+1, right+1]
            elif suma < target:
                left += 1
            else:
                right -= 1
