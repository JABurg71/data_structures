# Composite Data Structures Using Lists and Dicts

# --------------------------------------
# 1. Stack (LIFO) using List
# --------------------------------------
import heapq


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return not self.items


# --------------------------------------
# 2. Queue (FIFO) using List
# --------------------------------------
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def is_empty(self):
        return not self.items


# --------------------------------------
# 3. Binary Tree using Class
# --------------------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# --------------------------------------
# 4. Graph using Adjacency List
# --------------------------------------
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        self.adj_list[node] = []

    def add_edge(self, src, dst):
        if src not in self.adj_list:
            self.add_node(src)
        if dst not in self.adj_list:
            self.add_node(dst)
        self.adj_list[src].append(dst)

    def neighbors(self, node):
        return self.adj_list.get(node, [])


# --------------------------------------
# 5. Min-Heap using heapq
# --------------------------------------


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else None

    def peek_min(self):
        return self.heap[0] if self.heap else None


# --------------------------------------
# Demo Usage
# --------------------------------------
if __name__ == "__main__":
    print("=== Stack ===")
    s = Stack()
    s.push(10)
    s.push(20)
    print("Pop:", s.pop())  # 20

    print("\n=== Queue ===")
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    print("Dequeue:", q.dequeue())  # A

    print("\n=== Binary Tree ===")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("Root:", root.value)
    print("Left child:", root.left.value)

    print("\n=== Graph ===")
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    print("Neighbors of A:", g.neighbors("A"))  # ['B', 'C']

    print("\n=== Min Heap ===")
    h = MinHeap()
    h.insert(5)
    h.insert(1)
    h.insert(3)
    print("Min value:", h.extract_min())  # 1
