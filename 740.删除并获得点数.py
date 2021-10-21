#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#
# https://leetcode-cn.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (62.90%)
# Likes:    451
# Dislikes: 0
# Total Accepted:    52.6K
# Total Submissions: 83.6K
# Testcase Example:  '[3,4,2]'
#
# 给你一个整数数组 nums ，你可以对它进行一些操作。
# 
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i]
# + 1 的元素。
# 
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
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
    def deleteAndEarn(self, nums: List[int]) -> int:
        # dp 198 house robber
        # cnt = collections.Counter(nums)
        # nums = list(cnt.keys())
        # nums.sort()
        # n = len(nums)
        # dp = [[0]*2 for _ in range(n)]
        # dp[0][1] = nums[0]*cnt[nums[0]]
        # for i in range(1, n):
        #     if nums[i]!=nums[i-1]+1:
        #         dp[i][1] = max(dp[i-1][1], dp[i-1][0]) + nums[i]*cnt[nums[i]]
        #     else:
        #         dp[i][1] = max(dp[i-1][0]+nums[i]*cnt[nums[i]], dp[i-1][1])
        #     dp[i][0] = max(dp[i-1][0],dp[i-1][1])
        # return max(dp[n-1])

        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for val in nums:
            total[val] += val
        
        def rob(nums: List[int]) -> int:
            size = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, size):
                first, second = second, max(first + nums[i], second)
            return second
        
        return rob(total)

            
        


        

# @lc code=end

