from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj_matrix = defaultdict(list)
        for prereq in prerequisites:
            adj_matrix[prereq[1]].append(prereq[0])

        for course in range(numCourses):
            if course not in adj_matrix:
                adj_matrix[course] = []
        
        visited = set()
        stack = []
        topo_sort = []

        def dfs(node):
            if node in visited:
                if node in stack:
                    return False
                return True
            visited.add(node)
            stack.append(node)
            if not node in adj_matrix:
                stack.pop(-1)
                topo_sort.insert(0, node)
                return True
            for neighbor in adj_matrix[node]:
                flag = dfs(neighbor)
                if not flag:
                    return False
            stack.pop(-1)
            topo_sort.insert(0, node)
            return True
        
        for node in adj_matrix:
            if node not in visited:
                flag = dfs(node)
                if not flag:
                    return []
        
        return topo_sort

s = Solution()
numCourses = 1
prerequisites = []
result = s.findOrder(numCourses, prerequisites)
print()