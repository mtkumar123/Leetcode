from typing import List
""" 

"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        mapper = {0: 1}
        odds = 0
        result = 0
        for n in nums:
            if not n % 2 == 0:
                odds += 1
            diff = odds - k
            result += mapper.get(diff, 0)
            
            mapper[odds] = mapper.get(odds, 0) + 1
        return result
            
        
if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))