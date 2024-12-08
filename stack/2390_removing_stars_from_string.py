class Solution:
    def removeStars(self, s: str) -> str:
        clean = ""
        for i in s:
            if not clean:
                clean += i
                continue

            if i == "*":
                clean = clean[:-1]
            else:
                clean += i
        return clean


s = Solution()
print(s.removeStars("leet**cod*e"))
