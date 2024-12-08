class Node:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def back(self, steps: int):
        c = 0
        while self.current.prev and c < steps:
            self.current = self.current.prev
            c += 1
        return self.current.url

    def forward(self, steps: int):
        c = 0
        while self.current.next and c < steps:
            self.current = self.current.next
            c += 1
        return self.current.url

    def visit(self, url: str) -> None:
        nextnode = Node(url)
        self.current.next = nextnode
        nextnode.prev = self.current
        self.current = self.current.next
