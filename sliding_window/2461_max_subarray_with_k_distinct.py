""" 
[1, 3, 0, 5, 0, 1, 5]
"""


class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = {}
        cursum = 0
        winsum = 0
        lp = 0

        for index, rp in enumerate(nums):
            seen[rp] = seen.get(rp, 0) + 1
            winsum += rp

            if index - lp + 1 == k:
                # check if we have k keys in seen
                if len(seen) == k:
                    cursum = max(cursum, winsum)

                # if we did not then we did not update the sum
                # but anyways let's slide the left pointer
                seen[nums[lp]] -= 1
                winsum -= nums[lp]
                if seen[nums[lp]] == 0:
                    # remove key if it is 0 freq
                    seen.pop(nums[lp])
                lp += 1
        return cursum


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
