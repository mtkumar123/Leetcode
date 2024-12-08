"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        class Node:
            def __init__(self, val = 0, neighbors = None):
                self.val = val
                self.neighbors = neighbors if neighbors is not None else []
        
        visited_nodes = {}

        def dfs(node):
            if node.val in visited_nodes:
                return visited_nodes[node.val]
            
            new_node = Node(node.val)
            visited_nodes[node.val] = new_node
            for neighbor_node in node.neighbors:
                if neighbor_node.val not in visited_nodes:
                    dfs(neighbor_node)
                new_node.neighbors.append(visited_nodes[neighbor_node.val])
            return new_node
        
        if not node:
            return []

        new_first_node = dfs(node)
        return new_first_node
                
s = Solution()
result = s.cloneGraph(None)

