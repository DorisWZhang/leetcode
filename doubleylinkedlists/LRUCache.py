class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # contains key and node
        # for our LRU we can use a doubly linked list, has pointer to start and end
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int: 
        if key not in self.cache:
            return -1
        # remove from current spot
        node = self.cache[key]
        self.remove(node)
        # move to end of the DLL
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        node = ListNode(key, value)
        self.cache[key] = node
        self.add(node)
        # if too many nodes, remove LRU
        if len(self.cache) > self.capacity:
            LRU_node = self.head.next
            self.remove(LRU_node)
            del self.cache[LRU_node.key]

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        previous_last = self.tail.prev
        previous_last.next = node
        node.prev = previous_last
        node.next = self.tail
        self.tail.prev = node
