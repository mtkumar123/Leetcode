class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        mapper = {}
        currlen = 0
        lp = 0
        for index, rp in enumerate(s):
            if rp not in mapper:
                mapper[rp] = index
                currlen += 1
                result = max(result, currlen)
            else:
                dupindex = mapper[rp]
                # move lp to one to the right of dupindex
                while lp <= dupindex:
                    del mapper[s[lp]]
                    lp += 1
                # update currlen
                currlen = index - lp + 1
                # update mapper with position
                mapper[rp] = index
        return result


if __name__ == "__main__":
    s = Solution()
    s.lengthOfLongestSubstring("tmmzuxt")
