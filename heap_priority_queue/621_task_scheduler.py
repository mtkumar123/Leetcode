import heapq
from collections import Counter, defaultdict
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [c * -1 for c in Counter(tasks).values()]
        queue = []
        heapq.heapify(count)
        time = 1
        t_complete = 0
        while True:
            try:
                t = heapq.heappop(count)
                t_complete+=1
                if t+1 < 0:
                    queue.append((t+1, time+n))
            except IndexError:
                pass
            if t_complete == len(tasks):
                break
            time+=1
            if queue and queue[0][-1] < time:
                heapq.heappush(count, queue[0][0])
                queue.pop(0)
        return time
            
        
        
        
s = Solution()
s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 0)