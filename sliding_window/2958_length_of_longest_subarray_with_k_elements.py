class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mapper = {}
        lp = 0
        result = 0

        for rp, n in enumerate(nums):
            while mapper.get(n, 0) + 1 > k:
                # move lp to the right
                mapper[nums[lp]] -= 1
                lp += 1
            mapper[n] = mapper.get(n, 0) + 1
            result = max(result, rp - lp + 1)
        return result
