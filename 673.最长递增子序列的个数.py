#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.57%)
# Likes:    493
# Dislikes: 0
# Total Accepted:    48.2K
# Total Submissions: 110.7K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未排序的整数数组，找到最长递增子序列的个数。
# 
# 示例 1:
# 
# 
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 
# 
# 示例 2:
# 
# 
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 
# 
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
# 
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp
        n = len(nums)
        dp = [[1]*2 for _ in range(n)]
        ans, max_len = 0, 0
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[i][0]<dp[j][0]+1:
                        dp[i][0] = dp[j][0]+1
                        dp[i][1] = dp[j][1]
                    elif dp[i][0]==dp[j][0]+1:
                        dp[i][1] += dp[j][1]
            if dp[i][0] > max_len:
                max_len = dp[i][0]
                ans = dp[i][1]  # 重置计数
            elif dp[i][0] == max_len:
                ans += dp[i][1]
        return ans

        # maxlen = max(dp[i][0] for i in range(n))
        # return sum(dp[i][1] for i in range(n) if dp[i][0]==maxlen)

# @lc code=end

