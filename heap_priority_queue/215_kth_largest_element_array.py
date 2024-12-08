import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [(num*-1, num) for num in nums]
        heapq.heapify(nums)
        for i in range(k):
            result = heapq.heappop(nums)[-1]
        return result