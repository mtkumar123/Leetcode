class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        f_orange = 0
        r_orange = []
        depth = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    f_orange += 1
                if grid[y][x] == 2:
                    r_orange.append((y,x))
        
        while r_orange and f_orange>0:
            for orange in range(len(r_orange)):
                y, x = r_orange.pop(0)
                # up
                if y-1>=0 and grid[y-1][x] == 1:
                    grid[y-1][x] = 2
                    r_orange.append((y-1, x))
                    f_orange -=1
                # down
                if y+1<len(grid) and grid[y+1][x] ==1:
                    grid[y+1][x] = 2
                    r_orange.append((y+1, x))
                    f_orange -=1
                # left
                if x-1>=0 and grid[y][x-1] == 1:
                    grid[y][x-1] = 2
                    r_orange.append((y, x-1))
                    f_orange -=1
                # right
                if x+1<len(grid[y]) and grid[y][x+1] ==1:
                    grid[y][x+1] = 2
                    r_orange.append((y, x+1))
                    f_orange -=1
            depth += 1
        
        return depth if f_orange == 0 else -1

s = Solution()

grid1 = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
grid3 = [[0,2]]

x = s.orangesRotting(grid1)
y = s.orangesRotting(grid2)
z = s.orangesRotting(grid3)
print()
            

