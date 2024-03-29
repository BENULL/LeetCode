#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] 最低票价
#
# https://leetcode-cn.com/problems/minimum-cost-for-tickets/description/
#
# algorithms
# Medium (63.41%)
# Likes:    401
# Dislikes: 0
# Total Accepted:    32.6K
# Total Submissions: 51.4K
# Testcase Example:  '[1,4,6,7,8,20]\n[2,7,15]'
#
# 在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到
# 365 的整数。
# 
# 火车票有三种不同的销售方式：
# 
# 
# 一张为期一天的通行证售价为 costs[0] 美元；
# 一张为期七天的通行证售价为 costs[1] 美元；
# 一张为期三十天的通行证售价为 costs[2] 美元。
# 
# 
# 通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第
# 5 天、第 6 天、第 7 天和第 8 天。
# 
# 返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。
# 
# 
# 
# 示例 1：
# 
# 输入：days = [1,4,6,7,8,20], costs = [2,7,15]
# 输出：11
# 解释： 
# 例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
# 在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
# 在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
# 在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
# 你总共花了 $11，并完成了你计划的每一天旅行。
# 
# 
# 示例 2：
# 
# 输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# 输出：17
# 解释：
# 例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划： 
# 在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
# 在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。 
# 你总共花了 $17，并完成了你计划的每一天旅行。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days 按顺序严格递增
# costs.length == 3
# 1 <= costs[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # recursive from bottom to up
        n = len(days)
        durations = [1,7,30]

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            ans = 10**9
            j = i
            for c, d in zip(costs, durations):
                while j < n and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)
            return ans

        return dp(0)

        # lastDay = days[-1]
        # dp = [0] * (lastDay+1)
        # j = 0
        # for i in range(1, lastDay+1):
        #     if i == days[j]:
        #         dp[i] = min((dp[i-1] if i>=1 else 0 )+costs[0],
        #                     (dp[i-7] if i>=7 else 0 )+costs[1],
        #                     (dp[i-30] if i>=30 else 0 )+costs[2])
        #         j += 1
        #     else:
        #         dp[i] = dp[i-1]

            
        # return dp[lastDay]

# @lc code=end

