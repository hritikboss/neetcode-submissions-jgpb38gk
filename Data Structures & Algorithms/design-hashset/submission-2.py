class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        b = key % self.size
        if key not in self.buckets[b]:
            self.buckets[b].append(key)

    def remove(self, key: int) -> None:
        b = key % self.size
        if key in self.buckets[b]:
            self.buckets[b].remove(key)

    def contains(self, key: int) -> bool:
        b = key % self.size
        return key in self.buckets[b]