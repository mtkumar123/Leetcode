from collections import defaultdict
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj_matrix = defaultdict(list)
        connected = 0
        for edge in edges:
            adj_matrix[edge[0]].append(edge[1])
            adj_matrix[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for neighbor in adj_matrix[n]:
                if neighbor not in visited:
                    dfs(neighbor)
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected += 1
        
        return connected

