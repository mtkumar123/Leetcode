# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        q = [root]
        new_root = None
        while q:
            cnode = q.pop(0)
            if not new_root:
                new_root = cnode
            if cnode.right:
                q.append(cnode.right)
            if cnode.left:
                q.append(cnode.left)
            temp = cnode.right
            cnode.right = cnode.left
            cnode.left = temp
        return new_root
        
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

x = TreeNode(val= 4, left= TreeNode(val= 2, left= TreeNode(val= 1, left= None, right= None), right= TreeNode(val= 3, left= None, right= None)), right= TreeNode(val= 7, left= TreeNode(val= 6, left= None, right= None), right= TreeNode(val= 9, left= None, right= None)))
s = Solution()
result = s.invertTree(x)
print()