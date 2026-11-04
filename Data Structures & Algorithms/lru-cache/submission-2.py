class CacheNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.cache = dict()
        self.head = None
        self.tail = None

    def unlink(self, node: CacheNode) -> None:
        pred, succ = node.prev, node.next

        if pred:
            pred.next = succ
        else:
            self.head = succ

        if succ:
            succ.prev = pred
        else:
            self.tail = pred

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        if node == self.head:
            return node.val

        self.unlink(node)

        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            if node != self.head:
                self.unlink(node)
                node.next = self.head
                self.head.prev = node
                self.head = node

        else:
            node = CacheNode(key, value)
            node.next = self.head

            if self.head:
                self.head.prev = node
            self.head = node

            if self.tail is None:
                self.tail = node

            self.cache[key] = node
            self.size += 1

            if self.size > self.cap:
                lru = self.tail
                self.unlink(lru)
                del self.cache[lru.key]
                self.size -= 1