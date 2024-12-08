from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one, zero = 0, 0
        mapper = {}
        result = 0
        for index, element in enumerate(nums):
            if element:
                one += 1
            else:
                zero += 1
            
            if one - zero not in mapper:
                mapper[one-zero] = index
            
            if zero == one:
                result = index + 1
            else:
                result = max(result, index - mapper[one-zero])
        return result
            
            

if __name__ == "__main__":        
    x = [0,0,1,0,0,0,1,1]
    s = Solution()
    print(s.findMaxLength(x))