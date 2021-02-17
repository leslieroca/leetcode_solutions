https://leetcode.com/problems/valid-parenthesis-string


class Solution:
    def checkValidString(self, s: str) -> bool:    
        stack_open = []
        stack_star = []
        
        for i, ch in enumerate(s):
            if ch == "(":
                stack_open.append(i)
            elif ch == "*":
                stack_star.append(i)
            
            else: # ch == ")"    
                if len(stack_open) > 0:
                    stack_open.pop()
                elif len(stack_star) > 0:
                    stack_star.pop()
                else: #len(stack_open) == 0 and len(stack_star) == 0
                    return False
                
        while len(stack_open) > 0 and len(stack_star) > 0:
            O = stack_open.pop()
            S = stack_star.pop()
            if O > S:
                return False
        
        return len(stack_open) == 0



