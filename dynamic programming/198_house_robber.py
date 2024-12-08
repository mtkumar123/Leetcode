class Solution(object):
    def help_rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        computed_values = {}
        computed_values[0] = (nums[0])
        computed_values[1] = (nums[1])
        house = 2
        while house < len(nums):
            computed_values[house] = nums[house]
            for i in range(house, 1, -1):
                computed_values[house] = max(computed_values[house], computed_values[house-2] + nums[i])
            house += 1
        return max(computed_values[len(nums)-1], computed_values[len(nums)-2])
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max1 = self.help_rob(nums[:-1])
        max2 = self.help_rob(nums[1:])
        return max(max1, max2)

s = Solution()
res = s.rob([1,2,3,1])