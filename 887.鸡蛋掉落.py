#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#
# https://leetcode-cn.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (29.18%)
# Likes:    684
# Dislikes: 0
# Total Accepted:    50.8K
# Total Submissions: 174K
# Testcase Example:  '1\n2'
#
# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
# 
# 已知存在楼层 f ，满足 0  ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
# 
# 每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1
# ）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
# 
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
# 
# 
# 示例 1：
# 
# 
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。 
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。 
# 如果它没碎，那么肯定能得出 f = 2 。 
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。 
# 
# 
# 示例 2：
# 
# 
# 输入：k = 2, n = 6
# 输出：3
# 
# 
# 示例 3：
# 
# 
# 输入：k = 3, n = 14
# 输出：4
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
    def superEggDrop(self, k: int, n: int) -> int:
        
        """
        dp bottom to up TLE
        """

        # dp = [[i for j in range(k+1)] for i in range(n+1)]

        # for j in range(k+1):
        #     dp[0][j] = 0

        # dp[1][0] = 0
        # for j in range(k+1):
        #     dp[1][j] = 1

        # for i in range(n+1):
        #     dp[i][0] = 0
        #     dp[i][1] = i

        # for i in range(2, n+1):
        #     # res = float('inf')
        #     for j in range(2, k+1):
        #         for l in range(1, i+1):
        #             dp[i][j] = min(dp[i][j], max(dp[l - 1][j - 1], dp[i - l][j]) + 1)

        # return dp[n][k]



        """
        dp + binary search
        """

        # TLE

        # dp = [[i for j in range(k+1)] for i in range(n+1)]

        # dp[1][0] = 0
        # for j in range(k+1):
        #     dp[0][j] = 0
        #     dp[1][j] = 1

        # for i in range(n+1):
        #     dp[i][0] = 0
        #     dp[i][1] = i

        # for i in range(2, n+1):
        #     # res = float('inf')
        #     for j in range(2, k+1):
        #         # 在区间 [1, i] 里确定一个最优值
        #         left, right = 1, i
        #         while left<right:
        #             mid = left + (right-left+1)//2
        #             breakCount = dp[mid - 1][j - 1]
        #             notBreakCount = dp[i - mid][j]
        #             if breakCount > notBreakCount:
        #                 right = mid - 1
        #             else:
        #                 left = mid
        #         dp[i][j] = max(dp[left - 1][j - 1], dp[i - left][j]) + 1


        # return dp[n][k]


        # AC

        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 x values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]
        return dp(k, n)



        """
        memo TLE up to bottom
        """
        
        # @functools.lru_cache(None)
        # def dp(K, N):
        #     if K==1: return N
        #     if N==0: return 0
            
        #     res = float('inf')
        #     for i in range(1, N+1):
        #         res = min(res,
        #         max(dp(K, N-i), dp(K-1, i-1))+1)
        #     return res
        # return dp(k,n)

# if __name__ == '__main__':
#     s = Solution()
#     s.superEggDrop(1,2)
# @lc code=end

