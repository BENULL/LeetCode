/*
 * @lc app=leetcode.cn id=513 lang=scala
 *
 * [513] 找树左下角的值
 *
 * https://leetcode-cn.com/problems/find-bottom-left-tree-value/description/
 *
 * algorithms
 * Medium (72.55%)
 * Likes:    169
 * Dislikes: 0
 * Total Accepted:    36.6K
 * Total Submissions: 50.2K
 * Testcase Example:  '[2,1,3]'
 *
 * 给定一个二叉树，在树的最后一行找到最左边的值。
 * 
 * 示例 1:
 * 
 * 
 * 输入:
 * 
 * ⁠   2
 * ⁠  / \
 * ⁠ 1   3
 * 
 * 输出:
 * 1
 * 
 * 
 * 
 * 
 * 示例 2: 
 * 
 * 
 * 输入:
 * 
 * ⁠       1
 * ⁠      / \
 * ⁠     2   3
 * ⁠    /   / \
 * ⁠   4   5   6
 * ⁠      /
 * ⁠     7
 * 
 * 输出:
 * 7
 * 
 * 
 * 
 * 
 * 注意: 您可以假设树（即给定的根节点）不为 NULL。
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
    // import scala.collection.mutable
    // def findBottomLeftValue(root: TreeNode): Int = {
    //     val leftByLevel = mutable.Map.empty[Int,Int]
    //     def traverse(root: TreeNode, level: Int): Unit = {
    //         if (root != null) {
    //             leftByLevel.getOrElseUpdate(level, root.value)
    //             traverse(root.left, level + 1)
    //             traverse(root.right, level + 1)
    //         }
    //     }
    //     traverse(root, 0)
    //     leftByLevel.toSeq.maxBy(_._1)._2
    // }

    
    def findBottomLeftValue(root: TreeNode): Int = {
        def traversal(level: List[TreeNode], leftValue: Int): Int = {
            level match {
                case Nil    => leftValue
                case _      =>
                    val nextlevel = level.flatMap(nd => List(nd.left, nd.right).filter(_ != null))
                    traversal(nextlevel, level.head.value)
            }
        }

        traversal(List(root), root.value)
        
    }
}
// @lc code=end

