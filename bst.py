#!/usr/bin/env python
from binarytree import Tree
class Node(object):
    def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def create(self, root, data):
        #return condition
        if root is None:
            root = Node(data)
        elif data < root.data:
            root.left = self.create(root.left, data)
        elif data > root.data:
            root.right = self.create(root.right, data)
        return root
    
    def get_tree_depth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.get_tree_depth(root.left), self.get_tree_depth(root.right))

    def search_val_recursion(self, root, value):
        if root is None or root.data == value:
            return root
        if value > root.data:
            return self.search_val_recursion(root.right, value)
        if value < root.data: 
            return self.search_val_recursion(root.left, value)

    def search_val_loop(self, root, value):
        while root != None and root.data != value:
            if value > root.data:
                root = root.right
            if value < root.data:
                root = root.left
        return root


    def get_max_element_recursion(self, root):
        if root is None:
            return root
        if root.right == None:
            return root
        else:
            return self.get_max_element_recursion(root.right)

    def get_max_element_loop(self, root):
        if root is None:
            return root
        while root.right is not None:
            root = root.right
        return root

    

if __name__ == "__main__":
    datas = [5,3,8,2,9,2,1,4]
    root_node = Node(3)
    for dt in datas:
        BST().create(root_node, dt)
    print('pre_order')
    Tree().pre_order(root_node)
    print('in order')
    Tree().in_order(root_node)
    print('breadth_travel')
    Tree().breadth_travel(root_node)
    print('tree depth')
    print BST().get_tree_depth(root_node)
    print('search node')
    print BST().search_val_recursion(root_node, 8).__dict__
    print BST().search_val_loop(root_node, 8).__dict__
    print('get max element in bst')
    print BST().get_max_element_recursion(root_node).__dict__
    print BST().get_max_element_loop(root_node).__dict__