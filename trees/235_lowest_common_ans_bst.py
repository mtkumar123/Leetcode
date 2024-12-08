# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        ans = []

        def dfs(node, p, q):
            if not ((p.val<node.val and q.val<node.val) or (p.val>node.val and q.val>node.val)):
                if p.val == node.val or q.val == node.val:
                    ans.append(node)
                    return
                return
            if p.val < node.val:
                ans.append(node.left)
                dfs(node.left, p, q)
            else:
                ans.append(node.right)
                dfs(node.right, p, q)

        
        dfs(root, p,q)
        return ans[-1]