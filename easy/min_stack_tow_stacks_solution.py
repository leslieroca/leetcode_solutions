https://leetcode.com/problems/min-stack


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_stack = list()
        

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            self.min_stack.append(x)
        else:
            self.stack.append(x)
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return -1
        else:
            popped = self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
            return popped
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]        


