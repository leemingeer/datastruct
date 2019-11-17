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