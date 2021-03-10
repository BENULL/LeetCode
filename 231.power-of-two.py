#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (43.66%)
# Likes:    1246
# Dislikes: 215
# Total Accepted:    402.4K
# Total Submissions: 918.4K
# Testcase Example:  '1'
#
# Given an integer n, return true if it is a power of two. Otherwise, return
# false.
# 
# An integer n is a power of two, if there exists an integer x such that n ==
# 2^x.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: true
# Explanation: 2^0 = 1
# 
# 
# Example 2:
# 
# 
# Input: n = 16
# Output: true
# Explanation: 2^4 = 16
# 
# 
# Example 3:
# 
# 
# Input: n = 3
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: n = 4
# Output: true
# 
# 
# Example 5:
# 
# 
# Input: n = 5
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= n <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0 if( n != 0) else False
        
# @lc code=end

