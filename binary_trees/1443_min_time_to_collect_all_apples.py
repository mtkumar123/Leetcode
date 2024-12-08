from typing import List


class Solution:
    def minTime(
        self, n: int, edges: List[List[int]], hasApple: List[bool]
    ) -> int:
        adj_matrix = {0: []}
        for edge in edges:
            if edge[0] not in adj_matrix:
                adj_matrix[edge[0]] = []
            if edge[1] not in adj_matrix:
                adj_matrix[edge[1]] = []
            adj_matrix[edge[0]].append(edge[1])
            adj_matrix[edge[1]].append(edge[0])

        visited = set()

        def dfs(node):
            visited.add(node)
            result = 0
            for next_node in adj_matrix[node]:
                if next_node in visited:
                    continue
                val = dfs(next_node)
                if val:
                    result += val + 2
                elif hasApple[next_node]:
                    result += 2
            return result

        return dfs(0)


if __name__ == "__main__":
    s = Solution()
    x = s.minTime(
        7,
        [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        [False, False, True, False, True, True, False],
    )
    print(x)

""" 
Recursively for each subtree compute
how much time if that node was the root
would it be to collect all the apples downstream
So for leaf nodes which will be the base case
it will be 0
now the parent node with 2 leaf nodes
calculate the time 
add the time returned by the leaf node
then add the time if the child node is also apple
"""
