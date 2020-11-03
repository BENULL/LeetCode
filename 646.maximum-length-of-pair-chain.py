#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (51.64%)
# Likes:    1097
# Dislikes: 86
# Total Accepted:    65.1K
# Total Submissions: 124.3K
# Testcase Example:  '[[1,2], [2,3], [3,4]]'
#
# 
# You are given n pairs of numbers. In every pair, the first number is always
# smaller than the second number.
# 
# 
# 
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b
# < c. Chain of pairs can be formed in this fashion. 
# 
# 
# 
# Given a set of pairs, find the length longest chain which can be formed. You
# needn't use up all the given pairs. You can select pairs in any order.
# 
# 
# 
# Example 1:
# 
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# 
# 
# 
# Note:
# 
# The number of given pairs will be in the range [1, 1000].
# 
# 
#

# @lc code=start
class Solution:
    # greedy
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs: return 0
        cur,res = float('-inf'), 0 
        for p in sorted(pairs,key=operator.itemgetter(1)):
            if cur<p[0]:
                cur = p[1]
                res +=1

        return res
        

# @lc code=end

