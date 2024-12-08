from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mapper = {} # store reminder to index
        # if we see the same reminder again then
        # it means that we have added a multiple of k
        # to the prefix sum
        curr_sum = 0

        for index, n in enumerate(nums):
            curr_sum += n
            r = curr_sum % k
            
            if r == 0 and index > 0:
                return True
            
            if r in mapper:
                if index - mapper[r] > 1:
                    return True
            else:
                mapper[r] = index
        return False
            
                
                
            

if __name__ == "__main__":
    s = Solution()
    print(s.checkSubarraySum([5,0,0,0], 3))