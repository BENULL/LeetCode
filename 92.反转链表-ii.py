#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (54.91%)
# Likes:    1058
# Dislikes: 0
# Total Accepted:    220.7K
# Total Submissions: 401.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目为 n
# 1 
# -500 
# 1 
# 
# 
# 
# 
# 进阶： 你可以使用一趟扫描完成反转吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # insert 
        if not head and not head.next:
            return head
        dummy = curr = ListNode(0, head)
        prev = None
        for _ in range(left-1):
            curr = curr.next
        prev, curr = curr, curr.next
        for _ in range(right-left):
            next = curr.next
            curr.next = next.next
            prev.next, next.next = next, prev.next
        return dummy.next
        





# @lc code=end

