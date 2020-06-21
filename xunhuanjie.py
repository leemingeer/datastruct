#!/usr/bin/env python

class Solution(object):

    def get_loopnode(self, s):
        if not s:
            return s
        res = []
        for i, c in enumerate(s[0:-2]):
            k = 0
            end = None
            while i + 1 + k < len(s):
                if s[i + 1 + k] == c:
                    end = i + 1 + k
                    break
                k += 1
            #print 'begin', c
            #print 'end', s[end]
            if not end and i != len(s) - 3:
                print i
                continue
            print i
            if not end and i == len(s) - 3:
                res = s
                return res
            candidate = s[i: end]
            print 'candidate', candidate
            for j in range(len(candidate)):
                if end + j + 1 >= len(s) - 1 or candidate[j+1] != s[end + j + 1]:
                    break
            if j > 0:
                res.append(candidate[:j+2])
        return res
test1 = 'abcdeabcde'
solution = Solution()
print 'result', solution.get_loopnode(test1)


        