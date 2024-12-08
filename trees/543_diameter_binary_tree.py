class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_diameter):
            lheight = -1
            rheight = -1
            lmax_diameter = 0
            rmax_diameter = 0
            if node.left:
                lheight, lmax_diameter = dfs(node.left, max_diameter)
            if node.right:
                rheight, rmax_diameter = dfs(node.right, max_diameter)
            height = 1 + max(lheight, rheight)
            diameter = lheight + rheight + 2
            max_diameter = max(diameter, lmax_diameter, rmax_diameter)
            return height, max_diameter
        height, max_diameter = dfs(root, 0)
        return max_diameter