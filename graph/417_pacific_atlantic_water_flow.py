### Think of using intersection next time!
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        def check_connected_ocean(i, j):
            oceans = {"a_ocean": False, "p_ocean": False}
            visited_nodes = set()

            def dfs(i, j):
                if (i, j) in visited_nodes:
                    return
                cell_height = heights[i][j]
                visited_nodes.add((i,j))
                # Check if on the top/left edge
                if i==0 or j==0:
                    oceans["a_ocean"] = True
                # Check if on the bottom/right edge
                if i==len(heights)-1 or j==len(heights[i])-1:
                    oceans["p_ocean"] = True
                
                if oceans["a_ocean"] and oceans["p_ocean"]:
                    return

                # Check move left
                if j-1>=0 and heights[i][j-1] <= cell_height:
                    dfs(i, j-1)
                # Check move right
                if j+1<len(heights[i]) and heights[i][j+1] <= cell_height:
                    dfs(i, j+1)
                # Check move up
                if i-1>=0 and heights[i-1][j] <= cell_height:
                    dfs(i-1, j)
                # Check move down
                if i+1<len(heights) and heights[i+1][j] <= cell_height:
                    dfs(i+1, j)

            
            dfs(i, j)

            if oceans["p_ocean"] and oceans["a_ocean"]:
                return True
            return False

        
        for i in range(len(heights)): # y axis
            for j in range(len(heights[i])): # x axis
                connected = False
                connected = check_connected_ocean(i, j)
                if connected:
                    result.append([i, j])
        return result

s = Solution()
heights1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
heights2 = [[1]]
result = s.pacificAtlantic(heights1)
result2 = s.pacificAtlantic(heights2)
print()      
        