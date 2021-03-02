https://leetcode.com/problems/reverse-linked-list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current:
            next_current = current.next
            current.next = prev
            prev = current
            current = next_current
        
        head = prev
        return head
