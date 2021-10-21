#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (56.47%)
# Likes:    558
# Dislikes: 0
# Total Accepted:    85.9K
# Total Submissions: 152.2K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 
# 
# 示例：
# 
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp 
        # dp[i][j]表示以 i，j为结束的子数组最长长度
        # m, n = len(nums1), len(nums2)
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if nums1[i-1]==nums2[j-1]: 
        #             dp[i][j] = dp[i-1][j-1] + 1
        # return max(itertools.chain.from_iterable(dp))

        m, n = len(nums1), len(nums2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]: 
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res,dp[i][j])
        return res

        


# @lc code=end

