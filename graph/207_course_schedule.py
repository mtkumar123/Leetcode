from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_matrix = defaultdict(list)
        for prereq in prerequisites:
            adj_matrix[prereq[1]].append(prereq[0])
        
        visited = set()
        stack = []

        def dfs(node):
            if node in visited:
                if node in stack:
                    return False
                return True
            visited.add(node)
            stack.append(node)
            if not node in adj_matrix:
                stack.pop()
                return True
            for neighbor in adj_matrix[node]:
                flag = dfs(neighbor)
                if not flag:
                    return False
            stack.pop()
            return True
        
        for node in adj_matrix:
            if node not in visited:
                flag = dfs(node)
                if not flag:
                    return False
        return True

s = Solution()
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
result = s.canFinish(numCourses, prerequisites)
print()