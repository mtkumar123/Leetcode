from typing import List
import math


# Definition for a QuadTree node.
class Node:
    def __init__(
        self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        if not grid:
            return

        def dfs(n, r, c):
            # check if within the n size grid if all values are
            # the same
            allequal = True
            for i in range(0, n):
                for j in range(0, n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allequal = False
                        break

            if allequal:
                # this subgrid is all equal so we can just return a
                # leaf node here
                return Node(grid[r][c], True, None, None, None, None)
            else:
                # half the size of the subgrid now again
                n = n // 2
                newnode = Node(1, False, None, None, None, None)
                newnode.topLeft = dfs(n, r, c)
                newnode.topRight = dfs(n, r, c + n)
                newnode.bottomLeft = dfs(n, r + n, c)
                newnode.bottomRight = dfs(n, r + n, c + n)
                return newnode

        return dfs(len(grid), 0, 0)
