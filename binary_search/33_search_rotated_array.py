import math
from typing import List

[1,2,3,4,5,6,7]
[2,3,4,5,6,7,1]
[5,6,7,1,2,3,4]


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rotation_binary_search(rotations):
            median = math.floor(len(rotations)/2) if len(rotations)%2!=0 else int(len(rotations)/2)-1
            if nums[rotations[median]] < nums[rotations[median]-1]:
                return rotations[median]
            if nums[0] > nums[rotations[median]]:
                return rotation_binary_search(rotations[:median])
            elif nums[rotations[median]] > nums[-1]:
                return rotation_binary_search(rotations[median+1:])
            else:
                return 0
        
        rotated_index = rotation_binary_search(list(range(len(nums))))
        
        def binary_search(sorted_nums, target, start):
            if not sorted_nums:
                return -1
            median = math.floor(len(sorted_nums)/2) if len(sorted_nums)%2!=0 else int(len(sorted_nums)/2)-1
            if sorted_nums[median]==target:
                return start+median
            elif sorted_nums[median] > target:
                return binary_search(sorted_nums[:median], target, start)
            elif sorted_nums[median] < target:
                return binary_search(sorted_nums[median+1:], target, start+median+1)
        
        
        min = nums[rotated_index]
        max = nums[rotated_index-1]
        
        if target >= min and target <= nums[-1]:
            if binary_search(nums[rotated_index:], target, 0) != -1:
                return binary_search(nums[rotated_index:], target, 0) + rotated_index
            return -1
        elif target <= max and target >= nums[0]:
            return binary_search(nums[:rotated_index], target, 0)
        else:
            return -1
    
        
            
            
        

s = Solution()
result = s.search(nums = [5,1,3], target = 2)
print(result)