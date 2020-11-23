#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (43.41%)
# Likes:    2789
# Dislikes: 188
# Total Accepted:    496K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def isBalanced(self, root: TreeNode) -> bool:
    
        # recursive
        # def depth(root:TreeNode):
        #     if not root:
        #         return 0
        #     return max(depth(root.right),depth(root.left))+1

        # if not root:
        #     return True
        # leftD = depth(root.left)
        # rightD = depth(root.right)
        # return abs(leftD - rightD)<=1 and self.isBalanced(root.right) and self.isBalanced(root.left)

        def dfs(root:TreeNode):
            if not root:
                return 0
            leftRes = dfs(root.left)
            if leftRes==-1:
                return -1
            rightRes = dfs(root.right)
            if rightRes==-1:
                return -1
            if abs(leftRes - rightRes) > 1:
                return -1
            return max(leftRes, rightRes) + 1

        # dfs
        return dfs(root) != -1
        
# @lc code=end

