class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert Pseudo Code

    #         create new Node
    #         if root == None then root = new Node
    #         temp = self.root
    #         While loop
    #               if new Node == temp return False
    #               if < left else > right
    #               if None insert new Node else move to next

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right
            else:
                return False

    def contains(self, value):
        # No need to check for the root being none,as while loop has 'is not none as conditional statement'
        # if self.root is None:
        #     return False
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            elif value == current.value:
                return True
        return False

    # 📘 BFS visits nodes level-by-level, from top to bottom and left to right.
    #    It uses a queue (FIFO) to keep track of the next nodes to visit.

    # Example Tree:
    #         10
    #        /  \
    #       6    15
    #      / \     \
    #     3   8     20

    # BFS Traversal Order:
    # [10, 6, 15, 3, 8, 20]

    # 🧠 Algorithm:
    # 1. Start with root → enqueue it
    # 2. While queue not empty:
    #    - Dequeue node
    #    - Process node (e.g., add to result)
    #    - Enqueue its left and right children (if not None)

    # ✅ Optimal Implementation:
    # - Use `collections.deque` instead of list for queue
    #   as `pop(0)` in list is O(n), while `popleft()` in deque is O(1)

    # 🕒 Time Complexity: O(n) — visits each node once
    # 💾 Space Complexity: O(n) — stores all nodes in queue at a level

    def breath_first_search(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    # 📘 Preorder DFS visits the root node *before* its subtrees.

    # Example Tree:
    #         10
    #        /  \
    #       6    15
    #      / \     \
    #     3   8     20

    # Preorder Traversal Order:
    # [10, 6, 3, 8, 15, 20]

    # 🧠 Algorithm (recursive):
    # 1. Visit node
    # 2. Traverse left subtree (Preorder)
    # 3. Traverse right subtree (Preorder)

    # ✅ Optimization:
    # - Use recursion for simplicity, or a stack for iteration if recursion depth is a concern

    # 🕒 Time Complexity: O(n)
    # 💾 Space Complexity:
    # - O(h) for recursive (h = height of tree)
    # - O(n) worst-case for stack in skewed tree

    def depth_first_search_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    # 📘 Postorder DFS visits children before their parent (useful for cleanup/deletion).

    # Example Tree:
    #         10
    #        /  \
    #       6    15
    #      / \     \
    #     3   8     20

    # Postorder Traversal Order:
    # [3, 8, 6, 20, 15, 10]

    # 🧠 Algorithm (recursive):
    # 1. Traverse left subtree (Postorder)
    # 2. Traverse right subtree (Postorder)
    # 3. Visit node

    # ✅ Usage:
    # - Used in freeing memory or evaluating expression trees

    # ✅ Optimization:
    # - Use two stacks for iterative version (reverse of modified preorder)

    # 🕒 Time Complexity: O(n)
    # 💾 Space Complexity: O(h), or O(n) for iterative stack approach

    def depth_first_search_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    # 📘 Inorder DFS visits the left subtree, then root, then right subtree.

    # Example Tree:
    #         10
    #        /  \
    #       6    15
    #      / \     \
    #     3   8     20

    # Inorder Traversal Order:
    # [3, 6, 8, 10, 15, 20]

    # 🧠 Algorithm (recursive):
    # 1. Traverse left subtree (Inorder)
    # 2. Visit node
    # 3. Traverse right subtree (Inorder)

    # 🧮 Special Use: On a Binary Search Tree (BST), it gives values in **ascending sorted order**

    # ✅ Optimization:
    # - Morris Traversal (O(1) space, but modifies tree temporarily)
    # - Standard recursion or stack-based iterative solution

    # 🕒 Time Complexity: O(n)
    # 💾 Space Complexity: O(h), or O(1) with Morris Traversal

    def depth_first_search_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def print_tree(self):
        def _print_tree(node, prefix="", is_left=True):
            if node is not None:
                _print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
                print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
                _print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

        _print_tree(self.root)


myTree = BinarySearchTree()
myTree.insert(47)
myTree.insert(21)
myTree.insert(18)
myTree.insert(24)
myTree.insert(76)
myTree.insert(52)
myTree.insert(82)

myTree.print_tree()


print("Root of the BST is:", myTree.root.value)
# print(myTree.contains(242))

print("Printing Pre_Order DFS:")
print(myTree.depth_first_search_pre_order())
print("Printing Post_Order DFS:")
print(myTree.depth_first_search_post_order())
print("Printing in_Order DFS:")
print(myTree.depth_first_search_in_order())
