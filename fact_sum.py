#!/usr/bin/env python

class Factorial(object):

    def __init__(self, n):
        self.n = n
        if not isinstance(self.n, int) and self.n < 1:
            print("input must be integers(>0)")
            return None

    def fact(self, n):
        if n == 1:
            return 1 
        return n*self.fact(n-1)

    def factorial_sum1(self):
        #M1    
        #fact1 complexity: n^2
        fact1 = [self.fact(i) for i in range(self.n + 1) if i >=1]
        return reduce(lambda x,y: x+y, fact1)

    def factorial_sum2(self):
        #M2
        #fact2 complexity: n
        fact2 = []
        for i in range(self.n + 1):
            if i == 0:
                continue
            tmp =  i * fact2[-1] if len(fact2) > 0 else 1
            fact2.append(tmp)
        return reduce(lambda x,y: x+y, fact2)

    def factorial_sum3(self):
        #M3
        fact3 = []
        sum = 0
        for i in range(self.n+1):
            if i == 0:
                continue
            fact_i =  i * fact3[-1] if len(fact3) > 0 else 1
            fact3.append(fact_i)  
            sum += fact_i
        return sum

# def fact(n):
#     if n == 1:
#         return 1 
#     return n*fact(n-1)

if __name__ == '__main__':
    f = Factorial(5)
    print(f.factorial_sum1())
    print(f.factorial_sum2())
    print(f.factorial_sum3())
