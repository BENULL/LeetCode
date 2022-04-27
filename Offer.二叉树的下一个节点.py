"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
题目解析：

图片我们知道二叉树中序遍历是：左子树->根节点->右子树
假设给定节点是 x
如果 x 存在右子树，那么它的下一个结点就是右子树的最左结点。比如 5 的下一个结点是 9
如果 x 没有右子树
x 是父结点的左子结点，那么其父结点就是它的下一个结点，比如 7 的结点是 4
x 是父结点的右子结点，那么需要一直沿着父结点向上遍历，找到该结点是其父结点的左子结点为止，那么这个结点的父结点就是 x 的下一个结点。比如 9 的下一个结点是 1

"""

# Definition for a binary tree node.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def GetNext(self, p: 'TreeLinkNode'):
        if not p:
            return None
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
            while p.next:
                if p == p.next.left:
                    return p.next
                p = p.next
        return None