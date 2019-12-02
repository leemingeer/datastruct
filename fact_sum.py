#!/usr/bin/env python

def factorial_sum(n):
    if not isinstance(n, int) and n < 1:
        print("input must be integers(>0)")
        return None
    #fact1 complexity: n^2
    fact1 = [fact(i) for i in range(n + 1) if i >=1]

    
    #fact2 complexity: n
    fact2 = []
    for i in range(n + 1):
        if i == 0:
            continue
        tmp =  i * fact2[-1] if len(fact2) > 0 else 1
        fact2.append(tmp)


    #return reduce(lambda x,y: x+y, fact1)
    return reduce(lambda x,y: x+y, fact2)

def fact(n):
    if n == 1:
        return 1 
    return n*fact(n-1)


if __name__ == '__main__':
    print(factorial_sum(5))
