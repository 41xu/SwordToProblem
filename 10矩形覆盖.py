# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number==0:
            return 0
        res=[i+1 for i in range(number)]
        for i in range(2,number):
            res[i]=res[i-1]+res[i-2]
        return res[-1]