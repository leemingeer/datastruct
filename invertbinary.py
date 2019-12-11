#!/usr/bin/env python
#encoding=utf-8
#    4
#  /  \
# 2    7
# /\   /\
#1  3 6  9 

#    4
#  /  \
# 7    2
# /\   /\
#9  6 3  1 

#翻转之后根节点仍然是 4 ，左子树和右子树交换。与此同时，以左子树和右子树为根节点的二叉树都会跟过来
from binarytree import Tree
#recursion

def invertbinarytree_recur(node):
    root = node
    if root is None:
        return
    root.right, root.left = root.left, root.right
    invertbinarytree_recur(root.left)
    invertbinarytree_recur(root.right)

#non recursion
def invertbinarytree_norecur(node):
    root = node

    if root is None:
        return
    queue = [root]

    while queue:
        curNode = queue.pop(0)
        # print("\n")
        # print(curNode.data, curNode.left.data, curNode.right.data)
        curNode.right, curNode.left = curNode.left, curNode.right
        if curNode.left is not None:
            queue.append(curNode.left)
        if curNode.right is not None:
            queue.append(curNode.right)


if __name__ == '__main__':
    tree = Tree()
    tree.add(4)
    tree.add(2)
    tree.add(7)
    tree.add(1)
    tree.add(3)
    tree.add(6)
    tree.add(9)

    Tree().breadth_travel(tree.root)
    #invertbinarytree_recur(tree.root)
    #print("revert with recursion:\n")
    #Tree().breadth_travel(tree.root)
    invertbinarytree_norecur(tree.root)
    print("revert with loop:\n")
    Tree().breadth_travel(tree.root)