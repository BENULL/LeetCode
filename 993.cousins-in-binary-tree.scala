/*
 * @lc app=leetcode id=993 lang=scala
 *
 * [993] Cousins in Binary Tree
 *
 * https://leetcode.com/problems/cousins-in-binary-tree/description/
 *
 * algorithms
 * Easy (51.99%)
 * Likes:    1175
 * Dislikes: 63
 * Total Accepted:    126.7K
 * Total Submissions: 243K
 * Testcase Example:  '[1,2,3,4]\n4\n3'
 *
 * In a binary tree, the root node is at depth 0, and children of each depth k
 * node are at depth k+1.
 * 
 * Two nodes of a binary tree are cousins if they have the same depth, but have
 * different parents.
 * 
 * We are given the root of a binary tree with unique values, and the values x
 * and y of two different nodes in the tree.
 * 
 * Return true if and only if the nodes corresponding to the values x and y are
 * cousins.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * Input: root = [1,2,3,4], x = 4, y = 3
 * Output: false
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
 * Output: true
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * 
 * 
 * Input: root = [1,2,3,null,4], x = 2, y = 3
 * Output: false
 * 
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree will be between 2 and 100.
 * Each node has a unique integer value from 1 to 100.
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
    def isCousins(root: TreeNode, x: Int, y: Int): Boolean = {
        def findDepth(toFind:Int, parent:Int, node: TreeNode, actualDepth: Int): Option[(Int,Int)] ={
            if (toFind == node.value) Some(actualDepth,parent)
            else{
                Option(node.left).flatMap(findDepth(toFind, node.value, _, actualDepth + 1))
                    .orElse(Option(node.right).flatMap(findDepth(toFind, node.value, _, actualDepth + 1)))

            }
        }
        findDepth(x,root.value,root,0)
            .zip(findDepth(y,root.value,root,0))
            .exists(pair => pair._1._2 != pair._2._2 && pair._1._1 == pair._2._1)
        
    }
}
// @lc code=end

