from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.helper(nums)
        
    def helper(self, nums: List[int]):
        self.prefix_sum = []
        for index, element in enumerate(nums):
            if index == 0:
                self.prefix_sum.append(element)
                continue
            self.prefix_sum.append(self.prefix_sum[-1] + element)
        assert len(self.prefix_sum) == len(self.nums)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left-1]
    
if __name__ == "__main__":
    x = NumArray([-2, 0, 3, -5, 2, -1])
    print(x.sumRange(0, 2))