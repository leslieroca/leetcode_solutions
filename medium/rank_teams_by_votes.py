https://leetcode.com/problems/rank-teams-by-votes/submissions


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1 or len(votes[0]) == 1:
            return votes[0]

        d = {}
        for c in votes[0]:
            d[c] = [0] * len(votes[0])
        
        
        # construncting a dictionary with 
        for vote in votes:
            for i in range(len(vote)):
                d[vote[i]][i] += 1
        
        
        # build arra
        scores = []
        for key in d:
            scores.append((d[key], ord('A') - ord(key)))
        
        scores.sort(reverse=True)
        
        return "".join([chr(ord('A') - t[1]) for t in scores])
