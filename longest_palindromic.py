#!/usr/bin/env python


def is_palindrome(s):
    return True if s == s[::-1] else False


def is_palindrome2(s):
    if not s:
        return True
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True


def manacher_solution(preS):
    s = '#' + '#'.join(preS) + '#'
    l = len(s)
    RL = [0] * l
    maxRight = pos = maxLen = 0
    for i in range(l):
        #https://www.zhihu.com/question/37289584?sort=created
        if i < maxRight:
            #Core: i in the scope of maxright, it can be derived from current knowns
            RL[i] = min(RL[2*pos - i], maxRight-i)
        else:
            #need center expand
            RL[i] = 1
        #center expand, the two condition defines the borders
        while i - RL[i] >= 0 and i + RL[i] < l and s[i - RL[i]] == s[i + RL[i]]:
              RL[i] += 1
        #update maxright and pos
        if i + RL[i] - 1 > maxRight:
            maxRight = i + RL[i] - 1
            pos = i
    maxLen = max(RL)
    #find index in the list
    idx = RL.index(maxLen)
    sub = s[idx - maxLen + 1: idx + maxLen]
    return sub.replace('#', '')


if __name__ == '__main__':
    print is_palindrome('abd')
    print is_palindrome2('aba')
    print manacher_solution('abcddcbefe')