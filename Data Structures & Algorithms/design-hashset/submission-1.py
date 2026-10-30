class MyHashSet:

    def __init__(self):
        self.capacity = 997
        self.buckets = [[] for _ in range(self.capacity)]
    
    def _hash(self, key: int) -> int:
        return key % self.capacity

    def add(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)