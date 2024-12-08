from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        root = head
        count = 1
        while root:
            if count == k:
                firstnode = root
                break
            else:
                root = root.next
                count += 1

        lp = head
        rp = firstnode

        while rp.next:
            lp = lp.next
            rp = rp.next

        secondnode = lp
        temp = secondnode.val
        secondnode.val = firstnode.val
        firstnode.val = temp

        return head
