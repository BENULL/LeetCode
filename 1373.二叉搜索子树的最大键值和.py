#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
#
# https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree/description/
#
# algorithms
# Hard (40.59%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    8.6K
# Total Submissions: 21.2K
# Testcase Example:  '[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]'
#
# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。
# 
# 二叉搜索树的定义如下：
# 
# 
# 任意节点的左子树中的键值都 小于 此节点的键值。
# 任意节点的右子树中的键值都 大于 此节点的键值。
# 任意节点的左子树和右子树都是二叉搜索树。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# 输出：20
# 解释：键值为 3 的子树是和最大的二叉搜索树。
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：root = [4,3,null,1,2]
# 输出：2
# 解释：键值为 2 的单节点子树是和最大的二叉搜索树。
# 
# 
# 示例 3：
# 
# 
# 输入：root = [-4,-2,-5]
# 输出：0
# 解释：所有节点键值都为负数，和最大的二叉搜索树为空。
# 
# 
# 示例 4：
# 
# 
# 输入：root = [2,1,3]
# 输出：6
# 
# 
# 示例 5：
# 
# 
# 输入：root = [5,4,8,3,null,6,3]
# 输出：7
# 
# 
# 
# 
# 提示：
# 
# 
# 每棵树有 1 到 40000 个节点。
# 每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
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
    def maxSumBST(self, root: TreeNode) -> int:
        # TLE 
        # def isBST(root):
        #     stack, pre, _sum = [], float('-inf'), 0
        #     while root or stack:
        #         while root:
        #             stack.append(root)
        #             root = root.left
        #         root = stack.pop()
        #         if pre>=root.val:
        #             return False, 0 
        #         _sum += root.val
        #         pre = root.val
        #         root = root.right
        #     return True, _sum

        # if not root: return 0
        # flag, _sum = isBST(root)
        
        # return max(self.maxSumBST(root.left),self.maxSumBST(root.right),_sum if flag else 0)

        # from bottom to up 
        res = float('-inf')
        def dfs(root):
            if not root: return (float('-inf'),float('inf'), 0, True)
            left = dfs(root.left)
            right = dfs(root.right)

            isBST = False
            _sum = left[2]+right[2]+root.val
            
            if left[0]<root.val and right[1]>root.val and left[3] and right[3]:
                isBST = True
            if isBST:
                nonlocal res
                res = max(res,_sum)
            return (max(left[0],right[0],root.val),min(left[1],right[1],root.val),_sum, isBST)
        
        
        dfs(root)
        return max(res, 0)


# @lc code=end

