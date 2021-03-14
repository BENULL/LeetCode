#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.79%)
# Likes:    1210
# Dislikes: 1359
# Total Accepted:    249.2K
# Total Submissions: 644.8K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Follow up: Could you write a solution that works in logarithmic time
# complexity?
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# 
# Example 2:
# 
# 
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# 
# Example 3:
# 
# 
# Input: n = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    # https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52373/Simple-CC%2B%2B-Solution-(with-detailed-explaination)
    def trailingZeroes(self, n: int) -> int:
        # return 0 if n==0 else (n/5  + self.trailingZeroes(n/5))
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
        
# @lc code=end

