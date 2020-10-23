#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (38.08%)
# Likes:    1556
# Dislikes: 77
# Total Accepted:    101.7K
# Total Submissions: 267.4K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
# 
# Si % Sj = 0 or Sj % Si = 0.
# 
# If there are multiple solutions, return any subset is fine.
# 
# Example 1:
# 
# 
# 
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,4,8]
# Output: [1,2,4,8]
# 
# 
# 
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        dp = [0]*len(nums)
        nums.sort()
        idx, size= 0, 0
        for i in range(len(nums)):
            k, c= -1, 0
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j] == 0 and len(dp[j])>c:
                    c = len(dp[j])
                    k = j 
            if k!=-1:
                dp[i] = dp[k]+[nums[i]]
            else:
                dp[i] = [nums[i]]

            if len(dp[i])>size:
                idx = i
                size = len(dp[i])
        return dp[idx]
# @lc code=end

