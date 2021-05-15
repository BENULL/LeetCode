#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#
# https://leetcode-cn.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (72.55%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    36.6K
# Total Submissions: 50.2K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，在树的最后一行找到最左边的值。
# 
# 示例 1:
# 
# 
# 输入:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# 输出:
# 1
# 
# 
# 
# 
# 示例 2: 
# 
# 
# 输入:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# 输出:
# 7
# 
# 
# 
# 
# 注意: 您可以假设树（即给定的根节点）不为 NULL。
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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # dfs + depth

        # res = -1
        # d = 0
        # @lru_cache(None)
        # def helper(root,depth):
        #     if not root: return 
        #     nonlocal res,d
        #     if not root.right and not root.left and depth>d:
        #         res = root.val
        #         d = depth
        #     helper(root.left,depth+1)
        #     helper(root.right,depth+1)
        # helper(root,1)
        # return res

        # bfs
        nodes,res = [root], -1
        while nodes:
            res = nodes[0].val
            nodes = [child for node in nodes for child in (node.left,node.right) if child]
        return res


# @lc code=end

