# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        l = head
        new_head = None
        n = None
        prev_n = None
        visited_nodes = {}

        # Copy linked list without random pointer set
        while l:
            if not new_head:
                new_head = Node(l.val)
                prev_n = new_head
                visited_nodes[head] = new_head
                l = l.next
                continue
            n = Node(l.val)
            visited_nodes[l] = n
            prev_n.next = n
            prev_n = n
            n = n.next
            l = l.next
        
        # Go through linked list and set random pointer
        l = head
        n = new_head
        while l:
            if not l.random:
                l = l.next
                n = n.next
                continue
            n.random = visited_nodes[l.random]
            l = l.next
            n = n.next
        return new_head
            
        

