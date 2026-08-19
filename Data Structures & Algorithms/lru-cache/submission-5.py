class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key: Object}
        self.right = Node(0,0) #MRU
        self.left = Node(0,0) #LRU
        self.right.prev = self.left
        self.left.next = self.right
    
    def remove(self,node): # remove it from where it is
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self,node): # Insert right before the MRU
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value) # updated
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
