#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#
# https://leetcode-cn.com/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (59.94%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    15.6K
# Total Submissions: 25.9K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# 有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。
# 
# 我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。
# 
# 如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。
# 
# 请返回封闭岛屿的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
# 
# 示例 2：
# 
# 
# 
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
# 
# 
# 示例 3：
# 
# 输入：grid = [[1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# ⁠            [1,1,1,1,1,1,1]]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
# 
# 
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if i<0 or i==len(grid) or j<0 or j == len(grid[0]):
                nonlocal val
                val = 0 
                return 
            if grid[i][j] != 0: return
            grid[i][j] = 1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        res = 0
        val = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    val = 1
                    dfs(i, j)
                    res += val
        return res

                
       


        




# @lc code=end

