#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (41.61%)
# Likes:    1073
# Dislikes: 189
# Total Accepted:    252.1K
# Total Submissions: 600.3K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Follow up: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # binary search  with range
        left, right = 1, num
        while left<=right:
            mid = left + (right-left)//2
            if mid**2<num:
                left = mid + 1
            elif mid**2 >num:
                right = mid -1
            else:
                return True
        return False


        
# @lc code=end

