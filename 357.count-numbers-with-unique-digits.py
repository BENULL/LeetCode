#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (48.30%)
# Likes:    464
# Dislikes: 923
# Total Accepted:    81.8K
# Total Submissions: 168.4K
# Testcase Example:  '2'
#
# Given a non-negative integer n, count all numbers with unique digits, x,
# where 0 ≤ x < 10^n.
# 
# 
# Example:
# 
# 
# Input: 2
# Output: 91 
# Explanation: The answer should be the total numbers in the range of 0 ≤ x <
# 100, 
# excluding 11,22,33,44,55,66,77,88,99
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # combination
        # so compute solution of n=0 which is 1
        # then n=1 using: f(1) = f(0) + 9
        # then n=2 using: f(2) = f(1) + 9 * 9
        # then n=3 using: f(3) = f(3) + 9 * 9 * 8
        dp = 1
        for d in range(1,n+1):
            dp +=  9 * (functools.reduce(operator.mul,range(11-d,10),1))
        return dp
        
# @lc code=end

