#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (34.17%)
# Likes:    4900
# Dislikes: 362
# Total Accepted:    450.6K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any node sequence from some starting
# node to any node in the tree along the parent-child connections. The path
# must contain at least one node and does not need to go through the root.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3]
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 3 * 10^4].
# -1000 <= Node.val <= 1000
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
    # https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        def oneSideSum(root:TreeNode):
            nonlocal ans
            if not root: return 0
            left = max(0,oneSideSum(root.left))
            right = max(0,oneSideSum(root.right))
            ans = max(ans,right+left+root.val)
            return max(left,right)+root.val
        oneSideSum(root)
        return ans
        
# @lc code=end

