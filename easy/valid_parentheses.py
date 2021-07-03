https://leetcode.com/problems/valid-parentheses



class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if dic.get(char, None) is not None:
                cur = ""
                if len(stack) != 0:
                    cur = stack.pop()
                if cur != dic[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


