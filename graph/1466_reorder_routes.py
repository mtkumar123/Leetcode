from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        cangozero = set()
        adjmatrix: dict[int, set] = {}
        neighbors: dict[int, set] = {}
        result = 0

        for c in connections:
            if c[0] not in adjmatrix:
                adjmatrix[c[0]] = set()
            adjmatrix[c[0]].add(c[1])
            if c[1] == 0:
                cangozero.add(c[0])

            if c[0] not in neighbors:
                neighbors[c[0]] = set()
            if c[1] not in neighbors:
                neighbors[c[1]] = set()
            neighbors[c[0]].add(c[1])
            neighbors[c[1]].add(c[0])

        # lets do bfs from zero using neighbor matrix
        queue = [0]
        visited = set()
        while queue:
            level = []
            current = queue.pop(0)
            visited.add(current)
            for n in neighbors[current]:
                if n in visited:
                    continue
                # check if n has path to 0 directly
                if n in cangozero:
                    pass
                # check if n has path to 0 indirectly
                elif (
                    n in adjmatrix
                    and len(adjmatrix[n].intersection(cangozero)) > 0
                ):
                    cangozero.add(n)
                # we have to change the direction
                else:
                    result += 1
                    cangozero.add(n)
                level.append(n)
            queue.extend(level)
        return result
