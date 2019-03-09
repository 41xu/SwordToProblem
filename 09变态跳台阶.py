# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number==1:
            return 1
        if number==2:
            return 2
        res=[i+1 for i in range(number)]
        for i in range(2,number):
            res[i]=1+sum(res[:i])
        return res[-1]