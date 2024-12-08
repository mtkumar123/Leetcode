class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        class Node:
            def __init__(self, parent, rank, value):
                self.parent = parent
                self.rank = rank
                self.value = value
        
        def make_node(value):
            return Node(None, 0, value)
        
        def find_root(node):
            if node.parent == None:
                return node
            node.parent = find_root(node.parent)
            return node.parent
        
        def link(node1, node2):
            if node1.rank > node2.rank:
                node2.parent = node1
            else:
                node1.parent = node2
                if node1.rank == node2.rank:
                    node2.rank += 1
        
        def union(node1, node2):
            link(find_root(node1), find_root(node2))

        graph = {}
        edge_not_added = None

        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = make_node(edge[0])
            if edge[1] not in graph:
                graph[edge[1]] = make_node(edge[1])
            if find_root(graph[edge[0]]) != find_root(graph[edge[1]]):
                union(graph[edge[0]], graph[edge[1]])
            else:
                edge_not_added = edge
        return edge_not_added

s = Solution()
edges = [[1,2],[1,3],[2,3]]
result = s.findRedundantConnection(edges)
print(result)        
                
# edges = [[1,2],[1,3],[2,3]]