from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lifo = []
        node = head
        while node:
            lifo.append(node)
            node = node.next 
        
        i = 1
        curr_node = None
        next_node = None
        prev_node = None
        while i <= n and lifo:
            curr_node = lifo.pop()
            next_node = curr_node.next
            prev_node = lifo[-1] if lifo else None
            i+=1
            