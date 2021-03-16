#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (38.42%)
# Likes:    2513
# Dislikes: 122
# Total Accepted:    445K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [], val = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [7,7,7,7], val = 7
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= k <= 50
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # recursive


        # if not head:
        #     return None
        # head.next = self.removeElements(head.next,val)
        # return head.next if head.val==val else head

        # iterative two 

        # dummy = ListNode(-1,head)
        # pre, node = dummy, dummy.next
        # while node:
        #     if node.val == val:
        #         pre.next = node.next
        #     else:
        #         pre = pre.next
        #     node = node.next
        # return dummy.next

        # iterative one 


        dummy = ListNode(-1,head)
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next



        
# @lc code=end

