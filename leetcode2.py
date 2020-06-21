# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from functools import reduce
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start0 = ListNode(0)
        node = start0 
        list1 = []
        list2 = []
        while True:
            list1.append(l1.val)
            if l1.next is not None:
                l1 = l1.next
            else:
                break

        while True:
            list2.append(l2.val)
            if l2.next is not None:
                l2 = l2.next
            else:
                break
        num1 = self.list2integer(list1[::-1])
        num2 = self.list2integer(list2[::-1])
        res =  self.integer2list(num1 + num2, node)
        return start0.next
    
    def list2integer(self, list1):
        res = 0
        for i in range(len(list1)):
            res = res * 10  + list1[i]
        return res

    def list2integer2(self, list1):
        return reduce(lambda x, y: x * 10 + y, list1)

    def integer2list(self, num, node):
        while True:
            next_node = ListNode(num % 10)
            node.next = next_node
            node = node.next
            num = num // 10
            if num == 0:
                break

#
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        node = start
        carry = 0
        while (l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + carry
            carry = s // 10
            val = s % 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            node.next = ListNode(val)
            node = node.next
        if carry:
            node.next = ListNode(1)
        
        return start.next


s = Solution()
l1 = [2, 4 ,3]
l2 = [5, 6, 4]
#print s.addTwoNumbers(l1, l2)
print s.list2integer2(l2)