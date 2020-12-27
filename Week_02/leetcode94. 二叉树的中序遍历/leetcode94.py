#!/usr/bin/env python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# solution1 recursion
class Solution:
    def inorderTraversal(self,root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    def helper(self,root,res):
        self.helper(root.left) #前序遍历、后序遍历的实现只需要将这三者调换位置。前序遍历：顶点-左-右；
        res.append(root.val)   # 后序遍历：左-右-顶点；中序遍历：左-顶点-右
        self.helper(root.right)