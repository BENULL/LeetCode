/*
 * @lc app=leetcode id=704 lang=scala
 *
 * [704] Binary Search
 *
 * https://leetcode.com/problems/binary-search/description/
 *
 * algorithms
 * Easy (51.89%)
 * Likes:    1109
 * Dislikes: 56
 * Total Accepted:    226.5K
 * Total Submissions: 419.3K
 * Testcase Example:  '[-1,0,3,5,9,12]\n9'
 *
 * Given a sorted (in ascending order) integer array nums of n elements and a
 * target value, write a function to search target in nums. If target exists,
 * then return its index, otherwise return -1.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [-1,0,3,5,9,12], target = 9
 * Output: 4
 * Explanation: 9 exists in nums and its index is 4
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [-1,0,3,5,9,12], target = 2
 * Output: -1
 * Explanation: 2 does not exist in nums so return -1
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * You may assume that all elements in nums are unique.
 * n will be in the range [1, 10000].
 * The value of each element in nums will be in the range [-9999, 9999].
 * 
 * 
 */

// @lc code=start
object Solution {
    // binary search
    // def search(nums: Array[Int], target: Int): Int = {
    //     var left = 0
    //     var right = nums.length - 1
    //     while (left<=right){
    //         var mid = left + (right - left)/2
    //         if (nums(mid)==target)
    //             return mid
    //         else if(nums(mid)>target)
    //             right = mid -1
    //         else
    //             left = mid + 1
    //     }
    //     return -1
        
    // }

    // tailrec
    // def search(nums: Array[Int], target: Int): Int = {

    //     @annotation.tailrec
    //     def helper(left:Int,right:Int):Int = {
    //         val mid = left + (right - left) / 2
    //         if (left > right) -1
    //         else if (nums(mid) == target) mid
    //         else if (nums(mid) < target) helper(mid + 1, right)
    //         else helper(left, mid - 1)
    //     }
    //     helper(0, nums.length - 1)
    // }

    import collection.Searching.Found
  
    def search(nums: Array[Int], target: Int): Int =
        nums.search(target) match {
            case Found(index) => index
            case _ => -1  
    }
}
// @lc code=end

