https://leetcode.com/problems/lru-cache


class DLL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
            
            
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLL(-1,-1)
        self.tail = self.head
        self.dic = {}
        self.length = 0
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        val = node.val
        
        if node == self.tail:
            return val
            
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        
        return val
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            
            if node == self.tail:
                return
            
            node.prev.next = node.next
            node.next.prev = node.prev
            
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            
        else:
            node = DLL(key, value)
            self.dic[key] = node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.length += 1
            
            if self.length > self.capacity:
                delete = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.dic[delete.key]
                self.length -= 1

