https://leetcode.com/problems/unique-number-of-occurrences



from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_occ = Counter(arr)
        set_occ = set()
        
        for value in num_occ.values():
            set_occ.add(value)
            
        return len(num_occ) == len(set_occ)
            
