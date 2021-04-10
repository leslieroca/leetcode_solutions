https://leetcode.com/problems/backspace-string-compare


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def final_sts(string) -> str:
            s_stack = []
            for ch in string:
                if ch != '#':
                    s_stack.append(ch)
                elif ch == '#' and len(s_stack) > 0:
                    s_stack.pop()
                    
            return "".join(s_stack)
                    
        return final_sts(S) == final_sts(T)
