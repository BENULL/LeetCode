#
# @lc app=leetcode.cn id=1884 lang=python3
#
# [1884] 鸡蛋掉落-两枚鸡蛋
#
# https://leetcode-cn.com/problems/egg-drop-with-2-eggs-and-n-floors/description/
#
# algorithms
# Medium (69.90%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 4.4K
# Testcase Example:  '2'
#
# 给你 2 枚相同 的鸡蛋，和一栋从第 1 层到第 n 层共有 n 层楼的建筑。
# 
# 已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都 会碎 ，从 f 楼层或比它低 的楼层落下的鸡蛋都 不会碎 。
# 
# 每次操作，你可以取一枚 没有碎 的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <=
# n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
# 
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2
# 输出：2
# 解释：我们可以将第一枚鸡蛋从 1 楼扔下，然后将第二枚从 2 楼扔下。
# 如果第一枚鸡蛋碎了，可知 f = 0；
# 如果第二枚鸡蛋碎了，但第一枚没碎，可知 f = 1；
# 否则，当两个鸡蛋都没碎时，可知 f = 2。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 100
# 输出：14
# 解释：
# 一种最优的策略是：
# - 将第一枚鸡蛋从 9 楼扔下。如果碎了，那么 f 在 0 和 8 之间。将第二枚从 1 楼扔下，然后每扔一次上一层楼，在 8 次内找到 f 。总操作次数
# = 1 + 8 = 9 。
# - 如果第一枚鸡蛋没有碎，那么再把第一枚鸡蛋从 22 层扔下。如果碎了，那么 f 在 9 和 21 之间。将第二枚鸡蛋从 10
# 楼扔下，然后每扔一次上一层楼，在 12 次内找到 f 。总操作次数 = 2 + 12 = 14 。
# - 如果第一枚鸡蛋没有再次碎掉，则按照类似的方法从 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99 和 100
# 楼分别扔下第一枚鸡蛋。
# 不管结果如何，最多需要扔 14 次来确定 f 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def twoEggDrop(self, n: int) -> int:
        # DP
        # https://leetcode-cn.com/problems/egg-drop-with-2-eggs-and-n-floors/solution/dong-tai-gui-hua-shu-xue-tui-dao-by-tang-1zz1/
        # dp[i][j] i 表示用了i+1个鸡蛋j层建筑最少尝试
        # 这道题两个鸡蛋 i=0 i=1 
        dp = [[float('inf')]*(n+1) for _ in range(2)]
       
        # base case 
        dp[0][0] = dp[1][0] = 0
        # 一枚鸡蛋 j层最少j次
        for j in range(1,n+1):
            dp[0][j] = j

        # 两枚鸡蛋
        for j in range(1,n+1):
            for k in range(1,j+1):
                dp[1][j] = min(dp[1][j], max(dp[0][k-1]+1, dp[1][j-k]+1))
        return dp[1][n]

        # 优化到1d dp
        for j in range(1,n+1):
            for k in range(1,j+1):
                dp[j] = min(dp[j], max(k, dp[j-k]+1))



# @lc code=end

