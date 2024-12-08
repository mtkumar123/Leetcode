from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        """
        [2,2,-1,2,2,2]
        [2,2,-1,1,3,1]
        """
        adjmatrix = defaultdict(list)
        head = None
        costmatrix = defaultdict(lambda: 0)

        # set up adjmatrix
        for i, v in enumerate(manager):
            costmatrix[i] = informTime[i]
            if not head and v == -1:
                head = i
                continue
            adjmatrix[v].append(i)

        # now do dfs based on adjmatrix
        result = [0]

        def dfs(n, time):
            if n not in adjmatrix:
                result[0] = max(result[0], time)
                return

            for child in adjmatrix[n]:
                dfs(child, time + costmatrix[n])

        dfs(head, 0)
        return result[0]
