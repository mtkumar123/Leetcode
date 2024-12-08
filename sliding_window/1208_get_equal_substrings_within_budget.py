class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        currsum = 0
        lp = 0
        result = 0
        for rp, n in enumerate(s):
            diff = abs(ord(s[rp]) - ord(t[rp]))
            currsum += diff
            while currsum > maxCost:
                # move lp
                currsum -= abs(ord(s[lp]) - ord(t[lp]))
                lp += 1
            if currsum <= maxCost:
                result = max(result, rp - lp + 1)
        return result
