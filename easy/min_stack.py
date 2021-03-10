https://leetcode.com/problems/min-stack


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.getMin())))

    def pop(self) -> None:
        if len(self.stack) == 0:
            return -1
        else:
            popped = self.stack.pop()
            return popped[0]
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]        

