from typing import List
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append((index, temp))
                continue
            while stack:
                if stack[-1][1] < temp:
                    result[stack[-1][0]] = index - stack[-1][0]
                    stack.pop()
                else:
                    break
            stack.append((index, temp))
        return result

s = Solution()
s.dailyTemperatures([30,40,50,60])
                
            