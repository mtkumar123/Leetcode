import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums, i, target):
            if not nums:
                return -1
            median = int(len(nums)/2) - 1 if len(nums)%2==0 else math.floor(len(nums)/2)
            if target > nums[median]:
                return binary_search(nums[median+1:], i+median+1, target)
            elif target < nums[median]:
                return binary_search(nums[:median], i, target)
            else:
                return i+median
        
        return binary_search(nums, 0, target)

s = Solution()
result = s.search([-1,0,3,5,9,12], 9)
print()