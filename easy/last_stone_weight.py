https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            heaviest1 = (0, 0)
            heaviest2 = (0, 0)
            for i in range(len(stones)):
                if stones[i] >= heaviest1[0]:
                    heaviest1, heaviest2 = (stones[i], i), heaviest1
                elif stones[i] > heaviest2[0]:
                    heaviest2 = (stones[i], i)
            
            stones.remove(heaviest1[0])
            stones.remove(heaviest2[0])
            
            smashed = heaviest1[0] - heaviest2[0]
            if smashed > 0:
                stones.append(smashed)
    
        if len(stones) == 0:
            return 0
        
        return stones[0]
