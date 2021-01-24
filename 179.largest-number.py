#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (28.58%)
# Likes:    2725
# Dislikes: 295
# Total Accepted:    233.4K
# Total Submissions: 765.9K
# Testcase Example:  '[10,2]'
#
# Given a list of non-negative integers nums, arrange them such that they form
# the largest number.
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,2]
# Output: "210"
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Example 3:
# 
# 
# Input: nums = [1]
# Output: "1"
# 
# 
# Example 4:
# 
# 
# Input: nums = [10]
# Output: "10"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start

class LargerNum(str):
    def __lt__(x,y):
        return x+y>y+x
        
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ''.join(sorted(map(str,nums),key=LargerNum))
        return '0' if res[0]=='0' else res





        
# @lc code=end

