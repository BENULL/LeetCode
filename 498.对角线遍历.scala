/*
 * @lc app=leetcode.cn id=498 lang=scala
 *
 * [498] 对角线遍历
 *
 * https://leetcode-cn.com/problems/diagonal-traverse/description/
 *
 * algorithms
 * Medium (43.17%)
 * Likes:    185
 * Dislikes: 0
 * Total Accepted:    33K
 * Total Submissions: 76.3K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
 * 
 * 
 * 
 * 示例:
 * 
 * 输入:
 * [
 * ⁠[ 1, 2, 3 ],
 * ⁠[ 4, 5, 6 ],
 * ⁠[ 7, 8, 9 ]
 * ]
 * 
 * 输出:  [1,2,4,7,5,3,6,8,9]
 * 
 * 解释:
 * 
 * 
 * 
 * 
 * 
 * 说明:
 * 
 * 
 * 给定矩阵中的元素总数不会超过 100000 。
 * 
 * 
 */

// @lc code=start
object Solution {
    // mle
    def findDiagonalOrder(mat: Array[Array[Int]]): Array[Int] = {
        mat.zipWithIndex.map{case(nums,idx)=>Array.fill(idx)(None)++:nums++:Array.fill(mat.length-idx-1)(None)}
        .transpose.zipWithIndex
        .flatMap{
            case(nums,idx) if idx%2==0 => nums.reverse
            case(nums,idx) => nums
        }
        .filter(_ != None).map(_.toString.toInt)

    }
}
// @lc code=end

