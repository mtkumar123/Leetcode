from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        computed_values = {}
        computed_values[0] = (nums[0], nums[0])
        for index in range(1, len(nums)):
            if nums[index] == 0:
                computed_values[index] = (0,0)
            minv1 = computed_values[index-1][0] * nums[index]
            minv2 = computed_values[index-1][1] * nums[index]
            maxv1 = computed_values[index-1][1] * nums[index]
            maxv2 = computed_values[index-1][0] * nums[index]
            minv = min(minv1, minv2, nums[index])
            maxv = max(maxv1, maxv2, nums[index])
            computed_values[index] = (minv, maxv)
        max_result = nums[0]
        for key, value in computed_values.items():
            max_result = max(max_result, value[0], value[1])
        return max_result

s = Solution()
# [-2,-3,-4]
# [4,-2,-5]
# [-2,-3,-4,5,6]
# [-2,-3,5,6]
# [-2,-3,0,5,6]
# [-2,-3,-4,1,1,-5]
result = s.maxProduct([-2,-3,-4,1,1,-5])
