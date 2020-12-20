/*
 * @lc app=leetcode id=438 lang=scala
 *
 * [438] Find All Anagrams in a String
 *
 * https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
 *
 * algorithms
 * Medium (43.08%)
 * Likes:    3710
 * Dislikes: 191
 * Total Accepted:    321.6K
 * Total Submissions: 723.4K
 * Testcase Example:  '"cbaebabacd"\n"abc"'
 *
 * Given a string s and a non-empty string p, find all the start indices of p's
 * anagrams in s.
 * 
 * Strings consists of lowercase English letters only and the length of both
 * strings s and p will not be larger than 20,100.
 * 
 * The order of output does not matter.
 * 
 * Example 1:
 * 
 * Input:
 * s: "cbaebabacd" p: "abc"
 * 
 * Output:
 * [0, 6]
 * 
 * Explanation:
 * The substring with start index = 0 is "cba", which is an anagram of "abc".
 * The substring with start index = 6 is "bac", which is an anagram of
 * "abc".
 * 
 * 
 * 
 * Example 2:
 * 
 * Input:
 * s: "abab" p: "ab"
 * 
 * Output:
 * [0, 1, 2]
 * 
 * Explanation:
 * The substring with start index = 0 is "ab", which is an anagram of "ab".
 * The substring with start index = 1 is "ba", which is an anagram of "ab".
 * The substring with start index = 2 is "ab", which is an anagram of "ab".
 * 
 * 
 */

// @lc code=start
object Solution {
   
    def findAnagrams(s: String, p: String): List[Int] = {
        val map = p.groupMapReduce(identity)(_ => 1)(_+_)
        s.zipWithIndex.view.foldLeft(List.empty[Int])((acc,x)=>{
            if (map.contains(x._1) && x._2+p.length <= s.length){
                val mapIdx = s.substring(x._2,x._2+p.length).groupMapReduce(identity)(_ => 1)(_+_)
                if(map == mapIdx) acc :+ x._2 else acc
            } else {
                acc
            }
        })
    }
}
// @lc code=end

