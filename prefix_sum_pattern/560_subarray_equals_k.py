""" 
[1, 2, 1, 3, 4, -7, 3] k=3 ans=5

[1, 0, 2, -2, 3]
{1: 3, 3: 1, 4: 1}

[1, 1, 1, 3]
{0: 1, 1:1, 2:1, 3:1, }

[-1, -1, -2, 1, 2, 3, 1, -1]
[1, 2, 3]
"""
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapper = {0: 1}
        curr_sum = 0
        result = 0
        for element in nums:
            curr_sum = curr_sum + element
            
            diff = curr_sum - k
            result += mapper.get(diff, 0)
            
            mapper[curr_sum] = mapper.get(curr_sum, 0) + 1
        return result
            
            

if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1], 0))