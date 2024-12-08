from typing import List

# [7,1,5,3,6,4]


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lp = 0
        profit = 0

        for rp in range(1, len(prices)):
            if prices[rp] < prices[lp]:
                lp = rp
                continue
            profit = max(profit, prices[rp] - prices[lp])
