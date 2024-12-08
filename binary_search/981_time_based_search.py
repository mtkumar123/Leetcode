from collections import defaultdict
import math
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        def binary_search(l, r, target, timestamps):
            if l>r:
                return ""
            median = math.floor((l+r)/2)
            if timestamps[median][0] == target:
                return timestamps[median][1]
            elif timestamps[median][0] > target:
                return binary_search(l, median-1, target, timestamps)
            elif timestamps[median][0] < target:
                value = binary_search(median+1, r, target, timestamps)
                if not value:
                    return timestamps[median][1]
                else:
                    return value
            
        t = binary_search(0, len(self.data[key])-1, timestamp, self.data[key])
        print(t)
        return t

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)  
x = timeMap.get("foo", 1)         
b = timeMap.get("foo", 3)         
y = timeMap.set("foo", "bar2", 4) 
z = timeMap.get("foo", 4)       
a = timeMap.get("foo", 5)
print()       