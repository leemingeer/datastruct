#!/usr/bin/env python

from __future__ import print_function
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

    def get_min_element_recursion(self, root):
        if root is None:
            return root
        if root.left == None:
            return root
        else:
            return self.get_min_element_recursion(root.left)
    
    def delete_node(self, root, value):
        if root is None:
            return None
        if value > root.data:
            root.right = self.delete_node(root.right, value)
        elif value < root.data:
            root.left = self.delete_node(root.left, value)
        else:
            #vaue == root.data
            #case1: current node data should be the minimal data of the node in the right subtree,
            #        and the minimal data node should be deleted 
            if root.left and root.right:
                temp_node = self.get_min_element_recursion(root.right)
                root.data = temp_node.data
                #the top root node in sub tree
                root.right = self.delete_node(root.right, temp_node.data)
            #case2: only one subtree exists, just return next node, the current node is skipped
            elif root.left is not None:
                # only right sub tree
                root = root.left
            elif root.right is not None:
                root = root.right
            #case3: leaf node ,root = None just deleted directly
            else:
                root = None
        #return current root node in sub tree which returns to the upper calls
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
    print(BST().get_tree_depth(root_node))
    print('search node')
    print(BST().search_val_recursion(root_node, 8).__dict__)
    print(BST().search_val_loop(root_node, 8).__dict__)
    print('get max element in bst')
    print(BST().get_max_element_recursion(root_node).__dict__)
    print(BST().get_max_element_loop(root_node).__dict__)

    print('delete node')
    print('before:')
    Tree().breadth_travel(root_node)
    new_root_node = BST().delete_node(root_node,5)
    print('\nafter:')
    Tree().breadth_travel(new_root_node)