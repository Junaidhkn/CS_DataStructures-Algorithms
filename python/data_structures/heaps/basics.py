# ------------------------ HEAP DATA STRUCTURE NOTES ------------------------

# A Heap is a complete binary tree-based data structure, commonly used to implement Priority Queues.

# Heap has two types:
# a) Max Heap - The parent node must always be greater than or equal to its child nodes.
#               Therefore, the maximum element is always at the root.
# b) Min Heap - The parent node must always be less than or equal to its child nodes.
#               Therefore, the minimum element is always at the root.

# ------------------------ HEAP INDEXING CONVENTIONS ------------------------

#### Convention when using an array starting from index 1:
# For a node at index = i:
#   - Left child     -> index = 2 * i
#   - Right child    -> index = 2 * i + 1
#   - Parent node    -> index = i // 2
# Example:
#   If i = 7, then parent = 7 // 2 = 3

#### Convention when using an array starting from index 0 (Python standard):
# For a node at index = i:
#   - Left child     -> index = 2 * i + 1
#   - Right child    -> index = 2 * i + 2
#   - Parent node    -> index = (i - 1) // 2
# Example:
#   If i = 7, then parent = (7 - 1) // 2 = 3

# ------------------------ INSERTION IN A HEAP ------------------------

# Step-by-step process:
# 1. Insert the new element at the bottom (i.e., the next available position, maintaining complete binary tree structure).
# 2. Compare the inserted element with its parent.
# 3. If the heap property is violated (i.e., in Max Heap: new > parent OR in Min Heap: new < parent),
#    swap the new element with its parent.
# 4. Repeat step 3 until the heap property is restored (called "heapify up" or "bubble up").

# Time Complexity of Insertion: O(log n)
# Because the height of the heap is log n, and the element may travel up to the root.

# ------------------------ DELETION IN A HEAP ------------------------

# Usually, deletion refers to removing the root element (max in Max Heap, min in Min Heap).

# Step-by-step process:
# 1. Replace the root with the last element in the heap.
# 2. Remove the last element (which is now moved to root).
# 3. Compare the new root with its children.
# 4. If the heap property is violated, swap it with the appropriate child:
#    - Max Heap: swap with the larger child
#    - Min Heap: swap with the smaller child
# 5. Repeat step 4 until the heap property is restored (called "heapify down" or "bubble down").

# Time Complexity of Deletion (Root): O(log n)
# Because the element may travel from root to leaf to restore heap structure.

# ------------------------ COMMON APPLICATIONS OF HEAP ------------------------

# 1. **Priority Queue**: Tasks with higher priority are served before tasks with lower priority.
#    (Heap is the most efficient way to implement a priority queue.)
# 2. **Heap Sort**: Sorting algorithm that builds a heap and repeatedly extracts max/min.
#    - Time Complexity: O(n log n)
# 3. **Graph Algorithms**:
#    - Dijkstra’s Shortest Path Algorithm (uses Min Heap to find minimum distance node).
#    - Prim’s Minimum Spanning Tree Algorithm.
# 4. **Scheduling Algorithms** in Operating Systems: For efficient task management.
# 5. **Median Maintenance** using two heaps: One Min Heap and one Max Heap.

# ------------------------ TIME COMPLEXITY SUMMARY ------------------------

# Operation        | Time Complexity
# ----------------|----------------
# Insertion        | O(log n)
# Deletion (root)  | O(log n)
# Get Max/Min      | O(1)
# Build Heap       | O(n)    <- Efficient method using "heapify" bottom-up

# ------------------------ HEAPIFY OPERATION ------------------------

# Heapify is a fundamental operation in heaps that restores the heap property.

# There are two types of heapify:
# 1. **Heapify Up** (a.k.a. bubble up / sift up):
#    - Used after insertion.
#    - Starts from the inserted node (bottom) and moves up toward the root,
#      swapping elements if the heap property is violated.
#    - Used in insert operations.

# 2. **Heapify Down** (a.k.a. bubble down / sift down):
#    - Used after deletion (usually of the root).
#    - Starts from the root and moves downward,
#      swapping with the appropriate child (larger in Max Heap, smaller in Min Heap)
#      until the heap property is restored.
#    - Used in delete and build_heap operations.

# Example (Max Heapify Down from index i):
# def max_heapify(arr, i, n):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         max_heapify(arr, largest, n)

# Time Complexity:
# - Heapify Up: O(log n)
# - Heapify Down: O(log n)

# ------------------------ PRIORITY QUEUE USING HEAP ------------------------

# A Priority Queue is a special type of queue in which elements are served
# based on their priority (not just insertion order).

# High priority elements are dequeued before low priority ones.

# Python uses a **Min Heap** to implement a Priority Queue via the `heapq` module.

# The `heapq` module:
# - Built-in module in Python
# - Implements a min-heap (lowest value has the highest priority)
# - Can be used to build priority queues efficiently

# Example usage:
# import heapq
# pq = []
# heapq.heappush(pq, 10)
# heapq.heappush(pq, 1)
# heapq.heappush(pq, 5)
# print(heapq.heappop(pq))  # Output: 1 (smallest/highest priority)

# For a Max Heap using `heapq`, invert the values:
# heapq.heappush(pq, -value)
# heapq.heappop(pq) * -1

# For tuples (priority, task):
# heapq.heappush(pq, (priority, "task_name"))

# ------------------------ PRIORITY QUEUE APPLICATIONS ------------------------

# Applications of Priority Queue:
# - Task Scheduling (shortest job first, earliest deadline first)
# - Dijkstra’s and A* pathfinding algorithms
# - Huffman Coding (compression)
# - Load Balancing Systems (process with the highest priority gets executed first)
# - Event-driven simulation systems

# ------------------------ HEAP VS PRIORITY QUEUE ------------------------

# Heap:
# - A complete binary tree used to represent a priority queue.
# - Provides the structure and rules (Min or Max) for efficient operations.

# Priority Queue:
# - A use-case or application built on top of a heap.
# - Ensures that higher-priority elements are served before lower-priority ones.

# In short: Heap is the **implementation**, Priority Queue is the **concept**.




# -------------------------------------------------------------------------

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self,index):
        return 2 * index + 1

    def _right_child(self,index):
        return 2 * index + 2

    def _parent(self,index):
        return (index - 1) // 2

    def _swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]

    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current,self._parent(current))
            current = self._parent(current)

    def print_tree(self):
        def _print_tree(index, prefix="", is_left=True):
            if index >= len(self.heap):
                return

            right = self._right_child(index)
            left = self._left_child(index)

            # First print right child (visually top branch)
            if right < len(self.heap):
                _print_tree(right, prefix + ("│   " if is_left else "    "), False)

            # Then print current node
            print(prefix + ("└── " if is_left else "┌── ") + str(self.heap[index]))

            # Then print left child (visually bottom branch)
            if left < len(self.heap):
                _print_tree(left, prefix + ("    " if is_left else "│   "), True)

        _print_tree(0)

myHeap = MaxHeap()
myHeap.insert(99)
myHeap.insert(72)
myHeap.insert(61)
myHeap.insert(58)
myHeap.insert(99)
myHeap.insert(75)
myHeap.insert(47)
myHeap.insert(147)


myHeap.print_tree()

