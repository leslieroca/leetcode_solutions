https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_list = list(pattern)
        s_list = s.split(" ")
        
        if len(p_list) != len(s_list):
            return False
        
        _map = dict()
        i = 0 
        while i < len(p_list):
            key = p_list[i]
            value = s_list[i]
            i += 1
            
            if key not in _map and value in _map.values():
                return False
            
            if key not in _map and value not in _map.values():
                _map[key] = value
                
            elif _map[key] != value:
                return False
       
        return True
