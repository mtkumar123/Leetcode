from collections import defaultdict

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        adj_matrix = defaultdict(list)
        inqueue = {}
        cost = {}
        result = 0
        for i in range(len(points)-1):
            cost[i] = float("inf")
            inqueue[i] = True
            for j in range(i+1, len(points)):
                x_axis = abs(points[i][0]-points[j][0])
                y_axis = abs(points[i][1] - points[j][1])
                distance = x_axis + y_axis
                adj_matrix[i].append([j, distance])
                adj_matrix[j].append([i, distance])
        
        smallest = len(points) - 1
        cost[len(points)-1] = 0

        while True:
            current_node = smallest
            current_cost = cost.pop(smallest)
            inqueue[current_node] = False
            result += current_cost

            for neighbor in adj_matrix[current_node]:
                if inqueue[neighbor[0]] and cost[neighbor[0]] > neighbor[1]:
                    cost[neighbor[0]] = neighbor[1]
            if cost == {}:
                break
            smallest = min(cost, key=cost.get)
        
        return result
        
        
s = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
s.minCostConnectPoints(points)