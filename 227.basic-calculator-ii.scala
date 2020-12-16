/*
 * @lc app=leetcode id=227 lang=scala
 *
 * [227] Basic Calculator II
 *
 * https://leetcode.com/problems/basic-calculator-ii/description/
 *
 * algorithms
 * Medium (36.76%)
 * Likes:    1960
 * Dislikes: 317
 * Total Accepted:    234K
 * Total Submissions: 614.1K
 * Testcase Example:  '"3+2*2"'
 *
 * Given a string s which represents an expression, evaluate this expression
 * and return its value. 
 * 
 * The integer division should truncate toward zero.
 * 
 * 
 * Example 1:
 * Input: s = "3+2*2"
 * Output: 7
 * Example 2:
 * Input: s = " 3/2 "
 * Output: 1
 * Example 3:
 * Input: s = " 3+5 / 2 "
 * Output: 5
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 3 * 10^5
 * s consists of integers and operators ('+', '-', '*', '/') separated by some
 * number of spaces.
 * s represents a valid expression.
 * All the integers in the expression are non-negative integers in the range
 * [0, 2^31 - 1].
 * The answer is guaranteed to fit in a 32-bit integer.
 * 
 * 
 */

// @lc code=start
object Solution {
    // 3+2*2
    val Additive = Array('+','-')
    val Multiplicative = Array('*','/')

    def calculate(s: String): Int = {
        val evals = s.split(Additive).map{ t => {
                val ints = t.split(Multiplicative).map(_.trim.toInt)
                t.filter(Multiplicative.contains).zip(ints.tail).foldLeft(ints.head){
                    case (left,('*',right)) => left*right
                    case (left,('/',right)) => left/right
                }

            }
        }

        s.filter(Additive.contains).zip(evals.tail).foldLeft(evals.head){
            case (left,('+',right)) => left+right
            case (left,('-',right)) => left-right
        }
        
    }
}
// @lc code=end

