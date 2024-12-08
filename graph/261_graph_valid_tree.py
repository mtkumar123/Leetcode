from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not len(edges) == n - 1:
            return False

        connected = 0
        adj_matrix = defaultdict(list)
        visited = set()
        for edge in edges:
            adj_matrix[edge[0]].append(edge[1])
            adj_matrix[edge[1]].append(edge[0])
        
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for neighbor in adj_matrix[n]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected+=1
        
        if connected==1:
            return True
        return False

s = Solution()
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
s.validTree(n, edges)
        
        