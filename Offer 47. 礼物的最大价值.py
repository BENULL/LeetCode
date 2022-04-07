class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """
        在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

     

    示例 1:

    输入: 
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 12
    解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
    
        # 2d dp
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 and j==0:
        #             continue
        #         if i == 0:
        #             grid[i][j] += grid[i][j-1]
        #         elif j==0:
        #             grid[i][j] += grid[i-1][j]
        #         else:
        #             grid[i][j] += max(grid[i][j-1],grid[i-1][j])
        # return grid[-1][-1]

        # 1d dp
        m, n = len(grid), len(grid[0])
        dp = [0]*(n+1)
        for i in range(m):
            for j in range(1,n+1):
                dp[j] = max(dp[j],dp[j-1])+grid[i][j-1]
        return dp[-1]

