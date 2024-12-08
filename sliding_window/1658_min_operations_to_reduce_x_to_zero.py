class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # target is the numbers excluded
        # from the operations
        # we want to make that window as
        # large as possible
        target = sum(nums) - x
        result = -1
        lp = 0
        currsum = 0
        for rp, n in enumerate(nums):
            currsum += n
            while currsum > target and lp <= rp:
                # move lp till it is smaller
                currsum -= nums[lp]
                lp += 1
            if currsum == target:
                result = max(result, rp - lp + 1)
        return len(nums) - result if result else -1
