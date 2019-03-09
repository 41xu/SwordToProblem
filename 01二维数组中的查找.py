# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, arr):
        # write code here
        i=0
        j=len(arr[0])-1
        while 0<=i<=len(arr)-1 and 0<=j<=len(arr[0])-1:
            if target<arr[i][j]:
                j-=1
            elif target>arr[i][j]:
                i+=1
            elif target==arr[i][j]:
                return True
        return False

        