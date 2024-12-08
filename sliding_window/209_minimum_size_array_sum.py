class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        lp = 0
        currsum = 0
        size = float("inf")
        for rp, n in enumerate(nums):
            currsum += n
            while currsum >= target:
                size = min(size, (rp - lp + 1))
                # reduce size of window by
                # moving lp
                currsum -= nums[lp]
                lp += 1
        return size if size != float("inf") else result


if __name__ == "__main__":
    s = Solution()
    print(
        s.minSubArrayLen(
            7,
            [2, 3, 1, 2, 4, 3],
        )
    )
