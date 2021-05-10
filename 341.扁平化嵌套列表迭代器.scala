/*
 * @lc app=leetcode.cn id=341 lang=scala
 *
 * [341] 扁平化嵌套列表迭代器
 *
 * https://leetcode-cn.com/problems/flatten-nested-list-iterator/description/
 *
 * algorithms
 * Medium (72.73%)
 * Likes:    331
 * Dislikes: 0
 * Total Accepted:    44.9K
 * Total Submissions: 61.7K
 * Testcase Example:  '[[1,1],2,[1,1]]'
 *
 * 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
 * 
 * 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: [[1,1],2,[1,1]]
 * 输出: [1,1,2,1,1]
 * 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
 * 
 * 示例 2:
 * 
 * 输入: [1,[4,[6]]]
 * 输出: [1,4,6]
 * 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
 * 
 * 
 */

// @lc code=start
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * trait NestedInteger {
 *
 *   // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *   def isInteger: Boolean
 *
 *   // Return the single integer that this NestedInteger holds, if it holds a single integer.
 *   def getInteger: Int
 *
 *   // Set this NestedInteger to hold a single integer.
 *   def setInteger(i: Int): Unit
 *
 *   // Return the nested list that this NestedInteger holds, if it holds a nested list.
 *   def getList: Array[NestedInteger]
 *
 *   // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *   def add(ni: NestedInteger): Unit
 * }
 */

class NestedIterator(_nestedList: List[NestedInteger]) {

    import scala.collection.mutable.Queue

    import scala.annotation.tailrec

    
    def loop(input: List[NestedInteger], acc: Queue[Int]): Queue[Int] = input match {
        case Nil => acc
        case x :: xs => {
            if (x.isInteger) loop(xs, acc.enqueue(x.getInteger))
            else loop(xs, loop(x.getList.toList, acc))  
        } 
    }

    val q:Queue[Int] = loop(_nestedList, Queue[Int]())

    def next(): Int =  q.dequeue
    
    def hasNext(): Boolean =  q.nonEmpty

}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * var obj = new NestedIterator(nestedList)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
// @lc code=end

