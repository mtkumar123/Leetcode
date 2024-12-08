from typing import List


class Solution:
    def countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        result = 0
        visited = set()

        def dfs(i, j, subisland):
            # add node to visited
            visited.add((i, j))

            if grid1[i][j] != 1:
                subisland = False

            # check left
            if (
                j - 1 >= 0
                and (i, j - 1) not in visited
                and grid2[i][j - 1] == 1
            ):
                subisland = dfs(i, j - 1, subisland)
            # check right
            if (
                j + 1 < len(grid2[i])
                and (i, j + 1) not in visited
                and grid2[i][j + 1] == 1
            ):
                subisland = dfs(i, j + 1, subisland)
            # check up
            if (
                i - 1 >= 0
                and (i - 1, j) not in visited
                and grid2[i - 1][j] == 1
            ):
                subisland = dfs(i - 1, j, subisland)
            # check down
            if (
                i + 1 < len(grid2)
                and (i + 1, j) not in visited
                and grid2[i + 1][j] == 1
            ):
                subisland = dfs(i + 1, j, subisland)
            # now done
            return subisland

        for i, r in enumerate(grid2):
            for j, c in enumerate(r):
                if c == 1 and (i, j) not in visited:
                    subisland = dfs(i, j, True)
                    if subisland:
                        result += 1

        return result


s = Solution()
result = s.countSubIslands(
    [
        [1, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 0, 0],
        [1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
    ],
    [
        [1, 1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0],
    ],
)
print(result)
