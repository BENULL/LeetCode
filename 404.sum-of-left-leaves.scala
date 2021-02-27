/*
 * @lc app=leetcode id=404 lang=scala
 *
 * [404] Sum of Left Leaves
 *
 * https://leetcode.com/problems/sum-of-left-leaves/description/
 *
 * algorithms
 * Easy (50.86%)
 * Likes:    1699
 * Dislikes: 163
 * Total Accepted:    235.2K
 * Total Submissions: 450.1K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Find the sum of all left leaves in a given binary tree.
 * 
 * Example:
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * There are two left leaves in the binary tree, with values 9 and 15
 * respectively. Return 24.
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
    def sumOfLeftLeaves(root: TreeNode): Int = {

        def helper(r:TreeNode,isLeft:Boolean) : Int = (r,isLeft) match {
            case (null,r) => 0
            case (r,true) if r.left==null && r.right==null => r.value
            case (r,_) => helper(r.left,true) + helper(r.right,false)
        }
        
        helper(root,false)
    }
}
// @lc code=end

