https://leetcode.com/problems/middle-of-the-linked-list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        list_length = 0 
        current = head
        
        while current != None:
            current = current.next
            list_length += 1
        
        mid_length = list_length // 2
        current = head
        
        while mid_length > 0:         
            current = current.next
            mid_length -= 1
            
        return current
