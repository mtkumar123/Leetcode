import math
from typing import Optional


# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        nodes = []
        n: ListNode = head
        while n:
            nodes.append(n)
            t = n.next
            n.next = None
            n = t
        
        n: Optional[ListNode] = None
        while nodes:
            if not n:
                n = nodes.pop(0)
                n.next = nodes.pop()
                continue
            n = n.next
            n.next = nodes.pop(0)
            n = n.next
            if nodes:
                n.next = nodes.pop()
        
        return head
            
            
            