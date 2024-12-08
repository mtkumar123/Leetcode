from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp = 0
        lp = len(numbers)-1
        
        while fp<lp:
            sum = numbers[fp] + numbers[lp]
            
            if sum < target:
                fp+=1
            elif sum > target:
                lp-=1
            elif sum==target:
                return [fp+1, lp+1]
        return False

s = Solution()
result = s.twoSum(numbers = [-1,0], target = -1)
print(result)