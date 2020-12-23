/*
 * @lc app=leetcode id=57 lang=scala
 *
 * [57] Insert Interval
 *
 * https://leetcode.com/problems/insert-interval/description/
 *
 * algorithms
 * Hard (33.42%)
 * Likes:    1665
 * Dislikes: 185
 * Total Accepted:    255K
 * Total Submissions: 761.6K
 * Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
 *
 * Given a set of non-overlapping intervals, insert a new interval into the
 * intervals (merge if necessary).
 * 
 * You may assume that the intervals were initially sorted according to their
 * start times.
 * 
 * Example 1:
 * 
 * 
 * Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
 * Output: [[1,5],[6,9]]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
 * Output: [[1,2],[3,10],[12,16]]
 * Explanation: Because the new interval [4,8] overlaps with
 * [3,5],[6,7],[8,10].
 * 
 * NOTE: input types have been changed on April 15, 2019. Please reset to
 * default code definition to get new method signature.
 * 
 */

// @lc code=start
object Solution {
    def insert(intervals: Array[Array[Int]], newInterval: Array[Int]): Array[Array[Int]] = {
        val (acc,last) = intervals.foldLeft((Array.empty[Array[Int]],newInterval)){
            case ((rest,newInterval),head) =>
                if(newInterval.last<head.head){
                    (rest:+newInterval,head)
                }else if (newInterval.head>head.last){
                    (rest:+head,newInterval)
                }else{
                    (rest,Array(Math.min(head.head,newInterval.head),Math.max(head.last,newInterval.last)))
                }
        }
        acc:+last
        
    }
}
// @lc code=end

