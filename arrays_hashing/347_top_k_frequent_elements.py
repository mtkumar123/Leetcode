import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda: 0)
        for num in nums:
            count[num]+=1
        result = []
        for key, value in count.items():
            if len(result) < k:
                heapq.heappush(result, (value, key))
            else:
                if value > result[0][0]:
                    heapq.heappop(result)
                    heapq.heappush(result, (value, key))
        return [r[1] for r in result]
            
s = Solution()
result = s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
print()