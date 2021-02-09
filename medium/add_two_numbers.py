# Leetcode: https://leetcode.com/problems/add-two-numbers

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        tail = head
        carry = 0
        
        while l1 or l2:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            
            new_val = val1 + val2 + carry
            carry = 0
                
            if new_val > 9:
                new_val = new_val % 10
                carry = 1
                
            tail.next = ListNode(new_val)
            tail = tail.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if carry == 1:
            tail.next = ListNode(1)
        
        return head.next
            
