class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        lp = 0
        currprod = 1
        for rp, n in enumerate(nums):
            currprod *= n
            while currprod >= k and lp < rp:
                currprod /= nums[lp]
                lp += 1
            if currprod < k:
                result += rp - lp + 1
        return result
