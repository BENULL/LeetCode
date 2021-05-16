#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#
# https://leetcode-cn.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (63.86%)
# Likes:    156
# Dislikes: 0
# Total Accepted:    16.4K
# Total Submissions: 25.4K
# Testcase Example:  '12\n[2,7,13,19]'
#
# 编写一段程序来查找第 n 个超级丑数。
# 
# 超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
# 
# 示例:
# 
# 输入: n = 12, primes = [2,7,13,19]
# 输出: 32 
# 解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12
# 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
# 
# 说明:
# 
# 
# 1 是任何给定 primes 的超级丑数。
# 给定 primes 中的数字以升序排列。
# 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000 。
# 第 n 个超级丑数确保在 32 位有符整数范围内。
# 
# 
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # https://leetcode-cn.com/problems/super-ugly-number/solution/liang-chong-fang-fa-jie-jue-ha-xi-biao-d-1bb0/
        # https://leetcode-cn.com/problems/ugly-number-ii/solution/fu-xue-ming-zhu-gai-shui-cheng-yi-2-3-5-92zlw/
        dp = [0] * n
        pointer = [0] * len(primes)
        dp[0] = 1 
        for i in range(1,n):
            dp[i] = min(x*dp[y] for x,y in zip(primes,pointer)) 
            for j in range(len(primes)):
                if dp[i] == primes[j]*dp[pointer[j]]:
                    pointer[j] += 1
        return dp[-1]
# @lc code=end

