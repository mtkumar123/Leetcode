class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited_nodes = []
        num_islands = 0
        def dfs(row, column):
            # Add to visited
            visited_nodes.append((row, column))
            # Move left
            if column-1 >= 0:
                if (row, column-1) not in visited_nodes and grid[row][column-1] == "1":
                    dfs(row, column-1)
            # Move right
            if column+1<len(grid[row]):
                if (row, column+1) not in visited_nodes and grid[row][column+1] == "1":
                    dfs(row, column+1)
            # Move up
            if row-1>=0:
                if (row-1, column) not in visited_nodes and grid[row-1][column] == "1":
                    dfs(row-1, column)
            # Move down
            if row+1 < len(grid):
                if (row+1, column) not in visited_nodes and grid[row+1][column] == "1":
                    dfs(row+1, column)
        
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if (row, column) not in visited_nodes and grid[row][column] == "1":
                    num_islands += 1
                    dfs(row, column)
        
        return num_islands

s = Solution()
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
r1 = s.numIslands(grid1)
r2 = s.numIslands(grid2)
print(r1)
print(r2)
                