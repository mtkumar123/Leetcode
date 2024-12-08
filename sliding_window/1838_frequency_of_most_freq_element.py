class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        lp = 0
        total, result = 0, 0
        for rp, n in enumerate(nums):
            # num at rp is the biggest so far
            # for the window
            total += n
            while n * (rp - lp + 1) > total + k:
                # this basically considers the
                # total sum reachable when all the
                # numbers in the window are the largest number
                # which is at rp.
                # if the total of the window added with k
                # increments is greater or equal that means
                # the window is still valid
                total -= nums[lp]
                lp += 1
            result = max(result, rp - lp + 1)
        return result


if __name__ == "__main__":
    s = Solution()
    s.maxFrequency(
        [1, 2, 4],
        5,
    )
