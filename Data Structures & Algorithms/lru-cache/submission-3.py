class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key=key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # We add the element first
        self.cache.update({key: value})
        # We also need to move the k/v to end in case we just updating
        self.cache.move_to_end(key=key)
        # Then we check if capacity is overfilled.
        if len(self.cache) > self.capacity:
            # remove first element
            # last = False removes first, True removes last....
            self.cache.popitem(last=False)