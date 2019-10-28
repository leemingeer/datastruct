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
        #None: p, q both not found under root node, In this case, all subnode is
        #traversed
        #find p or q, because lca can't be under subroot node
        #no need to find under root node again, just return to uppper node
        if root is None or root is p or root is q:
            return root
        
        
        left = self.get_lca(root.left, p, q)
        right = self.get_lca(root.right, p, q)
        #root node and find in its subtree recursively
        #return the find result to the upper call
        #if left and right are all not None then the root of this
        # level call is lca point
        if left is not None and right is not None:
            return root
        #only find in its right subtree, return to upper call
        #because left not here, so lca is in upper level node
        if left is None and right is not None:
            return right
        #the same
        if left is not None and right is None:
            return left
        #not found in this root node, return to None to upper node
        return None


if __name__ == '__main__':

    #generate a test tree by hand
    #the n1 node is also a Tree
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
