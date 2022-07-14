# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    面试题 02.01. 移除重复节点
    编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

    示例1:

    输入：[1, 2, 3, 3, 2, 1]
    输出：[1, 2, 3]
    示例2:

    输入：[1, 1, 1, 1, 2]
    输出：[1, 2]
    提示：

    链表长度在[0, 20000]范围内。
    链表元素在[0, 20000]范围内。
    进阶：

    如果不得使用临时缓冲区，该怎么解决？
    """
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        visited = set()
        while cur:
            if cur.val in visited:
                pre.next = cur.next
            else:
                visited.add(cur.val)
                pre = cur
            cur = cur.next
        return head
