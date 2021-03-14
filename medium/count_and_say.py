https://leetcode.com/problems/count-and-say


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev_say = self.countAndSay(n -1)
        
        result = []
        i = 0 
        while i < len(prev_say):
            j = i
            while j < len(prev_say) and prev_say[j] == prev_say[i]:
                j += 1
            result.append(str(j-i) + prev_say[i])
            i = j
        
        return "".join(result)
    
    
