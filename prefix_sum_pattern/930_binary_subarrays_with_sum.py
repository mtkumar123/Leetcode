from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mapper = {0: 1}
        result = 0
        curr_sum = 0
        for n in nums:
            curr_sum += n
            diff = curr_sum - goal
            result += mapper.get(diff, 0)
            
            mapper[curr_sum] = mapper.get(curr_sum, 0) + 1
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.numSubarraysWithSum([1,0,1,0,1], 2))