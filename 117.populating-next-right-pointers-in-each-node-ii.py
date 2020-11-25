#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (38.81%)
# Likes:    1925
# Dislikes: 190
# Total Accepted:    283.6K
# Total Submissions: 702.4K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# Given a binary tree
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# 
# Follow up:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # recursive
        """
        tricky part is that, we have to make sure the right part of the tree is complete before tackling the left part, 
        as when middle nodes are missing, 
        we need completed next information on the right part of the tree for correctness
        """
        def findNext(root):
            if not root: return root
            if root.left: return root.left
            if root.right: return root.right
            return findNext(root.next)
        
        if not root: return root
        if root.left:
            if root.right:
                root.left.next=root.right
            else:
                root.left.next = findNext(root.next)
            
        if root.right:
            root.right.next = findNext(root.next)
        
        self.connect(root.right)
        self.connect(root.left)
        return root

        
        # return root

        # bfs
        # if not root:
        #     return root
        # queue = [root]
        # while queue:
        #     for i in range(0,len(queue)-1):
        #         queue[i].next = queue[i+1]
        #     newq = []
        #     for q in queue:
        #         if q.left:
        #             newq.append(q.left)
        #         if q.right:
        #             newq.append(q.right)
        #     queue = newq
        # return root

        #bfs with point
        # queue, level, curr = root, None, None
        # while queue:
        #     if queue.left:
        #         if not level:
        #             level = curr = queue.left
        #         else:
        #             curr.next = queue.left
        #             curr = curr.next
        #     if queue.right:
        #         if not level:
        #             level = curr = queue.right
        #         else:
        #             curr.next = queue.right
        #             curr = curr.next
        #     queue = queue.next
        #     if not queue and level:
        #         queue, level, curr = level, None, None
        # return root
                
        
# @lc code=end

