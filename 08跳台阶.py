# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==1:
            return 1
        if number==2:
            return 2
        res=[i+1 for i in range(number)]
        res[0]=1
        res[1]=2
        for x in range(2,number):
            res[x]=res[x-1]+res[x-2]
        return res[-1]