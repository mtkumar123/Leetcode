class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = ["0" if i % 2 == 0 else "1" for i in range(len(s) * 2)]
        b = ["1" if i % 2 == 0 else "0" for i in range(len(s) * 2)]
        diff1 = 0
        diff2 = 0
        for i in range(len(s)):
            if a[i] != s[i]:
                diff1 += 1
            if b[i] != s[i]:
                diff2 += 1
        lp = 0
        result = float("inf")
        # remove the element at lp
        # compare it to the element at lp
        # in a and b adjust diff1 and diff2
        # now add the element to the end of the string
        # this means rp will be lp + len(s)
        # do this while lp < len(s)
        while lp < len(s):
            if s[lp] != a[lp]:
                diff1 -= 1
            if s[lp] != b[lp]:
                diff2 -= 1

            if a[lp + len(s)] != s[lp]:
                diff1 += 1
            if b[lp + len(s)] != s[lp]:
                diff2 += 1

            result = min(diff1, diff2, result)
            lp += 1
        return result


if __name__ == "__main__":
    s = Solution()
    s.minFlips("01001001101")
