class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class RecursiveBinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert(self,current_node,value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__insert(current_node.left,value)
        if value > current_node.value:
            current_node.right = self.__insert(current_node.right,value)
        return current_node



    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__insert(self.root,value)

    def r__contains(self, current_node,value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.r__contains(current_node.left,value)
        return self.r__contains(current_node.right,value)

    def contains(self, value):
        return self.r__contains(self.root,value)


    def print_tree(self):
        def _print_tree(node, prefix="", is_left=True):
            if node is not None:
                _print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
                print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
                _print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

        _print_tree(self.root)



myTree = RecursiveBinarySearchTree()
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
print(myTree.contains(52))


