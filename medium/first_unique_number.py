https://leetcode.com/problems/first-unique-number


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = []
        self.dic = {}
        self.nums = nums
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        while len(self.queue) > 0 and self.dic[self.queue[0]] > 1:
            self.queue.pop(0)
        
        if len(self.queue) == 0: 
            return -1
        
        return self.queue[0]

    
    
    def add(self, value: int) -> None:
        if value in self.dic:
            self.dic[value] += 1
        else:
            self.dic[value] = 1
            self.queue.append(value) 
