#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
# https://leetcode-cn.com/problems/last-stone-weight-ii/description/
#
# algorithms
# Medium (65.62%)
# Likes:    388
# Dislikes: 0
# Total Accepted:    52.2K
# Total Submissions: 79.5K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
# 
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x 。那么粉碎的可能结果如下：
# 
# 
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 
# 
# 最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：stones = [2,7,4,1,8,1]
# 输出：1
# 解释：
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
# 
# 
# 示例 2：
# 
# 
# 输入：stones = [31,26,33,21,40]
# 输出：5
# 
# 
# 示例 3：
# 
# 
# 输入：stones = [1,2]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 分成两堆 01背包问题
        total = sum(stones)
        target = total // 2
        n = len(stones)
        dp = [[0]*(target+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1, target+1):
                if j<stones[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i-1]]+stones[i-1])
        return total-2*dp[n][target]
# @lc code=end

