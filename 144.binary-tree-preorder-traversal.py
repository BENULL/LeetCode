#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (55.44%)
# Likes:    1944
# Dislikes: 75
# Total Accepted:    573K
# Total Submissions: 1M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the preorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [1,2,3]
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
# Output: [1,2]
# 
# 
# Example 5:
# 
# 
# Input: root = [1,null,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
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

    # 99.07% 8.8%
    # def __init__(self):
    #     self.res = []

    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root: return
    #     self.res.append(root.val)
    #     self.preorderTraversal(root.left)
    #     self.preorderTraversal(root.right)
    #     return self.res

    # 8.16% 84.3%
    # def preorderTraversal(self, root: TreeNode) -> List[int]:      
    #     output = []
    #     self._helper(root, output)
    #     return output
    
    # def _helper(self, root, output):
    #     if root is None: return 
    #     output.append(root.val)
    #     self._helper(root.left, output)
    #     self._helper(root.right, output)

    # iterative 54.13% 84.3%
    def preorderTraversal(self, root: TreeNode) -> List[int]: 
        res = []
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return res
        
        



        
# @lc code=end

