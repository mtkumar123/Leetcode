class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        cur = 0
        result = 0
        lp = 0
        vowels = set(["a", "e", "i", "o", "u"])
        for rp, n in enumerate(s):
            if n in vowels:
                cur += 1
            result = max(result, cur)
            if (rp - lp + 1) == k:
                # move lp to the right
                if s[lp] in vowels:
                    cur -= 1
                lp += 1
        return result
