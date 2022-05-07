class Solution:
    """
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

    问总共有多少条不同的路径？

    """
    def uniquePaths(self, m: int, n: int) -> int:
        # math
        return comb(m + n - 2, n - 1)


        # dp
        # dp = [[0]*n for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if i==0 or j==0:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i][j-1] + dp[i-1][j]
        # return dp[-1][-1]
        