import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for point in points:
            distance.append((math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2), point))
        heapq.heapify(distance)
        k_closest = [point[-1] for point in heapq.nsmallest(k, distance)]
        return k_closest

s = Solution()
result = s.kClosest([[1,3],[-2,2]], 1)
print()