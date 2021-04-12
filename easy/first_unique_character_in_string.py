https://leetcode.com/problems/first-unique-character-in-a-string


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.Counter(s)
        
        for i, val in enumerate(s) :
            if dic[val] == 1:
                return i
        
        return -1 
