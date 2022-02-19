#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (51.22%)
# Likes:    1141
# Dislikes: 0
# Total Accepted:    211.6K
# Total Submissions: 412.8K
# Testcase Example:  '[1,5,11,5]'
#
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
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
    def canPartition(self, nums) -> bool:
        # 01 背包
        total = sum(nums)
        if total % 2 !=0:
            return False
        target = total//2
        n = len(nums)
        # dp = [[False]*(target+1) for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0] = True

        # for i in range(1, n+1):
        #     for j in range(1, target+1):
        #         if j<nums[i-1]:
        #             # 放不进背包
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
        # return dp[n][target]


        # 状态压缩 只依靠i-1, 重点在j倒序
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range(target,num-1,-1):
                if target>=i:
                    dp[i]= dp[i] or dp[i-num]
        return dp[target]
        

if __name__ == "__main__":
    s = Solution()
    s.canPartition([1,5,11,5])

# @lc code=end

