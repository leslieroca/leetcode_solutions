class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):text1,text2 = text2,text1
            
        n,m = len(text1),len(text2)
        dp = [0]*m
        ans = 0
        
        for i in range(n):
            curr = 0
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[j],curr = curr + 1,dp[j]
                else:
                    curr = max(curr,dp[j])
                    
        return max(dp)



