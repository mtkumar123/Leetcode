class Solution(object):
    def maxDepth(self, root):
        """
        =type root= TreeNode
        =rtype= int
        """
        if not root:
            return 0
        def dfs(node, curr_depth, max_depth):
            curr_depth+=1
            max_depth = max(max_depth, curr_depth)
            if node.left:
                max_depth = dfs(node.left, curr_depth, max_depth)
            if node.right:
                max_depth = dfs(node.right, curr_depth, max_depth)
            return max_depth
        
        max_depth = dfs(root, 0, 0)
        return max_depth

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

x = TreeNode(val= 3, left= TreeNode(val= 9, left= None, right= None), right= TreeNode(val= 20, left= TreeNode(val= 15, left= None, right= None), right= TreeNode(val= 7, left= None, right= None)))
s = Solution()
result = s.maxDepth(x)