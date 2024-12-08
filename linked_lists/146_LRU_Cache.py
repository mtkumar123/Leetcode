class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    
    def __repr__(self,):
        prev = self.prev.val if self.prev else None
        nex = self.next.val if self.next else None
        return "{0}--{1}--{2}".format(prev, self.val, nex)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.last_node = None
        self.first_node = None

    def insert_node(self, node):
        if self.last_node:
            self.last_node.next = node
            node.prev = self.last_node
        else:
            self.first_node = node
        node.next = None
        self.last_node = node
        return

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        elif prev_node:
            prev_node.next = None
            self.last_node = prev_node
        elif next_node:
            next_node.prev = None
            self.first_node = next_node
        else:
            self.first_node = None
            self.last_node = None
        return

    

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.insert_node(node)
            return node.val
        return -1

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove_node(self.cache[key])
        elif len(self.cache) >= self.capacity:
            del self.cache[self.first_node.key]
            self.remove_node(self.first_node)
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# x = LRUCache(1)
# x.get(6)
# x.get(8)
# x.put(12,1)
# x.get(2)
# x.put(15,11)
# x.put(5,2)
# x.put(1,15)
# x.put(4,2)
# x.get()
# x.put(3,3)
