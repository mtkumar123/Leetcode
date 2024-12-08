# n = 3 ((())) (()()) (()()) ()()() ()(()) (())() - 6
# n = 2 (()) ()() - 4
# n = 1 () - 2

# n = 4 - 8 
# (((()))) (((()())))
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = {}
        temp = {}
        for i in range(2*n):
            if not result:
                result["("] = (1,0)
                continue
            for key, value in result.items():
                if value[0] < n:
                    temp[key+"("] = (value[0]+1, value[1])
                if value[1] < value[0]:
                    temp[key+")"] = (value[0], value[1]+1)
            result = temp
            temp = {}
        return list(result.keys())

s = Solution()
s.generateParenthesis(3)
            