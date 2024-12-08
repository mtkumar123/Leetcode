# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        res = []
        width = 1
        while queue:
            new_width = 0
            for i in range(width):
                cnode = queue.pop(0)
                if cnode.left:
                    queue.append(cnode.left)
                    new_width += 1
                if cnode.right:
                    queue.append(cnode.right)
                    new_width += 1
            width = new_width
            res.append(cnode.val)
        return res
                