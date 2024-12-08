class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        mapper = {0: 1}
        currsum = 0
        result = 0
        for index, n in enumerate(nums):
            currsum += n
            diff = currsum - goal
            if diff in mapper:
                result += mapper[diff]
            mapper[currsum] = mapper.get(currsum, 0) + 1
        return result
