/*
 * @lc app=leetcode id=872 lang=scala
 *
 * [872] Leaf-Similar Trees
 *
 * https://leetcode.com/problems/leaf-similar-trees/description/
 *
 * algorithms
 * Easy (64.61%)
 * Likes:    959
 * Dislikes: 43
 * Total Accepted:    107.6K
 * Total Submissions: 166.8K
 * Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +
  '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
 *
 * Consider all the leaves of a binary tree, from left to right order, the
 * values of those leaves form a leaf value sequence.
 * 
 * 
 * 
 * For example, in the given tree above, the leaf value sequence is (6, 7, 4,
 * 9, 8).
 * 
 * Two binary trees are considered leaf-similar if their leaf value sequence is
 * the same.
 * 
 * Return true if and only if the two given trees with head nodes root1 and
 * root2 are leaf-similar.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
 * [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root1 = [1], root2 = [1]
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: root1 = [1], root2 = [2]
 * Output: false
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: root1 = [1,2], root2 = [2,2]
 * Output: true
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: root1 = [1,2,3], root2 = [1,3,2]
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in each tree will be in the range [1, 200].
 * Both of the given trees will have values in the range [0, 200].
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

    

    // def leafSimilar(root1: TreeNode, root2: TreeNode): Boolean = leafs(Seq(root1)) == leafs(Seq(root2))
    
    // private def leafs(nodes: Seq[TreeNode]): Seq[Int] = 
    //     if (nodes.exists(n => n.left != null || n.right!=null))
    //         leafs(nodes.flatMap{n => 
    //             if (n.left == null && n.right==null)
    //                 Seq(n)
    //             else
    //                 Seq(n.left, n.right).filter(null !=)
    //         })
    //     else
    //         nodes.map(_.value)
    import scala.language.postfixOps
    def leafSimilar(root1: TreeNode, root2: TreeNode): Boolean = {

        @scala.annotation.tailrec
        def leafs(nodes: Seq[TreeNode]):Seq[Int]= {
            if (nodes.exists(n=>n.left!=null||n.right!=null))
                leafs(nodes.flatMap{ n =>
                    if (n.left==null && n.right==null)
                        Seq(n)
                    else
                        Seq(n.left,n.right).filter(null!=)
                })
            else
                nodes.map(_.value)
        }
        leafs(Seq(root1)) == leafs(Seq(root2))
        
    }
}
// @lc code=end

