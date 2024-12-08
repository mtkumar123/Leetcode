from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = 0
        mod = 10**9 + 7
        # 9, 9, 6, 9, 9, 5
        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                right = i - j
                left = j - stack[-1][0] if stack else j + 1
                res = (res + m * left * right) % mod
            stack.append((i, n))

        while stack:
            i, n = stack.pop()
            right = len(arr) - i
            left = i - stack[-1][0] if stack else i + 1
            res = (res + n * left * right) % mod
        return res


s = Solution()
print(s.sumSubarrayMins([3, 1, 2, 4]))
