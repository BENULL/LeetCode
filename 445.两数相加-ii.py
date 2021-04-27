#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (58.38%)
# Likes:    371
# Dislikes: 0
# Total Accepted:    69.2K
# Total Submissions: 118.7K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 
# 
# 进阶：
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 
# 
# 示例：
# 
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # stack 考python无限长整形没有大数相加问题 可以不用栈
        s1, s2 = [], [] 
        while l1:
            s1.insert(0,l1.val)
            l1 = l1.next
        while l2:
            s2.insert(0,l2.val)
            l2 = l2.next

        res = ListNode()
        carry = 0 
        for a,b in itertools.zip_longest(s1,s2,fillvalue = 0):
            node = ListNode((a+b+carry) % 10,res.next)
            carry = (a+b+carry) // 10
            res.next = node

        if carry!=0:
            node = ListNode(carry,res.next)
            res.next = node
        return res.next



# @lc code=end

