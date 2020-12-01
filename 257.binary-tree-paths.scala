/*
 * @lc app=leetcode id=257 lang=scala
 *
 * [257] Binary Tree Paths
 *
 * https://leetcode.com/problems/binary-tree-paths/description/
 *
 * algorithms
 * Easy (51.16%)
 * Likes:    2156
 * Dislikes: 121
 * Total Accepted:    354.7K
 * Total Submissions: 673.2K
 * Testcase Example:  '[1,2,3,null,5]'
 *
 * Given a binary tree, return all root-to-leaf paths.
 * 
 * Note: A leaf is a node with no children.
 * 
 * Example:
 * 
 * 
 * Input:
 * 
 * ⁠  1
 * ⁠/   \
 * 2     3
 * ⁠\
 * ⁠ 5
 * 
 * Output: ["1->2->5", "1->3"]
 * 
 * Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    
    

    // def binaryTreePaths(root: TreeNode): List[String] = {
    //     import scala.collection.mutable.ListBuffer

    //     def dfs(root:TreeNode,path:List[Int],ret:ListBuffer[String]):Unit = {
    //         if (root==null)
    //             return 
    //         val newPath = path:+root.value
    //         if (root.left==null && root.right==null)
    //             ret += newPath.mkString("->")
    //         dfs(root.left,newPath,ret)
    //         dfs(root.right,newPath,ret)

    //     }
    //     val ret = ListBuffer[String]()
    //     dfs(root,List(),ret)
    //     ret.toList
    // }


    def binaryTreePaths(root: TreeNode): List[String] = {
        binaryTreePaths(root, List[Int](), List[List[Int]]()).map(_.mkString("->"))
    }
    
    def binaryTreePaths(root: TreeNode, par:List[Int] ,res:List[List[Int]]):List[List[Int]]= {
        root match {
            case null => res 
            case _ => (root.left, root.right) match {
                case (l:TreeNode, r:TreeNode )=> binaryTreePaths(l, par:::List(root.value), res) ::: binaryTreePaths(r, par:::List(root.value), res)
                case (l:TreeNode, null) => binaryTreePaths(l, par:::List(root.value), res)
                case (null, r:TreeNode) => binaryTreePaths(r, par:::List(root.value), res)
                case (null, null) => (par:::List(root.value)):: res
            }
        }
    }
}
// @lc code=end

