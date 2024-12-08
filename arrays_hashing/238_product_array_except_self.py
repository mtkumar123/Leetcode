from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_multi = []
        backward_multi = []
        result = [1]*(len(nums))
        for index in range(len(nums)):
            if index == 0:
                forward_multi.append(nums[index])
            else:
                forward_multi.append(forward_multi[index-1]*nums[index])
        
        for index in range(len(nums)-1, -1, -1):
            if index == len(nums)-1:
                backward_multi.append(nums[index])
            else:
                backward_multi.insert(0, backward_multi[0]*nums[index])
        
        for index in range(len(nums)):
            if index == 0:
                result[0] = backward_multi[index+1]
            elif index == len(nums)-1:
                result[index] = forward_multi[index-1]
            else:
                result[index] = forward_multi[index-1] * backward_multi[index+1]
        return result

s = Solution()
res = s.productExceptSelf([1,2,3,4])
print()
            