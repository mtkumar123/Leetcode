from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        fp = 0
        result = []
        while fp<len(nums)-2:
            if fp>0:
                if nums[fp] == nums[fp-1]:
                    fp+=1
                    continue
            sp = fp+1
            tp = len(nums) - 1
            sum = 0-nums[fp]
            while sp<tp:
                cur_sum = nums[sp] + nums[tp]
                if cur_sum < sum:
                    sp+=1
                elif cur_sum > sum:
                    tp-=1
                elif cur_sum == sum:
                    result.append([nums[fp], nums[sp], nums[tp]])
                    sp+=1
                    while nums[sp] == nums[sp-1] and sp<tp:
                        sp+=1
            fp+=1
        return result

s = Solution()
result = s.threeSum([0,0,0,0])
print(result)
        