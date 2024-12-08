from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # use the mapper to store the remainder
        # based on the prefix sum and the value
        # will be the number of possible positions
        # where we have seen that remainder before
        # this way we can be like oh if we remove the 
        # sum till that position our remainder will 
        # reduce by that number
        mapper = {0: 1}
        sum = 0
        result = 0
        for n in nums:
            sum += n
            remainder = sum % k
            result += mapper.get(remainder, 0)
            
            mapper[remainder] = mapper.get(remainder, 0) + 1
            
        return result