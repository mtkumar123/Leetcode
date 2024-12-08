class Solution:
    def makeGood(self, s: str) -> str:
        clean = ""
        for index, i in enumerate(s):
            if not clean:
                clean += i
                continue

            if clean[-1] != i and (
                clean[-1] == i.upper() or clean[-1] == i.lower()
            ):
                # rule applies
                clean = clean[:-1]
            else:
                # rule doesn't apply
                clean += i
        return clean


s = Solution()
print(s.makeGood("leEeetcode"))
