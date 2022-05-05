# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

    假设二叉树中至少有一个节点。

 

    示例 1:



    输入: root = [2,1,3]
    输出: 1
    示例 2:



    输入: [1,2,3,4,null,5,6,null,null,7]
    输出: 7

    """
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        res  = None
        queue = [root]
        while queue:
            res = queue[0].val
            queue = [child for node in queue for child in (node.left,node.right) if child]
        return res
