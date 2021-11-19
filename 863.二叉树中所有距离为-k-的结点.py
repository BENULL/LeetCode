#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#
# https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (60.43%)
# Likes:    449
# Dislikes: 0
# Total Accepted:    36.4K
# Total Submissions: 60.2K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
# 
# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 输出：[7,4,1]
# 解释：
# 所求结点为与目标结点（值为 5）距离为 2 的结点，
# 值分别为 7，4，以及 1
# 
# 
# 
# 注意，输入的 "root" 和 "target" 实际上是树上的结点。
# 上面的输入仅仅是对这些对象进行了序列化描述。
# 
# 
# 
# 
# 提示：
# 
# 
# 给定的树是非空的。
# 树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
# 目标结点 target 是树上的结点。
# 0 <= K <= 1000.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # bfs + adjacency list
        # build
        parents = {}
        res = []
        if k==0: return [target.val]
        def findParents(node):
            if node.left:
                parents[node.left.val] = node
                findParents(node.left)
            if node.right:
                parents[node.right.val] = node
                findParents(node.right)

        findParents(root)
        queue = [target]
        visited = set()
        level = 0
        while queue:
            level += 1
            tmp = []
            for node in queue:
                visited.add(node.val)
                for child in [node.left, node.right, parents[node.val] if node.val in parents else None]:
                    if child and child.val not in visited:
                        tmp.append(child)
            queue = tmp
            if level==k:
                return [node.val for node in queue]
        return []




        """
        tree -> directed graph 
        dfs + memory father node
        """
       
        # parents = {}
        # res = []

        # def findParents(node):
        #     if node.left:
        #         parents[node.left.val] = node
        #         findParents(node.left)
        #     if node.right:
        #         parents[node.right.val] = node
        #         findParents(node.right)

        # def dfs(node, origin, depth):
        #     if not node: return 
        #     if depth==k:
        #         res.append(node.val)
        #     if node.left != origin:
        #         dfs(node.left, node, depth + 1)
        #     if node.right != origin:
        #         dfs(node.right, node, depth + 1)
        #     if parents.get(node.val,None) != origin:
        #         dfs(parents.get(node.val,None), node, depth + 1)

        # findParents(root)
        # dfs(target, None, 0)
        # return res




        
        
# @lc code=end

