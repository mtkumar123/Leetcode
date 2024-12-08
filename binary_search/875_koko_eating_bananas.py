import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        
        def binary_search(min_speed, max_speed):
            if not min_speed < max_speed:
                return max_speed
            median = math.floor((max_speed+min_speed)/2) 
            total_hours = 0
            for pile in piles:
                total_hours+= math.ceil(pile/median)
            if total_hours <= h:
                return binary_search(min_speed, median)
            elif total_hours > h:
                return binary_search(median+1, max_speed)
        
        return binary_search(1, max_pile)

s = Solution()
result = s.minEatingSpeed(piles = [30,11,23,4,20], h = 6)
print()