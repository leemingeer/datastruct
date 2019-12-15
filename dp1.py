#!/usr/bin/env python
import logging
class Steps(object):
    
    def __init__(self, m , n):
        self.x = m
        self.y = n

# x * y matrics, (0,0) -> (x, y)
def roads_num_recur(x, y):
    
    if x < 0 or y < 0:
        logging.warning("x y must be > 0")
        return None
    if x == 0:
        return 1
    if y == 0:
        return 1
    return roads_num_recur(x, y-1) + roads_num_recur(x-1, y)

def roads_num_recur_opt(x, y):
    cache = {}
    if x == 0 and y == 0:
        logging.warning("x y must be > 0")
        return None
    if x == 0:
        return 1
    if y == 0:
        return 1
    # if (x,y) in cache:
    #     return cache[(x,y)
    # else:
    #     return counts2(x-1, y) + counts2(x, y-1)
    #     #steps = counts2(x-1, y) + counts2(x, y-1)
    #     #cache[(x,y)] = steps
    #     #return steps

def roads_num_dp(m, n):
    dp = []
    # need (m +1) x (n + 1) 2-D array
    x = m + 1
    y = n + 1
    for i in range(y):
        dp.append([0]*x)
    for i in range(x):
        dp[0][i] = 1

    for i in range(y):
        dp[i][0] = 1
    for i in range(1, x):
        for j in range(1, y):
            dp[j][i] = dp[j-1][i] + dp[j][i-1]
            print dp
    return dp[y-1][x-1]


if __name__ == '__main__':
    print roads_num_recur(3,4)
    print roads_num_dp(3,4)