class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        computed_values = {}
        computed_values[0] = cost[0]
        computed_values[1] = cost[1]
        highest_cost = sum(cost)
        steps = 2
        climbs = [1,2]
        while steps < len(cost):
            computed_values[steps] = highest_cost
            for climb in climbs:
                if steps-climb >=0:
                    computed_values[steps] = min(computed_values[steps], computed_values[steps-climb] + cost[steps])
            steps += 1
        return min(computed_values[len(cost)-1], computed_values[len(cost)-2])
        
s = Solution()
res = s.minCostClimbingStairs([10,15,20])