#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# https://leetcode-cn.com/problems/burst-balloons/description/
#
# algorithms
# Hard (68.72%)
# Likes:    918
# Dislikes: 0
# Total Accepted:    66.2K
# Total Submissions: 96.2K
# Testcase Example:  '[3,1,5,8]'
#
# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i -
# 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
# 
# 求所能获得硬币的最大数量。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# 
# 示例 2：
# 
# 
# 输入：nums = [1,5]
# 输出：10
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/burst-balloons/solution/zhe-ge-cai-pu-zi-ji-zai-jia-ye-neng-zuo-guan-jian-/
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        def range_best(i, j):
            m = 0 
            for k in range(i+1, j):
                left = dp[i][k]
                right = dp[k][j]
                a = left+right+nums[i]*nums[k]*nums[j]
                m = max(m, a)
            dp[i][j] = m
        
        for window in range(2, len(nums)):
            for i in range(0, n-window):
                range_best(i, i+window)
        return dp[0][n-1]

# @lc code=end

