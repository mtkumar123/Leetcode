class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        expected = {}
        window = {}
        lp = 0
        for c in s1:
            expected[c] = expected.get(c, 0) + 1

        for index, rp in enumerate(s2):
            window[rp] = window.get(rp, 0) + 1

            if index - lp + 1 == len(s1):
                # check
                if expected == window:
                    return True
                else:
                    # reduce lp character count
                    window[s2[lp]] -= 1
                    if window[s2[lp]] == 0:
                        del window[s2[lp]]
                    # increase lp
                    lp += 1
        return False
