from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for index, pos in enumerate(position):
            cars.append((pos, speed[index]))
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        
        for car in cars:
            time = (target - car[0])/car[1]
            if not stack:
                stack.append(time)
                continue
            if time > stack[-1]:
                stack.append(time)
        return len(stack)

s = Solution()
result = s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])