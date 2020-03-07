#/usr/bin/env python
#coding=utf-8
from collections import OrderedDict

class LastUpdatedOrderedDict(object):

    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.remain = capacity

    def __setitem__(self, key, value):
        if key in self.__dict__:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value

l = LastUpdatedOrderedDict(4)
l['a'] = 2
l['b'] = 3
l['c'] = 4
print l.__dict__
l['d'] = 5
l['e'] = 6
print l.__dict__

# class Tag:
#     def __init__(self):
#         self.change={'python':'This is python',
#                      'php':'PHP is a good language'}
 
#     def __getitem__(self, item):
#         print('调用getitem')
#         return self.change[item]
 
#     def __setitem__(self, key, value):
#         print('调用setitem')
#         self.change[key]=value
 
# a=Tag()
# print(a['php'])
# a['php']='PHP is not a good language'
# print(a['php'])

# print a.__dict__