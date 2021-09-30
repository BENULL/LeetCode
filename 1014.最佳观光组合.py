#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#
# https://leetcode-cn.com/problems/best-sightseeing-pair/description/
#
# algorithms
# Medium (54.79%)
# Likes:    228
# Dislikes: 0
# Total Accepted:    37.7K
# Total Submissions: 68.6K
# Testcase Example:  '[8,1,5,2,6]'
#
# 给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。
# 
# 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去
# 它们两者之间的距离。
# 
# 返回一对观光景点能取得的最高分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：values = [8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
# 
# 
# 示例 2：
# 
# 
# 输入：values = [1,2]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 2 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        greedy
        """
        # mx = values[0] + 0
        # res = 0 
        # for j in range(1, len(values)):
        #     res = max(res, mx+values[j]-j)
        #     mx = max(mx, values[j]+j)
        # return res

        """
        dp
        """
        ans = float('-inf')
        dp = [0] * len(values)
        for i in range(1, len(values)):
            dp[i] = max(dp[i - 1], values[i - 1] + i - 1)
            ans = max(ans, values[i] - i + dp[i])
        return ans

# @lc code=end

