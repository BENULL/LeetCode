#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (59.61%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    70.9K
# Total Submissions: 118.8K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 
# 差值是一个正数，其数值等于两值之差的绝对值。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [4,2,6,1,3]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目范围是 [2, 100]
# 0 <= Node.val <= 10^5
# 
# 
# 
# 
# 注意：本题与
# 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同
# 
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
    def minDiffInBST(self, root: TreeNode) -> int:

        def findRightNode(root):
            while root.right:
                root = root.right
            return root.val
        def findLeftNode(root):
            while root.left:
                root = root.left
            return root.val
        leftDiffMin = rightDiffMin = 100001
        if not root.left and not root.right:
            return 100001
        if root.left:
            leftDiffMin = min(abs(root.val - findRightNode(root.left)),self.minDiffInBST(root.left))
        if root.right:
            rightDiffMin = min(abs(root.val - findLeftNode(root.right)),self.minDiffInBST(root.right))
        return min(leftDiffMin,rightDiffMin)

        """
        inorder traversal
        """
        # recursive
        # def inorder(root):
        #     if not root: return  
        #     nonlocal pre,ans
        #     inorder(root.left)
        #     if pre==-1:
        #         pre = root.val
        #     else:
        #         ans = min(abs(pre-root.val), ans)
        #         pre  = root.val
        #     inorder(root.right)
        # ans = float('inf')
        # pre = -1
        # inorder(root)       
        # return ans

        # recursive
        # def in_order(prev, curr, m):
        #     if not curr:
        #         return prev, m
        #     prev, m = in_order(prev, curr.left, m)
        #     m, prev = min(m, curr.val - prev), curr.val
        #     return in_order(prev, curr.right, m)
        # return in_order(-float("inf"),root,float("inf"))[1]

        # iterative
        # ans, pre = float("inf"), -1
        # stack = []
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop(-1)
        #     if pre == -1:
        #         pre = root.val
        #     else:
        #         ans = min(ans,root.val - pre)
        #         pre = root.val
        #     root = root.right 
        # return ans
