#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#
# https://leetcode-cn.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (47.84%)
# Likes:    477
# Dislikes: 0
# Total Accepted:    49.1K
# Total Submissions: 102.7K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key
# 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
# 
# 一般来说，删除节点可分为两个步骤：
# 
# 
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 
# 
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
# 
# 示例:
# 
# 
# root = [5,3,6,2,4,null,7]
# key = 3
# 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
# 
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
# 
# 另一个正确答案是 [5,2,6,null,4,null,7]。
# 
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
# 
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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # recursive
        if not root: return root
        p = root
        if p.val == key:
            if p.left and p.right:
                tmp = p.right

                ltree = p.left
                # 找到最右边节点
                while ltree.right:
                    ltree = ltree.right
                ltree.right = tmp

                p = p.left
            else:
                p = p.left or p.right
            
        elif p.val <key:
            p.right = self.deleteNode(p.right, key)
        else:
            p.left = self.deleteNode(p.left, key)
        return p
# @lc code=end

