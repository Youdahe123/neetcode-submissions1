class Node:
    def __init__(self,key,val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0) # LRUCache
        self.right = Node(0,0) #MRUCache
        self.left.next = self.right
        self.right.prev = self.left

        ## {1:Node Object}
        
    # Insert right before MRU
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right 
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


    # return the value corresponding with the key
    # mark it as used
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if self.capacity < len(self.cache):
            lru = self.left.next
            self.remove(lru) # removes it from our double linked list
            del self.cache[lru.key]
        
