class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        
        def bfs(row, col):
            queue = []
            visited_nodes = set()
            queue.append((row, col))
            cost = 0

            while queue:
                l = len(queue)
                for i in range(l):
                    r, c = queue.pop(0)
                    visited_nodes.add((r,c))
                    if r-1>=0 and rooms[r-1][c] > 0 and (r-1, c) not in visited_nodes:
                        queue.append((r-1, c))
                        visited_nodes.add((r-1,c))
                    if r+1<len(rooms) and rooms[r+1][c] > 0 and (r+1, c) not in visited_nodes:
                        queue.append((r+1, c))
                        visited_nodes.add((r+1,c))
                    if c-1>=0 and rooms[r][c-1] > 0 and (r, c-1) not in visited_nodes:
                        queue.append((r, c-1))
                        visited_nodes.add((r,c-1))
                    if c+1<len(rooms[r]) and rooms[r][c+1] > 0 and (r, c+1) not in visited_nodes:
                        queue.append((r, c+1))
                        visited_nodes.add((r,c+1))
                    rooms[r][c] = min(rooms[r][c], cost)
                cost+=1
            
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    bfs(i, j)
        
        return rooms





s = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
s.wallsAndGates(rooms)
