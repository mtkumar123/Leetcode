class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # [1,2,3,4,5]
        subsets = []
        temp = []
        def func(index):
            if index == len(nums):
                subsets.append(temp.copy())
                return
            temp.append(nums[index])
            func(index+1)
            temp.pop()
            func(index+1)
        func(0)
        return subsets

s = Solution()
ans = s.subsets([1,2,3,4,5])