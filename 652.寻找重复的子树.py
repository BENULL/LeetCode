#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#
# https://leetcode-cn.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (57.11%)
# Likes:    352
# Dislikes: 0
# Total Accepted:    37.5K
# Total Submissions: 65.7K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
# 
# 两棵树重复是指它们具有相同的结构以及相同的结点值。
# 
# 示例 1：
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# 
# 下面是两个重复的子树：
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# 
# 和
# 
# ⁠   4
# 
# 
# 因此，你需要以列表的形式返回上述重复子树的根结点。
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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []

        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid
        lookup(root)
        return ans
# @lc code=end

