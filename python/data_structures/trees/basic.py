class Node:
    def __init__(self,value):
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
        #     else: return True
        return False


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
myTree.insert(100)

myTree.print_tree()




print('Root of the BST is:',myTree.root.value)
# print(myTree.contains(242))

# print('Printing all nodes :')