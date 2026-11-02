class Node:
    def __init__(self,key,val):
        self.key, self.val = key,val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.maxlen = capacity
        self.dl, self.dr = Node(0,0),Node(0,0)
        self.dl.next, self.dr.prev = self.dr, self.dl

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.dr.prev, self.dr
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # removal of the node
        self.remove(node)
        # insert to the right 
        self.insert(node)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.maxlen:
            lruNode = self.dl.next
            self.remove(lruNode)
            del self.cache[lruNode.key]
        
        
