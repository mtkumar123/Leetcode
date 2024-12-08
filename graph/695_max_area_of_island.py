class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        max_connected_nodes = 0
        visited_nodes = set()
        # index is tuple
        # index[0] - y axis
        # index[1] - x axis
        def dfs(index):
            if index in visited_nodes:
                return
            visited_nodes.add(index)
            # Move left
            if index[1] - 1 >=0 and grid[index[0]][index[1]-1] == 1:
                dfs((index[0], index[1] - 1))
            # Move right
            if index[1] + 1 < len(grid[index[0]]) and grid[index[0]][index[1]+1] == 1:
                dfs((index[0], index[1] + 1))
            # Move up
            if index[0] - 1 >=0 and grid[index[0]-1][index[1]] == 1:
                dfs((index[0] - 1, index[1]))
            # Move down
            if index[0] + 1 < len(grid) and grid[index[0]+1][index[1]] == 1:
                dfs((index[0] + 1, index[1]))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) in visited_nodes:
                    continue
                if grid[i][j] == 0:
                    continue
                initial_nodes = len(visited_nodes)
                dfs((i,j))
                after_dfs_nodes = len(visited_nodes)
                max_connected_nodes = max(max_connected_nodes, after_dfs_nodes-initial_nodes)
        return max_connected_nodes


s = Solution()
grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid2 = [[0,0,0,0,0,0,0,0]]
result = s.maxAreaOfIsland(grid1)
result2 = s.maxAreaOfIsland(grid2)
print()