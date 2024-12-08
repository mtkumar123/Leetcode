class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        result = ""
        "1(2(4)3)"

        def dfs(node):
            nonlocal result
            result += f"{node.val}"
            if node.left == None and node.right == None:
                return
            if node.left:
                result += "("
                dfs(node.left)
                result += ")"
            else:
                result += "()"
            if node.right:
                result += "("
                dfs(node.right)
                result += ")"
            else:
                # no need for empty brackets
                # if right node is empty
                pass
            return

        dfs(root)

        return result
