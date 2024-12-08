from collections import defaultdict
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        cost = {}
        previous_hops = defaultdict(lambda: -1)
        for i in range(n):
            cost[i] = float("inf")
        cost[src] = 0

        for i in range(n):
            for flight in flights:
                start_city = flight[0]
                end_city = flight[1]
                price = flight[2]
                if cost[start_city] + price < cost[end_city]:
                    if previous_hops[start_city] < k:
                        cost[end_city] = cost[start_city] + price
                        previous_hops[end_city] = previous_hops[start_city] + 1

        
        if cost[dst] == float("inf"):
            return -1
        return cost[dst]

s = Solution()
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
n = 4
src = 0
dst = 3
k = 1
result = s.findCheapestPrice(n, flights, src, dst, k)
print()