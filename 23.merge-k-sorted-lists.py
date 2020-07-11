#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Brute Force
    # sorted then add to a new List
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     nodes = []
    #     head = point = ListNode(0)
    #     for l in lists:
    #         while l:
    #             nodes.append(l.val)
    #             l = l.next
    #     for x in sorted(nodes):
    #         point.next = ListNode(x)
    #         point = point.next
    #     return head.next


    # Merge with Divide And Conquer
    # Pair up \text{k}k lists and merge each pair
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount  = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0,amount-interval,2*interval):
                lists[i]=self.merge2(lists[i],lists[i+interval])
            interval *= 2
        return lists[0] if amount>0 else None


    def merge2(self,l1,l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next
            
# @lc code=end

