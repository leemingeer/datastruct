#!/usr/bin/env python
# LCA: least common ancestor

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LCASolution(object):
    def __init__(self):
        pass

    def get_lca(self, root, p, q):
        if root is None or root is p or root is q:
            return root
        
        left = self.get_lca(root.left, p, q)
        right = self.get_lca(root.right, p, q)

        if left is not None and right is not None:
            return root
        if left is None and right is not None:
            return right
        if left is not None and right is None:
            return left
        return None


if __name__ == '__main__':

    #generate a test tree by hand
    #the n1 node is alse a Tree
    n1 = Tree = Node(2) 
    n2 = n1.left = Node(3)
    n3 = n1.right = Node(4)
    n4 = n2.left = Node(5)
    n5 = n3.right = Node(6)
    n6 = n4.right = Node(7)
    n7 = n5.left = Node(8)
    n8 = n5.right = Node(9)
    n9 = n7.right = Node(10)

    LCA= LCASolution()

    print(LCA.get_lca(Tree, n9, n8).data)    
