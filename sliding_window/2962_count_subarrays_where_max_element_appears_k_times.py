class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        lp = 0
        count = 0
        maxn = max(nums)
        for rp, n in enumerate(nums):
            if n == maxn:
                count += 1
            while count > k or (count == k and lp <= rp and nums[lp] != maxn):
                if nums[lp] == maxn:
                    count -= 1
                lp += 1
            if count == k:
                result = result + lp + 1
        return result
