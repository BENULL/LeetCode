#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
# https://leetcode-cn.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (78.81%)
# Likes:    1114
# Dislikes: 0
# Total Accepted:    348.9K
# Total Submissions: 442.7K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# 翻转一棵二叉树。
# 
# 示例：
# 
# 输入：
# 
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
# 
# 输出：
# 
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
# 
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
# 
# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # recursive

        # if not root: return None
        # root.left,root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root

        # bfs iterative

        # if not root: return None
        # queue = [root]
        # while queue:
        #     node = queue.pop(0)
        #     node.left, node.right = node.right, node.left
        #     [queue.append(n) for n in [node.left, node.right] if n]
        # return root

        # dfs pre-order iterative
        # if not root: return None
        # stack = []
        # node = root
        # while stack or node:
        #     if node:  
        #         node.left, node.right = node.right, node.left
        #         stack.append(node) 
        #         node = node.left
        #     else:
        #         node = stack.pop()
        #         node = node.right
        # return root









# @lc code=end

