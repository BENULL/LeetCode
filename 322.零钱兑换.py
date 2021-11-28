#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (44.68%)
# Likes:    1586
# Dislikes: 0
# Total Accepted:    329.1K
# Total Submissions: 736.3K
# Testcase Example:  '[1,2,5]\n11'
#
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 
# 你可以认为每种硬币的数量是无限的。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1
# 
# 示例 2：
# 
# 
# 输入：coins = [2], amount = 3
# 输出：-1
# 
# 示例 3：
# 
# 
# 输入：coins = [1], amount = 0
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：coins = [1], amount = 1
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：coins = [1], amount = 2
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp bottom to up
        # dp = [0] * (amount+1)
        # for i in range(1,amount+1):
        #     res = [dp[i-c]+1 for c in coins if i>=c and dp[i-c]>=0]
        #     if res:
        #         dp[i] = min(res)
        #     else:
        #         dp[i] = -1    
        # return dp[amount]

        # dp up to bottom
        # @lru_cache(None)
        # def count(amount):

        #     if amount==0: return 0
        #     res =  [count(amount-c) for c in coins if amount>=c]
        #     res = list(map(lambda y: y+1 ,filter(lambda x: x>=0, res)))

        #     if res:
        #         return min(res)
        #     else:
        #         return -1

        # return count(amount)


        # bfs
        if amount==0: return 0
        coins.sort()
        visited = {amount}
        queue = [amount]
        step = 1
        while queue:
            for _ in range(len(queue)):
                money = queue.pop(0)
                for coin in coins:
                    next = money - coin
                    if next == 0: return step
                    if next < 0: break
                    if next not in visited:
                        queue.append(next)
                        visited.add(next)
            step += 1
        return -1 

# @lc code=end

