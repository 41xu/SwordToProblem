# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        fib=[i for i in range(n+1)]
        for i in range(2,n+1):
            fib[i]=fib[i-1]+fib[i-2]
        return fib[-1]
        