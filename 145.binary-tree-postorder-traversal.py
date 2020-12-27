#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (54.63%)
# Likes:    2261
# Dislikes: 109
# Total Accepted:    438.8K
# Total Submissions: 772.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: root = [1,2]
# Output: [2,1]
# 
# 
# Example 5:
# 
# 
# Input: root = [1,null,2]
# Output: [2,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# 
# Follow up:
# 
# Recursive solution is trivial, could you do it iteratively?
# 
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
    # recursion
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     return [] if not root else self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]

    # iterative
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     res, stack = [],[]
    #     while stack or root:
    #         if root:
    #             stack.append((root,False))
    #             root = root.left
    #         else:
    #             root,visited = stack[-1]
    #             if visited:
    #                 stack.pop()
    #                 res.append(root.val)
    #                 root = None
    #             else:
    #                 stack[-1]= (root,True)
    #                 root = root.right
    #     return res

    # Post Order Traverse use per order reverse
    def postorderTraversal(self, root: TreeNode) -> List[int]: 
        res,stack = [],[]
        while stack or root:
            if root:
                res.insert(0,root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        return res
        
# @lc code=end

