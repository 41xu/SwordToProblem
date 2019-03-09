# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        news=""
        for i in range(len(s)):
            if s[i]==" ":
                news+="%20"
            else:
                news+=s[i]
        return news