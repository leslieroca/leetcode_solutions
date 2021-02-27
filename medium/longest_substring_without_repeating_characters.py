https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        longest = 0
        
        i = 0
        while i < len(s) :
            ch_index = dict()
            
            j = i
            while j < len(s) and s[j] not in ch_index:
                ch_index[s[j]] = j
                j += 1
                
            longest = max(longest, j - i)
            
            if j == len(s):
                break
            else:
                i = ch_index[s[j]] + 1
            
        return longest
