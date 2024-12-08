class MinStack:

    def __init__(self):
        self.queue = []
        self.min_queue = []

    def push(self, val: int) -> None:
        if self.min_queue:
            if val<=self.min_queue[-1]:
                self.min_queue.append(val)
        else:
            self.min_queue.append(val)
        self.queue.append(val)

    def pop(self) -> None:
        if self.queue[-1] == self.min_queue[-1]:
            self.min_queue.pop()
        self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]
        
    def getMin(self) -> int:
        return self.min_queue[-1]