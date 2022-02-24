#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#
# https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (20.03%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 94.4K
# Testcase Example:  '[1]\n1'
#
# 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回
# -1 。
# 
# 子数组 是数组中 连续 的一部分。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1], k = 1
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2], k = 4
# 输出：-1
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [2,-1,2], k = 3
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 1 <= k <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
# @lc code=end

