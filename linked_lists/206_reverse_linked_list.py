from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        
        n = head
        prev_node = None
        while n:
            temp = n.next
            n.next = prev_node
            prev_node = n
            n = temp
        
        return prev_node