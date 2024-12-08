class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        computed_values = {}
        computed_values[len(s)] = 1
        def dfs(index):
            if index in computed_values:
                return computed_values[index]
            if s[index] == "0":
                return 0
            res = dfs(index+1)
            if index+1 < len(s) and s[index] == "1":
                res += dfs(index+2)
            elif index+1 < len(s) and s[index] == "2" and s[index+1] in "0123456":
                res += dfs(index+2)
            computed_values[index] = res
            return res
        return dfs(0)

s = Solution()
res = s.numDecodings("11111")