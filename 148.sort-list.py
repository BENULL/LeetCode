#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (41.95%)
# Likes:    2929
# Dislikes: 137
# Total Accepted:    275.3K
# Total Submissions: 646.6K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # merge sort
    def sortList(self, head: ListNode) -> ListNode:
        def mergeSort(head):
            if not head or not head.next:
                return head
            # finf middle
            left = slow = fast = head
            fast = fast.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            leftSorted = mergeSort(left)
            rightSorted = mergeSort(right)
            return merge(leftSorted,rightSorted)

        def merge(left,right):
            dummy = ListNode(-1)
            prev = dummy
            while left and right:
                if left.val < right.val:
                    prev.next = left
                    left = left.next
                else:
                    prev.next = right
                    right = right.next
                prev = prev.next
            prev.next = left or right
            return dummy.next
        return mergeSort(head)
       
# @lc code=end

