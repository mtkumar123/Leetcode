from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            res = None
            if token == "*":
                res = int(stack[-2]) * int(stack[-1])
            elif token == "+":
                res = int(stack[-2]) + int(stack[-1])
            elif token == "/":
                res = int(stack[-2]) / int(stack[-1])
            elif token == "-":
                res = int(stack[-2]) - int(stack[-1])

            if res is not None:
                stack = stack[:-2]
                stack.append(res)
            else:
                stack.append(token)
        return stack[0]


s = Solution()
result = s.evalRPN(
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
)
print(result)
