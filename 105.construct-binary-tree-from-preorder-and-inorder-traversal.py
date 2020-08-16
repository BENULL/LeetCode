#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (48.35%)
# Likes:    3634
# Dislikes: 98
# Total Accepted:    376.7K
# Total Submissions: 770.4K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    # recursive
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        ind  = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder,inorder[:ind])
        root.right = self.buildTree(preorder,inorder[ind+1:])
        return root

        
# @lc code=end

