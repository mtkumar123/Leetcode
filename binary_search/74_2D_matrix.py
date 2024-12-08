import math
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        vert = [(row[-1], row[0], index) for index, row in enumerate(matrix)]
        
        def vert_binary_search(vert, i, target):
            if not vert:
                return -1
            median = int(len(vert)/2) - 1 if len(vert)%2==0 else math.floor(len(vert)/2)
            if target == vert[median][0]:
                return vert[median][2]
            if target > vert[median][0]:
                return vert_binary_search(vert[median+1:], i+median, target)
            elif target < vert[median][0] and target == vert[median][1]:
                return vert[median][2]
            elif target < vert[median][0] and target > vert[median][1]:
                return vert[median][2]
            elif target < vert[median][0]:
                return vert_binary_search(vert[:median], i, target)
        
        vert_index = vert_binary_search(vert, 0, target)
        if vert_index == -1:
             return False
         
        def binary_search(nums, i, target):
            if not nums:
                return False
            median = int(len(nums)/2) - 1 if len(nums)%2==0 else math.floor(len(nums)/2)
            if target > nums[median]:
                return binary_search(nums[median+1:], i+median, target)
            elif target < nums[median]:
                return binary_search(nums[:median], i, target)
            elif target == nums[median]:
                return True
            
        return binary_search(matrix[vert_index], 0, target)

s = Solution()
result = s.searchMatrix(matrix = [[1,3]], target = 1)
print()