#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (43.52%)
# Likes:    3072
# Dislikes: 74
# Total Accepted:    203.4K
# Total Submissions: 462.5K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# Note:
# 
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    # similar backpack
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 !=0:
            return False
        target = total//2
        dp = [0]*(target+1)
        dp[0] = True
        for num in nums:
            if target>=num:
                for i in range(target,num-1,-1):
                    dp[i]= dp[i] or dp[i-num]
        return dp[target]
        
        
        
        
# @lc code=end

