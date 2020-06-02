
#recursion
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了
        return root

# iterator
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        queue = [root]
        while queue:
            cur_node = queue.pop()
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
        return root