#!/usr/bin/env python
import collections

class LRUCache(object):

    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v # set key sa the newest one
        return v

    def put(self, key, value):
        if key in self.dic:
        # first delete key and then set key as the newest one
            self.dic.pop(key)
        else:
            if self.remain > 0:
                # no need delete, just set key sa the newest one
                self.remain -= 1
            else: # self.dic is full, delete oldest one(first one) and set key as the newest one
                self.dic.popitem(last=False)
        self.dic[key] = value

if __name__ == '__main__':
    lrucache = LRUCache(5)
    lrucache.put('z', 1)
    lrucache.put('y', 2)
    lrucache.put('x', 3)
    print 'origin:', lrucache.dic
    print lrucache.get('y')
    print 'after get y', lrucache.dic
    lrucache.put('m', 4)
    lrucache.put('n', 5)
    print 'full now:', lrucache.dic
    lrucache.put('p', 6)
    print 'after full:', lrucache.dic