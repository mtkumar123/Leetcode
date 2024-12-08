class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        computed_values = {}
        computed_values[0] = (nums[0], nums[0])
        computed_values[1] = (nums[1], max(nums[0], nums[1]))
        house = 2
        while house < len(nums):
            computed_values[house] = (0, 0)
            for i in range(house, 1, -1):
                max1 = max(computed_values[house][0], computed_values[i-2][0] + nums[house])
                max2 = max(computed_values[house][1], computed_values[i-1][1])
                computed_values[house] = (max1, max2)
            house += 1
        return max(computed_values[len(nums)-2][0], computed_values[len(nums)-1][1])
                
s = Solution()
res = s.rob([1,2,3,1])