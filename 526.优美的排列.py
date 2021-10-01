#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#
# https://leetcode-cn.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (73.49%)
# Likes:    246
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 45.1K
# Testcase Example:  '2'
#
# 假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列
# ：
# 
# 
# perm[i] 能够被 i 整除
# i 能够被 perm[i] 整除
# 
# 
# 给你一个整数 n ，返回可以构造的 优美排列 的 数量 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2
# 输出：2
# 解释：
# 第 1 个优美的排列是 [1,2]：
# ⁠   - perm[1] = 1 能被 i = 1 整除
# ⁠   - perm[2] = 2 能被 i = 2 整除
# 第 2 个优美的排列是 [2,1]:
# ⁠   - perm[1] = 2 能被 i = 1 整除
# ⁠   - i = 2 能被 perm[2] = 1 整除
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 15
# 
# 
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        """
        dfs
        """
        # visited = [False]*(n+1)
        # def dfs(i):
        #     if i>n: return 1
        #     ans = 0
        #     for num in range(1,n+1):
        #         if not visited[num] and ( num % i == 0 or i % num == 0):
        #             visited[num] = True
        #             ans += dfs(i+1)
        #             visited[num] = False
        #     return ans

        # return dfs(1)

        """
        dfs + 状态压缩 （n<=15）
        """

        # def dfs(i, vis):
        #     if i>n: return 1
        #     ans = 0
        #     for num in range(1,n+1):
        #         if  ((1<<num) & vis)==0  and (num % i == 0 or i % num == 0):
        #             ans += dfs(i+1, (1 << num) | vis)
        #     return ans

        # return dfs(1,0)

        """
        dp 
        """
        mask =  1<<n
        dp = [[0] * mask for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for state in range(mask):
                for k in range(1, n+1):
                    if ((state>>(k-1))&1==1) and (k % i == 0 or i % k == 0):
                        dp[i][state] += dp[i-1][state & (~(1 << (k - 1)))]
        return dp[n][mask - 1]
                    


        
# @lc code=end

