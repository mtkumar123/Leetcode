from collections import defaultdict
class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        adj_matrix = defaultdict(list)
        inqueue = set()
        cost = {}
        for connection in connections:
            adj_matrix[connection[0]].append([connection[1], connection[2]])
            adj_matrix[connection[1]].append([connection[0], connection[2]])
        for i in range(1, n+1):
            cost[i] = float("inf")
        
        total_cost = 0
        #choose city 1 to start with
        cost[1] = 0
        for i in range(n):
            # Extract city with lowest cost
            smallest = min(cost, key=cost.get)
            if cost[smallest] == float("inf"):
                return -1
            inqueue.add(smallest)
            total_cost += cost[smallest]
            cost.pop(smallest)

            for neighbor in adj_matrix[smallest]:
                # Check if inqueue
                if neighbor[0] in inqueue:
                    continue
                # Check the weight
                if cost[neighbor[0]] > neighbor[1]:
                    cost[neighbor[0]] = neighbor[1]
                
        return total_cost
        

s = Solution()
connections = [[1,2,5],[1,3,6],[2,3,1]]
n = 3

result = s.minimumCost(n, connections)
print()
# n = 4
# connections = [[1,2,3],[3,4,4]]
# result = s.minimumCost(n, connections)
print()
