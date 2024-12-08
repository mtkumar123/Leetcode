from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # aabababaa
        result = 1
        lp = 0
        rp = 0
        mapper = defaultdict(lambda: 0)
        while rp < len(s):
            mapper[s[rp]] += 1
            while (rp - lp + 1) - max(mapper.values()) > k:
                mapper[s[lp]] -= 1
                lp += 1
            result = max(result, (rp - lp + 1))
            rp += 1

        return result
