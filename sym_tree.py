#!/usr/bin/env python

from binarytree import Tree


def is_symmetric(root):
    if root is None:
        return True
    #divide into two sub tree
    return is_symm(root.left, root.right)

def is_symm(r1, r2):
    if r1 is None and r2 is None:
        return True
    if r1 is None or r2 is None:
        return False
    return r1.data == r2.data and is_symm(r1.left, r2.right) and is_symm(r1.right, r2.left)


if __name__ == '__main__':
    datas = [2,3,3,4,5,5,4,6,7,8,None,None,8,7,6]
    tree = Tree()
    for dt in datas:
        tree.add(dt)
    Tree().breadth_travel(tree.root)
    print "\nis this a symmetric tree?", is_symmetric(tree.root)

    
