# recursion
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        return self.is_two_tree_symmetric(root.left, root.right)

    def is_two_tree_symmetric(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val == t2.val 
        and self.is_two_tree_symmetric(t1.left, t2.right) 
        and self.is_two_tree_symmetric(t1.right, t2.left)

#iterator
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        queue = deque()
        queue.append((root, root))
        while queue:
            left, right = queue.popleft()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True