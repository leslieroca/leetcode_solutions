https://leetcode.com/problems/design-phone-directory


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.hits = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        length = len(self.queue)
        
        if length > 0 and self.queue[length-1][0] == timestamp:
            # if same timestamp of last hit, just update the count of hits
            self.queue[length-1][1] += 1
            self.hits += 1
            return
                        
        # the "hit" call will append to the queue a list [timestamp, count], usin this in case several "hits" arrive at the same timestamp.        
        self.queue.append([timestamp, 1])
        self.hits += 1
        
        
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        
        if timestamp > 300:
            old_seconds = timestamp - 300 
            while len(self.queue) > 0 and self.queue[0][0] <= old_seconds:
                old = self.queue.pop(0)
                self.hits -= old[1]
        
        return self.hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
