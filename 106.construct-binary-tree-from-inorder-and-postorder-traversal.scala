/*
 * @lc app=leetcode id=106 lang=scala
 *
 * [106] Construct Binary Tree from Inorder and Postorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
 *
 * algorithms
 * Medium (45.36%)
 * Likes:    2198
 * Dislikes: 41
 * Total Accepted:    264.3K
 * Total Submissions: 544.8K
 * Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
 *
 * Given inorder and postorder traversal of a tree, construct the binary tree.
 * 
 * Note:
 * You may assume that duplicates do not exist in the tree.
 * 
 * For example, given
 * 
 * 
 * inorder = [9,3,15,20,7]
 * postorder = [9,15,7,20,3]
 * 
 * Return the following binary tree:
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def buildTree(inorder: Array[Int], postorder: Array[Int]): TreeNode = {
        var postIndex = postorder.length-1
        def buildTreeNode(from:Int,to:Int):TreeNode = {
            if (from>to) return null
            val value = postorder(postIndex)
            postIndex -= 1
            val inorderIndex =inorder.indexOf(value,from)

            val right = buildTreeNode(inorderIndex+1,to)
            val left = buildTreeNode(from,inorderIndex-1)
            new TreeNode(value,left,right)
        }
        
        buildTreeNode(0,inorder.length-1)
    }
}
// @lc code=end

