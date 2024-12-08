from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        cost = {}
        finished = set()
        adj_matrix = defaultdict(list)
        for i in range(1, n+1):
            cost[i] = float("inf")
        
        for time in times:
            adj_matrix[time[0]].append(time[1:])
        
        smallest = k
        cost[k] = 0
        max_cost = 0

        while True:
            current_node = smallest
            current_cost = cost.pop(smallest)
            finished.add(current_node)
            max_cost = max(current_cost, max_cost)

            for neighbor in adj_matrix[current_node]:
                if neighbor[0] not in finished:
                    if current_cost + neighbor[1] < cost[neighbor[0]]:
                        cost[neighbor[0]] = current_cost + neighbor[1]
            
            if cost == {}:
                break
            smallest = min(cost, key=cost.get)
            if cost[smallest] == float("inf"):
                return -1
            
        return max_cost

s = Solution()
times = [[1,2,1]]
n = 2
k = 2
result = s.networkDelayTime(times, n, k)
print(result)