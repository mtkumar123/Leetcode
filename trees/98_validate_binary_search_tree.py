# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            lflag = True
            rflag = True
            if node.left:
                if not (dfs(node.left) and node.left.val < node.val):
                    lflag = False
            if node.right:
                if not (dfs(node.right) and node.right.val > node.val):
                    rflag = False
                
            if lflag and rflag:
                return True
            return False

        return dfs(root)

x = TreeNode(val= 5, left= TreeNode(val= 4, left= None, right= None), right= TreeNode(val= 6, left= TreeNode(val= 3, left= None, right= None), right= TreeNode(val= 7, left= None, right= None)))
s = Solution()
result = s.isValidBST(x)