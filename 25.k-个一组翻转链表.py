#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (65.78%)
# Likes:    1345
# Dislikes: 0
# Total Accepted:    240.8K
# Total Submissions: 366K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 进阶：
# 
# 
# 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
# 
# 
# 示例 4：
# 
# 
# 输入：head = [1], k = 1
# 输出：[1]
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 列表中节点的数量在范围 sz 内
# 1 
# 0 
# 1 
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head and not head.next:
            return head
        dummy = curr = end = ListNode(0, head)
        prev = None
        for _ in range(k):
            end = end.next

        while end:
            prev, curr = curr, curr.next
            end = end.next
            for _ in range(k-1):
                next = curr.next
                curr.next = next.next
                prev.next, next.next = next, prev.next
                if end:
                    end = end.next
        return dummy.next
            



    #     _len = 0
    #     p = head
    #     while p:
    #         _len += 1
    #         p = p.next
    #     for start in range(0,_len-k+1,k):
    #         head = self.reverseBetween(head, start+1, start+k)
    #     return head

    # def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    #     # insert 
    #     if not head and not head.next:
    #         return head
    #     dummy = curr = ListNode(0, head)
    #     prev = None
    #     for _ in range(left-1):
    #         curr = curr.next
    #     prev, curr = curr, curr.next
    #     for _ in range(right-left):
    #         next = curr.next
    #         curr.next = next.next
    #         prev.next, next.next = next, prev.next
    #     return dummy.next
        
        


# @lc code=end

