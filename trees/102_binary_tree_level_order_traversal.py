# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        width = 1
        res = []
        while queue:
            level = []
            new_width = 0
            for i in range(width):
                cnode = queue.pop(0)
                level.append(cnode.val)
                if cnode.left:
                    queue.append(cnode.left)
                    new_width+=1
                if cnode.right:
                    queue.append(cnode.right)
                    new_width+=1
            res.append(level)
            width = new_width
        return res

x = TreeNode(val= 3, left= TreeNode(val= 9, left= None, right= None), right= TreeNode(val= 20, left= TreeNode(val= 15, left= None, right= None), right= TreeNode(val= 7, left= None, right= None)))
s = Solution()
result = s.levelOrder(x)
print()