#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (47.31%)
# Likes:    2462
# Dislikes: 91
# Total Accepted:    267.9K
# Total Submissions: 545.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# 
# Example 1:
# 
# 
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
# 
# 
# Example 2:
# 
# 
# Input: head = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [0]
# Output: [0]
# 
# 
# Example 4:
# 
# 
# Input: head = [1,3]
# Output: [3,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in head is in the range [0, 2 * 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMiddle(self, head):
        prevPtr = None
        fastPtr = head
        slowPtr = head
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        if prevPtr:
            prevPtr.next = None

        return slowPtr

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        mid = self.findMiddle(head)
        node = TreeNode(mid.val)
        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
# @lc code=end

