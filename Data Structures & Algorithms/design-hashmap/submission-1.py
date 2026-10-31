class MyHashMap:

    def __init__(self):
        self.capacity = 997
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v
        
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)