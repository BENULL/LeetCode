#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (52.10%)
# Likes:    1826
# Dislikes: 353
# Total Accepted:    247.2K
# Total Submissions: 473.8K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,3,2]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
#

# @lc code=start
class Solution:
    # Let the numbers be x,y,z,.....
    # require sum should be 3x+3y+3z
    # original sum = 3x+3y+z
    # Sub req sum from original sum
    # (3x+3y+3z) - (3x+3y-z) = 2z
    # div the ans by 2 = 2z/2 = z--> our ans
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums))-sum(nums)) // 2
        
# @lc code=end

