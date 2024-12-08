# ({[]()})
# ()[]{}
class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for c in s:
            if c in {"{", "[", "("}:
                queue.append(c)
            elif c in {"}", "]", ")"}:
                if queue and queue.pop()+c in {"{}", "()", "[]"}:
                    continue
                else:
                    return False
        if queue:
            return False
        return True

s = Solution()
result = s.isValid("({[]()})")
print(result)