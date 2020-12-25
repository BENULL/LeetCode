/*
 * @lc app=leetcode id=103 lang=scala
 *
 * [103] Binary Tree Zigzag Level Order Traversal
 *
 * https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
 *
 * algorithms
 * Medium (47.12%)
 * Likes:    2879
 * Dislikes: 116
 * Total Accepted:    450.9K
 * Total Submissions: 909.5K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given a binary tree, return the zigzag level order traversal of its nodes'
 * values. (ie, from left to right, then right to left for the next level and
 * alternate between).
 * 
 * 
 * For example:
 * Given binary tree [3,9,20,null,null,15,7],
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 * 
 * return its zigzag level order traversal as:
 * 
 * [
 * ⁠ [3],
 * ⁠ [20,9],
 * ⁠ [15,7]
 * ]
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
    def zigzagLevelOrder(root: TreeNode): List[List[Int]] = {

        def bfs(visited:List[List[TreeNode]]):List[List[TreeNode]]={
            visited.last.filter(_!=null).flatMap(node => List(node.left,node.right)).filter(_!=null) match {
                case newLevel if newLevel.isEmpty => visited
                case newLevel:List[TreeNode] => bfs(visited:::List(newLevel))
            }
        }

        if (root ==null) List()
        else bfs(List(List(root))).zipWithIndex.map({
            case (level,index) if index%2==0 => level.map(_.value)
            case (level,index) => level.map(_.value).reverse
        })     
    }
}
// @lc code=end

