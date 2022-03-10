#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (74.76%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    112.4K
# Total Submissions: 149.1K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
# 
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[1,3,5,6,2,4]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]
# 
# 
# 
# 
# 提示：
# 
# 
# 节点总数在范围 [0, 10^4]内
# 0 <= Node.val <= 10^4
# n 叉树的高度小于或等于 1000
# 
# 
# 
# 
# 进阶：递归法很简单，你可以使用迭代法完成此题吗?
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # res = []
        # if not root:
        #     return []
        # res.append(root.val)
        # for child in root.children:
        #     res.extend(self.preorder(child))
        # return res

        # iterate
        # 在前序遍历中，我们会先遍历节点本身，然后从左向右依次先序遍历该每个以子节点为根的子树，此时利用栈先进后出的原理，依次从右向左将子节点入栈，这样出栈的时候即可保证从左向右依次遍历每个子树。参考方法二的原理，可以提前将后续需要访问的节点压入栈中，这样就可以避免记录每个节点的子节点访问数量。
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(reversed(node.children))
            # for child in node.children[::-1]:
            #     stack.append(child)
        return res






        
# @lc code=end

