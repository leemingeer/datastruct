#!/usr/bin/env python

COUNT = 3
used = [0] * COUNT
result = [0] * COUNT 

def dfs(count):
    if count == 3:
        print result

    for i in range(3):
        if used[i] == 0:
            used[i] = 1
            result[count] = i + 1
            dfs(count + 1)
            used[i] = 0

dfs(0)