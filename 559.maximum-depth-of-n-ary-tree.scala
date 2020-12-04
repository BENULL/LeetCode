/*
 * @lc app=leetcode id=559 lang=scala
 *
 * [559] Maximum Depth of N-ary Tree
 *
 * https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
 *
 * algorithms
 * Easy (68.40%)
 * Likes:    1093
 * Dislikes: 51
 * Total Accepted:    136.5K
 * Total Submissions: 197.4K
 * Testcase Example:  '[1,null,3,2,4,null,5,6]'
 *
 * Given a n-ary tree, find its maximum depth.
 * 
 * The maximum depth is the number of nodes along the longest path from the
 * root node down to the farthest leaf node.
 * 
 * Nary-Tree input serialization is represented in their level order traversal,
 * each group of children is separated by the null value (See examples).
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: root = [1,null,3,2,4,null,5,6]
 * Output: 3
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: root =
 * [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
 * Output: 5
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The depth of the n-ary tree is less than or equal to 1000.
 * The total number of nodes is between [0, 10^4].
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var children: List[Node] = List()
 * }
 */

object Solution {
    def maxDepth(root: Node): Int = {
        //1.
        // var maxDepth:Int = 0

        // def dfs(root:Node,depth:Int):Unit={
            
        //     if (root==null) return 
        //     if (root.children != null || !root.children.isEmpty){
        //         for (node <- root.children){
        //             dfs(node,depth+1)
        //         }
        //     }
        //     maxDepth = math.max(depth+1,maxDepth)
            
        // }
        // dfs(root,0)
        // return maxDepth

        //2.
        // if (root==null) 0
        // else if (root.children == null || root.children.isEmpty) 1
        // else {
        //     root.children.foldLeft(1)((acc,n)=> math.max(acc,1+maxDepth(n)))
        // }


        //3.
        if (root==null) 0
        else if (!root.children.isEmpty){
            root.children.map(node=>1+maxDepth(node)).max
        }else{
            1
        }
        
    }
}
// @lc code=end

