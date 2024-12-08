""" 
[1,2,3,1], k = 3
1,3,5,2,1
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapper = {}
        for index, n in enumerate(nums):
            if n in mapper:
                if index - mapper[n] <= k:
                    return True
            mapper[n] = index
