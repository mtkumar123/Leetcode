# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        =type p= TreeNode
        =type q= TreeNode
        =rtype= bool
        """
        if not p and not q:
            return True
        elif p and not q or q and not p:
            return False
        def dfs(node1, node2, flag):
            lflag = True
            rflag = True
            if node1.left and node2.left:
                lflag = dfs(node1.left, node2.left, flag)
            elif node1.left is None and node2.left is None:
                pass
            else:
                return False
            if node1.right and node2.right:
                rflag = dfs(node1.right, node2.right, flag)
            elif node1.right is None and node2.right is None:
                pass
            else:
                return False
            if lflag and rflag and node1.val == node2.val:
                return True
            return False
        return dfs(p, q, True)

p = TreeNode(val= 1, left= TreeNode(val= 2, left= None, right= None), right= TreeNode(val= 3, left= None, right= None))
q = TreeNode(val= 1, left= TreeNode(val= 2, left= None, right= None), right= TreeNode(val= 3, left= None, right= None))

s = Solution()
result = s.isSameTree(p,q)