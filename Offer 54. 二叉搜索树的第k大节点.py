# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

 

    示例 1:

    输入: root = [3,1,4,null,2], k = 1
    3
    / \
    1   4
    \
       2
    输出: 4
    示例 2:

    输入: root = [5,3,6,2,4,null,null,1], k = 3
        5
        / \
        3   6
        / \
    2   4
    /
    1
    输出: 4
     

    限制：

    1 ≤ k ≤ 二叉搜索树元素个数

    """
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # recursive
        res = None
        index = 0
        def inorder(root):
            if not root:
                return None
            inorder(root.right)
            nonlocal index, res
            index += 1
            if index == k:
                res = root.val
                return 
            inorder(root.left)
        inorder(root)
        return res
