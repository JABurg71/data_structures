// ============================================
// 1. Stack (LIFO) using Array
// ============================================
class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  pop() {
    return this.items.pop();
  }

  peek() {
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }
}

// ============================================
// 2. Queue (FIFO) using Array
// ============================================
class Queue {
  constructor() {
    this.items = [];
  }

  enqueue(item) {
    this.items.push(item);
  }

  dequeue() {
    return this.items.shift();
  }

  isEmpty() {
    return this.items.length === 0;
  }
}

// ============================================
// 3. Binary Tree using Class
// ============================================
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// ============================================
// 4. Graph using Adjacency List
// ============================================
class Graph {
  constructor() {
    this.adjList = new Map();
  }

  addNode(node) {
    if (!this.adjList.has(node)) {
      this.adjList.set(node, []);
    }
  }

  addEdge(src, dst) {
    this.addNode(src);
    this.addNode(dst);
    this.adjList.get(src).push(dst);
  }

  neighbors(node) {
    return this.adjList.get(node) || [];
  }
}

// ============================================
// 5. Min Heap using array (manual implementation)
// ============================================
class MinHeap {
  constructor() {
    this.heap = [];
  }

  insert(val) {
    this.heap.push(val);
    this._bubbleUp(this.heap.length - 1);
  }

  extractMin() {
    if (this.heap.length < 2) return this.heap.pop();
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._sinkDown(0);
    return min;
  }

  peekMin() {
    return this.heap[0];
  }

  _bubbleUp(index) {
    let parent = Math.floor((index - 1) / 2);
    while (index > 0 && this.heap[index] < this.heap[parent]) {
      [this.heap[index], this.heap[parent]] = [this.heap[parent], this.heap[index]];
      index = parent;
      parent = Math.floor((index - 1) / 2);
    }
  }

  _sinkDown(index) {
    const length = this.heap.length;
    while (true) {
      let left = 2 * index + 1;
      let right = 2 * index + 2;
      let smallest = index;

      if (left < length && this.heap[left] < this.heap[smallest]) smallest = left;
      if (right < length && this.heap[right] < this.heap[smallest]) smallest = right;

      if (smallest === index) break;

      [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
      index = smallest;
    }
  }
}

// ============================================
// Demo Usage
// ============================================
console.log("=== Stack ===");
const stack = new Stack();
stack.push(10);
stack.push(20);
console.log("Pop:", stack.pop());  // 20

console.log("\n=== Queue ===");
const queue = new Queue();
queue.enqueue("A");
queue.enqueue("B");
console.log("Dequeue:", queue.dequeue());  // A

console.log("\n=== Binary Tree ===");
const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
console.log("Root:", root.value);
console.log("Left:", root.left.value);

console.log("\n=== Graph ===");
const graph = new Graph();
graph.addEdge("A", "B");
graph.addEdge("A", "C");
graph.addEdge("B", "D");
console.log("Neighbors of A:", graph.neighbors("A"));  // ['B', 'C']

console.log("\n=== Min Heap ===");
const heap = new MinHeap();
heap.insert(5);
heap.insert(1);
heap.insert(3);
console.log("Extract Min:", heap.extractMin());  // 1
console.log("Next Min:", heap.peekMin());        // 3

