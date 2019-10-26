#!/usr/bin/env python

class Node(object):
    def __init__(self,item):
        self.data = item
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self): 
        self.root = None

    def add(self, item):
        node = Node(item)
        # init root Node
        if self.root is None:
            self.root = node
            return 
        #begin from the root node when add items every time
        queue = [self.root]
    
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node 
                return 
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node 
                return 
            else:
                queue.append(cur_node.right)
    #width priority travel
    def breadth_travel(self, node):
        self.root = node 
        if self.root is None:
            return
       #self.root is the head node of tree
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.data)
            if cur_node.left is not None:
                queue.append(cur_node.left)  
            if cur_node.right is not None:
                queue.append(cur_node.right)  
    
    #deep proority travel includes: 1,2,3
    #the node is a variable since base node is changed during recursion
    def pre_order(self, node): 
        # there must be a recursion stop condition
        if node is None:
            return
        print(node.data) 
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node): 
        if node is None:
            return
        self.in_order(node.left)
        print(node.data) 
        self.in_order(node.right)

    def post_order(self, node): 
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data) 
                 
   
if __name__ == '__main__':
    tree = Tree() 
    tree.add(2)
    tree.add(6)
    tree.add(3)
    tree.add(9)
    tree.add(5)
    tree.add(8)
    tree.add(7)
    print 'print randomly'
    print tree.root.data 
    print tree.root.left.data 
    print tree.root.left.right.data 
    print tree.root.right.data 
    print tree.root.right.right.data 
    print 'breadth priority travel'
    tree.breadth_travel(tree.root)
    #tree is a tree
    #t.root is the first node(an object), that is base node 
    print('pre order:')
    tree.pre_order(tree.root)
    print('in order:')
    tree.in_order(tree.root)
    print('post order:')
    tree.post_order(tree.root)
