class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
 
    def insert(self,node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next



    #that get its going to basically update the hash 
    # if it reaches capacity we remove the LRU 
    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        
    # if we reach capacity 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
        
