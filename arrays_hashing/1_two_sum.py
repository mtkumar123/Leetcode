class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index in range(len(nums)):
            if target-nums[index] in seen:
                return [index, seen[target-nums[index]]]
            seen[nums[index]] = index

s = Solution()
a = s.twoSum([-3,4,3,90], 0)
print()