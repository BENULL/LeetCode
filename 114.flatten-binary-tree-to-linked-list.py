#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (48.84%)
# Likes:    3007
# Dislikes: 342
# Total Accepted:    358.9K
# Total Submissions: 726.6K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    """
    We can solve this problem recursively, suppose we already flattened the left part of the root, 
    then we need set it as the right child of the root (the previous right child of the root should be preserved first by using a temp variable before this operation), 
    after that, the previous right child is connected to the right most of the flattened left child. 
    Don't forget to set the left child of root to None after these operations.
    """
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                self.flatten(root.left)
                tail = root.left
                while tail.right:
                    tail = tail.right
                tail.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        
# @lc code=end

