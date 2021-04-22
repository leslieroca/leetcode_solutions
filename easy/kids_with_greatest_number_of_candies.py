https://leetcode.com/problems/kids-with-the-greatest-number-of-candies


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        result = [None]*len(candies)
        
        for i, c in enumerate(candies):
            result[i] = (c + extraCandies) >= greatest
        
        return result
         

