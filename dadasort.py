#!/usr/bin/env python
#coding: utf-8
import unittest

class MysortTest(unittest.TestCase):
    def test_sort_all_0(self):
        alist1 = [0] * 6
        ret = mysort(alist1)
        self.assertEqual(ret, alist1)

    def test_sort_half_0(self):
        alist1 = [0,1,0,1,1,1,1,0,0,1,0]
        ret = mysort(alist1)
        sorted_alist = alist1.sort()
        self.assertEqual(ret, alist1)

#list.sort() only list, modify the same id, return value is none
#sorted(iterable), all iterable items, return a new sorted object with different id
#
#data = [
#    {'name':'li','age':40},
#    {'name':'zhang','age':30}
#    ] 
#sorted_data = sorted(data,key=lambda i:i['age'])
#print data, sorted_data
 


def mysort(alist):
    i = 0
    j = len(alist) - 1
    num1 = 0
    num0 = 1
    while i <= j:
        if alist[i] == 1:
            num1 = 1
        else:
            num1 = 0
            i += 1
        if alist[j] == 0:
            num0 = 0
        else:
            num0 = 1
            j -= 1
        if num1 == 1 and num0 == 0:
            alist[i], alist[j] = num0, num1
            i += 1
            j -= 1
    return alist

def mysort2(A):
    i = 0
    j = len(A) - 1
    print A
    #while i <= j:
    while True:
        while A[i] != 1 and i <= j:
            i += 1
        while A[j] != 0 and i <= j:
            j -= 1
        if j >= i:
            A[i], A[j] = A[j], A[i]
        else:
            break
    print A
        


    

if __name__ == '__main__':
    #python dadasort.py
    #unittest.main()
    alist1 = [0,1,0,1,1,1,1,0,0,1]
    mysort2(alist1)

    #python -m unittest 编译该层目录下继承unittest模块的所有py文件

    #python -m unittest dadasort.MysortTest.test_sort_half_0 只执行py文件中名为xxx的unittest类的xxx函数


    # python -m <mod> run library module as a script (terminates option list)
    # python -m SimpleHTTPServer    #python2 run http erver
    # python -m http.server    #python3 run http erver
    #4、将模块当做脚本去启动有什么用？

    #python xxx.py
    #python -m xxx.py

#这是两种加载py文件的方式:
#1叫做直接运行
#2相当于import,叫做当做模块来启动