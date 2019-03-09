# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        root=pre[0]
        rootindex=tin.index(root)
        
        leftnum=rootindex
        rightnum=len(tin)-leftnum-1
        
        left_pre=pre[1:leftnum+1]
        right_pre=pre[leftnum+1:]
        left_tin=tin[:rootindex]
        right_tin=tin[rootindex+1:]
        curroot=TreeNode(root)
        #if left_pre!=[]:
            #curroot.left=TreeNode(left_pre[0])
        #if right_pre!=[]:
            #curroot.right=TreeNode(right_pre[0])
        if left_pre!=[]:
            curroot.left=self.reConstructBinaryTree(left_pre,left_tin)
        if right_pre!=[]:
            curroot.right=self.reConstructBinaryTree(right_pre,right_tin)
        return curroot
    