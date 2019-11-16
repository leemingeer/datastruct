#!/usr/bin/env python
from binarytree import Tree
class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

#find the root node recursively
def construct_tree(pre_order, mid_order):
    if len(pre_order) == 0 or len(mid_order) == 0:
        #can't construct this tree
        return None
    root = pre_order[0]
    i = mid_order.index(root)
    left = construct_tree(pre_order[1: i + 1], mid_order[:i])
    right = construct_tree(pre_order[i + 1 :] , mid_order[i + 1:])
    return Node(root, left, right)

if __name__ == "__main__":
    pre_order = [1,2,4,7,3,5,6,8]
    mid_order = [4,7,2,1,5,3,8,6]
    root = construct_tree(pre_order, mid_order)
    print('breadth travel')
    Tree().breadth_travel(root)
    print('post order')
    Tree().post_order(root)

    print('test disply')
    n1 = root
    n2 = root.left
    n3 = root.right
    n4 = n2.left
    n5 = n2.right
    n6 = n3.left
    n7 = n3.right
    for n in [n1,n2,n3,n4,n5,n6,n7]:
        if n == None:
            print 'null'
        else:
            print n.data
