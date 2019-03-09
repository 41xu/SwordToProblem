# -*- coding:utf-8 -*-
"""
这题写的我好别扭...明明一个list就能当栈用能当队列用...可能C++写起来会更舒服一些？
"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, node):
        # write code here
        self.stack1.append(node)
        
    def pop(self):
        # return xx
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return 
        elif len(self.stack2) == 0:
            while len(self.stack1) > 1:
                self.stack2.append(self.stack1.pop())
            return self.stack1.pop()
        return self.stack2.pop()
