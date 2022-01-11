# priority_queue.py

class BinaryTree:
    def __init__(self, capacity=0):
        self.elements = [None] * (capacity + 1)
        self.last = Position(self, 0)
        self.root = Position(self, 1)

    def empty(self):
        return self.last.pos == 0

    def swap_elements(self, t1, t2):
        self.elements[t1.pos], self.elements[t2.pos] = self.elements[t2.pos], self.elements[t1.pos]

    def add(self, x):
        if self.last.pos + 1 < len(self.elements):
            self.elements[self.last.pos + 1] = x
        else:
            self.elements.append(x)

        self.last.pos += 1

    def remove(self):
        item = self.elements[self.last.pos]
        self.elements[self.last.pos] = None
        self.last.pos -= 1
        return item


class Position:
    def __init__(self, tree, pos):
        self.tree = tree
        self.pos = pos
            
    def element(self):
        return self.tree.elements[self.pos]
    
    def left(self):
        return Position(self.tree, 2*self.pos)
    
    def right(self):
        return Position(self.tree, 2*self.pos + 1)
    
    def parent(self):
        return Position(self.tree, self.pos // 2)
    
    def sibling(self):
        if self == self.parent().left():
            return self.parent().right()
        else:
            return self.parent().left()

    def is_external(self):
        return 2 * self.pos > self.tree.last.pos

    def has_left(self):
        return 2 * self.pos <= self.tree.last.pos

    def has_right(self):
        return 2 * self.pos + 1 <= self.tree.last.pos

    def __gt__(self, other):
        return self.pos > other.pos

    def __lt__(self, other):
        return self.pos < other.pos
    
    def __eq__(self, other):
        return self.tree == other.tree and self.pos == other.pos


class Heap(BinaryTree):
    def __init__(self, capacity=0, compare_to=None):
        super().__init__(capacity)
        if compare_to:
            self.compare_to = compare_to
        else:
            self.compare_to = lambda x, y: x < y

    def less(self, t1, t2):
        return self.compare_to(self.elements[t1.pos], self.elements[t2.pos])

    def heapify_up(self, t):
        if t == self.root:
            return

        p = t.parent()

        if self.less(p, t):
            self.swap_elements(t, p)

        self.heapify_up(p)

    def heapify_down(self, t):
        if t.is_external():
            return
        
        if not t.has_left():
            max_child = t.right()
        elif not t.has_right():
            max_child = t.left()
        else:
            max_child = t.left() if self.less(t.right(), t.left()) else t.right()

        if self.less(t, max_child):
            self.swap_elements(t, max_child)

        self.heapify_down(max_child)


class MaxPriorityQueue:
    def __init__(self, capacity=0, compare_to=None):
        self.heap = Heap(capacity, compare_to)

    def empty(self):
        return self.heap.empty()

    def insert(self, key):
        self.heap.add(key)
        self.heap.heapify_up(self.heap.last)

    def max(self):
        return self.heap.root.element()

    def remove_max(self):
        self.heap.swap_elements(self.heap.root, self.heap.last)
        item = self.heap.remove()
        self.heap.heapify_down(self.heap.root)
        return item


class MinPriorityQueue:
    def __init__(self, capacity=0, compare_to=None):
        if compare_to:
            self.heap = Heap(capacity, lambda x, y: not compare_to(x, y))
        else:
            self.heap = Heap(capacity, lambda x, y: x > y)

    def empty(self):
        return self.heap.empty()

    def insert(self, key):
        self.heap.add(key)
        self.heap.heapify_up(self.heap.last)

    def min(self):
        return self.heap.root.element()

    def remove_min(self):
        self.heap.swap_elements(self.heap.root, self.heap.last)
        item = self.heap.remove()
        self.heap.heapify_down(self.heap.root)
        return item


def heapsort(t, key=None):
    if key:
        pq = PriorityQueue(compare_to = lambda x, y: key(x) > key(y))
    else:
        pq = PriorityQueue(compare_to = lambda x, y: x > y)

    while t:
        pq.insert(t.pop())

    while not pq.empty():
        t.append(pq.remove_max())
        
