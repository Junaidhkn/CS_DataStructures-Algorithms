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




