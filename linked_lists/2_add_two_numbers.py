from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        result = None
        carry = 0
        while l1 or l2:
            s = 0
            if l1 and l2:
                s = l1.val + l2.val + carry
            elif l1 or l2:
                s = l1.val + carry if l1 else l2.val + carry
            
            if s>=10:
                carry = 1
                s = s % 10
            else:
                carry = 0
            
            if not result:
                result = ListNode(s)
                head = result
            elif result:
                result.next = ListNode(s)
                result = result.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        if carry:
            result.next = ListNode(carry)
        
        return head
            
            
                
            