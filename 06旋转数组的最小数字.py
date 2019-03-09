# -*- coding:utf-8 -*-
"""
这题我有点没看懂？然后随便写就完事了？可能C++写会更难？会不一样？想法不同？没懂这题啥意思2333
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray==[]:
            return 0
        cur=rotateArray[0]
        for i in range(len(rotateArray)):
            if cur>rotateArray[i]:
                cur=rotateArray[i]
        return cur
