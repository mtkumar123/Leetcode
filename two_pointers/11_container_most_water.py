from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height)-1
        max_area = 0
        
        while lp < rp:
            max_area = max((rp-lp) * min(height[lp], height[rp]), max_area)
            if height[lp]<=height[rp]:
                lp+=1
            else:
                rp-=1
        
        return max_area

s = Solution()
result = s.maxArea([2,3,4,5,18,17,6])
print(result)