class cacheNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None
        # self.prev = self.next = None
        

class LRUCache:

# Linked list version?

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Cache keys assigned to nodes...
        self.cache = {}
        self.left, self.right = cacheNode(0,0), cacheNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # First create LL helpers functions
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        self.right.prev = node

        node.next = self.right
        node.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # We need to re-insert into LL
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # I don't think we need to re-insert into cache, not ordered...
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if its in already remove to re-input
        if key in self.cache:
            self.remove(self.cache[key])
        # Put said node in cache then re-insert to LL
        self.cache[key] = cacheNode(key, value)
        self.insert(self.cache[key])

        # Check if cache is full, if it is we need to remove LEFT most node
        if len(self.cache) > self.capacity:
            lru = self.left.next
            # Remove the lru (left most LL) from LL
            self.remove(lru)
            # Delete from cache as well
            del self.cache[lru.key]
        
