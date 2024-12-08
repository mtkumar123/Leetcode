class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        mapper = {}
        result = 0
        lp = 0
        for rp, n in enumerate(fruits):
            mapper[n] = mapper.get(n, 0) + 1
            while len(mapper.keys()) > 2:
                # we need to move lp to the
                # right till number of keys left is only
                # 2
                mapper[fruits[lp]] -= 1
                if mapper[fruits[lp]] == 0:
                    del mapper[fruits[lp]]
                lp += 1
            result = max(result, rp - lp + 1)
        return result
