#!/usr/bin/env python

class Solution(object):

    def __init__(self):
        self.sum = dict()

    def climbstairs_recursion(self, n):
        if n == 1:
            return 1
        if n == 2: 
            return 2
        return self.climbstairs_recursion(n -1) + self.climbstairs_recursion(n -2)

    def climbstairs_iteration(self, n):
        if n == 1:
            return 1
        if n == 2: 
            return 2
        a = 1
        b = 2
        i = 2
        # a = climbstairs(n -2)
        # b = climbstairs(n -1)
        # iter from the 1,2 => n
        while(i < n):
            b = a + b
            a =  b - a
            i += 1
        return b
    #traverse the cache
    #if not found ,calculate it with derivative previous values
    def climbstairs_optimize1(self, n):
        if n == 1:
            self.sum[1] = 1
            return 1
        if n == 2:
            self.sum[2] = 2
            return 2
        if n in self.sum:
            return self.sum[n]
        else:
            self.sum[n] = self.climbstairs_optimize1(n - 1) + self.climbstairs_optimize1(n - 2)
            return self.sum[n]

    def climbstairs_optimize2(self, n):
        if n == 1:
            self.sum[1] = 1
            return 1
        if n == 2:
            self.sum[2] = 2
            return 2
        if n in self.sum:
            return self.sum[n]
        else:
            self.sum[n] = self.sum[n - 1] + self.sum[n - 2]
            return self.sum[n]

if __name__ == '__main__':
    s = Solution()
    print(s.climbstairs_recursion(10))
    print(s.climbstairs_iteration(10))
    print(s.climbstairs_optimize1(10))
    print(s.climbstairs_optimize2(10))


