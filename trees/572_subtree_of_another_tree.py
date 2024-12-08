# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root and not subRoot:
            return True
        if not root and subRoot or root and not subRoot:
            return False

        def root_tree_traversal(node):
            if check_tree(node, subRoot):
                return True
            if node.left:
                if root_tree_traversal(node.left):
                    return True
            if node.right:
                if root_tree_traversal(node.right):
                    return True
            return False
            
                
        
        def check_tree(node1, node2):
            if node1.val != node2.val:
                return False
            if node1.left and node2.left:
                if not check_tree(node1.left, node2.left):
                    return False
            elif node1.left is None and node2.left is None:
                pass
            else:
                return False
            if node1.right and node2.right:
                if not check_tree(node1.right, node2.right):
                    return False
            elif node1.right is None and node2.right is None:
                pass
            else:
                return False
            return True
        return root_tree_traversal(root)

